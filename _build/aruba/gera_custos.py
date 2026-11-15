# -*- coding: utf-8 -*-
"""Ficha de custos de Aruba: 5 dias, 1 pessoa, dolar americano.

Mesmo molde do salvador/gera_custos.py: COM HOSPEDAGEM, pela diaria media
(ADR) de 2025 do Banco Central de Aruba, State of the Economy 2025
Retrospective, Tabela 1: US$ 408,99. So o numero anual: os meses de 2026
nao foram lidos, e por isso o seletor tem uma opcao so.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
A Sustainability Fee (US$ 20) entra no total: e por pessoa, obrigatoria
para quem chega de aviao, paga no ED card.

O imposto de hospedagem (12,5%) e a taxa ambiental (US$ 3 por quarto por
noite) ficam FORA do total, na propria linha: a calculadora nao modela
percentual sobre a diaria escolhida. A nota diz quanto da na media: US$
216,50 em 4 noites, por quarto.

O taxi do aeroporto fica fora: e por carro (1 a 4 pessoas), e a conta e por
pessoa. O onibus entra em 8 viagens - suposicao desta ficha.

Uso
---
    python _build/aruba/gera_custos.py
    python _build/aruba/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_aruba_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "aruba": {
        "nome": "Aruba", "dias": 5, "moeda": "US$", "dec": 2,
        "titulo": "Quanto custa 5 dias em Aruba em 2026",
        "descricao": ("O custo de 5 dias em Aruba, por pessoa, com a diária média dos hotéis "
                      "de 2025, a taxa de US$ 20 do formulário de entrada e os impostos que "
                      "não estão na diária."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas em "
                     "15 de novembro de 2026. <b>Com hospedagem</b>: a diária média dos hotéis "
                     "de Aruba em 2025, do Banco Central de Aruba — e, à parte, os 12,5% de "
                     "imposto e os US$ 3 por noite que a diária não inclui."),
        "hosp": [
            {"k": "media", "rot": "Média dos hotéis em 2025 (Banco Central de Aruba)",
             "ref": 408.99, "mn": 408.99, "mx": 408.99},
        ],
        "hospPadrao": "media",
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em dólar. "
                  "Mude as datas e o número de pessoas, desmarque o que você não vai fazer, "
                  "e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">A diária não é o que você paga.</b> Por cima dela "
            "vêm <b>12,5% de imposto de hospedagem</b> e <b>US$ 3 por noite por quarto</b> "
            "de taxa ambiental. Na diária média, isso dá <b>US$ 216,50 por quarto em quatro "
            "noites</b>, que esta calculadora não soma — ela não modela percentual. "
            "<b style=\"color:var(--gelo)\">A taxa de US$ 20 do formulário de entrada está no "
            "total</b>, por pessoa; menor de 8 anos não paga. A hospedagem é a média anual de "
            "2025 do Banco Central de Aruba, por quarto, duas pessoas por quarto: não há série "
            "mensal publicada que tenhamos lido."),
        "linhas": [
            # ---------------------------------------------------- entrada
            ("fixo", 20.00, "Sustainability Fee, no formulário de entrada", "US$ 20,00",
             "Por pessoa que chega de avião, <b>paga no ED card, só no cartão de crédito, "
             "antes do check-in do voo</b>. Em vigor desde 1º/jul/2024. Menor de 8 anos não "
             "paga. Quem volta no mesmo ano é isento, mas o sistema não reconhece: paga e pede "
             "reembolso em até 60 dias. Fonte: aruba.com, 15/nov/2026."),
            # ---------------------------------------------------- ingressos
            ("ingresso", 22.00, "Parque Nacional Arikok", "US$ 22,00",
             "Adulto; <b>menor de 17 não paga</b>. Vale também para a Natural Pool, que só se "
             "alcança de 4x4. Fonte: Aruba Conservation Foundation (acf.aw), 15/nov/2026."),
            ("ingresso", 5.00, "California Lighthouse", "US$ 5,00",
             "Para subir ao topo, sem reserva, das 9h às 19h. Fonte: aruba.com, "
             "15/nov/2026."),
            ("ingresso", 19.00, "Butterfly Farm", "US$ 19,00",
             "Adulto; US$ 16 sênior e estudante; US$ 10 de 4 a 17 anos. <b>O ingresso deixa "
             "voltar durante a viagem</b>, por até um mês. Fonte: thebutterflyfarm.com, "
             "15/nov/2026."),
            ("ingresso", 0.00, "Praias, Donkey Sanctuary e costa norte", "grátis",
             "As praias são públicas pela política oficial do governo; a cadeira montada pelo "
             "hotel é do hotel. O Donkey Sanctuary não cobra entrada e aceita doação. Na costa "
             "norte, as páginas oficiais não citam cobrança."),
            ("ingresso", None, "Renaissance Island (day pass)",
             "<span class=\"flag\">Não publicado</span>",
             "A autoridade de turismo diz que a ilha é <b>só para hóspedes</b> do resort. Day "
             "pass e preço não aparecem em fonte oficial; fora do total."),
            # ---------------------------------------------------- transporte
            ("fixo", 20.80, "Ônibus, 8 viagens", "US$ 20,80",
             "<b>US$ 2,60 a viagem</b> (AWG 4.50); passe do dia, US$ 15. Aceita dinheiro a "
             "bordo, e a Linha 2 vai ao aeroporto. <b>Oito viagens é suposição desta ficha, "
             "não dado.</b> Fonte: arubus.com, 15/nov/2026."),
            ("ingresso", None, "Táxi do aeroporto até Palm Beach", "US$ 40 a US$ 41",
             "Por carro, de 1 a 4 pessoas, sem sobretaxa (aruba.com); Oranjestad US$ 26, Eagle "
             "Beach US$ 37. Tabela do governo em taxi.aw desde 20/mai/2026. <b>Fora do "
             "total</b>, porque é por carro e esta conta é por pessoa."),
            # ---------------------------------------------------- taxa
            ("taxa", None, "Imposto de hospedagem e taxa ambiental", "12,5% + US$ 3 por noite",
             "<b>12,5% do valor do quarto</b> (Landsverordening toeristenheffing, art. 5) e "
             "<b>Afl. 5,37 (US$ 3) por noite por quarto</b> (impuesto.aw), consultados em "
             "15/nov/2026. Na diária média, US$ 216,50 por quarto em quatro noites. <b>Fora do "
             "total</b>: a calculadora não modela percentual sobre a diária."),
            # ---------------------------------------------------- cama
            ("hosp", None, "Hospedagem, 4 noites", "US$ 1.635,96",
             "Fonte: <b>Banco Central de Aruba</b>, <i>State of the Economy 2025 "
             "Retrospective</i>, Tabela 1: diária média (ADR) dos hotéis em 2025, <b>US$ 408,99 "
             "por quarto por noite</b>, contra US$ 364,28 em 2024 — 12,3% de alta —, com "
             "ocupação de 76,4%, consultado em 15/nov/2026.<br>"
             "<span class=\"flag\">Ressalva</span> é a média anual da ilha inteira; não se sabe "
             "se inclui pacotes all-inclusive, e os meses de 2026 não foram lidos. "
             "<b>Impostos à parte</b>, na linha de cima."),
        ],
        "rodape_tabela": (
            "Valores em dólar, por pessoa, apurados em 15 de novembro de 2026. <b>Três linhas "
            "estão fora do total</b>: os impostos da hospedagem, que são percentuais; o táxi, "
            "que é por carro; e o day pass da Renaissance Island, que não tem preço "
            "publicado.<br>"
            "<b>A linha que mais pesa é a cama</b>, e ela subiu 12,3% em um ano. Por cima "
            "dela, conte 12,5% e US$ 3 por noite."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e resorts"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. A taxa de entrada, as praias, "
            "o farol e o táxi vêm da Aruba Tourism Authority (aruba.com); o parque, da Aruba "
            "Conservation Foundation; o ônibus, do Arubus; os impostos, da lei de hospedagem e "
            "do departamento de impostos (impuesto.aw); a diária, do Banco Central de Aruba. "
            "<b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("londres", "Londres"), ("florianopolis", "Florianópolis"),
    ("sao-paulo", "São Paulo"), ("aruba", "Aruba"),
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
