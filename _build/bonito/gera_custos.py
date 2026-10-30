# -*- coding: utf-8 -*-
"""Ficha de custos de Bonito: 4 dias, 1 pessoa, real.

Mesmo molde do fernando-de-noronha/gera_custos.py, e SEM HOSPEDAGEM.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
O total leva so o que tem fonte oficial: a TCA da prefeitura e o tarifario
publicado pelo Nascente Azul. Os outros atrativos tem preco tabelado, mas
nao publicado pelo atrativo nem pela prefeitura; o valor de agencia aparece
na observacao da linha, marcado como fonte secundaria, e a linha fica fora
do total (valor None). Decisao do Allan em 29/10/2026.

A TCA entra como linha fixa de 4 dias de passeio (R$ 60): a prefeitura cobra
so os dias "em que ha visitacao em atrativos", e o roteiro tem passeio nos
quatro.

Uso
---
    python _build/bonito/gera_custos.py
    python _build/bonito/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_bonito_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

SEC = '<span class="flag">Só em fonte secundária</span> '
AG = "tabela de 2026 de uma agência credenciada (Acqua Viagens, atualizada em 16/fev/2026)"

FICHAS = {
    "bonito": {
        "nome": "Bonito", "dias": 4, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 4 dias em Bonito em 2026",
        "descricao": ("O custo de 4 dias em Bonito, por pessoa, com o que tem preço "
                      "oficial — a taxa ambiental e o Nascente Azul — e os outros passeios "
                      "pelo preço de agência, marcado e fora do total. Sem a hospedagem."),
        "abertura": ("A conta do que tem preço oficial, por pessoa, conferida em 29 de "
                     "outubro de 2026. <b>Em Bonito o preço é tabelado, mas quase nenhum "
                     "atrativo o publica</b>: os outros passeios aparecem com o preço de "
                     "agência, marcado, e ficam fora do total. <b>Sem a hospedagem</b>, que "
                     "não tem diária oficial publicada."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 4 dias, 1 pessoa, valores em "
                  "real, baixa temporada. Mude as datas e o número de pessoas, desmarque "
                  "o que você não vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">O total tem só o que tem fonte oficial.</b> "
            "Em Bonito todo passeio tem preço tabelado, igual em qualquer agência — mas o "
            "atrativo não o publica. Achamos em fonte oficial a TCA da prefeitura e o "
            "tarifário do Nascente Azul; <b>Rio da Prata, Gruta do Lago Azul, Balneário "
            "Municipal e Abismo Anhumas aparecem com o preço de agência, marcado, e ficam "
            "fora da soma</b>.<br>"
            "<b>Esta ficha não tem hospedagem nem traslado</b>: nenhum dos dois tem "
            "tabela oficial."),
        "linhas": [
            ("fixo", 60.00, "Taxa de Conservação Ambiental, 4 dias de passeio", "R$ 60,00",
             "Fonte: <b>Prefeitura de Bonito</b>, nota informativa de 19/11/2025, "
             "consultada em 29/out/2026: <b>R$ 15 por pessoa por dia</b>, desde "
             "20/12/2025. <b>Conta só os dias com passeio</b> — <i>“dias em que há "
             "visitação em atrativos”</i>. Menor de 7 não paga. Paga-se no portal "
             "turistapornatureza.com.br, antes dos vouchers."),
            ("ingresso", 374.00, "Nascente Azul, flutuação + day-use", "R$ 374,00",
             "Fonte: tarifário publicado pelo atrativo (nascenteazul.com.br), válido até "
             "12/12/2026, consultado em 29/out/2026. <b>Baixa temporada; R$ 462 na "
             "alta.</b><br>"
             "<b>Morador de MS: R$ 337. Morador de Bonito: R$ 162</b>, só na baixa. "
             "<b>Na baixa temporada fecha na terça.</b>"),
            ("ingresso", None, "Recanto Ecológico Rio da Prata, flutuação",
             "R$ 470 (agência)",
             SEC + "o site do Rio da Prata não publica preço. Na " + AG + ": <b>R$ 470 "
             "na baixa, R$ 570 na alta</b>, validade até 31/12/2026. <b>Fora do "
             "total.</b> Idade mínima 5 anos, diz o site."),
            ("ingresso", None, "Gruta do Lago Azul", "R$ 120 (agência)",
             SEC + "a prefeitura administra a Gruta e não publica o preço. Na " + AG +
             ": R$ 120 na baixa, R$ 180 na alta — <b>com validade até 30/06/2026, já "
             "vencida</b>. <b>Fora do total.</b>"),
            ("ingresso", None, "Balneário Municipal", "R$ 70 (agência)",
             SEC + "o Balneário é da prefeitura, que não publica o preço. Na " + AG +
             ": R$ 70 na baixa, R$ 98 na alta — <b>validade até 30/06/2026, já "
             "vencida</b>. <b>Fora do total.</b>"),
            ("ingresso", None, "Abismo Anhumas, flutuação", "R$ 1.598 (agência)",
             SEC + "o site do Abismo não publica preço. Na " + AG + ": <b>R$ 1.598</b>, na "
             "baixa e na alta, validade até 28/02/2027. O mais caro daquela tabela. "
             "<b>Fora do total.</b>"),
            ("fixo", None, "Traslado aos atrativos", "sem tabela oficial",
             "<span class=\"flag\">Lacuna declarada</span> os atrativos ficam fora da "
             "cidade e o traslado é vendido pela agência com o voucher, <b>sem tabela "
             "oficial</b>. Fora do total."),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, baixa temporada, conferidos em 29 de outubro de "
            "2026. <b>O total tem só o que tem fonte oficial</b>: a TCA e o Nascente Azul. "
            "<b>Os preços de agência estão nas observações, marcados, e fora da soma.</b> "
            "Sem a hospedagem e sem o traslado.<br>"
            "<b>Somados os preços de agência</b> — Rio da Prata, Gruta e Balneário na "
            "baixa —, a viagem passaria de R$ 434 para R$ 1.094, sem o Abismo."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. A TCA vem da nota oficial "
            "da Prefeitura de Bonito; o Nascente Azul, do tarifário publicado pelo próprio "
            "atrativo. <b>Os outros preços vêm da tabela de uma agência credenciada</b>, "
            "porque o atrativo e a prefeitura não os publicam — estão marcados como fonte "
            "secundária e fora do total. As páginas lidas estão guardadas com data."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("foz-do-iguacu", "Foz do Iguaçu"),
    ("fernando-de-noronha", "Fernando de Noronha"), ("bonito", "Bonito"),
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
