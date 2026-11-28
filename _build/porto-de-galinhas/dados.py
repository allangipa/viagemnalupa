# -*- coding: utf-8 -*-
"""Porto de Galinhas (com Recife): o trigesimo primeiro destino, em sete pontos.

Mesmo molde do bonito/dados.py. Par 2 da fila de 15/11/2026, com Toquio.

O ACHADO PRINCIPAL: O PASSEIO QUE TODO MUNDO FAZ NAO TEM PRECO PUBLICADO
--------------------------------------------------------------------------
A jangada as piscinas naturais e o passeio de Porto de Galinhas, e nao
achamos tabela oficial em lugar nenhum - nem da associacao dos jangadeiros,
nem da Prefeitura de Ipojuca. Os guias de viagem vao de R$ 50 a R$ 100: o
dobro. Fica fora do total, marcado.

O SEGUNDO: A TERCA GRATIS DO BRENNAND SOME EM JANEIRO, JULHO E DEZEMBRO
--------------------------------------------------------------------------
O Instituto Ricardo Brennand da entrada franca na ultima terca do mes -
"Apenas nos casos dos meses de JANEIRO, JULHO e DEZEMBRO nao ha ultima terca
gratuita". Sao os meses de ferias.

O TERCEIRO: A OFICINA BRENNAND COBRA MENOS DE PERNAMBUCANO
--------------------------------------------------------------------------
R$ 50 a inteira; "Para moradores de Pernambuco: Inteira R$ 40".

HOSPEDAGEM: painel do setor, nao orgao oficial. O Hotel Report 2026 da
Omnibees (motor de reservas), publicado pelo Hotelier News em 18/08/2026, da
a diaria media de Ipojuca: R$ 1.134 em 2025 e R$ 1.093 em 2026 ate junho.
Entra como em Paris (painel do setor via imprensa), com a ressalva escrita.

O QUE FICOU SEM RESPOSTA
--------------------------------------------------------------------------
    jangada            sem tabela oficial
    decreto 149/2025   so pela imprensa; nao achamos o texto oficial
    taxa de turismo    nao achamos nenhuma em Ipojuca
    Cais do Sertao     site fora do ar; ficou fora do guia

Fontes guardadas em _build/porto-de-galinhas/fontes/. Apuracao de 27 de
novembro de 2026.
"""

APURACAO = "27 de novembro de 2026"
APURACAO_CURTA = "27/nov/2026"

FLAG = '<span class="flag">%s</span> '
SEC = FLAG % "Só em fonte secundária"


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


PORTO = {
    "slug": "porto-de-galinhas",
    "nome": "Porto de Galinhas",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "Porto de Galinhas e Recife: 7 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 7 pontos de Porto de Galinhas e do Recife, com a "
                  "jangada que não tem preço publicado, a consumação mínima proibida nas "
                  "barracas e a terça grátis do Brennand que some nas férias."),
    "abertura": ("Sete pontos de Porto de Galinhas e do Recife com preço, horário e fonte "
                 "conferidos em 27 de novembro de 2026 — e duas coisas que os guias não dizem: "
                 "<b>a jangada às piscinas naturais, o passeio que todo mundo faz, não tem preço "
                 "publicado em lugar nenhum</b>, e os guias vão de R$ 50 a R$ 100. <b>E a "
                 "terça gratuita do Instituto Ricardo Brennand não existe em janeiro, julho e "
                 "dezembro</b>, os meses de férias."),
    "busca": ("porto de galinhas ipojuca recife pernambuco pe brasil piscinas naturais jangada "
              "muro alto maracaipe cupe consumacao minima instituto ricardo brennand oficina "
              "francisco brennand paco do frevo onibus 195 191"),
    "grupos": [
        {"id": "g1", "titulo": "A praia: a jangada e as barracas",
         "intro": ("O passeio sem tabela e a regra que mudou na virada de 2026: barraca não "
                   "pode mais exigir consumação mínima.")},
        {"id": "g2", "titulo": "Recife: três museus com tabela publicada",
         "intro": ("O Instituto Ricardo Brennand, a Oficina Francisco Brennand e o Paço do "
                   "Frevo: cada um com um dia grátis ou um desconto que depende de quem você "
                   "é e de quando vai.")},
        {"id": "g3", "titulo": "Chegar e dormir",
         "intro": ("O ônibus do Recife, com tarifa oficial, e a hospedagem, pelo painel do "
                   "setor.")},
    ],
    "pontos": [
        {
            "id": "piscinas-naturais",
            "foto": {"arq": "porto-de-galinhas/piscinas-naturais.webp",
                     "alt": "Uma jangada amarela, de vela recolhida, no mar verde de Porto de Galinhas, vista da linha d’água",
                     "cred": "Leo Benini · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Piscinas naturais, de jangada",
            "tag": "Passeio",
            "preco_val": "sem preço oficial",
            "preco_nota": "guias citam de R$ 50 a R$ 100; só na maré baixa",
            "campos": [
                ("O preço que ninguém publica",
                 SEC +
                 "<b>não achamos tabela oficial do passeio de jangada</b> — nem da associação "
                 "dos jangadeiros, nem da Prefeitura de Ipojuca. Os guias de viagem divergem: "
                 "<b>R$ 50</b> num, R$ 60 a R$ 70 em outro, R$ 80 numa tabela vista em janeiro "
                 "de 2026, <b>R$ 90 a R$ 100</b> na alta temporada num guia de maio. <b>O mais "
                 "caro é o dobro do mais barato.</b> Pergunte o preço na praia antes de "
                 "embarcar. Fora do total da ficha de custos."),
                ("Só na maré baixa",
                 "As piscinas só se formam na maré baixa: confira a tábua de marés do dia "
                 "antes de marcar o passeio — e antes de escolher as datas da viagem."),
                ("Onde fica",
                 mapa("Piscinas naturais de Porto de Galinhas, Ipojuca, PE")),
            ],
        },
        {
            "id": "barracas",
            "foto": {"arq": "porto-de-galinhas/barracas.webp",
                     "alt": "A praia de Porto de Galinhas na maré baixa, com a areia molhada refletindo o céu e coqueiros ao fundo",
                     "cred": "Andrevruas · CC BY 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Barracas de praia: consumação mínima proibida",
            "tag": "Regra",
            "preco_val": "proibida",
            "preco_nota": "decreto de Ipojuca; vale também em Cupê, Muro Alto e Maracaípe",
            "campos": [
                ("O que mudou",
                 SEC +
                 "<b>a Prefeitura de Ipojuca proibiu a consumação mínima nas barracas</b>, pelo "
                 "Decreto nº 149/2025, na virada de 2026, depois da agressão a um casal de "
                 "turistas numa discussão sobre cadeiras e guarda-sol. O decreto veda também "
                 "<b>taxa ou multa por não consumir</b> e <b>venda casada</b>, e vale em Porto "
                 "de Galinhas, Cupê, Muro Alto e Maracaípe (Brasilturis, 2/jan/2026; CBN "
                 "Recife, 3/jan/2026).<br>"
                 "<b>Não achamos o texto oficial do decreto</b>; a imprensa diverge na data, "
                 "entre 29/12/2025 e os primeiros dias de janeiro."),
                ("O que acontece com quem cobra",
                 "A barraca pode ter o alvará suspenso ou cassado. Na primeira semana, a "
                 "prefeitura fiscalizou 49 barracas e notificou 6 (CBN Recife, 3/jan/2026). "
                 "<b>Se cobrarem consumação mínima, a cobrança é irregular.</b>"),
                ("Onde fica",
                 mapa("Praia de Porto de Galinhas, Ipojuca, PE")),
            ],
        },
        {
            "id": "instituto-ricardo-brennand",
            "foto": {"arq": "porto-de-galinhas/instituto-ricardo-brennand.webp",
                     "alt": "Um coreto branco à beira do lago, entre as árvores do Instituto Ricardo Brennand",
                     "cred": "Wilfredor · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Instituto Ricardo Brennand (Recife)",
            "tag": "Museu",
            "preco_val": "R$ 60",
            "preco_nota": "meia R$ 30; última terça grátis, menos em jan, jul e dez",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de horários e ingressos do site oficial "
                 "(institutoricardobrennand.org.br), consultada em 27/nov/2026.<br>"
                 "<b>Inteira: R$ 60,00. Meia: R$ 30,00.</b><br>"
                 "Só o Jardim e a Capela: R$ 30,00 e R$ 15,00. <b>Museu + Jardim e Capela: "
                 "R$ 80,00</b> e R$ 40,00.<br>"
                 "Meia para pessoa com deficiência, estudante, professor e idoso acima de 60. "
                 "<b>Criança até 5 anos não paga.</b> Pagamento só com Pix ou cartão."),
                ("A terça grátis, e os três meses sem ela",
                 "<b>Na última terça-feira do mês a entrada é franca</b>, com ingressos "
                 "distribuídos a partir das 13h, por ordem de chegada.<br>"
                 "<b>Menos nas férias</b> — a página: <i>“Apenas nos casos dos meses de "
                 "JANEIRO, JULHO e DEZEMBRO não há última terça gratuita.”</i>"),
                ("Dias e horários",
                 FLAG % "Fontes divergem" +
                 "<b>a mesma página dá dois horários</b>: “de terça-feira a domingo, das 13h00 "
                 "às 17h00” num trecho, e “terça e quarta, 13h às 17h; quinta a domingo, 10h "
                 "às 17h” em outro. <b>Fecha na segunda.</b> Última entrada às 16h30. Para "
                 "não errar, vá a partir das 13h."),
                ("Onde fica",
                 mapa("Instituto Ricardo Brennand, Várzea, Recife, PE")),
            ],
        },
        {
            "id": "oficina-francisco-brennand",
            "foto": {"arq": "porto-de-galinhas/oficina-francisco-brennand.webp",
                     "alt": "O pátio da Oficina Francisco Brennand, com esculturas de cerâmica em fila e um templo de cúpula azul",
                     "cred": "Valdiney Pimenta · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Oficina Francisco Brennand (Recife)",
            "tag": "Museu-ateliê",
            "preco_val": "R$ 50",
            "preco_nota": "meia R$ 25; morador de Pernambuco paga R$ 40",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de visitação do site oficial (oficinafranciscobrennand.org.br), "
                 "consultada em 27/nov/2026.<br>"
                 "<b>Inteira: R$ 50. Meia: R$ 25.</b><br>"
                 "<b>Morador de Pernambuco: inteira R$ 40, meia R$ 20.</b>"),
                ("Dias e horários",
                 "<b>Terça a domingo, das 10h às 17h</b>, com entrada até as 16h. <b>Fecha na "
                 "segunda</b>, e em 24, 25 e 31 de dezembro e 1º de janeiro."),
                ("Onde fica",
                 mapa("Oficina Francisco Brennand, Várzea, Recife, PE")),
            ],
        },
        {
            "id": "paco-do-frevo",
            "foto": {"arq": "porto-de-galinhas/paco-do-frevo.webp",
                     "alt": "Uma sala vermelha do Paço do Frevo, com nomes de músicos nas paredes e a palavra frevo repetida",
                     "cred": "Eduardo Fonseca · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Paço do Frevo (Recife)",
            "tag": "Museu",
            "preco_val": "R$ 10",
            "preco_nota": "meia R$ 5; grátis às terças; fecha na segunda",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de visitação do site oficial (pacodofrevo.org.br), consultada "
                 "em 27/nov/2026.<br>"
                 "<b>Inteira: R$ 10,00. Meia: R$ 5,00.</b><br>"
                 "<b>Entrada gratuita para todos às terças-feiras.</b> Criança até 5 anos não "
                 "paga; meia a partir de 60 anos."),
                ("Dias e horários",
                 "<b>Segunda: fechado.</b> Terça a sexta, 10h às 18h. Sábado e domingo, 11h "
                 "às 19h. Última entrada meia hora antes de fechar."),
                ("Onde fica",
                 mapa("Paço do Frevo, Recife Antigo, Recife, PE")),
            ],
        },
        {
            "id": "onibus",
            "foto": {"arq": "porto-de-galinhas/onibus.webp",
                     "alt": "Dois prédios históricos de cúpulas na Praça do Marco Zero, no Recife Antigo",
                     "cred": "Wilfredor · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Ônibus Recife–Porto de Galinhas",
            "tag": "Transporte",
            "preco_val": "R$ 14,80",
            "preco_nota": "linha 191, sem ar; a 195, opcional, R$ 22,50",
            "campos": [
                ("A tarifa",
                 "Fonte: <b>Grande Recife Consórcio de Transporte</b>, página oficial de "
                 "tarifas (granderecife.pe.gov.br), consultada em 27/nov/2026.<br>"
                 "<b>191 – Recife/Porto de Galinhas (sem ar-condicionado): R$ 14,80.</b><br>"
                 "<b>195 – Recife/Porto de Galinhas (opcional): R$ 22,50.</b><br>"
                 "O bilhete único urbano do Grande Recife custa R$ 4,50 e não vale nessas "
                 "duas linhas."),
                ("Onde fica",
                 mapa("Aeroporto Internacional do Recife, PE")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem",
            "tag": "Conta, não lugar",
            "preco_val": "R$ 1.134",
            "preco_nota": "diária média de 2025, painel do setor; não é dado oficial",
            "campos": [
                ("De onde vem o número",
                 FLAG % "Painel do setor, pela imprensa" +
                 "<b>diária média de Ipojuca: R$ 1.134 em 2025</b>, contra R$ 1.059 em 2024, "
                 "e R$ 1.093 em 2026 com dados até junho. Fonte: <i>Hotel Report 2026</i>, da "
                 "Omnibees, publicado pelo Hotelier News em 18/ago/2026.<br>"
                 "<b>Não é dado oficial:</b> é a média das reservas que passam pelo sistema de "
                 "uma empresa de reservas, num destino de resorts. Sirva-se dele como ordem de "
                 "grandeza. Nenhum órgão público publica a diária de Porto de Galinhas."),
                ("Taxa de turismo",
                 FLAG % "Lacuna declarada" +
                 "<b>não achamos taxa de turismo, de preservação nem de veículos em "
                 "Ipojuca.</b> Ausência não se prova com documento; se aparecer na conta do "
                 "hotel, pergunte com base em quê."),
            ],
        },
    ],
}

DESTINOS = [PORTO]
