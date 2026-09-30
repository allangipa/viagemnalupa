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
por cidade. Cobertura em 30/set/2026: Rio 10 de 16, Lisboa 8 de 16, Nova York
12 de 20, Porto 9 de 16.

| cidade | o `sv.py` é | quem chama |
|---|---|---|
| `rio`, `lisboa` | só módulo, com `botao(pid)` | o `lib.py` da cidade, ao gerar a página |
| `nova-york`, `porto` | módulo **e script**, com `main()` | ninguém: a página é mantida à mão |

Por isso os `sv.py` de Nova York e do Porto estão na cadeia acima, e os do Rio e
de Lisboa não.
Ele é idempotente: rodado duas vezes seguidas, a página continua com 12 botões
e 1 script.

**O botão sem o script não faz nada.** O `streetview.js` precisa estar na
página; Rio e Lisboa o ganham do gerador, Nova York o ganha do próprio `sv.py`.
Os doze botões de Nova York entraram e ficaram mudos até essa tag aparecer.

### Quatro armadilhas do Street View, todas pagas

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
python _build/parceiros/booking.py --aplica             # ANTES do espalha
python _build/parceiros/espalha.py --aplica
python _build/parceiros/aside.py --aplica

python _build/nova-york/sv.py --aplica                  # so estes dois; ver abaixo
python _build/porto/sv.py --aplica
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

### Ao acrescentar um destino, registre em três listas

Nenhuma delas é derivada do disco, e cada uma falha de um jeito diferente:

| Arquivo | Lista | O que acontece se esquecer |
|---|---|---|
| `schema/gera.py` | `DESTINOS` | avisa e pula: a página fica sem JSON-LD |
| `parceiros/booking.py` | `BUSCA` | `KeyError` cru, sem mensagem — `link_de()` lê `BUSCA[slug]` direto |
| `parceiros/aside.py` | `CIDADES` | `PARADO: destino em disco que nao esta na lista CIDADES` |

O `espalha.py` tem uma mensagem amigável para o mesmo esquecimento
(`Destino sem busca da Booking: … Acrescente em BUSCA`), mas ela só aparece pelo
caminho em que a ficha de custos **ainda não existe**. Com a ficha no disco, quem
estoura primeiro é o `booking.py`, com o `KeyError` pelado.

O `confere/tudo.py` pega as três depois do fato. Registrar antes evita a
segunda passada.

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
python _build/confere/tudo.py                 # confere o artefato
```

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
