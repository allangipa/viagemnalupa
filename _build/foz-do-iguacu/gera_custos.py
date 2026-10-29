# -*- coding: utf-8 -*-
"""Ficha de custos de Foz do Iguacu: 3 dias, 1 pessoa, real.

Mesmo molde do gramado/gera_custos.py, e SEM HOSPEDAGEM pelo mesmo motivo:
nenhum orgao publica diaria media de Foz, e a casa nao estima.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
Uma linha em peso argentino numa ficha em real. O Parque Nacional Iguazu
cobra AR$ 60.000 de visitante internacional; a linha converte pela taxa de
venda do boletim de fechamento do BCB de 23/10/2026 (ARS 0,003299), o mesmo
arquivo do /comparar/ e de Bariloche:

    60.000 x 0,003299 = 197,94

O IOF do cartao fica fora da conta e dito na linha: a bilheteria aceita
cartao ou peso em dinheiro, e quem leva peso nao paga IOF.

O Parque Nacional do Iguacu entra pela faixa Brasil/Mercosul (R$ 121), a do
leitor do site; a integral (R$ 134) esta dita na linha.

O onibus urbano entra como 8 viagens a R$ 5,00: aeroporto-hotel, Cataratas
ida e volta, Itaipu ida e volta, Marco ida e volta, hotel-aeroporto. O
onibus para a Argentina nao tem preco publicado e fica fora, dito.

Uso
---
    python _build/foz-do-iguacu/gera_custos.py
    python _build/foz-do-iguacu/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_foz_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

ARS_VENDA = 0.003299            # BCB, boletim de fechamento de 23/10/2026
IGUAZU = round(60000 * ARS_VENDA, 2)
assert IGUAZU == 197.94, IGUAZU

FICHAS = {
    "foz-do-iguacu": {
        "nome": "Foz do Iguaçu", "dias": 3, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 3 dias em Foz do Iguaçu em 2026",
        "descricao": ("O custo de 3 dias em Foz do Iguaçu, por pessoa, com as Cataratas "
                      "dos dois lados — o argentino cobra de brasileiro o preço de "
                      "estrangeiro —, Itaipu e o Parque das Aves, sem a hospedagem, "
                      "porque não há diária oficial publicada."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas "
                     "nas páginas oficiais em 29 de outubro de 2026. <b>Sem a "
                     "hospedagem</b> — nenhum órgão publica a diária média de Foz do "
                     "Iguaçu, e a página explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 3 dias, 1 pessoa, valores em "
                  "real. Mude as datas e o número de pessoas, desmarque o que você não "
                  "vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> Nenhum órgão publica a diária média de Foz do Iguaçu — o "
            "Panorama da Hotelaria Brasileira não traz a cidade, e a Secretaria de "
            "Turismo publica só a ocupação. Como a regra desta casa é não estimar, a "
            "hospedagem ficou de fora e o total diz isso no próprio rótulo.<br>"
            "<b>Uma linha está em peso argentino</b>: o lado argentino das Cataratas, "
            "AR$ 60.000, convertido pela taxa de venda do boletim de fechamento do "
            "Banco Central de 23/out/2026."),
        "linhas": [
            # ---------------------------------------------------- ingressos
            ("ingresso", 121.00, "Parque Nacional do Iguaçu, Brasil/Mercosul", "R$ 121,00",
             "Fonte: site oficial (cataratasdoiguacu.com.br), tabela de 2026 publicada em "
             "19/12/2025, consultada em 29/out/2026: R$ 118,00 de ingresso + R$ 3,00 do "
             "Fundo Iguaçu, <b>que é voluntário</b>.<br>"
             "Integral, para quem vem de fora do Mercosul: <b>R$ 134,00</b>. Até 6 anos "
             "não paga.<br>"
             "<span class=\"flag\">Sem meia-entrada</span> o parque é federal, e a "
             "própria página diz que não tem meia nem desconto adicional: idoso e "
             "estudante pagam R$ 121."),
            ("ingresso", IGUAZU, "Parque Nacional Iguazú (Argentina)", "AR$ 60.000 · R$ 197,94",
             "Fonte: tabela oficial (iguazuargentina.com e Administración de Parques "
             "Nacionales), vigente desde 1/jun/2026, consultada em 29/out/2026. "
             "<b>Visitantes internacionais: AR$ 60.000</b>, com o trem até a Garganta "
             "do Diabo.<br>"
             "<span class=\"flag\">Sem tarifa Mercosul</span> o brasileiro paga como "
             "qualquer estrangeiro — 64% a mais que o lado brasileiro.<br>"
             "Em real pela taxa de venda do boletim de fechamento do Banco Central de "
             "23/out/2026 (AR$ 1 = R$ 0,003299). <b>A bilheteria aceita cartão ou "
             "peso argentino em dinheiro</b>; no cartão brasileiro entra o IOF, que não "
             "está nesta linha. <b>O segundo dia sai pela metade.</b>"),
            ("ingresso", 384.00, "Macuco Safari", "R$ 384,00",
             "Fonte: site oficial (macucosafari.com.br), consultado em 29/out/2026. Cerca "
             "de 2 horas, 25 a 30 minutos de barco, saídas a cada 20 minutos.<br>"
             "<b>Não inclui a entrada do Parque Nacional</b>, que é a linha de cima. "
             "R$ 192,00 de 7 a 11 anos, brasileiro acima de 60, estudante e morador da "
             "região. <b>É a linha mais cara da ficha:</b> quem não vai, desmarca."),
            ("ingresso", 110.00, "Parque das Aves", "R$ 110,00",
             "Fonte: página de valores do site oficial (parquedasaves.com.br), consultada "
             "em 29/out/2026. Meia: R$ 55,00. Até 8 anos não paga.<br>"
             "<b>A página avisa: “Preços válidos até 30/11/2026.”</b> Estacionamento "
             "R$ 60,00 a diária, fora desta linha."),
            ("ingresso", 63.00, "Itaipu Panorâmica", "R$ 63,00",
             "Fonte: site oficial do Turismo Itaipu (turismoitaipu.com.br), consultado em "
             "29/out/2026. Cerca de 1h10, só por fora, todos os dias das 8h15 às 17h.<br>"
             "O passeio por dentro, <b>Itaipu Especial, custa R$ 185,00</b>; o Refúgio "
             "Biológico, R$ 48,00, e fecha na terça. Meia de estudante só para "
             "instituição brasileira. <b>Dinheiro, só em real.</b>"),
            ("ingresso", 60.00, "Marco das Três Fronteiras", "R$ 60,00",
             "Fonte: site oficial (marcodastresfronteiras.com.br), consultado em "
             "29/out/2026: R$ 57 + R$ 3 do Fundo Iguaçu. Reduzida: R$ 31,50.<br>"
             "<span class=\"flag\">Fontes divergem</span> a página diz que a reduzida "
             "vale para estudante e professor “brasileiros” no quadro e “do estado do "
             "Paraná” na nota.<br>"
             "<b>Terça a domingo, 14h às 21h: fecha na segunda.</b>"),
            ("ingresso", 0.00, "Templo Budista Chen Tien", "grátis",
             "<span class=\"flag\">Só em fonte secundária</span> não achamos página "
             "oficial; os guias de viagem concordam que a entrada é gratuita e que o "
             "templo fecha na segunda. O horário de fechamento aparece como 16h30 e "
             "como 17h."),
            # ---------------------------------------------------- transporte
            ("fixo", 40.00, "Ônibus urbano, 8 viagens", "R$ 40,00",
             "Fonte: <b>Secretaria Municipal de Turismo</b> (destino.foz.br), consultada "
             "em 29/out/2026: <i>“O valor da tarifa é de R$ 5,00”</i>.<br>"
             "Oito viagens: aeroporto–hotel, Cataratas ida e volta, Itaipu ida e volta, "
             "Marco ida e volta, hotel–aeroporto.<br>"
             "<b>Pode ir a R$ 6:</b> o novo modelo de concessão levado a consulta "
             "pública em agosto de 2026 prevê essa tarifa. Quem vai de carro, desmarca."),
            ("fixo", None, "Ônibus até as Cataratas argentinas", "não publicado",
             "Duas empresas, Crucero del Norte e Río Uruguay, saem do Terminal de "
             "Transporte Urbano todos os dias das 7h às 19h, segundo a Secretaria de "
             "Turismo. <span class=\"flag\">Lacuna declarada</span> <b>a página não "
             "publica o preço.</b> Fora do total."),
            # ---------------------------------------------------- taxa
            ("taxa", None, "Taxa de turismo dos hotéis", "sem lei nem valor achados",
             "Hotéis associados ao Visit Iguassu cobram uma “taxa de turismo” na "
             "recepção, segundo a imprensa do setor. <span class=\"flag\">Lacuna "
             "declarada</span> <b>não achamos lei municipal que a crie nem o valor "
             "publicado.</b> Se aparecer na conta, pergunte se é obrigatória. "
             "<b>Fora do total.</b>"),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, apurados nas páginas oficiais em 29 de outubro "
            "de 2026. <b>Sem a hospedagem</b>, que não tem diária oficial publicada, e "
            "<b>sem o ônibus até a Argentina</b>, que não tem preço publicado.<br>"
            "<b>Duas linhas mudam esta conta mais que qualquer corte.</b><br>"
            "<b>A primeira: o Macuco Safari</b>, R$ 384, mais de um terço do total. É "
            "opcional, e as Cataratas se veem inteiras sem ele.<br>"
            "<b>A segunda: o lado argentino</b>, que cobra em peso e muda com o câmbio. "
            "A R$ 197,94 de 23 de outubro, já custa 64% a mais que o lado brasileiro."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. Os ingressos vêm das "
            "páginas oficiais de cada atração — Parque Nacional do Iguaçu, Parque "
            "Nacional Iguazú e a Administración de Parques Nacionales, Macuco Safari, "
            "Parque das Aves, Turismo Itaipu, Marco das Três Fronteiras. A tarifa de "
            "ônibus vem da Secretaria Municipal de Turismo; o câmbio do peso, do boletim "
            "de fechamento do Banco Central do Brasil. <b>Nenhum valor veio de agregador "
            "de viagem.</b> O Templo Budista é a exceção declarada: só achamos guias de "
            "viagem, e a linha diz isso. As páginas lidas estão guardadas com data."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("foz-do-iguacu", "Foz do Iguaçu"),
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
