# -*- coding: utf-8 -*-
"""Ficha de custos de Bariloche e Punta Cana.

Reusa o renderizador de novos/gera_custos.py - o mesmo que fez Cancun e
Fortaleza. So os dados sao daqui. Duplicar o renderizador significaria duas
fichas que divergem sozinhas com o tempo.

DE ONDE VEM CADA NUMERO
-----------------------
Do novos2/dados.py, que e a apuracao de 17 de setembro de 2026, com fonte
por campo. Nenhum valor foi inventado aqui nem arredondado.

AS DUAS FICHAS SAEM SEM HOSPEDAGEM, e pelo mesmo motivo do Fortaleza: nao
ha diaria media publicada por orgao nenhum para as duas cidades. Procurei
no INDEC, que publica a Encuesta de Ocupacion Hotelera da Argentina, e na
ASONAHORES, que e a associacao hoteleira dominicana. O INDEC anunciou
mudanca na divulgacao da EOH a partir de janeiro de 2026 e nao achei tarifa
media por localidade; a ASONAHORES nao publica ADR aberto por polo.
Inventar uma diaria de agregador seria furar a regra da casa na linha mais
cara da viagem.

VALOR None SIGNIFICA FORA DO TOTAL
----------------------------------
E o mecanismo que o ficha.js ja usa para lacuna declarada. Em Punta Cana
ele carrega quase toda a pagina, e isso e o proprio assunto: tres dos sete
pontos nao tem tarifa unica publicada. O total fica magro de proposito, e
a nota diz por que.

Uso
---
    python _build/novos2/gera_custos.py
    python _build/novos2/gera_custos.py --aplica
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base  # noqa: E402

FICHAS = {
    "bariloche": {
        "nome": "Bariloche", "dias": 5, "moeda": "ARS", "dec": 0,
        "titulo": "Quanto custa 5 dias em Bariloche em 2026",
        "descricao": ("O custo de 5 dias em Bariloche, por pessoa, com a taxa do Parque "
                      "Nacional que não vem dentro do valor da excursão — e sem a "
                      "hospedagem, porque não há diária publicada."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 17 de setembro de 2026. <b>Sem a hospedagem</b> — e a página "
                     "explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em peso "
                  "argentino. Mude as datas e o número de pessoas, desmarque o que você "
                  "não vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> O INDEC publica a Encuesta de Ocupación Hotelera, mas anunciou "
            "mudança na divulgação a partir de janeiro de 2026 e não encontramos tarifa "
            "média por localidade que cubra Bariloche. Preferimos a lacuna escrita a uma "
            "diária de agregador na linha mais cara da viagem. "
            "<b>O transporte também está fora</b>: não apuramos tarifa de ônibus urbano nem "
            "de transfer do aeroporto. Linhas marcadas como não apuradas continuam fora do "
            "total."),
        "linhas": [
            ("ingresso", 35000, "Parque Nacional Nahuel Huapi", "ARS 35.000",
             "Tarifa de <b>estrangeiro não residente, por dia</b>, na tabela publicada no "
             "site oficial do parque (nahuelhuapi.gov.ar), consultada em 17/set/2026. "
             "Residente argentino paga ARS 15.000 e residente de Río Negro, ARS 8.000. "
             "<b>Há 50% de desconto no segundo dia</b>, e o valor acima é o do primeiro. "
             "<span class=\"flag\">Fontes divergem na data de vigência</span> a imprensa "
             "patagônica noticiou 1º de junho de 2026; a página oficial não informa data. "
             "Os valores batem nas duas."),
            ("ingresso", 90000, "Cerro Catedral, passe pedestre", "ARS 90.000",
             "Tabela da Catedral Alta Patagonia, rotulada pela própria página como "
             "<b>TARIFAS 2026</b>, consultada em 17/set/2026. É o passe de quem sobe para "
             "ver a vista. <b>Esquiar é outro preço</b>, ARS 160.000. "
             "<span class=\"flag\">O que não apuramos</span> o cerro opera em duas "
             "temporadas muito diferentes e não achamos tabela separada de verão."),
            ("ingresso", 60000, "Teleférico Cerro Otto", "ARS 60.000",
             "Tarifa de maior de 13 anos, na página do próprio teleférico, consultada em "
             "17/set/2026."),
            ("ingresso", 18000, "Cerro Campanario", "ARS 18.000",
             "Adulto. Criança de 6 a 12 anos paga ARS 10.000. Consultado em 17/set/2026."),
            ("ingresso", 182600, "Isla Victoria e Bosque de Arrayanes", "ARS 182.600",
             "<b>Três cobranças somadas, e só a primeira aparece no anúncio:</b> a excursão "
             "de adulto, mais a taxa portuária, mais a entrada do Parque Nacional. O "
             "operador (islavictoriayarrayanes.com) informa vigência a partir de 1º de "
             "junho de 2026. É o número que mais surpreende quem compara com o anúncio."),
            ("ingresso", 136000, "Puerto Blest e Cascada Los Cántaros", "ARS 136.000",
             "Excursão de dia inteiro pela Turisur, consultada em 17/set/2026, com sinal de "
             "ARS 24.000 na reserva e ARS 112.000 no dia. <b>Não inclui a chegada ao porto, "
             "as taxas nem as refeições</b> — e <b>não inclui a entrada do Parque "
             "Nacional</b>, que está na linha de cima e é cobrada à parte."),
            ("ingresso", 0, "Circuito Chico e Punto Panorámico", "Grátis",
             "O Parque Municipal Llao Llao não cobra entrada. O custo aqui é o do "
             "transporte até lá, que não apuramos."),
            ("ingresso", 0, "Colonia Suiza", "Grátis",
             "Não há bilheteria. A feira acontece às quartas e domingos."),
            ("ingresso", None, "Museo de la Patagonia", "Contribuição",
             "<span class=\"flag\">Sem valor fixo</span> o museu pede contribuição "
             "voluntária, sem tabela publicada. Fica fora do total porque não há número a "
             "somar."),
        ],
        "rodape_tabela": ("Valores em peso argentino, por pessoa, apurados em 17 de setembro "
                          "de 2026. <b>A entrada do Parque Nacional é por dia</b> e aparece "
                          "uma vez só na tabela; quem fizer Puerto Blest e um cerro em dias "
                          "diferentes paga de novo, com 50% de desconto no segundo dia."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e cabanas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": ("Cada linha traz a fonte e a data no próprio campo. As tarifas vêm das "
                   "páginas oficiais do Parque Nacional Nahuel Huapi, da Catedral Alta "
                   "Patagonia, do Teleférico Cerro Otto e dos operadores da Isla Victoria e "
                   "de Puerto Blest. <b>Nenhum valor veio de agregador de viagem.</b> Onde a "
                   "data de vigência não se confirma, isso está dito na própria linha."),
    },

    "punta-cana": {
        "nome": "Punta Cana", "dias": 5, "moeda": "US$", "dec": 0,
        "titulo": "Quanto custa 5 dias em Punta Cana em 2026",
        "descricao": ("O custo de 5 dias em Punta Cana, por pessoa — e por que três dos "
                      "sete pontos não têm tarifa única publicada, o que deixa o total "
                      "menor do que a viagem."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 17 de setembro de 2026. <b>O total aqui é pequeno de propósito</b> "
                     "— e a página explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em dólar. "
                  "Mude as datas e o número de pessoas, desmarque o que você não vai fazer, "
                  "e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Punta Cana é o destino do site com menos tarifa "
            "oficial publicada, e isso muda o que esta ficha pode prometer.</b> Quase tudo "
            "ali é operador privado de excursão, com preço que varia por quem vende. O "
            "Ministerio de Medio Ambiente não publica tarifa de Los Haitises, não existe "
            "tarifa única para a Isla Saona, e o Parque Ojos Indígenas aparece a US$ 50 numa "
            "fonte e a US$ 15 em outra. <b>Três das sete linhas ficam fora do total</b>, com "
            "o motivo escrito. Isso não é defeito da apuração: é como o destino funciona. "
            "A hospedagem também está fora — a ASONAHORES não publica diária média aberta "
            "por polo."),
        "linhas": [
            ("ingresso", 129, "Hoyo Azul e Scape Park", "US$ 129",
             "Admissão geral do Scape Park, que inclui o cenote e as demais atividades do "
             "parque, consultada em 17/set/2026. <b>Só o cenote sai por US$ 65.</b>"),
            ("ingresso", None, "Reserva Ecológica Ojos Indígenas", "US$ 15 ou US$ 50",
             "<span class=\"flag\">Duas fontes, e não escolhemos</span> a reserva aparece a "
             "US$ 50 numa fonte e a US$ 15 em outra, ambas consultadas em 17/set/2026. "
             "Como não há tarifa oficial publicada para desempatar, a linha fica fora do "
             "total e os dois valores ficam na página."),
            ("ingresso", 60, "Altos de Chavón", "US$ 60",
             "Preço de excursão, adulto, consultado em 17/set/2026. Criança de 4 a 12 anos, "
             "US$ 35. <b>Não é bilheteria</b>: é o pacote de quem vai de Punta Cana, e "
             "inclui o transporte de cerca de duas horas."),
            ("ingresso", None, "Isla Saona", "US$ 75 a 135",
             "<span class=\"flag\">Sem tarifa única</span> é excursão compartilhada, e o "
             "preço varia por operador dentro dessa faixa. Fica fora do total porque "
             "escolher um número seria inventar a premissa."),
            ("ingresso", None, "Parque Nacional Los Haitises", "Sem tarifa publicada",
             "<span class=\"flag\">O órgão não publica</span> o Ministerio de Medio Ambiente "
             "não divulga tarifa de entrada. O que se acha é preço de excursão, a partir de "
             "€ 115 com transporte saindo de Punta Cana. Fora do total."),
            ("ingresso", 0, "Playa Bávaro", "Grátis",
             "<b>O acesso é garantido por lei.</b> A legislação dominicana declara as praias "
             "de uso público, inclusive as que ficam em frente a resorts."),
            ("ingresso", 0, "Playa Macao", "Grátis",
             "A praia pública mais aberta da região. Não há bilheteria."),
        ],
        "rodape_tabela": ("Valores em dólar, por pessoa, apurados em 17 de setembro de 2026. "
                          "<b>Três linhas estão fora do total</b> por falta de tarifa única "
                          "publicada, e estão marcadas na tabela. O total é o que dá para "
                          "somar com fonte, não o que a viagem custa."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "resorts e hotéis"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": ("Cada linha traz a fonte e a data no próprio campo. <b>Punta Cana é o "
                   "destino com menos tarifa oficial do site</b>: onde só existe preço de "
                   "operador, isso está dito, e onde duas fontes divergem, as duas ficam. "
                   "Nenhum número foi escolhido por conveniência nem tirado por média."),
    },
}

# A barra "Calcular para" lista todas as fichas do site. As duas novas
# entram no fim, na ordem em que foram publicadas.
base.CIDADES = base.CIDADES + [("bariloche", "Bariloche"), ("punta-cana", "Punta Cana")]
base.FICHAS = FICHAS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
