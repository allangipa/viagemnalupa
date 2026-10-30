# _build — geradores das páginas de destino

Esta pasta **não faz parte do site publicado**. Ela guarda o código que gera as
páginas, para que elas possam ser refeitas sem escrever HTML à mão.

## Como funciona

Cada destino tem o mesmo desenho:

- `lib.py` — funções de renderização: `ficha()` monta um ponto turístico com os
  10 campos, `mapa()` o botão "ver no mapa", `flag()` a bandeira, `ul()` as listas.
  `ROTULOS` define a ordem dos 10 campos e é a fonte única dessa ordem.
- `g1.py` … `g4.py` — os dados dos 16 pontos, quatro por arquivo, agrupados por
  região da cidade. É aqui que mora o texto de cada ficha.
- `build.py` — monta a página inteira: cabeçalho, painel de números, avisos
  transversais, as 16 fichas e o JSON-LD. As constantes do topo
  (`CSSV`, `TITULO`, `AVISOS`, `PAINEL`) são o que se mexe com mais frequência.

Para regenerar:

    python3 build.py > index.html

E copiar o resultado para `destinos/<cidade>/index.html`.

## CSSV — a armadilha

`CSSV` no topo de cada `build.py` é o parâmetro `?v=` do `assets/css/site.css`.
Ele existe para furar cache. **Toda vez que o `site.css` mudar**, recalcule:

    python3 -c "import hashlib;print(hashlib.md5(open('assets/css/site.css','rb').read()).hexdigest()[:8])"

e atualize o `CSSV` nos dois `build.py` e o `?v=` nas páginas já publicadas.
Esquecer disso faz o visitante receber o CSS antigo sem nenhum erro aparente.

O stylesheet real é `assets/css/site.css`. Não `assets/site.css`.

## streetview/

Registro do trabalho de Street View: `aprovados.json` tem a escolha final por
ponto (panorama, ângulo, data de captura, o que aparece) e a lista do que ainda
falta refazer, com o motivo. `bruto.json` é o levantamento completo dos
panoramas encontrados em volta de cada ponto. `panos.json` guarda as decisões
com o texto do porquê.

A explicação do método está no Projeto, em `claude/streetview-estado.md`.

### Onde mora o botão "Ver na rua"

O registro fica aqui, mas **quem escreve o botão é `_build/<cidade>/sv.py`**, um
por cidade. Cobertura em 1/out/2026: Rio 10 de 16, Lisboa 8 de 16, Nova York
12 de 20, Porto 9 de 16, Granada 7 de 10 — a melhor proporção até agora.

| cidade | o `sv.py` é | quem chama |
|---|---|---|
| `rio`, `lisboa` | só módulo, com `botao(pid)` | o `lib.py` da cidade, ao gerar a página |
| `nova-york`, `porto`, `granada` | módulo **e script**, com `main()` | ninguém: a página é mantida à mão, ou o gerador não sabe de Street View |

Por isso os `sv.py` de Nova York, do Porto e de Granada estão na cadeia acima, e
os do Rio e de Lisboa não. Granada é o caso novo: ela **tem** gerador
(`novos/gera.py`), mas ele não sabe de Street View — então regerar o guia apaga
os sete botões, e só o `sv.py` os repõe.
Todos são idempotentes: rodados duas vezes seguidas, a página continua com o
mesmo número de botões e **um** script — Nova York com 12, Granada com 7.

### Três fontes de panorama, não duas

Até o Porto só apareceram duas: o **carro do Google** (ID comum, entra por
`m="pano"`) e a **esfera de colaborador** (ID começando em `CAoS`, que o Embed
recusa, então entra por `m="loc"`).

Granada revelou a terceira: a **coleção interna do Google**. O panorama de dentro
dos Palacios Nazaríes tem ID de formato comum, aceita `m="pano"` e é creditado a
`© Google`, sem nome de colaborador — mas está num interior onde nenhum carro
entra. É o que salvou o ponto principal da ficha de Granada, depois de **duas**
esferas diferentes caírem fora do pátio.

Para distinguir: `CAoS…` é colaborador; o resto pode ser carro **ou** coleção
interna, e só o quadro renderizado diz qual.

**O botão sem o script não faz nada.** O `streetview.js` precisa estar na
página; Rio e Lisboa o ganham do gerador, e Nova York, Porto e Granada o ganham
do próprio `sv.py`. Os doze botões de Nova York entraram e ficaram mudos até essa
tag aparecer.

### Cinco armadilhas do Street View, todas pagas

**1. O Embed não aceita ID de esfera de colaborador.** Só o do carro do Google.
Esfera entra por coordenada, com `m="loc"`. O cabeçalho do `rio/sv.py` já dizia
isso, e mesmo assim `topofrock` e `guggenheim` foram escritos como `m="pano"`
antes de alguém reler.

**2. O metadado devolve o panorama MAIS PRÓXIMO do endereço** — e o mais
próximo de um arranha-céu é a calçada do pé dele, de onde o prédio não aparece.
Em Nova York isso derrubou oito pontos. Os casos que valem exemplo:

- `edge` caiu **dentro do shopping** de Hudson Yards, com o Shake Shack na tela
- `liberdade` caiu no Liberty State Park, **em Nova Jersey**
- `empire`, pela Quinta Avenida, caiu num **corredor de interior**

**3. Lugar elevado tem a mesma coordenada da rua embaixo**, e o Street View não
distingue altura. A High Line abria na calçada. A saída é procurar em trechos no
**meio do quarteirão**, onde não há via pública por baixo — e conferir que a
coordenada cai na esfera certa **com e sem** o parâmetro `radius`, que o Embed
não aceita.

**4. O nome resolve para UM ponto, e lugar grande não cabe num ponto.**
"Central Park" geocodifica para um lugar só, e o panorama mais próximo dali era
o do carro, de 2012 — um caminho que podia ser qualquer parque. O que resolveu
foi **consultar coordenadas de lugares específicos dentro** do parque: apareceram
cinco esferas, de 2017 a 2022, e ficou o Sheep Meadow com o skyline de Midtown
atrás. Vale igual para a High Line e para qualquer parque, orla ou bairro.

E o corolário: **onde o ponto é uma vista ou um interior, a esfera de
colaborador é a única coisa que existe** — o carro do Google não sobe em mirante
nem entra em museu. Cinco dos doze de Nova York são esfera: a rampa do
Guggenheim por dentro, o mirante do Top of the Rock, a passarela da Ponte do
Brooklyn, o gramado da High Line e o Sheep Meadow.

> **Correção de 30/set/2026.** Esta armadilha esteve escrita aqui por algumas
> horas como *"`source=outdoor` exclui as esferas de colaborador"*. É falso, e
> foi testado: em 20 pontos de Nova York e 16 do Porto, `source=outdoor` e a
> busca sem restrição devolveram **o mesmo panorama nos 36**, esferas inclusive.
> `outdoor` opõe-se a *indoor*, não a *colaborador*. A causa do Central Park
> sempre foi a resolução do nome, descrita acima.

**5. Dois pontos podem cair no MESMO panorama.** No Porto, `se-do-porto` e
`metro-do-porto` devolveram os dois a mesma estação de metrô; `ponte-dom-luis` e
`centro-historico-ribeira`, o mesmo mirante com palmeiras. Publicar assim mostra
a mesma imagem sob nomes diferentes — defeito pior que a falta do botão, porque
parece que funciona. **Antes de publicar, confira se há `v` repetido** entre as
entradas do `sv.py`.

### Acento

`titulo` e `nota` vão para a tela. Os comentários deste repositório são escritos
sem acento por convenção — **os campos que o leitor vê, não.** Doze textos de
Nova York foram publicados sem acento por essa confusão.

## coords.json

As 32 coordenadas geocodificadas pelo Nominatim. Servem para os links "ver no
mapa" e para o JSON-LD. **Não servem para enquadrar Street View**: são
centroides de polígono, e em alguns casos caem longe da fachada — o Parque Lage
erra o palacete em cerca de 200 metros.

## Dívida conhecida

Os botões de Street View estão hoje escritos direto no HTML construído, não
nestes geradores. Um rebuild os apaga. Ao estender a função aos demais pontos,
mover para um dicionário `sv` nos módulos `g1`…`g4`.

**Esse “um rebuild os apaga” não é só do Street View.** É o comportamento de
tudo que os scripts de pós-processamento escrevem dentro de uma página já
gerada — e a seção seguinte lista o que se perde e em que ordem repor.

## Regerar uma página desfaz o que veio depois dela

`novos/gera.py` escreve `destinos/<slug>/index.html` **do zero**. Os geradores de
ficha e de roteiro fazem o mesmo com as páginas deles. Tudo que outro script
acrescentou àquele arquivo depois — e são muitos — desaparece sem aviso e sem
erro.

O que se perde, e quem repõe:

| O que some | Quem repõe |
|---|---|
| índice lateral pegajoso | `layout/reorganiza.py --todos` |
| atalhos de "quanto custa" e "roteiro" | `layout/atalhos.py` |
| blocos de páginas irmãs e barra "Calcular para" | `layout/vizinhos.py` |
| **link de afiliado da Booking** | `parceiros/booking.py` |
| bloco de parceiros no guia e no roteiro | `parceiros/espalha.py` |
| botões de afiliado no índice lateral | `parceiros/aside.py` |
| JSON-LD (TouristDestination, WebPage, Offer…) | a cadeia de busca, abaixo |
| `?v=` do CSS e do JS | `cachebust/atualiza.py` |

A ordem que funciona, depois de regerar qualquer página de um destino:

```
VNL_DADOS=<slug> python _build/novos/gera.py --aplica   # so se regerou o guia
python _build/<slug>/gera_custos.py --aplica            # so se regerou a ficha
python _build/<slug>/gera_roteiro.py --aplica           # so se regerou o roteiro

python _build/layout/reorganiza.py --todos --aplica
python _build/layout/atalhos.py --aplica
python _build/layout/vizinhos.py --aplica
python _build/layout/sem_moldura.py --aplica
python _build/layout/assinatura.py --aplica             # "Apurado por …"; regerar apaga
python _build/layout/faq.py --aplica                    # perguntas no fim do guia; idem
python _build/layout/tamanhos.py --aplica               # roteiro "ou 3, 4 e 5 dias" no title e no bloco; idem
python _build/layout/capa.py --aplica                   # foto do cartao da home na primeira tela do guia; idem
python _build/recortes/gratis.py --aplica               # /gratis/, dos guias; atualiza o cartao da home
python _build/parceiros/booking.py --aplica             # ANTES do espalha
python _build/parceiros/espalha.py --aplica
python _build/parceiros/aside.py --aplica

python _build/nova-york/sv.py --aplica                  # so estes tres; ver abaixo
python _build/porto/sv.py --aplica
python _build/granada/sv.py --aplica
```

E daí em diante a cadeia de busca da seção seguinte, terminando no
`confere/tudo.py`. Rodar duas vezes não faz mal: da segunda em diante quase
tudo responde "0 escrito".

**Medido em 29/set/2026**, montando Miami e Salvador. Os dois guias foram
gerados, a cadeia inteira rodou, e depois os guias foram **regerados** para
anexar a foto de capa ao ponto correspondente. O resultado, conferido:

- o `confere/tudo.py` acusou as duas páginas `no ar sem nenhum dado estruturado`
  e `sem o bloco de parceiros`;
- o `aside.py` passou a responder `nao achei onde encaixar no aside` para as
  duas, porque o índice lateral em que ele encaixa os botões tinha sido apagado
  junto;
- só voltaram ao normal quando `reorganiza` rodou **antes** de `aside`, que é a
  ordem acima.

Nada disso deu erro. As páginas continuaram válidas e bonitas — só mais pobres.

### O link de afiliado não está em gerador nenhum

Este é o que custa dinheiro, e por isso tem subtítulo próprio.

Nenhum `gera_custos.py` escreve o link comissionado. Todos declaram a URL crua:

```python
"parceiros": [
    ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
```

Confira em `sevilha/`, `porto/`, `miami/` e `salvador/`: a nota ao lado muda de
um para o outro, mas **a URL é a mesma crua nos quatro**. Quem troca isso pelo
link da Commission Junction é **`parceiros/booking.py`, que é um script e não só
um módulo** — tem `main(aplica)` e uma âncora que casa tanto a URL crua quanto um
link CJ já posto.

Ou seja: **regerar uma ficha de custos substitui o link comissionado por um link
comum, em silêncio.** A página continua bonita, o link continua funcionando, e a
comissão deixa de existir.

O único sintoma visível é indireto: `espalha.py` passa a dizer
`SEM ficha de custos com Booking - pulado`, porque ele procura `jdoqocy` no HTML
e não acha. Se você vir essa linha, o afiliado daquela cidade caiu — rode
`booking.py --aplica` e depois `espalha.py` de novo.

### Ao acrescentar um destino, registre em cinco listas

Nenhuma delas é derivada do disco, e cada uma falha de um jeito diferente:

| Arquivo | Lista | O que acontece se esquecer |
|---|---|---|
| `schema/gera.py` | `DESTINOS` | avisa e pula: a página fica sem JSON-LD |
| `parceiros/booking.py` | `BUSCA` | `KeyError` cru, sem mensagem — `link_de()` lê `BUSCA[slug]` direto |
| `parceiros/aside.py` | `CIDADES` | `PARADO: destino em disco que nao esta na lista CIDADES` |
| `voos/atualiza.py` | `DESTINOS` (código IATA) | nada avisa: a ficha fica sem a passagem, e o `espalha.py` diz `sem link de voo - vai so com Booking` até a Action rodar |
| `calculadora/sincroniza.py` | `PROSA` | o destino entra na calculadora sem o texto de grátis/fonte/nota |

O `espalha.py` tem uma mensagem amigável para o mesmo esquecimento
(`Destino sem busca da Booking: … Acrescente em BUSCA`), mas ela só aparece pelo
caminho em que a ficha de custos **ainda não existe**. Com a ficha no disco, quem
estoura primeiro é o `booking.py`, com o `KeyError` pelado.

O `confere/tudo.py` pega as três depois do fato. Registrar antes evita a
segunda passada.

## Regerar uma ficha de custos: `regera_ficha.py`

Para mexer numa ficha que já está no ar (diária nova, nota corrigida), use:

```
python _build/regera_ficha.py <slug> <gerador.py> [args extras do gerador]

python _build/regera_ficha.py barcelona _build/barcelona/gera_custos.py
python _build/regera_ficha.py cancun    _build/novos/gera_custos.py  --so cancun
python _build/regera_ficha.py bariloche _build/novos2/gera_custos.py --so bariloche
```

Ele roda o gerador, repõe o bloco do voo, roda a cadeia inteira (a da seção
anterior e a de busca, abaixo), depois `calculadora/sincroniza.py`,
`recortes/comparar.py` e `cluster/home.py`, e termina no `confere/tudo.py`.
Grava direto e para no primeiro `rc != 0`.

### O bloco do voo não tem gerador nesta máquina

`<!-- voo:inicio --> … <!-- voo:fim -->` é escrito pela Action `voos.yml`, que
tem o token da Aviasales. O gerador da ficha não sabe o preço da passagem, e
**alguns escrevem um bloco provisório** ("Ainda não coletado… o primeiro valor
aparece aqui na próxima coleta") no lugar do que estava no ar.

O `regera_ficha.py` guarda o bloco antes e o devolve depois, **trocando o
provisório** se houver. Isso custou caro uma vez, em 29/out/2026, regerando
Barcelona: a primeira versão do script só repunha o bloco quando ele faltava.
O provisório contava como presente, e o bloco real sumiu. Junto sumiu o link
da Aviasales, que o `espalha.py` copia **da ficha** para o guia e o roteiro.
O roteiro passou de "Passagem e hospedagem" para só "Hospedagem", sem erro
nenhum. O único sinal foi um diff inesperado em `roteiro-5-dias/`.

Se regerar à mão, confira com `git diff` que o bloco do voo da ficha não
encolheu.

### `--so`: os geradores que escrevem várias fichas

`novos/gera_custos.py` escreve Cancún e Fortaleza, e `novos2/gera_custos.py`
reusa o mesmo renderizador para Bariloche e Punta Cana. Sem `--so <slug>`,
eles regeram todas as fichas de uma vez, e o `regera_ficha.py` só protege o
voo da que foi nomeada. Passe sempre o `--so`.

### `--refaz`: a calculadora de uma cidade que já está nela

`calculadora/sincroniza.py` sem argumento só **acrescenta** cidades que faltam.
Com `--refaz <slug>`, remonta o botão e o bloco inteiros daquela cidade a partir
da ficha e do `PROSA`. Use depois de mudar qualquer valor ou texto da ficha.
O `regera_ficha.py` já faz isso.

### O preço do JSON-LD não acompanha uma diária nova

`schema/ofertas.py` **nunca reescreve um `offers` que já existe** (ver "O preco
do JSON-LD sai do HTML publicado", abaixo). Ao mudar uma diária que aparece no
guia, troque à mão o `"price"` do Offer daquele ponto. Exemplo: o
`#hospedagem` de Barcelona passou de `"178.75"` para `"179.45"` em 29/out/2026.
Senão a página mostra um preço e o dado estruturado, outro.

### O guia de algumas cidades não tem gerador no repositório

O parágrafo de câmbio do guia de Cancún ("Preço em moeda estrangeira não foi
convertido…") não aparece em nenhum arquivo de `_build/`: só existe no HTML
publicado, e a correção de 29/out/2026 foi feita direto nele. Antes de corrigir
um guia, procure a frase em `_build/`. Se não aparecer, edite o
`destinos/<slug>/index.html`. Se aparecer no `dados.py`, mude nos dois.
Regerar o guia inteiro só para trocar uma frase desfaz a cadeia toda.

**A ficha de Buenos Aires também não tem gerador** (nasceu escrita à mão, em
9/set/2026), e o bloco dela na calculadora é anterior ao `sincroniza.py`: não
está no `PROSA`, e `--refaz buenos-aires` estoura com `KeyError`. Mudou a ficha,
mude o bloco `data-cidade="buenos-aires"` de `calculadora/index.html` com o
mesmo texto, inclusive o `value` do campo de pessoas e o botão "US$ … por
pessoa". Para rodar só a cadeia, use `regera_ficha.py buenos-aires /dev/null`.
O passo da calculadora falha no fim, e os anteriores já rodaram.

### Fontes guardadas como prova

Quando o número vem de uma API ou de um arquivo que pode mudar, a resposta fica
em `_build/<slug>/fontes/` (ou `_build/recortes/fontes/`), com a data no nome
ou no comentário do gerador:

- `madri/fontes/` e `barcelona/fontes/`: série do INE (tabela 46298) em JSON.
  O INE revisa meses já publicados: Barcelona, set/2025, passou de 198,64 para
  196,10. Por isso a janela de 12 meses e a data da leitura ficam escritas.
- `recortes/fontes/bcb-fechamento-20261023.csv`: boletim de fechamento do BCB,
  taxa de venda. É dele que saem o `/comparar/` e as ordens de grandeza de
  Bariloche (ARS) e Cancún (MXN). **A PTAX cobre só dez moedas**, e os pesos
  argentino e mexicano não estão entre elas. O BCB publica os dois no boletim
  de fechamento. Não confunda os dois: o site já disse "o Banco Central só
  publica dez moedas", e estava errado.
- `rio/fontes/`, `miami/fontes/`, `paris/fontes/`, `novos/fohb-…`: tabelas de
  táxi e diárias (FOHB, GMCVB, In Extenso).

### O que o `confere/tudo.py` passou a pegar em outubro de 2026

- **`confere_calculadora_x_ficha`**: o total de cada cidade na calculadora
  bate com o da ficha. Nasceu do Porto, que entrou sem a taxa turística
  (€ 113,25 contra € 125,25). Também acusa a nota "Esta ficha não tem
  hospedagem" numa cidade que já tem diária.
- **`confere_fila`**: a fila da home ("Os próximos da fila") não pode
  anunciar destino que já está publicado.
- **"N destinos"**: o número tem de ser o total do site (25 desde Bonito, 29/out/2026). Para subconjunto,
  escreva "cidades" ("17 cidades com diária"). O título da calculadora diz
  "N cidades".

## Páginas de cluster: `cluster/`, `rio/paginas.py`, `lisboa/paginas.py`

Páginas de uma pergunta só, penduradas no guia: Cristo Redentor, Pão de
Açúcar, o que fecha cada dia, descontos, quando ir, aeroporto, onde ficar,
Palácio da Pena, Lisboa Card.

- **`cluster/comum.py`** tem a mecânica: ler e escrever, a trava de números,
  o FAQ, as migalhas, o "Continue", o bloco da Booking e a foto de capa. Nada
  ali sabe de cidade.
- **`<cidade>/paginas.py`** tem os dados e o texto. Duas travas param o script
  com `PARADO`:
  - `confere_numeros`: todo número escrito à mão tem de aparecer no texto da
    fonte;
  - as "provas": frases que têm de existir na ficha da qual a página empresta
    o dado.
- **`cluster/home.py`** monta o bloco "As respostas mais procuradas" na home,
  entre `<!-- cluster:inicio -->` e `<!-- cluster:fim -->`. A lista sai do
  disco: cidade nova com cluster entra sozinha.

O link "Página completa" no guia vai num `<p class="ponto-mais">` antes de
`<div class="campos">`, e **não** num `foto-nota`, que o `sem_moldura.py`
apaga. O `liga_no_ponto` confere por regex se o link já está lá. A versão
antiga conferia por texto, o atributo `style` quebrava a comparação, e cada
rodada punha mais um link (Lisboa chegou a ter três).

Regerar uma página de cluster tem o mesmo problema das outras: rode a cadeia
depois. **`layout/faq.py` sozinho tira o FAQPage do JSON-LD**, e quem o devolve
é o `schema/gera.py`.

## Busca: a cadeia de pos-processamento

Rode nesta ordem. Cada um so acrescenta o que falta, entao rodar duas vezes
nao faz mal — mas rodar **fora de ordem** faz: o `schema/editor.py` le a data
do `sitemap.xml`, e um sitemap velho propaga o atraso em vez de corrigi-lo.

```
python _build/sitemap/atualiza.py --aplica    # a data, do ultimo commit
python _build/schema/gera.py --aplica         # os blocos que faltam
python _build/schema/editor.py --aplica       # Organization, publisher, dateModified
python _build/schema/ofertas.py --aplica      # o preco de cada ponto, como Offer
python _build/imagens/srcset.py --aplica      # as fotos menores e o srcset
python _build/layout/fontes.py --aplica       # CSS do Google Fonts sem bloquear a pintura
python _build/adsense/instala.py --aplica     # meta e preconnect do AdSense no <head>
python _build/drive/instala.py --aplica       # Travelpayouts Drive no <head>, em TODAS
python _build/confere/tudo.py                 # confere o artefato
```

Os dois instaladores de `<head>` entraram na corrente em 18/10/2026: o Drive
tinha ficado em 32 de 68 paginas, porque foi instalado uma vez (16/9) e as dez
cidades seguintes nasceram sem ele. O Allan pediu que fosse padrao - toda
pagina nova passa por aqui antes do `confere`.

### `<lastmod>` vazio — o bug que travou 14 URLs

`data_do_commit()` devolve `None` para arquivo ainda nao commitado, e a pagina
entra no mapa no **mesmo lote em que e criada** — ou seja, sempre antes do
commit. A linha `d = data_do_commit(p) or ""` gravava `<lastmod></lastmod>`,
que o protocolo de sitemap nao aceita.

E nao se curava sozinho: o regex de conserto pedia `[^<]+`, e tag vazia nao
casa com "um ou mais". Ficou preso desde que Cancun e Fortaleza entraram, em
14 das 45 URLs — Cancun, Fortaleza, Bariloche, Punta Cana, Porto e Sevilha.
Treze delas estavam como "Detectada, mas nao indexada" no Search Console.

Corrigido nos dois pontos: `[^<]*` no regex, e **tag ausente** em vez de tag
vazia quando nao ha data. Ausente e valido; vazia nao.

### O que esses scripts se recusam a escrever

A regra editorial vale para o dado estruturado igual vale para a prosa.

- **Preco em faixa, piso ou divergencia fica sem `offers`.** "US$ 24-36",
  "A partir de R$ 250", "Fontes divergem" e "—" nao viram numero. Sao 20 dos
  154 pontos, e cada recusa sai nomeada no relatorio do `ofertas.py`.
- **Horario nao entra.** `openingHoursSpecification` pede dia e hora de abrir
  e fechar; o site guarda prosa em rotulos que variam, e muitas vezes so o dia
  de folga. Estruturar isso seria inventar a parte que falta.
- **`dateModified` nunca entra no `TouristDestination`.** Ele herda de `Place`,
  nao de `CreativeWork`. Vai num `WebPage` proprio.
- **Nada de `aggregateRating`.** O site nao tem avaliacao de ninguem.

### O preco do JSON-LD sai do HTML publicado

O `ofertas.py` le o `<span class="preco-val">` da propria pagina, nao uma
tabela a parte. Os dois nao podem divergir porque sao o mesmo texto. A moeda
do ponto **gratis** vem apurada dos outros pontos da mesma ficha — senao o
Mosteiro dos Jeronimos sairia com preco em real.

## Identidade: marca, favicon, og:image

Fora da corrente - os arquivos trocam de conteudo, nao de nome.

    python _build/identidade/kit.py --aplica   # avatar, favicons, marca-1024 -> assets/img
    chrome --headless --window-size=1200,630 --screenshot=og-image.png og.html   # o OG, com texto

A fonte e `_build/identidade/candidatas/c2.png` (emblema de 18/10/2026; o
`kit.py` conta a origem). O icone de 30 px do cabecalho tambem sai do kit
(PNG com alfa, `marca-cabecalho-64.png`); `identidade/aplica.py --aplica` o
poe no lugar do SVG antigo e completa favicon e og:image onde faltarem.

## Desempenho: o que foi medido e o que mudou

Medido pelo Allan no PageSpeed (Moto G Power emulado, 4G lento, CPU 4x), home,
celular. Antes de mexer em desempenho de novo, medir de novo.

| quando | nota | FCP | LCP | bloqueio | Speed Index | o que havia |
|---|---|---|---|---|---|---|
| 18/10/2026 10:11 | 63 | 4,9 s | 8,1 s | 50 ms | 4,9 s | linha de base |
| 18/10/2026 10:22 | 61 | 5,1 s | 8,5 s | 60 ms | 6,2 s | mesma coisa, segunda rodada |
| 18/10/2026 10:32 | **80** | **3,1 s** | **3,7 s** | **0 ms** | 4,9 s | AdSense no gesto ou 4 s apos o load; CSS do Google Fonts sem bloquear (`d5e8ab7`) |
| 18/10/2026 10:39 | **93** | **2,5 s** | **2,7 s** | **0 ms** | **2,5 s** | Travelpayouts Drive no mesmo gatilho (`d894504`) |

O peso nunca foi o problema (HTML 13 KB, CSS 14 KB comprimidos, TTFB 0,11 s,
brotli). Era a espera: o CSS das fontes bloqueava a pintura e o adsbygoogle.js
(55 KB + 165 KB + tres iframes) disputava a banda com a foto do hero. No
computador a nota era 81 com 390 ms de bloqueio, todo do AdSense.

De 61 a 93 sem tirar um byte da pagina: tudo o que era de terceiro e nao
precisava estar na primeira pintura (AdSense, Drive, o CSS das fontes) saiu
dela. O que ainda pesa, por ordem: o `site.css` (bloqueante, 14 KB, mesma
origem), as fontes (~160 KB, Fraunces variavel e a maior) e a foto do hero
(70 KB a 820). Os cortes que sobram sao caros de manter para ganho pequeno
(CSS critico inline, fonte com menos eixos); parar aqui foi a decisao de
18/10. Ao instalar qualquer script novo, entrar pelo mesmo gatilho de gesto.

Observacao: a CDN da Hostinger (`hcdn`) responde 403 com "Checking your
browser" a cliente que manda UA de navegador sem os outros cabecalhos
(Accept, Accept-Language, Sec-Fetch-*). Navegador de verdade e o Lighthouse
passam; `curl -A` sozinho nao. Para conferir o site no ar com curl, mandar os
cabecalhos completos ou nenhum UA.
