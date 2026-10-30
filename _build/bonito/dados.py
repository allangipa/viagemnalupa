# -*- coding: utf-8 -*-
"""Bonito: o vigesimo quinto destino, em oito pontos e tres grupos.

Mesmo molde do fernando-de-noronha/dados.py.

O ACHADO PRINCIPAL: O PRECO E TABELADO, E QUASE NINGUEM OFICIAL O PUBLICA
--------------------------------------------------------------------------
Em Bonito todo passeio se compra por agencia credenciada, com voucher, e o
preco de cada atrativo e o mesmo em qualquer agencia. Mas o atrativo nao o
publica: nas paginas lidas do Rio da Prata, Buraco das Araras, Abismo
Anhumas e Boca da Onca nao ha preco, e a prefeitura nao publica o da
Gruta do Lago Azul nem o do Balneario Municipal, que ela administra. Em
fonte oficial, so a TCA (prefeitura) e o tarifario do Nascente Azul.

Decisao do Allan em 29/10/2026: o total da ficha leva so o oficial; os
precos de agencia aparecem no texto, marcados "So em fonte secundaria" e
fora do total.

O SEGUNDO: O MORADOR PAGA MENOS DA METADE
--------------------------------------------------------------------------
No tarifario do Nascente Azul (valido ate 12/12/2026), a flutuacao custa
R$ 374 ao adulto na baixa temporada, R$ 337 a quem mora em MS e R$ 162 a
quem mora em Bonito - 43% do preco do turista.

O TERCEIRO: A TCA CONTA SO OS DIAS DE PASSEIO
--------------------------------------------------------------------------
A nota da prefeitura: "O sistema gera o valor total da taxa referente aos
dias em que ha visitacao em atrativos". R$ 15 por pessoa por dia de passeio,
nao por dia na cidade.

O QUE FICOU SEM RESPOSTA
--------------------------------------------------------------------------
    precos de atrativo  so em agencia (ver acima); dois com validade vencida
    hospedagem          nenhum orgao publica diaria media de Bonito
    transporte          os atrativos ficam fora da cidade; o traslado e
                        vendido pela agencia, sem tabela oficial
    calendario          o Nascente Azul segue o calendario do COMTUR, mas a
                        pagina mostra o de 2025

Fontes guardadas em _build/bonito/fontes/. Apuracao de 29 de outubro de 2026.
"""

APURACAO = "29 de outubro de 2026"
APURACAO_CURTA = "29/out/2026"

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


AGENCIA = ("tabela de 2026 de uma agência credenciada (Acqua Viagens, atualizada em "
           "16/fev/2026), lida em 29/out/2026")

BONITO = {
    "slug": "bonito",
    "nome": "Bonito",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "Bonito: 8 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 8 pontos de Bonito, com o preço tabelado que "
                  "quase nenhum atrativo publica, a taxa ambiental que conta só os dias de "
                  "passeio e o morador que paga menos da metade."),
    "abertura": ("Oito pontos de Bonito com preço, horário e fonte conferidos em 29 de "
                 "outubro de 2026 — e uma coisa que muda a forma de ler os preços: <b>todo "
                 "passeio tem preço tabelado, igual em qualquer agência, mas quase nenhum "
                 "atrativo o publica.</b> Em fonte oficial só achamos a taxa ambiental e o "
                 "tarifário do Nascente Azul; o resto vem de agência e está marcado assim. "
                 "<b>E o morador paga menos da metade:</b> a flutuação do Nascente Azul "
                 "custa R$ 374 ao turista e R$ 162 a quem mora em Bonito."),
    "busca": ("bonito mato grosso do sul ms brasil serra da bodoquena voucher unico tca "
              "taxa de conservacao ambiental flutuacao nascente azul rio da prata gruta do "
              "lago azul balneario municipal abismo anhumas buraco das araras"),
    "grupos": [
        {"id": "g1", "titulo": "Como Bonito cobra",
         "intro": ("Agência obrigatória, voucher por passeio, preço tabelado que quase "
                   "ninguém publica — e uma taxa da prefeitura por dia de passeio.")},
        {"id": "g2", "titulo": "As águas: flutuação, gruta e balneário",
         "intro": ("O único atrativo com tarifário oficial publicado, o Rio da Prata que "
                   "não publica, e os dois atrativos da prefeitura.")},
        {"id": "g3", "titulo": "O mais caro, e a cama",
         "intro": ("O Abismo Anhumas, a R$ 1.598 em tabela de agência, e a hospedagem, "
                   "sem diária oficial publicada.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - como Bonito cobra
        # =============================================================
        {
            "id": "voucher",
            "grupo": "g1",
            "nome": "O voucher e a agência obrigatória",
            "tag": "Regra",
            "preco_val": "tabelado",
            "preco_nota": "igual em qualquer agência; quase nenhum atrativo publica",
            "campos": [
                ("Como se compra",
                 "Fonte: tarifário oficial do Nascente Azul (nascenteazul.com.br), "
                 "consultado em 29/out/2026: <i>“Todos os passeios de Bonito e região são "
                 "operados exclusivamente pelas Agências de Turismo locais e têm os valores "
                 "de cada atividade tabelados.”</i><br>"
                 "<b>Não se compra na porta do atrativo.</b> A agência emite um voucher por "
                 "passeio, com data e horário, e a TCA da prefeitura é paga antes, num "
                 "portal próprio."),
                ("O preço que ninguém publica",
                 FLAG % "Lacuna declarada" +
                 "<b>O preço é o mesmo em toda agência, mas os atrativos não o publicam.</b> "
                 "Nas páginas que lemos do Rio da Prata, do Buraco das Araras, do Abismo "
                 "Anhumas e da Boca da Onça não há preço; o Rio da Prata tem uma página "
                 "“Onde comprar”. A "
                 "prefeitura não publica o da Gruta do Lago Azul nem o do Balneário "
                 "Municipal, que ela administra.<br>"
                 "<b>Os preços de agência desta página estão marcados como fonte "
                 "secundária</b> e ficam fora do total da ficha de custos."),
            ],
        },
        {
            "id": "tca",
            "foto": {"arq": "bonito/tca.webp",
                     "alt": "Cardume de peixes no Rio Formoso, em Bonito, visto de cima da água cristalina",
                     "cred": "Ateliesandraromano · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Taxa de Conservação Ambiental (TCA)",
            "tag": "Taxa",
            "preco_val": "R$ 15",
            "preco_nota": "por pessoa, por dia de passeio; menor de 7 não paga",
            "campos": [
                ("Valor, e o que conta como dia",
                 "Fonte: <b>Prefeitura Municipal de Bonito</b>, nota informativa de "
                 "19/11/2025 (atualizada em 27/11/2025), consultada em 29/out/2026. "
                 "Cobrança desde 20 de dezembro de 2025, pela Lei Municipal 162/2021.<br>"
                 "<b>R$ 15,00 por dia, por pessoa</b>, brasileiro ou estrangeiro.<br>"
                 "<b>Conta só os dias de passeio:</b> <i>“O sistema gera o valor total da "
                 "taxa referente aos dias em que há visitação em atrativos.”</i> Quatro "
                 "dias na cidade com três de passeio: R$ 45."),
                ("Quem não paga, e o que vem junto",
                 "<b>Menor de 7 anos</b>, morador de Bonito e quem trabalha no município.<br>"
                 "Paga-se só pelo portal <b>turistapornatureza.com.br</b>, antes da emissão "
                 "dos vouchers. Em troca, a prefeitura dá um <b>seguro ao visitante</b> "
                 "(morte acidental e invalidez até R$ 20 mil) e atendimento pré-hospitalar "
                 "das 7h às 19h."),
                ("A taxa na Justiça",
                 SEC +
                 "<b>associações do turismo contestam a taxa num mandado de segurança</b>, "
                 "que o Tribunal de Justiça de MS reabriu (Campo Grande News). Até a "
                 "consulta desta ficha, a cobrança seguia valendo."),
            ],
        },
        # =============================================================
        #  g2 - as aguas
        # =============================================================
        {
            "id": "nascente-azul",
            "foto": {"arq": "bonito/nascente-azul.webp",
                     "alt": "Uma pessoa flutuando de máscara e snorkel sobre a água cristalina e as plantas do fundo, no Nascente Azul",
                     "cred": "Jamiledsp · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Nascente Azul",
            "tag": "Flutuação",
            "preco_val": "R$ 374",
            "preco_nota": "baixa temporada; R$ 462 na alta; morador de Bonito R$ 162",
            "campos": [
                ("O tarifário oficial",
                 "Fonte: tarifário publicado pelo próprio atrativo (nascenteazul.com.br), "
                 "consultado em 29/out/2026: <i>“Os valores a seguir são referentes ao ano "
                 "de 2025/2026, válidos até 12/12/2026”</i>.<br>"
                 "<b>Flutuação + day-use, adulto: R$ 374 na baixa temporada, R$ 462 na "
                 "alta.</b> 7 a 11 anos: R$ 337 / R$ 418. 4 a 6 anos: R$ 33,70 / R$ 41,80.<br>"
                 "<b>Morador de MS: R$ 337. Morador de Bonito: R$ 162</b> — os dois só na "
                 "baixa temporada. O bonitense paga 43% do preço do turista.<br>"
                 "Só o balneário (day-use): R$ 126 na baixa, R$ 139 na alta."),
                ("Dias e horários",
                 "<b>Alta temporada: todos os dias, 7h às 17h. Baixa temporada: de quarta "
                 "a segunda, 8h às 16h</b> — <b>fecha na terça</b>.<br>"
                 + FLAG % "Fontes divergem" +
                 "<b>a página diz seguir o calendário de temporadas do COMTUR, mas mostra o "
                 "calendário de 2025</b>, embora os preços valham até dezembro de 2026. "
                 "Confira com a agência em que temporada cai a sua data."),
                ("Onde fica",
                 mapa("Nascente Azul, Rodovia Bonito Bodoquena km 22, Bonito, MS")),
            ],
        },
        {
            "id": "rio-da-prata",
            "grupo": "g2",
            "nome": "Recanto Ecológico Rio da Prata",
            "tag": "Flutuação",
            "preco_val": "sem preço oficial",
            "preco_nota": "agência: R$ 470 na baixa, R$ 570 na alta",
            "campos": [
                ("O preço",
                 SEC +
                 "<b>o site do Rio da Prata não publica preço</b>; tem só uma página "
                 "“Onde comprar”. Na " + AGENCIA + ", a flutuação sai por <b>R$ 470 na baixa "
                 "temporada e R$ 570 na alta</b>, com validade até 31/12/2026."),
                ("O que o próprio site diz",
                 "Fonte: perguntas frequentes do site oficial (riodaprata.eco.br), "
                 "consultadas em 29/out/2026.<br>"
                 "<b>Idade mínima: 5 anos</b>; menor de 12, acompanhado dos pais.<br>"
                 "<b>Começou, não tem volta:</b> <i>“Não é possível ressarcir o valor do "
                 "passeio de crianças e adultos após o início da atividade, mesmo que não "
                 "seja realizada completamente.”</i>"),
                ("Onde fica",
                 mapa("Recanto Ecológico Rio da Prata, Jardim, MS")),
            ],
        },
        {
            "id": "gruta-do-lago-azul",
            "foto": {"arq": "bonito/gruta-do-lago-azul.webp",
                     "alt": "O lago azul no fundo da gruta, sob as estalactites, na Gruta do Lago Azul",
                     "cred": "Valdiney Pimenta · CC BY 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Gruta do Lago Azul",
            "tag": "Gruta",
            "preco_val": "sem preço oficial",
            "preco_nota": "a prefeitura administra e não publica o preço",
            "campos": [
                ("O preço",
                 SEC +
                 "<b>a Gruta é administrada pela prefeitura, que não publica o preço do "
                 "ingresso.</b> Na " + AGENCIA + ", R$ 120 na baixa temporada e R$ 180 na "
                 "alta.<br>"
                 + FLAG % "Validade vencida" +
                 "<b>a própria tabela da agência dá validade até 30/06/2026</b> para esse "
                 "valor. Pode ter mudado; confirme na compra."),
                ("O que a prefeitura publica",
                 "Fonte: Prefeitura de Bonito, notícia de 21/out/2026: o município prepara "
                 "para 2027 ações de segurança, acessibilidade e o recadastramento dos "
                 "guias da Gruta. Nenhuma linha sobre preço ou horário."),
                ("Onde fica",
                 mapa("Gruta do Lago Azul, Bonito, MS")),
            ],
        },
        {
            "id": "balneario-municipal",
            "foto": {"arq": "bonito/balneario-municipal.webp",
                     "alt": "A água verde e transparente do Balneário Municipal de Bonito, com peixes e folhas de palmeira",
                     "cred": "Moisés Aguiar 1989 · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Balneário Municipal",
            "tag": "Balneário",
            "preco_val": "sem preço oficial",
            "preco_nota": "a prefeitura administra e não publica o preço",
            "campos": [
                ("O preço",
                 SEC +
                 "<b>o Balneário é da prefeitura, e o preço não está no site dela.</b> Na "
                 + AGENCIA + ", R$ 70 na baixa temporada e R$ 98 na alta.<br>"
                 + FLAG % "Validade vencida" +
                 "<b>a tabela da agência dá validade até 30/06/2026</b> para esse valor."),
                ("O que a prefeitura publica",
                 "Fonte: Prefeitura de Bonito, notícia de 23/set/2026: o Balneário "
                 "concluiu a construção e a reforma dos decks. Também sem preço."),
                ("Onde fica",
                 mapa("Balneário Municipal de Bonito, MS")),
            ],
        },
        # =============================================================
        #  g3 - o mais caro e a cama
        # =============================================================
        {
            "id": "abismo-anhumas",
            "foto": {"arq": "bonito/abismo-anhumas.webp",
                     "alt": "Um facho de luz entra pela abertura do Abismo Anhumas e ilumina o lago, com um bote na água",
                     "cred": "Caio Vilela · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Abismo Anhumas",
            "tag": "Rapel e flutuação",
            "preco_val": "sem preço oficial",
            "preco_nota": "agência: R$ 1.598, o mais caro da tabela",
            "campos": [
                ("O preço",
                 SEC +
                 "<b>o site do Abismo não publica preço.</b> Na " + AGENCIA + ", a "
                 "flutuação sai por <b>R$ 1.598, na baixa e na alta</b>, com validade até "
                 "28/02/2027 — mais que quatro dias de Nascente Azul. É o passeio mais "
                 "caro daquela tabela."),
                ("Onde fica",
                 mapa("Abismo Anhumas, Bonito, MS")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem e traslado",
            "tag": "Conta, não lugar",
            "preco_val": "sem dado oficial",
            "preco_nota": "nem diária nem traslado têm tabela oficial",
            "campos": [
                ("Por que não há diária nesta ficha",
                 FLAG % "Lacuna declarada" +
                 "<b>Nenhum órgão publica a diária média de Bonito.</b> O Panorama da "
                 "Hotelaria Brasileira (FOHB/HotelInvest) não traz a cidade.<br>"
                 "<b>A regra desta casa é não estimar.</b> A ficha de custos mostra o total "
                 "sem a hospedagem, e diz isso no rótulo."),
                ("O traslado",
                 FLAG % "Lacuna declarada" +
                 "<b>os atrativos ficam fora da cidade</b> — o Nascente Azul no km 22 da "
                 "rodovia para Bodoquena, o Rio da Prata em Jardim — e o traslado é vendido "
                 "pela agência junto com o voucher, sem tabela oficial."),
            ],
        },
    ],
}

DESTINOS = [BONITO]
