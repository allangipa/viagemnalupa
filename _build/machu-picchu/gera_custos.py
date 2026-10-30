# -*- coding: utf-8 -*-
"""Ficha de custos de Machu Picchu: 4 dias, 1 pessoa, real.

Mesmo molde do bonito/gera_custos.py, e SEM HOSPEDAGEM.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
Duas linhas em sol peruano numa ficha em real, convertidas pela taxa de
venda do boletim de fechamento do BCB de 23/10/2026 (PEN 1,4613), o mesmo
arquivo do /comparar/:

    S/ 152 x 1,4613 = 222,12      bilhete de estrangeiro
    S/  11 x 1,4613 =  16,07      taxa do SERNANP

As duas entram no total marcadas como "tarifa oficial noticiada pela
imprensa": a tabela oficial fica atras de um "no soy un robot". Onibus,
Boleto Turistico e trem ficam fora, com o valor dos guias marcado.
Decisao do Allan em 29/10/2026.

Uso
---
    python _build/machu-picchu/gera_custos.py
    python _build/machu-picchu/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_machu_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

PEN_VENDA = 1.4613              # BCB, boletim de fechamento de 23/10/2026
BOLETO = round(152 * PEN_VENDA, 2)
SERNANP = round(11 * PEN_VENDA, 2)
assert (BOLETO, SERNANP) == (222.12, 16.07), (BOLETO, SERNANP)

IMP = '<span class="flag">Tarifa oficial noticiada pela imprensa</span> '
SEC = '<span class="flag">Só em fonte secundária</span> '

FICHAS = {
    "machu-picchu": {
        "nome": "Machu Picchu", "dias": 4, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 4 dias em Machu Picchu e Cusco em 2026",
        "descricao": ("O custo de 4 dias em Machu Picchu e Cusco, por pessoa: a entrada de "
                      "estrangeiro e a taxa do SERNANP em real, com o trem, o ônibus e o "
                      "Boleto Turístico pelo valor dos guias, marcados e fora do total."),
        "abertura": ("A conta do que tem tarifa oficial, por pessoa, conferida em 29 de "
                     "outubro de 2026. <b>A entrada e a taxa ambiental vêm da imprensa "
                     "peruana</b>, que reproduz a tarifa do governo — a tabela oficial fica "
                     "atrás de uma verificação “não sou um robô”. Trem, ônibus e Boleto "
                     "Turístico ficam fora, com o valor dos guias marcado. <b>Sem a "
                     "hospedagem.</b>"),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 4 dias, 1 pessoa, valores em "
                  "real. Mude as datas e o número de pessoas, desmarque o que você não "
                  "vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">O total tem só as duas tarifas do governo "
            "peruano</b>: o bilhete de estrangeiro (S/ 152) e a taxa do SERNANP (S/ 11), "
            "convertidos pela taxa de venda do Banco Central de 23/out/2026. O trem é de "
            "empresa privada, com preço por data; o ônibus e o Boleto Turístico não "
            "tinham site oficial legível. <b>Esta ficha não tem hospedagem</b>: não achamos "
            "diária oficial."),
        "linhas": [
            ("ingresso", BOLETO, "Machu Picchu, bilhete de estrangeiro", "S/ 152 · R$ 222,12",
             IMP + "El Comercio e Infobae, fev/2026, atribuindo ao Ministério da Cultura. "
             "Estudante estrangeiro S/ 77.<br>"
             "<b>Peruano e cidadão da Comunidade Andina pagam S/ 64</b> (R.M. "
             "000284-2025-MC, pela Andina) — o Brasil não é membro, e o brasileiro paga "
             "2,4 vezes. Hora de entrada marcada; de 4 a 6 horas no sítio.<br>"
             "<span class=\"flag\">Fontes divergem</span> a Infobae de nov/2025 dava "
             "US$ 60."),
            ("ingresso", SERNANP, "Taxa do SERNANP", "S/ 11 · R$ 16,07",
             "Data oficial: R.D. 000006-2026-SERNANP/DUSRN (El Peruano, 4/fev/2026), "
             "<b>desde 1º/5/2026</b>, depois de quatro adiamentos. " + IMP +
             "S/ 11 para estrangeiro, somados ao bilhete (El Comercio, fev/2026). Quem "
             "chega pelo Caminho Inca não paga."),
            ("ingresso", None, "Montanha (Huayna Picchu ou Montanha Machu Picchu)",
             "S/ 200 (guias)",
             SEC + "para estrangeiro, guias citam S/ 200 pela rota com montanha; o peruano "
             "paga S/ 112 (Andina). Quem escolhe a montanha troca a linha do bilhete. "
             "<b>Fora do total.</b>"),
            ("fixo", None, "Trem Cusco–Aguas Calientes", "por data",
             "<span class=\"flag\">Lacuna declarada</span> trens de empresas privadas, "
             "com preço por data e horário. <b>Fora do total.</b>"),
            ("fixo", None, "Ônibus Aguas Calientes–ruínas, ida e volta", "US$ 24 (guias)",
             SEC + "o site da Consettur estava com certificado inválido em 29/out/2026. "
             "<b>Fora do total.</b>"),
            ("ingresso", None, "Boleto Turístico de Cusco", "S/ 130 (guias)",
             SEC + "o site do COSITUC estava fora do ar em 29/out/2026. Integral de 10 "
             "dias; não inclui Machu Picchu. <b>Fora do total.</b>"),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, conferidos em 29 de outubro de 2026. <b>O total "
            "tem só as duas tarifas do governo peruano</b>, pela imprensa: o bilhete e a "
            "taxa do SERNANP. <b>Sem a hospedagem e sem o trajeto</b> — trem, ônibus e "
            "Boleto Turístico ficam fora, com o valor dos guias marcado.<br>"
            "<b>O que mais muda esta conta é o passaporte.</b> O mesmo bilhete custa "
            "S/ 64 ao peruano, ao boliviano, ao colombiano e ao equatoriano, e S/ 152 ao "
            "brasileiro."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis em Cusco e Aguas Calientes"),
            ("https://www.getyourguide.com/", "GetYourGuide", "passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. A data da taxa do SERNANP "
            "vem da resolução publicada no El Peruano; a tarifa de peruanos e andinos, da "
            "Andina, agência de notícias do governo peruano; o bilhete de estrangeiro e o "
            "valor do SERNANP, de El Comercio e Infobae, que reproduzem a tarifa oficial. "
            "O câmbio é o do boletim de fechamento do Banco Central do Brasil. <b>Nenhum "
            "valor do total veio de agregador de viagem</b>; os valores de guia estão "
            "marcados e fora da soma."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("foz-do-iguacu", "Foz do Iguaçu"),
    ("fernando-de-noronha", "Fernando de Noronha"), ("bonito", "Bonito"),
    ("machu-picchu", "Machu Picchu"),
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
