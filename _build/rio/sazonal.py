# -*- coding: utf-8 -*-
"""O ano do Rio mes a mes: diaria, ocupacao e clima. Apuracao de 23/out/2026.

Os dois conjuntos entram aqui uma vez, digitados da fonte, e as paginas
importam daqui. A pagina "Quando ir" e o unico consumidor por enquanto.

DIARIA E OCUPACAO - HotelInvest e FOHB, Panorama da Hotelaria Brasileira,
20a edicao, pagina 31, "Historico de desempenho mensal", Rio de Janeiro,
2025. Valores REAIS, corrigidos para dez/2025 (o proprio grafico diz).
Media de hoteis filiados, cidade inteira: nao ha recorte por bairro.
Texto extraido do PDF em _build/rio/fontes/fohb-panorama-20-rio.txt.
Conferido na apuracao: diaria x ocupacao da o RevPAR publicado no mesmo
grafico (jan 609 x 76% = 463, publicado 465; mar 750 x 77% = 577,
publicado 581; jun 534 x 63% = 336, publicado 337; dez 732 x 67% = 490,
publicado 488). E junho, marco, dezembro e a media de R$ 610 sao os
mesmos que a ficha de custos ja publicava desde setembro.

CLIMA - Climatempo, climatologia de Rio de Janeiro, "valores calculados a
partir de uma serie de dados de 30 anos observados",
climatempo.com.br/climatologia/321/riodejaneiro-br, consultado em
23/out/2026. Junho, julho, agosto e janeiro batem com o que as fichas ja
citavam.
"""

FONTE_DIARIA = ("HotelInvest e FOHB, Panorama da Hotelaria Brasileira, 20ª edição, página 31: série mensal "
                "do Rio de Janeiro em 2025, em valores reais de dezembro de 2025, consultada em 23/out/2026")
FONTE_CLIMA = ("Climatempo, climatologia do Rio de Janeiro, médias de 30 anos observados, consultada em "
               "23/out/2026")
MEDIA_ANO = 610          # diaria media de 2025, pagina 30 do mesmo Panorama

MESES = [
    # mes,         diaria, ocupacao %, minima, maxima, chuva mm
    ("janeiro",    609, 76, 22, 31, 236),
    ("fevereiro",  620, 80, 22, 31, 169),
    ("março",      750, 77, 22, 29, 175),
    ("abril",      702, 76, 20, 28, 92),
    ("maio",       543, 67, 17, 25, 63),
    ("junho",      534, 63, 16, 25, 38),
    ("julho",      548, 67, 15, 25, 37),
    ("agosto",     548, 71, 16, 26, 35),
    ("setembro",   543, 74, 18, 27, 68),
    ("outubro",    552, 75, 19, 28, 105),
    ("novembro",   609, 74, 20, 28, 172),
    ("dezembro",   732, 67, 22, 30, 199),
]
