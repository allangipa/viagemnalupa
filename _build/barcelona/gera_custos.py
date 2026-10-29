# -*- coding: utf-8 -*-
"""Ficha de custos de Barcelona: 5 dias, 1 pessoa, euro.

Mesmo molde do granada/gera_custos.py.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
E a primeira ficha espanhola do site com TAXA TURISTICA - Sevilha e
Granada nao tem, porque a Andaluzia nao criou. Barcelona tem a mais alta
da Espanha, e ela dobrou em 1 de abril de 2026 (Llei 2/2026): 2,00 EUR
de imposto catalao mais 5,00 de recarrec municipal num hotel de ate tres
estrelas, por pessoa e por noite. Quatro noites sao 28 EUR. A linha usa
o data-noite para o calculador escalar pelas noites do leitor, e o teto
de 7 noites que a lei fixa.

A SEGUNDA DIFERENCA: TRES LINHAS CAEM COM O CALENDARIO
-------------------------------------------------------
    quinta   Museu Picasso, 16h-19h, por reserva        12 EUR
    sabado   MNAC, a partir das 15h                     12 EUR
    domingo  Castell de Montjuic, a partir das 15h      12 EUR

Sao 36 EUR de ingresso que uma viagem de quinta a segunda tira da conta.
O roteiro e montado em cima disso.

A TERCEIRA: QUATRO PRECOS "A PARTIR DE"
----------------------------------------
Casa Batllo, La Pedrera, o museu do Barca e o Hola Barcelona publicam
"From". A tabela usa o "From" como piso e diz isso linha a linha. E a
Sagrada Familia, que tem tabela fixa, e nominativa e sem devolucao.

Uso
---
    python _build/barcelona/gera_custos.py
    python _build/barcelona/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_barcelona_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

APURADO = "18 de outubro de 2026"

# Serie do INE, tabela 46298, "Barcelona. Tarifa media diaria (ADR)",
# EOT43584, lida pela API (servicios.ine.es/wstempus) em 29/10/2026 e
# guardada em _build/barcelona/fontes/. Janela de out/2025 a set/2026, a
# mesma de Madri: a de 18/10 comecava em set/2025, mes que o INE revisou
# depois (198,64 -> 196,10). Inteira aqui para a media ser conferivel.
ADR = {
    "out/2025": 190.29, "nov/2025": 155.67, "dez/2025": 131.41,
    "jan/2026": 135.13, "fev/2026": 153.00, "mar/2026": 188.47,
    "abr/2026": 193.14, "mai/2026": 223.37, "jun/2026": 214.34,
    "jul/2026": 186.09, "ago/2026": 175.42, "set/2026": 207.03,
}
MEDIA = round(sum(ADR.values()) / len(ADR), 2)      # 179.45
assert len(ADR) == 12, "a media diz 12 meses; confira a serie"
assert min(ADR, key=ADR.get) == "dez/2025", "dezembro deixou de ser o mais barato"
assert max(ADR, key=ADR.get) == "mai/2026", "maio deixou de ser o mais caro"
assert MEDIA == 179.45, "a media mudou; atualize os textos que a citam"

NOITES = 4
TAXA_NOITE = 7.00       # 2,00 IEET + 5,00 recarrec, hotel de ate 3 estrelas

FICHAS = {
    "barcelona": {
        "nome": "Barcelona", "dias": 5, "moeda": "€", "dec": 2,
        "titulo": "Quanto custa 5 dias em Barcelona em 2026",
        "descricao": ("O custo de 5 dias em Barcelona, por pessoa, com a taxa turística "
                      "que dobrou em abril de 2026, os quatro ingressos de Gaudí e as três "
                      "tardes da semana em que os museus não cobram."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas "
                     "em fonte oficial em 18 de outubro de 2026. <b>Com hospedagem</b> — "
                     "e com a taxa turística em linha própria, porque em Barcelona ela "
                     "passou a ser uma das maiores da conta: € 7 por pessoa por noite "
                     "num hotel de três estrelas, fora do preço do quarto."),
        "hosp": [
            {"k": "media", "rot": "Média dos 12 meses (cálculo nosso, INE)",
             "ref": MEDIA, "mn": MEDIA, "mx": MEDIA},
            {"k": "baixa", "rot": "Dezembro — o mês mais barato do ano (INE)",
             "ref": ADR["dez/2025"], "mn": ADR["dez/2025"], "mx": ADR["dez/2025"]},
            {"k": "alta", "rot": "Maio — o mês mais caro do ano (INE)",
             "ref": ADR["mai/2026"], "mn": ADR["mai/2026"], "mx": ADR["mai/2026"]},
        ],
        "hospPadrao": "media",
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em "
                  "euro. Mude as datas e o número de pessoas, troque a época da "
                  "hospedagem, desmarque o que você não vai fazer, e a conta se refaz "
                  "na hora."),
        "nota_calc": (
            "As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
            "quarto. <b style=\"color:var(--gelo)\">A diária vem do INE espanhol, aberta "
            "por ponto turístico</b> — Barcelona é um deles.<br>"
            "<b>A taxa turística escala pelas suas noites</b>, até o teto legal de 7, e "
            "está calculada para hotel de até três estrelas: num quatro estrelas são "
            "€ 8,40 por noite; num apartamento turístico, € 9,50; num cinco estrelas, "
            "€ 12. Linhas marcadas como piso podem subir no caixa."),
        "linhas": [
            # ---------------------------------------------------- ingressos
            ("ingresso", 26.00, "Sagrada Família, basílica com audioguia", "€ 26,00",
             "Fonte: página de preços do site oficial (sagradafamilia.org), consultada "
             "em 18/out/2026.<br>"
             "<b>Com as torres são € 36.</b> Maior de 65: € 21; menor de 30 e "
             "estudante: € 24; menor de 11: não paga.<br>"
             "<b>Nominativo, com documento original na entrada, e sem troca nem "
             "devolução</b> — só se o ingresso não foi validado e a culpa for do "
             "monumento (fechamento, mau tempo). <b>Só se vende on-line.</b>"),
            ("ingresso", 18.00, "Park Güell", "€ 18,00",
             "Fonte: <i>Prices and times</i> do site oficial (parkguell.barcelona), "
             "consultada em 18/out/2026. IVA de 21% incluído.<br>"
             "De 7 a 12 anos e maior de 65: € 13,50. Até 6 anos: € 0, com ingresso "
             "emitido.<br>"
             "<b>30 minutos de tolerância depois da hora marcada; depois disso perde.</b> "
             "Compra obrigatoriamente antecipada e on-line."),
            ("ingresso", 29.00, "Casa Batlló, visita geral", "desde € 29,00",
             "Fonte: página de ingressos on-line do site oficial (casabatllo.es), "
             "consultada em 18/out/2026.<br>"
             "<span class=\"flag\">É piso, não total</span> "
             "o site publica <i>“From € 29”</i> e diz que comprar com antecedência "
             "economiza <i>“up to € 15 per person”</i> — <b>o preço muda com a data e a "
             "tabela não está publicada</b>. Menor de 12 anos não paga; estudante e de 13 "
             "a 17 anos, € 6 a menos; maior de 65, € 3 a menos."),
            ("ingresso", 29.00, "La Pedrera, visita Essential", "desde € 29,00",
             "Fonte: página de ingressos do site oficial (lapedrera.com), consultada em "
             "18/out/2026. <b>“From € 29”, válida até 1º de novembro de 2026</b> "
             "(<i>“Until 01/11/26”</i>).<br>"
             "Sunset, depois das 17h30: desde € 25. Menor de 12 anos não paga. "
             "<b>Não há preço de estudante nem de maior de 65 publicado.</b> Combinada "
             "com Sant Pau ou com o Palau: € 42, abaixo das duas separadas."),
            ("ingresso", 12.00, "Museu Picasso", "€ 12,00",
             "Fonte: <i>Buy tickets and opening hours</i> do site oficial "
             "(museupicassobcn.cat), consultada em 18/out/2026. <b>€ 12 on-line, € 13 "
             "na bilheteria.</b> Reduzida € 7; menor de 18 não paga.<br>"
             "<b>Há como não pagar esta linha: quinta-feira das 16h às 19h e primeiro "
             "domingo do mês, com reserva</b> — e a reserva gratuita <b>abre quatro "
             "dias antes, às 10h</b>. <b>Fecha toda segunda.</b>"),
            ("ingresso", 12.00, "MNAC", "€ 12,00",
             "Fonte: <i>Opening hours and prices</i> do site oficial "
             "(museunacional.cat), consultada em 18/out/2026. <b>Vale dois dias</b> "
             "dentro de um mês. Menor de 16 e maior de 65 não pagam.<br>"
             "<b>Há como não pagar esta linha: todo sábado a partir das 15h e primeiro "
             "domingo do mês</b>, reservando on-line. <b>Fecha segunda.</b> A entrada "
             "básica de € 2 dá o edifício e o terraço-mirante sem as salas."),
            ("ingresso", 12.00, "Castell de Montjuïc", "€ 12,00",
             "Fonte: <i>Planning your visit</i> do site oficial, no domínio do "
             "Ayuntamiento, consultada em 18/out/2026. Reduzida € 8; menor de 16 não "
             "paga.<br>"
             "<b>Há como não pagar esta linha: todo domingo a partir das 15h e primeiro "
             "domingo do mês.</b> <b>Só vende no site próprio</b>, sem devolução. O "
             "funicular até lá está dentro do bilhete simples da TMB."),
            ("ingresso", 17.00, "Recinte Modernista de Sant Pau, depois das 14h", "€ 17,00",
             "Fonte: página da visita livre do site oficial (santpaubarcelona.org), "
             "consultada em 18/out/2026. <b>€ 18 até as 14h, € 17 depois</b> — a linha "
             "usa o da tarde, que é o que o roteiro faz: manhã na Sagrada Família, dez "
             "minutos a pé pela Avinguda de Gaudí, Sant Pau depois das 14h.<br>"
             "Reduzida € 11,90 (12 a 24 anos, maior de 65); menor de 12 não paga. "
             "<b>Abre todos os dias</b>, inclusive segunda."),
            ("ingresso", 16.00, "Catedral de Barcelona, visita turística", "€ 16,00",
             "Fonte: página de horários da visita turística do site oficial "
             "(catedralbcn.org), consultada em 18/out/2026. Isento de IVA. Reduzida "
             "€ 14 (estudante até 25 anos).<br>"
             "<b>Domingo só das 14h às 17h.</b> "
             "<span class=\"flag\">Lacuna declarada</span> a página não diz o que os "
             "€ 16 incluem nem publica o horário de culto, em que a entrada é livre."),
            ("ingresso", 20.00, "Palau de la Música Catalana, com audioguia", "€ 20,00",
             "Fonte: <i>Visit the Palau</i> do site oficial (palaumusica.cat), "
             "consultada em 18/out/2026. Guiada: € 24, 50 minutos.<br>"
             "<span class=\"flag\">Lacuna declarada</span> o site diz que há reduzida "
             "para crianças, maiores de 65 e famílias <b>e não publica o valor</b>, nem a "
             "idade da gratuidade. Combinado com La Pedrera: € 42."),
            ("ingresso", 28.00, "Museu do Barça, com o mirante das obras", "desde € 28,00",
             "Fonte: página de ingressos do museu em fcbarcelona.com, consultada em "
             "18/out/2026. <b>“From € 28”</b>, com o <i>Construction Viewpoint</i>.<br>"
             "<b>O tour clássico do estádio não está à venda na página consultada</b>: "
             "o Spotify Camp Nou segue em obras (a imprensa de agosto de 2026 fala em "
             "terceiro anel no início de 2027 e cobertura a partir de junho de 2027 — "
             "<b>não é fonte oficial</b>). Spotify Camp Nou Experience, com vista "
             "panorâmica: desde € 69. <b>Quem vai pelo gramado, desmarca.</b>"),
            # ---------------------------------------------------- transporte
            ("fixo", 11.80, "Metrô do aeroporto, ida e volta", "€ 11,80",
             "Fonte: página de tarifas da <b>TMB</b> (tmb.cat), consultada em "
             "18/out/2026: <b>bilhete de aeroporto € 5,90</b>, <i>“A metro journey "
             "including Aeroport T1 and Aeroport T2 stations”</i>, na linha L9 Sud. A "
             "linha conta ida e volta.<br>"
             "<b>A T-casual não vale nas estações do aeroporto</b> — a própria TMB avisa. "
             "O Hola Barcelona Travel Card (<i>“From € 12.50”</i>) inclui o aeroporto, "
             "mas a página não publica a tabela por dias.<br>"
             "<span class=\"flag\">Lacuna declarada</span> <b>o Aerobus não publica o "
             "preço em texto</b>: a tarifa do site oficial está só numa imagem "
             "decorativa, e nenhuma página do domínio traz o valor. Sites de terceiros "
             "citam € 7,45 a € 7,75. <b>Não confirmamos.</b>"),
            ("fixo", 13.00, "T-casual, 10 viagens", "€ 13,00",
             "Fonte: página de tarifas da <b>TMB</b>, consultada em 18/out/2026: "
             "<i>“T-casual — From: € 13”</i>, 10 viagens, uma pessoa, zona 1. O "
             "bilhete simples custa <b>€ 2,90</b> e inclui o funicular de Montjuïc; a "
             "T-dia (24 horas) custa € 12.<br>"
             "<b>Dez viagens em cinco dias é suposição desta ficha, não dado.</b> "
             "Passeig de Gràcia, o Gòtic e o Born se fazem a pé; o metrô é para Park "
             "Güell, Montjuïc, Sant Pau e Camp Nou. Quem andar mais, desmarca.<br>"
             "A imprensa catalã registra a tabela em vigor desde 15 de janeiro de 2026; "
             "a página da TMB diz só <i>“until the next fare change”</i>."),
            # ---------------------------------------------------- taxa
            ("taxa", NOITES * TAXA_NOITE,
             "Taxa turística (IEET + recargo de Barcelona), 4 noites", "€ 28,00",
             "Fonte: <b>Agència Tributària de Catalunya</b>, tabela do IEET em vigor de "
             "<b>01.04.2026 a 31.03.2027</b> (atc.gencat.cat), consultada em "
             "18/out/2026.<br>"
             "<b>€ 7,00 por pessoa por noite num hotel de até três estrelas</b>: "
             "€ 2,00 de imposto catalão mais <b>€ 5,00 de recargo do Ayuntamiento de "
             "Barcelona</b>. Quatro estrelas: € 8,40. Apartamento turístico: € 9,50. "
             "Cinco estrelas: € 12,00. Albergue: € 6,00.<br>"
             "<b>Teto de 7 noites; menor de 17 não paga.</b> O calculador escala pelas "
             "suas noites, até o teto.<br>"
             "<b>Dobrou em 1º de abril de 2026</b> (Llei 2/2026) <b>e já tem aumento "
             "marcado</b>: o recargo vai a € 6 em 1º de abril de 2027 e a € 7 em 2028. "
             "<b>Em reserva antecipada vale a tarifa do dia do pagamento</b>, se "
             "imposto e recargo forem pagos junto — quem paga tudo antes de abril de "
             "2027 trava os € 5.<br>"
             "<b>Não vem no preço da reserva</b>: o hotel cobra à parte.",
             {"noite": "%.4f" % TAXA_NOITE, "teto": "7",
              "rot": "Taxa turística (IEET + recargo de Barcelona), {n}"}),
            # ---------------------------------------------------- hospedagem
            ("hosp", None, "Hospedagem, 4 noites", "€ 717,79",
             "Fonte: <b>INE</b>, <i>Indicadores de Rentabilidad del Sector Hotelero</i>, "
             "tabela 46298 — tarifa média diária (ADR) por <b>ponto turístico</b>, série "
             "<i>Barcelona, total de categorias</i>, lida pela API do INE em "
             "29/out/2026.<br>"
             "<b>O valor mostrado usa a média dos 12 meses de out/2025 a set/2026: "
             "€ 179,45 por quarto por noite.</b> Os doze valores são do INE; <b>a média "
             "é cálculo nosso</b>, e está rotulada como tal no seletor.<br>"
             "<b>Maio é o mês mais caro (€ 223,37) e dezembro o mais barato "
             "(€ 131,41): 70% de diferença pelo mesmo quarto.</b> Agosto (€ 175,42) "
             "fica perto da média — Barcelona não tem o agosto ao contrário de "
             "Granada.<br>"
             "Troque a época no seletor acima e veja a conta mudar.<br>"
             "ADR é por <b>quarto ocupado</b>, não por pessoa, e cobre <b>hotéis</b>, "
             "não apartamentos. A conta divide por duas pessoas por quarto, como nas "
             "outras fichas. <b>A taxa turística está na linha de cima, não aqui.</b>"),
        ],
        "rodape_tabela": (
            "Valores em euro, por pessoa, apurados em fonte oficial em 18 de outubro "
            "de 2026. <b>Quatro linhas estão marcadas como piso</b> — Casa Batlló, La "
            "Pedrera, o museu do Barça e, por tabela, a Sagrada Família sem as torres — "
            "porque o preço final depende da data ou da modalidade.<br>"
            "<b>Duas coisas mudam esta conta mais que qualquer corte.</b><br>"
            "<b>A primeira: três tardes tiram € 36.</b> Picasso na quinta das 16h às "
            "19h (com reserva que abre quatro dias antes), MNAC no sábado a partir das "
            "15h, Montjuïc no domingo a partir das 15h. <b>Uma viagem de quinta a "
            "segunda pega as três.</b> No primeiro domingo do mês, os três são "
            "gratuitos o dia inteiro.<br>"
            "<b>A segunda: a taxa turística é por pessoa, por noite, fora do preço do "
            "quarto</b> — € 7 num três estrelas, € 12 num cinco —, dobrou em abril de "
            "2026 e sobe de novo em abril de 2027. É a única linha desta tabela com "
            "aumento já publicado."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. Os ingressos vêm das "
            "páginas de preços dos próprios monumentos e museus — Sagrada Família, "
            "Park Güell, Casa Batlló, La Pedrera, Museu Picasso, MNAC, Castell de "
            "Montjuïc, Sant Pau, Catedral, Palau de la Música e FC Barcelona. O "
            "transporte vem da TMB. A taxa turística vem da tabela oficial da "
            "Agència Tributària de Catalunya, e a hospedagem, dos Indicadores de "
            "Rentabilidad del Sector Hotelero do INE espanhol, lidos pela API. "
            "<b>Nenhum valor veio de agregador de viagem.</b> O que ficou sem resposta "
            "está dito na linha: o preço do Aerobus, que o site oficial só mostra em "
            "imagem; as tarifas reduzidas do Palau; o horário do museu do Barça; e o "
            "valor final dos ingressos vendidos como “a partir de”."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
]
_vistos, _limpo = set(), []
for _slug, _nome in base.CIDADES:
    if _slug not in _vistos:
        _vistos.add(_slug)
        _limpo.append((_slug, _nome))
base.CIDADES = _limpo

base.FICHAS = FICHAS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
