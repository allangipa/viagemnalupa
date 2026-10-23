# Cluster do Rio de Janeiro: plano de páginas — 23/10/2026

Continuação do item SEO 2 de `concorrentes-2026-10-17.md` ("várias páginas por destino, não
três"). Lá a saída foi uma página só, `/gratis/`. Aqui o Rio vira o primeiro destino com
cluster: as três páginas de hoje viram o centro, e em volta entram páginas de **uma
pergunta só**. É o molde do Dica de Portugal (cerca de 12 páginas por cidade), com a regra
da casa: **nenhuma página com número que não temos**.

Por que o Rio: tem ficha por ponto em `_build/rio/g1.py`…`g4.py` (a mais completa do site),
três obras ou restrições em vigor, que envelhecem os guias concorrentes, e o carrossel e o
Reel do Cristo já levam gente do Instagram para lá.

## O que já existe (o centro do cluster)

| página | responde a |
|---|---|
| `/destinos/rio-de-janeiro/` | o que ver, quanto custa cada ponto, o que fecha, FAQ com 4 perguntas |
| `/destinos/rio-de-janeiro/quanto-custa/` | quanto custam 6 dias (R$ 3.696 por pessoa), diária, quando ir |
| `/destinos/rio-de-janeiro/roteiro-6-dias/` | roteiro de 3 a 6 dias, por região |
| `/gratis/` (seção Rio) | os 8 pontos sem entrada |

## Fase A: páginas derivadas, sem apuração nova

Tudo sai do que já está em `g1.py`…`g4.py`, no `AVISOS` do `build.py` e na ficha de custos.
Gerador novo: `_build/rio/paginas.py`, que **importa** os `g*.py`, para o número da página
nova nunca divergir do guia.

### 1. Cristo Redentor: ingresso, preço e como subir

`/destinos/rio-de-janeiro/cristo-redentor/`

- **Busca:** "ingresso cristo redentor", "preço cristo redentor", "como subir o cristo".
- **Conteúdo** (tudo em `g1.py`, apurado em 13/set/2026):
  - as cinco formas de subir, com preço: van das Paineiras R$ 87, van de Copacabana ou do
    Largo do Machado R$ 132, trem R$ 134, trilha R$ 60, com guia R$ 185;
  - meia, criança e idoso de cada uma;
  - "não existe tarifa de morador";
  - a obra das escadas rolantes até maio de 2027: 50% dos ingressos e 80 degraus;
  - metrô de cada embarque;
  - o melhor mês pelo clima (julho e agosto são os mais secos).
- **Schema:** `TouristAttraction` com um `Offer` por forma de subir, mais `FAQPage` ("qual
  é o jeito mais barato?", "tem desconto para morador?", "até quando vai a obra?") e
  `BreadcrumbList`.
- **Primeira da fila:** é a busca de maior volume do Rio, e a obra torna a informação
  diferente da de qualquer guia de 2025.

### 2. O que abre e o que fecha em cada dia da semana

`/destinos/rio-de-janeiro/o-que-fecha-cada-dia/`

- **Busca:** "o que fazer no rio na segunda-feira", "museus abertos segunda rio".
- **Conteúdo:** uma tabela dia × ponto, tirada dos horários das 16 fichas e do aviso "O
  calendário do Centro". Conclusão que a página já tem: quinta e sexta são os únicos dias
  com tudo do Centro aberto; quarta fecha Museu do Amanhã e MAR; segunda fecha o Forte de
  Copacabana e o Parque das Ruínas.
- **Modelo para as outras cidades:** é o recorte "o que fecha na segunda-feira" do
  documento de concorrentes, e a mesma tabela sai para os 20 destinos.

### 3. Pão de Açúcar: ingresso e desconto

`/destinos/rio-de-janeiro/pao-de-acucar/`

- **Busca:** "ingresso pão de açúcar preço", "pão de açúcar desconto morador".
- **Conteúdo:** R$ 205 a inteira, R$ 160 para brasileiro, R$ 89 para quem mora no Estado do
  Rio; o documento que é pedido e o que acontece sem ele; horário, metrô, clima. A fonte é o
  SAC oficial do Parque Bondinho, em 13/set/2026.
- **Conferir antes:** a ficha do Pão de Açúcar precisa ter horário e metrô completos, como
  a do Cristo. O que faltar fica como lacuna escrita, sem número inventado.

### 4. Onde morador e brasileiro pagam menos

`/destinos/rio-de-janeiro/descontos/`

- **Busca:** "rio de janeiro meia entrada turista", "desconto morador rio pontos
  turísticos".
- **Conteúdo** (do aviso "Onde ser brasileiro, ou morar no Rio, corta o preço pela metade"
  mais as fichas):
  - Pão de Açúcar R$ 89, R$ 160 ou R$ 205;
  - Jardim Botânico R$ 40 ou R$ 80;
  - MAR: meia para carioca e terça grátis;
  - Museu do Amanhã: R$ 10 todo dia 10;
  - Theatro: meia solidária;
  - Cristo: sem tarifa de morador, mas R$ 45 de diferença pelo embarque.

### 5. Quando ir ao Rio

`/destinos/rio-de-janeiro/quando-ir/`

- **Busca:** "melhor época para ir ao rio de janeiro", "rio de janeiro em julho".
- **Conteúdo:**
  - diária média por mês (FOHB, de R$ 534 em junho a R$ 750 em março);
  - Carnaval: R$ 1.312 no mês e R$ 2.657 na noite de pico;
  - Réveillon: ocupação de 90,58%, e a diária da noite fica como lacuna;
  - clima mês a mês (Climatempo, 30 anos);
  - férias escolares.
- **Conferir antes:** a página só sai se a série completa dos 12 meses de diária e de clima
  estiver nas fontes já citadas. Hoje o site mostra os extremos (junho e março) e o clima
  de julho e agosto. Se os 12 meses não estiverem anotados, é a única página da fase A que
  pede uma volta à fonte (a mesma fonte, sem fonte nova).

## Fase B: pede apuração nova (não criar sem ela)

| página | busca | por que não sai agora |
|---|---|---|
| Aeroporto–Zona Sul e Centro (Galeão e Santos Dumont) | "como ir do galeão para copacabana" | a ficha diz "traslado do aeroporto não incluído": não temos tarifa de BRT, VLT, ônibus, táxi nem app. É a busca de maior volume fora dos pontos; vale apurar primeiro |
| Onde ficar no Rio, por bairro | "onde ficar no rio de janeiro" | a diária por bairro está "não encontrada" (FOHB e Riotur não desagregam). Sem número, a página vira a prosa genérica que não fazemos. Só com uma amostra rotulada como amostra, ou não fazer |
| Bate-voltas (Petrópolis, Arraial, Búzios) | "bate e volta rio" | fora dos 16 pontos; seria destino novo |

## Ligações internas

- O guia (`/destinos/rio-de-janeiro/`) ganha os links novos no bloco "As outras páginas do
  Rio de Janeiro", e a ficha do Cristo e a do Pão de Açúcar ganham "Página completa do …" no
  fim.
- Cada página nova leva:
  - no topo, o breadcrumb Início › Destinos › Rio de Janeiro › <página>;
  - no fim, links para o guia, a ficha de custos, o roteiro e a calculadora;
  - os blocos de sempre: assinatura, capa, parceiros no fim e FAQ.
- A ficha de custos liga para "Quando ir" na seção de mesmo nome, e o roteiro liga para "O
  que fecha cada dia" na lista "As regras que sustentam esta ordem".

## Checklist de cada página (o que o site já exige)

1. Gerar com `_build/rio/paginas.py`; números importados, nunca digitados.
2. `python _build/adsense/instala.py --aplica`.
3. `python _build/cachebust/atualiza.py --aplica`, se mexer em CSS ou JS.
4. Acrescentar a URL no `sitemap.xml`, com o `lastmod` do dia.
5. `python _build/confere/tudo.py` sem reclamação.
6. Conferir no celular: a foto na primeira tela e o alt descritivo.
7. Push na `main` (publica na Hostinger), com `git pull --rebase` antes, por causa das
   rotinas de câmbio, passagens e Instagram.

## Ordem e medição

Ordem: 1 Cristo → 2 o que fecha → 3 Pão de Açúcar → 4 descontos → 5 quando ir. Depois, a
decisão de apurar o aeroporto.

Medição: impressões e cliques por URL no Search Console 4 semanas depois de cada página.
Se o Cristo e o "o que fecha" renderem, o mesmo molde (página do ponto principal, o que
fecha cada dia, descontos) passa para Lisboa, e depois para os outros destinos, que já têm
o `dados.py`.

No Instagram, cada página nova vira o destino do link de um post. O carrossel do Cristo
(06/10) e o Reel (20/10) passam a mandar para `/cristo-redentor/` em vez do guia.
