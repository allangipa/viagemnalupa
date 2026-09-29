# -*- coding: utf-8 -*-
"""Ficha de custos de Salvador.

Reusa o renderizador de novos/gera_custos.py, como Porto, Sevilha, Miami
e os demais.

O NUMERO QUE ESTA FICHA EXISTE PARA DIZER
-----------------------------------------
Quatro pontos pagos, R$ 20 cada, total de R$ 80. Mas TRES dos quatro sao
equipamentos municipais, e os equipamentos municipais nao cobram nada as
quartas-feiras.

    Num dia qualquer          R$ 80
    Numa quarta-feira         R$ 20

O unico que continua cobrando na quarta e o Farol da Barra, que e do
Museu Nautico e nao da prefeitura. Essa diferenca de R$ 60 e a maior
economia programavel da cidade, e e o eixo da ficha e do roteiro.

A ARMADILHA DO ELEVADOR LACERDA
-------------------------------
Ele entra como zero, porque hoje esta gratuito - mas NAO e um zero
estavel. As duas paginas oficiais da prefeitura publicam R$ 0,15, a
imprensa apurou gratuidade por tempo limitado, e a tarifa anunciada para
o fim da gratuidade e R$ 1,00.

Tres valores, duas fontes oficiais desatualizadas, e o mais provavel de
mudar durante a validade desta pagina. A linha diz os tres.

O QUE FICA FORA DO TOTAL, E POR QUE
-----------------------------------
Sao Francisco esta fechada para restauro e nao tem preco praticado hoje.
Hospedagem e transporte ficam de fora por falta de fonte oficial
apurada. Mercado Modelo e Porto da Barra sao gratuitos para entrar, e o
que se consome neles nao tem tabela.

Uso
---
    python _build/salvador/gera_custos.py
    python _build/salvador/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base  # noqa: E402

# A armadilha do Porto: o rodape imprime base.APURACAO, que no
# renderizador e a data do novos/dados.py. Sem esta troca a pagina sai
# datada de 17 de setembro sobre uma apuracao de 29.
_s = importlib.util.spec_from_file_location(
    "dados_salvador_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "salvador": {
        "nome": "Salvador", "dias": 5, "moeda": "R$", "dec": 0,
        "titulo": "Quanto custa 5 dias em Salvador em 2026",
        "descricao": ("O custo de 5 dias em Salvador, por pessoa, com os sete museus "
                      "municipais que não cobram nada às quartas-feiras."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 29 de setembro de 2026. <b>Sem a hospedagem</b> — e a página "
                     "explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em real. "
                  "Mude as datas e o número de pessoas, desmarque o que você não vai "
                  "fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Três dos quatro pontos pagos são municipais, e "
            "municipais não cobram nada às quartas-feiras.</b> Desmarque Casa do Carnaval, "
            "Casa do Rio Vermelho e os Espaços do Forte e você vê o total de uma quarta: "
            "<b>R$ 20</b>, só o Farol da Barra, que é do Museu Náutico e cobra os sete "
            "dias. São R$ 60 de diferença por pessoa, e basta escolher o dia. "
            "<b>Esta ficha não tem hospedagem</b>, e isso é deliberado: não apuramos "
            "diária média publicada por órgão oficial para Salvador nesta rodada, e usar "
            "média de agregador seria furar a regra da casa na linha mais cara da viagem. "
            "Linhas marcadas como não apuradas continuam fora do total."),
        "linhas": [
            ("ingresso", 20, "Casa do Carnaval da Bahia", "R$ 20",
             "Inteira. <b>Meia R$ 10</b> para estudante, <b>residente em Salvador</b> e "
             "maior de 60 anos; criança de até 6 anos não paga. <b>Gratuita às "
             "quartas-feiras</b>, para morador e turista, sem restrição. Terça a domingo, "
             "9h às 17h, <b>última entrada às 16h</b>; fecha segunda. Fonte: Prefeitura de "
             "Salvador, 29/set/2026."),
            ("ingresso", 20, "Casa do Rio Vermelho", "R$ 20",
             "Inteira, mesma regra de meia e mesma grade da Casa do Carnaval: terça a "
             "domingo, 9h às 17h, última entrada às 16h, fecha segunda. <b>Gratuita às "
             "quartas.</b> É a casa onde Jorge Amado e Zélia Gattai viveram mais de "
             "cinquenta anos. Fonte: Prefeitura de Salvador, 29/set/2026."),
            ("ingresso", 20, "Espaço Pierre Verger e Espaço Carybé", "R$ 20",
             "<b>Um bilhete só dá acesso aos dois espaços</b>, que ficam no mesmo forte — "
             "é a melhor relação desta ficha, e fica ainda melhor na quarta, quando não "
             "custa nada. Mesma meia de R$ 10. "
             "<span class=\"flag\">Horário não confirmado individualmente</span> a lista "
             "da prefeitura não publica a grade de cada espaço. Fonte: Prefeitura de "
             "Salvador, 29/set/2026."),
            ("ingresso", 20, "Farol da Barra e Museu Náutico da Bahia", "R$ 20",
             "Inteira; meia R$ 10 para estudante, professor e maior de 60. Não pagam "
             "menores de 7, museólogos, arqueólogos, aluno de escola pública, militares, "
             "policiais e pessoa com deficiência mais acompanhante. <b>Atenção: este não "
             "é da prefeitura e NÃO tem quarta gratuita</b> — é o único dos quatro que "
             "cobra na quarta. Em compensação <b>abre todos os dias</b>, 9h às 18h, e "
             "salva a segunda-feira, quando os municipais fecham. Fonte: Museu Náutico da "
             "Bahia, 29/set/2026."),
            ("ingresso", None, "Igreja e Convento de São Francisco", "Fechada para restauro",
             "<span class=\"flag\">Fora do total</span> a página da prefeitura carimba "
             "<b>“FECHADA PARA RESTAURO”</b> no próprio título do verbete, <b>sem data de "
             "reabertura</b>. Quando aberta, a visitação custava R$ 10 pela fonte oficial; "
             "outras fontes registram R$ 5 e R$ 15 para combinados. <b>Nenhum desses "
             "valores é praticado hoje</b>, então nenhum entra na conta. É o ponto mais "
             "vendido do Pelourinho e segue listado como aberto em quase todo guia."),
            ("ingresso", 0, "Elevador Lacerda", "Grátis hoje",
             "<b>E este zero não é estável.</b> As duas páginas oficiais da prefeitura — "
             "o portal de turismo e a secretaria de Mobilidade — publicam <b>R$ 0,15</b>. "
             "A imprensa apurou que o elevador reabriu após obra de mais de R$ 14 milhões "
             "e <b>segue gratuito por tempo limitado</b>, com <b>R$ 1,00</b> anunciado "
             "para quando a gratuidade acabar — alta de cerca de 566%. <b>Três valores, e "
             "as duas fontes oficiais são as desatualizadas.</b> Leve moeda."),
            ("ingresso", 0, "Pelourinho e Centro Histórico", "Grátis",
             "Não existe bilhete: é rua pública. Patrimônio Mundial da UNESCO desde 1985 "
             "e o maior conjunto de arquitetura colonial portuguesa das Américas. O que "
             "cobra são os equipamentos dentro dele, que têm linha própria acima."),
            ("ingresso", 0, "Basílica do Senhor do Bonfim", "Grátis",
             "Igreja em funcionamento, sem bilheteria. Abre todos os dias: segunda a "
             "quinta e sábado das 6h30 às 18h; <b>sexta e domingo das 5h30</b>, porque "
             "sexta é o dia do Senhor do Bonfim e o movimento é muito maior. As fitinhas "
             "são vendidas por ambulantes no largo, e "
             "<span class=\"flag\">não há preço oficial</span> para isso."),
            ("ingresso", 0, "Mercado Modelo", "Grátis",
             "Entrar não custa nada. <span class=\"flag\">Horário não confirmado</span> "
             "não localizamos página oficial com horário publicado. O que se compra "
             "dentro é comércio privado, sem tabela — e a negociação de preço é esperada."),
            ("ingresso", 0, "Praia do Porto da Barra", "Grátis",
             "Bem público, acesso livre 24 horas, ninguém cobra pela areia. Fica "
             "<b>dentro da Baía de Todos os Santos</b>, com água calma e rasa. Cadeira, "
             "guarda-sol e barraca são concessão e comércio privado, "
             "<span class=\"flag\">sem tabela apurada</span>."),
            ("ingresso", 0, "Hospedagem",
             "<span class=\"flag\">Não apurada</span>",
             "<b>Não há diária média oficial de Salvador nesta apuração</b>, e usar média "
             "de agregador seria furar a regra da casa na linha mais cara da viagem. É a "
             "mesma lacuna declarada de Fortaleza, Bariloche, Punta Cana e Miami."),
            ("ingresso", 0, "Transporte urbano e travessias",
             "<span class=\"flag\">Não apurado</span>",
             "Não apuramos tarifa de ônibus, metrô nem das travessias para Itaparica e "
             "Morro de São Paulo. <b>Registre o que a geografia obriga:</b> Bonfim e Rio "
             "Vermelho ficam fora do Centro Histórico e não são caminhada — são "
             "deslocamento, e não estão nesta conta."),
        ],
        "rodape_tabela": ("Valores em real, por pessoa, apurados em 29 de setembro de 2026. "
                          "<b>Quatro linhas estão fora do total</b>: São Francisco, que "
                          "está fechada, mais hospedagem e transporte, que não têm fonte. "
                          "<b>E o total de R$ 80 vira R$ 20 numa quarta-feira</b>, quando "
                          "os três museus municipais não cobram."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": ("Cada linha traz a fonte e a data no próprio campo. <b>A quarta-feira "
                   "gratuita é regra permanente publicada pela Prefeitura de Salvador</b>, "
                   "não promoção — e vale para sete equipamentos municipais, dos quais "
                   "três estão nesta ficha. O Elevador Lacerda é o caso oposto: "
                   "<b>duas páginas oficiais da mesma prefeitura publicam uma tarifa que "
                   "não é mais a praticada</b>, e a página registra as três versões."),
    },
}

# A barra "Calcular para" lista todas as fichas do site, na ordem de
# publicacao. Miami e Salvador entram no fim, na mesma leva.
base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"),
    ("miami", "Miami"), ("salvador", "Salvador"),
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
