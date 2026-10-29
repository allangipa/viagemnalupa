# -*- coding: utf-8 -*-
"""Roteiro de 3 dias em Foz do Iguacu, montado pelo calendario.

Mesmo molde do gramado/gera_roteiro.py.

O QUE O CALENDARIO DECIDE
-------------------------
    segunda  o Marco das Tres Fronteiras fecha ("de terca-feira a
             domingo"), e os guias dizem que o Templo Budista tambem.
             O roteiro vai de sexta a domingo.
    terca    o Refugio Biologico de Itaipu fecha ("de quarta-feira a
             segunda-feira") - nao entra no roteiro, mas fica dito
    sexta,   a Itaipu Iluminada (R$ 50) so acontece nesses dois dias,
    sabado   as 19h

POR QUE SEXTA, SABADO E DOMINGO
-------------------------------
    sexta    o lado brasileiro: Parque das Aves na abertura (8h30), o
             Parque Nacional e o Macuco Safari, todos na mesma avenida
    sabado   o lado argentino: abre as 8h, e o ultimo trem para a
             Garganta sai as 15h30 - a Garganta vem primeiro
    domingo  Itaipu Panoramica de manha, o Templo Budista, e o Marco,
             que so abre as 14h, para o por do sol

A ARMADILHA QUE MAIS PEGA
--------------------------
O lado argentino nao tem tarifa Mercosul e a bilheteria so aceita cartao
ou peso argentino em dinheiro. Quem chega com real na mao nao entra pelo
guiche em dinheiro. O aviso "a" existe por isso.

Uso
---
    python _build/foz-do-iguacu/gera_roteiro.py
    python _build/foz-do-iguacu/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_foz_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "foz-do-iguacu": {
        "dias": 3,
        "titulo": "Roteiro de 3 dias em Foz do Iguaçu",
        "descricao": ("Três dias em Foz do Iguaçu na ordem que o calendário permite: as "
                      "Cataratas dos dois lados, o último trem da Garganta às 15h30 e o "
                      "Marco das Três Fronteiras, que fecha na segunda."),
        "abertura": ("Três dias de sexta a domingo, porque <b>o Marco das Três Fronteiras "
                     "fecha na segunda</b> — e o Templo Budista também, segundo os guias. "
                     "<b>E uma conta que muda de um lado do rio para o outro:</b> o lado "
                     "brasileiro cobra R$ 121 do brasileiro e do argentino; o lado "
                     "argentino cobra AR$ 60.000, cerca de R$ 198, de qualquer "
                     "estrangeiro, brasileiro incluído."),
        "avisos": [
            ("a", "O lado argentino cobra preço de estrangeiro — e não aceita real em dinheiro",
             "<p>A tabela oficial do Parque Nacional Iguazú, vigente desde 1º de junho de "
             "2026, tem <b>“Visitantes internacionales AR$ 60.000”</b> e <b>nenhuma faixa "
             "Mercosul</b>. Brasileiro paga como qualquer estrangeiro. Pela taxa de venda "
             "do Banco Central de 23 de outubro, <b>R$ 197,94</b> — 64% a mais que os "
             "R$ 121 do lado brasileiro.</p>"
             "<p>A bilheteria aceita <b>cartão de crédito, débito e dinheiro em peso "
             "argentino</b>. Real não. No cartão brasileiro entra o IOF.</p>"
             "<p><b>Vai voltar no dia seguinte?</b> Guarde o ingresso: apresentado na "
             "bilheteria, <b>o segundo dia sai pela metade</b>.</p>"),
            ("b", "No lado brasileiro não há meia-entrada — idoso e estudante pagam R$ 121",
             "<p>A página de descontos do Parque Nacional do Iguaçu diz que ele <b>“não "
             "dispõe de meia-entrada ou descontos adicionais na tabela”</b>. A lei da meia "
             "estudantil e o Estatuto da Pessoa Idosa valem para outros lugares, não para "
             "parque federal.</p>"
             "<p><b>Criança até 6 anos não paga.</b> Morador dos 14 municípios do entorno "
             "tem o Passe Comunidade, de R$ 26. Do resto, todo brasileiro paga R$ 121 — e "
             "os R$ 3 do Fundo Iguaçu, incluídos nesse valor, são voluntários.</p>"
             "<p>O Macuco Safari, dentro do parque, é outra empresa e tem meia: R$ 192 "
             "para idoso brasileiro e estudante.</p>"),
            ("a", "A segunda-feira fecha o Marco — por isso o roteiro termina no domingo",
             "<p>O <b>Marco das Três Fronteiras</b> abre <b>“de terça-feira a domingo, "
             "das 14h às 21h”</b>, diz o site oficial. Na segunda, fechado.</p>"
             "<p>O <b>Templo Budista</b> também não abre na segunda, segundo os guias de "
             "viagem — não achamos página oficial do templo.</p>"
             "<p>E o <b>Refúgio Biológico de Itaipu</b> funciona “de quarta-feira a "
             "segunda-feira”: fecha na terça. <b>Se a sua viagem incluir uma segunda</b>, "
             "ponha nela as Cataratas, que abrem todos os dias dos dois lados, e a Itaipu "
             "Panorâmica.</p>"),
            ("b", "O último trem para a Garganta do Diabo sai às 15h30",
             "<p>No lado argentino, o parque abre às 8h, mas <b>a entrada na Área Cataratas "
             "vai só até as 16h</b> e <b>o último trem da Estação Central para a Estação "
             "Garganta sai às 15h30</b>. O último retorno é às 17h30.</p>"
             "<p>A mesma página diz que a entrada nos circuitos vai até 15h45 e, mais "
             "abaixo, até 16h45. <b>Conte com o horário mais cedo</b> — e faça a Garganta "
             "primeiro.</p>"),
            ("a", "O que este roteiro não alcança, e está dito",
             "<p><b>A hospedagem.</b> Nenhum órgão publica a diária média de Foz do "
             "Iguaçu, e a ficha de custos fica sem ela em vez de estimar.</p>"
             "<p><b>O preço do ônibus até o lado argentino</b>: a Secretaria de Turismo "
             "diz quem faz a linha e o horário, não quanto custa.</p>"
             "<p><b>A taxa de turismo dos hotéis</b>, cobrada pelos associados do Visit "
             "Iguassu: não achamos lei nem valor.</p>"
             "<p><b>O estacionamento das Cataratas brasileiras</b>, que só tem link de "
             "reserva, e <b>o horário do Templo Budista</b>, que só aparece em guias de "
             "viagem.</p>"),
        ],
        "dias_lista": [
            ("Sexta — o lado brasileiro: Parque das Aves, Cataratas e Macuco",
             "<b>Parque das Aves às 8h30</b>, quando abre: <b>R$ 110</b> a inteira, "
             "<b>R$ 55</b> a meia, até 8 anos não paga — e a página avisa que o preço "
             "vale até 30 de novembro. Fica na Avenida das Cataratas, perto da entrada do "
             "Parque Nacional. Depois, o <b>Parque Nacional do Iguaçu</b>: <b>R$ 121</b> "
             "para brasileiro e cidadão do Mercosul, <b>sem meia-entrada</b>. Nos dias "
             "úteis a página dá 9h às 16h. Dentro do parque, o <b>Macuco Safari</b> — "
             "<b>R$ 384</b>, cerca de 2 horas, saídas a cada 20 minutos, sem reserva — "
             "<b>não inclui a entrada do parque</b>. É a linha mais cara da viagem, e as "
             "Cataratas se veem inteiras sem ela. O ônibus urbano, <b>R$ 5</b>, vai do "
             "centro até a portaria.",
             ["Parque das Aves · R$ 110 · 8h30–16h30",
              "Parque Nacional · R$ 121 · sem meia",
              "Macuco Safari · R$ 384 · entrada à parte",
              "Ônibus urbano · R$ 5",
              "Fundo Iguaçu · R$ 3 voluntário"]),

            ("Sábado — o lado argentino, com a Garganta primeiro",
             "<b>Leve peso argentino ou cartão</b>: a bilheteria do Parque Nacional Iguazú "
             "não aceita real em dinheiro. A entrada é <b>AR$ 60.000</b>, cerca de "
             "<b>R$ 198</b>, para qualquer estrangeiro — <b>o brasileiro não tem tarifa "
             "Mercosul</b>. Inclui o Trem Ecológico. <b>Vá direto à Garganta do Diabo:</b> "
             "o primeiro trem sai às 8h20 e <b>o último às 15h30</b>, e a entrada na Área "
             "Cataratas vai só até as 16h. Depois, os circuitos Superior e Inferior. O "
             "ônibus sai do Terminal de Transporte Urbano todos os dias das 7h às 19h, "
             "por duas empresas — <b>o preço não está publicado</b>. Leve documento: a "
             "bilheteria pede DNI ou passaporte para definir a categoria. "
             "<b>Na volta, se ainda houver fôlego</b>, a Itaipu Iluminada é sábado às 19h, "
             "R$ 50.",
             ["Parque Nacional Iguazú · AR$ 60.000",
              "Cartão ou peso em dinheiro · real não",
              "Último trem à Garganta · 15h30",
              "Entrada até 16h",
              "Segundo dia · metade do preço"]),

            ("Domingo — Itaipu de manhã, o Templo e o Marco no fim da tarde",
             "<b>Itaipu Panorâmica</b>: <b>R$ 63</b>, cerca de 1h10, todos os dias das "
             "8h15 às 17h, saídas a cada 30 minutos por ordem de chegada. Para entrar na "
             "usina até a Sala do Comando Central, a <b>Itaipu Especial</b> custa "
             "<b>R$ 185</b>, com vagas limitadas. <b>Dinheiro, só em real.</b> Depois, o "
             "<b>Templo Budista Chen Tien</b>, de graça — o horário aparece como 9h30 às "
             "16h30 num guia e até 17h em outro, então chegue cedo. <b>O Marco das Três "
             "Fronteiras abre às 14h</b> e vai até as 21h: <b>R$ 60</b>, ou R$ 31,50 na "
             "reduzida. É domingo porque o Marco fecha na segunda.",
             ["Itaipu Panorâmica · R$ 63 · 8h15–17h",
              "Itaipu Especial · R$ 185",
              "Templo Budista · grátis · fecha na segunda",
              "Marco das Três Fronteiras · R$ 60 · 14h–21h",
              "Fecha na segunda"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de "
                   "custos, apurados em 29 de outubro de 2026 nas páginas oficiais do "
                   "Parque Nacional do Iguaçu, do Parque Nacional Iguazú, do Macuco "
                   "Safari, do Parque das Aves, do Turismo Itaipu, do Marco das Três "
                   "Fronteiras e da Secretaria Municipal de Turismo. <b>Quatro coisas "
                   "ficaram sem resposta, e estão ditas nas fichas:</b> a diária de "
                   "hospedagem, que ninguém publica; o preço do ônibus até a Argentina; "
                   "a taxa de turismo dos hotéis; e o horário do Templo Budista, que só "
                   "aparece em guias. <b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
