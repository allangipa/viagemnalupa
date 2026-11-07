# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Londres, montado pelo calendario.

Mesmo molde do gramado/gera_roteiro.py.

O QUE O CALENDARIO DECIDE
-------------------------
    seg, qua, sex  a troca da guarda em Buckingham (novembro de 2026,
                   calendario da Household Division), 11h, gratis
    sexta          British Museum ate 20h30 e National Gallery ate 21h:
                   a noite de sexta e dos museus gratuitos
    domingo        a Abadia de Westminster so abre para culto - por isso
                   ela fica num dia util
    sabado         a Abadia fecha a visita as 15h no sabado consultado

POR QUE SEGUNDA A SEXTA
-----------------------
    segunda  Westminster: a troca da guarda as 11h e a Abadia a tarde
    terca    a Torre de Londres de manha, St Paul's a tarde
    quarta   South Kensington: Natural History Museum, gratis
    quinta   a margem sul: London Eye no fim da tarde
    sexta    British Museum e National Gallery, os dois abertos a noite

Uso
---
    python _build/londres/gera_roteiro.py
    python _build/londres/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_londres_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "londres": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Londres",
        "descricao": ("Cinco dias em Londres na ordem que o calendário permite: a troca "
                      "da guarda que não é todo dia, a Abadia que fecha para turista no "
                      "domingo e a sexta em que os museus gratuitos abrem à noite."),
        "abertura": ("Cinco dias de segunda a sexta, porque <b>a troca da guarda só "
                     "acontece em dias alternados</b>, <b>a Abadia de Westminster só abre "
                     "para culto no domingo</b> e <b>a sexta é a noite em que o British "
                     "Museum e a National Gallery ficam abertos até tarde</b> — e não "
                     "cobram."),
        "avisos": [
            ("a", "A ETA se paga antes de embarcar — e cada pessoa paga a sua",
             "<p>O gov.uk responde, para brasileiro em turismo: <b>“You'll need an "
             "electronic travel authorisation (ETA) or a visa.”</b> A ETA custa "
             "<b>£ 20</b> e vale para estadias de até 6 meses.</p>"
             "<p><b>Bebê e criança também precisam</b> — <i>“Each person travelling needs "
             "an ETA, including babies and children.”</i> Uma família de quatro paga "
             "£ 80.</p>"
             "<p>Peça no gov.uk ou no aplicativo oficial. <b>Site que cobra mais é "
             "intermediário</b>, e o próprio governo avisa.</p>"),
            ("b", "Buckingham por dentro só no verão — no resto do ano, £ 100",
             "<p>As salas de Estado do Palácio de Buckingham <b>só abrem no verão</b>: em "
             "2027, de <b>8 de julho a 26 de setembro</b>, a £ 35 com compra "
             "antecipada.</p>"
             "<p><b>De outubro a junho, a única entrada é a visita guiada da Ala Leste, a "
             "£ 100 por pessoa</b>, em datas escolhidas.</p>"
             "<p>Este roteiro é de novembro, e por isso <b>vê o palácio por fora</b>, na "
             "troca da guarda, que não cobra.</p>"),
            ("a", "A troca da guarda não é todo dia",
             "<p>No calendário oficial da Household Division para novembro de 2026, a "
             "troca da guarda em Buckingham é <b>segunda, quarta e sexta, às 11h</b>.</p>"
             "<p><b>As paradas de domingo, às 10h, são outra coisa.</b> E o calendário não "
             "diz se a cerimônia é cancelada com chuva: confira no próprio dia.</p>"),
            ("b", "O metrô cobra por teto diário — no mesmo cartão",
             "<p>Com cartão por aproximação, o metrô e o ônibus <b>param de cobrar quando "
             "chegam ao teto do dia</b>. A TfL diz que os tetos <b>não mudam até março de "
             "2027</b>; o valor, <b>£ 8,90 nas zonas 1 e 2</b>, é de guias de transporte, "
             "porque a página oficial não abriu.</p>"
             "<p><b>O teto é por cartão.</b> Quem alterna dois cartões, ou o cartão e o "
             "celular, paga dois tetos.</p>"
             "<p><b>A Elizabeth line até Heathrow custa £ 15,50 desde março</b> — subiu "
             "£ 1,60 de uma vez.</p>"),
            ("a", "O que este roteiro não alcança, e está dito",
             "<p><b>A hospedagem</b>: nenhum órgão publica a diária média de Londres, e a "
             "ficha fica sem ela em vez de estimar.</p>"
             "<p><b>O horário de visita da St Paul's</b>, que a página de ingressos não "
             "traz.</p>"
             "<p><b>O preço final do London Eye</b>, que muda com a demanda: £ 29 é o "
             "piso on-line, e na hora custa £ 39.</p>"
             "<p><b>A tarifa de ônibus depois de 1º de novembro</b>: a TfL anunciou "
             "£ 1,85, e não conseguimos confirmar na página de tarifas.</p>"),
        ],
        "dias_lista": [
            ("Segunda — a troca da guarda e a Abadia",
             "<b>Às 11h, a troca da guarda em Buckingham</b>, de graça, na rua — em "
             "novembro ela é segunda, quarta e sexta. Chegue antes: o lugar na grade é de "
             "quem chega primeiro. Atravesse o St James's Park até <b>Westminster</b> e, "
             "à tarde, a <b>Abadia</b>: <b>£ 32</b> o adulto, £ 14 de 6 a 17 anos, e "
             "<b>a família de 1 adulto e 1 criança paga £ 32</b>. Compre no site oficial "
             "e peça na Abadia para virar <b>passe anual, de graça</b>. <b>É segunda "
             "porque no domingo ela só abre para culto.</b>",
             ["Troca da guarda · 11h · grátis",
              "Só segunda, quarta e sexta",
              "Abadia · £ 32 · criança de 1+1 grátis",
              "Ingresso do site vira passe anual",
              "Domingo a Abadia é só culto"]),

            ("Terça — a Torre de manhã, St Paul's à tarde",
             "<b>A Torre de Londres</b> custa <b>£ 38</b> na coluna “No donation”; a "
             "outra coluna, com a doação opcional de 10%, dá £ 41,80 — confira qual está "
             "no carrinho. Inclui as Joias da Coroa e a visita com os Yeoman Warders. "
             "Morador do bairro paga £ 1, e isso diz bastante sobre quem financia o "
             "monumento. À tarde, a pé ou de metrô, a <b>Catedral de St Paul's</b>: "
             "<b>£ 27</b> fora do verão. <b>O culto não cobra</b> — quem quer ver a nave "
             "sem pagar, vai na hora da missa.",
             ["Torre de Londres · £ 38 · doação opcional",
              "Até 4 anos não paga",
              "St Paul's · £ 27 · culto grátis",
              "Horário de visita não publicado",
              "Mesmo cartão o dia todo"]),

            ("Quarta — South Kensington, de graça",
             "<b>O Natural History Museum</b> não cobra: <i>“Our galleries are free to "
             "explore.”</i> Abre às 10h e a última entrada é às 17h30. <b>Reserve o "
             "ingresso gratuito</b> se for em dia cheio, senão é fila. Na mesma rua estão "
             "outros museus nacionais. <b>Às 11h há troca da guarda de novo</b>, para "
             "quem perdeu a de segunda.",
             ["Natural History Museum · grátis",
              "10h–17h50 · última entrada 17h30",
              "Ingresso gratuito evita fila",
              "Troca da guarda · 11h · quarta",
              "Fecha 24 a 26/dez"]),

            ("Quinta — a margem sul e o London Eye no fim da tarde",
             "<b>O London Eye</b> é o único ponto do roteiro com preço que muda: "
             "<b>desde £ 29 on-line</b>, e <b>£ 39 na bilheteria</b>. Compre antes, para "
             "o fim da tarde, quando a cidade acende. Menor de 2 anos não paga. A margem "
             "sul do Tâmisa, entre o London Eye e a Tower Bridge, se faz a pé.",
             ["London Eye · desde £ 29 on-line",
              "£ 39 na bilheteria",
              "Preço muda com a demanda",
              "Margem sul a pé · grátis",
              "Menor de 2 não paga"]),

            ("Sexta — os dois maiores museus, até tarde e de graça",
             "<b>Sexta é a noite dos museus gratuitos.</b> O <b>British Museum</b> fica "
             "aberto até <b>20h30</b> e a <b>National Gallery</b> até <b>21h</b> — os dois "
             "sem cobrar entrada. Comece pelo British Museum, com o ingresso gratuito "
             "reservado, e feche a noite na National Gallery, em Trafalgar Square. "
             "<b>Às 11h, a última troca da guarda da semana.</b> Para Heathrow, a "
             "<b>Elizabeth line custa £ 15,50</b> desde março de 2026.",
             ["British Museum · grátis · até 20h30",
              "National Gallery · grátis · até 21h",
              "Reserve o gratuito do British",
              "Troca da guarda · 11h · sexta",
              "Elizabeth line · £ 15,50 até Heathrow"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de custos, "
                   "apurados em 7 de novembro de 2026 nas páginas oficiais de cada "
                   "monumento e museu, no Royal Collection Trust, no calendário da "
                   "Household Division, no gov.uk e nos comunicados da TfL. <b>A página "
                   "de tarifas da TfL respondeu com verificação anti-robô, e não a "
                   "contornamos</b>; o valor do teto diário do metrô está marcado como "
                   "fonte secundária. <b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
