# -*- coding: utf-8 -*-
"""Gramado: o vigesimo segundo destino, em dez pontos e tres grupos.

Mesmo molde do barcelona/dados.py.

O ACHADO PRINCIPAL: O PARQUE DO CARACOL COBRA O DOBRO DE QUEM NAO E GAUCHO
--------------------------------------------------------------------------
A pagina de compra oficial (parquecaracol.com.br/pt/comprar-ingresso),
lida em 18/10/2026, tem tres abas de categoria. Na de "Brasileiros e
Estrangeiros", o Bilhete Caracol custa a partir de R$ 134,90 a inteira.
Na de "Gauchos e Residentes do RS", o mesmo parque, pelo Bilhete Gaucho,
custa a partir de R$ 67,00 o adulto - metade, exatos 50,3% a menos. E na
de "Canelense e Gramadense", o morador entra de graca com comprovante.
Quem chega de Sao Paulo paga o dobro do vizinho de Porto Alegre pela
mesma cascata.

O SEGUNDO: A TAXA DE TURISMO FOI REVOGADA, E O QUE SOBROU E VOLUNTARIO
--------------------------------------------------------------------------
A Taxa de Turismo Sustentavel (Lei 3.461/2015), R$ 3,43 por dia e por
apartamento, foi revogada pela Camara em 13/abr/2026 (PLO 077/2025 e
PLC 004/2025), depois de acordo com o Ministerio Publico do RS, que a
considerava inconstitucional. No lugar, o Gramado Canela Convention &
Visitors Bureau anunciou em maio uma "Room Tax" do mesmo valor - mas
VOLUNTARIA: "sera opcional o pagamento por parte dos hospedes". Quem ve a
linha no check-out pode recusar. Nao achamos a sancao publicada, e isso
esta dito.

O TERCEIRO: QUARTA-FEIRA FECHA DOIS DOS GRANDES PARQUES
--------------------------------------------------------------------------
O Mundo a Vapor diz "fechado nas quartas-feiras". O calendario de compra
da Snowland marca TODAS as quartas de outubro de 2026 como "Parque
Fechado". O roteiro foge da quarta.

O QUE FICOU SEM RESPOSTA, E ESTA DITO EM CADA FICHA
--------------------------------------------------------------------------
    hospedagem          nenhum orgao publica diaria media de Gramado;
                        o FOHB/HotelInvest cobre capitais. Sem estimativa.
    Mundo a Vapor       a pagina mostra dois valores por passaporte
                        (129 e 149) sem dizer qual e o promocional
    Snowland            preco por data, em quatro temporadas; so lemos
                        uma (22/10, media temporada)
    Dreamland, Bustour  "a partir de"
    Le Jardin           o site recusou a conexao (403); ficou de fora
    Natal Luz           o calendario das noites de cada espetaculo nao
                        estava na pagina inicial do site oficial

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
#  GRAMADO
# =====================================================================
GRAMADO = {
    "slug": "gramado",
    "nome": "Gramado",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "Gramado: 10 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 10 pontos de Gramado e Canela, com o Parque "
                  "do Caracol que cobra o dobro de quem não é gaúcho e a taxa de turismo "
                  "que a Câmara revogou em 2026."),
    "abertura": ("Dez pontos de Gramado e Canela com preço, horário e fonte conferidos em "
                 "18 de outubro de 2026 — e duas coisas que os guias não dizem: <b>o "
                 "Parque do Caracol vende o mesmo bilhete por R$ 134,90 a quem vem de fora "
                 "do Rio Grande do Sul e por R$ 67,00 a quem é gaúcho</b>, na própria "
                 "página oficial. <b>E a taxa de turismo de Gramado foi revogada pela "
                 "Câmara em abril de 2026</b> — o que pode aparecer no check-out agora é "
                 "uma “Room Tax” do mesmo valor, que é voluntária."),
    "busca": ("gramado canela serra gaucha rio grande do sul rs brasil natal luz snowland "
              "mini mundo gramadozoo dreamland museu de cera mundo a vapor caracol cascata "
              "lago negro rua coberta taxa de turismo"),
    "grupos": [
        {"id": "g1", "titulo": "O Natal Luz: o que é pago e o que é de graça",
         "intro": ("De 22 de outubro de 2026 a 17 de janeiro de 2027 a cidade inteira "
                   "vira evento. Quatro espetáculos cobram, e cinco atrações na rua não.")},
        {"id": "g2", "titulo": "Os parques: cinco ingressos, cinco regras",
         "intro": ("Snowland, Mini Mundo, GramadoZoo, Dreamland e Mundo a Vapor — cada um "
                   "com seu jeito de cobrar: preço por data, meia que vai até 15 anos, "
                   "valor único, “a partir de” e dois números na mesma página.")},
        {"id": "g3", "titulo": "Canela, o que não cobra e a conta da cama",
         "intro": ("A cascata que cobra o dobro de quem não é gaúcho, os lagos e a Rua "
                   "Coberta que não cobram nada, e a hospedagem — sem diária oficial "
                   "publicada e com a taxa que acabou.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - Natal Luz
        # =============================================================
        {
            "id": "natal-luz-pagos",
            "grupo": "g1",
            "nome": "Natal Luz: os quatro espetáculos pagos",
            "tag": "Evento",
            "preco_val": "R$ 120 a R$ 420",
            "preco_nota": "inteira; 5% a menos até 21 de outubro",
            "campos": [
                ("Valor dos ingressos",
                 "Fonte: site oficial do 41º Natal Luz de Gramado "
                 "(natalluzdegramado.com.br), consultado em 18/out/2026.<br>"
                 "<b>O Grande Desfile de Natal</b>, na Expogramado: <b>inteira R$ 420</b>; "
                 "“a partir de R$ 210” (a meia).<br>"
                 "<b>Nativitaten</b>, no Serra Park: <b>inteira R$ 360</b>; a partir de "
                 "R$ 180.<br>"
                 "<b>O Brilho do Natal</b> e <b>Natal Luz In Concert</b>, no Palácio dos "
                 "Festivais: <b>inteira R$ 120</b> cada; a partir de R$ 60.<br>"
                 "<b>O lote atual tem 5% de desconto e acaba em 21 de outubro</b> — o site: "
                 "<i>“Este é o lote com 5% de desconto, e ele termina em 21 out.”</i> Nele, o "
                 "desfile sai por R$ 399, o Nativitaten por R$ 342 e os shows por R$ 114. "
                 "Há ainda 10% para cartão Bradesco, somados depois."),
                ("As datas",
                 "<b>De 22 de outubro de 2026 a 17 de janeiro de 2027</b>, segundo o "
                 "site oficial. É a 41ª edição.<br>"
                 + FLAG % "Lacuna declarada" +
                 "<b>a página inicial do site não traz o calendário das noites de cada "
                 "espetáculo</b> — o desfile e o Nativitaten não acontecem todo dia. "
                 "Escolha a noite no seletor de compra antes de montar o roteiro em cima "
                 "dela."),
                ("Onde fica",
                 mapa("Expogramado, Av. das Hortênsias, Gramado, RS")),
            ],
        },
        {
            "id": "natal-luz-gratis",
            "foto": {"arq": "gramado/natal-luz-gratis.webp",
                     "alt": "Ruas de Gramado iluminadas para o Show de Acendimento do Natal Luz, à noite",
                     "cred": "Larissa Fraga · CC BY 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Natal Luz: as cinco atrações gratuitas",
            "tag": "Evento na rua",
            "preco_val": "Grátis",
            "preco_nota": "a Vila e o Acendimento vão só até 10 de janeiro",
            "campos": [
                ("O que não cobra",
                 "Fonte: site oficial do Natal Luz, consultado em 18/out/2026.<br>"
                 "<b>Vila de Natal</b>, na Praça das Etnias: todos os dias, <b>9h às "
                 "21h</b>.<br>"
                 "<b>Show de Acendimento</b>, no Palácio dos Festivais: todos os dias, "
                 "<b>20h</b>.<br>"
                 "<b>Parada de Natal</b>, na Av. Borges de Medeiros: <b>sexta, sábado e "
                 "domingo, 15h</b>.<br>"
                 "<b>Palco da Rua Coberta</b>: terça a domingo, 18h30, e também 11h30 no "
                 "sábado e no domingo.<br>"
                 "<b>Caminho de Luzes</b>: terças, 18h30, da Praça das Etnias à Rua "
                 "Coberta."),
                ("A data que não bate",
                 FLAG % "Fontes divergem" +
                 "<b>o mesmo site diz que o Natal Luz vai até 17 de janeiro e que a Vila "
                 "de Natal e o Show de Acendimento vão até 10 de janeiro.</b> Quem chega "
                 "entre 11 e 17 de janeiro pega os espetáculos pagos, mas talvez não a "
                 "Vila nem o Acendimento. Confira perto da data."),
                ("Onde fica",
                 mapa("Praça das Etnias, Gramado, RS")),
            ],
        },
        # =============================================================
        #  g2 - os parques
        # =============================================================
        {
            "id": "snowland",
            "foto": {"arq": "gramado/snowland.webp",
                     "alt": "Esculturas de ursos polares na área de neve da Snowland, em Gramado",
                     "cred": "MTur Destinos · domínio público · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Snowland",
            "tag": "Parque de neve",
            "preco_val": "desde R$ 144,50",
            "preco_nota": "preço muda com a data; quarta fecha em outubro",
            "campos": [
                ("Valor da entrada, e por que muda",
                 "Fonte: loja oficial de ingressos (ingressos.snowland.com.br), consultada "
                 "em 18/out/2026, para a data de <b>22 de outubro de 2026, quinta-feira</b>, "
                 "marcada como <b>média temporada</b>.<br>"
                 "<b>Ingresso: a partir de R$ 144,50</b>, com o kit de roupas (botas, "
                 "calça, jaqueta e luvas) e as atrações da área de neve (−5 °C), do "
                 "vilarejo alpino com patinação (15 °C) e da área climatizada.<br>"
                 "<b>Meia-entrada: a partir de R$ 86,70</b>, com documento original na "
                 "bilheteria — <i>“Não serão aceitos comprovantes de matrícula ou "
                 "pagamento.”</i><br>"
                 "<b>Morador: R$ 86,70</b>, para quinze municípios da serra, com "
                 "comprovante de residência.<br>"
                 "<b>Menor de 4 anos não paga.</b> Aniversariante ganha cortesia no dia.<br>"
                 "<b>O preço é por data, em quatro temporadas</b> — baixa, média, alta e "
                 "super — e só lemos a média. <b>R$ 144,50 é piso.</b> E o site avisa: "
                 "<i>“O valor do ingresso na bilheteria não possui desconto de compra "
                 "antecipada.”</i>"),
                ("Dias e horários",
                 "<b>Todos os dias, 10h às 17h</b>, diz a página.<br>"
                 "<b>Mas o calendário de compra de outubro de 2026 marca todas as quartas "
                 "— 7, 14, 21 e 28 — como “Parque Fechado”.</b> Confira o dia no "
                 "calendário antes de montar a viagem."),
                ("Onde fica",
                 mapa("Snowland, RS-235, Linha Carazal 9009, Gramado, RS")),
            ],
        },
        {
            "id": "mini-mundo",
            "foto": {"arq": "gramado/mini-mundo.webp",
                     "alt": "Vista geral das miniaturas do Mini Mundo, com casas, trilhos e jardins",
                     "cred": "Cesar Cardoso · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Mini Mundo",
            "tag": "Parque",
            "preco_val": "R$ 156",
            "preco_nota": "meia de 3 a 15 anos e acima de 60",
            "campos": [
                ("Valor da entrada",
                 "Fonte: loja oficial (ingressos.minimundo.com.br), consultada em "
                 "18/out/2026, para a mesma data.<br>"
                 "<b>Inteira: R$ 156,00.</b><br>"
                 "<b>Meia-entrada infantil, de 3 até 15 anos: R$ 78,00.</b> A meia de "
                 "criança aqui vai <b>até 15 anos</b> — na maioria dos parques da serra "
                 "ela para em 12.<br>"
                 "<b>Meia sênior, acima de 60: R$ 78,00.</b><br>"
                 "Havia ainda dois combos no dia: 2 adultos por R$ 216 e um combo de Dia "
                 "das Crianças por R$ 256."),
                ("Dias e horários",
                 "<b>Todos os dias, 9h às 17h</b>, ao ar livre. O próprio site diz que "
                 "<i>“dias de chuva também são lindos por aqui”</i> — ou seja, não fecha "
                 "por chuva."),
                ("Onde fica",
                 mapa("Mini Mundo, Rua Horácio Cardoso 291, Gramado, RS")),
            ],
        },
        {
            "id": "gramadozoo",
            "foto": {"arq": "gramado/gramadozoo.webp",
                     "alt": "Duas araras-canindé, azul e amarela, no GramadoZoo",
                     "cred": "diegodobelo · CC BY-SA 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "GramadoZoo",
            "tag": "Zoológico",
            "preco_val": "R$ 115",
            "preco_nota": "valor único; estacionamento R$ 20",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de funcionamento do site oficial (gramadozoo.com.br), "
                 "consultada em 18/out/2026.<br>"
                 "<b>Ingresso único: R$ 115,00</b> — <i>“Ingresso único com valor de "
                 "R$ 115,00”</i>, sem meia publicada na página.<br>"
                 "<b>Menor de 3 anos não paga.</b><br>"
                 "<b>Estacionamento: R$ 20,00</b>, valor único."),
                ("Dias e horários",
                 "<b>10h às 16h</b>, e 16h é a <b>última entrada</b>.<br>"
                 "Outubro, novembro e dezembro de 2026: todos os dias, <b>exceto 9 de "
                 "novembro e 25 de dezembro</b>.<br>"
                 "<b>E chuva forte fecha:</b> <i>“Em dias de chuva forte, o GramadoZoo "
                 "poderá não abrir, ou fechar sem aviso prévio.”</i>"),
                ("Onde fica",
                 mapa("GramadoZoo, Gramado, RS")),
            ],
        },
        {
            "id": "dreamland",
            "foto": {"arq": "gramado/dreamland.webp",
                     "alt": "Figura de cera sentada num ambiente de época no Dreamland Museu de Cera, em Gramado",
                     "cred": "Cesar Cardoso · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Dreamland Museu de Cera",
            "tag": "Museu",
            "preco_val": "desde R$ 89,99",
            "preco_nota": "passaporte com mais 6 atrações desde R$ 219,99",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de ingressos do site oficial (dreamland.com.br), "
                 "consultada em 18/out/2026.<br>"
                 "<b>Museu de Cera de Gramado: “A partir de R$ 89,99”.</b><br>"
                 "<b>Passaporte “Dreamland + 6”: a partir de R$ 219,99</b> — o museu mais "
                 "seis atrações do mesmo grupo na Av. das Hortênsias (Hollywood Dream Cars, "
                 "Super Carros, Dreams Motor Show, Vale dos Dinossauros e outras).<br>"
                 "<b>Dois “a partir de”: são pisos.</b> A página não publica meia, idade "
                 "da gratuidade nem horário."),
                ("A conta do passaporte",
                 "<b>O passaporte só compensa a partir da terceira atração.</b> Com o "
                 "museu a R$ 89,99, duas atrações avulsas no mesmo patamar já passam de "
                 "R$ 180; o passaporte inteiro sai por R$ 219,99. Quem quer só o museu "
                 "de cera, compra só o museu."),
                ("Onde fica",
                 mapa("Dreamland Museu de Cera, Av. das Hortênsias 5507, Gramado, RS")),
            ],
        },
        {
            "id": "mundo-a-vapor",
            "foto": {"arq": "gramado/mundo-a-vapor.webp",
                     "alt": "A fachada do Mundo a Vapor, em Canela, com a locomotiva que atravessa a parede",
                     "cred": "Mundo a Vapor · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Mundo a Vapor (Canela)",
            "tag": "Parque",
            "preco_val": "R$ 149",
            "preco_nota": "a página mostra 129 e 149 sem dizer qual vale; fecha quarta",
            "campos": [
                ("Valor da entrada, e os dois números",
                 "Fonte: site oficial (mundoavapor.com.br), consultado em 18/out/2026.<br>"
                 "<b>Passaporte adulto, de 13 a 59 anos:</b> a página mostra <b>R$ 129,00 "
                 "e R$ 149,00</b> no mesmo cartão, sem rótulo de promoção. "
                 "<b>Esta ficha usa R$ 149, o maior</b> — errar para cima não estraga "
                 "viagem.<br>"
                 "<b>Especial: R$ 89 ou R$ 109</b>, o mesmo problema. Vale para criança de "
                 "4 a 12 anos, professor, estudante, sênior, PCD e doador de sangue.<br>"
                 "<b>VIP: R$ 159 ou R$ 179</b>, com roda-gigante em cabine temática e uma "
                 "bebida.<br>"
                 "O passaporte inclui a visita guiada nas 10 salas, um passeio de trem no "
                 "bosque e uma volta na roda-gigante."),
                ("Dias e horários",
                 "<b>9h às 18h30</b>, e <b>“fechado nas quartas-feiras”</b>, como diz o "
                 "site. É o segundo grande parque da serra que fecha na quarta — a "
                 "Snowland é o outro."),
                ("Onde fica",
                 mapa("Mundo a Vapor, Canela, RS")),
            ],
        },
        # =============================================================
        #  g3 - Canela, o gratis e a cama
        # =============================================================
        {
            "id": "parque-caracol",
            "foto": {"arq": "gramado/parque-caracol.webp",
                     "alt": "A Cascata do Caracol caindo entre o paredão de rocha e a mata, em Canela",
                     "cred": "Tiago Fioreze · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Parque do Caracol (Canela)",
            "tag": "Cascata",
            "preco_val": "R$ 134,90",
            "preco_nota": "R$ 67 para gaúcho; morador de Canela e Gramado não paga",
            "campos": [
                ("O mesmo bilhete, três preços",
                 "Fonte: página de compra oficial (parquecaracol.com.br/pt/comprar-ingresso), "
                 "consultada em 18/out/2026. A página tem três abas de categoria.<br>"
                 "<b>“Brasileiros e Estrangeiros”: Bilhete Caracol, inteira a partir de "
                 "R$ 134,90</b>; meia a partir de R$ 67,00.<br>"
                 "<b>“Gaúchos e Residentes do RS”: Bilhete Gaúcho, adulto a partir de "
                 "R$ 67,00</b>; criança a partir de R$ 33,50. A página o chama de "
                 "<i>“um ingresso promocional”</i>, para morador e nascido no RS, com "
                 "comprovação.<br>"
                 "<b>“Canelense e Gramadense”: grátis</b>, com comprovante de residência "
                 "no nome e documento com foto.<br>"
                 "<b>Quem vem de São Paulo paga o dobro de quem vem de Porto Alegre pela "
                 "mesma cascata.</b> Menor de 3 anos não paga; meia de 4 a 12 anos e acima "
                 "de 60, só no Bilhete Caracol."),
                ("O que é cobrado à parte",
                 "<b>Corajoso</b> (plataforma suspensa sobre a cascata) e <b>Ousado</b> "
                 "(a descida pela cascata a 140 m) são pagos à parte. Em combo: Caracol + "
                 "Corajoso R$ 159,90 a inteira; Caracol + Ousado a partir de R$ 469,90."),
                ("Dias e horários",
                 "<b>Segunda a sexta, 9h às 17h</b> (entrada até 16h30).<br>"
                 "<b>Fim de semana, feriado e emenda, 9h às 18h</b> (entrada até 17h30)."),
                ("Onde fica",
                 mapa("Parque do Caracol, Rodovia RS 466 km 0, Canela, RS")),
            ],
        },
        {
            "id": "lago-negro",
            "foto": {"arq": "gramado/lago-negro.webp",
                     "alt": "O Lago Negro, em Gramado, com as árvores escuras refletidas na água",
                     "cred": "Amanda Likes · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Lago Negro, Rua Coberta e o que não cobra",
            "tag": "Gratuito",
            "preco_val": "Grátis",
            "preco_nota": "o pedalinho cobra; o valor não está publicado",
            "campos": [
                ("A lista oficial do que é grátis",
                 "Fonte: <b>Secretaria de Turismo de Gramado</b>, portal oficial "
                 "gramadoinesquecivel.tur.br, seção <i>Atrativos gratuitos</i>, consultada "
                 "em 18/out/2026.<br>"
                 "<b>Lago Negro:</b> <i>“Acesso livre / Cobrança de ingresso para "
                 "pedalinho”</i>. <b>Aberto 24h</b>; pedalinhos das <b>8h30 às 18h</b>.<br>"
                 "<b>Rua Coberta:</b> <i>“Acesso livre”</i>, horário livre — a que liga a "
                 "Borges de Medeiros à Garibaldi, e é a saída da cidade para dia de "
                 "chuva.<br>"
                 "Na mesma lista oficial: o <b>Lago Joaquina Rita Bier</b>, o <b>Belvedere "
                 "do Vale do Quilombo</b>, a <b>Igreja do Relógio</b>, o <b>Espaço Cultural "
                 "Museu do Trem</b>, o <b>Museu Municipal Professor Hugo Daros</b> e a "
                 "<b>Rótula das Bandeiras</b>."),
                ("O que não está publicado",
                 FLAG % "Lacuna declarada" +
                 "<b>o portal diz que o pedalinho cobra e não diz quanto.</b> Guias de "
                 "viagem citam de R$ 20 a R$ 50; não confirmamos nenhum."),
                ("Onde fica",
                 mapa("Lago Negro, Rua A. J. Renner, Gramado, RS")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem, e a taxa que acabou",
            "tag": "Conta, não lugar",
            "preco_val": "sem dado oficial",
            "preco_nota": "a Room Tax de R$ 3,43 é voluntária",
            "campos": [
                ("Por que não há diária nesta ficha",
                 FLAG % "Lacuna declarada" +
                 "<b>Nenhum órgão publica a diária média de Gramado.</b> O Panorama da "
                 "Hotelaria Brasileira (FOHB/HotelInvest), que usamos no Rio, cobre "
                 "capitais — Porto Alegre está, Gramado não. O que circula são médias de "
                 "aluguel de temporada de plataformas privadas.<br>"
                 "<b>A regra desta casa é não estimar.</b> A ficha de custos mostra o "
                 "total sem a hospedagem, e diz isso no rótulo — como em Fortaleza."),
                ("A taxa de turismo foi revogada",
                 "A <b>Taxa de Turismo Sustentável</b>, criada pela Lei 3.461/2015 e "
                 "cobrada a <b>R$ 3,43 por dia e por apartamento</b>, teve a revogação "
                 "<b>aprovada pela Câmara de Vereadores em 13 de abril de 2026</b> "
                 "(PLO 077/2025 e PLC 004/2025), depois de acordo com o Ministério "
                 "Público do RS, que a considerava inconstitucional por atingir só quem "
                 "se hospeda. Fonte: jornal ABC Mais, 17/abr/2026.<br>"
                 + FLAG % "Só em fonte secundária" +
                 "<b>não achamos a sanção do prefeito publicada</b>; o portal de leis do "
                 "município recusou a conexão na consulta. Se o seu hotel cobrar a TTS, "
                 "pergunte com base em quê."),
                ("O que pode aparecer no lugar: a Room Tax, que é voluntária",
                 "O <b>Gramado Canela Convention & Visitors Bureau</b> anunciou em maio de "
                 "2026 a volta da <b>Room Tax</b>, cobrada no check-out pelos hotéis "
                 "associados, <b>no mesmo valor: R$ 3,43</b> por hóspede, por dia. "
                 "<b>E é opcional</b> — a reportagem: <i>“será opcional o pagamento por "
                 "parte dos hóspedes”</i>. Fonte: ABC Mais, 6/mai/2026.<br>"
                 "<b>Se a linha aparecer na sua conta, você pode pedir para tirar.</b> Ela "
                 "não é imposto."),
            ],
        },
    ],
}

DESTINOS = [GRAMADO]
