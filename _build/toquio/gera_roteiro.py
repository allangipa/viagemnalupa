# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Toquio, montado pelo calendario e pelo passe.

Mesmo molde do machu-picchu/gera_roteiro.py.

O QUE DECIDE A ORDEM
--------------------
    segunda   o Museu Nacional fecha (se for feriado, fecha na terca)
    26-31/12  o Museu Nacional fecha no fim do ano
    sex, sab  o Museu Nacional vai ate as 20h
    passe     o Tokyo Subway Ticket de 72 horas cobre tres dias seguidos:
              o roteiro junta neles o que depende de metro

POR QUE ESTA ORDEM (quarta a domingo)
-------------------------------------
    quarta   chegada
    quinta   passe de 72 h comeca; Skytree, com ingresso comprado online
    sexta    Museu Nacional, aberto ate as 20h
    sabado   ultimo dia do passe; compras, com o tax-free novo
    domingo  volta

Uso
---
    python _build/toquio/gera_roteiro.py
    python _build/toquio/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_toquio_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

SEC = '<span class="flag">Só em fonte secundária</span> '

ROTEIROS = {
    "toquio": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Tóquio",
        "descricao": ("Cinco dias em Tóquio na ordem que o calendário e o passe de metrô "
                      "permitem: o Museu Nacional fora da segunda, o Skytree comprado online e "
                      "três dias seguidos de passe."),
        "abertura": ("Cinco dias de quarta a domingo, porque <b>o Museu Nacional fecha na "
                     "segunda</b> e fica aberto até as 20h na sexta e no sábado — e porque o "
                     "<b>passe de metrô de 72 horas</b> rende mais com três dias seguidos de "
                     "cidade. <b>Quatro cobranças do turista mudaram em 2026</b>; guia antigo "
                     "erra todas."),
        "avisos": [
            ("a", "Quatro cobranças mudaram em 2026 — confira a data do guia que você leu",
             "<p><b>14 de março:</b> o Tokyo Subway Ticket de 24 horas foi de ¥ 800 para "
             "<b>¥ 1.000</b>; o de 72 horas, de ¥ 1.500 para ¥ 2.000.</p>"
             "<p><b>1º de julho:</b> a taxa de saída do Japão triplicou, de ¥ 1.000 para "
             "<b>¥ 3.000</b>. Vem na passagem.</p>"
             "<p><b>1º de novembro:</b> o tax-free virou reembolso, segundo a imprensa: paga-se "
             "com imposto e recebe-se na saída.</p>"
             "<p><b>1º de abril de 2027:</b> a taxa de hospedagem de Tóquio, hoje de ¥ 100 ou "
             "¥ 200 por noite, vira 3% da diária.</p>"),
            ("b", "No Skytree, o balcão cobra ¥ 500 a mais",
             "<p>A página oficial avisa: <b>¥ 500 de taxa de serviço por ingresso</b> para "
             "quem compra no balcão ou nas máquinas do 4º andar. Online, o Tembo Deck sai a "
             "partir de ¥ 1.800.</p>"
             "<p>O preço é “a partir de”: muda com a data.</p>"),
            ("a", "O Museu Nacional fecha na segunda e de 26 a 31 de dezembro",
             "<p><b>Fecha na segunda</b>; se a segunda for feriado, abre e fecha na terça. "
             "<b>Fechado de 26 a 31 de dezembro de 2026</b>, e reabre em 1º de janeiro, do "
             "meio-dia às 20h.</p>"
             "<p>Na sexta e no sábado vai até as 20h.</p>"),
            ("b", "O que este roteiro não alcança, e está dito",
             "<p><b>A hospedagem</b>, sem diária oficial.</p>"
             "<p><b>O Shibuya Sky e os outros mirantes</b>, cuja página não conseguimos "
             "ler.</p>"
             "<p><b>O trem do aeroporto</b>, que não apuramos.</p>"
             "<p><b>As regras finas do tax-free</b>: não lemos a agência oficial.</p>"),
        ],
        "dias_lista": [
            ("Quarta — a chegada",
             "Dia de chegada. A taxa de hospedagem de Tóquio aparece na conta do hotel: "
             "<b>¥ 100 ou ¥ 200 por pessoa por noite</b>, conforme a diária, e nada abaixo de "
             "¥ 10.000.",
             ["Taxa de hospedagem · ¥ 100 ou ¥ 200",
              "Isenta abaixo de ¥ 10.000"]),

            ("Quinta — o passe começa, e o Skytree",
             "Compre o <b>Tokyo Subway Ticket de 72 horas</b>: <b>¥ 2.000</b>, cerca de "
             "R$ 64, válido nas duas redes de metrô. <b>Tokyo Skytree</b> com ingresso "
             "comprado online: Tembo Deck <b>a partir de ¥ 1.800</b>, cerca de R$ 58; combo "
             "dos dois andares a partir de ¥ 3.000. No balcão, ¥ 500 a mais.",
             ["Passe 72 h · ¥ 2.000",
              "Skytree · desde ¥ 1.800",
              "Balcão · ¥ 500 a mais",
              "Até 5 anos · grátis"]),

            ("Sexta — o Museu Nacional, até as 20h",
             "<b>Museu Nacional de Tóquio</b>, no Parque Ueno: <b>¥ 1.000</b>, cerca de R$ 32, "
             "o acervo permanente. Na sexta fica aberto <b>até as 20h</b>, com última entrada "
             "meia hora antes.",
             ["Museu Nacional · ¥ 1.000",
              "Sexta e sábado · até 20h",
              "Fecha na segunda"]),

            ("Sábado — o último dia do passe, e as compras",
             "Último dia das 72 horas de metrô. Para as compras: " + SEC +
             "desde 1º de novembro de 2026 o <b>tax-free é reembolso</b> — paga-se o preço "
             "com imposto e recebe-se na saída do país, com mínimo de ¥ 5.000 na mesma loja "
             "no mesmo dia.",
             ["Passe · último dia",
              "Tax-free · reembolso na saída",
              "Mínimo · ¥ 5.000 por loja"]),

            ("Domingo — a volta",
             "A <b>taxa de saída do Japão, ¥ 3.000</b>, já veio na passagem. Guarde os "
             "comprovantes das compras para o reembolso do tax-free.",
             ["Taxa de saída · ¥ 3.000 · na passagem",
              "Reembolso do tax-free"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de custos, "
                   "conferidos em 27 de novembro de 2026: páginas oficiais do Tokyo Skytree e "
                   "do Museu Nacional, comunicado e documento do Governo Metropolitano de "
                   "Tóquio, e a JNTO. <b>Vêm só da imprensa</b> o tax-free novo e a data da "
                   "taxa de hospedagem de 3%."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
