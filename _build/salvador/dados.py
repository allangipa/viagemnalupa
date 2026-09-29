# -*- coding: utf-8 -*-
"""Salvador: dez pontos, com fonte e data em cada numero.

Mesmo molde do miami/dados.py, escrito no mesmo dia. O renderizador e o
novos/gera.py, chamado com VNL_DADOS=salvador.

POR QUE SALVADOR, E POR QUE AGORA
---------------------------------
Fecha o Nordeste ao lado de Maceio e Fortaleza, e fecha a GRADE: com
quinze destinos a home terminava em sete linhas cheias mais um cartao
sozinho, porque ela e de duas colunas. Com dezesseis, fecham oito linhas.
E o mesmo motivo que fez Sevilha entrar quando havia treze.

O QUE ESTA APURACAO ACHOU
-------------------------

1. A QUARTA-FEIRA EM SALVADOR E DE GRACA EM SETE MUSEUS MUNICIPAIS.
   Nao e promocao nem data comemorativa: e regra permanente, publicada
   pela propria prefeitura. Sao Casa das Historias, Casa do Carnaval,
   Casa do Rio Vermelho, Cidade da Musica, Espaco Pierre Verger, Espaco
   Carybe e Galeria Mercado. A inteira normal e R$ 20 em quase todos.

   Esta e a maior economia programavel da cidade, e e o eixo do roteiro.

2. AS DUAS PAGINAS OFICIAIS DA PREFEITURA ESTAO DESATUALIZADAS SOBRE O
   ELEVADOR LACERDA, o monumento mais fotografado da cidade.

       Pelourinho Dia e Noite (turismo municipal)  R$ 0,15
       Mobilidade Salvador (secretaria)            R$ 0,15
       Imprensa, maio/2026                         gratuito hoje,
                                                   R$ 1,00 anunciado

   O elevador ficou cerca de dez meses fechado, reabriu depois de obra
   de mais de R$ 14 milhoes com as quatro cabines trocadas, e segue com
   acesso gratuito por tempo limitado. As duas paginas oficiais seguem
   publicando a tarifa antiga e o horario antigo.

   E o mesmo tipo de achado do Elevador de Santa Justa em Lisboa, onde a
   pagina do metro continuava listando um ascensor encerrado.

3. A IGREJA DE SAO FRANCISCO ESTA FECHADA PARA RESTAURO. E a das 800 kg
   de ouro, o ponto mais vendido do Pelourinho, e a propria pagina da
   prefeitura carimba "FECHADA PARA RESTAURO" no titulo. Sem data de
   reabertura publicada.

4. A MEIA-ENTRADA MUNICIPAL VALE PARA QUEM MORA EM SALVADOR. Nos museus
   da prefeitura, residente paga meia junto com estudante e maior de 60.
   Para o turista isso nao serve - mas serve saber, porque explica por
   que tanta gente na fila paga R$ 10 e voce paga R$ 20.

O QUE ESTA APURACAO NAO TEM, E FICA ESCRITO
-------------------------------------------
Nao apuramos tarifa de transporte urbano, nem travessia para Itaparica
ou Morro de Sao Paulo, nem diaria media de hospedagem com fonte oficial.
Onde nao ha fonte, a linha diz que nao ha.

Campos como "Visitantes por ano" e "Fatos historicos" so aparecem onde
ha fonte. Onde nao apuramos, o campo nao existe - em vez de existir
vazio.

Apuracao de 29 de setembro de 2026.
"""

APURACAO = "29 de setembro de 2026"
APURACAO_CURTA = "29/set/2026"

FLAG = '<span class="flag">%s</span> '


def mapa(consulta):
    """Link para o Google Maps no padrao da casa."""
    import urllib.parse
    q = urllib.parse.quote(consulta)
    return ('<a class="mapa" href="https://www.google.com/maps/search/?api=1&query=%s"'
            ' target="_blank" rel="noopener" aria-label="Abrir %s no Google Maps">'
            '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
            '<path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z" stroke="currentColor"'
            ' stroke-width="1.8" stroke-linejoin="round"></path><circle cx="12" cy="10" r="2.5"'
            ' stroke="currentColor" stroke-width="1.8"></circle></svg><span>Ver no mapa</span></a>'
            % (q, consulta.split(",")[0]))


# =====================================================================
#  SALVADOR
# =====================================================================
SALVADOR = {
    "slug": "salvador",
    "nome": "Salvador",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "Salvador: 10 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 10 pontos de Salvador, com os sete museus "
                  "que não cobram nada às quartas-feiras."),
    "abertura": ("Dez pontos com preço, horário e fonte conferidos em 29 de setembro de "
                 "2026 — e a regra que muda a conta de quem se organiza: <b>sete museus "
                 "municipais não cobram nada às quartas-feiras, e isso é permanente, não "
                 "promoção</b>."),
    "busca": ("salvador bahia brasil nordeste pelourinho centro historico elevador lacerda "
              "igreja sao francisco ouro senhor do bonfim fitinha farol da barra museu "
              "nautico porto da barra mercado modelo casa do carnaval casa do rio vermelho "
              "jorge amado zelia gattai pierre verger carybe forte santo antonio quarta "
              "gratuita baia de todos os santos"),
    "grupos": [
        {"id": "g1", "titulo": "O Centro Histórico",
         "intro": ("O Pelourinho e o que desce até a Cidade Baixa — onde está o museu "
                   "mais barato da lista, o mais famoso fechado para obra, e um elevador "
                   "cuja tarifa nem a prefeitura publica direito.")},
        {"id": "g2", "titulo": "A Barra e a orla",
         "intro": ("O farol que é museu e a praia dentro da baía — um dos poucos pontos "
                   "pagos de Salvador que não é da prefeitura, e por isso não entra na "
                   "quarta gratuita.")},
        {"id": "g3", "titulo": "Bonfim, Rio Vermelho e o forte",
         "intro": ("Fora do centro: a igreja das fitinhas, a casa de Jorge Amado e os "
                   "dois espaços de arte que se visitam com um bilhete só.")},
    ],
    "pontos": [

        # ---------------------------------------------------------- g1
        {
            "id": "pelourinho",
            "foto": {"arq": "salvador/pelourinho.webp",
                     "alt": ("Vista do alto do Largo do Pelourinho, em Salvador, com as "
                             "fachadas coloridas dos dois lados da ladeira de pedra, as "
                             "torres da igreja ao fundo e o mar no horizonte"),
                     "cred": "MTur Destinos · domínio público · via Wikimedia Commons"},
            "grupo": "g1",
            "nome": "Pelourinho e o Centro Histórico",
            "tag": "Centro histórico",
            "preco_val": "Grátis",
            "preco_nota": "andar pelo conjunto; os museus cobram",
            "campos": [
                ("Valor da entrada",
                 "<b>Não existe bilhete para o Pelourinho.</b> É bairro, é rua pública, e "
                 "o conjunto arquitetônico se vê andando, a qualquer hora, sem pagar "
                 "nada.<br>"
                 "<b>O que cobra são os equipamentos dentro dele</b> — Casa do Carnaval, "
                 "os espaços do Forte, as igrejas com visitação. Cada um tem a sua ficha "
                 "nesta página.<br>"
                 "O Centro Histórico de Salvador é <b>Patrimônio Mundial da UNESCO desde "
                 "1985</b>, e é o maior conjunto de arquitetura colonial portuguesa das "
                 "Américas."),
                ("Dias em que não funciona",
                 "<b>A rua não fecha.</b> Os equipamentos dentro dela têm horário próprio, "
                 "e a maioria dos museus municipais <b>fecha às segundas-feiras</b> — "
                 "ponto que vale para quase toda esta ficha.<br>"
                 "<b>O Pelourinho tem vida noturna concentrada nas terças</b>, com a "
                 "programação de rua que o bairro mantém há décadas. É o dia em que o "
                 "conjunto está mais cheio e mais tocado, e o dia em que menos museu "
                 "está aberto."),
                ("Pontos de referência",
                 "O Terreiro de Jesus e o Largo do Pelourinho são as duas praças que "
                 "organizam tudo. A Igreja e Convento de São Francisco fica no Terreiro "
                 "de Jesus — <b>e está fechada, veja a ficha abaixo</b>. A Casa do "
                 "Carnaval fica na Praça Ramos de Queirós. A ladeira que desce à Cidade "
                 "Baixa termina no Elevador Lacerda.<br>"
                 + mapa("Largo do Pelourinho, Salvador, BA")),
            ],
        },
        {
            "id": "igreja-sao-francisco",
            "foto": {"arq": "salvador/sao-francisco.webp",
                     "alt": ("A fachada da Igreja de São Francisco iluminada à noite, com a "
                             "talha barroca em pedra e a cruz no alto do frontão"),
                     "cred": "Paul R. Burley · CC BY-SA 4.0 · via Wikimedia Commons"},
            "grupo": "g1",
            "nome": "Igreja e Convento de São Francisco",
            "tag": "Igreja — fechada para restauro",
            "preco_val": "Fechada",
            "preco_nota": "restauro, sem data de reabertura",
            "campos": [
                ("Dias em que não funciona",
                 "<b>Nenhum, porque não funciona nenhum.</b> A página oficial da "
                 "prefeitura carimba a condição no próprio título do verbete: "
                 "<b>“Igreja e Convento de São Francisco – Ordem 1ª (FECHADA PARA "
                 "RESTAURO)”</b>. Fonte: Pelourinho Dia e Noite, portal da Prefeitura de "
                 "Salvador, consultado em 29/set/2026.<br>"
                 + FLAG % "Sem data de reabertura" +
                 "a página não publica previsão, e não encontramos uma em fonte oficial.<br>"
                 "<b>Isso importa mais do que parece:</b> é o ponto mais vendido do "
                 "Pelourinho, o da talha dourada, e <b>continua listado como aberto em "
                 "quase todo guia e em plataformas de passeio</b>. Quem montar o dia em "
                 "cima dele vai bater na porta."),
                ("Valor da entrada",
                 "<b>Quando aberta, a visitação custava R$ 10.</b> Fonte: mesma página da "
                 "prefeitura.<br>"
                 + FLAG % "Fontes divergem" +
                 "outras fontes registram R$ 5 para a visita simples e R$ 15 para o "
                 "combinado de igreja mais convento. <b>Como o monumento está fechado, "
                 "nenhum desses valores é praticado hoje</b>, e não há como conferir qual "
                 "voltará a valer. Registramos os três e não escolhemos nenhum.<br>"
                 "<b>Nos horários de missa a entrada sempre foi gratuita</b>, com a "
                 "ressalva de que não se circula pelo claustro nem pela capela nesse "
                 "período."),
                ("Pontos de referência",
                 "Fica no Terreiro de Jesus, no coração do Pelourinho, colada à Catedral "
                 "Basílica e à Igreja da Ordem Terceira de São Francisco — que é outro "
                 "prédio, com a fachada em pedra lavrada, e <b>não é o mesmo monumento</b>. "
                 "A confusão entre as duas é comum e agora tem consequência prática: uma "
                 "está fechada e a outra não é a que você viu na foto.<br>"
                 + mapa("Igreja e Convento de Sao Francisco, Terreiro de Jesus, Salvador, BA")),
            ],
        },
        {
            "id": "casa-do-carnaval",
            "grupo": "g1",
            "nome": "Casa do Carnaval da Bahia",
            "tag": "Museu",
            "preco_val": "R$ 20",
            "preco_nota": "inteira; grátis às quartas",
            "campos": [
                ("Valor da entrada",
                 "Fonte: Prefeitura de Salvador e portal Pelourinho Dia e Noite, "
                 "consultados em 29/set/2026.<br>"
                 "<b>Inteira R$ 20.</b> <b>Meia R$ 10</b> para estudantes, "
                 "<b>residentes em Salvador</b> e pessoas a partir de 60 anos. "
                 "<b>Criança de até 6 anos não paga.</b><br>"
                 "<b>E às quartas-feiras a entrada é gratuita para todo mundo</b> — "
                 "morador ou turista, sem restrição. É um dos sete equipamentos "
                 "municipais com essa regra permanente.<br>"
                 "<b>Repare na meia de residente:</b> ela explica por que a pessoa à sua "
                 "frente na fila paga R$ 10 e você paga R$ 20. Não é erro nem privilégio "
                 "escondido — é política municipal publicada."),
                ("Dias em que não funciona",
                 "<b>Fecha às segundas-feiras.</b> Abre de <b>terça a domingo, das 9h às "
                 "17h</b>, com <b>última entrada às 16h</b>.<br>"
                 "<b>A última entrada é uma hora antes do fechamento</b>, e não meia hora "
                 "— chegar às 16h30 não resolve."),
                ("Pontos de referência",
                 "Praça Ramos de Queirós, no Pelourinho. Tem <b>terraço com vista para a "
                 "Baía de Todos os Santos</b>, que é a parte que menos aparece nas fotos "
                 "e uma das melhores vistas gratuitas do conjunto — já incluída no "
                 "bilhete.<br>"
                 + mapa("Casa do Carnaval da Bahia, Praca Ramos de Queiros, Salvador, BA")),
            ],
        },
        {
            "id": "elevador-lacerda",
            "foto": {"arq": "salvador/elevador-lacerda.webp",
                     "alt": ("A torre do Elevador Lacerda vista da Cidade Alta, com o relógio "
                             "no topo e palmeiras ao lado da praça"),
                     "cred": "Paul R. Burley · CC BY-SA 4.0 · via Wikimedia Commons"},
            "grupo": "g1",
            "nome": "Elevador Lacerda",
            "tag": "Elevador urbano",
            "preco_val": "Grátis",
            "preco_nota": "hoje; R$ 1,00 anunciado",
            "campos": [
                ("Valor da entrada",
                 "<b>Este é o ponto com a informação oficial mais bagunçada de Salvador, "
                 "e vale ler antes de acreditar em qualquer tabela.</b><br>"
                 "<b>O que a prefeitura publica:</b> tanto o portal de turismo "
                 "(Pelourinho Dia e Noite) quanto a secretaria de Mobilidade informam "
                 "<b>R$ 0,15 por passageiro</b> — a tarifa histórica. Consultados em "
                 "29/set/2026.<br>"
                 "<b>O que a imprensa apurou:</b> o elevador ficou cerca de <b>dez meses "
                 "fechado</b> para obra de mais de <b>R$ 14 milhões</b>, com as quatro "
                 "cabines substituídas e novos sistemas de climatização e iluminação. "
                 "Reabriu, e <b>segue com acesso gratuito por tempo limitado</b> para "
                 "moradores e turistas. Quando a gratuidade acabar, a tarifa passa a "
                 "<b>R$ 1,00</b> — alta de cerca de <b>566%</b> sobre os R$ 0,15.<br>"
                 + FLAG % "Duas páginas oficiais desatualizadas" +
                 "<b>as duas fontes da própria prefeitura seguem publicando a tarifa "
                 "antiga e o horário antigo, sem uma palavra sobre a obra.</b> Não é "
                 "divergência entre um órgão e um blog: são dois órgãos municipais contra "
                 "o que a própria prefeitura entregou.<br>"
                 "<b>Na prática, leve moeda mesmo assim.</b> Se a gratuidade tiver "
                 "acabado quando você for, R$ 1,00 resolve."),
                ("Dias em que não funciona",
                 "<b>Não fecha nenhum dia da semana.</b> E aqui o horário também diverge:<br>"
                 "<b>Secretaria de Mobilidade:</b> das 6h às 22h.<br>"
                 "<b>Portal de turismo da prefeitura:</b> segunda a sexta 6h30 às 21h30; "
                 "sábado 7h às 21h30; domingo e feriado 7h às 21h.<br>"
                 "<b>Imprensa, após a reabertura:</b> segunda a sexta 6h30 às 21h30; "
                 "sábados, domingos e feriados 7h às 21h30.<br>"
                 "<b>As duas últimas quase batem; a da Mobilidade é a destoante.</b> Se "
                 "for no fim da noite, use 21h como limite seguro."),
                ("Pontos de referência",
                 "Liga a <b>Praça Municipal (Cidade Alta)</b>, ao lado do Palácio Rio "
                 "Branco, ao <b>Mercado Modelo (Cidade Baixa)</b>, em 22 segundos e 72 "
                 "metros de desnível. Transporta cerca de <b>6 mil pessoas por dia</b> — "
                 "<b>é transporte público, não brinquedo turístico</b>, e a fila do fim "
                 "da tarde é de gente voltando do trabalho.<br>"
                 + mapa("Elevador Lacerda, Praca Municipal, Salvador, BA")),
            ],
        },
        {
            "id": "mercado-modelo",
            "foto": {"arq": "salvador/mercado-modelo.webp",
                     "alt": ("O frontão do Mercado Modelo, com o nome gravado em letras altas "
                             "na pedra clara e o brasão ao centro"),
                     "cred": "Ben Tavener · CC BY 2.0 · via Wikimedia Commons"},
            "grupo": "g1",
            "nome": "Mercado Modelo",
            "tag": "Mercado",
            "preco_val": "Grátis",
            "preco_nota": "entrar; o que se compra, não",
            "campos": [
                ("Valor da entrada",
                 "<b>Entrar não custa nada.</b> É mercado de artesanato, com lojas no "
                 "térreo e no primeiro andar, e restaurantes com varanda para a baía.<br>"
                 + FLAG % "Preços de comércio não apurados" +
                 "não levantamos valor de artesanato nem cardápio: são lojas privadas, "
                 "sem tabela publicada, e variam demais para virar número nesta ficha.<br>"
                 "<b>O que vale saber antes:</b> a negociação de preço é esperada e "
                 "normal aqui, e o mesmo objeto costuma aparecer em várias lojas do "
                 "próprio mercado."),
                ("Dias em que não funciona",
                 FLAG % "Horário não confirmado em fonte oficial" +
                 "não localizamos página oficial do mercado com horário publicado durante "
                 "esta apuração, e não vamos imprimir um horário que não conferimos. "
                 "Confirme antes de ir — especialmente aos domingos."),
                ("Pontos de referência",
                 "Fica na Cidade Baixa, no pé do Elevador Lacerda — os dois se resolvem no "
                 "mesmo deslocamento, e é o encaixe mais natural desta ficha. Dali saem os "
                 "barcos da Baía de Todos os Santos, e o <b>Forte de São Marcelo</b> se vê "
                 "da varanda, no meio da água.<br>"
                 + mapa("Mercado Modelo, Praca Visconde de Cayru, Salvador, BA")),
            ],
        },

        # ---------------------------------------------------------- g2
        {
            "id": "farol-da-barra",
            "foto": {"arq": "salvador/farol-da-barra.webp",
                     "alt": ("O Farol da Barra ao pôr do sol, visto das pedras da orla, com o "
                             "céu alaranjado sobre a Baía de Todos os Santos"),
                     "cred": "Ruy Carvalho · CC BY-SA 3.0 · via Wikimedia Commons"},
            "grupo": "g2",
            "nome": "Farol da Barra e Museu Náutico da Bahia",
            "tag": "Farol e museu",
            "preco_val": "R$ 20",
            "preco_nota": "inteira; não tem quarta grátis",
            "campos": [
                ("Valor da entrada",
                 "Fonte: Museu Náutico da Bahia, site oficial, consultado em "
                 "29/set/2026.<br>"
                 "<b>Inteira R$ 20.</b> <b>Meia R$ 10</b> para estudantes, professores e "
                 "maiores de 60 anos.<br>"
                 "<b>Não pagam:</b> menores de 7 anos, museólogos, arqueólogos, alunos de "
                 "escola pública, militares, policiais civis e militares, e pessoas com "
                 "deficiência mais um acompanhante.<br>"
                 "<b>Atenção a uma diferença que engana:</b> <b>este museu não é da "
                 "prefeitura</b>, e por isso <b>não entra na quarta-feira gratuita</b>. "
                 "Custa os mesmos R$ 20 dos museus municipais, mas cobra os sete dias da "
                 "semana. Quem montar a quarta achando que tudo é grátis vai pagar aqui."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias, das 9h às 18h.</b> É um dos poucos pontos pagos "
                 "desta ficha <b>sem dia de fechamento semanal</b> — o que faz dele o "
                 "plano B natural de uma segunda-feira, quando os museus municipais estão "
                 "todos fechados."),
                ("Pontos de referência",
                 "Largo do Farol da Barra, dentro do <b>Forte de Santo Antônio da Barra</b>. "
                 "A <b>Praia do Porto da Barra</b> fica a poucos minutos a pé, e o pôr do "
                 "sol visto do farol é o cartão-postal mais reproduzido da cidade depois "
                 "do Elevador.<br>"
                 + mapa("Farol da Barra, Largo do Farol da Barra, Salvador, BA")),
            ],
        },
        {
            "id": "porto-da-barra",
            "foto": {"arq": "salvador/porto-da-barra.webp",
                     "alt": ("A Praia do Porto da Barra cheia, com guarda-sóis coloridos na "
                             "areia e os prédios da orla ao fundo"),
                     "cred": "Jofrigerio · CC BY-SA 4.0 · via Wikimedia Commons"},
            "grupo": "g2",
            "nome": "Praia do Porto da Barra",
            "tag": "Praia",
            "preco_val": "Grátis",
            "preco_nota": "a areia; cadeira e guarda-sol, não",
            "campos": [
                ("Valor da entrada",
                 "<b>Praia é bem público e ninguém pode cobrar pela areia.</b> Não há "
                 "bilheteria, portão nem horário.<br>"
                 "<b>O que custa</b> são cadeira, guarda-sol e o consumo nas barracas, "
                 "que são concessões e comércio privado. "
                 + FLAG % "Preços de barraca não apurados" +
                 "não há tabela publicada, e varia por barraca e por temporada."),
                ("Dias em que não funciona",
                 "<b>Não fecha.</b> A praia é de acesso livre 24 horas.<br>"
                 "<b>O que muda é a maré, e aqui isso importa de verdade:</b> o Porto da "
                 "Barra fica <b>dentro da Baía de Todos os Santos</b>, não no mar aberto. "
                 "A água é calma e rasa — é a praia urbana mais protegida de Salvador, e "
                 "por isso a mais cheia nos fins de semana."),
                ("Pontos de referência",
                 "Entre o Forte de Santa Maria e o Forte de São Diogo, na península da "
                 "Barra. O <b>Farol da Barra</b> fica a poucos minutos a pé pela orla, e "
                 "os dois se fazem no mesmo dia sem transporte.<br>"
                 + mapa("Praia do Porto da Barra, Salvador, BA")),
            ],
        },

        # ---------------------------------------------------------- g3
        {
            "id": "igreja-do-bonfim",
            "foto": {"arq": "salvador/bonfim.webp",
                     "alt": ("A Basílica do Senhor do Bonfim vista do largo, com as duas "
                             "torres claras despontando acima das árvores"),
                     "cred": "Elvis Boaventura · CC BY 3.0 · via Wikimedia Commons"},
            "grupo": "g3",
            "nome": "Basílica do Senhor do Bonfim",
            "tag": "Igreja",
            "preco_val": "Grátis",
            "preco_nota": "a igreja; o museu dos ex-votos à parte",
            "campos": [
                ("Valor da entrada",
                 "<b>A entrada na basílica é gratuita.</b> É igreja em funcionamento, com "
                 "missas, não equipamento turístico com bilheteria.<br>"
                 "<b>As fitinhas do Bonfim são vendidas por ambulantes no largo</b>, e o "
                 "preço é de rua — não há tabela, e "
                 + FLAG % "não apuramos valor" +
                 "porque não existe fonte oficial para preço de ambulante.<br>"
                 "<b>Um aviso que evita constrangimento:</b> amarrar a fita no gradil da "
                 "igreja é costume consolidado, mas o local é <b>santuário em uso "
                 "religioso</b>. A Sala dos Milagres, com os ex-votos, é espaço de fé "
                 "antes de ser atração — vale entrar em silêncio."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias</b>, com horário que muda conforme o dia:<br>"
                 "<b>Segunda a quinta e sábado:</b> das 6h30 às 18h.<br>"
                 "<b>Sexta e domingo:</b> das 5h30 às 18h — abre uma hora mais cedo, "
                 "porque <b>sexta é o dia do Senhor do Bonfim</b> e o movimento de fiéis "
                 "é muito maior.<br>"
                 "<b>Se o seu objetivo é ver a igreja com calma, evite a sexta.</b> Se é "
                 "ver a devoção acontecendo, é justamente o dia."),
                ("Pontos de referência",
                 "Largo do Bonfim, na Península Itapagipana, <b>longe do Centro "
                 "Histórico</b> — não é caminhada, é deslocamento. Nos fundos há um "
                 "<b>mirante para a Baía de Todos os Santos</b> que quase ninguém "
                 "inclui.<br>"
                 + mapa("Basilica do Senhor do Bonfim, Largo do Bonfim, Salvador, BA")),
            ],
        },
        {
            "id": "casa-do-rio-vermelho",
            "foto": {"arq": "salvador/rio-vermelho.webp",
                     "alt": ("A fachada da Casa do Rio Vermelho, com a placa do memorial a "
                             "Jorge Amado e Zélia Gattai sobre a entrada amarela"),
                     "cred": "Turismo Bahia · CC BY-SA 2.0 · via Wikimedia Commons"},
            "grupo": "g3",
            "nome": "Casa do Rio Vermelho — Jorge Amado e Zélia Gattai",
            "tag": "Casa-museu",
            "preco_val": "R$ 20",
            "preco_nota": "inteira; grátis às quartas",
            "campos": [
                ("Valor da entrada",
                 "Fonte: Prefeitura de Salvador, consultada em 29/set/2026.<br>"
                 "<b>Inteira R$ 20</b>, <b>meia R$ 10</b> para estudantes, residentes em "
                 "Salvador e maiores de 60 anos.<br>"
                 "<b>Gratuito às quartas-feiras</b>, como os outros seis equipamentos "
                 "municipais.<br>"
                 "É a casa onde <b>Jorge Amado e Zélia Gattai viveram por mais de "
                 "cinquenta anos</b>, e onde os dois estão enterrados, sob a mangueira do "
                 "jardim. O acervo tem mais de 30 horas de vídeo e projeções."),
                ("Dias em que não funciona",
                 "<b>Fecha às segundas-feiras.</b> Abre de <b>terça a domingo, das 9h às "
                 "17h</b>, com <b>última entrada às 16h</b> — mesma grade da Casa do "
                 "Carnaval."),
                ("Pontos de referência",
                 "Rua Alagoinhas, 33, no <b>Rio Vermelho</b> — bairro da vida noturna e "
                 "dos bares, longe do Pelourinho. <b>É o encaixe natural de um fim de "
                 "tarde</b>: fecha às 17h e o bairro começa logo depois.<br>"
                 + mapa("Casa do Rio Vermelho, Rua Alagoinhas 33, Salvador, BA")),
            ],
        },
        {
            "id": "espacos-do-forte",
            "foto": {"arq": "salvador/forte-santo-antonio.webp",
                     "alt": ("A muralha branca do Forte de Santo Antônio Além do Carmo, com "
                             "vegetação subindo pela pedra da rampa"),
                     "cred": "Paul R. Burley · CC BY-SA 4.0 · via Wikimedia Commons"},
            "grupo": "g3",
            "nome": "Espaço Pierre Verger e Espaço Carybé",
            "tag": "Dois museus, um bilhete",
            "preco_val": "R$ 20",
            "preco_nota": "um bilhete para os dois; grátis às quartas",
            "campos": [
                ("Valor da entrada",
                 "Fonte: Prefeitura de Salvador, consultada em 29/set/2026.<br>"
                 "<b>Inteira R$ 20</b>, <b>meia R$ 10</b> para estudantes, residentes em "
                 "Salvador e maiores de 60 anos. <b>Gratuitos às quartas-feiras.</b><br>"
                 "<b>E aqui está a melhor relação desta ficha:</b> <b>um único bilhete dá "
                 "acesso aos dois espaços</b>, que ficam no mesmo forte. São dois museus "
                 "pelo preço de um — e de graça na quarta.<br>"
                 "O <b>Espaço Pierre Verger da Fotografia Baiana</b> guarda o trabalho do "
                 "fotógrafo e etnólogo francês que documentou o candomblé e a relação "
                 "entre a Bahia e a África. O <b>Espaço Carybé de Artes</b> reúne a obra "
                 "do artista argentino-brasileiro que ilustrou Jorge Amado."),
                ("Dias em que não funciona",
                 FLAG % "Horário não confirmado individualmente" +
                 "a lista da prefeitura não publica a grade de cada espaço. <b>Os demais "
                 "equipamentos municipais desta ficha abrem de terça a domingo, das 9h às "
                 "17h, e fecham segunda</b> — o mais provável é que estes sigam o mesmo "
                 "padrão, mas <b>a fonte não diz isso</b>, e por isso não afirmamos. "
                 "Confirme antes de ir."),
                ("Pontos de referência",
                 "Os dois ficam no <b>Forte de Santo Antônio Além do Carmo</b>, no alto do "
                 "Centro Histórico, a caminhada do Pelourinho. O forte tem vista aberta "
                 "para a baía e para a Cidade Baixa.<br>"
                 + mapa("Forte de Santo Antonio Alem do Carmo, Salvador, BA")),
            ],
        },
    ],
}

DESTINOS = [SALVADOR]
