# -*- coding: utf-8 -*-
"""Florianopolis: o vigesimo oitavo destino, em oito pontos e tres grupos.

Mesmo molde do gramado/dados.py.

O ACHADO PRINCIPAL: A ILHA DO CAMPECHE NAO DEVOLVE O DINHEIRO
--------------------------------------------------------------
O site oficial da Prefeitura (ilhadocampeche.pmf.sc.gov.br), lido em
07/11/2026, poe a regra antes do botao de reservar: "Nao e possivel
reagendamento ou restituicao do valor pago" e "A prefeitura nao se
responsabiliza por impossibilidade de visitacao devido as condicoes
meteorologicas ou de navegacao". E o voucher "sera liberado 24 horas apos
a compensacao" do pagamento. Quem paga no dia nao entra no dia; quem paga
e pega mar ruim perde. O limite e de 800 visitantes por dia, das 9h as
17h, e a taxa municipal e de R$ 15 (ND Mais, 18/01/2026 - o valor so
aparece no site depois do login), alem do barco.

O SEGUNDO: AS FORTALEZAS NAO COBRAM NO ULTIMO DOMINGO DO MES
--------------------------------------------------------------
fortalezas.ufsc.br: "No ultimo domingo de cada mes, entre marco e
novembro, a visitacao e gratuita para todo o publico nas tres
Fortalezas". Nos outros dias, R$ 20 a inteira (Resolucao Normativa
n. 39/2026/CC). E Anhatomirim esta "temporariamente fechada" por obra no
trapiche; nas ilhas a portaria so aceita dinheiro.

O TERCEIRO: A PASSAGEM DE ONIBUS MAIS CARA ENTRE AS CAPITAIS
--------------------------------------------------------------
R$ 7,70 no QR Code desde 1/jan/2026, R$ 7,20 no Cartao Turista, R$ 6,20
no Cartao Cidadao do morador, R$ 20 nas linhas executivas (ND Mais). E o
pagamento em dinheiro saiu de dentro do onibus em 5/jan/2026.

O QUE FICOU SEM RESPOSTA
--------------------------------------------------------------
    hospedagem        nenhum orgao publica a diaria media; sem estimativa
    tarifa de onibus  o decreto nao foi achado no site da Prefeitura; os
                      valores vem da imprensa e estao marcados
    barcos            Campeche e Costa da Lagoa: preco de cada associacao,
                      sem tabela oficial
    Ponte e Mercado   horarios nao achados em fonte oficial

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


IMP = FLAG % "Tarifa oficial noticiada pela imprensa"

# =====================================================================
#  FLORIANOPOLIS
# =====================================================================
FLORIPA = {
    "slug": "florianopolis",
    "nome": "Florianópolis",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "Florianópolis: 8 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 8 pontos de Florianópolis, com a Ilha do "
                  "Campeche que não devolve o dinheiro e as fortalezas que não cobram no "
                  "último domingo do mês."),
    "abertura": ("Oito pontos de Florianópolis com preço, horário e fonte conferidos em 7 "
                 "de novembro de 2026 — e duas regras que os guias não contam: <b>a Ilha "
                 "do Campeche só libera o voucher 24 horas depois de o pagamento "
                 "compensar, e não devolve nem reagenda, nem com mar ruim</b>; e <b>as "
                 "fortalezas da UFSC não cobram no último domingo de cada mês</b>, de "
                 "março a novembro. A praia, por lei, é de graça."),
    "busca": ("florianopolis floripa ilha de santa catarina sc brasil praia campeche "
              "fortaleza ufsc ponta grossa ratones anhatomirim ponte hercilio luz mercado "
              "publico lagoa da conceicao costa da lagoa joaquina jurere onibus"),
    "grupos": [
        {"id": "g1", "titulo": "O que cobra para entrar: Campeche e as fortalezas",
         "intro": ("A ilha com limite diário e regra sem devolução, e as três fortalezas "
                   "do século XVIII que a UFSC administra — e libera um domingo por "
                   "mês.")},
        {"id": "g2", "titulo": "O que não cobra",
         "intro": ("As praias, que a lei federal garante de acesso livre, a ponte, o "
                   "mercado e a Lagoa — só o barco cobra.")},
        {"id": "g3", "titulo": "Circular, e a conta da cama",
         "intro": ("O ônibus mais caro entre as capitais, com preço diferente para turista "
                   "e para morador, e a hospedagem sem diária oficial — numa cidade sem "
                   "taxa turística.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - o que cobra
        # =============================================================
        {
            "id": "ilha-do-campeche",
            "foto": {"arq": "florianopolis/ilha-do-campeche.webp",
                     "alt": "Pedras arredondadas e água transparente na Ilha do Campeche, com a praia e o morro ao fundo",
                     "cred": "Rodrigo Soldon · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Ilha do Campeche",
            "tag": "Ilha",
            "preco_val": "R$ 15",
            "preco_nota": "taxa municipal; o barco é à parte e não devolve",
            "campos": [
                ("A regra que faz perder o dinheiro",
                 "Fonte: site oficial da <b>Prefeitura de Florianópolis</b> "
                 "(ilhadocampeche.pmf.sc.gov.br), consultado em 7/nov/2026.<br>"
                 "<i>“Não é possível reagendamento ou restituição do valor pago.”</i><br>"
                 "<i>“A prefeitura não se responsabiliza por impossibilidade de visitação "
                 "devido às condições meteorológicas ou de navegação.”</i> E o próprio "
                 "site pede: <i>“Verifique a previsão do tempo antes de fazer a sua "
                 "reserva!”</i><br>"
                 "<b>O voucher só é liberado 24 horas depois de o pagamento "
                 "compensar.</b> Quem descobre o Campeche no dia não entra no dia."),
                ("Quanto custa, e o limite",
                 IMP +
                 "a reportagem do ND Mais de 18/01/2026 dá <b>R$ 15 por pessoa</b> de taxa "
                 "municipal, emitida no site — o valor só aparece no site oficial depois "
                 "do login. <b>O barco é à parte</b>, de uma das associações credenciadas "
                 "que o site lista, e a mesma reportagem fala em R$ 185 a R$ 250 por "
                 "pessoa. <b>Não há tabela oficial do barco.</b><br>"
                 "<b>Limite de 800 visitantes por dia, com acesso das 9h às 17h</b>, na "
                 "mesma reportagem.<br>"
                 "A ilha é tombada pelo IPHAN desde 2000 e virou Monumento Natural "
                 "Municipal em 2025 — <i>“a maior concentração de oficinas líticas e "
                 "inscrições rupestres do litoral brasileiro”</i>, diz o site."),
                ("Onde fica",
                 mapa("Ilha do Campeche, Florianópolis, SC")),
            ],
        },
        {
            "id": "fortaleza-ponta-grossa",
            "foto": {"arq": "florianopolis/fortaleza-ponta-grossa.webp",
                     "alt": "A muralha de pedra e a guarita da Fortaleza de São José da Ponta Grossa, entre árvores",
                     "cred": "Luluhgomes · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Fortaleza de São José da Ponta Grossa",
            "tag": "Fortaleza",
            "preco_val": "R$ 20",
            "preco_nota": "grátis no último domingo do mês, de março a novembro",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página da taxa de visitação do <b>Departamento das Fortalezas da "
                 "UFSC</b> (fortalezas.ufsc.br), consultada em 7/nov/2026, com os valores "
                 "da <b>Resolução Normativa nº 39/2026/CC, de 11 de junho de 2026</b>.<br>"
                 "<b>Inteira: R$ 20,00. Meia: R$ 10,00</b> — estudante, professor da "
                 "educação básica, doador de sangue de SC, entre outros.<br>"
                 "Paga-se no site ou na portaria, <b>em dinheiro ou PIX</b>."),
                ("O domingo que não cobra",
                 "<i>“No último domingo de cada mês, entre março e novembro, a visitação "
                 "é gratuita para todo o público nas três Fortalezas administradas pela "
                 "Universidade Federal de Santa Catarina.”</i><br>"
                 "<b>Em 2026 o último é 29 de novembro.</b> Dezembro, janeiro e fevereiro "
                 "— a temporada — não têm o dia grátis."),
                ("Dias e horários",
                 "<b>Todos os dias, 8h30 às 18h30, inclusive feriados</b>, com entrada "
                 "até 18h. Fica na Praia do Forte, no norte da ilha, e se chega por "
                 "terra."),
                ("Onde fica",
                 mapa("Fortaleza de São José da Ponta Grossa, Praia do Forte, Florianópolis, SC")),
            ],
        },
        {
            "id": "fortaleza-ratones",
            "grupo": "g1",
            "nome": "Fortalezas das ilhas: Ratones e Anhatomirim",
            "tag": "Fortaleza",
            "preco_val": "R$ 20",
            "preco_nota": "portaria só aceita dinheiro; Anhatomirim fechada",
            "campos": [
                ("Valor, e o dinheiro em espécie",
                 "Mesma fonte e mesma resolução: <b>R$ 20 a inteira, R$ 10 a meia</b>. "
                 "Havia o ingresso duplo para as duas ilhas, a R$ 30.<br>"
                 "<b>Na portaria das ilhas, só dinheiro</b> — <i>“Fortalezas de Santa "
                 "Cruz de Anhatomirim e Santo Antônio de Ratones: pagamento aceito apenas "
                 "em dinheiro.”</i> Ou pague antes, no site."),
                ("Anhatomirim está fechada",
                 "<i>“Temporariamente fechada em virtude das obras no trapiche de "
                 "acesso.”</i> Em 7/nov/2026, só <b>Santo Antônio de Ratones</b> recebia "
                 "visita entre as das ilhas — todos os dias, 8h30 às 18h30.<br>"
                 "<b>O barco não é da UFSC</b>: <i>“A UFSC não é responsável pelo traslado "
                 "a essas ilhas”</i>. O valor é de cada empresa náutica."),
                ("Onde fica",
                 mapa("Fortaleza de Santo Antônio de Ratones, Ilha de Ratones Grande, Florianópolis, SC")),
            ],
        },
        # =============================================================
        #  g2 - o que nao cobra
        # =============================================================
        {
            "id": "praias",
            "foto": {"arq": "florianopolis/praias.webp",
                     "alt": "As dunas da Praia da Joaquina vistas do alto, com o mar e os morros ao fundo",
                     "cred": "Amanda Likes · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "As praias",
            "tag": "Praia",
            "preco_val": "Grátis",
            "preco_nota": "acesso livre por lei federal",
            "campos": [
                ("O que a lei diz",
                 "Fonte: <b>Lei federal nº 7.661/1988</b>, artigo 10: <i>“As praias são "
                 "bens públicos de uso comum do povo, sendo assegurado, sempre, livre e "
                 "franco acesso a elas e ao mar, em qualquer direção e sentido”</i>.<br>"
                 "<b>Ninguém pode cobrar para você pisar na areia</b> — nem condomínio, "
                 "nem beach club. O que se cobra é estacionamento, cadeira e guarda-sol, "
                 "e isso é serviço, não acesso."),
                ("Onde fica",
                 mapa("Praia da Joaquina, Florianópolis, SC")),
            ],
        },
        {
            "id": "centro",
            "foto": {"arq": "florianopolis/centro.webp",
                     "alt": "A Ponte Hercílio Luz, ponte pênsil de 1926, ligando a ilha ao continente",
                     "cred": "Daniel Becher · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Ponte Hercílio Luz e Mercado Público",
            "tag": "Centro",
            "preco_val": "Grátis",
            "preco_nota": "horários não achados em fonte oficial",
            "campos": [
                ("O que não cobra",
                 "<b>A Ponte Hercílio Luz</b>, a ponte pênsil de 1926, reaberta em 2019, "
                 "se atravessa a pé sem pagar. <b>O Mercado Público</b>, no centro, também "
                 "não cobra entrada — paga-se o que se consome.<br>"
                 "Em maio de 2026 um vereador falou em cobrar visitação na ponte para a "
                 "manutenção; <b>não há projeto de lei</b>, segundo o ND Mais."),
                ("O que não está publicado",
                 FLAG % "Lacuna declarada" +
                 "<b>não achamos em fonte oficial o horário da ponte para pedestres nem o "
                 "do Mercado.</b> O que circula é de matérias de 2019 a 2021, do tempo das "
                 "obras."),
                ("Onde fica",
                 mapa("Ponte Hercílio Luz, Florianópolis, SC")),
            ],
        },
        {
            "id": "lagoa",
            "foto": {"arq": "florianopolis/lagoa.webp",
                     "alt": "A Lagoa da Conceição vista do morro, com o casario à beira d'água",
                     "cred": "Rodrigo Soldon · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Lagoa da Conceição e Costa da Lagoa",
            "tag": "Lagoa",
            "preco_val": "Grátis",
            "preco_nota": "o barco da Costa da Lagoa cobra; fontes divergem",
            "campos": [
                ("O que cobra e o que não",
                 "<b>A Lagoa, o Centrinho e as dunas da Joaquina não cobram.</b> A <b>Costa "
                 "da Lagoa</b>, a vila sem estrada do outro lado, se alcança de barco, "
                 "pela cooperativa que sai do Centrinho."),
                ("O preço do barco",
                 FLAG % "Fontes divergem" +
                 "guias de viagem citam <b>R$ 12,50 e R$ 15</b> por trecho, e <b>R$ 2,50 "
                 "para o morador cadastrado</b> da Costa. Não há tabela oficial publicada; "
                 "a própria cooperativa divulga horários pelo Instagram. <b>Esta linha fica "
                 "fora da conta.</b>"),
                ("Onde fica",
                 mapa("Lagoa da Conceição, Florianópolis, SC")),
            ],
        },
        # =============================================================
        #  g3 - circular e a cama
        # =============================================================
        {
            "id": "onibus",
            "grupo": "g3",
            "nome": "O ônibus, e o cartão de turista",
            "tag": "Transporte",
            "preco_val": "R$ 7,20",
            "preco_nota": "Cartão Turista; R$ 7,70 no QR Code",
            "campos": [
                ("Quanto custa, e quem paga menos",
                 IMP +
                 "a tarifa municipal subiu em <b>1º de janeiro de 2026</b> (ND Mais):<br>"
                 "<b>QR Code: R$ 7,70.</b><br>"
                 "<b>Cartão Turista: R$ 7,20.</b><br>"
                 "<b>Cartão Cidadão, do morador: R$ 6,20.</b><br>"
                 "Linhas executivas: <b>R$ 20</b>.<br>"
                 "<b>É a passagem mais cara entre as capitais</b>, e o turista paga R$ 1 a "
                 "mais por viagem que o morador."),
                ("O dinheiro saiu do ônibus",
                 FLAG % "Fontes divergem" +
                 "desde <b>5 de janeiro de 2026</b> o ônibus não aceita dinheiro — uma "
                 "reportagem diz que em lugar nenhum; outra, que só nas bilheterias dos "
                 "terminais. O Cartão Passe Rápido dá <b>integração de três horas</b> entre "
                 "linhas.<br>"
                 + FLAG % "Lacuna declarada" +
                 "não achamos o decreto da tarifa no site da Prefeitura."),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem, e a taxa que não existe",
            "tag": "Conta, não lugar",
            "preco_val": "sem dado oficial",
            "preco_nota": "Florianópolis não cobra taxa turística",
            "campos": [
                ("Por que não há diária nesta ficha",
                 FLAG % "Lacuna declarada" +
                 "<b>Nenhum órgão publica a diária média de Florianópolis.</b> A regra "
                 "desta casa é não estimar: a ficha mostra o total sem a hospedagem, e "
                 "diz isso no rótulo — como em Gramado e Fortaleza."),
                ("A taxa que não existe",
                 "<b>Florianópolis não cobra taxa turística de quem se hospeda.</b> O que "
                 "a cidade passou a cobrar, desde o fim de novembro de 2025, é o <b>Selo "
                 "Turismo Legal</b>, de <b>veículos de turismo</b>: R$ 225 por ônibus "
                 "sem pernoite, R$ 135 por micro-ônibus, R$ 105 por van (Brasilturis, "
                 "28/11/2025). <b>Quem chega de carro ou de avião não paga.</b>"),
            ],
        },
    ],
}

DESTINOS = [FLORIPA]
