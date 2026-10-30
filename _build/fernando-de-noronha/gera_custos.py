# -*- coding: utf-8 -*-
"""Ficha de custos de Fernando de Noronha: 5 dias, 1 pessoa, real.

Mesmo molde do foz-do-iguacu/gera_custos.py, e SEM HOSPEDAGEM: nenhum orgao
publica diaria media de Noronha, e a casa nao estima.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
O total e quase so taxa. Os dois numeros oficiais da ilha sao cobrancas, nao
passeios: a TPA (Distrito) e o ingresso do Parque (ICMBio). O que se faz
depois disso - barco, mergulho, condutor de trilha - e de empresa privada
sem tabela oficial, e fica fora, dito linha a linha. Como Punta Cana, o total
fica magro de proposito.

A TPA entra como linha fixa de 5 dias, R$ 520,50, da tabela oficial. Ela e
progressiva e nao e por noite: o ficha.js nao sabe recalcular, e a linha diz
para conferir a tabela quem muda as datas. 5 e nao 4 porque a pagina nao diz
se chegada e partida contam; usamos o maior.

O ingresso do Parque entra pelo valor da pagina oficial em 29/10/2026,
R$ 192; a linha diz que muda para R$ 196,50 em 1/11/2026, segundo a
imprensa citando o ICMBio.

Uso
---
    python _build/fernando-de-noronha/gera_custos.py
    python _build/fernando-de-noronha/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_noronha_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "fernando-de-noronha": {
        "nome": "Fernando de Noronha", "dias": 5, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 5 dias em Fernando de Noronha em 2026",
        "descricao": ("O custo de 5 dias em Fernando de Noronha, por pessoa: R$ 712,50 só "
                      "de taxa ambiental e ingresso do Parque, antes de qualquer passeio — "
                      "sem a hospedagem, porque não há diária oficial publicada."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas "
                     "nas páginas oficiais em 29 de outubro de 2026. <b>Sem a "
                     "hospedagem</b> — nenhum órgão publica a diária média da ilha, e a "
                     "página explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em "
                  "real. Mude as datas e o número de pessoas, desmarque o que você não "
                  "vai fazer, e a conta se refaz na hora — <b>menos a TPA</b>, que é "
                  "progressiva e está fixa em 5 dias."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> Nenhum órgão publica a diária média de Fernando de "
            "Noronha. Como a regra desta casa é não estimar, a hospedagem ficou de fora "
            "e o total diz isso no próprio rótulo.<br>"
            "<b>A TPA está fixa em 5 dias (R$ 520,50).</b> A tabela oficial é "
            "progressiva — barateia por dia até o 10º e dispara no 11º —, e a calculadora "
            "não a recalcula pelas datas. Para outra permanência, use a tabela no guia."),
        "linhas": [
            ("fixo", 520.50, "Taxa de Preservação Ambiental, 5 dias", "R$ 520,50",
             "Fonte: <b>Administração do Distrito Estadual de Fernando de Noronha</b> "
             "(noronha.pe.gov.br), tabela de permanência da TPA 2026, consultada em "
             "29/out/2026. 4 dias: R$ 423,17. 7 dias: R$ 672,85. 10 dias: R$ 901,36.<br>"
             "<span class=\"flag\">Lacuna declarada</span> a página não diz se o dia da "
             "chegada e o da partida contam; <b>usamos 5 dias para 4 noites, o "
             "maior</b>.<br>"
             "<b>Dia excedente não agendado é cobrado em dobro.</b>"),
            ("ingresso", 192.00, "Ingresso do Parque Nacional Marinho", "R$ 192,00",
             "Fonte: <b>ICMBio</b> (parnanoronha.com.br/visitante), consultada em "
             "29/out/2026, Portaria 4.423/2025: R$ 192 para brasileiro, R$ 384 para o "
             "público geral, <b>válido por 10 dias</b>. Menor de 12 e brasileiro acima de "
             "60 não pagam.<br>"
             "<span class=\"flag\">Muda em 1º de novembro</span> R$ 196,50 para "
             "brasileiro a partir de 1º/11/2026, segundo a imprensa citando o ICMBio "
             "(Brasilturis, 27/out/2026)."),
            ("ingresso", 0.00, "Sancho, Golfinhos, Porcos, Leão e Sueste", "incluído no ingresso do Parque",
             "Fonte: ICMBio, página de atrativos, consultada em 29/out/2026. Já pagos "
             "pelo ingresso do Parque. <b>A escada do Sancho tem horário de descer e de "
             "subir</b>; <b>no Sueste o banho está proibido</b>; na Baía dos Golfinhos "
             "não se desce."),
            ("ingresso", 0.00, "Trilha da Atalaia, agendada", "incluído no ingresso do Parque",
             "Fonte: ICMBio. Vaga por dia e horário pela maré baixa; <b>sem o número do "
             "ingresso não se agenda</b>. Dispensa condutor. Colete, máscara e snorkel "
             "obrigatórios; protetor solar proibido antes do banho."),
            ("ingresso", 0.00, "Praias de acesso livre", "grátis",
             "Fonte: ICMBio, página de visitação: Cacimba do Padre, Bode, Americano, "
             "Boldró, Conceição, Meio, Cachorro e Porto de Santo Antônio <i>não "
             "precisam de ingresso</i>. A TPA vale do mesmo jeito."),
            ("ingresso", None, "Condutor das trilhas longas", "não publicado",
             "Capim-Açu, Pontinha–Caieira, Atalaia–Pontinha–Caieira e Morro São José a "
             "nado exigem condutor credenciado pelo ICMBio. <span class=\"flag\">Lacuna "
             "declarada</span> <b>o serviço é privado e o ICMBio não publica o "
             "preço.</b> Fora do total."),
            ("fixo", None, "Passeio de barco", "não publicado",
             "Só empresas autorizadas pelo Parque fazem; o ingresso é conferido no "
             "Porto de Santo Antônio. <span class=\"flag\">Lacuna declarada</span> "
             "<b>o preço é de cada empresa, sem tabela oficial.</b> Fora do total."),
            ("fixo", None, "Ônibus da ilha", "sem tarifa oficial",
             "<span class=\"flag\">Só em fonte secundária</span> não achamos a tarifa em "
             "página da Administração; guias de viagem citam R$ 5, o mais recente de "
             "2024. Fora do total."),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, apurados nas páginas oficiais em 29 de outubro "
            "de 2026. <b>Sem a hospedagem</b>, que não tem diária oficial publicada, e "
            "<b>sem barco, condutor e ônibus</b>, que não têm preço em fonte "
            "oficial.<br>"
            "<b>O total é quase só taxa, e isso é o achado:</b> R$ 520,50 de TPA e R$ 192 "
            "de Parque, antes de qualquer passeio.<br>"
            "<b>O que mais muda a conta é quantos dias você fica.</b> Até o 10º dia, cada "
            "dia a mais de TPA custa menos; o 11º custa R$ 126,95, mais que o primeiro."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. A TPA vem da tabela "
            "oficial da Administração do Distrito Estadual de Fernando de Noronha; o "
            "ingresso, as regras de cada praia e as trilhas, das páginas do ICMBio do "
            "Parque Nacional Marinho. O reajuste de 1º de novembro vem da imprensa, "
            "citando o ICMBio. <b>Nenhum valor veio de agregador de viagem.</b> As "
            "páginas lidas estão guardadas com data."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("foz-do-iguacu", "Foz do Iguaçu"),
    ("fernando-de-noronha", "Fernando de Noronha"),
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
