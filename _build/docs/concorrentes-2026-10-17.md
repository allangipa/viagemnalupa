# Quem ranqueia nas nossas buscas, e o que copiar — 17/10/2026

Pergunta do Allan: "olhe sites do mesmo nicho que tenham mais visitas e veja o
que podemos implantar", aos moldes do `docs/concorrentes-2026-10-17.md` do Guia
Produto na Lupa. Mesmo método: três buscas em português, **uma por tipo de
página que temos** (ficha de custos, guia, roteiro), leitura da **estrutura** de
sete páginas que ranqueiam (não do conteúdo), cruzada com as regras da casa.

Mora em `_build/docs/` e não em `docs/` porque a raiz deste repositório é o
`public_html`: `docs/` seria servida; `_build/` devolve 403.

## Quem aparece na primeira página

| Busca | Quem ranqueia |
|---|---|
| quanto custa viajar para Lisboa | Dica de Portugal, Grupo Dicas, MyRoteiro, Revista Fórum (2), Visit Lisboa Blog, Decolar |
| o que fazer em Lisboa, pontos turísticos | Dica de Portugal (2), Viagens e Caminhos, Fui Ser Viajante, Viciada em Viajar, Eurodicas, Allianz, Crônicas do Agora, Dicas da Europa |
| roteiro Lisboa 5 dias | Dica de Portugal (2), Grupo Dicas (2), Viagens e Caminhos, Nomad, Ideias na Mala, Turismocity |

**Dica de Portugal e Grupo Dicas são a mesma operação** — o mesmo autor,
Gabriel Lorenzi, assina nos dois domínios. Uma pessoa ocupa 9 dos ~27 resultados
das três buscas, com o mesmo molde de página repetido. É o concorrente a olhar.

Páginas lidas: Dica de Portugal `/lisboa/quanto-custa-viajar-para-lisboa/`,
`/pontos-turisticos/pontos-turisticos-em-lisboa-portugal/` e
`/lisboa/roteiro-completo-de-5-dias-em-lisboa/`; Grupo Dicas
`/quanto-custa-viajar-para-lisboa-preco-de-tudo/`; Viagens e Caminhos
`/lisboa-portugal/` (56 pontos) e `/roteiro-lisboa/`; Fui Ser Viajante
redirecionou para a home (lida como home, serve pouco).

## O que nós temos, medido antes de olhar os outros

Inventário de 67 páginas, 38 KB de média. Das doze coisas comuns no nicho,
**temos duas**: busca interna (na home) e breadcrumb (no guia). Não temos autor
(0 de 67; a página Sobre não cita pessoa), compartilhar, FAQ (o `<summary>` que
parecia FAQ é a caixa "o que já está apurado"; nenhum guia tem pergunta como
título), data de atualização visível no topo, relacionados, newsletter nem
comentários. O que temos de sobra é dado estruturado: 220 `TouristAttraction`,
191 `Offer`, 20 `TouristTrip`.

## O que todos fazem e nós não — a ordem combinada

1. **Autor com nome, página e bio.** As seis matérias lidas têm — Gabriel
   Lorenzi, Bruna Soares, Jair Prandi —, com link para página do autor e bloco
   de bio no fim. Nós: **zero em 67**. A proposição do site inteiro é "nós
   conferimos", e ninguém está nomeado. É o buraco mais barato de fechar e o
   maior em E-E-A-T: `Person` no JSON-LD, linha "Apurado por …" no guia, na
   ficha e no roteiro, e um bloco de quem escreve na página Sobre.
2. **Várias páginas por destino, não três.** O Dica de Portugal tem ~12 por
   cidade — quanto custa, pontos turísticos (duas versões), roteiro (duas),
   onde ficar, documentos, tax free, compras, vida noturna, ingressos, trem,
   seguro, chip. Nós, três. Mesmo achado nº 1 do Guia Produto, e a mesma
   saída: **recortes derivados do que já está apurado**, sem apuração nova —
   "o que não cobra em Lisboa" (81 pontos grátis no site), "o que fecha na
   segunda-feira", "o que não cobra de menor de 12". Tudo sai do `dados.py`.
   Nada de página com número que não temos.
3. **Perguntas como títulos no fim de cada página.** Dica de Portugal faz nos
   três tipos, quatro H3 por página. Entra no "As pessoas também perguntam".
   Nós: zero. As nossas ressalvas **já são respostas** — "compensa o Lisboa
   Card?", "tem dia grátis?", "fecha na segunda?" — só não estão em forma de
   pergunta. Bloco gerado do `dados.py`, com `FAQPage` no JSON-LD, que hoje
   não existe em nenhuma página. Mesmo achado nº 2 do Guia Produto.
4. **Compartilhar no WhatsApp.** As seis matérias têm, no topo e no fim, com o
   WhatsApp em primeiro e destacado. Nós, nada. No Brasil é assim que o plano
   de viagem chega a quem viaja junto. Uma linha de botões; custo quase zero.
5. **Um roteiro que atende vários tamanhos.** Viagens e Caminhos responde
   "roteiro Lisboa 2, 3, 4, 5 dias" numa URL só. O nosso é um tamanho fixo
   (`roteiro-6-dias`): a busca "roteiro Lisboa 3 dias" não nos encontra. O
   conteúdo já é dia a dia; falta o título e a abertura dizerem o corte
   ("com três dias, faça os dias 1, 2 e 4") e a URL não travar o número.
6. **Foto na primeira tela.** Deles: autor, compartilhar e foto grande acima
   da dobra. Nossa: só texto até passar o cartão "4 de 16". Ver visual 2.

## O que eles fazem e não copiamos

Preço sem fonte nem data — Viagens e Caminhos ainda publica "(preços de 2020)"
no meio do texto. CTA de afiliado sem aviso: "ECONOMIZE ATÉ 42%", "HOTEL BEM
BARATO" em caixa-alta, "site que a gente usa"; nosso "Estes links dão comissão
ao site" fica. Cards de hotel **no meio** da lista de pontos (Dica de Portugal,
entre o 3º e o 4º): quebra a leitura; nosso bloco de parceiros segue no fim.
Prosa sem campo fixo por ponto — o nosso formato é melhor. Seções genéricas
"Dicas insider" e "Cuidados e armadilhas". Alt de imagem com placeholder.
Comentários (só Viagens e Caminhos tem; não é o que ranqueia).

## Onde já estamos à frente

Fonte e data em todo número; nenhum dos sete tem, e um tem preço de 2020.
Campos fixos por ponto — preço, horário, endereço, mapa — que nenhum tem.
Calculadora; nenhum tem (Grupo Dicas: tabela estática de três perfis).
Street View em quatro cidades. Aviso de afiliado. Lacuna declarada. JSON-LD
de ponto e de oferta, onde eles têm `Article`. 38 KB por página contra páginas
de blog WordPress com barra lateral.

## Visual — lido em duas telas no celular (nosso guia de Lisboa × o deles)

1. **Faixa de cookies cobre um quinto da tela** e esconde o segundo cartão.
   Idêntico ao visual 1 do Guia Produto; mesma correção: uma linha, compacta.
2. **Primeira tela só de texto**: logo, nav, breadcrumb, eyebrow, H1, abertura
   de cinco linhas, cartão "4 de 16". A foto do Jerónimos vem depois. A deles
   põe a foto da Praça do Comércio acima da dobra. Mesmo visual 3 do Guia
   Produto: a primeira tela entrega menos do que a página tem.
3. **Cabeçalho de ~160 px no celular**, com a nav em linha. O deles: hambúrguer
   e busca em ~60 px. Sobra uma tela inteira a cada rolagem.
4. **Sem autor nem compartilhar na primeira tela** — são os itens 1 e 4 acima,
   vistos na tela.

## Ordem proposta, e o que já foi feito (17/10/2026)

SEO 1 (autor) → 4 (WhatsApp) → 3 (FAQ) → 2 (recortes) → 5 (roteiro por tamanho);
visual 1, 3 e 2 na sequência. Nada disso pede apuração nova: tudo sai do que já
está em `dados.py` ou no HTML publicado.

| item | estado | onde |
|---|---|---|
| SEO 1 · autor | **feito** — "Apurado por Allan Vitor · @viagemnalupabr" em 60 páginas; `author: Person` em 66 | `layout/assinatura.py`, `schema/editor.py`, commit `3221188` |
| SEO 4 · compartilhar | **feito com troca**: o Allan quis o Instagram, não o WhatsApp — a conta nasceu em outubro e o site é o único ativo que manda gente para lá | idem |
| SEO 3 · FAQ | **feito** — 4 perguntas em `<h3>` nos 20 guias, `FAQPage` nos 20; respostas derivadas dos pontos e da ficha, nunca escritas à mão | `layout/faq.py`, commit `99c314d` |
| SEO 2 · recortes | **feito como UMA página**, `/gratis/` (81 pontos, 20 cidades, 102 links para os guias), e não vinte por cidade: 7 cidades têm só 1–2 pontos grátis | `recortes/gratis.py`, commits `650eea9` e `6af64b6` |
| SEO 5 · roteiro por tamanho | **feito pelo caminho barato** — `<title>` ganha "(ou 3, 4 e 5)" e um bloco "Com menos dias" abre o conteúdo com H2 "Roteiro de Lisboa em 3, 4 ou 5 dias" e a lista dos dias; a URL não muda, o H1 não muda. Qual dia cortar não está em `dados.py`, então o bloco só diz o que é verdade nos 20: corte dias inteiros | `layout/tamanhos.py` |
| visual 1 · cookies | **feito** — de ~22% para 11% da tela no celular | `consentimento.js`, commit `99c314d` |
| visual 3 · cabeçalho | **feito** — no celular o nome sai de vista (fica para leitor de tela) e a nav cabe na linha do ícone: de 139 px para 71. O YouTube já tinha saído da nav | CSS `@media (max-width:44rem)` em `site.css`; `layout/sem_youtube.py` |
| visual 2 · foto na primeira tela | **feito nos 20** — a capa do cartão da home (com o `srcset` e o crédito) entra como faixa 16:9 abaixo da assinatura; em Lisboa a primeira foto passou de 4.761 px para 489 px do topo no celular. Cinco capas (Bariloche, Cancún, Fortaleza, Punta Cana, Sevilha) só existem na home e tiveram o crédito recuperado dos geradores de cartão e do commit `908b4b6` | `layout/capa.py` (aceita um slug; tabela `RESERVA` com os cinco créditos) |

### Identidade visual e a logo do Instagram — feito em 18/10/2026

Retomado no mesmo dia, depois de o Allan ver as quatro candidatas que a
sessão do Guia Produto na Lupa gerou para aquele site. Quatro candidatas
GPT Image 2.5 (6 créditos, 1,5 cada — menos que o medido abaixo), escolhida
a 2 pela leitura a 110 px; kit em `_build/identidade/kit.py`, OG pelo
`og.html` no Chrome headless. Os cinco PNGs do site trocaram de conteúdo com
os mesmos nomes. O registro da apuração anterior fica abaixo como estava.

Pedido do Allan: uma logo "de alta resolução, como o Vestígio Oculto e o Xadrez
Bélico", principalmente para o avatar do @viagemnalupabr. Apurado antes de adiar:

- **Vestígio Oculto** (`GitHub/Vestigio-Oculto/_src/marca/`): silhueta chapada em
  duas cores (chapéu creme, óculos dourados), SVG de paths puros, sem texto,
  exportado 512×512 sobre fundo escuro com vinheta. **Xadrez Bélico**
  (xadrezbelico.com, `assets/marca/cavalo-*.png`): emblema renderizado, escudo
  metálico com o cavalo de elmo, bronze sobre preto, nome dentro. O que os dois
  têm e a nossa não: um distintivo quadrado com presença em qualquer tamanho.
- **A nossa hoje**: o ícone de traços finos do cabeçalho (que o
  `Instagram/_ferramentas/perfil/gerar_foto_perfil.py` redesenha em PIL e vira
  mancha a 110 px) e o `assets/img/marca-1024.png`, render sombreado do Higgsfield
  que a 110 px vira borrão. `_build/identidade/aplica.py` documenta a origem.
- **Plano**: gerar candidatas nos dois registros e escolher como nas fotos.
  Recraft V4.1 `--model_type vector` com `--colors` na paleta do site e
  `--background_color #0B1622` (registro Vestígio); GPT Image 2.5 `--quality high
  --resolution 2k --background opaque` com o `marca-1024` em `--image` como
  continuidade (registro Xadrez). Custos medidos com os parâmetros reais:
  Recraft 2,5 cr a 1k e **10 cr a 2k**; GPT Image **2,75 cr**. Explorar a 1k,
  finalizar a 2k: ~23 créditos de 236,59 (plano ultra, CLI logada).
- **Depois da escolha, sem gasto**: kit em `_build/identidade/` — avatar 1080
  sobre fundo escuro com vinheta, favicon 32/512, apple-touch 180, OG 1200×630 e
  as pré-visualizações do app. Não há rasterizador de SVG na máquina (cairosvg,
  resvg, inkscape, magick: nenhum); o kit é PIL.

Achado de passagem: o cartão da calculadora na home dizia "Nova York, Santiago,
Buenos Aires e Maceió… Rio e Lisboa entram em seguida" com a calculadora já em
19 cidades. É o "herói velho" do Guia Produto, versão nossa. Corrigido em `650eea9`.
