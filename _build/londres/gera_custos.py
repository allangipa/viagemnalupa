# -*- coding: utf-8 -*-
"""Ficha de custos de Londres: 5 dias, 1 pessoa, libra.

Mesmo molde do gramado/gera_custos.py: SEM HOSPEDAGEM, porque ninguem
publica a diaria media de Londres de graca (o dado e da STR/CoStar).

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
Primeira em libra (£). O schema/ofertas.py e o recortes/comparar.py
aprenderam o simbolo junto com ela.

A ETA (£ 20) entra como custo fixo por pessoa: e obrigatoria para
brasileiro e cobre bebe. Nao e ingresso, mas e conta da viagem.

O metro entra pelo teto diario (tipo "dia"), que e como o cartao por
aproximacao cobra quem anda o dia inteiro. O VALOR do teto (£ 8,90 nas
zonas 1-2) e de fonte secundaria: a pagina de tetos da TfL respondeu com
verificacao anti-robo, e o comunicado oficial so diz que o teto "nao
muda". A linha diz isso.

Buckingham entra SEM valor: no periodo da ficha (novembro) as salas estao
fechadas, e a unica entrada e a visita guiada de £ 100.

Uso
---
    python _build/londres/gera_custos.py
    python _build/londres/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_londres_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

TETO_DIA = 8.90     # zonas 1-2, cartao por aproximacao - fonte secundaria

FICHAS = {
    "londres": {
        "nome": "Londres", "dias": 5, "moeda": "£", "dec": 2,
        "titulo": "Quanto custa 5 dias em Londres em 2026",
        "descricao": ("O custo de 5 dias em Londres, por pessoa, com a ETA de £ 20 que o "
                      "brasileiro paga antes do voo, o trem de Heathrow que subiu em março "
                      "e os museus que não cobram — sem a hospedagem, porque não há diária "
                      "oficial publicada."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas "
                     "nas páginas oficiais em 7 de novembro de 2026. <b>Sem a "
                     "hospedagem</b> — nenhum órgão publica a diária média de Londres, e a "
                     "página explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em "
                  "libra. Mude as datas e o número de pessoas, desmarque o que você não "
                  "vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> O dado de diária média de Londres é da STR/CoStar, pago, e "
            "os números que circulam de graça não batem entre si. Como a regra desta casa "
            "é não estimar, a hospedagem ficou de fora e o total diz isso no próprio "
            "rótulo.<br>"
            "<b>O metrô entra pelo teto diário</b>, multiplicado pelos seus dias. O valor "
            "do teto vem de fonte secundária — a página oficial não abriu —, e a linha "
            "diz isso."),
        "linhas": [
            # ---------------------------------------------------- ingressos
            ("ingresso", 38.00, "Torre de Londres", "£ 38,00",
             "Fonte: tabela de preços da Historic Royal Palaces (hrp.org.uk), consultada "
             "em 7/nov/2026. Coluna <b>“No donation”</b>; com a doação opcional de 10%, "
             "£ 41,80.<br>"
             "De 5 a 17 anos: £ 19,00. Até 4 anos não paga. <b>Morador de Tower Hamlets "
             "paga £ 1,00</b>, na bilheteria."),
            ("ingresso", 32.00, "Abadia de Westminster", "£ 32,00",
             "Fonte: página de horários e preços do site oficial, consultada em "
             "7/nov/2026. De 6 a 17 anos: £ 14. <b>Família de 1 adulto e 1 criança: "
             "£ 32</b>, o preço do adulto.<br>"
             "<b>Comprado no site oficial, o ingresso vira passe anual de graça</b> — três "
             "visitas pelo preço de uma. <b>Domingo só abre para culto.</b>"),
            ("ingresso", 27.00, "Catedral de St Paul's", "£ 27,00",
             "Fonte: página de ingressos do site oficial, consultada em 7/nov/2026, "
             "visita de segunda a sábado fora do verão. <b>£ 24 de 25/jun a 1º/set.</b> "
             "De 6 a 17 anos: £ 10,50.<br>"
             "<b>O culto não cobra.</b> "
             "<span class=\"flag\">Lacuna declarada</span> a página não publica o horário "
             "de visita."),
            ("ingresso", 29.00, "London Eye", "desde £ 29,00",
             "Fonte: página de ingressos do site oficial, consultada em 7/nov/2026: "
             "<i>“From £29”</i> on-line, <b>£ 39 na bilheteria</b>.<br>"
             "<span class=\"flag\">É piso</span> o preço on-line varia com a demanda. "
             "Menor de 2 anos não paga."),
            ("ingresso", 0.00,
             "British Museum, National Gallery e Natural History Museum", "grátis",
             "Fontes: as páginas de visita dos três sites oficiais, consultadas em "
             "7/nov/2026. <b>Os três têm entrada livre</b>; as exposições temporárias "
             "cobram à parte. O British Museum recomenda reservar o ingresso gratuito; a "
             "National Gallery aceita chegar sem reserva."),
            ("ingresso", None, "Palácio de Buckingham por dentro", "só no verão",
             "Fonte: Royal Collection Trust (rct.uk), consultado em 7/nov/2026.<br>"
             "<b>As salas de Estado só abrem no verão</b> — em 2027, de 8/jul a 26/set, "
             "a £ 35 com antecedência. <b>No resto do ano, a única entrada é a visita "
             "guiada da Ala Leste, a £ 100</b>. Por isso esta linha fica fora do total. "
             "A troca da guarda, do lado de fora, não cobra."),
            # ---------------------------------------------------- entrar e circular
            ("fixo", 20.00, "ETA, a autorização eletrônica de viagem", "£ 20,00",
             "Fonte: <b>gov.uk</b>, consultado em 7/nov/2026: para brasileiro em turismo, "
             "<i>“You'll need an electronic travel authorisation (ETA) or a visa”</i>, e "
             "<i>“An ETA costs £20.”</i><br>"
             "<b>Cada pessoa paga a sua, inclusive bebê.</b> Site que cobra mais é "
             "intermediário — o próprio gov.uk avisa."),
            ("fixo", 31.00, "Elizabeth line, Heathrow–centro, ida e volta", "£ 31,00",
             "Fonte: comunicado oficial da <b>TfL</b> de 20/fev/2026: <b>a tarifa da zona "
             "1 a Heathrow passou de £ 13,90 para £ 15,50</b> a partir de 1º de março. A "
             "linha conta ida e volta."),
            ("dia", TETO_DIA, "Metrô e ônibus no teto diário, zonas 1 e 2", "£ 8,90 por dia",
             "<span class=\"flag\">Só em fonte secundária</span> o comunicado oficial da "
             "TfL de 20/fev/2026 diz que <b>os tetos diários não mudam até março de "
             "2027</b>, mas não diz o valor, e a página de tetos da TfL respondeu com "
             "verificação anti-robô. Guias de transporte publicam <b>£ 8,90</b> nas zonas "
             "1 e 2 com cartão por aproximação.<br>"
             "<b>Use o mesmo cartão o dia todo</b>: o teto é por cartão. Quem anda a pé, "
             "desmarca.",
             {"rot": "Metrô e ônibus no teto diário, {d} dias"}),
            # ---------------------------------------------------- taxa
            ("taxa", None, "Taxa turística", "ainda não existe",
             "<span class=\"flag\">Só em fonte secundária</span> o governo britânico deu "
             "aos prefeitos o poder de criar uma taxa por noite, e o de Londres prometeu "
             "teto de 5%. <b>A imprensa britânica não a espera antes de 2028.</b> Fora do "
             "total, porque em 2026 ela não é cobrada."),
        ],
        "rodape_tabela": (
            "Valores em libra, por pessoa, apurados nas páginas oficiais em 7 de novembro "
            "de 2026. <b>Sem a hospedagem</b>, que não tem diária oficial publicada.<br>"
            "<b>Duas coisas mudam esta conta mais que qualquer corte.</b><br>"
            "<b>A primeira: o que é de graça é o melhor da cidade.</b> British Museum, "
            "National Gallery e Natural History Museum não cobram, e a troca da guarda é "
            "na rua. Um roteiro só com eles custa o metrô.<br>"
            "<b>A segunda: a época.</b> O Palácio de Buckingham só abre por dentro no "
            "verão; no resto do ano, a visita guiada custa £ 100."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. Os ingressos vêm das "
            "páginas oficiais da Historic Royal Palaces, da Abadia de Westminster, da "
            "Catedral de St Paul's, do London Eye, do Royal Collection Trust e dos três "
            "museus nacionais. A ETA vem do gov.uk. O transporte vem dos comunicados "
            "oficiais da TfL — <b>a página de tarifas da TfL respondeu com verificação "
            "anti-robô, e não a contornamos</b>; por isso o valor do teto diário está "
            "marcado como fonte secundária. <b>Nenhum valor veio de agregador de "
            "viagem.</b>"),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("londres", "Londres"),
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
