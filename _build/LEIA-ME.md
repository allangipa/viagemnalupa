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
