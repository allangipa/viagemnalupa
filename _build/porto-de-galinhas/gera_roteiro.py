# -*- coding: utf-8 -*-
"""Roteiro de 4 dias em Porto de Galinhas, com um dia no Recife.

Mesmo molde do bonito/gera_roteiro.py.

O QUE DECIDE A ORDEM
--------------------
    mare     as piscinas naturais so se formam na mare baixa: o dia da
             jangada e o da mare, nao o do calendario
    segunda  fecham os tres museus do Recife (Instituto Ricardo Brennand,
             Oficina Francisco Brennand e Paco do Frevo)
    terca    o Paco do Frevo e gratis; na ultima terca do mes o Instituto
             Ricardo Brennand tambem - menos em janeiro, julho e dezembro

POR QUE ESTA ORDEM (sabado a terca)
-----------------------------------
    sabado   chegada e a praia
    domingo  a jangada, no horario da mare baixa
    segunda  praia: os museus do Recife estao fechados
    terca    Recife no caminho do aeroporto: Paco do Frevo de graca e os
             dois Brennand

Uso
---
    python _build/porto-de-galinhas/gera_roteiro.py
    python _build/porto-de-galinhas/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_pg_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

SEC = '<span class="flag">Só em fonte secundária</span> '

ROTEIROS = {
    "porto-de-galinhas": {
        "dias": 4,
        "titulo": "Roteiro de 4 dias em Porto de Galinhas e Recife",
        "descricao": ("Quatro dias em Porto de Galinhas, com um dia no Recife, na ordem que a "
                      "maré e o calendário permitem: a jangada na maré baixa e os museus fora "
                      "da segunda-feira."),
        "abertura": ("Quatro dias de sábado a terça, porque <b>a jangada depende da maré "
                     "baixa</b> e <b>os três museus do Recife fecham na segunda</b>. A terça "
                     "fica para o Recife: é o dia em que o Paço do Frevo não cobra."),
        "avisos": [
            ("a", "A jangada não tem preço publicado — pergunte antes de embarcar",
             "<p>O passeio às piscinas naturais é o que todo mundo faz, e <b>não achamos "
             "tabela oficial</b>, nem da associação dos jangadeiros nem da prefeitura.</p>"
             "<p>Os guias de viagem vão de <b>R$ 50 a R$ 100</b> por pessoa: o mais caro é o "
             "dobro do mais barato. <b>Combine o preço na praia, antes de subir na "
             "jangada.</b></p>"
             "<p>As piscinas só se formam na <b>maré baixa</b>: olhe a tábua de marés antes "
             "de escolher o dia.</p>"),
            ("b", "Barraca não pode cobrar consumação mínima",
             "<p>Segundo a imprensa, a Prefeitura de Ipojuca proibiu a <b>consumação "
             "mínima</b>, a taxa por não consumir e a venda casada nas barracas, pelo Decreto "
             "nº 149/2025, na virada de 2026. Vale em Porto de Galinhas, Cupê, Muro Alto e "
             "Maracaípe.</p>"
             "<p>Na primeira semana, 49 barracas foram fiscalizadas e 6 notificadas. Não "
             "achamos o texto oficial do decreto.</p>"),
            ("a", "Segunda fecha os museus; terça tem um de graça",
             "<p><b>Instituto Ricardo Brennand, Oficina Francisco Brennand e Paço do Frevo "
             "fecham na segunda.</b></p>"
             "<p><b>Na terça, o Paço do Frevo é gratuito para todos.</b> Na última terça do "
             "mês, o Instituto Ricardo Brennand também — <b>menos em janeiro, julho e "
             "dezembro</b>, os meses de férias.</p>"),
            ("b", "O que este roteiro não alcança, e está dito",
             "<p><b>O preço da jangada</b>, que só aparece em guias de viagem.</p>"
             "<p><b>A hospedagem em fonte oficial</b>: a diária da ficha vem de um painel do "
             "setor.</p>"
             "<p><b>Buggy, mergulho e os passeios de Muro Alto e Maracaípe</b>, de operadores "
             "privados, sem tabela.</p>"),
        ],
        "dias_lista": [
            ("Sábado — a chegada e a praia",
             "Do Recife, o ônibus <b>191</b> custa <b>R$ 14,80</b> e o <b>195</b>, opcional, "
             "<b>R$ 22,50</b>, pela tabela do Grande Recife. À tarde, a praia. <b>Nas "
             "barracas, consumação mínima está proibida</b>, segundo a imprensa.",
             ["Ônibus 191 · R$ 14,80",
              "Ônibus 195 · R$ 22,50",
              "Consumação mínima · proibida"]),

            ("Domingo — a jangada, na hora da maré",
             "<b>Piscinas naturais de jangada</b>, no horário da maré baixa. " + SEC +
             "o preço não é publicado; os guias vão de <b>R$ 50 a R$ 100</b>. Combine antes "
             "de embarcar.",
             ["Jangada · guias R$ 50 a R$ 100",
              "Só na maré baixa",
              "Combine o preço antes"]),

            ("Segunda — praia, porque o Recife está fechado",
             "Os três museus do Recife fecham na segunda. Dia de praia em Porto de Galinhas "
             "ou nas vizinhas Muro Alto e Maracaípe, onde vale o mesmo decreto das "
             "barracas.",
             ["Museus do Recife · fechados",
              "Muro Alto e Maracaípe"]),

            ("Terça — o Recife, no caminho de volta",
             "<b>Paço do Frevo</b>, grátis às terças (R$ 10 nos outros dias), das 10h às 18h. "
             "<b>Oficina Francisco Brennand</b>: <b>R$ 50</b>, R$ 40 para morador de "
             "Pernambuco, das 10h às 17h. <b>Instituto Ricardo Brennand</b>: <b>R$ 60</b>, "
             "última entrada às 16h30 — a página dá dois horários de abertura, então vá a "
             "partir das 13h. Na última terça do mês ele é grátis, menos em janeiro, julho e "
             "dezembro.",
             ["Paço do Frevo · grátis na terça",
              "Oficina Brennand · R$ 50",
              "Instituto Ricardo Brennand · R$ 60",
              "Última entrada · 16h30"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de custos, "
                   "conferidos em 27 de novembro de 2026: páginas oficiais dos três museus e "
                   "do Grande Recife Consórcio de Transporte. <b>Vêm da imprensa</b> o decreto "
                   "das barracas e, de guias de viagem, o preço da jangada."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
