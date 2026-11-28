# -*- coding: utf-8 -*-
"""Ficha de custos de Toquio: 5 dias, 1 pessoa, real.

Mesmo molde do machu-picchu/gera_custos.py, e SEM HOSPEDAGEM.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
Linhas em iene numa ficha em real, pela taxa de venda do boletim de
fechamento do BCB de 23/10/2026 (JPY 0,03211), o mesmo arquivo do /comparar/:

    ¥ 1.800 x 0,03211 = 57,80     Tokyo Skytree, Tembo Deck
    ¥ 1.000 x 0,03211 = 32,11     Museu Nacional
    ¥ 2.000 x 0,03211 = 64,22     Tokyo Subway Ticket de 72 horas

A taxa de saida (¥ 3.000) fica FORA: vem embutida na passagem, que a ficha
nao inclui. A taxa de hospedagem fica fora porque depende da diaria.

O iene nao entrou como moeda do site (schema/ofertas.py, recortes/comparar.py
e layout/faq.py nao o conhecem): a ficha e em real, como a de Machu Picchu.

Uso
---
    python _build/toquio/gera_custos.py
    python _build/toquio/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_toquio_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

JPY_VENDA = 0.03211             # BCB, boletim de fechamento de 23/10/2026
SKY, MUSEU, METRO = (round(v * JPY_VENDA, 2) for v in (1800, 1000, 2000))
assert (SKY, MUSEU, METRO) == (57.80, 32.11, 64.22), (SKY, MUSEU, METRO)

SEC = '<span class="flag">Só em fonte secundária</span> '

FICHAS = {
    "toquio": {
        "nome": "Tóquio", "dias": 5, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 5 dias em Tóquio em 2026",
        "descricao": ("O custo de 5 dias em Tóquio, por pessoa, em real: o Skytree, o Museu "
                      "Nacional e o passe de metrô de 72 horas, mais as taxas que mudaram em "
                      "2026. Sem a hospedagem, porque não há diária oficial."),
        "abertura": ("A conta do que foi apurado, por pessoa, conferida em 27 de novembro de "
                     "2026. Os preços são em iene, convertidos pela taxa de venda do Banco "
                     "Central de 23 de outubro. <b>Sem a hospedagem</b>, que não tem diária "
                     "oficial, e <b>sem a taxa de saída</b>, que vem na passagem."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em real. "
                  "Mude as datas e o número de pessoas, desmarque o que você não vai fazer, "
                  "e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> Não achamos diária média oficial de Tóquio, e a regra desta casa "
            "é não estimar.<br>"
            "<b>Os preços são em iene</b>, convertidos pela taxa de venda do boletim de "
            "fechamento do Banco Central de 23/out/2026 (¥ 1 = R$ 0,03211). <b>A taxa de "
            "saída do Japão, ¥ 3.000, vem na passagem</b> e fica fora da soma."),
        "linhas": [
            ("ingresso", SKY, "Tokyo Skytree, Tembo Deck", "¥ 1.800 · R$ 57,80",
             "Fonte: página oficial de ingressos, consultada em 27/nov/2026: <b>a partir de "
             "¥ 1.800</b> o adulto; combo dos andares 350 e 450 a partir de ¥ 3.000. Até 5 anos "
             "não paga.<br>"
             "<span class=\"flag\">É piso</span> o preço muda com a data. <b>No balcão, "
             "¥ 500 a mais por ingresso.</b>"),
            ("ingresso", MUSEU, "Museu Nacional de Tóquio", "¥ 1.000 · R$ 32,11",
             "Fonte: página de visitação do site oficial, consultada em 27/nov/2026. "
             "Universitário: ¥ 500. <b>Fecha na segunda e de 26 a 31/12/2026.</b> Três dias "
             "grátis em 2026: 19/5, 21/9 e 3/11."),
            ("fixo", METRO, "Tokyo Subway Ticket, 72 horas", "¥ 2.000 · R$ 64,22",
             "Fonte: Governo Metropolitano de Tóquio, comunicado de 30/jan/2026. <b>Desde "
             "14/3/2026</b>: 24 h ¥ 1.000, 48 h ¥ 1.500, 72 h ¥ 2.000 — antes, ¥ 800, ¥ 1.200 "
             "e ¥ 1.500. Criança paga metade."),
            ("fixo", None, "Taxa de saída do Japão", "¥ 3.000 (na passagem)",
             "Fonte: JNTO, consultada em 27/nov/2026: <b>de ¥ 1.000 para ¥ 3.000 em "
             "1º/7/2026</b>, cerca de R$ 96,33. Vem embutida na passagem, que esta ficha não "
             "inclui. <b>Fora do total.</b>"),
            ("taxa", None, "Taxa de hospedagem de Tóquio", "¥ 100 ou ¥ 200 por noite",
             "Fonte: Governo Metropolitano de Tóquio. Isenta abaixo de ¥ 10.000 de diária por "
             "pessoa; ¥ 100 até ¥ 15.000; ¥ 200 acima. <b>Vira 3% da diária em abril de "
             "2027</b>, segundo a proposta oficial e a imprensa. Depende da diária: <b>fora do "
             "total.</b>"),
            ("ingresso", None, "Tax-free nas compras", "reembolso na saída",
             SEC + "desde 1º/11/2026 o turista paga com imposto e recebe o reembolso ao sair "
             "do Japão, com mínimo de ¥ 5.000 por loja e por dia. Não é custo: <b>fora do "
             "total.</b>"),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, conferidos em 27 de novembro de 2026, com o iene "
            "pela taxa de venda do Banco Central de 23 de outubro. <b>Sem a hospedagem</b>, "
            "que não tem diária oficial, e <b>sem a taxa de saída</b>, que vem na "
            "passagem.<br>"
            "<b>Guia de antes de 2026 erra três números</b>: o passe de metrô, a taxa de "
            "saída e a forma do tax-free."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo: a página oficial do Tokyo "
            "Skytree, a do Museu Nacional de Tóquio, o comunicado do Governo Metropolitano "
            "sobre o passe de metrô, a JNTO para a taxa de saída e o documento do Governo "
            "Metropolitano sobre a taxa de hospedagem. O câmbio é o do boletim de fechamento "
            "do Banco Central do Brasil. <b>O tax-free vem só de imprensa e guias</b>, "
            "marcado. As páginas lidas estão guardadas com data."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("londres", "Londres"), ("florianopolis", "Florianópolis"),
    ("sao-paulo", "São Paulo"), ("aruba", "Aruba"),
    ("porto-de-galinhas", "Porto de Galinhas"), ("toquio", "Tóquio"),
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
