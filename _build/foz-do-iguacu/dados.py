# -*- coding: utf-8 -*-
"""Foz do Iguacu: o vigesimo terceiro destino, em nove pontos e tres grupos.

Mesmo molde do gramado/dados.py.

O ACHADO PRINCIPAL: O LADO ARGENTINO COBRA DE BRASILEIRO PRECO DE ESTRANGEIRO
------------------------------------------------------------------------------
O Parque Nacional do Iguacu, do lado brasileiro, tem a faixa "Brasil/
Mercosul": R$ 121,00, contra R$ 134,00 da integral - um argentino paga o
mesmo que um brasileiro. Do outro lado, o Parque Nacional Iguazu nao tem
faixa Mercosul: "Visitantes internacionales AR$ 60.000" (tabela oficial,
iguazuargentina.com, e APN, a partir de 1/6/2026). Pelo boletim de
fechamento do BCB de 23/10/2026 (ARS venda 0,003299), sao R$ 197,94 -
64% a mais que o lado brasileiro. E a bilheteria so aceita cartao ou
dinheiro em PESO ARGENTINO.

O SEGUNDO: NO LADO BRASILEIRO NAO HA MEIA-ENTRADA
--------------------------------------------------------------------------
A pagina de descontos do parque: ele "nao dispoe de meia-entrada ou
descontos adicionais na tabela" - a lei da meia estudantil e o Estatuto
da Pessoa Idosa nao valem para parque federal. Idoso e estudante pagam
R$ 121. Crianca ate 6 anos nao paga.

O TERCEIRO: SEGUNDA-FEIRA FECHA O MARCO
--------------------------------------------------------------------------
O Marco das Tres Fronteiras abre "de terca-feira a domingo, das 14h as
21h". O roteiro termina no domingo.

O QUE FICOU SEM RESPOSTA, E ESTA DITO EM CADA FICHA
--------------------------------------------------------------------------
    hospedagem       nenhum orgao publica diaria media de Foz; o Panorama
                     FOHB/HotelInvest (20a ed.) nao cobre a cidade, e a
                     Secretaria de Turismo publica so ocupacao
    taxa de turismo  a cobrada nos hoteis associados ao Visit Iguassu: nao
                     achamos lei nem valor
    onibus a         as duas empresas que saem do TTU nao tem tarifa
    Argentina        publicada na pagina da Secretaria de Turismo
    Templo Budista   so fonte secundaria; horario diverge (16h30 ou 17h)
    estacionamento   o parque brasileiro so tem link de reserva, sem valor
    das Cataratas

Fontes guardadas em _build/foz-do-iguacu/fontes/. Apuracao de 29 de
outubro de 2026.
"""

APURACAO = "29 de outubro de 2026"
APURACAO_CURTA = "29/out/2026"

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
#  FOZ DO IGUACU
# =====================================================================
FOZ = {
    "slug": "foz-do-iguacu",
    "nome": "Foz do Iguaçu",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "Foz do Iguaçu: 9 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 9 pontos de Foz do Iguaçu, com o lado "
                  "argentino das Cataratas que cobra de brasileiro o preço de "
                  "estrangeiro e o lado brasileiro que não tem meia-entrada."),
    "abertura": ("Nove pontos de Foz do Iguaçu com preço, horário e fonte conferidos em "
                 "29 de outubro de 2026 — e duas coisas que os guias não dizem: <b>o "
                 "lado argentino das Cataratas não tem tarifa Mercosul</b>. O brasileiro "
                 "paga AR$ 60.000, cerca de R$ 198, o mesmo que qualquer estrangeiro — "
                 "64% a mais que os R$ 121 do lado brasileiro, onde o argentino paga "
                 "como brasileiro. <b>E o lado brasileiro não tem meia-entrada</b>: "
                 "idoso e estudante pagam o valor cheio, porque a lei não vale para "
                 "parque federal."),
    "busca": ("foz do iguacu foz do iguaçu cataratas iguacu iguazu parana pr brasil "
              "argentina puerto iguazu garganta do diabo garganta del diablo itaipu "
              "marco das tres fronteiras parque das aves macuco safari templo budista "
              "triplice fronteira paraguai"),
    "grupos": [
        {"id": "g1", "titulo": "As Cataratas, dos dois lados",
         "intro": ("O mesmo rio, duas bilheterias e duas regras: a brasileira dá ao "
                   "argentino o preço de brasileiro; a argentina cobra do brasileiro o "
                   "preço de estrangeiro. E o barco que chega perto da queda é pago à "
                   "parte.")},
        {"id": "g2", "titulo": "Itaipu, o Marco e o que não cobra",
         "intro": ("A usina, com cinco passeios de R$ 48 a R$ 185; o Marco das Três "
                   "Fronteiras, que fecha na segunda; e o Templo Budista, que não "
                   "cobra.")},
        {"id": "g3", "titulo": "O Parque das Aves, o ônibus e a cama",
         "intro": ("O parque em frente às Cataratas, com preço válido só até 30 de "
                   "novembro; o ônibus de R$ 5 que leva a quase tudo; e a hospedagem, "
                   "sem diária oficial publicada.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - as Cataratas
        # =============================================================
        {
            "id": "parque-nacional-do-iguacu",
            "foto": {"arq": "foz-do-iguacu/parque-nacional-do-iguacu.webp",
                     "alt": "A Garganta do Diabo vista do lado brasileiro, com a névoa subindo entre a mata",
                     "cred": "Marinelson Almeida · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Parque Nacional do Iguaçu (lado brasileiro)",
            "tag": "Cataratas",
            "preco_val": "R$ 121",
            "preco_nota": "Brasil e Mercosul; integral R$ 134; sem meia-entrada",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial do parque (cataratasdoiguacu.com.br), tabela de 2026 "
                 "publicada em 19/12/2025 e consultada em 29/out/2026.<br>"
                 "<b>Brasil/Mercosul: R$ 121,00</b> — R$ 118,00 de ingresso mais R$ 3,00 de "
                 "contribuição ao Fundo Iguaçu.<br>"
                 "<b>Integral: R$ 134,00</b> — R$ 131,00 mais os mesmos R$ 3,00. É a de quem "
                 "vem de fora do Mercosul.<br>"
                 "<b>Passe Comunidade: R$ 26,00</b>, para morador dos 14 municípios do "
                 "entorno, com comprovante e cadastro no guichê.<br>"
                 "<b>Os R$ 3,00 do Fundo Iguaçu são voluntários</b> — a página: <i>“A "
                 "contribuição ao Fundo Iguaçu é voluntária.”</i> Sem ela, a faixa "
                 "Brasil/Mercosul sai por R$ 118."),
                ("Quem não paga, e a meia que não existe",
                 "<b>Criança até 6 anos não paga</b>, com documento original com foto.<br>"
                 "<b>Não há meia-entrada.</b> A página de descontos diz que o parque "
                 "<i>“não dispõe de meia-entrada ou descontos adicionais na tabela”</i>: "
                 "a lei da meia estudantil e o Estatuto da Pessoa Idosa valem para outros "
                 "estabelecimentos, não para parque federal. <b>Idoso e estudante pagam "
                 "R$ 121.</b>"),
                ("Dias e horários",
                 "<b>Todos os dias do ano.</b> A página inicial: <b>segunda a sexta, 9h às "
                 "16h; sábado e domingo, 8h30 às 16h</b>.<br>"
                 "Trilhas com horário próprio: Caminho das Bananeiras 9h às 16h; Trilha "
                 "Ytepopo 9h às 14h30; Poço Preto a pé 9h às 12h.<br>"
                 + FLAG % "Lacuna declarada" +
                 "<b>o estacionamento só tem link de reserva</b>, para uma empresa "
                 "terceira, sem o valor na página do parque."),
                ("Onde fica",
                 mapa("Parque Nacional do Iguaçu, Centro de Visitantes, BR-469 km 18, Foz do Iguaçu, PR")),
            ],
        },
        {
            "id": "parque-nacional-iguazu",
            "grupo": "g1",
            "nome": "Parque Nacional Iguazú (lado argentino)",
            "tag": "Cataratas",
            "preco_val": "AR$ 60.000",
            "preco_nota": "cerca de R$ 198; brasileiro paga como estrangeiro",
            "campos": [
                ("Valor da entrada, e a faixa que não existe",
                 "Fonte: tabela oficial do parque (iguazuargentina.com, <i>Tarifas</i>) e da "
                 "Administración de Parques Nacionales (argentina.gob.ar), vigente desde "
                 "1º de junho de 2026, consultadas em 29/out/2026.<br>"
                 "<b>Visitantes internacionais: AR$ 60.000.</b> Inclui o Trem Ecológico até "
                 "a Garganta do Diabo.<br>"
                 "Residente na Argentina: AR$ 25.000. Residente de Misiones: AR$ 8.000. "
                 "Estudante argentino: AR$ 15.000.<br>"
                 "<b>Não há faixa Mercosul.</b> O brasileiro paga o mesmo que qualquer "
                 "estrangeiro — o contrário do lado brasileiro, onde o argentino paga "
                 "R$ 121, como brasileiro.<br>"
                 "<b>Em real: cerca de R$ 198</b> (R$ 197,94), pela taxa de venda do "
                 "boletim de fechamento do Banco Central de 23/out/2026. É <b>64% a mais "
                 "que o lado brasileiro</b>."),
                ("Como pagar, e o segundo dia",
                 "A página de perguntas frequentes: <i>“Se aceptan tarjetas de crédito, "
                 "débito y dinero efectivo en boletería (pesos argentinos).”</i> <b>Dinheiro, "
                 "só peso argentino</b> — real não. No cartão brasileiro entra o IOF de "
                 "compra internacional.<br>"
                 "<b>O segundo dia sai pela metade</b>, apresentando o ingresso do primeiro "
                 "na bilheteria.<br>"
                 "Menor de 6 anos não paga. Na bilheteria se mostra DNI ou passaporte "
                 "para definir a categoria."),
                ("Dias e horários",
                 "<b>Todos os dias do ano, das 8h às 18h</b>, inclusive com chuva. "
                 "<b>Entrada na Área Cataratas até 16h.</b><br>"
                 "Trem até a Garganta: primeira saída 8h20, <b>última 15h30</b>, último "
                 "retorno 17h30.<br>"
                 + FLAG % "Fontes divergem" +
                 "<b>a mesma página diz “Ingreso a Circuitos hasta las 15:45” e, mais "
                 "abaixo, “Último ingreso 16:45”.</b> Conte com o horário mais cedo."),
                ("Onde fica",
                 mapa("Parque Nacional Iguazú, Ruta 101 km 142, Puerto Iguazú, Misiones, Argentina")),
            ],
        },
        {
            "id": "macuco-safari",
            "grupo": "g1",
            "nome": "Macuco Safari",
            "tag": "Passeio de barco",
            "preco_val": "R$ 384",
            "preco_nota": "não inclui a entrada do parque; 7 a 11 anos R$ 192",
            "campos": [
                ("Valor do passeio",
                 "Fonte: site oficial (macucosafari.com.br), consultado em 29/out/2026.<br>"
                 "<b>Adulto: R$ 384,00.</b><br>"
                 "<b>R$ 192,00</b> (50%) para criança de 7 a 11 anos, brasileiro acima de "
                 "60, estudante e morador de Foz e dos municípios vizinhos ao parque.<br>"
                 "<b>Até 6 anos não paga.</b><br>"
                 "<b>A entrada do parque é à parte</b> — a página: <i>“O ingresso de "
                 "entrada no Parque Nacional do Iguaçu – Cataratas NÃO está incluso”</i>. "
                 "Somado aos R$ 121 do parque, o dia sai por R$ 505."),
                ("Como funciona",
                 "Cerca de <b>2 horas</b>, das quais 25 a 30 minutos de barco. <b>Sem "
                 "reserva</b>: saídas a cada 20 minutos, segunda a sexta das 9h às 17h, "
                 "sábado e domingo das 8h30 às 17h. Fica dentro do Parque Nacional do "
                 "Iguaçu, no caminho das Cataratas."),
                ("Onde fica",
                 mapa("Macuco Safari, Parque Nacional do Iguaçu, Foz do Iguaçu, PR")),
            ],
        },
        # =============================================================
        #  g2 - Itaipu, o Marco e o gratis
        # =============================================================
        {
            "id": "itaipu",
            "foto": {"arq": "foz-do-iguacu/itaipu.webp",
                     "alt": "A barragem de Itaipu, com os condutos forçados brancos e o vertedouro aberto",
                     "cred": "Deni Williams · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Itaipu Binacional",
            "tag": "Usina",
            "preco_val": "R$ 63",
            "preco_nota": "Panorâmica; Especial R$ 185; Refúgio R$ 48",
            "campos": [
                ("Os cinco passeios",
                 "Fonte: site oficial do Turismo Itaipu (turismoitaipu.com.br), consultado "
                 "em 29/out/2026. Valores de inteira.<br>"
                 "<b>Itaipu Panorâmica: R$ 63,00</b> — cerca de 1h10, só por fora: os tubos "
                 "brancos, o topo da barragem, o Mirante Central e o do Vertedouro. "
                 "Todos os dias, das 8h15 às 17h, saídas a cada 30 minutos, por ordem de "
                 "chegada.<br>"
                 "<b>Itaipu Especial: R$ 185,00</b> — cerca de 2h30, por dentro, até a Sala "
                 "do Comando Central. Vagas e horários limitados.<br>"
                 "<b>Refúgio Biológico: R$ 48,00</b> — cerca de 2h30, <b>de quarta a "
                 "segunda</b>: fecha na terça.<br>"
                 "<b>Itaipu Iluminada: R$ 50,00</b> — sexta e sábado, 19h. Com jantar, "
                 "R$ 180,00."),
                ("Meia, gratuidade e pagamento",
                 "<b>Meia de estudante só para instituição brasileira</b>; para "
                 "estrangeiro, a meia vale só para pessoa com deficiência.<br>"
                 "<b>Morador de município lindeiro ao lago não paga a Panorâmica</b>, com "
                 "reserva pelo portal do lindeiro.<br>"
                 "Pagamento: cartão de crédito e débito, PIX e <b>dinheiro só em real</b>."),
                ("Onde fica",
                 mapa("Centro de Recepção de Visitantes de Itaipu, Av. Tancredo Neves 6702, Foz do Iguaçu, PR")),
            ],
        },
        {
            "id": "marco-das-tres-fronteiras",
            "foto": {"arq": "foz-do-iguacu/marco-das-tres-fronteiras.webp",
                     "alt": "O Marco das Três Fronteiras sobre o encontro dos rios Iguaçu e Paraná",
                     "cred": "MTur Destinos · domínio público · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Marco das Três Fronteiras",
            "tag": "Mirante",
            "preco_val": "R$ 60",
            "preco_nota": "reduzida R$ 31,50; fecha na segunda",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (marcodastresfronteiras.com.br), consultado em "
                 "29/out/2026.<br>"
                 "<b>Integral, a partir de 12 anos: R$ 60</b> — R$ 57 de ingresso mais R$ 3 "
                 "do Fundo Iguaçu.<br>"
                 "<b>Reduzida: R$ 31,50</b> — R$ 28,50 mais R$ 3.<br>"
                 "<b>De 0 a 5 anos não paga</b>, com responsável. <b>Morador de Foz não "
                 "paga</b>, com comprovante."),
                ("Quem tem a reduzida: a página diz duas coisas",
                 FLAG % "Fontes divergem" +
                 "<b>o quadro de preços diz “estudantes e professores brasileiros”; a "
                 "nota logo abaixo diz “estudantes e professores do estado do "
                 "Paraná”.</b> Os dois textos concordam com criança de 6 a 11 anos, idoso "
                 "brasileiro a partir de 60 e doador de sangue do Paraná. Estudante de "
                 "fora do Paraná: leve a carteira e pergunte na bilheteria."),
                ("Dias e horários",
                 "<b>De terça a domingo, das 14h às 21h.</b> <b>Fecha na segunda</b> — e "
                 "abre só à tarde: é o ponto do pôr do sol sobre a junção dos rios Iguaçu "
                 "e Paraná, com Argentina e Paraguai do outro lado."),
                ("Onde fica",
                 mapa("Marco das Três Fronteiras, Av. General Meira, Foz do Iguaçu, PR")),
            ],
        },
        {
            "id": "templo-budista",
            "foto": {"arq": "foz-do-iguacu/templo-budista.webp",
                     "alt": "O portão de entrada do Templo Budista Chen Tien, com a inscrição em chinês",
                     "cred": "Jonas de Carvalho · CC BY-SA 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Templo Budista Chen Tien",
            "tag": "Gratuito",
            "preco_val": "Grátis",
            "preco_nota": "fecha na segunda; horário só em fonte secundária",
            "campos": [
                ("O que se sabe",
                 FLAG % "Só em fonte secundária" +
                 "<b>não achamos página oficial do templo com preço e horário.</b> Os guias "
                 "de viagem concordam em duas coisas: <b>a entrada é gratuita</b> e <b>o "
                 "templo não abre na segunda</b>.<br>"
                 + FLAG % "Fontes divergem" +
                 "<b>o horário aparece como 9h30 às 16h30 num guia e 9h30 às 17h em "
                 "outro</b>, de terça a domingo. Chegue antes das 16h30."),
                ("Onde fica",
                 mapa("Templo Budista Chen Tien, Foz do Iguaçu, PR")),
            ],
        },
        # =============================================================
        #  g3 - o Parque das Aves, o onibus e a cama
        # =============================================================
        {
            "id": "parque-das-aves",
            "foto": {"arq": "foz-do-iguacu/parque-das-aves.webp",
                     "alt": "A entrada do Parque das Aves, entre palmeiras e plantas tropicais",
                     "cred": "Jorge Andrade · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Parque das Aves",
            "tag": "Parque",
            "preco_val": "R$ 110",
            "preco_nota": "meia R$ 55; preço válido até 30/11/2026",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de valores do site oficial (parquedasaves.com.br), "
                 "consultada em 29/out/2026.<br>"
                 "<b>Integral, brasileiros e estrangeiros: R$ 110,00.</b><br>"
                 "<b>Meia-entrada: R$ 55,00.</b><br>"
                 "<b>Criança até 8 anos não paga</b>, com o responsável.<br>"
                 "<b>Ingresso Comunidade: R$ 15,00</b>, para morador das cidades vizinhas ao "
                 "Parque Nacional.<br>"
                 "<b>A própria página avisa: “Preços válidos até 30/11/2026.”</b> Quem vai "
                 "em dezembro, confira de novo."),
                ("O que é cobrado à parte",
                 "<b>Estacionamento: R$ 60,00</b> a diária, das 8h às 18h30. Armário: "
                 "R$ 30,00 por ficha. Carrinho de criança: R$ 30,00."),
                ("Dias e horários",
                 "<b>Todos os dias, das 8h30 às 16h30.</b> Fica na Avenida das Cataratas, "
                 "perto da entrada do Parque Nacional — dá para fazer os dois no mesmo "
                 "dia."),
                ("Onde fica",
                 mapa("Parque das Aves, Av. das Cataratas, Foz do Iguaçu, PR")),
            ],
        },
        {
            "id": "transporte",
            "grupo": "g3",
            "nome": "Ônibus, e a travessia para a Argentina",
            "tag": "Transporte",
            "preco_val": "R$ 5",
            "preco_nota": "a passagem urbana; pode ir a R$ 6",
            "campos": [
                ("A tarifa",
                 "Fonte: <b>Secretaria Municipal de Turismo</b> (destino.foz.br), página de "
                 "transporte público, consultada em 29/out/2026: <i>“O valor da tarifa é "
                 "de R$ 5,00”</i>.<br>"
                 "<b>Pode subir.</b> Em agosto de 2026 a Foztrans levou a consulta pública "
                 "um novo modelo de concessão com <b>tarifa de R$ 6</b> (Rádio Cultura Foz, "
                 "6/ago/2026). Até a consulta desta ficha, não achamos o reajuste em "
                 "vigor.<br>"
                 "A linha que vai do aeroporto ao centro e às Cataratas é citada pelos "
                 "guias como a 120. "
                 + FLAG % "Só em fonte secundária" +
                 "o número da linha não estava na página da Secretaria."),
                ("Para o lado argentino",
                 "Duas empresas, <b>Crucero del Norte e Río Uruguay</b>, saem do Terminal de "
                 "Transporte Urbano (TTU), <b>todos os dias das 7h às 19h</b>, segundo a "
                 "Secretaria de Turismo.<br>"
                 + FLAG % "Lacuna declarada" +
                 "<b>a página não publica o preço</b>, e não o confirmamos em fonte "
                 "oficial. Leve documento: o parque argentino pede DNI ou passaporte na "
                 "bilheteria para definir a categoria."),
                ("Onde fica",
                 mapa("Terminal de Transporte Urbano TTU, Foz do Iguaçu, PR")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem, e a taxa que ninguém publica",
            "tag": "Conta, não lugar",
            "preco_val": "sem dado oficial",
            "preco_nota": "a ocupação é publicada; a diária, não",
            "campos": [
                ("Por que não há diária nesta ficha",
                 FLAG % "Lacuna declarada" +
                 "<b>Nenhum órgão publica a diária média de Foz do Iguaçu.</b> O Panorama da "
                 "Hotelaria Brasileira (FOHB/HotelInvest, 20ª edição), que usamos em "
                 "Salvador e Fortaleza, não traz a cidade. A Secretaria Municipal de "
                 "Turismo publica todo mês a <b>ocupação</b> — e não a diária.<br>"
                 "<b>A regra desta casa é não estimar.</b> A ficha de custos mostra o total "
                 "sem a hospedagem, e diz isso no rótulo — como em Gramado e Fortaleza."),
                ("A taxa de turismo dos hotéis",
                 FLAG % "Lacuna declarada" +
                 "<b>hotéis associados ao Visit Iguassu, o instituto que promove o "
                 "destino, cobram uma “taxa de turismo” na recepção</b>, segundo a "
                 "imprensa do setor. <b>Não achamos lei municipal que a crie nem o "
                 "valor publicado.</b> Se aparecer na sua conta, pergunte se é "
                 "obrigatória — como a Room Tax de Gramado, pode não ser."),
            ],
        },
    ],
}

DESTINOS = [FOZ]
