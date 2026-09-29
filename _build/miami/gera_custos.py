# -*- coding: utf-8 -*-
"""Ficha de custos de Miami.

Reusa o renderizador de novos/gera_custos.py, como Porto, Sevilha,
Cancun, Fortaleza, Bariloche e Punta Cana.

O NUMERO QUE ESTA FICHA EXISTE PARA DIZER
-----------------------------------------
O Everglades cobra US$ 100 POR PESSOA de quem nao mora nos Estados
Unidos, desde 1 de janeiro de 2026. Isso nao e detalhe: e a maior linha
da tabela, maior que o zoologico e o museu de ciencias somados.

UMA LIMITACAO DA CALCULADORA, DECLARADA EM VEZ DE ESCONDIDA
-----------------------------------------------------------
A entrada do Everglades tem duas partes com regras diferentes:

    US$ 35   por VEICULO, uma vez, vale 7 dias
    US$ 100  por PESSOA de 16 anos ou mais, nao residente

O ficha.js soma ingresso POR PESSOA. Os US$ 100 entram certos e escalam
certo. Os US$ 35 nao tem tipo que os modele - nao sao por pessoa, nao sao
por dia e nao sao por noite. Se entrassem como ingresso, um casal veria
US$ 270 onde a verdade e US$ 235.

Entao os US$ 35 entram com valor None, que e o mecanismo de lacuna
declarada que o ficha.js ja usa, e a linha explica a conta. A ficha
prefere somar de menos e dizer por que, a somar errado em silencio.

O QUE MAIS FICA FORA DO TOTAL, E POR QUE
-----------------------------------------
Vizcaya e Wynwood Walls cobram e nao publicam tabela - as duas vendem por
widget de reserva. Hospedagem fica fora porque nao apuramos ADR oficial
de Miami nesta rodada, e usar media de agregador seria furar a regra da
casa na linha mais cara. Transporte fica fora pelo mesmo motivo.

Sao cinco linhas fora do total numa tabela de onze. O total e o que da
para somar com fonte, nao o que a viagem custa - e a pagina diz isso.

Uso
---
    python _build/miami/gera_custos.py
    python _build/miami/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base  # noqa: E402

# A ARMADILHA DO PORTO, E ELA MORDEU AQUI NA PRIMEIRA RODADA.
#
# O rodape imprime base.APURACAO, que no renderizador e a data do
# novos/dados.py - 17 de setembro. A primeira versao desta ficha saiu
# publicando "Tarifas verificadas em 17 de setembro de 2026" sobre uma
# apuracao de 29 de setembro. Nada quebra, nada avisa: so a data sai
# errada, que e o pior tipo de erro num site cuja promessa e a data.
_s = importlib.util.spec_from_file_location(
    "dados_miami_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "miami": {
        "nome": "Miami", "dias": 5, "moeda": "US$", "dec": 2,
        "titulo": "Quanto custa 5 dias em Miami em 2026",
        "descricao": ("O custo de 5 dias em Miami, por pessoa, com o adicional de US$ 100 "
                      "dos Everglades para quem não mora nos EUA."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 29 de setembro de 2026. <b>Sem a hospedagem</b> — e a página "
                     "explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em "
                  "dólar. Mude as datas e o número de pessoas, desmarque o que você não "
                  "vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">O adicional do Everglades escala por pessoa, "
            "e a entrada do veículo não.</b> Os US$ 100 são cobrados de cada "
            "não-residente de 16 anos ou mais, e a calculadora os multiplica certo. Os "
            "US$ 35 do carro são cobrados uma vez, valem 7 dias e <b>estão fora do "
            "total</b>: não existe tipo nesta calculadora que os modele, e somá-los por "
            "pessoa daria um número errado. Some US$ 35 uma vez, qualquer que seja o "
            "número de ocupantes. "
            "<b>Esta ficha também não tem hospedagem</b>, e isso é deliberado: não "
            "apuramos diária média publicada por órgão oficial para Miami nesta rodada, "
            "e em Miami a diária anunciada não é o que se paga — faltam de 13% a 14% de "
            "impostos e a resort fee diária. Linhas marcadas como não apuradas "
            "continuam fora do total."),
        "linhas": [
            ("ingresso", 100, "Everglades, adicional de não-residente", "US$ 100",
             "<b>Por pessoa de 16 anos ou mais que não mora nos Estados Unidos</b>, em "
             "vigor desde <b>1º de janeiro de 2026</b>. O Everglades é um dos "
             "<b>onze parques nacionais</b> com essa cobrança, ao lado de Grand Canyon, "
             "Yellowstone, Yosemite e Zion. Fonte: página central do NPS sobre o "
             "adicional de não-residente, consultada em 29/set/2026.<br>"
             "<b>Os oito dias de entrada gratuita do ano não isentam você</b>: o texto do "
             "NPS diz que, a partir de 2026, a gratuidade vale apenas para cidadãos e "
             "residentes americanos."),
            ("ingresso", None, "Everglades, entrada do veículo", "US$ 35 por carro",
             "<span class=\"flag\">Fora do total</span> <b>é por veículo, não por "
             "pessoa</b>, e esta calculadora soma por pessoa. Vale <b>7 dias corridos</b> "
             "nas três entradas do parque. <b>Some US$ 35 uma vez</b>, sejam um ou quatro "
             "ocupantes. Pedestre ou ciclista paga US$ 20 em vez disso; menor de 16 não "
             "paga. <b>O parque não aceita dinheiro</b>, só cartão. Fonte: nps.gov/ever, "
             "29/set/2026."),
            ("ingresso", 30, "Zoo Miami", "US$ 30",
             "<b>Preço a partir de 1º de outubro de 2026</b>, com imposto já incluído — "
             "esta apuração é de 29 de setembro e pega a virada. <b>Até 30 de setembro o "
             "adulto custava US$ 25,95 mais imposto.</b> Criança de 3 a 12 anos paga "
             "US$ 26; até 2 anos não paga; sênior de 65 ou mais tem 25% de desconto com "
             "documento. Fonte: zoomiami.org, 29/set/2026."),
            ("ingresso", 29.95, "Frost Science", "A partir de US$ 29,95",
             "<b>Piso publicado para adulto.</b> <span class=\"flag\">Preço variável</span> "
             "o museu escreve que o valor muda conforme o dia da visita — o número aqui é "
             "o menor anunciado, não o de uma data qualquer. Jovem de 4 a 11 anos a partir "
             "de US$ 24,95; até 3 anos não paga. <b>Um ingresso só cobre exposições, "
             "aquário e uma sessão do planetário.</b> Fonte: frostscience.org, "
             "29/set/2026."),
            ("ingresso", 18, "Pérez Art Museum Miami", "US$ 18",
             "Adulto. Sênior de 62 ou mais, estudante e jovem de 7 a 18 pagam US$ 14; até "
             "6 anos não paga. <b>É gratuito para todos nas quintas depois das 17h</b>, e "
             "o museu fica aberto até as 21h nesse dia — <b>quem puder encaixar a quinta "
             "à noite tira esta linha inteira da conta</b>. Fonte: pamm.org, 29/set/2026."),
            ("ingresso", None, "Vizcaya Museum and Gardens", "US$ 24 a US$ 39",
             "<span class=\"flag\">Sem tabela publicada</span> o Vizcaya vende por tipo de "
             "visita, num widget de reserva, e não publica preço por faixa etária. A "
             "própria página descreve a faixa acima. <b>Não há número único para somar</b>, "
             "e não inventamos um. Associado paga US$ 10 e criança de até 5 anos não paga. "
             "Fonte: vizcaya.org, 29/set/2026."),
            ("ingresso", None, "Wynwood Walls", "Cobra, sem valor publicado",
             "<span class=\"flag\">Preço não publicado</span> a página de admissões não "
             "mostra valor: o total só aparece depois de escolher data e quantidade. "
             "Criança de menos de 12 anos não paga, mas precisa de ingresso emitido. "
             "<b>O bairro de Wynwood em volta é rua aberta e não custa nada</b> — o que se "
             "paga é o recinto fechado. Fonte: thewynwoodwalls.com, 29/set/2026."),
            ("ingresso", 0, "Little Havana e a Calle Ocho", "Grátis",
             "Não existe bilheteria: é bairro e via pública. O Parque do Dominó também é "
             "público. O que custa é o que se consome, e isso não apuramos."),
            ("ingresso", 0, "South Beach e o Art Deco District", "Grátis",
             "A praia é pública e as ruas do conjunto art déco se veem andando. <b>A "
             "visita guiada da Miami Design Preservation League é paga</b>, e "
             "<span class=\"flag\">não apuramos a tarifa</span> em fonte oficial. Cadeira "
             "e guarda-sol na areia são concessão privada dos hotéis."),
            ("ingresso", 0, "Hospedagem",
             "<span class=\"flag\">Não apurada</span>",
             "<b>Não há diária média oficial de Miami nesta apuração</b>, e usar média de "
             "agregador seria furar a regra da casa na linha mais cara da viagem. E aqui "
             "seria pior que em outros destinos: <b>a diária anunciada não é o que se "
             "paga</b>. Somam-se de <b>13% a 14% de impostos</b> — e a composição muda "
             "conforme o bairro — mais uma <b>resort fee diária</b> de US$ 25 a US$ 60. "
             "A ficha do guia detalha as duas coisas."),
            ("ingresso", 0, "Transporte urbano e aluguel de carro",
             "<span class=\"flag\">Não apurado</span>",
             "Não apuramos tarifa de Metromover, Metrorail, ônibus nem diária de locadora. "
             "<b>Mas registre o que a geografia obriga:</b> Everglades e Zoo Miami ficam "
             "longe e não têm ligação fácil por transporte público. O carro que leva ao "
             "parque é o mesmo que paga os US$ 35 da linha acima."),
        ],
        "rodape_tabela": ("Valores em dólar, por pessoa, apurados em 29 de setembro de 2026. "
                          "<b>Cinco linhas estão fora do total</b>, todas marcadas na "
                          "tabela: a entrada do veículo no Everglades, Vizcaya, Wynwood "
                          "Walls, hospedagem e transporte. O total é o que dá para somar "
                          "com fonte, não o que a viagem custa."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis em Miami e Miami Beach"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": ("Cada linha traz a fonte e a data no próprio campo. <b>O adicional de "
                   "não-residente do Everglades é o número mais importante desta página</b>, "
                   "e vale ler a ficha do parque no guia: <b>duas páginas oficiais do NPS "
                   "se contradizem</b> sobre qual passe dispensa a cobrança, numa diferença "
                   "de US$ 180. Registramos as duas e não escolhemos nenhuma."),
    },
}

# A barra "Calcular para" lista todas as fichas do site. A lista do
# renderizador base parou nas dez primeiras; as cinco seguintes foram
# acrescentadas por cada gerador, o que deixou cada pagina publicada com
# uma barra congelada na data em que nasceu. Aqui entram todas, na ordem
# de publicacao, e o layout/vizinhos.py sincroniza as demais depois.
base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
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
