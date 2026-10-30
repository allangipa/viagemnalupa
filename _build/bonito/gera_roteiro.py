# -*- coding: utf-8 -*-
"""Roteiro de 4 dias em Bonito, montado pelo voucher.

Mesmo molde do fernando-de-noronha/gera_roteiro.py.

O QUE DECIDE A ORDEM
--------------------
    antes    a TCA e paga no portal da prefeitura e so depois a agencia
             emite os vouchers: nada se compra na porta
    terca    na baixa temporada o Nascente Azul fecha ("de quarta-feira a
             segunda-feira"); o roteiro poe a flutuacao no domingo
    dias     a TCA conta so os dias com passeio; o roteiro tem passeio nos
             quatro, R$ 60

POR QUE ESTA ORDEM (sexta a segunda)
------------------------------------
    sexta    chegada e o Balneario Municipal, perto da cidade
    sabado   Rio da Prata (idade minima 5 anos)
    domingo  Nascente Azul, que na baixa temporada fecharia na terca
    segunda  Gruta do Lago Azul de manha e a volta

Uso
---
    python _build/bonito/gera_roteiro.py
    python _build/bonito/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_bonito_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "bonito": {
        "dias": 4,
        "titulo": "Roteiro de 4 dias em Bonito",
        "descricao": ("Quatro dias em Bonito na ordem que o voucher e o calendário "
                      "permitem: a taxa paga antes, o Nascente Azul fora da terça e um "
                      "passeio por dia."),
        "abertura": ("Quatro dias de sexta a segunda, com um passeio por dia — e "
                     "<b>nenhum comprado na porta</b>: em Bonito a taxa ambiental se paga "
                     "antes, num portal da prefeitura, e cada passeio sai num voucher de "
                     "agência, com data e hora. <b>O preço é tabelado, mas quase nenhum "
                     "atrativo o publica</b>; onde o valor vem de agência, o roteiro "
                     "diz."),
        "avisos": [
            ("a", "Nada se compra na porta: taxa primeiro, voucher depois",
             "<p>Todo passeio de Bonito é vendido por <b>agência credenciada</b>, com "
             "<b>voucher</b> de data e horário. O preço de cada atrativo é o mesmo em "
             "qualquer agência.</p>"
             "<p>Antes dos vouchers vem a <b>TCA</b>, a Taxa de Conservação Ambiental: "
             "<b>R$ 15 por pessoa por dia de passeio</b>, paga no portal "
             "turistapornatureza.com.br. Menor de 7 não paga.</p>"
             "<p><b>Só conta dia com passeio</b>: chegar à noite e só jantar não "
             "gera taxa.</p>"),
            ("b", "O preço é tabelado — e quase ninguém oficial o publica",
             "<p>O <b>Nascente Azul</b> publica o tarifário: <b>R$ 374</b> a flutuação na "
             "baixa temporada, <b>R$ 462</b> na alta, <b>R$ 162</b> para quem mora em "
             "Bonito.</p>"
             "<p>O <b>Rio da Prata</b>, o <b>Abismo Anhumas</b> e a prefeitura — que "
             "administra a <b>Gruta do Lago Azul</b> e o <b>Balneário Municipal</b> — não "
             "publicam. Os valores desses quatro, neste roteiro, vêm da tabela de uma "
             "agência e estão marcados. <b>Dois deles, Gruta e Balneário, aparecem com "
             "validade vencida em 30/06/2026.</b></p>"),
            ("a", "Na baixa temporada o Nascente Azul fecha na terça",
             "<p>A página do Nascente Azul: <b>alta temporada, todos os dias, 7h às 17h; "
             "baixa, de quarta a segunda, 8h às 16h</b>.</p>"
             "<p>A temporada segue o calendário do Conselho Municipal de Turismo, mas a "
             "página mostra o de 2025. <b>Pergunte à agência em que temporada cai a sua "
             "data</b> — muda o preço e o dia de folga.</p>"),
            ("b", "O que este roteiro não alcança, e está dito",
             "<p><b>A hospedagem</b>, que nenhum órgão publica.</p>"
             "<p><b>O traslado</b> aos atrativos, que ficam fora da cidade e são "
             "vendidos com o voucher, sem tabela oficial.</p>"
             "<p><b>O preço oficial do Rio da Prata, da Gruta, do Balneário e do "
             "Abismo</b>, que o atrativo ou a prefeitura não publicam.</p>"),
        ],
        "dias_lista": [
            ("Sexta — a chegada e o Balneário Municipal",
             "<b>TCA paga e vouchers emitidos antes de sair de casa.</b> À tarde, o "
             "<b>Balneário Municipal</b>, da prefeitura, perto da cidade. "
             "<span class=\"flag\">Só em fonte secundária</span> a prefeitura não publica "
             "o preço; na tabela de uma agência, <b>R$ 70</b> na baixa temporada, com "
             "validade vencida em junho. O dia já conta R$ 15 de TCA.",
             ["TCA · R$ 15 por dia de passeio",
              "Vouchers · antes da viagem",
              "Balneário Municipal · agência R$ 70",
              "Preço · sem fonte oficial"]),

            ("Sábado — a flutuação do Rio da Prata",
             "O <b>Recanto Ecológico Rio da Prata</b> fica em Jardim, fora de Bonito — o "
             "traslado sai com o voucher. <b>Idade mínima: 5 anos</b>, e <b>começou, não "
             "tem reembolso</b>, mesmo se o passeio não for até o fim, diz o próprio "
             "site. <span class=\"flag\">Só em fonte secundária</span> o site não publica "
             "preço; na tabela de uma agência, <b>R$ 470</b> na baixa, R$ 570 na alta.",
             ["Rio da Prata · agência R$ 470",
              "Idade mínima · 5 anos",
              "Sem reembolso depois de começar",
              "Traslado · com o voucher"]),

            ("Domingo — o Nascente Azul",
             "<b>Flutuação + day-use no Nascente Azul</b>, no km 22 da rodovia para "
             "Bodoquena: <b>R$ 374</b> na baixa temporada, <b>R$ 462</b> na alta, pelo "
             "tarifário do próprio atrativo, válido até 12/12/2026. Quem mora em MS paga "
             "R$ 337; em Bonito, R$ 162. <b>É domingo porque na baixa temporada o "
             "Nascente Azul fecha na terça.</b> O restaurante do atrativo cobra R$ 94 o "
             "adulto.",
             ["Nascente Azul · R$ 374 baixa · R$ 462 alta",
              "Morador de Bonito · R$ 162",
              "Fecha na terça na baixa",
              "Restaurante · R$ 94"]),

            ("Segunda — a Gruta do Lago Azul e a volta",
             "<b>Gruta do Lago Azul de manhã</b>, administrada pela prefeitura. "
             "<span class=\"flag\">Só em fonte secundária</span> o preço não é publicado "
             "pela prefeitura; na tabela de uma agência, <b>R$ 120</b> na baixa, R$ 180 "
             "na alta — com validade vencida em junho de 2026. Depois, a volta. Quatro "
             "dias de passeio: <b>R$ 60 de TCA</b>.",
             ["Gruta do Lago Azul · agência R$ 120",
              "Validade · vencida em 30/06/2026",
              "TCA · R$ 60 nos quatro dias"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de custos, "
                   "conferidos em 29 de outubro de 2026. <b>Têm fonte oficial</b> a TCA "
                   "(Prefeitura de Bonito) e o Nascente Azul (tarifário do atrativo). "
                   "<b>Vêm da tabela de uma agência credenciada</b>, marcados, os preços "
                   "do Rio da Prata, da Gruta do Lago Azul e do Balneário Municipal. "
                   "Ficaram sem resposta a hospedagem e o traslado."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
