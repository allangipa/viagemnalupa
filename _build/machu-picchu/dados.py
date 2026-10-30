# -*- coding: utf-8 -*-
"""Machu Picchu: o vigesimo sexto destino, em oito pontos e tres grupos.

Mesmo molde do bonito/dados.py.

O ACHADO PRINCIPAL: O BRASILEIRO PAGA 2,4 VEZES O PERUANO
----------------------------------------------------------
A tarifa promocional de 2026 (R.M. 000284-2025-MC, pela Andina) e S/ 64
para peruano, residente e cidadao da Comunidade Andina - Bolivia, Colombia,
Equador e Peru. O Brasil nao e membro da CAN: o brasileiro paga a tarifa de
estrangeiro, S/ 152 (El Comercio e Infobae, fev/2026, atribuindo ao
Ministerio da Cultura) - 2,38 vezes. E desde 1/5/2026 soma-se a tarifa do
SERNANP, S/ 11 para estrangeiro.

O SEGUNDO: A TAXA DO SERNANP FOI ADIADA QUATRO VEZES ANTES DE PEGAR
--------------------------------------------------------------------------
A R.D. 000006-2026-SERNANP/DUSRN (El Peruano, 4/2/2026) registra as datas
anteriores: 1/1/2024, 1/1/2025, 1/1/2026 e 1/2/2026. A quinta, 1/5/2026,
foi a que valeu.

COMO OS NUMEROS ENTRAM (decisao do Allan em 29/10/2026)
--------------------------------------------------------------------------
A tabela oficial do Ministerio (tuboleto.cultura.pe) so aparece depois do
"no soy un robot", que nao fazemos. Os S/ 152 e os S/ 11 entram no total
marcados como "tarifa oficial noticiada pela imprensa". Onibus, Boleto
Turistico de Cusco e trem ficam fora, com o valor dos guias marcado como
fonte secundaria.

O QUE FICOU SEM RESPOSTA
--------------------------------------------------------------------------
    onibus Consettur   o site estava com certificado invalido
    Boleto Turistico   o site do COSITUC estava fora do ar
    trem               preco por data, de empresa privada
    montanhas          preco do estrangeiro so em guias
    hospedagem         nenhum orgao publica diaria media

Fontes guardadas em _build/machu-picchu/fontes/. Apuracao de 29 de outubro de 2026.
"""

APURACAO = "29 de outubro de 2026"
APURACAO_CURTA = "29/out/2026"

FLAG = '<span class="flag">%s</span> '
SEC = FLAG % "Só em fonte secundária"
IMP = FLAG % "Tarifa oficial noticiada pela imprensa"


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


MACHU = {
    "slug": "machu-picchu",
    "nome": "Machu Picchu",
    "pais": "Peru",
    "regiao": "america-do-sul",
    "titulo": "Machu Picchu: 8 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 8 pontos de Machu Picchu e Cusco, com a "
                  "entrada que custa ao brasileiro 2,4 vezes o que custa ao peruano e a "
                  "taxa ambiental que foi adiada quatro vezes antes de valer."),
    "abertura": ("Oito pontos de Machu Picchu e Cusco com preço, horário e fonte "
                 "conferidos em 29 de outubro de 2026 — e duas coisas que os guias não "
                 "dizem: <b>o brasileiro paga 2,4 vezes o que paga o peruano</b>. A "
                 "tarifa promocional de 2026, S/ 64, vale só para peruanos e cidadãos da "
                 "Comunidade Andina, de que o Brasil não faz parte; o brasileiro paga "
                 "S/ 152. <b>E desde maio há mais S/ 11</b>, de uma taxa ambiental adiada "
                 "quatro vezes antes de começar."),
    "busca": ("machu picchu machupicchu cusco cuzco peru llaqta aguas calientes huayna "
              "picchu montanha machu picchu circuito sernanp consettur peru rail inca rail "
              "boleto turistico caminho inca"),
    "grupos": [
        {"id": "g1", "titulo": "A entrada, e quem paga quanto",
         "intro": ("Um bilhete com hora marcada, três circuitos, uma tarifa para peruanos "
                   "e andinos e outra para o resto do mundo — e a taxa ambiental que entrou "
                   "em maio.")},
        {"id": "g2", "titulo": "Chegar lá em cima",
         "intro": ("O trem até Aguas Calientes, o ônibus até as ruínas e o Caminho Inca: "
                   "três trajetos, nenhum com preço oficial que conseguimos ler.")},
        {"id": "g3", "titulo": "Cusco, e a cama",
         "intro": ("O Boleto Turístico, que abre os sítios do Vale Sagrado e não inclui "
                   "Machu Picchu, e a hospedagem, sem diária oficial publicada.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - a entrada
        # =============================================================
        {
            "id": "boleto",
            "foto": {"arq": "machu-picchu/boleto.webp",
                     "alt": "A cidadela de Machu Picchu vista do alto, com o Huayna Picchu ao fundo e as montanhas em volta",
                     "cred": "Jorge Castro Ruso · CC BY-SA 2.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "O bilhete de Machu Picchu",
            "tag": "Ingresso",
            "preco_val": "S/ 152",
            "preco_nota": "estrangeiro adulto, cerca de R$ 222; peruano e andino S/ 64",
            "campos": [
                ("Quanto custa, e para quem",
                 IMP +
                 "<b>estrangeiro adulto: S/ 152</b>; estudante estrangeiro: S/ 77; menor "
                 "estrangeiro de 3 a 17 anos: de S/ 70 a S/ 125, conforme o circuito (El "
                 "Comercio, 7/fev/2026, e Infobae, 9/fev/2026, atribuindo ao Ministério da "
                 "Cultura). Em real, <b>cerca de R$ 222</b> (R$ 222,12), pela taxa de venda "
                 "do Banco Central de 23/out/2026.<br>"
                 "<b>Peruano, residente e cidadão da Comunidade Andina: S/ 64</b>, tarifa "
                 "promocional de 2026 (R.M. 000284-2025-MC, segundo a Andina, agência de "
                 "notícias do governo peruano). Reduzida: S/ 32. Menor de 3 não paga.<br>"
                 "<b>O Brasil não é membro da Comunidade Andina</b> — Bolívia, Colômbia, "
                 "Equador e Peru são. O brasileiro paga 2,4 vezes o peruano."),
                ("Por que não lemos a tabela oficial",
                 "A venda oficial é só pelo <b>tuboleto.cultura.pe</b>, do Ministério da "
                 "Cultura, e a tabela de preços aparece depois de uma verificação “não sou "
                 "um robô”, que não fazemos. Por isso os valores acima vêm da imprensa "
                 "peruana, que reproduz a tarifa oficial.<br>"
                 + FLAG % "Fontes divergem" +
                 "<b>a Infobae de novembro de 2025 dava US$ 60 ao adulto estrangeiro</b>, "
                 "que não bate com os S/ 152 de fevereiro de 2026. Usamos o mais recente."),
                ("Hora marcada e permanência",
                 "Cada bilhete tem <b>hora exata de entrada</b>, e dá de 4 a 6 horas no "
                 "sítio, conforme o percurso (Infobae, nov/2025). A página oficial dá o "
                 "<b>horário de atenção: todos os dias, 8h às 16h15</b>.<br>"
                 "Há venda presencial em Aguas Calientes, no Centro Cultural de Machu Picchu "
                 "Pueblo, <b>das 15h às 22h, para o dia seguinte</b> — mil bilhetes por dia, "
                 "segundo a Andina."),
                ("Onde fica",
                 mapa("Machu Picchu, Cusco, Peru")),
            ],
        },
        {
            "id": "sernanp",
            "grupo": "g1",
            "nome": "A taxa do SERNANP",
            "tag": "Taxa",
            "preco_val": "S/ 11",
            "preco_nota": "estrangeiro, desde 1º/5/2026; peruano S/ 5",
            "campos": [
                ("O que é, e desde quando",
                 "Fonte oficial da data: <b>Resolução Diretoral 000006-2026-SERNANP/DUSRN</b>, "
                 "publicada no diário oficial El Peruano em 4/fev/2026, consultada em "
                 "29/out/2026: o SERNANP, órgão das áreas naturais protegidas, cobra a "
                 "tarifa de ingresso ao Santuário Histórico <b>“a partir del 01 de mayo de "
                 "2026”</b>.<br>"
                 + IMP +
                 "<b>S/ 11 para estrangeiro, S/ 5 para peruano</b>, somados ao bilhete (El "
                 "Comercio e Infobae, fev/2026). O valor não está no texto da resolução. "
                 "Quem chega pelo Caminho Inca não paga."),
                ("Adiada quatro vezes",
                 "A própria resolução lista as datas anteriores de início: <b>1º/1/2024, "
                 "1º/1/2025, 1º/1/2026 e 1º/2/2026</b>. A quinta, 1º de maio de 2026, foi a "
                 "que valeu. Não achamos notícia de suspensão depois disso."),
            ],
        },
        {
            "id": "circuitos",
            "foto": {"arq": "machu-picchu/circuitos.webp",
                     "alt": "Os terraços e as construções de pedra de Machu Picchu sob a névoa, com o Huayna Picchu atrás",
                     "cred": "Allard Schmidt · domínio público · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Os três circuitos e as montanhas",
            "tag": "Regra",
            "preco_val": "3 circuitos",
            "preco_nota": "a montanha custa mais; quatro rotas só na alta temporada",
            "campos": [
                ("Circuitos e rotas",
                 "Fonte: <b>Ministério da Cultura</b>, tuboleto.cultura.pe, consultado em "
                 "29/out/2026: desde 1º de junho de 2024 o sítio tem <b>três circuitos e 10 "
                 "rotas</b> — Circuito 1, Panorâmico; Circuito 2, Clássico; Circuito 3, "
                 "Realeza.<br>"
                 "Segundo a Andina: <b>as rotas 1-C, 1-D, 3-C e 3-D só abrem na temporada "
                 "alta</b>. As de montanha são a 1-A (Montanha Machu Picchu), a 3-A (Huayna "
                 "Picchu) e a 3-C (Grande Caverna)."),
                ("Quanto custa a montanha",
                 "Para peruano e andino, a rota com montanha custa <b>S/ 112</b>, contra "
                 "S/ 64 dos circuitos (Andina).<br>"
                 + SEC +
                 "<b>para estrangeiro, guias de viagem citam S/ 200</b>; não achamos o valor "
                 "na imprensa nem em fonte oficial legível."),
                ("Quantos entram por dia",
                 "<b>5.600 visitantes na temporada alta, 4.500 no resto do ano</b> (R.M. "
                 "000285-2025-MC, pela Andina). A alta de 2026: 1º/1, 2 a 5/4, <b>19/6 a "
                 "2/11</b> e 30–31/12."),
            ],
        },
        # =============================================================
        #  g2 - chegar la em cima
        # =============================================================
        {
            "id": "trem",
            "foto": {"arq": "machu-picchu/trem.webp",
                     "alt": "Um trem azul subindo o vale ao lado do Rio Urubamba",
                     "cred": "Sashimi-b · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "O trem até Aguas Calientes",
            "tag": "Transporte",
            "preco_val": "por data",
            "preco_nota": "empresa privada; o preço muda com o dia e o horário",
            "campos": [
                ("O que se sabe",
                 FLAG % "Lacuna declarada" +
                 "<b>Machu Picchu fica a 210 km de Cusco</b>, diz a página oficial, e o "
                 "caminho habitual é de trem até Aguas Calientes (Machu Picchu Pueblo). Os "
                 "trens são de <b>empresas privadas, com preço por data e horário</b>, sem "
                 "tabela única. Não entra na conta."),
                ("Onde fica",
                 mapa("Estação de Aguas Calientes, Machu Picchu Pueblo, Peru")),
            ],
        },
        {
            "id": "onibus",
            "foto": {"arq": "machu-picchu/onibus.webp",
                     "alt": "A estátua de Pachacútec com uma águia de asas abertas, numa praça de Aguas Calientes",
                     "cred": "Diego Delso · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "O ônibus até as ruínas",
            "tag": "Transporte",
            "preco_val": "sem preço oficial",
            "preco_nota": "guias citam US$ 24 ida e volta",
            "campos": [
                ("O preço",
                 SEC +
                 "<b>o site da Consettur, que faz o trajeto de Aguas Calientes até a entrada, "
                 "estava com certificado de segurança inválido</b> em 29/out/2026 e não "
                 "abriu. Guias de viagem citam <b>US$ 24 ida e volta</b> para estrangeiro. "
                 "Não entra na conta."),
                ("Onde fica",
                 mapa("Consettur, Aguas Calientes, Peru")),
            ],
        },
        {
            "id": "caminho-inca",
            "foto": {"arq": "machu-picchu/caminho-inca.webp",
                     "alt": "O vale visto do Inti Punku, a Porta do Sol, no fim do Caminho Inca, com a estrada em zigue-zague até Machu Picchu",
                     "cred": "Bastian Greshake Tzovaras · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "O Caminho Inca",
            "tag": "Trilha",
            "preco_val": "por agência",
            "preco_nota": "fechado em fevereiro; quem chega por ele não paga o SERNANP",
            "campos": [
                ("Como funciona",
                 "Segundo a Andina (dez/2025): quem chega pela <b>Rede de Caminhos Inca</b> "
                 "entra por cotas diárias, reservadas e pagas por <b>agências "
                 "autorizadas</b> (R.M. 000306-2025-MC). <b>Em fevereiro não há percursos</b>, "
                 "por manutenção.<br>"
                 "Quem chega por ele <b>não paga a taxa do SERNANP</b> (El Comercio).<br>"
                 + FLAG % "Lacuna declarada" +
                 "<b>o preço é da agência, e não achamos tabela oficial.</b>"),
            ],
        },
        # =============================================================
        #  g3 - Cusco e a cama
        # =============================================================
        {
            "id": "boleto-turistico",
            "foto": {"arq": "machu-picchu/boleto-turistico.webp",
                     "alt": "A Plaza de Armas de Cusco num dia de sol, com a catedral ao fundo e as montanhas em volta",
                     "cred": "Diego Delso · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Boleto Turístico de Cusco",
            "tag": "Ingresso combinado",
            "preco_val": "sem preço oficial",
            "preco_nota": "guias citam S/ 130; não inclui Machu Picchu",
            "campos": [
                ("O preço",
                 SEC +
                 "<b>o site do comitê que vende o boleto (COSITUC) estava fora do ar</b> em "
                 "29/out/2026. Guias de viagem citam <b>S/ 130</b> para o estrangeiro, no "
                 "boleto integral de 10 dias, que abre os sítios arqueológicos de Cusco e do "
                 "Vale Sagrado. <b>Não inclui Machu Picchu.</b> Não entra na conta."),
                ("Onde fica",
                 mapa("Plaza de Armas, Cusco, Peru")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem",
            "tag": "Conta, não lugar",
            "preco_val": "sem dado oficial",
            "preco_nota": "nenhum órgão publica a diária média",
            "campos": [
                ("Por que não há diária nesta ficha",
                 FLAG % "Lacuna declarada" +
                 "<b>Não achamos diária média oficial de Cusco nem de Aguas Calientes.</b> "
                 "<b>A regra desta casa é não estimar.</b> A ficha de custos mostra o total "
                 "sem a hospedagem, e diz isso no rótulo."),
            ],
        },
    ],
}

DESTINOS = [MACHU]
