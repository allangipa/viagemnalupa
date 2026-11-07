# -*- coding: utf-8 -*-
"""Ficha de custos de Florianopolis: 4 dias, 1 pessoa, real.

Mesmo molde do gramado/gera_custos.py: SEM HOSPEDAGEM, porque nenhum orgao
publica a diaria media de Florianopolis.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
Os dois barcos - o do Campeche e o da Costa da Lagoa - ficam FORA do
total: cada associacao cobra o seu, sem tabela oficial, e a casa nao
escolhe um numero. A linha diz a faixa que a imprensa publicou.

O onibus entra pelo Cartao Turista (R$ 7,20), em oito viagens - suposicao
desta ficha, dita na linha. O valor vem da imprensa: o decreto nao foi
achado no site da Prefeitura.

Uso
---
    python _build/florianopolis/gera_custos.py
    python _build/florianopolis/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_floripa_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

IMP = '<span class="flag">Tarifa oficial noticiada pela imprensa</span> '

FICHAS = {
    "florianopolis": {
        "nome": "Florianópolis", "dias": 4, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 4 dias em Florianópolis em 2026",
        "descricao": ("O custo de 4 dias em Florianópolis, por pessoa, com a taxa da Ilha "
                      "do Campeche, as fortalezas que não cobram no último domingo do mês e "
                      "o ônibus mais caro entre as capitais — sem a hospedagem, porque não "
                      "há diária oficial publicada."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas "
                     "em 7 de novembro de 2026. <b>Sem a hospedagem</b> — nenhum órgão "
                     "publica a diária média de Florianópolis, e a página explica por "
                     "quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 4 dias, 1 pessoa. Mude as datas e o "
                  "número de pessoas, desmarque o que você não vai fazer, e a conta se "
                  "refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> Nenhum órgão publica a diária média de Florianópolis, e a "
            "regra desta casa é não estimar: o total diz isso no próprio rótulo.<br>"
            "<b>Os dois barcos também ficam fora</b> — Campeche e Costa da Lagoa —, "
            "porque cada associação cobra o seu e não há tabela oficial. É por isso que "
            "o total parece baixo: a linha que mais pesa, o barco do Campeche, não "
            "entra."),
        "linhas": [
            # ---------------------------------------------------- ingressos
            ("ingresso", 15.00, "Ilha do Campeche, taxa municipal", "R$ 15,00",
             IMP + "ND Mais, 18/01/2026; o site oficial da Prefeitura só mostra o valor "
             "depois do login.<br>"
             "<b>Sem reagendamento e sem devolução, nem por mau tempo</b> — o site "
             "oficial. <b>O voucher sai 24 horas depois de o pagamento compensar.</b> "
             "Limite de 800 visitantes por dia, das 9h às 17h."),
            ("ingresso", None, "Barco até a Ilha do Campeche", "R$ 185 a R$ 250",
             IMP + "a mesma reportagem dá essa faixa por pessoa, conforme a associação e o "
             "ponto de saída. <b>Não há tabela oficial</b>, e por isso a linha está fora "
             "do total — mas é ela que mais pesa nesta viagem."),
            ("ingresso", 20.00, "Fortaleza de São José da Ponta Grossa", "R$ 20,00",
             "Fonte: Departamento das Fortalezas da UFSC, Resolução Normativa nº "
             "39/2026/CC, consultado em 7/nov/2026. Meia R$ 10.<br>"
             "<b>Grátis no último domingo de cada mês, de março a novembro.</b> Dinheiro "
             "ou PIX na portaria."),
            ("ingresso", 20.00, "Fortaleza de Santo Antônio de Ratones", "R$ 20,00",
             "Mesma fonte. <b>A portaria só aceita dinheiro</b>; pague antes, no site. "
             "<b>O barco é à parte</b>, de empresa náutica, e não está nesta linha. "
             "Anhatomirim está fechada por obra no trapiche."),
            ("ingresso", 0.00, "Praias, Ponte Hercílio Luz e Mercado Público", "grátis",
             "As praias têm acesso livre por lei — <b>Lei federal nº 7.661/1988</b>, "
             "art. 10. A ponte e o Mercado não cobram entrada."),
            ("ingresso", None, "Barco da Costa da Lagoa, ida e volta",
             "<span class=\"flag\">Fontes divergem</span>",
             "Guias de viagem citam R$ 12,50 e R$ 15 por trecho, e R$ 2,50 para o morador "
             "cadastrado. Sem tabela oficial; fora do total."),
            # ---------------------------------------------------- transporte
            ("fixo", 57.60, "Ônibus, 8 viagens no Cartão Turista", "R$ 57,60",
             IMP + "ND Mais: desde 1º/jan/2026, <b>R$ 7,20 no Cartão Turista</b>, R$ 7,70 "
             "no QR Code, R$ 6,20 no Cartão Cidadão do morador, R$ 20 nas executivas.<br>"
             "<b>Oito viagens é suposição desta ficha, não dado.</b> O Passe Rápido "
             "integra linhas por três horas. <b>O ônibus não aceita dinheiro desde "
             "5/jan/2026.</b> Quem vai de carro, desmarca."),
            # ---------------------------------------------------- taxa
            ("taxa", None, "Taxa turística", "não existe",
             "<b>Florianópolis não cobra taxa de quem se hospeda.</b> O Selo Turismo "
             "Legal, de nov/2025, é cobrado de ônibus, micro-ônibus e vans de turismo — "
             "não de quem chega de carro ou de avião. <b>Fora do total.</b>"),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, apurados em 7 de novembro de 2026. <b>Sem a "
            "hospedagem</b>, que não tem diária oficial, e <b>sem os dois barcos</b>, que "
            "não têm tabela oficial.<br>"
            "<b>Duas coisas mudam esta conta mais que qualquer corte.</b><br>"
            "<b>A primeira: o barco do Campeche</b>, de R$ 185 a R$ 250 segundo a "
            "imprensa, pesa mais que todas as outras linhas somadas — e não devolve com "
            "mar ruim.<br>"
            "<b>A segunda: o último domingo do mês</b>, de março a novembro, quando as "
            "fortalezas da UFSC não cobram."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. A regra do Campeche vem "
            "do site oficial da Prefeitura; o valor da taxa, da imprensa, porque o site "
            "só o mostra depois do login. As fortalezas vêm do Departamento das "
            "Fortalezas da UFSC. A lei das praias é federal. <b>A tarifa de ônibus vem "
            "da imprensa</b> — o decreto não foi achado no site da Prefeitura —, e está "
            "marcada. <b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("londres", "Londres"), ("florianopolis", "Florianópolis"),
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
