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

## coords.json

As 32 coordenadas geocodificadas pelo Nominatim. Servem para os links "ver no
mapa" e para o JSON-LD. **Não servem para enquadrar Street View**: são
centroides de polígono, e em alguns casos caem longe da fachada — o Parque Lage
erra o palacete em cerca de 200 metros.

## Dívida conhecida

Os botões de Street View estão hoje escritos direto no HTML construído, não
nestes geradores. Um rebuild os apaga. Ao estender a função aos demais pontos,
mover para um dicionário `sv` nos módulos `g1`…`g4`.

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
