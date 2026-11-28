# -*- coding: utf-8 -*-
"""Ficha de custos de Porto de Galinhas (com Recife): 4 dias, 1 pessoa, real.

Mesmo molde do bonito/gera_custos.py, mas COM hospedagem.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
A hospedagem vem de painel do setor, nao de orgao oficial: Hotel Report 2026
da Omnibees, publicado pelo Hotelier News em 18/08/2026 - diaria media de
Ipojuca de R$ 1.134 em 2025 (R$ 1.059 em 2024; R$ 1.093 em 2026 ate junho).
Entra como Paris entrou (painel do setor via imprensa), com a ressalva
escrita na linha: e media de reservas de um motor de reservas, num destino de
resorts. 3 noites x 1.134 = 3.402.

A jangada as piscinas naturais, o passeio principal, fica FORA do total: nao
ha tabela oficial, e os guias vao de R$ 50 a R$ 100.

O onibus entra pela linha 191 (R$ 14,80), ida e volta: 29,60.

Uso
---
    python _build/porto-de-galinhas/gera_custos.py
    python _build/porto-de-galinhas/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_pg_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

ADR_2025, ADR_2024, ADR_2026 = 1134, 1059, 1093
SEC = '<span class="flag">Só em fonte secundária</span> '

FICHAS = {
    "porto-de-galinhas": {
        "nome": "Porto de Galinhas", "dias": 4, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 4 dias em Porto de Galinhas e Recife em 2026",
        "descricao": ("O custo de 4 dias em Porto de Galinhas, com um dia no Recife, por "
                      "pessoa: a diária média do painel do setor, três museus com tabela "
                      "oficial, o ônibus — e a jangada, que não tem preço publicado."),
        "abertura": ("A conta do que foi apurado, por pessoa, conferida em 27 de novembro de "
                     "2026. <b>A hospedagem vem de um painel do setor</b>, não de órgão "
                     "oficial, e está marcada. <b>A jangada às piscinas naturais fica fora do "
                     "total</b>: não tem preço publicado, e os guias vão de R$ 50 a R$ 100."),
        "hosp": [
            {"k": "media", "rot": "Média de Ipojuca em 2025 (painel Omnibees)",
             "ref": ADR_2025, "mn": ADR_2024, "mx": ADR_2025},
        ],
        "hospPadrao": "media",
        "intro": ("A tabela abaixo é a nossa apuração: 4 dias, 1 pessoa, valores em real. "
                  "Mude as datas e o número de pessoas, desmarque o que você não vai fazer, "
                  "e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">A hospedagem é a diária média de Ipojuca em "
            "2025, R$ 1.134, de um painel do setor</b> (Hotel Report 2026, da Omnibees, pelo "
            "Hotelier News). Não é dado oficial: é a média das reservas de um sistema de "
            "reservas, num destino de resorts. Por quarto, duas pessoas por quarto.<br>"
            "<b>A jangada às piscinas naturais não entra na soma</b>: não há tabela "
            "oficial."),
        "linhas": [
            ("ingresso", None, "Jangada às piscinas naturais", "R$ 50 a R$ 100 (guias)",
             SEC + "não achamos tabela oficial, nem da associação dos jangadeiros nem da "
             "Prefeitura de Ipojuca. Os guias de viagem vão de R$ 50 a R$ 100 — o dobro. "
             "Só na maré baixa. <b>Fora do total.</b>"),
            ("ingresso", 60.00, "Instituto Ricardo Brennand (Recife)", "R$ 60,00",
             "Fonte: página de horários e ingressos do site oficial, consultada em "
             "27/nov/2026. Meia: R$ 30,00. Com o Jardim e a Capela: R$ 80,00. Até 5 anos "
             "não paga.<br>"
             "<b>Última terça do mês grátis — menos em janeiro, julho e dezembro.</b> Fecha "
             "na segunda."),
            ("ingresso", 50.00, "Oficina Francisco Brennand (Recife)", "R$ 50,00",
             "Fonte: página de visitação do site oficial, consultada em 27/nov/2026. Meia: "
             "R$ 25. <b>Morador de Pernambuco: R$ 40</b> a inteira, R$ 20 a meia. Terça a "
             "domingo, 10h às 17h."),
            ("ingresso", 10.00, "Paço do Frevo (Recife)", "R$ 10,00",
             "Fonte: página de visitação do site oficial, consultada em 27/nov/2026. Meia: "
             "R$ 5,00. <b>Grátis às terças.</b> Fecha na segunda."),
            ("fixo", 29.60, "Ônibus Recife–Porto de Galinhas, ida e volta", "R$ 29,60",
             "Fonte: <b>Grande Recife Consórcio de Transporte</b>, página oficial de tarifas, "
             "consultada em 27/nov/2026: linha 191, sem ar-condicionado, <b>R$ 14,80</b> por "
             "trecho. A 195, opcional, custa R$ 22,50. Quem vai de carro ou transfer, "
             "desmarca."),
            ("hosp", None, "Hospedagem, 3 noites", "R$ 3.402,00",
             "<span class=\"flag\">Painel do setor, pela imprensa</span> diária média de "
             "Ipojuca em 2025: <b>R$ 1.134 por quarto por noite</b>, contra R$ 1.059 em 2024 "
             "e R$ 1.093 em 2026 com dados até junho. Fonte: <i>Hotel Report 2026</i>, da "
             "Omnibees, publicado pelo Hotelier News em 18/ago/2026.<br>"
             "<b>Não é dado oficial</b>: é a média das reservas de um sistema de reservas, "
             "num destino de resorts — pousada simples fica abaixo. Nenhum órgão público "
             "publica a diária de Porto de Galinhas."),
            ("taxa", None, "Taxa de turismo", "não achada",
             "<span class=\"flag\">Lacuna declarada</span> não achamos taxa de turismo, de "
             "preservação nem de veículos em Ipojuca. Ausência não se prova com documento. "
             "<b>Fora do total.</b>"),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, conferidos em 27 de novembro de 2026. <b>A "
            "hospedagem é de um painel do setor</b>, não de órgão oficial, e pesa 96% do "
            "total. <b>Sem a jangada</b>, que não tem preço publicado.<br>"
            "<b>Nas barracas de praia, a consumação mínima está proibida</b> por decreto de "
            "Ipojuca desde a virada de 2026, segundo a imprensa."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. Os três museus do Recife vêm "
            "das páginas oficiais de cada um; o ônibus, da página de tarifas do Grande Recife "
            "Consórcio de Transporte. <b>A hospedagem vem de um painel do setor</b> (Omnibees, "
            "pelo Hotelier News), marcada como tal. <b>A jangada só aparece em guias de "
            "viagem</b> e fica fora da soma. As páginas lidas estão guardadas com data."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("londres", "Londres"), ("florianopolis", "Florianópolis"),
    ("sao-paulo", "São Paulo"), ("aruba", "Aruba"),
    ("porto-de-galinhas", "Porto de Galinhas"),
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
