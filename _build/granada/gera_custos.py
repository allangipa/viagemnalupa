# -*- coding: utf-8 -*-
"""Ficha de custos de Granada: 3 dias, 1 pessoa, euro.

Mesmo molde do sevilha/gera_custos.py, que e a outra ficha andaluza.

O QUE ESTA FICHA TEM DE DIFERENTE DE TODAS AS OUTRAS
-----------------------------------------------------
E a primeira em que a linha mais cara do site NAO TEM VALOR FINAL
PUBLICADO. A Alhambra tem preco em lei (21 EUR, Orden de 17 de julio de
2025) e outro preco no proprio site do monumento (22,27 EUR), e o site
ainda avisa que a comissao se soma a esse segundo numero. O caixa esta
atras de verificacao anti-bot e nao abriu.

A tabela usa 22,27 e diz que e PISO, nao total. Preferimos o numero maior
dos dois publicados, porque errar para cima nao estraga viagem de
ninguem - errar para baixo, sim.

A SEGUNDA DIFERENCA: DOIS DIAS DA SEMANA MUDAM A CONTA
-------------------------------------------------------
Granada tem gratuidade em dois dias diferentes, e nenhum guia junta os
dois:

    QUARTA a tarde   Catedral e Capilla Real, de graca, por reserva
                     nominativa no site da diocese (17 EUR de economia)
    DOMINGO          monumentos andalusies, de graca, sem reserva

Quem encaixa quarta e domingo na mesma viagem tira 19 EUR da conta - mais
de um quarto do total sem hospedagem. O roteiro usa isso.

A TERCEIRA: O TRANSPORTE ESTA EM PROMOCAO QUE VENCE
----------------------------------------------------
A tabela do Consorcio de Transportes publicada em 30/set/2026 esta sob o
titulo "Tarifas temporales a partir del 1 de julio al 31 de diciembre de
2026 (40% descuento)". O onibus do aeroporto a 3,10 EUR e preco
promocional COM PRAZO. Depois de 31 de dezembro de 2026 ele sobe, e a
tabela nao diz para quanto. Isso esta dito na linha.

O onibus urbano e outra coisa: tarifa do MUNICIPIO, 1,60 EUR desde 1 de
outubro de 2024, sem prazo de validade anunciado.

Uso
---
    python _build/granada/gera_custos.py
    python _build/granada/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_granada_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

APURADO = "30 de setembro de 2026"

# Serie do INE, tabela 46298, "Granada. Tarifa media diaria (ADR)".
# Guardada aqui inteira para a media ser conferivel sem sair do arquivo.
ADR = {
    "set/2025": 100.39, "out/2025": 122.46, "nov/2025": 88.11,
    "dez/2025": 96.66, "jan/2026": 92.66, "fev/2026": 87.94,
    "mar/2026": 91.50, "abr/2026": 107.98, "mai/2026": 110.48,
    "jun/2026": 90.20, "jul/2026": 79.56, "ago/2026": 73.07,
}
MEDIA = round(sum(ADR.values()) / len(ADR), 2)      # 95.08
assert len(ADR) == 12, "a media diz 12 meses; confira a serie"
assert min(ADR, key=ADR.get) == "ago/2026", "agosto deixou de ser o mais barato"
assert max(ADR, key=ADR.get) == "out/2025", "outubro deixou de ser o mais caro"

FICHAS = {
    "granada": {
        "nome": "Granada", "dias": 3, "moeda": "€", "dec": 2,
        "titulo": "Quanto custa 3 dias em Granada em 2026",
        "descricao": ("O custo de 3 dias em Granada, por pessoa, com a Alhambra que tem "
                      "dois preços oficiais e os dois dias da semana em que se entra de "
                      "graça."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas "
                     "em fonte oficial em 30 de setembro de 2026. <b>Com hospedagem</b> "
                     "— e com a diária aberta em três épocas, porque em Granada o mês "
                     "mais barato do ano é agosto, e isso é o contrário do que todo "
                     "mundo supõe."),
        "hosp": [
            {"k": "media", "rot": "Média dos 12 meses (cálculo nosso, INE)",
             "ref": MEDIA, "mn": MEDIA, "mx": MEDIA},
            {"k": "baixa", "rot": "Agosto — o mês mais barato do ano (INE)",
             "ref": ADR["ago/2026"], "mn": ADR["ago/2026"], "mx": ADR["ago/2026"]},
            {"k": "alta", "rot": "Outubro — o mês mais caro do ano (INE)",
             "ref": ADR["out/2025"], "mn": ADR["out/2025"], "mx": ADR["out/2025"]},
        ],
        "hospPadrao": "media",
        "intro": ("A tabela abaixo é a nossa apuração: 3 dias, 1 pessoa, valores em "
                  "euro. Mude as datas e o número de pessoas, troque a época da "
                  "hospedagem, desmarque o que você não vai fazer, e a conta se refaz "
                  "na hora."),
        "nota_calc": (
            "As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
            "quarto. <b style=\"color:var(--gelo)\">A diária vem do INE espanhol, aberta "
            "por ponto turístico</b> — Granada é um deles —, e por isso esta ficha tem "
            "hospedagem.<br>"
            "<b>O seletor de três épocas é o que mais muda a conta nesta cidade.</b> "
            "A diária oficial de outubro é <b>68% maior</b> que a de agosto, pelo mesmo "
            "quarto. Granada é Andaluzia de dentro, não costa: em agosto faz calor "
            "demais, a cidade esvazia e o preço cai. "
            "Linhas marcadas como não apuradas continuam fora do total."),
        "linhas": [
            # ---------------------------------------------------- ingressos
            ("ingresso", 22.27, "Alhambra, visita diurna geral", "€ 22,27",
             "Fontes: <b>Orden de 17 de julio de 2025</b> (BOJA nº 142 de 25/jul/2025) "
             "e a página de horários e tarifas do site oficial "
             "(alhambra-patronato.es), consultadas em 30/set/2026.<br>"
             "<span class=\"flag\">Há dois preços oficiais, e nenhum é o final</span> "
             "<b>a lei fixa € 21. O site do próprio monumento publica € 22,27</b> — "
             "6,05% acima. E a mesma página diz: <i>“A estos precios hay que añadir la "
             "comisión de servicio (para compras en la página web)”</i>, ou seja, a "
             "comissão se soma <b>aos € 22,27</b>.<br>"
             "Ainda há o artigo 1.2 da ordem, que manda somar IVA, e o artigo 2, que "
             "manda somar a comissão de gestão na venda antecipada.<br>"
             "<b>Esta tabela usa € 22,27 como piso</b>, que é o maior dos dois números "
             "publicados. <b>Não é o total.</b><br>"
             "<b>O caixa oficial não abriu para conferência:</b> "
             "tickets.alhambra-patronato.es responde com verificação anti-bot, e não "
             "contornamos esse tipo de proteção."),
            ("ingresso", 12.73, "Alhambra, visita noturna aos Palacios Nazaríes", "€ 12,73",
             "Mesmas fontes, mesma data. <b>A lei fixa € 12; o site publica € 12,73.</b><br>"
             "<b>Esta linha é um acréscimo, e repete o espaço:</b> a visita noturna "
             "entra nos mesmos Palacios Nazaríes da visita diurna. Quem vai fazer só "
             "uma das duas <b>desmarca esta</b> e a conta se refaz.<br>"
             "<b>Ela está aqui porque é barata e porque o calendário decide.</b> "
             "De 15 de outubro a 31 de março só roda <b>sexta e sábado</b>; de 1º de "
             "abril a 14 de outubro, <b>de terça a sábado</b>. Quem vai no inverno e "
             "não cai numa sexta ou num sábado não tem essa opção, por preço nenhum."),
            ("ingresso", 10.00, "Catedral de Granada", "€ 10,00",
             "Fonte: <b>ticketsgranadacristiana.com</b>, o canal oficial de venda que "
             "o próprio site da catedral indica, consultado em 30/set/2026.<br>"
             "<span class=\"flag\">O site da catedral não publica tabela</span> "
             "catedraldegranada.com diz apenas <i>“Ahora puede comprar online su "
             "ticket”</i> e manda para o site de venda. O número é oficial, mas não "
             "está na página da catedral.<br>"
             "<b>Há como não pagar esta linha.</b> A catedral tem visita gratuita por "
             "reserva nominativa em <b>entradasgratuitas.diocesisgranada.es</b>, em "
             "<b>quartas-feiras à tarde</b> — as sessões são 15h15, 15h30, 16h e 16h30, "
             "e as datas abertas na nossa consulta eram 2, 9 e 16 de dezembro de 2026. "
             "Duas entradas por pessoa, reserva até 24 horas antes, documento na "
             "entrada, proibido fotografar."),
            ("ingresso", 7.00, "Capilla Real", "€ 7,00",
             "Mesma fonte e mesma data: o canal oficial de venda indicado pelo site da "
             "Capilla Real, que também <b>não publica os valores</b>.<br>"
             "São os túmulos de Isabel e Fernando, os Reis Católicos. Fica colada à "
             "catedral e é <b>bilhete separado</b>.<br>"
             "<b>Tem a mesma quarta-feira gratuita</b>, no mesmo site da diocese, com "
             "sessões diferentes: <b>15h15, 15h30, 16h30 e 17h</b>. <b>Dá para fazer as "
             "duas na mesma quarta</b> — mas são duas reservas separadas.<br>"
             "<span class=\"flag\">O horário normal não está publicado</span> "
             "o próprio site pede, em caixa alta, <i>“ROGAMOS QUE CONFIRMEN HORARIOS "
             "PREVIAMENTE A LA VISITA”</i>, pelo telefone 958 22 78 48."),
            ("ingresso", 6.00, "Museo Cuevas del Sacromonte", "€ 6,00",
             "Fonte: <b>caixa oficial</b> (shop.sacromontegranada.com), consultado em "
             "30/set/2026 — o resumo de compra diz <b>“Visita diurna Museo — 6,00 €”</b>.<br>"
             "<b>O € 5 que circula na internet está errado</b>, e vem de resenhas de "
             "visitantes hospedadas na própria página do museu. Número de resenha não é "
             "número apurado.<br>"
             "Inclui as 11 cavernas originais, o jardim botânico, o mirador e audioguia. "
             "<b>Menor de 10 anos não paga.</b><br>"
             "<b>Não confunda com a Abadía del Sacromonte</b>, que é outro lugar, mais "
             "acima no morro, e custa <b>€ 7,00</b> no circuito das igrejas.<br>"
             "E o caixa avisa: <i>“No se admiten cambios o devoluciones.”</i>"),
            ("ingresso", 2.00, "Monumentos andalusíes, um deles", "€ 2,00",
             "Fonte: <b>Orden de 17 de julio de 2025</b>, que é explícita: "
             "<i>“Visita de cada monumento de forma individual (Corral del Carbón "
             "gratuito): 2 €.”</i><br>"
             "São o <b>Bañuelo</b>, banhos árabes do século XI, a <b>Casa Morisca del "
             "Horno de Oro</b>, o <b>Palacio de Dar al-Horra</b> e o <b>Maristán</b>. "
             "Cada um custa € 2 — a linha conta <b>um</b>.<br>"
             "<b>E no domingo não custa nada.</b> A página oficial diz, em caixa alta: "
             "<b>“LA ENTRADA EN DOMINGO ES GRATUITA”</b> — o domingo inteiro, para "
             "todos, sem reserva e sem comprovação de residência."),
            ("ingresso", 0.00, "Museo de la Alhambra", "grátis",
             "<b>Há um museu dentro do recinto da Alhambra em que se entra sem comprar "
             "o ingresso do monumento — e isso está em norma legal.</b><br>"
             "O <b>artigo 9.1</b> da Orden de 17 de julio de 2025: <i>“Todos los "
             "visitantes podrán acceder gratuitamente durante el horario de apertura al "
             "Museo de la Alhambra y al monumento El Corral del Carbón.”</i> A página do "
             "museu confirma: <b>“ENTRADA LIBRE”</b>.<br>"
             "Fica dentro do <b>Palacio de Carlos V</b>, o palácio renascentista de "
             "pátio circular, no meio da Alhambra.<br>"
             "<b>Não é “a Alhambra de graça”:</b> não dá os Palacios Nazaríes, nem a "
             "Alcazaba, nem o Generalife. Mas resolve o dia de quem não conseguiu "
             "ingresso — e isso acontece, porque os palácios vendem 300 vagas a cada "
             "meia hora.<br>"
             "<b>Fecha às segundas</b>, e domingo e terça fecham às 14h30."),
            ("ingresso", 0.00, "Miradouros: San Nicolás, Silla del Moro, Torres Bermejas",
             "grátis",
             "<b>O Mirador de San Nicolás não tem bilheteria, horário nem ingresso.</b> "
             "É praça pública no Albaicín, e é de lá a vista mais fotografada da "
             "cidade.<br>"
             "<b>O que cobra ali é outra coisa:</b> a Iglesia y torre de San Nicolás, a "
             "poucos metros, custa <b>€ 3,00</b>. Quem quer só a vista não paga nada.<br>"
             "<b>Silla del Moro e Torres Bermejas</b> são da própria Alhambra e a página "
             "oficial marca os dois como <b>“VISITA GRATUITA”</b>.<br>"
             "<b>Mas só abrem sábado e domingo</b> — e com regras de domingo diferentes "
             "entre si: a Silla del Moro fecha às <b>14h</b> no domingo, e as Torres "
             "Bermejas seguem até <b>20h</b> no verão, igual ao sábado. São dois "
             "lugares do mesmo órgão, a 20 minutos de caminhada um do outro."),
            # ---------------------------------------------------- transporte
            ("fixo", 6.20, "Ônibus do aeroporto, ida e volta", "€ 6,20",
             "Fonte: tabela de tarifas do <b>Consorcio de Transporte Metropolitano del "
             "Área de Granada</b> (siu.ctagr.es), órgão da Junta de Andalucía, "
             "consultada em 30/set/2026: <b>Servicio Granada–Aeropuerto (Línea 245), "
             "billete sencillo € 3,10</b>. A linha conta ida e volta.<br>"
             "<span class=\"flag\">Este preço tem prazo de validade</span> "
             "a tabela está publicada sob o título <i>“Tarifas temporales a partir del "
             "1 de julio al 31 de diciembre de 2026 (40% descuento)”</i>. "
             "<b>São € 3,10 porque há um desconto de 40% que vence em 31 de dezembro de "
             "2026</b> — e a tabela <b>não diz para quanto volta</b> depois disso. "
             "Se a sua viagem for em 2027, trate esta linha como piso.<br>"
             "Com a tarjeta do Consorcio a mesma viagem sai por <b>€ 1,62</b>, mas a "
             "tarjeta custa <b>€ 1,50</b> de emissão, não reembolsável."),
            ("fixo", 9.60, "Ônibus urbano, 6 viagens", "€ 9,60",
             "Fonte: <b>Área de Movilidad do Ayuntamiento de Granada</b> "
             "(movilidadgranada.com), consultada em 30/set/2026: <b>billete ordinario "
             "€ 1,60</b>, IVA de 10% incluído, em vigor desde <b>1º de outubro de "
             "2024</b> pela Resolución de 23 de septiembre de 2024.<br>"
             "<b>Esta tarifa é do município e não está no desconto temporário do "
             "Consorcio</b> — são dois sistemas diferentes, com duas tabelas "
             "diferentes.<br>"
             "<b>O transbordo é grátis por 60 minutos</b>, entre linhas diferentes, "
             "tanto no bilhete simples quanto no bonobus. Isso importa em Granada: os "
             "micro-ônibus que sobem à Alhambra e ao Albaicín conectam com as linhas do "
             "centro, e <b>uma passagem cobre a subida mais a conexão</b>.<br>"
             "<b>Seis viagens é suposição desta ficha, não dado.</b> O centro se faz a "
             "pé; a subida à Alhambra e ao Mirador de San Nicolás é que cansa. "
             "<b>Quem andar só a pé desmarca.</b><br>"
             "O ônibus noturno custa <b>€ 1,70</b>."),
            # ---------------------------------------------------- a taxa que nao ha
            ("taxa", None, "Taxa turística municipal", "não existe",
             "<b>Não há taxa turística na Andaluzia em 2026</b>, e portanto não há em "
             "Granada.<br>"
             "É o mesmo achado que a ficha de Sevilha registra: <b>a criação depende da "
             "Junta de Andalucía</b>, que não aprovou, e sem a Junta o município não "
             "pode instituí-la.<br>"
             "Se o seu hotel em Granada cobrar algo chamado de taxa turística, "
             "<b>confira o que está sendo cobrado</b> — municipal não é. "
             "<b>Fora do total, porque não há valor.</b>"),
            # ---------------------------------------------------- hospedagem
            ("hosp", None, "Hospedagem, 2 noites", "€ 190,16",
             "Fonte: <b>INE</b> (Instituto Nacional de Estadística de Espanha), "
             "<i>Indicadores de Rentabilidad del Sector Hotelero</i>, tabela 46298 — "
             "tarifa média diária (ADR) por <b>ponto turístico</b>, série "
             "<i>Granada, total de categorias</i>, consultada em 30/set/2026.<br>"
             "<b>O valor mostrado usa a média dos 12 meses de set/2025 a ago/2026: "
             "€ 95,08 por quarto por noite.</b> Os doze valores são do INE; "
             "<b>a média é cálculo nosso</b>, e está rotulada como tal no seletor.<br>"
             "<b>O achado desta página é o mês ao contrário:</b> <b>€ 73,07 em agosto</b> "
             "contra <b>€ 122,46 em outubro</b> — <b>68% mais caro</b> pelo mesmo "
             "quarto. <b>Agosto é o mês mais barato do ano em Granada</b>, o que é o "
             "inverso do que se espera de um destino europeu.<br>"
             "<b>A explicação é o calor.</b> No mesmo agosto de 2026 o INE registra "
             "<b>€ 163,05 em Málaga</b>, a 130 quilômetros, na costa — <b>2,2 vezes "
             "Granada</b> —, e a média nacional espanhola é <b>€ 166,90</b>. Córdoba "
             "(€ 62,06) e Sevilha (€ 87,39) fazem o mesmo movimento. Não é Granada: é a "
             "Andaluzia de dentro.<br>"
             "Troque a época no seletor acima e veja a conta mudar.<br>"
             "ADR é por <b>quarto ocupado</b>, não por pessoa, e cobre <b>hotéis</b>, "
             "não apartamentos. A conta divide por duas pessoas por quarto, como nas "
             "outras fichas."),
        ],
        "rodape_tabela": (
            "Valores em euro, por pessoa, apurados em fonte oficial em 30 de setembro "
            "de 2026. <b>Uma linha está fora do total</b> — a taxa turística, porque "
            "ela não existe — e está marcada na tabela.<br>"
            "<b>Duas advertências que valem mais que qualquer corte de visita.</b><br>"
            "<b>A primeira: a Alhambra não tem preço final publicado.</b> A lei diz "
            "€ 21, o site do monumento diz € 22,27, e o site avisa que a comissão ainda "
            "se soma. Usamos o maior dos dois como piso.<br>"
            "<b>A segunda: dois dias da semana tiram € 19 desta conta.</b> "
            "<b>Quarta-feira à tarde</b>, Catedral e Capilla Real são gratuitas por "
            "reserva — € 17. <b>Domingo</b>, os monumentos andalusíes são gratuitos — "
            "€ 2. <b>Encaixar uma quarta e um domingo na mesma viagem corta mais de um "
            "quarto do que não é hospedagem.</b>"),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. Os preços da Alhambra "
            "vêm da <b>Orden de 17 de julio de 2025</b>, publicada no BOJA, e da página "
            "oficial do Patronato — <b>e os dois discordam</b>, o que está dito na "
            "linha. Catedral, Capilla Real e Sacromonte vêm dos canais oficiais de "
            "venda que os próprios monumentos indicam, porque nenhum deles publica "
            "tabela na sua página. O transporte vem de duas fontes distintas: o "
            "Consorcio de Transporte Metropolitano, para o aeroporto, e o Ayuntamiento "
            "de Granada, para o ônibus urbano. A hospedagem vem dos Indicadores de "
            "Rentabilidad del Sector Hotelero do INE espanhol. "
            "<b>Nenhum valor veio de agregador de viagem</b> — e um número que circula "
            "muito, os € 5 do Museo Cuevas del Sacromonte, foi desmentido pelo caixa do "
            "próprio museu, que cobra € 6."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"),
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
