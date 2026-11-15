# -*- coding: utf-8 -*-
"""Ficha de custos de Sao Paulo: 5 dias, 1 pessoa, real.

Mesmo molde do salvador/gera_custos.py: COM HOSPEDAGEM, pela diaria media
da FOHB/HotelInvest (Panorama 20a ed., p. 26-27, texto guardado em
fontes/fohb-panorama-20-sao-paulo.txt). Valores reais de dez/2025.

O QUE ESTA FICHA TEM DE DIFERENTE
---------------------------------
Os sete museus pagos (R$ 261,20) tem, todos, janela gratis - em dias
diferentes. O roteiro de quarta a domingo pega seis delas, e os ingressos
caem para R$ 25 (so o Museu do Futebol, que so nao cobra na terca).

O metro entra em 10 viagens - suposicao desta ficha, dita na linha. O
aeroporto entra pela Linha 13-Jade da CPTM a R$ 5,40, a tarifa do quadro
oficial; o Expresso nao tem valor proprio publicado.

Uso
---
    python _build/sao-paulo/gera_custos.py
    python _build/sao-paulo/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_sao_paulo_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "sao-paulo": {
        "nome": "São Paulo", "dias": 5, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 5 dias em São Paulo em 2026",
        "descricao": ("O custo de 5 dias em São Paulo, por pessoa, com a diária média dos "
                      "hotéis da cidade e os sete museus pagos — que, cada um no seu dia, não "
                      "cobram nada."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas em "
                     "15 de novembro de 2026. <b>Com hospedagem</b>: a diária média dos hotéis "
                     "de São Paulo em 2025, da FOHB, a mesma fonte das fichas do Rio e de "
                     "Salvador."),
        "hosp": [
            {"k": "media", "rot": "Média da cidade em 2025 (FOHB)", "ref": 602, "mn": 508, "mx": 706},
            {"k": "baixa", "rot": "Janeiro, o mês mais barato (FOHB)", "ref": 508, "mn": 508, "mx": 508},
            {"k": "alta", "rot": "Novembro, o mês mais caro (FOHB)", "ref": 706, "mn": 706, "mx": 706},
        ],
        "hospPadrao": "media",
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em real. "
                  "Mude as datas e o número de pessoas, troque a época da hospedagem, "
                  "desmarque o que você não vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Os sete museus pagos somam R$ 261,20, e todos "
            "têm uma janela grátis — em dias diferentes.</b> Terça: MASP, Língua Portuguesa "
            "e Futebol. Quarta: Ipiranga e Afro Brasil. Sexta à noite: MASP. Sábado: "
            "Pinacoteca. Domingo: MAM e Língua Portuguesa. <b>Uma viagem de quarta a domingo "
            "pega seis dos sete</b>, e os ingressos caem para <b>R$ 25</b>: só o Museu do "
            "Futebol, que só não cobra na terça. "
            "<b style=\"color:var(--gelo)\">A hospedagem é a média dos hotéis de São Paulo "
            "em 2025, da FOHB.</b> Por quarto, duas pessoas por quarto; troque para janeiro, "
            "o mês mais barato, ou novembro, o mais caro — na capital, o ano corporativo é o "
            "caro, e as férias são baratas."),
        "linhas": [
            # ---------------------------------------------------- ingressos
            ("ingresso", 85.00, "MASP", "R$ 85,00",
             "Inteira; meia R$ 42 para estudante, professor e maior de 60. <b>Grátis às "
             "terças e na sexta a partir das 18h</b>, com agendamento on-line obrigatório "
             "também nos dias grátis. Fecha segunda. Fonte: masp.org.br, 15/nov/2026."),
            ("ingresso", 40.00, "Pinacoteca", "R$ 40,00",
             "Inteira; meia R$ 20; on-line, mais R$ 2 de taxa. Um ingresso vale para os três "
             "prédios no mesmo dia. <b>Maior de 60 não paga.</b> <b>Grátis aos sábados e no "
             "segundo domingo do mês.</b> <b>Fecha às terças</b> e abre na segunda. Fonte: "
             "pinacoteca.org.br, 15/nov/2026."),
            ("ingresso", 25.00, "Museu da Língua Portuguesa", "R$ 25,00",
             "Inteira; meia R$ 12,50. <b>Grátis às terças e aos domingos</b> — não mais aos "
             "sábados, como dizem os guias antigos. Ingresso obrigatório mesmo grátis. Fecha "
             "segunda. Fonte: museudalinguaportuguesa.org.br, 15/nov/2026."),
            ("ingresso", 25.00, "Museu do Futebol", "R$ 25,00",
             "Inteira; meia R$ 12,50; até 7 anos não paga. <b>Grátis às terças</b>; na "
             "primeira terça do mês, aberto até 21h. Fecha segunda. Comprando aqui pelo "
             "Sympla, a Língua Portuguesa sai pela metade até 30/dez/2026. Fonte: "
             "museudofutebol.org.br, 15/nov/2026."),
            ("ingresso", 30.00, "Museu do Ipiranga", "R$ 30,00",
             "<span class=\"flag\">Plataforma de venda indicada pelo museu</span> o site do "
             "museu não publica valor em reais; a Fever, para onde ele manda, dá R$ 30 e "
             "R$ 15 a meia, 15/nov/2026. <b>Grátis às quartas e no primeiro domingo do "
             "mês</b>, só retirando na bilheteria no dia — o grátis não se agenda. Fecha "
             "segunda; os jardins abrem todo dia, de graça."),
            ("ingresso", 41.20, "MAM", "R$ 41,20",
             "R$ 40 mais R$ 1,20 de taxa da Eventim; meia R$ 20,60. <b>Grátis aos "
             "domingos.</b> Fecha segunda. Fonte: mam.org.br, 15/nov/2026."),
            ("ingresso", 15.00, "Museu Afro Brasil", "R$ 15,00",
             "Inteira; meia R$ 7,50. <b>Grátis às quartas.</b> Terça a domingo, 10h às 17h. "
             "Fonte: museuafrobrasil.org.br, 15/nov/2026."),
            ("ingresso", 0.00, "Theatro Municipal, visita guiada", "grátis",
             "Gratuita, com ingresso pela INTI liberado <b>na véspera, a partir das 10h</b>. "
             "Em português, de terça a sexta; sábado só em inglês, para estrangeiros. Fonte: "
             "theatromunicipal.org.br, 15/nov/2026."),
            ("ingresso", 0.00, "Paulista, Ibirapuera, Mercadão e Beco do Batman", "grátis",
             "A Paulista fecha para carros aos domingos e feriados, <b>das 9h às 16h</b> "
             "(Subprefeitura Sé). O Ibirapuera e o Beco são públicos; o Mercadão não cobra "
             "entrada, e não tem horário oficial publicado."),
            # ---------------------------------------------------- transporte
            ("fixo", 54.00, "Metrô e trem, 10 viagens", "R$ 54,00",
             "<b>R$ 5,40 a viagem desde 6/jan/2026</b> (governo do estado e quadro da CPTM). "
             "<b>Dez viagens é suposição desta ficha, não dado.</b> O Bilhete 24 horas custa "
             "R$ 20,50. <b>No domingo, o ônibus municipal não cobra</b> (SPTrans); metrô e "
             "trem cobram."),
            ("fixo", 10.80, "Aeroporto de Guarulhos, ida e volta de trem", "R$ 10,80",
             "Linha 13-Jade da CPTM, R$ 5,40 por trecho pelo quadro oficial. "
             "<span class=\"flag\">Sem tarifa própria publicada</span> o Expresso Aeroporto "
             "não tem valor separado em página oficial de 2026. O ônibus executivo da EMTU "
             "custa R$ 45,50 na página do serviço, e mais em algumas linhas."),
            # ---------------------------------------------------- taxa
            ("taxa", None, "Taxa turística", "não achada",
             "<b>Não achamos taxa turística na capital</b>, nem por hóspede nem por "
             "visitante. <span class=\"flag\">Lacuna declarada</span> ausência não se prova "
             "com documento. Fora do total."),
            # ---------------------------------------------------- cama
            ("hosp", None, "Hospedagem, 4 noites", "R$ 2.408,00",
             "Fonte: <b>FOHB e HotelInvest</b>, <i>Panorama da Hotelaria Brasileira</i>, 20ª "
             "edição, páginas 26 e 27: diária média (ADR) dos hotéis de São Paulo em 2025, "
             "<b>R$ 602 por quarto por noite</b>, com 62,6% de ocupação, em valores "
             "corrigidos para dez/2025, consultado em 15/nov/2026. A mesma fonte das fichas do "
             "Rio e de Salvador.<br>"
             "<b>A série mensal vai de R$ 508 em janeiro a R$ 706 em novembro</b>: o "
             "relatório põe os melhores meses entre setembro e novembro, pelo calendário de "
             "feiras e congressos.<br>"
             "<span class=\"flag\">Ressalva</span> é a média dos hotéis do painel, da cidade "
             "inteira, sem recorte por bairro. O aluguel por temporada fica perto de R$ 233 de "
             "diária, no mesmo relatório."),
        ],
        "rodape_tabela": (
            "Valores em real, por pessoa, apurados em 15 de novembro de 2026. <b>A taxa "
            "turística está fora</b>, porque não achamos nenhuma.<br>"
            "<b>Duas coisas mudam esta conta mais que qualquer corte.</b><br>"
            "<b>A primeira: os dias grátis.</b> Os sete museus somam R$ 261,20; de quarta a "
            "domingo, pelo roteiro, viram R$ 25.<br>"
            "<b>A segunda: o mês.</b> A mesma diária vai de R$ 508 em janeiro a R$ 706 em "
            "novembro — R$ 792 de diferença em quatro noites."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. Os ingressos vêm das páginas "
            "oficiais de cada museu; o do Ipiranga, da plataforma de venda que o próprio "
            "museu indica, e está marcado. As tarifas de transporte vêm do governo do estado, "
            "da CPTM e da SPTrans. A diária vem do Panorama da Hotelaria Brasileira, da FOHB "
            "e da HotelInvest. <b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"), ("granada", "Granada"), ("barcelona", "Barcelona"),
    ("gramado", "Gramado"), ("londres", "Londres"), ("florianopolis", "Florianópolis"),
    ("sao-paulo", "São Paulo"),
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
