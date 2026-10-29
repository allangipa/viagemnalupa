# -*- coding: utf-8 -*-
"""Barcelona: o vigesimo primeiro destino, em doze pontos e tres grupos.

Mesmo molde do granada/dados.py.

O ACHADO PRINCIPAL: A TAXA TURISTICA DOBROU EM 1 DE ABRIL DE 2026, E E
A LINHA QUE MAIS CRESCE DA CONTA
--------------------------------------------------------------------
A Llei 2/2026, de 6 de marco, mudou o impost sobre les estades en
establiments turistics (IEET) da Catalunha, e a Agencia Tributaria de
Catalunya publica a tabela em vigor de 01.04.2026 a 31.03.2027 para a
cidade de Barcelona, por pessoa e por noite:

    hotel 5 estrelas / gran luxo ............ 7,00  + recarrec 5,00 = 12,00
    hotel 4 estrelas ........................ 3,40  + recarrec 5,00 =  8,40
    apartamento turistico (HUT) ............. 4,50  + recarrec 5,00 =  9,50
    albergue ................................ 1,00  + recarrec 5,00 =  6,00
    resta d'establiments (hoteis de 1 a 3
    estrelas, hostals, pensoes) ............. 2,00  + recarrec 5,00 =  7,00

O recarrec e do Ayuntamiento de Barcelona e a tabela da ATC ja publica
os proximos: 6,00 a partir de 01.04.2027 e 7,00 a partir de 01.04.2028.
Teto de 7 noites por pessoa no mesmo estabelecimento; menores de 17 nao
pagam. Quatro noites num hotel de ate tres estrelas sao 28 EUR por
pessoa - mais que o ingresso do Museu Picasso e do MNAC somados. E a
regra que quase ninguem diz: em reserva antecipada vale a tarifa do dia
do pagamento, se o imposto e o recarrec forem pagos junto. Quem paga
antes de 1 de abril de 2027 trava os 5 EUR.

O SEGUNDO ACHADO: A SEMANA TEM TRES TARDES GRATIS, EM TRES DIAS
--------------------------------------------------------------------
    quinta   Museu Picasso, 16h as 19h, por reserva (abre 4 dias antes, as 10h)
    sabado   MNAC, a partir das 15h
    domingo  Castell de Montjuic, a partir das 15h

Mais o primeiro domingo do mes, em que os tres sao gratuitos o dia
inteiro. Sao 36 EUR de ingresso que caem com o calendario certo. Uma
viagem de quinta a segunda pega as tres tardes.

O TERCEIRO: O INE DIZ QUAL E O MES MAIS CARO, E E MAIO
--------------------------------------------------------------------
Tabela 46298, serie "Barcelona. Tarifa media diaria (ADR)", 12 meses
de out/2025 a set/2026 (lida em 29/10/2026): maio de 2026 a 223,37 EUR
por quarto e dezembro de 2025 a 131,41 - 70% de diferenca. Media dos
doze: 179,45 (calculo
nosso). Barcelona nao tem o "agosto ao contrario" de Granada: agosto
(175,42) fica perto da media.

O QUE FICOU SEM RESPOSTA, E ESTA DITO EM CADA FICHA
--------------------------------------------------------------------
    Aerobus                 o site oficial publica a tarifa so em imagem
                            decorativa; o preco nao esta em texto em
                            pagina nenhuma do dominio
    Sagrada Familia         horario das torres; o aviso "fechada
                            temporariamente" sem data na pagina de
                            ingressos (o unico fechamento datado foi
                            4/out ate 14h, por tempo)
    Casa Batllo, Pedrera    precos "a partir de": o valor final depende
                            da data e so aparece no caixa
    Palau de la Musica      valor das tarifas reduzidas nao publicado
    Camp Nou                horario do museu nao esta na pagina de
                            ingressos; o estado das obras vem da imprensa
    Catedral                horario de culto (entrada livre) nao publicado
                            na pagina de horarios da visita turistica

Apuracao de 18 de outubro de 2026.
"""

APURACAO = "18 de outubro de 2026"
APURACAO_CURTA = "18/out/2026"

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
#  BARCELONA
# =====================================================================
BARCELONA = {
    "slug": "barcelona",
    "nome": "Barcelona",
    "pais": "Espanha",
    "regiao": "europa",
    "titulo": "Barcelona: 12 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 12 pontos de Barcelona, com a taxa turística "
                  "que dobrou em abril de 2026 e as três tardes da semana em que os museus "
                  "não cobram."),
    "abertura": ("Doze pontos com preço em euro, horário e fonte conferidos em 18 de "
                 "outubro de 2026 — e duas coisas que os guias não somam: <b>a taxa "
                 "turística de Barcelona dobrou em 1º de abril de 2026 e já tem aumento "
                 "marcado para 2027 e 2028</b>; quatro noites num hotel de três estrelas "
                 "são € 28 de taxa por pessoa, fora do preço do quarto. <b>E a semana tem "
                 "três tardes grátis em três dias diferentes</b> — Picasso na quinta, "
                 "MNAC no sábado, Montjuïc no domingo —, que uma viagem de quinta a "
                 "segunda pega todas."),
    "busca": ("barcelona espanha espana catalunha cataluna europa gaudi sagrada familia "
              "park guell parque guell casa batllo pedrera casa mila picasso mnac montjuic "
              "sant pau catedral palau musica camp nou barca taxa turistica"),
    "grupos": [
        {"id": "g1", "titulo": "Gaudí: quatro ingressos, quatro regras diferentes",
         "intro": ("Sagrada Família, Park Güell, Casa Batlló e La Pedrera — cada um com "
                   "um dono, um preço e uma regra de entrada. Só um deles tem preço "
                   "fixo publicado.")},
        {"id": "g2", "titulo": "As três tardes grátis da semana",
         "intro": ("Picasso, MNAC e o Castell de Montjuïc não cobram em três tardes de "
                   "três dias diferentes, e o primeiro domingo do mês libera os três. "
                   "Mais o Sant Pau, que cobra € 1 a menos depois das 14h.")},
        {"id": "g3", "titulo": "O resto da cidade, o estádio em obras e a conta da cama",
         "intro": ("Catedral, Palau de la Música e o Camp Nou que ainda não voltou a ser "
                   "visitável por inteiro — e a hospedagem com a taxa que mais cresce "
                   "da Espanha.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - Gaudi
        # =============================================================
        {
            "id": "sagrada-familia",
            "foto": {"arq": "barcelona/sagrada-familia.webp",
                     "alt": "A fachada da Sagrada Família vista de baixo, com as torres e os guindastes da obra, em dezembro de 2025",
                     "cred": "Enric · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Sagrada Família",
            "tag": "Basílica",
            "preco_val": "€ 26",
            "preco_nota": "com as torres € 36; nominativo, sem devolução",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de preços do site oficial (sagradafamilia.org/en/prices), "
                 "consultada em 18/out/2026.<br>"
                 "<b>Basílica, com o app de audioguia incluído: € 26.</b><br>"
                 "<b>Basílica + torres: € 36.</b> Visita guiada: € 30; guiada + torres: "
                 "€ 40.<br>"
                 "<b>Maior de 65 anos: € 21</b> (torres € 28). <b>Menor de 30 e "
                 "estudante com carteira: € 24</b> (torres € 34). <b>Menor de 11 anos "
                 "não paga</b>, nem pessoa com deficiência; o acompanhante paga só os "
                 "serviços extras.<br>"
                 "<b>Os ingressos só se vendem on-line</b> — a página de horários diz "
                 "<i>“Tickets can only be purchased online”</i>."),
                ("A regra que faz perder o ingresso",
                 "Fonte: <b>Rules and conditions of sale</b> do site oficial, "
                 "consultadas em 18/out/2026.<br>"
                 "<b>O ingresso é nominativo:</b> cláusula 4.2, <i>“Tickets are "
                 "nominative, personal, and non-transferable”</i>. A cláusula 13.2 "
                 "exige <b>documento original</b> na entrada, e o acesso pode ser "
                 "negado se o nome não bater.<br>"
                 "<b>Não há troca nem devolução</b> (cláusula 5.1). A exceção da 5.2 "
                 "vale só para ingresso <b>não validado</b> e por problema de acesso "
                 "que não seja culpa do visitante — fechamento, mau tempo. Nesses "
                 "casos o pedido tem de entrar em <b>15 dias</b> e o dinheiro volta em "
                 "até 30; <b>nunca se reembolsa</b> transporte ou hospedagem "
                 "(cláusula 5.4).<br>"
                 "<b>Hora marcada:</b> a cláusula 13.3 manda apresentar-se <i>“at the "
                 "time indicated during the purchase”</i>, e <b>não publica "
                 "tolerância de atraso</b>. Quem sai não entra de novo."),
                ("Dias e horários",
                 "Fonte: página de horários do site oficial, consultada em "
                 "18/out/2026.<br>"
                 "<b>Novembro a fevereiro:</b> segunda a sábado, <b>9h às 18h</b>; "
                 "domingo, <b>10h30 às 18h</b>.<br>"
                 "<b>Março e outubro:</b> segunda a sexta, <b>9h às 19h</b>; sábado, "
                 "9h às 18h; domingo, 10h30 às 19h.<br>"
                 "<b>Abril a setembro:</b> segunda a sexta, <b>9h às 20h</b>; sábado, "
                 "9h às 18h; domingo, 10h30 às 20h.<br>"
                 "<b>25 e 26 de dezembro, 1º e 6 de janeiro: 9h às 14h.</b><br>"
                 "<b>O sábado fecha às 18h o ano inteiro</b>, mesmo no verão — duas "
                 "horas antes da sexta."),
                ("O que não está publicado",
                 FLAG % "Lacuna declarada" +
                 "<b>o horário das torres não está na página de horários</b>, só o da "
                 "basílica.<br>"
                 "E a página de ingressos exibia, em 18/out/2026, um aviso <b>sem "
                 "data</b> de que a basílica está <i>“temporarily closed to the "
                 "public”</i>. <b>O único fechamento datado que achamos</b> é o aviso "
                 "de 3/out/2026: fechada em <b>4 de outubro até as 14h</b> por previsão "
                 "de mau tempo, com reembolso automático para quem comprou pelo canal "
                 "oficial. Confira a página de notícias do site antes de ir.<br>"
                 "O site também avisa que a <b>Casa-Museu Gaudí</b>, no Park Güell, "
                 "<i>“is closed temporarily”</i>."),
                ("Onde fica",
                 mapa("Basílica de la Sagrada Família, Carrer de Mallorca 401, 08013 Barcelona, Espanha")),
            ],
        },
        {
            "id": "park-guell",
            "foto": {"arq": "barcelona/park-guell.webp",
                     "alt": "O banco ondulado de mosaico do terraço do Park Güell, com a cidade e o mar ao fundo",
                     "cred": "Julian Lupyan · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Park Güell",
            "tag": "Parque",
            "preco_val": "€ 18",
            "preco_nota": "30 minutos de tolerância; depois perde",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página <i>Prices and times</i> do site oficial "
                 "(parkguell.barcelona), consultada em 18/out/2026. <b>Os preços "
                 "incluem 21% de IVA.</b><br>"
                 "<b>Geral: € 18.</b><br>"
                 "<b>De 7 a 12 anos: € 13,50.</b> Maior de 65 e acompanhante de pessoa "
                 "com deficiência: € 13,50.<br>"
                 "<b>De 0 a 6 anos: € 0</b> — mas precisa de ingresso emitido.<br>"
                 "Com o bilhete do MUHBA ou da Ruta del Modernisme: € 14,50.<br>"
                 "<b>A compra é obrigatoriamente antecipada e on-line</b>: a home do "
                 "site diz <i>“Tickets for Park Güell must be purchased in advance and "
                 "online”</i>."),
                ("A regra dos 30 minutos",
                 "<b>Você tem 30 minutos depois da hora marcada para entrar.</b> O site: "
                 "<i>“you can enter the restricted area up to 30 minutes after your "
                 "allocated start time”</i> — reserva das 9h30, entrada até 10h. "
                 "<b>Depois disso o direito de entrar se perde.</b><br>"
                 "Dentro, fica o tempo que quiser. <b>Mas quem sai não entra de "
                 "novo.</b>"),
                ("Dias e horários",
                 "<b>Visita com ingresso: 9h30 às 19h30</b>, e o site diz que o parque "
                 "<i>“is open all the year round”</i>.<br>"
                 "<b>Das 7h às 9h30 e das 20h às 22h o parque é dos vizinhos</b> "
                 "(faixas <i>Bon dia Barcelona</i> e <i>Bon vespre Barcelona</i>), "
                 "<b>sem visita turística</b>.<br>"
                 + FLAG % "Lacuna declarada" +
                 "<b>a página oficial não publica horário de inverno</b> — o campo "
                 "<i>“Last hour of access”</i> está em branco. Sites de terceiros dizem "
                 "que no inverno fecha por volta das 17h30, por falta de iluminação. "
                 "<b>Não confirmamos isso em fonte oficial.</b>"),
                ("Onde fica",
                 mapa("Park Güell, Carrer d'Olot, 08024 Barcelona, Espanha")),
            ],
        },
        {
            "id": "casa-batllo",
            "foto": {"arq": "barcelona/casa-batllo.webp",
                     "alt": "A fachada da Casa Batlló vista da calçada, com as sacadas em forma de máscara e o telhado escamado",
                     "cred": "Teodoir · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Casa Batlló",
            "tag": "Casa de Gaudí",
            "preco_val": "desde € 29",
            "preco_nota": "preço muda com a data; o final só no caixa",
            "campos": [
                ("Valor da entrada, e por que é “desde”",
                 "Fonte: página de ingressos on-line do site oficial (casabatllo.es), "
                 "consultada em 18/out/2026.<br>"
                 "<b>Visita geral: “From € 29”.</b> A mesma página diz <i>“Advance: "
                 "save up to € 15 per person”</i>, ou seja, <b>o preço varia com a "
                 "data e a antecedência</b> e o site não publica a tabela. "
                 "<b>€ 29 é piso, não total.</b><br>"
                 "<b>Menor de 12 anos não paga.</b> Estudante com carteira, de 13 a 17 "
                 "anos e pessoa com deficiência: <b>€ 6 a menos</b>. Maior de 65: "
                 "<b>€ 3 a menos</b>.<br>"
                 "<b>Visita noturna: desde € 25</b>, com taça de cava, <b>sem o "
                 "terraço</b> (<i>“Rooftop not included”</i>), só até 15 de novembro e "
                 "só on-line. <b>Be the First</b>, entrada às 8h30 antes do público: "
                 "€ 45, com terraço."),
                ("Horários",
                 "O formulário de grupos do site diz <i>“Every day from 9am to "
                 "10:30pm”</i> para a casa, e abre faixas de 17h só de 15/3 a 15/10 e "
                 "de 18h só de 1/4 a 31/8.<br>"
                 + FLAG % "Lacuna declarada" +
                 "<b>a página de ingressos não publica o horário da visita geral por "
                 "estação</b>; o que está em texto é o do formulário de grupos. "
                 "Confira a hora no próprio seletor de compra."),
                ("Onde fica",
                 mapa("Casa Batlló, Passeig de Gràcia 43, 08007 Barcelona, Espanha")),
            ],
        },
        {
            "id": "la-pedrera",
            "foto": {"arq": "barcelona/la-pedrera.webp",
                     "alt": "La Pedrera na esquina do Passeig de Gràcia, com as árvores e o trânsito da avenida em primeiro plano",
                     "cred": "Txllxt TxllxT · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "La Pedrera (Casa Milà)",
            "tag": "Casa de Gaudí",
            "preco_val": "desde € 29",
            "preco_nota": "tarifa “Essential” válida até 1/11/2026",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de ingressos do site oficial (lapedrera.com), "
                 "consultada em 18/out/2026. <b>Todos os preços estão como “From”.</b><br>"
                 "<b>La Pedrera Essential: desde € 29</b>, 9h às 17h30, com videoguia em "
                 "11 línguas — pátios, apartamento, sótão e terraço. <b>Marcada como "
                 "“Until 01/11/26”.</b><br>"
                 "<b>Sunset: desde € 25</b>, 17h30 às 20h30, mesmo conteúdo.<br>"
                 "<b>Night Experience: desde € 39,50</b>, sessões das 20h40 às 22h20, "
                 "guiada, com espetáculo no terraço e taça de cava.<br>"
                 "<b>Open Date: desde € 45</b> — a única sem dia marcado.<br>"
                 "<b>Menor de 12 anos não paga</b> em todas, menos na Premium (€ 120, "
                 "máximo 6 pessoas).<br>"
                 "<b>Combinados a € 42:</b> Pedrera + Sant Pau, ou Pedrera + Palau de "
                 "la Música — ambos saem mais baratos que as duas entradas separadas."),
                ("O que não está publicado",
                 FLAG % "Lacuna declarada" +
                 "<b>não há preço reduzido de estudante ou de maior de 65 na página</b>, "
                 "só o “From” de cada modalidade e a gratuidade até 11 anos.<br>"
                 "E a data <i>“Until 01/11/26”</i> da Essential diz que <b>a tarifa de "
                 "€ 29 tem prazo</b>. Depois de 1º de novembro de 2026, confira."),
                ("Onde fica",
                 mapa("La Pedrera - Casa Milà, Passeig de Gràcia 92, 08008 Barcelona, Espanha")),
            ],
        },
        # =============================================================
        #  g2 - as tres tardes gratis
        # =============================================================
        {
            "id": "museu-picasso",
            "foto": {"arq": "barcelona/museu-picasso.webp",
                     "alt": "O pátio gótico de um dos palácios do Museu Picasso, na Carrer de Montcada, com a escadaria e as arcadas",
                     "cred": "Enric · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Museu Picasso",
            "tag": "Museu",
            "preco_val": "€ 12",
            "preco_nota": "€ 13 na bilheteria; quinta 16h–19h grátis com reserva",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página <i>Buy tickets and opening hours</i> do site oficial "
                 "(museupicassobcn.cat), consultada em 18/out/2026.<br>"
                 "<b>Coleção + exposição temporária: € 12 on-line, € 13 na "
                 "bilheteria.</b> Comprar antes custa € 1 a menos.<br>"
                 "<b>Reduzida: € 7</b> — de 18 a 25 anos, maior de 65, estudante "
                 "universitário com comprovante, desempregado.<br>"
                 "<b>Menor de 18 anos não paga.</b><br>"
                 "<b>Articket BCN: € 38</b> para seis museus (Picasso, MNAC, MACBA, "
                 "CCCB, Fundació Tàpies, Fundació Miró) — paga-se com Picasso + MNAC + "
                 "mais um."),
                ("As horas em que não cobra",
                 "<b>Quinta-feira, das 16h às 19h: grátis, com reserva prévia.</b><br>"
                 "<b>Primeiro domingo de cada mês: grátis, com reserva prévia.</b><br>"
                 "De 31 de março a 27 de setembro, também <b>quinta, sexta e sábado das "
                 "19h às 21h</b>.<br>"
                 "Portas abertas em <b>12 de fevereiro, 17 de maio e 24 de "
                 "setembro</b>.<br>"
                 "<b>A regra que decide:</b> o site diz <i>“Free-of-charge times: four "
                 "days before the visit, from 10 am onwards”</i> — <b>a reserva "
                 "gratuita abre quatro dias antes, às 10h</b>, e o museu tem lotação "
                 "limitada. Para a quinta, é na segunda de manhã."),
                ("Dias e horários",
                 "<b>29 de setembro a 29 de março:</b> terça a domingo, <b>10h às "
                 "19h</b>.<br>"
                 "<b>31 de março a 27 de setembro:</b> terça, quarta e domingo, 9h às "
                 "20h; <b>quinta, sexta e sábado, 9h às 21h</b>.<br>"
                 "<b>Fecha toda segunda-feira</b>, 1º de janeiro, 1º de maio, 24 de "
                 "junho e 25 de dezembro. 24 e 31 de dezembro: 10h às 14h.<br>"
                 "A bilheteria fecha 30 minutos antes."),
                ("Onde fica",
                 mapa("Museu Picasso, Carrer de Montcada 15-23, 08003 Barcelona, Espanha")),
            ],
        },
        {
            "id": "mnac",
            "foto": {"arq": "barcelona/mnac.webp",
                     "alt": "As fontes de Montjuïc em cascata, com o Palau Nacional, sede do MNAC, no alto",
                     "cred": "Enric · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "MNAC — Museu Nacional d'Art de Catalunya",
            "tag": "Museu",
            "preco_val": "€ 12",
            "preco_nota": "sábado a partir das 15h grátis; vale dois dias",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página <i>Opening hours and prices</i> do site oficial "
                 "(museunacional.cat), consultada em 18/out/2026.<br>"
                 "<b>Entrada geral: € 12</b>, e <b>vale dois dias</b> dentro de um mês "
                 "da compra — coleção permanente, temporárias e o terraço-mirante.<br>"
                 "<b>Entrada básica: € 2</b> — só o edifício, o terraço e o material "
                 "de visita autoguiada. É o preço de ver o Palau Nacional por dentro "
                 "e a vista de Montjuïc sem entrar nas salas.<br>"
                 "<b>Reduzida: 30% de desconto</b> para estudante, família (2 adultos "
                 "+ 1 criança) e grupos; 50% com Carnet Jove.<br>"
                 "<b>Menor de 16 e maior de 65 não pagam a entrada geral</b> — o site "
                 "diz que a gratuidade <b>não vale para a entrada básica de € 2</b>.<br>"
                 "Articket BCN: € 38, seis museus, válido um ano."),
                ("As horas em que não cobra",
                 "<b>Todo sábado a partir das 15h.</b><br>"
                 "<b>Todo primeiro domingo do mês.</b><br>"
                 "Mais os dias de portas abertas. O site: <i>“Admission to the museum "
                 "is free every Saturday from 3 pm, every first Sunday of the month and "
                 "open doors days.”</i> E avisa que <b>a entrada gratuita também se "
                 "reserva on-line</b>."),
                ("Dias e horários",
                 "<b>Outubro a abril:</b> terça a sábado, <b>10h às 18h</b>; domingo e "
                 "feriado, 10h às 15h.<br>"
                 "<b>Maio a setembro:</b> terça a sábado, <b>10h às 20h</b>; domingo e "
                 "feriado, 10h às 15h.<br>"
                 "<b>Fecha segunda-feira</b> (salvo feriado), 1º de janeiro, 1º de maio "
                 "e 25 de dezembro.<br>"
                 "Bilheteria fecha 30 minutos antes; as salas, 15 minutos antes.<br>"
                 "<b>O sábado grátis no inverno dura três horas</b> (15h às 18h); no "
                 "verão, cinco."),
                ("Onde fica",
                 mapa("Museu Nacional d'Art de Catalunya, Palau Nacional, Parc de Montjuïc, 08038 Barcelona, Espanha")),
            ],
        },
        {
            "id": "castell-montjuic",
            "foto": {"arq": "barcelona/castell-montjuic.webp",
                     "alt": "A entrada do Castell de Montjuïc, com o pátio de pedra e a torre de vigia",
                     "cred": "Txllxt TxllxT · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Castell de Montjuïc",
            "tag": "Fortaleza e mirante",
            "preco_val": "€ 12",
            "preco_nota": "domingo a partir das 15h grátis; só vende no site próprio",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página <i>Planning your visit</i> do site oficial, no "
                 "domínio do Ayuntamiento (ajuntament.barcelona.cat/castelldemontjuic), "
                 "consultada em 18/out/2026.<br>"
                 "<b>Geral: € 12. Reduzida: € 8.</b><br>"
                 "<b>Menor de 16 anos não paga.</b><br>"
                 "Só as exposições temporárias: € 6. Com visita guiada: € 16 (€ 4 nos "
                 "dias gratuitos).<br>"
                 "<b>O castelo só vende ingresso no próprio site</b> — a página diz que "
                 "<i>“only sells online tickets through its own website”</i> e que não "
                 "tem acordo com plataforma nenhuma. <b>Não há devolução</b>, salvo "
                 "força maior comprovada."),
                ("As horas em que não cobra",
                 "<b>Todo domingo a partir das 15h.</b><br>"
                 "<b>Todo primeiro domingo do mês, o dia inteiro.</b><br>"
                 "É o terceiro vértice da semana: Picasso na quinta, MNAC no sábado, "
                 "Montjuïc no domingo."),
                ("Dias e horários",
                 "<b>1º de março a 31 de outubro: 10h às 20h</b> (bilheteria até "
                 "19h30).<br>"
                 "<b>1º de novembro a 28 de fevereiro: 10h às 18h</b> (bilheteria até "
                 "17h30).<br>"
                 "<b>Abre todos os dias</b>; fecha só em 25 de dezembro e 1º de "
                 "janeiro.<br>"
                 "<b>O funicular de Montjuïc está dentro do bilhete simples da TMB</b> "
                 "(€ 2,90): a página de tarifas diz <i>“Valid for metro, bus, and "
                 "Montjuïc funicular”</i>. O teleférico até o castelo é outra empresa "
                 "e outro bilhete."),
                ("Onde fica",
                 mapa("Castell de Montjuïc, Carretera de Montjuïc 66, 08038 Barcelona, Espanha")),
            ],
        },
        {
            "id": "sant-pau",
            "foto": {"arq": "barcelona/sant-pau.webp",
                     "alt": "A fachada do Recinte Modernista de Sant Pau vista da rua, com um ônibus da TMB passando",
                     "cred": "Oleksandr Dede · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Recinte Modernista de Sant Pau",
            "tag": "Hospital modernista",
            "preco_val": "€ 18",
            "preco_nota": "€ 17 depois das 14h; menor de 12 não paga",
            "campos": [
                ("Valor da entrada, e a hora que muda o preço",
                 "Fonte: página da visita livre do site oficial (santpaubarcelona.org), "
                 "consultada em 18/out/2026.<br>"
                 "<b>Visita livre: € 18 até as 14h, € 17 depois das 14h.</b> O site "
                 "escreve exatamente assim: <i>“€18 (until 2 PM), €17 (after 2 PM)”</i>. "
                 "<b>É o único ponto desta ficha que fica mais barato à tarde.</b><br>"
                 "<b>Reduzida: € 11,90</b> — de 12 a 24 anos, maior de 65, família "
                 "numerosa.<br>"
                 "<b>Menor de 12 anos não paga</b> (acompanhado). Desempregado com "
                 "comprovante espanhol também não.<br>"
                 "<b>Visita guiada: € 21</b> (€ 5 de 3 a 11 anos), 75 minutos, "
                 "<b>só em fim de semana e feriado</b>: sábado 10h30 em inglês e 12h em "
                 "francês; sábado, domingo e feriado 11h em espanhol e 12h30 em "
                 "catalão.<br>"
                 "Combinado com La Pedrera: € 42."),
                ("Dias e horários",
                 "<b>Abril a outubro:</b> todos os dias, <b>9h30 às 18h30</b>.<br>"
                 "<b>Novembro a março:</b> todos os dias, <b>9h30 às 17h</b>.<br>"
                 "Entrada até 30 minutos antes de fechar. Duração sugerida: 45 a 60 "
                 "minutos.<br>"
                 "<b>Não fecha às segundas</b> — é o museu para a segunda-feira, "
                 "quando Picasso e MNAC fecham.<br>"
                 "<b>Fica a 10 minutos a pé da Sagrada Família</b>, pela Avinguda de "
                 "Gaudí, em linha reta. Uma manhã na basílica e o Sant Pau depois das "
                 "14h, por € 17, é o arranjo que a geografia e o preço combinam."),
                ("O domingo que não é para todos",
                 "O primeiro domingo do mês <b>não é gratuito no Sant Pau para o "
                 "público geral</b>: o site reserva a gratuidade a <i>“Persons over 65 "
                 "on the first Sunday of the month (organized groups)”</i>, por e-mail. "
                 "<b>Não confunda com o primeiro domingo de Picasso, MNAC e "
                 "Montjuïc.</b>"),
                ("Onde fica",
                 mapa("Recinte Modernista de Sant Pau, Carrer de Sant Antoni Maria Claret 167, 08025 Barcelona, Espanha")),
            ],
        },
        # =============================================================
        #  g3 - o resto, o estadio e a cama
        # =============================================================
        {
            "id": "catedral",
            "foto": {"arq": "barcelona/catedral.webp",
                     "alt": "As torres da Catedral de Barcelona sobre os telhados do Barri Gòtic",
                     "cred": "Enric · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Catedral de Barcelona",
            "tag": "Catedral",
            "preco_val": "€ 16",
            "preco_nota": "visita turística; domingo só à tarde",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de horários da visita turística do site oficial "
                 "(catedralbcn.org), consultada em 18/out/2026. <b>Preços isentos de "
                 "IVA.</b><br>"
                 "<b>Individual: € 16.</b><br>"
                 "<b>Reduzida: € 14</b> — estudante até 25 anos, família numerosa e "
                 "monoparental, com comprovante.<br>"
                 "Pessoa com deficiência de 33% ou mais e membro do ICOM: não pagam. "
                 "Grupos: € 8 por pessoa."),
                ("Dias e horários da visita turística",
                 "<b>Dias úteis: 9h30 às 18h30</b> (entrada até 17h45).<br>"
                 "<b>Sábado e véspera de festa religiosa: 9h30 às 17h15</b> (entrada "
                 "até 16h30).<br>"
                 "<b>Domingo e festa religiosa: 14h às 17h</b> (entrada até 16h30). "
                 "<b>De manhã, no domingo, não há visita turística.</b>"),
                ("O que não está publicado",
                 FLAG % "Lacuna declarada" +
                 "<b>a página de horários não diz o que a entrada de € 16 inclui</b> — "
                 "terraços, coro e museu capitular aparecem no site, mas não na linha "
                 "do preço.<br>"
                 "<b>E não publica o horário de culto</b>, em que a entrada para rezar "
                 "é livre. O calendário do site lista missas (18h às 19h no altar-mor, "
                 "por exemplo), mas não diz se o turista entra nelas sem pagar. "
                 "<b>Não inferimos; perguntamos na porta.</b>"),
                ("Onde fica",
                 mapa("Catedral de Barcelona, Pla de la Seu, 08002 Barcelona, Espanha")),
            ],
        },
        {
            "id": "palau-musica",
            "foto": {"arq": "barcelona/palau-musica.webp",
                     "alt": "A sala de concertos do Palau de la Música Catalana, com a claraboia de vitral e as esculturas do palco",
                     "cred": "Alvesgaspar · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Palau de la Música Catalana",
            "tag": "Sala de concertos",
            "preco_val": "€ 20",
            "preco_nota": "com audioguia; guiada € 24; reduzidas sem valor publicado",
            "campos": [
                ("Valor da visita",
                 "Fonte: página <i>Visit the Palau</i> do site oficial "
                 "(palaumusica.cat), consultada em 18/out/2026.<br>"
                 "<b>Visita autoguiada com audioguia: € 20.</b><br>"
                 "<b>Visita guiada: € 24</b>, 50 minutos, em várias línguas.<br>"
                 "Combinado com La Pedrera: € 42.<br>"
                 "É a sala de concertos de Lluís Domènech i Montaner — o mesmo "
                 "arquiteto do Sant Pau —, Patrimônio Mundial desde 1997."),
                ("O que não está publicado",
                 FLAG % "Lacuna declarada" +
                 "<b>o site diz que há tarifa reduzida para crianças, maiores de 65 e "
                 "famílias, mas não publica o valor</b> — <i>“Reduced rates are "
                 "available for children, over-65s, families and other eligible "
                 "categories”</i>, e só.<br>"
                 "<b>Nem a idade em que a criança não paga</b>, nem os horários das "
                 "sessões: o site manda <i>“choose your time slot”</i> no seletor de "
                 "compra. Dias sem visita (ensaios, concertos) também só aparecem lá."),
                ("Onde fica",
                 mapa("Palau de la Música Catalana, Carrer del Palau de la Música 4-6, 08003 Barcelona, Espanha")),
            ],
        },
        {
            "id": "camp-nou",
            "grupo": "g3",
            "nome": "Spotify Camp Nou e Museu do Barça",
            "tag": "Estádio em obras",
            "preco_val": "desde € 28",
            "preco_nota": "museu com “mirador das obras”; tour do campo não está à venda",
            "campos": [
                ("O que se vende hoje, e por quanto",
                 "Fonte: página de ingressos do museu no site oficial do clube "
                 "(fcbarcelona.com/en/tickets/museum), consultada em 18/out/2026. "
                 "<b>Todos os preços estão como “From”.</b><br>"
                 "<b>Museu: desde € 28</b>, com o <i>“Construction Viewpoint”</i> — o "
                 "mirante das obras.<br>"
                 "<b>Museu Flexível: desde € 38</b>, sem data, <i>“Valid until "
                 "02/28/2027”</i>.<br>"
                 "<b>Spotify Camp Nou Experience: desde € 69</b>, com vista panorâmica "
                 "do estádio. Match Day Tour: € 149. Barça Sky Tour: € 214.<br>"
                 "<b>O tour clássico do estádio, com vestiário e beira do gramado, não "
                 "está na lista</b> da página consultada. O que existe é museu mais "
                 "mirante.<br>"
                 "<b>Preço de criança não está separado</b> na página."),
                ("O estado das obras",
                 FLAG % "Só em fonte secundária" +
                 "<b>o site do clube não publica, na página de ingressos, um calendário "
                 "das obras.</b> O que a imprensa esportiva registrava em agosto de "
                 "2026: o estádio voltou a receber jogos em 16 de agosto de 2026, com "
                 "<b>62.652 lugares</b> (fase 1C); o terceiro anel foi adiado para o "
                 "<b>início de 2027</b>; e a cobertura nova começa a ser instalada em "
                 "<b>junho de 2027</b>, obra de quatro a cinco meses durante a qual o "
                 "estádio não receberia jogos. <b>Nada disso é oficial do clube</b>, e "
                 "muda a cada mês. Para quem vai pelo estádio, confira a semana da "
                 "viagem."),
                ("Horário",
                 FLAG % "Lacuna declarada" +
                 "<b>a página de ingressos não publica o horário do museu</b>; manda "
                 "para uma seção de informação prática que devolveu erro 404 à "
                 "consulta. Sites de venda de terceiros falam em 10h às 18h de "
                 "segunda a sábado no inverno, <b>sem confirmação oficial aqui</b>."),
                ("Onde fica",
                 mapa("Spotify Camp Nou, Carrer d'Arístides Maillol 12, 08028 Barcelona, Espanha")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem, e a taxa que dobrou",
            "tag": "Conta, não lugar",
            "preco_val": "€ 179,45",
            "preco_nota": "média de 12 meses por quarto; mais € 7 por pessoa por noite de taxa",
            "campos": [
                ("A diária: a fonte, e o que o número é",
                 "Fonte: <b>INE</b> (Instituto Nacional de Estadística de Espanha), "
                 "<i>Indicadores de Rentabilidad del Sector Hotelero</i>, <b>tabela "
                 "46298</b> — tarifa média diária (ADR) por <b>ponto turístico</b>, "
                 "série <i>Barcelona, total de categorias</i>, lida pela API do INE em "
                 "29/out/2026.<br>"
                 "<b>É por quarto ocupado, por noite, e não por pessoa</b>, e cobre "
                 "<b>hotéis</b>, não apartamentos.<br>"
                 "<b>Os € 179,45 são a média dos 12 meses de outubro de 2025 a setembro "
                 "de 2026.</b> Os doze valores são do INE; <b>a média é cálculo "
                 "nosso</b>.<br>"
                 "Os doze, para você conferir: out/2025 € 190,29 · nov/2025 € 155,67 · "
                 "<b>dez/2025 € 131,41</b> · jan/2026 € 135,13 · fev/2026 € 153,00 · "
                 "mar/2026 € 188,47 · abr/2026 € 193,14 · <b>mai/2026 € 223,37</b> · "
                 "jun/2026 € 214,34 · jul/2026 € 186,09 · ago/2026 € 175,42 · "
                 "set/2026 € 207,03.<br>"
                 "<b>Maio é o mês mais caro e dezembro o mais barato: 70% de diferença "
                 "pelo mesmo quarto.</b> Barcelona não tem o agosto ao contrário de "
                 "Granada: agosto fica perto da média."),
                ("A taxa turística, que dobrou em 1º de abril de 2026",
                 "Fonte: <b>Agència Tributària de Catalunya</b>, página <i>Quota "
                 "tributària, tarifes i recàrrecs municipals</i> do IEET "
                 "(atc.gencat.cat), consultada em 18/out/2026 — tabela em vigor de "
                 "<b>01.04.2026 a 31.03.2027</b>, por pessoa e por noite, na cidade de "
                 "Barcelona:<br>"
                 "<b>Hotel de 1 a 3 estrelas, hostal, pensão (“resta d'establiments”): "
                 "€ 2,00 + recargo municipal € 5,00 = € 7,00.</b><br>"
                 "Hotel 4 estrelas: € 3,40 + € 5,00 = <b>€ 8,40</b>.<br>"
                 "Hotel 5 estrelas e gran luxo: € 7,00 + € 5,00 = <b>€ 12,00</b>.<br>"
                 "Apartamento turístico (HUT): € 4,50 + € 5,00 = <b>€ 9,50</b>.<br>"
                 "Albergue: € 1,00 + € 5,00 = <b>€ 6,00</b>.<br>"
                 "<b>Teto de 7 noites</b> por pessoa no mesmo estabelecimento; "
                 "<b>menor de 17 anos não paga</b>.<br>"
                 "<b>Quatro noites num três estrelas: € 28 por pessoa</b>, fora do preço "
                 "do quarto — mais que Picasso e MNAC somados. A mudança veio da "
                 "<b>Llei 2/2026, de 6 de março</b>, publicada no DOGC em 10/3/2026."),
                ("O aumento já está marcado — e a regra para travar o valor",
                 "<b>A tabela da ATC já publica o recargo de Barcelona dos próximos "
                 "anos: € 6,00 a partir de 01.04.2027 e € 7,00 a partir de "
                 "01.04.2028.</b> Um três estrelas passa a € 8 e depois € 9 por "
                 "noite.<br>"
                 "<b>E a página diz qual tarifa vale na reserva antecipada:</b> a do "
                 "momento da reserva, <i>desde que o valor da reserva, o imposto e o "
                 "recargo sejam pagos nesse momento</i>. <b>Quem paga tudo antes de "
                 "1º de abril de 2027 trava o recargo em € 5</b>, mesmo dormindo "
                 "depois. Reserva só com pré-autorização de cartão não trava nada."),
            ],
        },
    ],
}

DESTINOS = [BARCELONA]
