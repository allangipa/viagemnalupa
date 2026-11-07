# -*- coding: utf-8 -*-
"""Londres: o vigesimo setimo destino, em doze pontos e tres grupos.

Mesmo molde do gramado/dados.py. Primeira cidade em libra.

O ACHADO PRINCIPAL: O PALACIO DE BUCKINGHAM SO ABRE NO VERAO
--------------------------------------------------------------
O Royal Collection Trust (rct.uk), lido em 07/11/2026: as salas de Estado
abrem "each summer" - em 2027, de 8 de julho a 26 de setembro, a £ 35 com
compra antecipada e £ 39 no dia. "During the rest of the year the Palace
only opens on selected dates for Exclusive Guided Tours": a visita
guiada da Ala Leste, de 6/nov/2026 a 31/jan/2027, a £ 100 por pessoa. Quem
vai a Londres entre outubro e junho e quer entrar no palacio paga quase
o triplo - ou ve a troca da guarda, que e na rua e nao cobra.

O SEGUNDO: O BRASILEIRO PAGA £ 20 ANTES DE EMBARCAR
--------------------------------------------------------------
O gov.uk ("Check if you need a UK visa", Brasil, turismo) responde:
"You'll need an electronic travel authorisation (ETA) or a visa". A ETA
"costs £20", vale para estadias de ate 6 meses, e "each person travelling
needs an ETA, including babies and children". E o gov.uk avisa: "Other
websites may charge more to apply."

O TERCEIRO: O MESMO MONUMENTO, DOIS PRECOS PELO ENDERECO
--------------------------------------------------------------
A Torre de Londres cobra £ 38 do adulto - e £ 1 de quem mora no bairro de
Tower Hamlets, so na bilheteria, com comprovante. E o mesmo padrao do
Parque do Caracol, em Gramado. A Abadia de Westminster faz parecido:
"Westminster residents" estao na lista de concessoes.

O QUE FICOU SEM RESPOSTA
--------------------------------------------------------------
    TfL            a pagina de tarifas e a de tetos respondem com
                   verificacao anti-robo (Cloudflare); nao contornamos. O
                   que esta aqui vem dos comunicados oficiais da TfL e,
                   para o valor do teto diario, de fonte secundaria
    hospedagem     nenhum orgao publica a diaria media de Londres; o que
                   circula e da STR/CoStar, pago. Sem estimativa.
    St Paul's      horario de visita nao esta na pagina de precos
    London Eye     preco dinamico, "from £29" on-line

Apuracao de 7 de novembro de 2026.
"""

APURACAO = "7 de novembro de 2026"
APURACAO_CURTA = "7/nov/2026"

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
#  LONDRES
# =====================================================================
LONDRES = {
    "slug": "londres",
    "nome": "Londres",
    "pais": "Reino Unido",
    "regiao": "europa",
    "titulo": "Londres: 12 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 12 pontos de Londres, com o Palácio de "
                  "Buckingham que só abre no verão, a ETA de £ 20 que o brasileiro paga "
                  "antes de embarcar e os museus que não cobram."),
    "abertura": ("Doze pontos de Londres com preço em libra, horário e fonte conferidos "
                 "em 7 de novembro de 2026 — e duas coisas que os guias não somam: <b>o "
                 "Palácio de Buckingham só abre no verão</b>, e fora dele a única entrada "
                 "é uma visita guiada de £ 100; <b>e o brasileiro paga £ 20 de ETA antes "
                 "de embarcar</b>, bebê incluído. Em compensação, os três maiores museus "
                 "da cidade não cobram nada."),
    "busca": ("londres london inglaterra reino unido uk europa british museum national "
              "gallery natural history museum torre de londres tower abadia westminster "
              "st pauls london eye buckingham troca da guarda eta metro tfl heathrow"),
    "grupos": [
        {"id": "g1", "titulo": "O que não cobra — e é o melhor da cidade",
         "intro": ("Os três grandes museus nacionais têm entrada livre, e a troca da "
                   "guarda é na rua. Só o que muda é o horário.")},
        {"id": "g2", "titulo": "Os pagos, e a regra de cada um",
         "intro": ("Torre, Abadia, St Paul's, London Eye e Buckingham: cada um com uma "
                   "“doação” opcional, um passe escondido ou uma temporada.")},
        {"id": "g3", "titulo": "Entrar, circular e a conta da cama",
         "intro": ("A ETA que se paga antes do voo, o trem do aeroporto que subiu em "
                   "março e a hospedagem — sem diária oficial publicada, e com uma taxa "
                   "que ainda não existe.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - o que nao cobra
        # =============================================================
        {
            "id": "british-museum",
            "foto": {"arq": "londres/british-museum.webp",
                     "alt": "O Great Court do British Museum, com a cobertura de vidro em treliça e a sala de leitura circular ao centro",
                     "cred": "Diliff · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "British Museum",
            "tag": "Museu",
            "preco_val": "Grátis",
            "preco_nota": "reserva recomendada; sexta até 20h30",
            "campos": [
                ("Entrada",
                 "Fonte: página de visita do site oficial (britishmuseum.org), consultada "
                 "em 7/nov/2026: <b>“Free entry”</b>.<br>"
                 "<b>A reserva é recomendada, não obrigatória</b> — <i>“Advance booking "
                 "recommended”</i>, com ingresso gratuito no site. As exposições "
                 "temporárias cobram à parte."),
                ("Dias e horários",
                 "<b>Todos os dias, 10h às 17h; sexta até 20h30.</b><br>"
                 "<b>Fecha de 24 a 26 de dezembro.</b>"),
                ("Onde fica",
                 mapa("British Museum, Great Russell Street, London WC1B 3DG")),
            ],
        },
        {
            "id": "national-gallery",
            "foto": {"arq": "londres/national-gallery.webp",
                     "alt": "A fachada da National Gallery vista da Trafalgar Square, com a fonte em primeiro plano",
                     "cred": "Ray in Manila · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "National Gallery",
            "tag": "Museu",
            "preco_val": "Grátis",
            "preco_nota": "sexta até 21h; sem reserva obrigatória",
            "campos": [
                ("Entrada",
                 "Fonte: página de visita do site oficial (nationalgallery.org.uk), "
                 "consultada em 7/nov/2026: <i>“The National Gallery is free to "
                 "visit”</i>. Algumas exposições cobram.<br>"
                 "<b>Não precisa reservar</b> — <i>“Walk-up entry is also available”</i>. "
                 "O ingresso gratuito on-line só dá entrada mais rápida."),
                ("Dias e horários",
                 "<b>Todos os dias, 10h às 18h; sexta até 21h.</b><br>"
                 "<b>Fecha de 24 a 26 de dezembro e em 1º de janeiro.</b>"),
                ("Onde fica",
                 mapa("National Gallery, Trafalgar Square, London WC2N 5DN")),
            ],
        },
        {
            "id": "natural-history-museum",
            "foto": {"arq": "londres/natural-history-museum.webp",
                     "alt": "O salão central do Natural History Museum, com os arcos neogóticos e o esqueleto de baleia suspenso",
                     "cred": "APK · CC BY 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Natural History Museum",
            "tag": "Museu",
            "preco_val": "Grátis",
            "preco_nota": "fila em dia cheio; o ingresso gratuito garante entrada",
            "campos": [
                ("Entrada",
                 "Fonte: página de visita do site oficial (nhm.ac.uk), consultada em "
                 "7/nov/2026: <i>“Our galleries are free to explore.”</i><br>"
                 "Para garantir a entrada, o museu oferece <b>ingresso gratuito "
                 "reservado</b>; sem ele, <i>“you may have to queue to enter”</i> nos "
                 "dias cheios."),
                ("Dias e horários",
                 "<b>Todos os dias, 10h às 17h50</b> (última entrada 17h30).<br>"
                 "<b>Fecha em 9 de outubro e de 24 a 26 de dezembro.</b>"),
                ("Onde fica",
                 mapa("Natural History Museum, Cromwell Road, London SW7 5BD")),
            ],
        },
        {
            "id": "troca-da-guarda",
            "foto": {"arq": "londres/troca-da-guarda.webp",
                     "alt": "Guardas de túnica vermelha e chapéu de pele no pátio do Palácio de Buckingham, durante a troca da guarda",
                     "cred": "Rennett Stowe · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Troca da guarda em Buckingham",
            "tag": "Cerimônia",
            "preco_val": "Grátis",
            "preco_nota": "em novembro, segunda, quarta e sexta às 11h",
            "campos": [
                ("Quando acontece",
                 "Fonte: calendário oficial da <b>Household Division</b> "
                 "(householddivision.org.uk), consultado em 7/nov/2026.<br>"
                 "<b>Em novembro de 2026: segunda, quarta e sexta, às 11h</b> — dias 2, 4, "
                 "6, 9, 11, 13, 16, 18, 20, 23, 25, 27 e 30.<br>"
                 "<b>Não é todo dia.</b> As paradas de domingo, às 10h, são outra coisa e "
                 "não são troca da guarda.<br>"
                 "É na rua, diante do palácio, e não tem ingresso."),
                ("O que não está publicado",
                 FLAG % "Lacuna declarada" +
                 "<b>o calendário não diz se a cerimônia é cancelada com chuva.</b> "
                 "Confira o calendário no próprio dia."),
                ("Onde fica",
                 mapa("Buckingham Palace, London SW1A 1AA")),
            ],
        },
        # =============================================================
        #  g2 - os pagos
        # =============================================================
        {
            "id": "torre-de-londres",
            "foto": {"arq": "londres/torre-de-londres.webp",
                     "alt": "A Torre Branca, de pedra clara e quatro torreões, no centro da Torre de Londres",
                     "cred": "Diego Delso · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Torre de Londres",
            "tag": "Castelo",
            "preco_val": "£ 38",
            "preco_nota": "£ 41,80 com a doação opcional; £ 1 para morador do bairro",
            "campos": [
                ("Valor da entrada",
                 "Fonte: tabela de preços do site oficial da Historic Royal Palaces "
                 "(hrp.org.uk), consultada em 7/nov/2026.<br>"
                 "<b>Adulto: £ 38,00.</b> Com a doação, £ 41,80.<br>"
                 "<b>De 5 a 15 anos: £ 19,00</b>; de 16 a 17, £ 19,00; <b>até 4 anos não "
                 "paga</b>. Sênior e estudante em tempo integral: £ 30,30.<br>"
                 "<b>A tabela tem duas colunas, “No donation” e “Donation”.</b> A doação "
                 "de 10% é <b>opcional</b> — a instituição é uma entidade beneficente sem "
                 "verba do governo e pede, mas não cobra. Confira qual coluna está no seu "
                 "carrinho.<br>"
                 "Inclui as Joias da Coroa, a Torre Branca, as muralhas e a visita com os "
                 "Yeoman Warders."),
                ("O preço de quem mora ao lado",
                 "<b>Morador de Tower Hamlets, o bairro da Torre, paga £ 1,00</b> — <i>“The "
                 "offer is valid all year round”</i>, só na bilheteria, com comprovante de "
                 "endereço, para a próxima faixa de horário. Até três crianças a £ 1 "
                 "cada.<br>"
                 "É o mesmo padrão do Parque do Caracol, em Gramado: o monumento cobra do "
                 "turista e quase nada de quem mora ao lado."),
                ("Onde fica",
                 mapa("Tower of London, London EC3N 4AB")),
            ],
        },
        {
            "id": "abadia-westminster",
            "foto": {"arq": "londres/abadia-westminster.webp",
                     "alt": "A fachada oeste da Abadia de Westminster, com as duas torres góticas",
                     "cred": "Paasikivi · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Abadia de Westminster",
            "tag": "Igreja",
            "preco_val": "£ 32",
            "preco_nota": "o ingresso do site vira passe anual de graça",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de horários e preços do site oficial "
                 "(westminster-abbey.org), consultada em 7/nov/2026.<br>"
                 "<b>Adulto: £ 32.</b> Acima de 65 e estudante: £ 29. <b>De 6 a 17 anos: "
                 "£ 14.</b> Até 5 anos não paga.<br>"
                 "<b>Família de 1 adulto e 1 criança: £ 32</b> — o mesmo preço do adulto "
                 "sozinho. A criança sai de graça.<br>"
                 "O guia multimídia, em 14 línguas, está incluído."),
                ("Três visitas pelo preço de uma",
                 "<b>Quem compra no site oficial pode transformar o ingresso em passe "
                 "anual, de graça</b> — <i>“you can upgrade it to an annual pass free of "
                 "charge. This will enable you to visit the Abbey three times for the "
                 "price of one.”</i> A troca se faz na própria Abadia, com a equipe. "
                 "<b>Ingresso comprado em revenda não vale</b>, nem os promocionais."),
                ("Dias e horários",
                 "No sábado consultado, <b>7 de novembro de 2026, visita das 9h às 15h</b> "
                 "(o calendário da página muda dia a dia).<br>"
                 "<b>Domingo, a Abadia só abre para culto</b> — <i>“Sunday open for "
                 "services”</i>. Quem vai para rezar não paga."),
                ("Onde fica",
                 mapa("Westminster Abbey, 20 Deans Yard, London SW1P 3PA")),
            ],
        },
        {
            "id": "st-pauls",
            "foto": {"arq": "londres/st-pauls.webp",
                     "alt": "A cúpula da Catedral de St Paul's contra o céu azul",
                     "cred": "Christine Matthews · CC BY-SA 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Catedral de St Paul's",
            "tag": "Igreja",
            "preco_val": "£ 27",
            "preco_nota": "£ 24 no verão; culto não cobra",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de ingressos do site oficial (stpauls.co.uk), consultada "
                 "em 7/nov/2026, tabela de <i>“Monday to Saturday sightseeing”</i>.<br>"
                 "<b>Adulto: £ 27</b> fora do verão; <b>£ 24 de 25 de junho a 1º de "
                 "setembro de 2026</b>. Com a doação opcional, £ 29,70.<br>"
                 "Acima de 65 e estudante: £ 24. <b>De 6 a 17 anos: £ 10,50.</b> Até 5 "
                 "anos não paga.<br>"
                 "<b>O culto não cobra</b>: a própria página diz <i>“Although our services "
                 "are free, we ask our sightseeing visitors to contribute a small entrance "
                 "fee.”</i>"),
                ("O que não está publicado",
                 FLAG % "Lacuna declarada" +
                 "<b>a página de ingressos não traz o horário de visita</b> nem diz se há "
                 "visita turística no domingo — a tabela é só de segunda a sábado."),
                ("Onde fica",
                 mapa("St Paul's Cathedral, London EC4M 8AD")),
            ],
        },
        {
            "id": "london-eye",
            "foto": {"arq": "londres/london-eye.webp",
                     "alt": "O London Eye à beira do Tâmisa, com o antigo County Hall ao lado",
                     "cred": "Rhododendrites · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "London Eye",
            "tag": "Roda-gigante",
            "preco_val": "desde £ 29",
            "preco_nota": "£ 39 comprando na hora",
            "campos": [
                ("Valor da entrada, e por que muda",
                 "Fonte: página de ingressos do site oficial (londoneye.com), consultada "
                 "em 7/nov/2026.<br>"
                 "<b>Adulto: “From £29” on-line, £ 39 na bilheteria.</b> Criança de 2 a "
                 "15 anos: desde £ 26 on-line, £ 35 na hora. <b>Menor de 2 não paga.</b><br>"
                 "<b>O preço on-line varia com a demanda</b> — <i>“prices may fluctuate "
                 "during periods of high demand”</i>. <b>£ 29 é piso.</b> E comprar na "
                 "hora custa pelo menos £ 10 a mais."),
                ("Horário",
                 "No dia consultado, <b>10h às 20h30</b> — a página mostra só o horário "
                 "“de hoje”."),
                ("Onde fica",
                 mapa("London Eye, Riverside Building, County Hall, London SE1 7PB")),
            ],
        },
        {
            "id": "buckingham",
            "foto": {"arq": "londres/buckingham.webp",
                     "alt": "A fachada principal do Palácio de Buckingham, com visitantes na praça em frente",
                     "cred": "Fatih Renkligil · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Palácio de Buckingham por dentro",
            "tag": "Palácio",
            "preco_val": "£ 35 no verão",
            "preco_nota": "fora do verão, só visita guiada a £ 100",
            "campos": [
                ("Só abre no verão",
                 "Fonte: página de visita do <b>Royal Collection Trust</b> (rct.uk), "
                 "consultada em 7/nov/2026.<br>"
                 "<i>“Buckingham Palace's magnificent State Rooms open to visitors each "
                 "summer. In 2027, the Palace will be open from 8 July to 26 "
                 "September.”</i><br>"
                 "<b>Ingresso padrão do verão de 2027: £ 35 com antecedência, £ 39 no "
                 "dia</b>; de 18 a 24 anos, £ 23 e £ 26; <b>de 5 a 17 anos, £ 17,50 e "
                 "£ 19,50</b>; menor de 5 não paga."),
                ("O resto do ano: £ 100",
                 "<i>“During the rest of the year the Palace only opens on selected dates "
                 "for Exclusive Guided Tours.”</i><br>"
                 "<b>A visita guiada da Ala Leste, de 6 de novembro de 2026 a 31 de "
                 "janeiro de 2027, custa £ 100 por pessoa</b> — <i>“the only way to visit "
                 "Buckingham Palace during the winter months”</i>.<br>"
                 "<b>Quase o triplo do ingresso de verão.</b> Para quem viaja entre outubro "
                 "e junho, a alternativa sem custo é a troca da guarda, do lado de fora."),
                ("Onde fica",
                 mapa("Buckingham Palace, London SW1A 1AA")),
            ],
        },
        # =============================================================
        #  g3 - entrar, circular e a cama
        # =============================================================
        {
            "id": "eta",
            "grupo": "g3",
            "nome": "ETA: a autorização antes do voo",
            "tag": "Documento",
            "preco_val": "£ 20",
            "preco_nota": "por pessoa, bebê incluído",
            "campos": [
                ("Quem precisa, e quanto custa",
                 "Fonte: <b>gov.uk</b>, consulta “Check if you need a UK visa” para "
                 "nacionalidade brasileira e turismo, e a página da ETA, em "
                 "7/nov/2026.<br>"
                 "<b>Brasileiro precisa:</b> <i>“You'll need an electronic travel "
                 "authorisation (ETA) or a visa.”</i><br>"
                 "<b>Custa £ 20</b> — <i>“An ETA costs £20.”</i> Vale para estadias de "
                 "até 6 meses.<br>"
                 "<b>Cada pessoa precisa da sua, inclusive bebês e crianças</b> — "
                 "<i>“Each person travelling needs an ETA, including babies and "
                 "children.”</i> Uma família de quatro paga £ 80.<br>"
                 "Quem só faz conexão em Heathrow <b>sem passar pela imigração</b> não "
                 "precisa; quem passa, precisa."),
                ("O golpe que o próprio governo avisa",
                 "O gov.uk escreve, logo abaixo do preço: <i>“Other websites may charge "
                 "more to apply. Avoid websites that imitate government services.”</i> "
                 "<b>O pedido se faz no gov.uk ou no aplicativo oficial.</b> Site que "
                 "cobra mais de £ 20 é intermediário."),
            ],
        },
        {
            "id": "metro-e-aeroporto",
            "grupo": "g3",
            "nome": "Metrô, ônibus e o trem de Heathrow",
            "tag": "Transporte",
            "preco_val": "£ 15,50",
            "preco_nota": "Elizabeth line até Heathrow, desde março de 2026",
            "campos": [
                ("O trem do aeroporto subiu",
                 "Fonte: comunicado oficial da <b>TfL</b> de 20/fev/2026, sobre as "
                 "tarifas a partir de 1º de março de 2026.<br>"
                 "<b>A Elizabeth line do centro (zona 1) a Heathrow passou de £ 13,90 "
                 "para £ 15,50.</b><br>"
                 "No mesmo comunicado: nenhuma tarifa avulsa de metrô dentro das zonas 1 "
                 "a 6 subiu mais de 20 pence, e <b>os tetos diários e semanais não mudam "
                 "até março de 2027</b>, porque os Travelcards ficaram congelados."),
                ("O teto diário",
                 FLAG % "Só em fonte secundária" +
                 "<b>o comunicado diz que o teto não muda, mas não diz o valor.</b> A "
                 "página de tetos da TfL respondeu com verificação anti-robô e não "
                 "abriu — <b>não contornamos</b>. Guias de transporte publicam "
                 "<b>£ 8,90 por dia nas zonas 1 e 2</b>, com cartão por aproximação, e "
                 "esta ficha usa esse número, marcado.<br>"
                 "<b>Use o mesmo cartão o dia inteiro</b>: o teto só funciona por "
                 "cartão. Dois cartões, dois tetos."),
                ("O ônibus",
                 "Comunicado da TfL de 3/jul/2026: o congelamento das tarifas de ônibus "
                 "ia <b>até 1º de novembro de 2026</b>, e depois a passagem "
                 "<i>“expected to increase 10p to £1.85”</i>, com teto diário de "
                 "<b>£ 5,55</b>.<br>"
                 + FLAG % "Lacuna declarada" +
                 "não conseguimos confirmar na página de tarifas, pelo mesmo motivo."),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem, e a taxa que ainda não existe",
            "tag": "Conta, não lugar",
            "preco_val": "sem dado oficial",
            "preco_nota": "a taxa turística foi autorizada, mas não antes de 2028",
            "campos": [
                ("Por que não há diária nesta ficha",
                 FLAG % "Lacuna declarada" +
                 "<b>Nenhum órgão publica a diária média de Londres.</b> O dado que "
                 "existe é da STR/CoStar, pago, e os números que circulam de graça não "
                 "batem entre si. <b>A regra desta casa é não estimar</b>: a ficha mostra o "
                 "total sem a hospedagem, e diz isso no rótulo."),
                ("A taxa turística: autorizada, não cobrada",
                 FLAG % "Só em fonte secundária" +
                 "em 2026, <b>Londres não cobra taxa turística</b>. O governo britânico "
                 "deu aos prefeitos o poder de criar uma <i>overnight visitor levy</i>, e "
                 "o prefeito Sadiq Khan disse que a de Londres teria teto de <b>5% por "
                 "noite</b>. <b>A imprensa britânica não vê a taxa na conta do hotel antes "
                 "de 2028.</b><br>"
                 "Se o seu hotel cobrar “city tax” em 2026, pergunte com base em quê."),
            ],
        },
    ],
}

DESTINOS = [LONDRES]
