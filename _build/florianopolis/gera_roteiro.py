# -*- coding: utf-8 -*-
"""Roteiro de 4 dias em Florianopolis, montado pelo calendario.

Mesmo molde do gramado/gera_roteiro.py.

O QUE O CALENDARIO DECIDE
-------------------------
    domingo   o ultimo do mes, de marco a novembro, e gratis nas tres
              fortalezas da UFSC - por isso o norte da ilha fica no
              domingo
    a vespera o voucher do Campeche so sai 24 horas DEPOIS de o
              pagamento compensar: o Campeche nao pode ser o primeiro dia
              de quem reserva ao chegar

POR QUE QUINTA A DOMINGO
------------------------
    quinta   o centro: a ponte e o Mercado; reservar o Campeche
    sexta    a Lagoa, a Joaquina e o barco da Costa da Lagoa
    sabado   o Campeche, com o voucher ja liberado
    domingo  o norte: a Fortaleza de Sao Jose da Ponta Grossa

Uso
---
    python _build/florianopolis/gera_roteiro.py
    python _build/florianopolis/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_floripa_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "florianopolis": {
        "dias": 4,
        "titulo": "Roteiro de 4 dias em Florianópolis",
        "descricao": ("Quatro dias em Florianópolis na ordem que as regras permitem: o "
                      "voucher do Campeche que só sai 24 horas depois do pagamento e o "
                      "domingo em que as fortalezas não cobram."),
        "abertura": ("Quatro dias de quinta a domingo, montados por duas regras: <b>o "
                     "voucher da Ilha do Campeche só é liberado 24 horas depois de o "
                     "pagamento compensar</b> — então o Campeche não pode ser o primeiro "
                     "dia —, e <b>no último domingo do mês, de março a novembro, as "
                     "fortalezas da UFSC não cobram</b>."),
        "avisos": [
            ("a", "O Campeche não devolve, nem reagenda — veja o mar antes de pagar",
             "<p>O site oficial da Prefeitura: <b>“Não é possível reagendamento ou "
             "restituição do valor pago.”</b> E: <b>“A prefeitura não se responsabiliza "
             "por impossibilidade de visitação devido às condições meteorológicas ou de "
             "navegação.”</b></p>"
             "<p><b>O voucher é liberado 24 horas após a compensação do pagamento.</b> "
             "Boleto leva dias para compensar. Reserve com antecedência — e com a "
             "previsão do tempo aberta.</p>"
             "<p>Taxa municipal de <b>R$ 15</b>, limite de <b>800 pessoas por dia</b>, "
             "das 9h às 17h (ND Mais). O barco é à parte, de uma das associações que o "
             "site lista.</p>"),
            ("b", "O último domingo do mês é grátis nas fortalezas — até novembro",
             "<p>O Departamento das Fortalezas da UFSC: <b>“No último domingo de cada "
             "mês, entre março e novembro, a visitação é gratuita para todo o "
             "público.”</b></p>"
             "<p>Nos outros dias, <b>R$ 20</b>. <b>Dezembro, janeiro e fevereiro — a "
             "temporada — não têm o dia grátis.</b> Em 2026, o último é 29 de "
             "novembro.</p>"
             "<p>Nas fortalezas das ilhas, <b>a portaria só aceita dinheiro</b>; e "
             "<b>Anhatomirim está fechada</b> por obra no trapiche.</p>"),
            ("a", "O ônibus: Cartão Turista, e nada de dinheiro",
             "<p>A passagem é <b>R$ 7,70 no QR Code</b> e <b>R$ 7,20 no Cartão "
             "Turista</b>; o morador paga R$ 6,20 (ND Mais, tarifa de 1º/jan/2026). "
             "<b>O ônibus deixou de aceitar dinheiro em 5 de janeiro de 2026.</b></p>"
             "<p>O Passe Rápido dá <b>três horas de integração</b> entre linhas — numa "
             "ilha em que quase tudo passa pelos terminais, isso conta.</p>"),
            ("b", "A praia é de graça por lei",
             "<p><b>Lei federal nº 7.661/1988, art. 10</b>: <i>“As praias são bens "
             "públicos de uso comum do povo, sendo assegurado, sempre, livre e franco "
             "acesso a elas e ao mar.”</i></p>"
             "<p>Estacionamento, cadeira e guarda-sol são serviço. <b>Pisar na areia não "
             "se cobra.</b></p>"),
            ("a", "O que este roteiro não alcança, e está dito",
             "<p><b>A hospedagem</b>, sem diária oficial publicada.</p>"
             "<p><b>O preço dos barcos</b> — Campeche e Costa da Lagoa —, que cada "
             "associação define, sem tabela oficial.</p>"
             "<p><b>Os horários da Ponte Hercílio Luz e do Mercado Público</b>, que não "
             "achamos em fonte oficial.</p>"
             "<p><b>O decreto da tarifa de ônibus</b>: os valores vêm da imprensa.</p>"),
        ],
        "dias_lista": [
            ("Quinta — o centro, e a reserva do Campeche",
             "<b>Antes de tudo, reserve o Campeche</b> no site da Prefeitura, para o "
             "sábado: o voucher só sai 24 horas depois de o pagamento compensar, e não "
             "há devolução — olhe a previsão do mar. Depois, o centro a pé: a <b>Ponte "
             "Hercílio Luz</b>, a ponte pênsil de 1926, se atravessa sem pagar, e o "
             "<b>Mercado Público</b> não cobra entrada. Para circular, o <b>Cartão "
             "Turista</b> — R$ 7,20 a passagem, contra R$ 7,70 no QR Code — e nada de "
             "dinheiro no ônibus.",
             ["Reserve o Campeche hoje",
              "Voucher sai 24h após compensar",
              "Ponte Hercílio Luz · grátis",
              "Mercado Público · grátis",
              "Ônibus · R$ 7,20 no Cartão Turista"]),

            ("Sexta — a Lagoa, a Joaquina e a Costa de barco",
             "<b>A Lagoa da Conceição e as dunas da Joaquina não cobram</b> — e a praia, "
             "por lei federal, nunca. Do Centrinho sai o <b>barco da cooperativa até a "
             "Costa da Lagoa</b>, a vila sem estrada do outro lado: os guias citam "
             "R$ 12,50 a R$ 15 por trecho, sem tabela oficial, e a cooperativa publica "
             "os horários pelo Instagram. Volte antes do último barco.",
             ["Lagoa e Joaquina · grátis",
              "Praia · acesso livre por lei",
              "Barco da Costa · preço sem tabela",
              "Horários pelo Instagram da cooperativa",
              "Morador da Costa paga R$ 2,50"]),

            ("Sábado — a Ilha do Campeche",
             "<b>Com o voucher em mãos</b>, o barco de uma das associações credenciadas: "
             "<b>R$ 185 a R$ 250 por pessoa</b>, segundo a imprensa, mais a taxa "
             "municipal de R$ 15. O acesso à ilha é das <b>9h às 17h</b>, com <b>limite "
             "de 800 visitantes</b>. A ilha é tombada pelo IPHAN e tem a maior "
             "concentração de inscrições rupestres do litoral brasileiro — as trilhas "
             "seguem as regras da equipe de monitores. <b>Mar ruim não dá direito a "
             "devolução.</b>",
             ["Campeche · taxa R$ 15 · sem devolução",
              "Barco · R$ 185 a R$ 250 (imprensa)",
              "Acesso 9h–17h · 800 por dia",
              "Leve o voucher",
              "Siga os monitores nas trilhas"]),

            ("Domingo — o norte, e a fortaleza que pode sair de graça",
             "<b>A Fortaleza de São José da Ponta Grossa</b>, na Praia do Forte, abre "
             "todos os dias das 8h30 às 18h30 e custa <b>R$ 20</b> — <b>R$ 0 se este for "
             "o último domingo do mês, de março a novembro</b>. Paga-se em dinheiro ou "
             "PIX. Quem quer uma das ilhas vai a <b>Santo Antônio de Ratones</b>, de "
             "barco de empresa náutica, com <b>dinheiro em espécie</b> para a portaria; "
             "<b>Anhatomirim está fechada</b>. A tarde é das praias do norte — de graça, "
             "por lei.",
             ["Ponta Grossa · R$ 20 · 8h30–18h30",
              "Último domingo do mês · grátis",
              "Ratones · só dinheiro na portaria",
              "Anhatomirim · fechada",
              "Praias do norte · grátis"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de custos, "
                   "apurados em 7 de novembro de 2026: a regra do Campeche no site "
                   "oficial da Prefeitura, as fortalezas no Departamento das Fortalezas "
                   "da UFSC, a lei das praias no texto federal. <b>A taxa do Campeche, "
                   "o barco e a tarifa de ônibus vêm da imprensa</b>, porque o site da "
                   "Prefeitura só mostra a taxa depois do login e o decreto da tarifa "
                   "não foi achado; estão marcados. <b>Nenhum valor veio de agregador "
                   "de viagem.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
