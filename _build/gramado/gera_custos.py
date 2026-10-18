# -*- coding: utf-8 -*-
"""Ficha de custos de Gramado: 4 dias, 1 pessoa, real.

Mesmo molde do barcelona/gera_custos.py, mas SEM HOSPEDAGEM, como a de
Fortaleza: nenhum orgao publica diaria media de Gramado, e a casa nao
estima. O total diz isso no proprio rotulo.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
O Parque do Caracol cobra R$ 134,90 de quem nao e do RS e R$ 67,00 de
gaucho. A linha usa o preco de quem vem de fora - e o leitor do site, em
regra, vem de fora - e diz o outro.

A taxa de turismo foi revogada pela Camara em abril de 2026; a linha de
taxa existe para dizer isso e para dizer que a Room Tax que sobrou e
voluntaria. Fora do total.

O Natal Luz entra com o Grande Desfile (R$ 420 a inteira), que so existe
de 22/out a 17/jan e so em algumas noites. Quem vai fora da temporada
desmarca.

Uso
---
    python _build/gramado/gera_custos.py
    python _build/gramado/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_gramado_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "gramado": {
        "nome": "Gramado", "dias": 4, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 4 dias em Gramado em 2026",
        "descricao": ("O custo de 4 dias em Gramado e Canela, por pessoa, com o Caracol "
                      "que cobra o dobro de quem não é gaúcho, o Natal Luz e a taxa de "
                      "turismo que foi revogada — sem a hospedagem, porque não há diária "
                      "oficial publicada."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas "
                     "nas páginas oficiais em 18 de outubro de 2026. <b>Sem a "
                     "hospedagem</b> — nenhum órgão publica a diária média de Gramado, e "
                     "a página explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 4 dias, 1 pessoa, valores em "
                  "real. Mude as datas e o número de pessoas, desmarque o que você não "
                  "vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> Nenhum órgão publica a diária média de Gramado — o Panorama "
            "da Hotelaria Brasileira cobre capitais, e Gramado não é uma. Como a regra "
            "desta casa é não estimar, a hospedagem ficou de fora e o total diz isso no "
            "próprio rótulo.<br>"
            "<b>Cinco linhas são piso</b>, porque o preço muda com a data ou a página diz "
            "“a partir de”: Snowland, Dreamland, Mundo a Vapor, o Bustour e o Grande "
            "Desfile do Natal Luz."),
        "linhas": [
            # ---------------------------------------------------- ingressos
            ("ingresso", 134.90, "Parque do Caracol, para quem não é do RS", "R$ 134,90",
             "Fonte: página de compra oficial (parquecaracol.com.br), consultada em "
             "18/out/2026, aba “Brasileiros e Estrangeiros”.<br>"
             "<span class=\"flag\">O mesmo bilhete custa metade para gaúcho</span> "
             "na aba “Gaúchos e Residentes do RS”, o Bilhete Gaúcho sai a partir de "
             "<b>R$ 67,00</b>. <b>Morador de Canela e Gramado não paga.</b> Se você é do "
             "RS, troque mentalmente esta linha por R$ 67.<br>"
             "Meia de 4 a 12 anos e acima de 60: R$ 67,00. Corajoso e Ousado são à parte."),
            ("ingresso", 144.50, "Snowland, média temporada", "desde R$ 144,50",
             "Fonte: loja oficial (ingressos.snowland.com.br), consultada em 18/out/2026 "
             "para 22/out/2026, quinta, <b>média temporada</b>. Inclui o kit de roupas.<br>"
             "<span class=\"flag\">É piso</span> o preço muda em quatro temporadas e só "
             "lemos uma. Meia e morador da serra: R$ 86,70. Menor de 4 não paga.<br>"
             "<b>No calendário de outubro, toda quarta aparece como “Parque Fechado”.</b>"),
            ("ingresso", 156.00, "Mini Mundo", "R$ 156,00",
             "Fonte: loja oficial (ingressos.minimundo.com.br), consultada em "
             "18/out/2026. <b>Meia de 3 a 15 anos e acima de 60: R$ 78,00.</b> Todos os "
             "dias, 9h às 17h."),
            ("ingresso", 115.00, "GramadoZoo", "R$ 115,00",
             "Fonte: página de funcionamento do site oficial, consultada em 18/out/2026: "
             "<i>“Ingresso único com valor de R$ 115,00”</i>. Menor de 3 não paga. "
             "<b>Estacionamento R$ 20,00</b>, fora desta linha. Chuva forte pode fechar o "
             "parque sem aviso."),
            ("ingresso", 89.99, "Dreamland Museu de Cera", "desde R$ 89,99",
             "Fonte: página de ingressos do site oficial (dreamland.com.br), consultada em "
             "18/out/2026: <i>“A partir de R$ 89,99”</i>.<br>"
             "<span class=\"flag\">É piso</span> a página não publica meia nem a tabela. "
             "O passaporte com mais seis atrações sai a partir de R$ 219,99 — "
             "compensa a partir da terceira."),
            ("ingresso", 149.00, "Mundo a Vapor (Canela), passaporte", "R$ 149,00",
             "Fonte: site oficial (mundoavapor.com.br), consultado em 18/out/2026.<br>"
             "<span class=\"flag\">Dois números na mesma página</span> o cartão do "
             "passaporte adulto mostra <b>R$ 129,00 e R$ 149,00</b> sem dizer qual vale. "
             "<b>Usamos o maior.</b> Especial (4 a 12 anos, estudante, sênior): R$ 89 ou "
             "R$ 109. <b>Fecha às quartas.</b>"),
            ("ingresso", 420.00, "Natal Luz: O Grande Desfile de Natal", "R$ 420,00",
             "Fonte: site oficial do 41º Natal Luz (natalluzdegramado.com.br), consultado "
             "em 18/out/2026. <b>Inteira R$ 420</b>; meia a partir de R$ 210. No lote "
             "atual, que acaba em 21 de outubro, R$ 399.<br>"
             "<b>Só existe de 22/out/2026 a 17/jan/2027, e não todas as noites.</b> Quem "
             "vai fora da temporada desmarca. O Nativitaten custa R$ 360; os shows do "
             "Palácio dos Festivais, R$ 120 cada. <b>Cinco atrações do Natal Luz são "
             "gratuitas</b> — veja o guia."),
            ("ingresso", 0.00, "Lago Negro, Rua Coberta e os atrativos gratuitos", "grátis",
             "Fonte: <b>Secretaria de Turismo de Gramado</b>, seção <i>Atrativos "
             "gratuitos</i> do portal oficial, consultada em 18/out/2026: Lago Negro "
             "com <i>“Acesso livre”</i>, aberto 24h, e Rua Coberta com acesso e horário "
             "livres. <b>O pedalinho do Lago Negro cobra e o valor não está "
             "publicado.</b>"),
            # ---------------------------------------------------- transporte
            ("fixo", 124.00, "Ônibus Porto Alegre–Gramado, ida e volta", "R$ 124,00",
             "Fonte: venda oficial da <b>Citral</b> (citral.passagensweb.com.br), "
             "consultada em 18/out/2026: <b>semi-direto R$ 62,00</b>, 2h45; comum "
             "R$ 62,85, 3h15; <b>executivo R$ 84,85</b>, 2h30. Sete saídas da rodoviária "
             "de Porto Alegre no domingo consultado. A linha conta ida e volta no "
             "semi-direto.<br>"
             "Gramado não tem aeroporto comercial: <b>o voo é para Porto Alegre</b>, a "
             "cerca de 120 km."),
            ("fixo", 78.00, "Bustour, 1 dia", "desde R$ 78,00",
             "Fonte: loja oficial (bustour.com.br), consultada em 18/out/2026: "
             "<i>“A partir de R$ 78 por pessoa”</i> no ticket de um dia, embarque livre "
             "nas paradas de Gramado e Canela.<br>"
             "<span class=\"flag\">É piso</span> é o menor preço do seletor, que separa "
             "por idade. Inclui monitor; não inclui os ingressos das atrações. Quem vai "
             "de carro, desmarca."),
            # ---------------------------------------------------- taxa
            ("taxa", None, "Taxa de Turismo Sustentável", "revogada",
             "A taxa municipal de <b>R$ 3,43 por dia e por apartamento</b> (Lei "
             "3.461/2015) teve a revogação <b>aprovada pela Câmara em 13/abr/2026</b>, "
             "após acordo com o Ministério Público do RS. Fonte: ABC Mais, 17/abr/2026. "
             "<span class=\"flag\">Só em fonte secundária</span> não achamos a sanção "
             "publicada.<br>"
             "<b>No lugar, o Convention Bureau anunciou uma Room Tax do mesmo valor — "
             "voluntária.</b> Se aparecer no check-out, você pode recusar. "
             "<b>Fora do total.</b>"),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, apurados nas páginas oficiais em 18 de outubro "
            "de 2026. <b>Sem a hospedagem</b>, que não tem diária oficial publicada, e "
            "<b>sem a taxa de turismo</b>, que foi revogada.<br>"
            "<b>Duas coisas mudam esta conta mais que qualquer corte.</b><br>"
            "<b>A primeira: ser ou não gaúcho.</b> O Parque do Caracol cobra R$ 134,90 de "
            "quem é de fora do RS e R$ 67,00 de quem é de dentro; a Snowland dá preço de "
            "morador a quinze municípios da serra.<br>"
            "<b>A segunda: a época.</b> O Grande Desfile do Natal Luz, a linha mais cara, "
            "só existe de 22 de outubro a 17 de janeiro — e a Snowland muda de preço em "
            "quatro temporadas."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. Os ingressos vêm das "
            "lojas e páginas oficiais de cada parque — Parque do Caracol, Snowland, Mini "
            "Mundo, GramadoZoo, Dreamland, Mundo a Vapor — e do site oficial do Natal "
            "Luz. Os gratuitos vêm da Secretaria de Turismo de Gramado. O ônibus vem da "
            "venda oficial da Citral; o Bustour, da loja da operadora. A revogação da "
            "taxa vem da imprensa local, porque o portal de leis do município não abriu. "
            "<b>Nenhum valor veio de agregador de viagem.</b> O site do Le Jardin, o "
            "parque de lavanda, recusou a conexão, e ficou de fora."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"),
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
