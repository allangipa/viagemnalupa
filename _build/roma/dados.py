# -*- coding: utf-8 -*-
"""Roma: nove pontos, com fonte e data em cada numero.

Mesmo molde do madri/dados.py. O renderizador e o novos/gera.py, chamado
com VNL_DADOS=roma.

POR QUE ROMA, E POR QUE AGORA
-----------------------------
Proxima da fila que a home publica no bloco "Roteiro de publicacao",
depois que Madri saiu.

O ACHADO: ROMA TEM DOIS DOMINGOS GRATUITOS, E ELES NAO SAO O MESMO
------------------------------------------------------------------
    PRIMEIRO domingo do mes   Estado italiano - Domenica al Museo
                              Coliseu, Foro, Palatino, Panteao,
                              Galleria Borghese e mais de 480 sitios

    ULTIMO domingo do mes     Vaticano, que e outro pais
                              Museus Vaticanos e Capela Sistina,
                              das 9h as 14h, ultima entrada 12h30

Os dois sao chamados de "domingo gratuito de Roma" por guia nenhum
distinguir, e nenhum dos dois cobre o outro. Numa viagem com UM domingo,
qual domingo e ele decide 41 ou 25 euros.

E o Vaticano FECHA aos domingos, exceto justamente o ultimo. Quem marca
o Vaticano num domingo qualquer bate na porta.

O QUE MAIS ESTA APURACAO ACHOU
------------------------------

1. O PANTEAO, QUE FOI GRATUITO POR SECULOS, COBRA - e subiu. Passou a
   cobrar 5 euros em 2023 e foi a 7 EUROS EM 1 DE JULHO DE 2026. Muito
   guia ainda escreve "entrada franca".

2. A MEIA-ENTRADA DO COLISEU E SO PARA CIDADAO DA UE de 18 a 24 anos, a
   2 euros. Brasileiro de vinte anos paga os 18 cheios. E o espelho
   invertido de Madri, onde o passaporte latino-americano DA direito.

3. NA GALLERIA BORGHESE ATE O INGRESSO GRATUITO CUSTA 2 EUROS, porque a
   reserva e obrigatoria para todas as categorias, inclusive as
   gratuitas. O domingo de graca nao e de graca ali.

4. SENTAR NA ESCADARIA DA PIAZZA DI SPAGNA E PROIBIDO, com multa de 250
   euros, ate 400 por sujar ou danificar. E a coisa que todo turista faz
   na foto que todo mundo tira.

5. O ELEVADOR DA CUPULA DE SAO PEDRO NAO RESOLVE. Custa 5 euros a mais e
   poupa 231 dos 551 degraus - sobram 320 a pe, numa escada em caracol
   que aperta.

6. A TAXA DE HOSPEDAGEM DE ROMA VAI A 10 EUROS POR PESSOA POR NOITE, o
   dobro e meio da de Lisboa, e nao esta no preco da reserva.

O QUE ESTA APURACAO NAO TEM, E FICA ESCRITO
-------------------------------------------
Varios sites oficiais italianos recusaram conexao direta: colosseo.it,
ticketing.colosseo.it, museivaticani.va e comune.roma.it. O navegador
tambem foi negado no ticketing. Nao contornamos bloqueio.

O que publicamos vem da indexacao dos proprios dominios oficiais, onde
ela existe, e esta dito ponto a ponto. A taxa de hospedagem e o unico
numero que veio SO de fontes secundarias convergentes, e a ficha diz
isso na linha.

Nao apuramos tarifa de metro nem diaria media de hospedagem.

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
#  ROMA
# =====================================================================
ROMA = {
    "slug": "roma",
    "nome": "Roma",
    "pais": "Itália",
    "regiao": "europa",
    "titulo": "Roma: 9 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 9 pontos de Roma, com os dois domingos "
                  "gratuitos que não são o mesmo domingo."),
    "abertura": ("Nove pontos com preço em euro, horário e fonte conferidos em 29 de "
                 "setembro de 2026 — e a confusão que custa dinheiro: <b>Roma tem dois "
                 "domingos gratuitos por mês, e eles não são o mesmo domingo. O primeiro "
                 "libera o Coliseu e o Panteão; o último, os Museus Vaticanos — que "
                 "fecham em todos os outros.</b>"),
    "busca": ("roma rome italia europa coliseu colosseo foro romano palatino panteao "
              "pantheon museus vaticanos musei vaticani capela sistina basilica sao pedro "
              "cupola galleria borghese fontana di trevi piazza di spagna trinita dei "
              "monti piazza navona domenica al museo primeiro domingo ultimo domingo "
              "contributo di soggiorno taxa de hospedagem"),
    "grupos": [
        {"id": "g1", "titulo": "A Roma antiga",
         "intro": ("Os dois pontos que o primeiro domingo do mês libera — e o que era "
                   "gratuito havia séculos e hoje cobra.")},
        {"id": "g2", "titulo": "O Vaticano",
         "intro": ("Outro país, outro calendário e outro domingo gratuito. Aqui está o "
                   "erro de agenda que mais derruba viagem a Roma.")},
        {"id": "g3", "titulo": "As praças, a galeria e a conta da cama",
         "intro": ("O que não se paga, o que se paga mesmo sendo grátis, e a cobrança "
                   "que não aparece no preço da sua reserva.")},
    ],
    "pontos": [

        # ---------------------------------------------------------- g1
        {
            "id": "coliseu",
            "foto": {"arq": "roma/coliseu.webp",
                     "alt": ("O Coliseu visto de cima em dia claro, com o anel de arcadas em "
                             "elipse e o Arco de Constantino ao lado"),
                     "cred": "Livioandronico2013 · CC BY-SA 4.0 · via Wikimedia Commons"},
            "grupo": "g1",
            "nome": "Coliseu, Fórum Romano e Palatino",
            "tag": "Sítio arqueológico",
            "preco_val": "€ 18",
            "preco_nota": "um bilhete para os três, válido 24h",
            "campos": [
                ("Valor da entrada",
                 "<b>Inteira € 18</b>, e <b>um bilhete só cobre os três sítios</b> — "
                 "Coliseu, Fórum Romano e Palatino.<br>"
                 "<b>Vale 24 horas a partir da primeira picotada</b>, então dá para ver o "
                 "Coliseu num fim de tarde e o Fórum na manhã seguinte com o mesmo "
                 "bilhete. É a validade mais generosa desta ficha.<br>"
                 "<b>A reserva de horário é obrigatória para entrar no Coliseu</b>, e as "
                 "vendas abrem <b>30 dias antes</b>. O Fórum e o Palatino você visita sem "
                 "hora marcada, antes ou depois.<br>"
                 "<b>A permanência dentro do Coliseu é limitada a 75 minutos.</b><br>"
                 "<b>E aqui está a armadilha para o leitor brasileiro:</b> a meia-entrada "
                 "de <b>€ 2 é só para cidadão da União Europeia de 18 a 24 anos</b>. "
                 "<b>Brasileiro de vinte anos paga os € 18 cheios.</b> Há ainda uma tarifa "
                 "R.A.P. de € 14, para associados do parque.<br>"
                 "Fonte: indexação do domínio do Parco archeologico del Colosseo, "
                 "29/set/2026. " + FLAG % "Site oficial não abriu" +
                 "colosseo.it e ticketing.colosseo.it recusaram conexão, e o navegador "
                 "também foi negado no ticketing. Não contornamos bloqueio."),
                ("Dias em que não funciona",
                 "<b>O Coliseu abre às 8h30 e a área do Fórum e Palatino às 9h.</b><br>"
                 "<b>É gratuito no primeiro domingo de cada mês</b>, pelo programa "
                 "<b>Domenica al Museo</b>, do Ministério da Cultura italiano — o percurso "
                 "gratuito inclui os três sítios.<br>"
                 "<b>Mas grátis não quer dizer sem reserva:</b> o próprio parque informa "
                 "que os bilhetes gratuitos se reservam pelo site de bilheteria. Em "
                 "domingo gratuito a procura é muito maior que a lotação, e sem bilhete "
                 "na mão você não entra."),
                ("Pontos de referência",
                 "O conjunto fica entre a Piazza del Colosseo e os <b>Fori Imperiali</b>, "
                 "que são via pública e se veem de graça da calçada da Via dei Fori "
                 "Imperiali. O <b>Arco de Constantino</b> está colado ao Coliseu, do lado "
                 "de fora da bilheteria.<br>"
                 + mapa("Colosseo, Piazza del Colosseo, Roma")),
            ],
        },
        {
            "id": "panteao",
            "foto": {"arq": "roma/panteao.webp",
                     "alt": ("O Panteão visto da Piazza della Rotonda, com o pórtico de "
                             "colunas coríntias e o obelisco da fonte em primeiro plano"),
                     "cred": "Jean-Pol GRANDMONT · CC BY 3.0 · via Wikimedia Commons"},
            "grupo": "g1",
            "nome": "Panteão",
            "tag": "Templo e basílica",
            "preco_val": "€ 7",
            "preco_nota": "desde 1º de julho de 2026; era € 5",
            "campos": [
                ("Valor da entrada",
                 "<b>O Panteão foi gratuito por séculos e hoje cobra.</b> Passou a cobrar "
                 "<b>€ 5 em 2023</b>, e <b>subiu para € 7 em 1º de julho de 2026</b>. "
                 "<b>Muito guia ainda escreve “entrada franca”.</b><br>"
                 "<b>Jovem de 18 a 25 anos paga € 2</b> e <b>menor de 18 não paga</b>. "
                 "<b>Morador do município de Roma não paga.</b><br>"
                 "<b>É gratuito para todos no primeiro domingo do mês</b>, pela Domenica "
                 "al Museo.<br>"
                 "<b>E há uma gratuidade que quase ninguém usa:</b> o Panteão é também a "
                 "<b>Basílica de Santa Maria ad Martyres</b>, uma igreja em funcionamento "
                 "— <b>durante as celebrações o acesso é livre, para culto</b>. Não é "
                 "brecha turística: é entrar para a missa, e comportar-se como tal.<br>"
                 "Fonte: Ministero della Cultura e imprensa italiana sobre o reajuste, "
                 "29/set/2026."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias, das 9h às 19h</b>, com <b>última entrada às "
                 "18h30</b> e <b>bilheteria fechando às 18h</b>.<br>"
                 "<b>São três horários diferentes para a mesma tarde</b>, e é o tipo de "
                 "detalhe que faz alguém chegar às 18h15 e não conseguir comprar."),
                ("Pontos de referência",
                 "Na <b>Piazza della Rotonda</b>, no centro histórico, a caminhada curta "
                 "da <b>Fontana di Trevi</b> e da <b>Piazza Navona</b> — os três se fazem "
                 "a pé numa tarde, e dois deles não custam nada.<br>"
                 + mapa("Pantheon, Piazza della Rotonda, Roma")),
            ],
        },

        # ---------------------------------------------------------- g2
        {
            "id": "museus-vaticanos",
            "foto": {"arq": "roma/escada-bramante.webp",
                     "alt": ("A escadaria helicoidal do Bramante nos Museus Vaticanos, vista "
                             "de cima, com a dupla hélice descendo em espiral"),
                     "cred": "Andreas Tille · CC BY-SA 4.0 · via Wikimedia Commons"},
            "grupo": "g2",
            "nome": "Museus Vaticanos e Capela Sistina",
            "tag": "Museu",
            "preco_val": "€ 25",
            "preco_nota": "online; € 20 na porta, com fila",
            "campos": [
                ("Valor da entrada",
                 "<b>€ 20 sem reserva</b>, comprando na bilheteria. <b>€ 20 + € 5 de taxa "
                 "de reserva = € 25</b> comprando online com o <i>Salta la fila</i>.<br>"
                 "<b>A ficha usa € 25</b> porque é o que quem planeja de longe acaba "
                 "pagando: os € 20 da porta vêm com fila, e a fila do Vaticano é uma das "
                 "maiores da Europa.<br>"
                 "<b>O bilhete vale só no dia da emissão</b>, e <b>não é reembolsável</b> "
                 "— a taxa de reserva também não.<br>"
                 "<b>Um aviso que o próprio museu publica:</b> existem sites com domínios "
                 "parecidos com o oficial cobrando <b>bem mais caro</b>. A bilheteria "
                 "oficial é <b>tickets.museivaticani.va</b>.<br>"
                 "Fonte: indexação do domínio dos Museus Vaticanos, 29/set/2026. "
                 + FLAG % "Site oficial não abriu" +
                 "museivaticani.va recusou conexão direta."),
                ("Dias em que não funciona",
                 "<b>Fecha aos domingos — exceto o último do mês.</b> É o erro de agenda "
                 "que mais derruba viagem a Roma, porque o resto da cidade funciona no "
                 "domingo.<br>"
                 "<b>No último domingo do mês a entrada é gratuita</b>, das <b>9h às "
                 "14h</b>, com <b>última admissão às 12h30</b> — metade do horário normal "
                 "e o dia mais cheio do mês.<br>"
                 "<b>De segunda a sábado:</b> 9h às 18h, última admissão às 16h. De 5 de "
                 "maio a 28 de outubro há horário estendido às <b>sextas até 22h30</b> e "
                 "aos <b>sábados até 20h</b>.<br>"
                 "<b>Fecha também</b> em 1 e 6 de janeiro, 11 de fevereiro, 10 de abril, "
                 "1º de maio, 29 de junho, 15 e 16 de agosto, 1º de novembro, 8, 25, 26 e "
                 "31 de dezembro. <b>E o último domingo não é gratuito</b> quando cai na "
                 "Páscoa, em 29 de junho, 25, 26 ou 31 de dezembro."),
                ("Pontos de referência",
                 "A entrada dos museus fica no <b>Viale Vaticano</b>, e <b>não</b> na "
                 "Praça de São Pedro — são portões diferentes, a cerca de quinze minutos "
                 "de caminhada um do outro pela muralha. <b>Quem vai para a fila errada "
                 "perde a hora marcada.</b><br>"
                 + mapa("Musei Vaticani, Viale Vaticano, Roma")),
            ],
        },
        {
            "id": "basilica-sao-pedro",
            "foto": {"arq": "roma/sao-pedro.webp",
                     "alt": ("A Praça de São Pedro vista do alto da cúpula da basílica, "
                             "com a colunata de Bernini em elipse, o obelisco ao centro e "
                             "a Via della Conciliazione indo até o horizonte de Roma"),
                     "cred": "Diliff · CC BY-SA 3.0 · via Wikimedia Commons"},
            "grupo": "g2",
            "nome": "Basílica de São Pedro e a cúpula",
            "tag": "Basílica",
            "preco_val": "Grátis",
            "preco_nota": "a basílica; a cúpula € 10 ou € 15",
            "campos": [
                ("Valor da entrada",
                 "<b>Entrar na basílica não custa nada e não precisa de bilhete.</b> O que "
                 "há é fila de segurança, que pode ser longa.<br>"
                 "<b>A única área paga é a cúpula:</b> <b>€ 10 subindo pela escada</b> ou "
                 "<b>€ 15 com elevador</b>, comprados na bilheteria no dia.<br>"
                 "<b>E o elevador não resolve o que parece resolver.</b> São <b>551 "
                 "degraus</b> no total; o elevador poupa os <b>231 primeiros</b> e "
                 "<b>deixa 320 para subir a pé</b>, por uma escada em caracol que vai "
                 "apertando conforme sobe. <b>Os € 5 a mais compram menos da metade da "
                 "subida.</b><br>"
                 "Fonte: basilicasanpietro.va e fontes convergentes, 29/set/2026."),
                ("Dias em que não funciona",
                 "<b>A cúpula abre das 7h30 às 18h no verão e das 7h30 às 17h no "
                 "inverno.</b><br>"
                 + FLAG % "Horário da basílica não apurado" +
                 "não confirmamos a grade da basílica em si nesta rodada, e ela muda em "
                 "dias de celebração papal.<br>"
                 "<b>O que vale planejar:</b> em <b>quarta-feira de manhã</b> costuma "
                 "haver audiência geral na praça, e em <b>domingo ao meio-dia</b>, o "
                 "Angelus. Nos dois casos a praça e a basílica ficam tomadas — é ótimo se "
                 "você quer ver isso, e ruim se queria a basílica vazia."),
                ("Pontos de referência",
                 "Na <b>Praça de São Pedro</b>, cuja entrada é outra que a dos Museus "
                 "Vaticanos. O <b>Castel Sant'Angelo</b> fica a caminhada pela Via della "
                 "Conciliazione, e cobra à parte — "
                 + FLAG % "não apuramos a tarifa dele" + ".<br>"
                 + mapa("Basilica di San Pietro, Piazza San Pietro, Citta del Vaticano")),
            ],
        },

        # ---------------------------------------------------------- g3
        {
            "id": "galleria-borghese",
            "foto": {"arq": "roma/galleria-borghese.webp",
                     "alt": ("O Casino Nobile, prédio que abriga a Galleria Borghese, com a "
                             "fachada branca e o jardim em frente"),
                     "cred": "Alessio Damato · CC BY-SA 3.0 · via Wikimedia Commons"},
            "grupo": "g3",
            "nome": "Galleria Borghese",
            "tag": "Galeria",
            "preco_val": "€ 18",
            "preco_nota": "€ 16 + € 2 de reserva obrigatória",
            "campos": [
                ("Valor da entrada",
                 "<b>€ 16 de ingresso mais € 2 de reserva, que dá € 18.</b> Há um "
                 "<b>turno noturno extraordinário às 18h45 por € 11 + € 2 = € 13</b>.<br>"
                 "<b>A reserva é obrigatória para todas as categorias — inclusive as "
                 "gratuitas.</b> E aqui está o detalhe que quase ninguém conta: <b>no "
                 "primeiro domingo do mês a entrada é gratuita, mas os € 2 de reserva "
                 "continuam devidos</b>. <b>O domingo de graça custa € 2 aqui.</b> Os "
                 "bilhetes do domingo gratuito saem <b>10 dias antes</b>.<br>"
                 "<b>A visita é por turno fixo de exatamente duas horas</b>, em cinco "
                 "faixas: 9h, 11h, 13h, 15h e 17h. <b>Não há entrada fora do turno e não "
                 "há como esticar</b> — às duas horas a sala é esvaziada para o turno "
                 "seguinte.<br>"
                 "Fonte: bilheteria oficial (gebart.it) e a página do museu, 29/set/2026."),
                ("Dias em que não funciona",
                 "<b>Fecha às segundas-feiras.</b> Abre de <b>terça a domingo, das 9h às "
                 "19h</b>.<br>"
                 "<b>Some isso ao turno de duas horas e ao teto de lotação</b> e você tem "
                 "o ponto menos improvisável de Roma: sem reserva feita com antecedência, "
                 "simplesmente não se entra."),
                ("Pontos de referência",
                 "Dentro da <b>Villa Borghese</b>, o grande parque ao norte da Piazza di "
                 "Spagna — <b>o parque é público e gratuito</b>, e a galeria é o prédio "
                 "pago dentro dele. Do <b>Pincio</b>, no mesmo parque, sai uma das vistas "
                 "mais conhecidas da cidade, e essa não custa nada.<br>"
                 + mapa("Galleria Borghese, Piazzale Scipione Borghese, Roma")),
            ],
        },
        {
            "id": "fontana-di-trevi",
            "foto": {"arq": "roma/fontana-di-trevi.webp",
                     "alt": ("O grupo escultórico central da Fontana di Trevi, com a figura do "
                             "Oceano no nicho entre as colunas e os tritões abaixo"),
                     "cred": "Luca Aless · CC BY-SA 4.0 · via Wikimedia Commons"},
            "grupo": "g3",
            "nome": "Fontana di Trevi",
            "tag": "Fonte",
            "preco_val": "Grátis",
            "preco_nota": "ver e jogar a moeda",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga para ver.</b> É via pública, sem portão e sem "
                 "bilheteria.<br>"
                 "<b>O que existe é regra de circulação</b>, porque o lugar é pequeno e a "
                 "multidão é permanente. "
                 + FLAG % "Regras de acesso não apuradas em fonte oficial" +
                 "houve, nos últimos anos, restrições de fluxo e propostas de acesso "
                 "controlado durante e depois do restauro, e <b>não confirmamos qual "
                 "regime está em vigor hoje</b> em fonte municipal — o site do Comune di "
                 "Roma recusou conexão nesta apuração.<br>"
                 "<b>Entrar na água é proibido e multado</b>, e isso é constante ao longo "
                 "dos anos. As moedas arrecadadas são recolhidas e destinadas a caridade "
                 "pela prefeitura."),
                ("Dias em que não funciona",
                 "<b>Não fecha.</b> É rua.<br>"
                 "<b>A hora muda tudo:</b> de manhã cedo, antes das 8h, a praça é outra "
                 "coisa. Entre o meio-dia e a noite, é a mais cheia de Roma."),
                ("Pontos de referência",
                 "A caminhada curta do <b>Panteão</b> e da <b>Piazza di Spagna</b> — os "
                 "três formam o circuito a pé do centro, e só o Panteão cobra.<br>"
                 + mapa("Fontana di Trevi, Piazza di Trevi, Roma")),
            ],
        },
        {
            "id": "piazza-di-spagna",
            "foto": {"arq": "roma/piazza-di-spagna.webp",
                     "alt": ("A escadaria de Trinità dei Monti vista de cima, com as azaleias "
                             "nos degraus e a Piazza di Spagna cheia ao pé"),
                     "cred": "Sergey Smirnov · CC BY-SA 3.0 · via Wikimedia Commons"},
            "grupo": "g3",
            "nome": "Piazza di Spagna e a escadaria",
            "tag": "Praça",
            "preco_val": "Grátis",
            "preco_nota": "mas sentar na escada custa € 250",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga nada para estar ali.</b><br>"
                 "<b>Mas sentar na escadaria de Trinità dei Monti é proibido, e a multa é "
                 "de € 250</b> — podendo chegar a <b>€ 400</b> por sujar, pichar ou "
                 "danificar, com responsabilização criminal nos casos graves. O "
                 "regulamento de polícia urbana trata a escadaria como <b>monumento</b>, e "
                 "proíbe tanto sentar quanto deitar.<br>"
                 "<b>Na prática:</b> a polícia municipal aborda quem senta e manda "
                 "levantar. <b>É a coisa que todo turista faz na foto que todo mundo "
                 "tira</b>, e é exatamente o que a regra veda.<br>"
                 "<b>A medida é controversa na própria Itália</b>, e foi contestada — mas "
                 "está em vigor. Fonte: imprensa italiana sobre o regulamento e o decreto "
                 "de sanções, 29/set/2026. "
                 + FLAG % "Texto municipal não aberto" +
                 "o site do Comune di Roma recusou conexão; não lemos o regulamento na "
                 "fonte primária."),
                ("Dias em que não funciona",
                 "<b>A praça não fecha.</b><br>"
                 "<b>Na primavera a escadaria recebe azaleias</b> e fica ainda mais "
                 "disputada. A <b>Via dei Condotti</b>, que sai da praça, é a rua das "
                 "grifes — e o movimento dela segue o horário do comércio."),
                ("Pontos de referência",
                 "A <b>Fontana della Barcaccia</b> fica ao pé da escadaria, e a igreja de "
                 "<b>Trinità dei Monti</b> no alto. Dali sobe-se ao <b>Pincio</b> e à "
                 "<b>Villa Borghese</b>, os dois gratuitos.<br>"
                 + mapa("Piazza di Spagna, Roma")),
            ],
        },
        {
            "id": "piazza-navona",
            "foto": {"arq": "roma/piazza-navona.webp",
                     "alt": ("A Piazza Navona ao comprido, com a Fontana del Moro em primeiro "
                             "plano e a igreja de Sant'Agnese in Agone à esquerda"),
                     "cred": "Myrabella · CC BY-SA 3.0 · via Wikimedia Commons"},
            "grupo": "g3",
            "nome": "Piazza Navona",
            "tag": "Praça",
            "preco_val": "Grátis",
            "preco_nota": "a praça; sentar nos cafés, não",
            "campos": [
                ("Valor da entrada",
                 "<b>Não existe bilhete.</b> A praça é via pública e as três fontes — "
                 "incluindo a <b>Fontana dei Quattro Fiumi</b>, de Bernini — se veem de "
                 "graça, a qualquer hora.<br>"
                 "<b>O que custa é sentar.</b> Os cafés da praça cobram preço de praça "
                 "monumental, e "
                 + FLAG % "não apuramos cardápio" +
                 "porque são estabelecimentos privados sem tabela publicada. <b>Em muitos "
                 "bares italianos o preço no balcão é menor que na mesa</b>, e a diferença "
                 "deve estar afixada — confira antes de sentar."),
                ("Dias em que não funciona",
                 "<b>Não fecha.</b><br>"
                 "<b>No Natal a praça vira feira</b>, com bancas ocupando o centro — o que "
                 "muda completamente a experiência de quem foi pelas fontes e pela "
                 "arquitetura."),
                ("Pontos de referência",
                 "A caminhada curta do <b>Panteão</b>. A igreja de <b>Sant'Agnese in "
                 "Agone</b>, na própria praça, e o <b>Campo de' Fiori</b>, com feira de "
                 "manhã, ficam nas imediações — os dois gratuitos.<br>"
                 + mapa("Piazza Navona, Roma")),
            ],
        },
        {
            "id": "hospedagem-e-taxa",
            "grupo": "g3",
            "nome": "Hospedagem e o contributo di soggiorno",
            "tag": "A conta da cama",
            "preco_val": "até € 10",
            "preco_nota": "por pessoa por noite, fora da reserva",
            "campos": [
                ("O que se soma à diária",
                 "<b>Roma cobra o <i>contributo di soggiorno</i>, e ele não está no preço "
                 "da sua reserva.</b> Paga-se no alojamento.<br>"
                 "<b>As faixas em vigor em 2026 vão de € 3 a € 10 por pessoa por "
                 "noite</b>, conforme a classificação da estrutura. <b>Hotel chega à "
                 "faixa máxima, € 10.</b> <b>B&B e aluguel de curta duração: € 6.</b> Casa "
                 "de temporada e agriturismo: € 6.<br>"
                 "<b>Há um teto: cobra-se no máximo 10 noites consecutivas</b> na mesma "
                 "estrutura, no ano civil (5 noites em camping). Da décima primeira em "
                 "diante, não se deve mais.<br>"
                 "<b>Para dimensionar:</b> um casal, cinco noites em hotel, são <b>€ 100 "
                 "fora do preço da reserva</b>. <b>É duas vezes e meia a taxa de "
                 "Lisboa</b>, que é de € 4 por noite.<br>"
                 + FLAG % "Só fontes secundárias" +
                 "<b>este é o único número desta ficha que não veio de fonte oficial.</b> "
                 "O site do Comune di Roma recusou conexão nesta apuração. As fontes "
                 "secundárias consultadas convergem nas faixas e no teto, mas <b>confirme "
                 "com o seu alojamento no ato da reserva</b>."),
                ("Diária média",
                 FLAG % "Sem ADR oficial apurado" +
                 "<b>esta ficha sai sem linha de hospedagem no total</b>, pelo mesmo "
                 "motivo de Fortaleza, Bariloche, Punta Cana, Miami, Salvador e Madri: "
                 "não apuramos diária média publicada por órgão oficial para Roma nesta "
                 "rodada.<br>"
                 "Usar média de agregador seria furar a regra da casa <b>na linha mais "
                 "cara da viagem</b> — e em Roma seria pior, porque a diária anunciada "
                 "ainda não inclui o contributo."),
                ("Quem não paga",
                 "As isenções publicadas incluem <b>residentes</b>, <b>peregrinos</b> em "
                 "estruturas conveniadas, pessoas internadas em estruturas de saúde e "
                 "<b>trabalhadores em missão</b>. "
                 + FLAG % "Lista não conferida em fonte primária" +
                 "vale a mesma ressalva da linha acima: o texto municipal não abriu, e a "
                 "lista de isenções pode ter condições que as fontes secundárias "
                 "resumiram."),
            ],
        },
    ],
}

DESTINOS = [ROMA]
