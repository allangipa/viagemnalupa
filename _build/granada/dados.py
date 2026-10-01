# -*- coding: utf-8 -*-
"""Granada: o vigesimo destino, em dez pontos e tres grupos.

Mesmo molde do paris/dados.py.

O ACHADO PRINCIPAL: A ALHAMBRA TEM DOIS PRECOS OFICIAIS PARA O MESMO
INGRESSO, E NENHUM DOS DOIS E O QUE SE PAGA
--------------------------------------------------------------------
A Orden de 17 de julio de 2025, publicada no BOJA n. 142 de 25 de julho
de 2025 e em vigor desde 1 de agosto de 2025, fixa em LEI:

    Visita diurna general ................................. 21 EUR
    Visita diurna Jardines, Generalife, Partal, Alcazaba .. 12 EUR
    Visita nocturna a los Palacios Nazaries ............... 12 EUR
    Visita nocturna al Palacio del Generalife .............. 8 EUR
    Dobla de Oro General .................................. 23 EUR

A pagina de horarios e tarifas do PROPRIO Patronato publica, na mesma
data de consulta:

    Visita Diurna General ............................. 22,27 EUR
    Jardines y Palacio del Generalife ................. 12,73 EUR
    Visita Nocturna a Palacios Nazaries ............... 12,73 EUR
    Visita Nocturna a Jardines ......................... 8,48 EUR
    Dobla de Oro General .............................. 30,48 EUR

E a mesma pagina acrescenta: "A estos precios hay que anadir la comision
de servicio (para compras en la pagina web)".

Ou seja: a norma diz 21, o site diz 22,27 - 6,05% acima -, e o site diz
que AINDA se soma comissao. Alem disso o artigo 1.2 da ordem diz que
"los precios publicos ... se incrementaran en el impuesto sobre el valor
anadido". Nao publicamos reconciliacao inventada: dizemos o que cada
fonte diz e declaramos que o valor final nao esta publicado em lugar
nenhum.

A Dobla de Oro foge do padrao: 23 na lei contra 30,48 no site, 32,5% de
diferenca, nao 6%. A propria ordem explica por que, no artigo 4 - nos
produtos em colaboracao os precios "hacen referencia exclusivamente a la
parte correspondiente al Patronato". A linha diz isso.

O CAIXA OFICIAL NAO ABRIU, E ISSO FICA ESCRITO
-----------------------------------------------
tickets.alhambra-patronato.es responde com verificacao anti-bot
("Voight-Kampff Browser Test") e nao abriu nem por leitura de pagina nem
por navegador. NAO CONTORNAMOS PROTECAO ANTI-BOT. E a mesma lacuna que
Madri anotou no Prado e Sevilha no TUSSAM.

O SEGUNDO ACHADO: A QUARTA-FEIRA QUE NINGUEM CONTA
---------------------------------------------------
A Catedral de Granada e a Capilla Real tem visita cultural GRATUITA por
reserva nominativa, em dominio proprio da diocese
(entradasgratuitas.diocesisgranada.es), que nenhum guia que abrimos
menciona. Lemos as vagas no proprio seletor do formulario:

    Catedral      sessoes 15:15, 15:30, 16:00, 16:30
    Capilla Real  sessoes 15:15, 15:30, 16:30, 17:00

E as datas abertas na consulta de 30/set/2026:

    Catedral      2, 9 e 16 de dezembro de 2026
    Capilla Real  25 de novembro e 2, 9 e 16 de dezembro de 2026

TODAS QUARTAS-FEIRAS. Maximo duas entradas por pessoa e por dia, reserva
fecha 24 horas antes, exige DNI ou passaporte do solicitante, 15 minutos
de tolerancia, proibido fotografar. O calendario abre poucas datas por
vez - isso esta dito na linha, porque o leitor tem de conferir.

O TERCEIRO ACHADO: O MES AO CONTRARIO
--------------------------------------
O ADR do INE para a cidade de Granada diz que AGOSTO E O MES MAIS BARATO
do ano - 73,07 euros por quarto -, e OUTUBRO o mais caro - 122,46. E o
inverso do que se supoe de um destino europeu, e tem explicacao fisica:
Granada e Andaluzia interior, e em agosto faz calor demais. No mesmo
agosto, Malaga, na costa, cobra 163,05.

Junta-se ao calendario da Alhambra: em agosto o horario diurno e o longo
(08:30-20:00) e a visita noturna aos Palacios roda de terca a sabado, nao
so sexta e sabado. Cama mais barata, monumento mais aberto, calor
insuportavel. A ficha diz os tres.

O QUE ESTA APURACAO NAO TEM, E FICA ESCRITO
--------------------------------------------
    caixa da Alhambra       verificacao anti-bot; valor final nao
                            confirmado
    precos da Catedral      catedraldegranada.com nao publica tabela;
                            os valores vem do site de venda que a
                            PROPRIA catedral linka
                            (ticketsgranadacristiana.com)
    horario da Capilla Real nao publicado por dia da semana; o proprio
                            site pede "ROGAMOS QUE CONFIRMEN HORARIOS
                            PREVIAMENTE A LA VISITA", telefone
                            958 22 78 48
    tapa gratis             nao existe fonte oficial com regra nem com
                            valor; andalucia.org devolveu 403 a
                            conferencia direta. Nao entra como numero.
    dia gratuito para todos o artigo 9.2.c da ordem preve dia livre
                            semanal "que determine el Patronato", e NAO
                            achamos determinacao publicada para o
                            publico geral - so o programa de fim de
                            semana para residentes de Granada
    taxa turistica          nao ha na Andaluzia; negativo sem pagina
                            oficial para citar, como em Sevilha

Apuracao de 30 de setembro de 2026.
"""

APURACAO = "30 de setembro de 2026"
APURACAO_CURTA = "30/set/2026"

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
#  GRANADA
# =====================================================================
GRANADA = {
    "slug": "granada",
    "nome": "Granada",
    "pais": "Espanha",
    "regiao": "europa",
    "titulo": "Granada: 10 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 10 pontos de Granada, com a Alhambra que "
                  "tem dois preços oficiais diferentes para o mesmo ingresso."),
    "abertura": ("Dez pontos com preço em euro, horário e fonte conferidos em 30 de "
                 "setembro de 2026 — e duas coisas que não achamos em guia nenhum: "
                 "<b>a Alhambra tem dois preços oficiais para o mesmo ingresso — a lei "
                 "da Junta de Andalucía diz € 21, o site do próprio monumento diz "
                 "€ 22,27, e o site ainda avisa que a comissão se soma a isso. E a "
                 "Catedral e a Capilla Real têm visita gratuita por reserva, em "
                 "quartas-feiras à tarde, num site da diocese que ninguém cita.</b>"),
    "busca": ("granada espanha espana andaluzia andalucia europa alhambra generalife "
              "palacios nazaries alcazaba partal visita nocturna noturna dobla de oro "
              "catedral de granada capilla real reyes catolicos sacromonte abadia museo "
              "cuevas albaicin albaycin mirador de san nicolas silla del moro castillo "
              "de santa elena torres bermejas corral del carbon banuelo bañuelo casa "
              "horno de oro dar al-horra maristan monumentos andalusies museo de la "
              "alhambra palacio de carlos v entrada gratuita entradas gratuitas quarta "
              "feira miercoles domingo gratis tapa gratis hospedagem adr ine "
              "boja orden precios publicos nominativa intransferible"),
    "grupos": [
        {"id": "g1", "titulo": "O ingresso que decide a viagem",
         "intro": ("A Alhambra em três bilhetes diferentes — e as regras que fazem "
                   "perder o ingresso pago, que são mais duras do que em qualquer "
                   "outro ponto deste site.")},
        {"id": "g2", "titulo": "A Granada cristã, e a quarta-feira que ninguém conta",
         "intro": ("Catedral, Capilla Real e Sacromonte: quanto custam, onde o preço "
                   "está publicado de verdade, e a visita gratuita por reserva que não "
                   "aparece nos guias.")},
        {"id": "g3", "titulo": "O que não cobra, e a conta da cama",
         "intro": ("Quatro linhas em que a entrada é livre ou custa € 2 — incluindo um "
                   "museu dentro da Alhambra — e o mês em que a cama de Granada é a "
                   "mais barata do ano.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - o ingresso que decide a viagem
        # =============================================================
        {
            "id": "alhambra-diurna",
            "grupo": "g1",
            "nome": "Alhambra e Generalife: visita diurna geral",
            "tag": "Palácio e fortaleza",
            "preco_val": "€ 22,27",
            "preco_nota": "a lei diz € 21; e a comissão ainda se soma",
            "campos": [
                ("Valor da entrada, e por que há mais de um",
                 "Fontes: <b>Orden de 17 de julio de 2025</b>, publicada no "
                 "<b>BOJA nº 142 de 25/jul/2025</b> e em vigor desde <b>1º de agosto de "
                 "2025</b>; e a página de horários e tarifas do site oficial "
                 "(alhambra-patronato.es), consultada em 30/set/2026.<br>"
                 "<b>Este é o único ponto deste site em que a lei e o site do próprio "
                 "monumento publicam preços diferentes para o mesmo ingresso.</b><br>"
                 "<b>A ordem fixa € 21.</b> É o preço público, em norma legal.<br>"
                 "<b>O site do Patronato publica € 22,27</b> — <b>6,05% acima</b>.<br>"
                 "E a mesma página acrescenta: <i>“A estos precios hay que añadir la "
                 "comisión de servicio (para compras en la página web)”</i> — a comissão "
                 "se soma <b>aos € 22,27</b>, não aos € 21.<br>"
                 "Ainda há uma terceira camada: o <b>artigo 1.2</b> da ordem diz que os "
                 "preços públicos <i>“se incrementarán en el impuesto sobre el valor "
                 "añadido”</i>, e o <b>artigo 2</b> diz que a venda antecipada "
                 "<i>“se incrementarán con la comisión de gestión establecida en el "
                 "contrato de servicio”</i>.<br>"
                 "<b>Não inventamos a conta que junta tudo isso.</b> Orçamente "
                 "<b>€ 22,27 como piso</b>, não como valor final."),
                ("Fonte que não abriu",
                 FLAG % "Lacuna declarada" +
                 "<b>o caixa oficial não abriu para conferência.</b> "
                 "tickets.alhambra-patronato.es responde com verificação anti-bot — a "
                 "página se identifica como <i>“Voight-Kampff Browser Test”</i> — e não "
                 "abriu nem por leitura direta nem por navegador. "
                 "<b>Não contornamos proteção anti-bot.</b><br>"
                 "Então <b>o valor que aparece no fim da compra não está confirmado "
                 "aqui</b>. É a mesma lacuna que este site anotou no Museo del Prado, em "
                 "Madri, e no TUSSAM, em Sevilha."),
                ("A regra que faz perder o ingresso pago",
                 "<b>Esta é a ficha mais rígida deste site, e vale ler antes de "
                 "comprar.</b><br>"
                 "<b>O ingresso é nominativo.</b> O site oficial diz: <i>“Sí, la entrada "
                 "es nominativa, así como personal e intransferible”</i>. Exige "
                 "<b>documento de identidade original</b>, e há conferência de "
                 "identidade na entrada.<br>"
                 "<b>Não há devolução.</b> <i>“Cualquier compra de entradas tiene "
                 "carácter definitivo y firme”</i> — e <b>data e hora não podem ser "
                 "alteradas</b>.<br>"
                 "<b>Os Palacios Nazaríes têm hora marcada: 300 pessoas a cada meia "
                 "hora.</b> E o site é explícito sobre o atraso: <i>“Transcurrido dicho "
                 "turno horario, se perderá el derecho a la visita de este espacio”</i>. "
                 "<b>Perder o turno é perder os palácios</b>, que são a razão da "
                 "visita — o resto do bilhete continua valendo.<br>"
                 "<b>Troca de nome só a partir de 5 ingressos</b>, só se ainda não "
                 "tiverem sido impressos, e até o dia anterior."),
                ("Dias e horários",
                 "<b>15 de outubro a 31 de março: 8h30 às 18h.</b><br>"
                 "<b>1º de abril a 14 de outubro: 8h30 às 20h.</b><br>"
                 "<b>Fecha em 25 de dezembro e 1º de janeiro.</b>"),
                ("Quem não paga, e quem você talvez pense que paga menos",
                 "Pelo <b>artigo 9 da ordem</b>:<br>"
                 "<b>Menor de 12 anos não paga</b>, em qualquer modalidade e qualquer "
                 "canal de venda — <b>sem restrição de nacionalidade</b>. Mas precisa de "
                 "ingresso emitido, tirado junto com os dos adultos.<br>"
                 "Também não pagam membros do <b>ICOMOS</b> e do <b>ICOM</b>, guias "
                 "oficiais de turismo em exercício, professores acompanhando alunos de "
                 "centros da UE, e jornalistas em exercício com autorização prévia.<br>"
                 "<b>16 de novembro</b>, Dia Internacional do Patrimônio Mundial, é "
                 "gratuito para todos nos espaços que o Patronato determinar.<br>"
                 "<b>A tarifa reduzida de € 14 provavelmente não é sua.</b> Ela vale "
                 "para maior de 65 anos <b>da União Europeia</b>, portador do Carné "
                 "Joven e pessoa com deficiência de 33% ou mais. <b>Brasileiro com mais "
                 "de 65 anos paga a tarifa cheia.</b>"),
                ("O dia grátis que a norma prevê e não achamos",
                 FLAG % "Lacuna declarada" +
                 "o <b>artigo 9.2.c</b> da ordem prevê entrada gratuita para "
                 "<i>“todos los visitantes”</i> no dia ou dias da semana não feriados e "
                 "no horário <i>“que determine el Patronato”</i>.<br>"
                 "<b>Não achamos essa determinação publicada para o público geral.</b> O "
                 "que o Patronato publica é o programa de fim de semana <b>para "
                 "residentes na província de Granada</b>, com reserva e comprovação de "
                 "residência — <b>o que não serve para quem vem de fora</b>.<br>"
                 "A previsão existe na norma. A data, não encontramos."),
                ("Onde fica",
                 mapa("Alhambra, Calle Real de la Alhambra, 18009 Granada, Espanha")),
            ],
        },
        {
            "id": "generalife",
            "grupo": "g1",
            "nome": "Jardines y Palacio del Generalife",
            "tag": "Jardins",
            "preco_val": "€ 12,73",
            "preco_nota": "a lei diz € 12; não entra nos Palacios Nazaríes",
            "campos": [
                ("O que é, e o que ele não é",
                 "Fontes: a mesma <b>Orden de 17 de julio de 2025</b> e a página oficial "
                 "de horários e tarifas, consultada em 30/set/2026.<br>"
                 "<b>É o bilhete barato da Alhambra, e a economia tem um preço que muita "
                 "gente descobre no portão.</b><br>"
                 "Ele dá <b>Jardines, Generalife, Partal e Alcazaba</b> — e "
                 "<b>não dá os Palacios Nazaríes</b>, que são os pátios dos Leões e de "
                 "Comares, a arquitetura que faz a Alhambra ser a Alhambra.<br>"
                 "<b>A ordem fixa € 12. O site publica € 12,73</b> — a mesma diferença "
                 "de 6% do bilhete geral, com a mesma advertência de comissão por "
                 "cima.<br>"
                 "<b>A diferença para o bilhete completo é de € 9,54</b> no preço do "
                 "site. É o que custa ver os palácios."),
                ("Reduzida, e os pedaços vendidos separados",
                 "<b>Reduzida: € 8</b> pela ordem — e vale para os mesmos grupos do "
                 "bilhete geral, ou seja, maior de 65 <b>da União Europeia</b>, Carné "
                 "Joven e deficiência de 33% ou mais.<br>"
                 "A ordem também prevê os pedaços soltos, a <b>€ 8</b> cada: "
                 "<b>Jardines, Partal e Palacio del Generalife</b>, ou <b>Alcazaba</b> "
                 "isolada. <b>Reduzida de cada pedaço: € 6.</b><br>"
                 "Somar dois pedaços a € 8 dá € 16 e fica <b>mais caro que o bilhete de "
                 "€ 12,73 que já traz os dois</b>."),
                ("Dias e horários",
                 "<b>Os mesmos da visita diurna geral:</b> 8h30 às 18h de 15 de outubro "
                 "a 31 de março, e 8h30 às 20h de 1º de abril a 14 de outubro.<br>"
                 "<b>Fecha em 25 de dezembro e 1º de janeiro.</b>"),
                ("Onde fica",
                 mapa("Generalife, Calle Real de la Alhambra, 18009 Granada, Espanha")),
            ],
        },
        {
            "id": "alhambra-noturna",
            "grupo": "g1",
            "nome": "Alhambra: as visitas noturnas",
            "tag": "Visita noturna",
            "preco_val": "€ 12,73",
            "preco_nota": "Palacios Nazaríes; só jardins € 8,48",
            "campos": [
                ("Valor da entrada",
                 "Fontes: a <b>Orden de 17 de julio de 2025</b> e a página oficial de "
                 "horários e tarifas, consultada em 30/set/2026.<br>"
                 "<b>Visita noturna aos Palacios Nazaríes:</b> a ordem fixa <b>€ 12</b>, "
                 "o site publica <b>€ 12,73</b>. Reduzida de <b>€ 8</b>.<br>"
                 "<b>Visita noturna aos Jardines del Generalife:</b> a ordem fixa "
                 "<b>€ 8</b>, o site publica <b>€ 8,48</b>. Reduzida de <b>€ 6</b>.<br>"
                 "<b>A noturna dos palácios custa quase a metade da diurna geral</b> "
                 "(€ 12,73 contra € 22,27) — e entra no mesmo espaço que é a razão da "
                 "visita. O que ela não dá é o resto do conjunto, que fecha de dia."),
                ("O calendário, que é o verdadeiro preço desta linha",
                 "<b>Aqui o mês importa mais que o valor.</b><br>"
                 "<b>Palacios Nazaríes, 15 de outubro a 31 de março: sexta e sábado, "
                 "20h às 21h30</b> — bilheteria 19h às 20h45.<br>"
                 "<b>Palacios Nazaríes, 1º de abril a 14 de outubro: terça a sábado, 22h "
                 "às 23h30</b> — bilheteria 21h às 22h45.<br>"
                 "<b>No inverno são duas noites por semana; no verão, cinco.</b> Quem vai "
                 "em novembro e quer a noturna tem de encaixar a viagem numa sexta ou "
                 "num sábado."),
                ("A noturna dos jardins fecha justamente no verão",
                 "<b>1º de abril a 31 de maio: terça a sábado, 22h às 23h30.</b><br>"
                 "<b>1º de setembro a 14 de outubro: terça a sábado, 22h às 23h30.</b><br>"
                 "<b>15 de outubro a 14 de novembro: sexta e sábado, 20h às 21h30.</b><br>"
                 "<b>Junho, julho e agosto não aparecem na tabela. Nem 15 de novembro a "
                 "31 de março.</b><br>"
                 "É o contrário do que se espera: <b>a noite de jardim não existe em "
                 "pleno verão</b>, que é quando a noite é mais agradável em Granada. "
                 "A noturna dos palácios, essa sim, roda o verão inteiro."),
                ("A mesma regra dura",
                 "<b>Valem aqui as mesmas regras do bilhete diurno:</b> nominativo, "
                 "pessoal, intransferível, documento original na entrada, sem devolução "
                 "e sem troca de data ou hora. E <b>o turno dos Palacios Nazaríes "
                 "continua sendo de meia hora</b> — perder o horário é perder o espaço."),
                ("Onde fica",
                 mapa("Alhambra, Calle Real de la Alhambra, 18009 Granada, Espanha")),
            ],
        },
        # =============================================================
        #  g2 - a Granada crista, e a quarta-feira
        # =============================================================
        {
            "id": "catedral",
            "grupo": "g2",
            "nome": "Catedral de Granada",
            "tag": "Catedral",
            "preco_val": "€ 10",
            "preco_nota": "e há visita gratuita por reserva; veja abaixo",
            "campos": [
                ("Valor da entrada, e onde ele está publicado de verdade",
                 FLAG % "Fonte oficial indireta" +
                 "<b>o site da catedral não publica tabela de preços.</b> "
                 "catedraldegranada.com diz apenas <i>“Ahora puede comprar online su "
                 "ticket o entrada a la Catedral de Granada”</i> e manda para o site de "
                 "venda.<br>"
                 "<b>O valor vem desse site de venda, que é o que a própria catedral "
                 "indica</b> — ticketsgranadacristiana.com, consultado em 30/set/2026: "
                 "<b>€ 10,00</b>, visita de cerca de 60 minutos.<br>"
                 "Não é número de agregador: é o canal oficial de venda da catedral. Mas "
                 "<b>não é a página da catedral</b>, e isso fica dito."),
                ("A visita gratuita que não está em guia nenhum",
                 "<b>A catedral tem visita cultural gratuita, por reserva nominativa, "
                 "num domínio próprio da diocese</b> — "
                 "entradasgratuitas.diocesisgranada.es, conferido em 30/set/2026.<br>"
                 "<b>As sessões são à tarde: 15h15, 15h30, 16h e 16h30.</b><br>"
                 "<b>As datas abertas na nossa consulta eram 2, 9 e 16 de dezembro de "
                 "2026 — todas quartas-feiras.</b><br>"
                 "<b>O calendário abre poucas datas por vez</b>, então confira antes de "
                 "montar o dia em cima disso. O que apuramos é que <b>o esquema "
                 "existe</b> e <b>cai em quarta à tarde</b>."),
                ("As regras da gratuita, que são apertadas",
                 "Das condições gerais do próprio site de reservas:<br>"
                 "<b>“Una misma persona sólo podrá retirar, como máximo, dos entradas "
                 "gratuitas para un mismo día.”</b> — duas por pessoa, por dia.<br>"
                 "<b>É nominativa</b> e só vale <i>“previa presentación del DNI del "
                 "solicitante”</i>.<br>"
                 "<b>“El periodo de reservas finalizará 24 horas antes de la visita.”</b> "
                 "— não dá para decidir na hora.<br>"
                 "<b>Tolerância de 15 minutos</b> de atraso.<br>"
                 "<b>Proibido fotografar e gravar</b>, e celular tem de ficar "
                 "desligado.<br>"
                 "<b>Não vale para grupos</b> e <b>não inclui audioguia</b> — que o "
                 "bilhete pago inclui.<br>"
                 "E o aviso que explica tudo: <b>“Los horarios y días de visita, pueden "
                 "verse alterados por necesidades de culto religioso.”</b>"),
                ("O bilhete das seis igrejas, e a conta que fecha",
                 "O mesmo site de venda oferece um <b>combinado de seis templos por "
                 "€ 33,00</b>, anunciado como <i>“Ahorra hasta un 19,5%”</i>.<br>"
                 "<b>Conferimos a conta somando os seis avulsos:</b> Catedral € 10, "
                 "Capilla Real € 7, Abadía del Sacromonte € 7, Real Monasterio de San "
                 "Jerónimo € 7, Monasterio de la Cartuja € 7 e Iglesia y torre de San "
                 "Nicolás € 3. <b>Dá exatamente € 41.</b><br>"
                 "<b>€ 33 contra € 41 são € 8 de economia, ou 19,5%</b> — o desconto "
                 "anunciado confere.<br>"
                 "<b>Mas conferimos quando ele compensa de verdade, e a resposta é mais "
                 "estreita que o anúncio sugere.</b><br>"
                 "<b>Com quatro templos ou menos, nunca compensa</b> — os quatro mais "
                 "caros somam € 31, abaixo dos € 33.<br>"
                 "<b>Com cinco, depende de quais cinco.</b> Se a Catedral estiver fora, "
                 "os outros cinco somam € 31 e o combinado continua perdendo. Se ela "
                 "estiver dentro, o combinado ganha — por € 1 a € 5, dependendo do que "
                 "você cortar.<br>"
                 "<b>Só nos seis a economia é os € 8 anunciados.</b><br>"
                 "Na prática: Catedral mais Capilla Real mais Sacromonte, que é o "
                 "roteiro realista de quem tem dois dias, dá <b>€ 24 avulso — € 9 mais "
                 "barato que o combinado</b>."),
                ("Horários",
                 FLAG % "Lacuna declarada" +
                 "<b>a visita acontece durante todo o ano, exceto em horário de culto e "
                 "outras celebrações religiosas</b> — é o que o site diz. "
                 "<b>Não publica grade por dia da semana</b> em página citável, e "
                 "publica apenas horários especiais de dezembro e janeiro.<br>"
                 "Telefone de confirmação no próprio site: <b>958 22 29 59</b>."),
                ("Onde fica",
                 mapa("Catedral de Granada, Calle Gran Vía de Colón 5, 18001 Granada, Espanha")),
            ],
        },
        {
            "id": "capilla-real",
            "grupo": "g2",
            "nome": "Capilla Real",
            "tag": "Capela e museu",
            "preco_val": "€ 7",
            "preco_nota": "gratuita por reserva em quartas; horário não publicado",
            "campos": [
                ("O que é, e o valor",
                 "<b>É onde estão os túmulos de Isabel de Castela e Fernando de "
                 "Aragão</b>, os Reis Católicos — os mesmos que assinaram a rendição de "
                 "Granada em 1492. Fica colada à catedral, e é bilhete separado.<br>" +
                 FLAG % "Fonte oficial indireta" +
                 "<b>o site da Capilla Real também não publica os valores.</b> "
                 "capillarealgranada.com avisa que <i>“a partir de 1 de enero de 2025 "
                 "aplicaremos nuevas tarifas de visita”</i> e manda para o site de "
                 "venda.<br>"
                 "<b>€ 7,00</b> no canal oficial de venda que o próprio site indica "
                 "(ticketsgranadacristiana.com), consultado em 30/set/2026. Visita de "
                 "cerca de 45 minutos."),
                ("A mesma quarta-feira gratuita",
                 "<b>A Capilla Real tem o mesmo esquema de visita gratuita por reserva "
                 "da catedral</b>, no mesmo domínio da diocese, conferido em "
                 "30/set/2026.<br>"
                 "<b>Sessões: 15h15, 15h30, 16h30 e 17h.</b> Note que são "
                 "<b>diferentes</b> das da catedral — 16h e 16h30 lá, 16h30 e 17h "
                 "aqui.<br>"
                 "<b>Datas abertas na nossa consulta: 25 de novembro e 2, 9 e 16 de "
                 "dezembro de 2026 — todas quartas-feiras.</b><br>"
                 "<b>Valem as mesmas regras:</b> duas entradas por pessoa por dia, "
                 "reserva fecha 24 horas antes, documento do solicitante, 15 minutos de "
                 "tolerância, proibido fotografar, não vale para grupos.<br>"
                 "<b>Dá para encaixar as duas na mesma quarta</b> — a catedral às 15h15 "
                 "e a capela às 16h30, por exemplo —, mas são <b>duas reservas "
                 "separadas</b>, cada uma no seu formulário, e cada uma conta no limite "
                 "de duas por pessoa."),
                ("Horários, e o pedido que a própria capela faz",
                 FLAG % "Lacuna declarada" +
                 "<b>a visita turística é diária, exceto em três dias: Sexta-feira "
                 "Santa, 25 de dezembro e 1º de janeiro.</b> Isso o site publica.<br>"
                 "<b>O que ele não publica é a grade por dia da semana</b> — só exemplos "
                 "de datas especiais, como 24 e 31 de dezembro das 11h às 13h30.<br>"
                 "E o site é direto sobre isso: <b>“ROGAMOS QUE CONFIRMEN HORARIOS "
                 "PREVIAMENTE A LA VISITA”</b>, pelo telefone <b>958 22 78 48</b>, "
                 "porque pode haver mudança sem aviso prévio.<br>"
                 "<b>Quando a própria fonte pede que se telefone, nós não inventamos a "
                 "tabela.</b>"),
                ("Onde fica",
                 mapa("Capilla Real de Granada, Calle Oficios, 18001 Granada, Espanha")),
            ],
        },
        {
            "id": "sacromonte",
            "grupo": "g2",
            "nome": "Sacromonte: a abadia e as cavernas",
            "tag": "Bairro e museu",
            "preco_val": "€ 6 e € 7",
            "preco_nota": "são dois lugares diferentes, com dois donos",
            "campos": [
                ("Dois lugares, dois bilhetes, e quase todo mundo confunde",
                 "<b>“Ir ao Sacromonte” pode querer dizer duas coisas, e elas são "
                 "diferentes, ficam em pontos diferentes do morro e têm donos "
                 "diferentes.</b><br>"
                 "<b>Museo Cuevas del Sacromonte — € 6,00.</b> São as cavernas onde se "
                 "morava, o museu ao ar livre, o jardim botânico e o mirador. É o que a "
                 "maioria quer ver.<br>"
                 "<b>Abadía del Sacromonte — € 7,00.</b> É a abadia do século XVII, mais "
                 "acima, com as catacumbas e o colégio. Visita de cerca de 75 minutos, "
                 "vendida no circuito das igrejas (ticketsgranadacristiana.com) e "
                 "incluída no combinado de € 33.<br>"
                 "<b>Um bilhete não dá o outro.</b> Os dois juntos custam € 13."),
                ("O € 5 que circula na internet está errado",
                 "<b>A própria página do museu exibe resenhas de visitantes dizendo "
                 "“entrada 5 euros”.</b> Não é o preço.<br>"
                 "<b>Fomos ao caixa oficial</b> (shop.sacromontegranada.com), em "
                 "30/set/2026, e o resumo de compra diz <b>“Visita diurna Museo — "
                 "6,00 €”</b>.<br>"
                 "<b>Número de resenha não é número apurado</b>, mesmo quando está "
                 "hospedado no site oficial."),
                ("Horários do museu, e a regra que não devolve dinheiro",
                 "Fonte: site oficial (sacromontegranada.com), consultado em "
                 "30/set/2026.<br>"
                 "<b>Inverno, 26 de outubro a 28 de março: todos os dias, 10h às 18h</b> "
                 "— última entrada 17h40.<br>"
                 "<b>Verão, 29 de março a 25 de outubro: todos os dias, 10h às 20h</b> "
                 "— última entrada 19h40.<br>"
                 "<b>Abre todos os dias</b>, o que em Granada é incomum e importa: a "
                 "segunda-feira, que fecha o Museo de la Alhambra, aqui não fecha "
                 "nada.<br>"
                 "<b>Menor de 10 anos não paga.</b><br>"
                 "E o caixa avisa, como o da Alhambra: <b>“No se admiten cambios o "
                 "devoluciones.”</b> <b>É o segundo ingresso irreversível desta "
                 "ficha.</b>"),
                ("O que o bilhete do museu inclui",
                 "<b>As 11 cavernas originais, o jardim botânico, o Mirador de las "
                 "Cuevas, audioguia gratuita em espanhol e inglês</b> e guias impressos "
                 "em francês, italiano e alemão.<br>"
                 "<b>Visita guiada em grupo</b>, a partir de 10 pessoas, custa <b>€ 7 "
                 "por pessoa</b> e dura cerca de uma hora. <b>Grupo autoguiado</b>, "
                 "acima de 10 pessoas e com reserva de 72 horas, sai por <b>€ 5 por "
                 "pessoa</b> — é a única forma de o número € 5 ser verdadeiro."),
                ("O que não apuramos",
                 FLAG % "Lacuna declarada" +
                 "<b>a zambra, o espetáculo de flamenco nas cavernas, não entra nesta "
                 "ficha com preço.</b> São casas particulares, cada uma com sua tabela, "
                 "e não há fonte oficial única que fixe valor.<br>"
                 "O mesmo vale para a <b>tapa grátis com a bebida</b>, que é tradição "
                 "real de Granada e aparece em campanha de turismo — mas <b>não existe "
                 "norma, nem obrigação, nem valor publicado</b>, e a página da "
                 "andalucia.org devolveu <b>403</b> à conferência direta. "
                 "<b>Costume não é tarifa, e não entra como número.</b>"),
                ("Onde fica",
                 mapa("Museo Cuevas del Sacromonte, Barranco de los Negros, 18010 Granada, Espanha")),
            ],
        },
        # =============================================================
        #  g3 - o que nao cobra, e a conta da cama
        # =============================================================
        {
            "id": "museo-alhambra",
            "grupo": "g3",
            "nome": "Museo de la Alhambra",
            "tag": "Museu",
            "preco_val": "Grátis",
            "preco_nota": "dentro da Alhambra, sem ingresso do monumento",
            "campos": [
                ("A linha mais útil desta ficha",
                 "<b>Há um museu dentro do recinto da Alhambra em que se entra de graça, "
                 "sem comprar o ingresso do monumento.</b><br>"
                 "E isso não é cortesia: está em <b>norma legal</b>. O "
                 "<b>artigo 9.1</b> da Orden de 17 de julio de 2025 diz: <b>“Todos los "
                 "visitantes podrán acceder gratuitamente durante el horario de apertura "
                 "al Museo de la Alhambra y al monumento El Corral del Carbón.”</b><br>"
                 "A página do museu confirma, em caixa alta: <b>“ENTRADA LIBRE”</b>. "
                 "Fonte: alhambra-patronato.es, consultada em 30/set/2026.<br>"
                 "<b>Ele fica dentro do Palacio de Carlos V</b>, o palácio renascentista "
                 "de pátio circular que está no meio da Alhambra — e guarda as peças "
                 "nazaríes tiradas do próprio monumento."),
                ("O que isso resolve, e o que não resolve",
                 "<b>Resolve:</b> quem não conseguiu ingresso para o dia — e isso "
                 "acontece, porque os Palacios Nazaríes vendem 300 vagas a cada meia "
                 "hora — ainda pode subir, ver o Palacio de Carlos V e o museu, e não "
                 "pagar nada.<br>"
                 "<b>Não resolve:</b> <b>não dá os Palacios Nazaríes, nem a Alcazaba, "
                 "nem o Generalife.</b> Esses continuam sendo bilhete pago, com hora "
                 "marcada.<br>"
                 "<b>Não é “a Alhambra de graça”.</b> É uma parte dela, e a parte que "
                 "está dita."),
                ("Horários, e a segunda-feira",
                 "<b>15 de outubro a 31 de março:</b> quarta a sábado, <b>8h30 às "
                 "18h</b>; domingo e terça, <b>8h30 às 14h30</b>.<br>"
                 "<b>1º de abril a 14 de outubro:</b> quarta a sábado, <b>8h30 às "
                 "20h</b>; domingo e terça, <b>8h30 às 14h30</b>.<br>"
                 "<b>Segunda-feira: fechado.</b><br>"
                 "<b>Sábados de maio a setembro: 8h30 às 21h30.</b><br>"
                 "<b>18 de maio</b>, Dia Internacional dos Museus: 8h30 às 21h30.<br>"
                 "<b>Atenção ao domingo e à terça</b>, que fecham às 14h30 — cinco horas "
                 "e meia antes do sábado de verão. Quem deixa o museu para a tarde de "
                 "domingo encontra porta fechada."),
                ("Onde fica",
                 mapa("Museo de la Alhambra, Palacio de Carlos V, Alhambra, 18009 Granada, Espanha")),
            ],
        },
        {
            "id": "monumentos-andalusies",
            "grupo": "g3",
            "nome": "Monumentos andalusíes",
            "tag": "Casas e banhos",
            "preco_val": "€ 2",
            "preco_nota": "por monumento; domingo é grátis",
            "campos": [
                ("Cinco lugares a € 2, e um que nunca cobra",
                 "<b>São os monumentos árabes espalhados pelo Albaicín e pelo centro, "
                 "sob a mesma administração da Alhambra</b> — e custam uma fração do "
                 "preço dela.<br>"
                 "A <b>Orden de 17 de julio de 2025</b> é explícita: "
                 "<b>“Visita de cada monumento de forma individual (Corral del Carbón "
                 "gratuito): 2 €.”</b><br>"
                 "São o <b>Bañuelo</b> (banhos árabes do século XI), a <b>Casa Morisca "
                 "del Horno de Oro</b>, o <b>Palacio de Dar al-Horra</b>, o "
                 "<b>Maristán</b> e o <b>Corral del Carbón</b>.<br>"
                 "<b>O Corral del Carbón é gratuito sempre</b>, para todos, pelo mesmo "
                 "artigo 9.1 que libera o Museo de la Alhambra. É uma pousada de "
                 "mercadores do século XIV, e é também onde fica o balcão de atendimento "
                 "do Patronato."),
                ("Quando é de graça",
                 "<b>A página oficial de horários e tarifas diz, em caixa alta: “LA "
                 "ENTRADA EN DOMINGO ES GRATUITA”.</b> Fonte: alhambra-patronato.es, "
                 "consultada em 30/set/2026.<br>"
                 "<b>É o domingo inteiro, não uma faixa de horário</b> — e vale para "
                 "todos, sem comprovação de residência e sem reserva.<br>"
                 "<b>Isto fecha com a quarta-feira da catedral:</b> em Granada, dois dias "
                 "da semana têm entrada livre em lugares diferentes, e nenhum dos dois é "
                 "o dia que os guias sugerem reservar para o centro histórico."),
                ("Horários",
                 "<b>1º de maio a 14 de setembro: todos os dias, 9h às 14h30 e 17h às "
                 "20h30.</b> Fecha no meio do dia — é o horário de verão andaluz, e o "
                 "vão das 14h30 às 17h é justamente quando faz mais calor.<br>"
                 "<b>15 de setembro a 30 de abril: todos os dias, 10h às 17h</b>, sem "
                 "interrupção.<br>"
                 "<b>O Corral del Carbón tem horário próprio e mais largo: todos os "
                 "dias, 9h às 20h.</b><br>"
                 "<b>Fecham em 25 de dezembro e 1º de janeiro.</b>"),
                ("Onde fica",
                 mapa("Corral del Carbón, Calle Mariana Pineda, 18009 Granada, Espanha")),
            ],
        },
        {
            "id": "miradouros",
            "grupo": "g3",
            "nome": "Os miradouros que não cobram",
            "tag": "Mirante",
            "preco_val": "Grátis",
            "preco_nota": "dois só abrem no fim de semana",
            "campos": [
                ("Mirador de San Nicolás, e a torre ao lado que cobra",
                 "<b>É a vista mais fotografada de Granada</b>: a Alhambra inteira de "
                 "frente, com a Sierra Nevada atrás. <b>Não há bilheteria, não há "
                 "horário, não há ingresso.</b> É praça pública, no Albaicín.<br>"
                 "<b>O que cobra é outra coisa, e fica a poucos metros:</b> a "
                 "<b>Iglesia y torre de San Nicolás</b> custa <b>€ 3,00</b> no circuito "
                 "das igrejas (ticketsgranadacristiana.com, consultado em 30/set/2026), "
                 "com visita de cerca de 30 minutos.<br>"
                 "<b>Quem quer só a vista não paga nada.</b> O € 3 é para subir a torre "
                 "e entrar na igreja."),
                ("Silla del Moro e Torres Bermejas: grátis, e só no fim de semana",
                 "<b>Dois miradouros da própria Alhambra, com entrada gratuita</b> — a "
                 "página oficial marca os dois como <b>“VISITA GRATUITA”</b>. "
                 "Fonte: alhambra-patronato.es, consultada em 30/set/2026.<br>"
                 "<b>E os dois só abrem sábado e domingo.</b> É a pegadinha desta "
                 "linha: são de graça, mas não estão disponíveis em cinco dos sete dias "
                 "da semana.<br>"
                 "<b>Silla del Moro</b>, que é o Castillo de Santa Elena, acima do "
                 "Generalife:<br>"
                 "<b>1º de abril a 14 de outubro — sábado 8h30 às 20h, domingo 8h30 às "
                 "14h.</b><br>"
                 "<b>15 de outubro a 31 de março — sábado 8h30 às 18h, domingo 8h30 às "
                 "14h.</b><br>"
                 "<b>Note a assimetria: no domingo fecha às 14h nas duas temporadas</b>, "
                 "seis horas antes do sábado de verão.<br>"
                 "<b>Torres Bermejas</b>, na encosta abaixo da Alhambra:<br>"
                 "<b>1º de abril a 14 de outubro — sábado e domingo, 8h30 às 20h.</b><br>"
                 "<b>15 de outubro a 31 de março — sábado e domingo, 8h30 às 18h.</b><br>"
                 "<b>Aqui o domingo é igual ao sábado</b> — ao contrário da Silla del "
                 "Moro, a 20 minutos de caminhada dali. <b>São dois lugares do mesmo "
                 "órgão, com regras de domingo diferentes.</b>"),
                ("Onde fica",
                 mapa("Mirador de San Nicolás, 18010 Granada, Espanha")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem, e o mês ao contrário",
            "tag": "Conta, não lugar",
            "preco_val": "€ 95,08",
            "preco_nota": "média de 12 meses por quarto; varia 68% no ano",
            "campos": [
                ("A fonte, e o que o número é",
                 "Fonte: <b>INE</b> (Instituto Nacional de Estadística de Espanha), "
                 "<i>Indicadores de Rentabilidad del Sector Hotelero</i>, <b>tabela "
                 "46298</b> — tarifa média diária (ADR) por <b>ponto turístico</b>, "
                 "série <i>Granada, total de categorias</i>, consultada em "
                 "30/set/2026.<br>"
                 "<b>É por quarto ocupado, por noite, e não por pessoa</b> — o rótulo do "
                 "INE é <i>“Tarifa media por habitación ocupada”</i>. E cobre "
                 "<b>hotéis</b>, não apartamentos de temporada.<br>"
                 "<b>Os € 95,08 são a média dos 12 meses de setembro de 2025 a agosto de "
                 "2026.</b> Os doze valores são do INE; <b>a média é cálculo nosso</b>, "
                 "e está dito."),
                ("O achado: agosto é o mês mais barato do ano",
                 "<b>Isto é o contrário do que se supõe de um destino europeu, e é dado "
                 "oficial.</b><br>"
                 "<b>Agosto de 2026: € 73,07</b> — o mais barato dos doze meses.<br>"
                 "<b>Outubro de 2025: € 122,46</b> — o mais caro.<br>"
                 "<b>São 68% de diferença pelo mesmo quarto</b>, só trocando o mês.<br>"
                 "Os doze valores, para você conferir: set/2025 € 100,39 · out/2025 "
                 "€ 122,46 · nov/2025 € 88,11 · dez/2025 € 96,66 · jan/2026 € 92,66 · "
                 "fev/2026 € 87,94 · mar/2026 € 91,50 · abr/2026 € 107,98 · mai/2026 "
                 "€ 110,48 · jun/2026 € 90,20 · jul/2026 € 79,56 · ago/2026 € 73,07.<br>"
                 "<b>A explicação é o calor.</b> Granada é Andaluzia interior, não "
                 "costa. Em agosto a cidade esvazia, e o preço cai. No <b>mesmo agosto "
                 "de 2026</b>, o INE registra <b>€ 163,05 em Málaga</b>, a 130 "
                 "quilômetros, na praia — <b>2,2 vezes Granada</b>. E a média nacional "
                 "espanhola no mês é <b>€ 166,90</b>, mais que o dobro.<br>"
                 "Córdoba (€ 62,06) e Sevilha (€ 87,39) fazem o mesmo movimento. "
                 "<b>Não é Granada: é a Andaluzia de dentro.</b>"),
                ("O que isso soma com o calendário da Alhambra",
                 "<b>Agosto junta três coisas, e duas são boas.</b><br>"
                 "<b>A cama é a mais barata do ano</b> (€ 73,07 contra € 122,46 em "
                 "outubro).<br>"
                 "<b>A Alhambra está no horário longo</b>, 8h30 às 20h, e não 8h30 às "
                 "18h.<br>"
                 "<b>A visita noturna aos Palacios Nazaríes roda de terça a sábado</b>, "
                 "cinco noites por semana, e não só sexta e sábado como no inverno.<br>"
                 "<b>A terceira coisa é o calor</b>, que é a razão de as outras duas "
                 "existirem. Andaluzia interior em agosto passa dos 40 °C com "
                 "frequência, e a Alhambra se visita a pé, ao sol, por horas.<br>"
                 "<b>Não estamos recomendando agosto.</b> Estamos dizendo que a troca é "
                 "essa, com número dos dois lados — e que a noturna existe justamente "
                 "para quem vai no verão."),
                ("A taxa que não há",
                 FLAG % "Só em fonte secundária" +
                 "<b>não há taxa turística municipal na Andaluzia em 2026</b>, e "
                 "portanto não há em Granada.<br>"
                 "É o mesmo achado que a ficha de Sevilha já registra: a criação da taxa "
                 "<b>depende da Junta de Andalucía</b>, que não aprovou, e sem a Junta o "
                 "município não pode instituí-la.<br>"
                 "<b>Um negativo não tem página oficial para citar</b>, e por isso esta "
                 "linha está marcada. Se o seu hotel em Granada cobrar algo chamado de "
                 "taxa turística, <b>confira o que está sendo cobrado</b> — municipal "
                 "não é."),
            ],
        },
    ],
}

DESTINOS = [GRANADA]
