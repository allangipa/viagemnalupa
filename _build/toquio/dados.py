# -*- coding: utf-8 -*-
"""Toquio: o trigesimo segundo destino, em sete pontos. O primeiro da Asia.

Mesmo molde do machu-picchu/dados.py. Par 2 da fila de 15/11/2026, com Porto
de Galinhas.

O ACHADO PRINCIPAL: 2026 MEXEU EM QUATRO COBRANCAS DO TURISTA NO JAPAO
----------------------------------------------------------------------
    14/03/2026  o passe de metro de 24 h foi de 800 para 1.000 ienes
                (comunicado do Governo Metropolitano, 30/01/2026)
    01/07/2026  a taxa de saida do pais triplicou: 1.000 -> 3.000 ienes
                (JNTO)
    01/11/2026  o tax-free virou reembolso: paga com imposto e recebe ao
                sair (so imprensa e guias)
    01/04/2027  a taxa de hospedagem de Toquio deixa de ser 100 ou 200
                ienes e vira 3% da diaria (proposta oficial do Governo
                Metropolitano; data pela imprensa)

O SEGUNDO: NO SKYTREE, COMPRAR NO BALCAO CUSTA 500 IENES A MAIS
--------------------------------------------------------------------------
"A 500-yen service fee per ticket will be added for purchases made at the
4th-floor ticket counter or ticket vending machines."

MOEDA: os precos ficam em iene, com o real ao lado pela taxa de venda do
boletim de fechamento do BCB de 23/10/2026 (JPY 0,03211), como o sol em
Machu Picchu. A ficha de custos e em real.

O QUE FICOU SEM RESPOSTA
--------------------------------------------------------------------------
    hospedagem   nenhuma diaria media oficial achada
    tax-free     so imprensa e guias; nao lemos a agencia oficial
    Shibuya Sky  pagina sem texto legivel; ficou fora

Fontes guardadas em _build/toquio/fontes/. Apuracao de 27 de novembro de 2026.
"""

APURACAO = "27 de novembro de 2026"
APURACAO_CURTA = "27/nov/2026"

FLAG = '<span class="flag">%s</span> '
SEC = FLAG % "Só em fonte secundária"
CAMBIO = "pela taxa de venda do Banco Central de 23/out/2026"


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


TOQUIO = {
    "slug": "toquio",
    "nome": "Tóquio",
    "pais": "Japão",
    "regiao": "asia",
    "titulo": "Tóquio: 7 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 7 pontos de Tóquio, com as quatro cobranças do "
                  "turista que mudaram em 2026: a taxa de saída que triplicou, o passe de "
                  "metrô, o tax-free e a taxa de hospedagem que vira 3%."),
    "abertura": ("Sete pontos de Tóquio com preço, horário e fonte conferidos em 27 de novembro "
                 "de 2026 — e uma coisa que os guias antigos erram: <b>2026 mexeu em quatro "
                 "cobranças do turista no Japão</b>. O passe de metrô de 24 horas subiu de 800 "
                 "para 1.000 ienes em março; <b>a taxa de saída do país triplicou em julho, de "
                 "1.000 para 3.000 ienes</b>; o tax-free virou reembolso em novembro; e a taxa "
                 "de hospedagem de Tóquio vira 3% da diária em abril de 2027."),
    "busca": ("toquio tokyo japao japan iene yen skytree museu nacional ueno metro subway "
              "ticket taxa de saida sayonara tax tax free taxa de hospedagem accommodation tax "
              "asia"),
    "grupos": [
        {"id": "g1", "titulo": "As três taxas do turista",
         "intro": ("A que vem na passagem, a que vem na conta do hotel e a que volta na saída "
                   "— as três mudaram ou mudam entre julho de 2026 e abril de 2027.")},
        {"id": "g2", "titulo": "O que ver, com tabela oficial",
         "intro": ("O Skytree, onde o balcão cobra mais que o site, e o Museu Nacional, que "
                   "fecha na segunda e tem três dias grátis por ano.")},
        {"id": "g3", "titulo": "Andar e dormir",
         "intro": ("O passe de metrô do visitante, 25% mais caro desde março, e a hospedagem, "
                   "sem diária oficial.")},
    ],
    "pontos": [
        {
            "id": "taxa-de-saida",
            "grupo": "g1",
            "nome": "Taxa de saída do Japão",
            "tag": "Taxa",
            "preco_val": "¥ 3.000",
            "preco_nota": "cerca de R$ 96; triplicou em 1º/7/2026; vem na passagem",
            "campos": [
                ("O que é, e quanto subiu",
                 "Fonte: <b>JNTO</b>, a organização nacional de turismo do Japão "
                 "(japan.travel), consultada em 27/nov/2026: <i>“As of July 1st, 2026, Japan’s "
                 "international tourist tax will increase from 1,000 JPY to 3,000 JPY.”</i><br>"
                 "É uma taxa única, por pessoa, cobrada de quem sai do Japão. <b>Em real, cerca "
                 "de R$ 96</b> (R$ 96,33), " + CAMBIO + "."),
                ("Onde ela aparece",
                 "<b>Na passagem</b>: segundo a JNTO, na grande maioria dos casos a taxa já vem "
                 "embutida no bilhete de volta, no momento da compra. Por isso fica fora do "
                 "total da ficha de custos, que não inclui a passagem."),
            ],
        },
        {
            "id": "taxa-de-hospedagem",
            "foto": {"arq": "toquio/taxa-de-hospedagem.webp",
                     "alt": "Os prédios iluminados de Shinjuku à noite, vistos do alto",
                     "cred": "康 复 (calvision) from Tokyo, Japan · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Taxa de hospedagem de Tóquio",
            "tag": "Taxa",
            "preco_val": "¥ 100 ou ¥ 200",
            "preco_nota": "por pessoa por noite; vira 3% da diária em abril de 2027",
            "campos": [
                ("Como é hoje",
                 "Fonte: <b>Governo Metropolitano de Tóquio</b>, <i>Review of the "
                 "Accommodation Tax</i> (novembro de 2025), consultado em 27/nov/2026.<br>"
                 "<b>Diária abaixo de ¥ 10.000 por pessoa: isenta.</b> De ¥ 10.000 a menos de "
                 "¥ 15.000: <b>¥ 100</b>. De ¥ 15.000 em diante: <b>¥ 200</b>, cerca de "
                 "R$ 6,42. Por pessoa, por noite, em hotel e ryokan."),
                ("Como fica",
                 "O mesmo documento propõe <b>3% da diária</b>, com a isenção subindo de "
                 "¥ 10.000 para <b>¥ 13.000</b>, e passa a cobrar também de hospedagem "
                 "particular.<br>"
                 + SEC +
                 "<b>a data, 1º de abril de 2027, e a aprovação do governo nacional em "
                 "30/jun/2026 vêm da imprensa</b> (SoraNews24, 7/jul/2026). Um hotel avisa que "
                 "a taxa nova vale para estadias a partir dessa data, qualquer que seja a data "
                 "da reserva."),
            ],
        },
        {
            "id": "tax-free",
            "grupo": "g1",
            "nome": "Tax-free: agora é reembolso",
            "tag": "Regra",
            "preco_val": "reembolso",
            "preco_nota": "desde 1º/11/2026 paga-se com imposto e recebe-se ao sair",
            "campos": [
                ("O que mudou",
                 SEC +
                 "<b>desde 1º de novembro de 2026, o turista paga o preço com imposto na loja e "
                 "recebe o reembolso depois</b>, com a conferência na alfândega ao sair do "
                 "Japão (japan-guide.com, nippon.com, Time Out Tokyo). Antes, o desconto era "
                 "dado na hora.<br>"
                 "Continua valendo o mínimo de <b>¥ 5.000</b> sem imposto, na mesma loja e no "
                 "mesmo dia.<br>"
                 "<b>Não lemos a página da agência oficial</b>; os guias divergem sobre por onde "
                 "o reembolso chega."),
            ],
        },
        {
            "id": "tokyo-skytree",
            "foto": {"arq": "toquio/tokyo-skytree.webp",
                     "alt": "A Tokyo Skytree sobressaindo acima das árvores, contra o céu azul",
                     "cred": "Manishprabhune · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Tokyo Skytree",
            "tag": "Mirante",
            "preco_val": "desde ¥ 1.800",
            "preco_nota": "cerca de R$ 58; no balcão, ¥ 500 a mais por ingresso",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página oficial de ingressos (tokyo-skytree.jp), consultada em "
                 "27/nov/2026.<br>"
                 "<b>Tembo Deck, o andar 350: a partir de ¥ 1.800</b> o adulto (15 anos ou "
                 "mais), cerca de R$ 57,80; de 6 a 14 anos, a partir de ¥ 900.<br>"
                 "<b>Combo dos andares 350 e 450: a partir de ¥ 3.000</b>; criança, ¥ 1.500.<br>"
                 "Só a Tembo Galleria, comprada lá em cima no dia: ¥ 1.400.<br>"
                 "<b>Até 5 anos não paga.</b> “A partir de” porque o preço muda com a data."),
                ("O balcão cobra mais",
                 "<b>¥ 500 a mais por ingresso</b> para quem compra no balcão ou nas máquinas "
                 "do 4º andar — a página: <i>“A 500-yen service fee per ticket will be "
                 "added”</i>. Compre online."),
                ("Onde fica",
                 mapa("Tokyo Skytree, Sumida, Tokyo")),
            ],
        },
        {
            "id": "museu-nacional",
            "foto": {"arq": "toquio/museu-nacional.webp",
                     "alt": "O prédio principal do Museu Nacional de Tóquio, de telhado japonês, refletido no espelho d’água",
                     "cred": "Wiiii · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Museu Nacional de Tóquio",
            "tag": "Museu",
            "preco_val": "¥ 1.000",
            "preco_nota": "cerca de R$ 32; fecha na segunda e de 26 a 31/12",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de visitação do site oficial (tnm.jp), consultada em "
                 "27/nov/2026.<br>"
                 "<b>Acervo permanente: ¥ 1.000</b> o adulto, cerca de R$ 32,11; universitário, "
                 "¥ 500. O ingresso comprado online vale dois meses. Exposição especial tem "
                 "bilhete próprio.<br>"
                 "<b>Três dias grátis em 2026</b>: 19 de maio, 21 de setembro e 3 de "
                 "novembro."),
                ("Dias e horários",
                 "<b>9h30 às 17h</b>; sexta e sábado até 20h. Última entrada 30 minutos "
                 "antes.<br>"
                 "<b>Fecha na segunda</b> — se for feriado, abre e fecha na terça. <b>Fechado "
                 "de 26 a 31 de dezembro de 2026</b>; reabre em 1º de janeiro, do meio-dia às "
                 "20h."),
                ("Onde fica",
                 mapa("Tokyo National Museum, Ueno Park, Tokyo")),
            ],
        },
        {
            "id": "metro",
            "foto": {"arq": "toquio/metro.webp",
                     "alt": "Um trem do metrô saindo do túnel sob um trem laranja da JR, à beira do rio, em Ochanomizu",
                     "cred": "Kabelleger / David Gubler · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Tokyo Subway Ticket, o passe do visitante",
            "tag": "Transporte",
            "preco_val": "¥ 1.000",
            "preco_nota": "24 horas; 48 h ¥ 1.500; 72 h ¥ 2.000; subiu em 14/3/2026",
            "campos": [
                ("A tabela, antes e depois",
                 "Fonte: <b>Governo Metropolitano de Tóquio</b>, comunicado de 30/jan/2026 da "
                 "Tokyo Metro e do departamento de transportes, consultado em 27/nov/2026. "
                 "Preços desde <b>14 de março de 2026</b>, adulto:<br>"
                 "<b>24 horas: ¥ 1.000</b> (antes, ¥ 800). <b>48 horas: ¥ 1.500</b> (antes, "
                 "¥ 1.200). <b>72 horas: ¥ 2.000</b> (antes, ¥ 1.500), cerca de R$ 64,22. "
                 "Criança paga metade.<br>"
                 "Vale nas linhas da Tokyo Metro e da Toei, as duas redes de metrô. Guia com "
                 "preço de antes de março de 2026 está desatualizado."),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem",
            "tag": "Conta, não lugar",
            "preco_val": "sem dado oficial",
            "preco_nota": "não achamos diária média oficial",
            "campos": [
                ("Por que não há diária nesta ficha",
                 FLAG % "Lacuna declarada" +
                 "<b>Não achamos diária média oficial de Tóquio.</b> <b>A regra desta casa é "
                 "não estimar.</b> A ficha de custos mostra o total sem a hospedagem, e diz "
                 "isso no rótulo.<br>"
                 "O que dá para saber de antemão é a taxa: até abril de 2027, ¥ 100 ou ¥ 200 "
                 "por pessoa por noite, conforme a diária."),
            ],
        },
    ],
}

DESTINOS = [TOQUIO]
