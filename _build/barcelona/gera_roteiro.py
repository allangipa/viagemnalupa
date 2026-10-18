# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Barcelona, montado pelo calendario.

Mesmo molde do granada/gera_roteiro.py.

O ACHADO DESTE ROTEIRO: A SEMANA TEM TRES TARDES GRATIS, E ELAS CABEM
---------------------------------------------------------------------
    quinta   Museu Picasso, 16h-19h, reserva que abre 4 dias antes   12 EUR
    sabado   MNAC, a partir das 15h                                  12 EUR
    domingo  Castell de Montjuic, a partir das 15h                   12 EUR

De quinta a segunda sao cinco dias, e os tres caem dentro. Granada tinha
duas gratuidades a cinco dias uma da outra e nao cabia as duas; Barcelona
tem tres em quatro dias e cabe todas. E o primeiro domingo do mes libera
os tres o dia inteiro.

POR QUE QUINTA, SEXTA, SABADO, DOMINGO E SEGUNDA
-------------------------------------------------
    quinta   Gotic e Catedral de manha, Palau ao meio-dia, Picasso as
             16h de graca (a reserva se faz na segunda anterior, as 10h)
    sexta    Sagrada Familia com hora marcada; Sant Pau a dez minutos a
             pe, depois das 14h, quando custa 1 EUR a menos
    sabado   Park Guell de manha (30 minutos de tolerancia); MNAC a
             partir das 15h, de graca, no mesmo morro do dia seguinte
    domingo  Casa Batllo de manha; Castell de Montjuic a partir das
             15h, de graca, subindo de funicular que esta no bilhete
             simples
    segunda  o dia em que Picasso e MNAC fecham - e por isso fica para
             La Pedrera e o museu do Barca, que abrem

A ARMADILHA DE PLANEJAMENTO QUE MAIS PEGA
------------------------------------------
A reserva gratuita do Picasso abre QUATRO DIAS ANTES, as 10h, e o museu
tem lotacao limitada. Quem descobre a quinta gratis ja em Barcelona
disputa as vagas que sobraram. Por isso o aviso "b" existe, e por isso
e o segundo.

Uso
---
    python _build/barcelona/gera_roteiro.py
    python _build/barcelona/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_barcelona_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "barcelona": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Barcelona",
        "descricao": ("Cinco dias em Barcelona na ordem que o calendário permite: as "
                      "três tardes grátis da semana, a Sagrada Família com hora marcada "
                      "e a segunda-feira que fecha os museus."),
        "abertura": ("Cinco dias organizados pelo calendário, que em Barcelona vale "
                     "€ 36: <b>Picasso não cobra na quinta à tarde, o MNAC no sábado à "
                     "tarde e o Castell de Montjuïc no domingo à tarde — e uma viagem de "
                     "quinta a segunda pega as três.</b> A segunda-feira, em que os "
                     "museus fecham, fica para o que abre."),
        "avisos": [
            ("a", "Três tardes grátis em três dias — e elas cabem numa viagem de cinco",
             "<p>Barcelona tem <b>três</b> entradas gratuitas em tardes fixas da semana, "
             "e elas são vizinhas.</p>"
             "<p><b>Quinta-feira, das 16h às 19h:</b> Museu Picasso, por reserva. "
             "<b>Vale € 12.</b></p>"
             "<p><b>Sábado, a partir das 15h:</b> MNAC, reservando on-line. <b>Vale "
             "€ 12.</b></p>"
             "<p><b>Domingo, a partir das 15h:</b> Castell de Montjuïc. <b>Vale "
             "€ 12.</b></p>"
             "<p><b>De quinta a domingo vão quatro dias.</b> Uma viagem de cinco que "
             "comece numa quinta pega as três — é o que este roteiro faz. <b>E no "
             "primeiro domingo do mês os três são gratuitos o dia inteiro</b>, com "
             "reserva no Picasso e no MNAC.</p>"
             "<p>O Sant Pau não entra nessa conta: o primeiro domingo lá é só para "
             "maiores de 65 em grupo organizado. O que ele tem é <b>€ 1 a menos depois "
             "das 14h</b>.</p>"),
            ("b", "A reserva grátis do Picasso abre quatro dias antes, às 10h — faça de casa",
             "<p>O site do museu é direto: <b>“Free-of-charge times: four days before "
             "the visit, from 10 am onwards.”</b> E avisa que <b>o museu tem lotação "
             "limitada</b>.</p>"
             "<p><b>Para a quinta à tarde, a reserva se faz na segunda-feira anterior, "
             "a partir das 10h de Barcelona</b> — 5h da manhã em Brasília. Quem "
             "descobre a gratuidade já na cidade disputa o que sobrou.</p>"
             "<p>A mesma regra vale para o primeiro domingo do mês e para as noites de "
             "verão (quinta, sexta e sábado das 19h às 21h, de 31 de março a 27 de "
             "setembro).</p>"
             "<p><b>O MNAC também pede reserva on-line para a entrada gratuita</b>, mas "
             "não publica antecedência. <b>Montjuïc não pede.</b></p>"),
            ("a", "A Sagrada Família é nominativa e não devolve — e o Park Güell dá 30 minutos",
             "<p><b>São as duas regras mais duras do roteiro, e as duas estão no "
             "fim de semana.</b></p>"
             "<p><b>Sagrada Família:</b> ingresso <b>nominativo, pessoal e "
             "intransferível</b> (cláusula 4.2 das condições de venda), com "
             "<b>documento original</b> conferido na entrada. <b>Sem troca nem "
             "devolução</b> — só se o ingresso não foi validado e o problema for do "
             "monumento. Hora marcada, <b>sem tolerância publicada</b>. Quem sai não "
             "entra de novo. Só se vende on-line.</p>"
             "<p><b>Park Güell:</b> <b>30 minutos depois da hora marcada, o direito de "
             "entrar se perde.</b> Dentro, fica o tempo que quiser; fora, não volta. "
             "Compra obrigatoriamente antecipada e on-line.</p>"
             "<p><b>Menor de 11 anos não paga na Sagrada Família; menor de 7 não paga "
             "no Park Güell</b> — mas os dois exigem ingresso emitido para a "
             "criança.</p>"),
            ("b", "A taxa turística é por pessoa, por noite, e não vem no preço do quarto",
             "<p><b>€ 7 por pessoa por noite num hotel de até três estrelas</b>, "
             "€ 8,40 num quatro, € 12 num cinco, € 9,50 num apartamento turístico — "
             "tabela oficial da Agència Tributària de Catalunya em vigor de 1º de "
             "abril de 2026 a 31 de março de 2027. <b>Quatro noites são € 28 por "
             "pessoa</b>, cobrados pelo hotel à parte.</p>"
             "<p><b>Menor de 17 anos não paga. Teto de 7 noites.</b></p>"
             "<p><b>O recargo de Barcelona sobe para € 6 em 1º de abril de 2027 e € 7 em "
             "2028</b>, e a ATC diz que em reserva antecipada vale a tarifa do dia do "
             "pagamento, se o imposto for pago junto. <b>Quem paga tudo antes de abril "
             "de 2027 trava o valor de hoje.</b></p>"),
            ("a", "O que este roteiro não alcança, e está dito",
             "<p><b>O gramado do Camp Nou.</b> O site do clube vende museu com "
             "“mirante das obras” desde € 28 e uma experiência com vista panorâmica "
             "desde € 69; <b>o tour clássico, com vestiário e beira do campo, não está "
             "na lista</b>. A imprensa de agosto de 2026 fala em obras até 2027 — não é "
             "fonte oficial.</p>"
             "<p><b>A Casa-Museu Gaudí, dentro do Park Güell</b>, está "
             "<i>“closed temporarily”</i> segundo o site da Sagrada Família, que a "
             "administra.</p>"
             "<p><b>Os preços “a partir de”</b> — Casa Batlló, La Pedrera, museu do "
             "Barça — podem subir no caixa conforme a data. O roteiro usa o piso.</p>"
             "<p><b>E a segunda-feira fecha Picasso, MNAC e, salvo feriado, boa parte "
             "dos museus municipais.</b> O quinto dia foi montado com o que abre.</p>"),
        ],
        "dias_lista": [
            ("Quinta — o Gòtic, o Palau e a tarde grátis do Picasso",
             "<b>Comece pela Catedral de Barcelona</b>, no coração do Barri Gòtic: a "
             "visita turística custa <b>€ 16</b> e, nos dias úteis, vai das 9h30 às "
             "18h30 — <b>no domingo só abre à tarde</b>, por isso ela está aqui e não "
             "no fim de semana. O site não diz o que os € 16 incluem nem publica o "
             "horário de culto, em que a entrada é livre; pergunte na porta. Dali são "
             "dez minutos a pé até o <b>Palau de la Música Catalana</b>: a visita com "
             "audioguia custa <b>€ 20</b>, a guiada <b>€ 24</b>, 50 minutos, e os "
             "horários só aparecem no seletor de compra. <b>Guarde as 16h.</b> É a "
             "hora em que o <b>Museu Picasso</b>, no Born, deixa de cobrar os € 12 — "
             "<b>com a reserva que você fez na segunda-feira anterior, às 10h de "
             "Barcelona</b>. Até as 19h no inverno; no verão, de quinta a sábado, a "
             "faixa gratuita é das 19h às 21h.",
             ["Catedral · € 16 · dias úteis 9h30–18h30",
              "Palau · € 20 com audioguia · € 24 guiada",
              "Picasso · 16h–19h · grátis com reserva",
              "Reserva abre 4 dias antes, às 10h",
              "No verão a faixa grátis é 19h–21h"]),

            ("Sexta — a Sagrada Família com hora marcada, e o Sant Pau a dez minutos",
             "<b>Chegue com o documento original e na hora marcada.</b> O ingresso da "
             "<b>Sagrada Família</b> é nominativo, custa <b>€ 26</b> com o audioguia "
             "no celular e <b>€ 36 com as torres</b>, e não se troca nem se devolve. "
             "Na sexta a basílica fica aberta até 19h em março e outubro, 20h de abril "
             "a setembro, 18h no inverno. <b>Depois das 14h, desça a Avinguda de "
             "Gaudí</b> — uma reta de dez minutos, com a basílica de um lado e o "
             "hospital modernista do outro — até o <b>Recinte Modernista de Sant "
             "Pau</b>, que <b>cobra € 17 depois das 14h e € 18 antes</b>. São os "
             "pavilhões de Domènech i Montaner, o arquiteto do Palau de ontem; abre "
             "todos os dias, até 18h30 de abril a outubro e 17h de novembro a março, "
             "com entrada até meia hora antes.",
             ["Sagrada Família · € 26 · torres € 36",
              "Nominativo · documento ORIGINAL",
              "Sem troca nem devolução",
              "Sant Pau · € 17 depois das 14h",
              "Dez minutos a pé pela Av. de Gaudí"]),

            ("Sábado — o Park Güell de manhã e o MNAC de graça à tarde",
             "<b>Park Güell cedo</b>, com a hora marcada comprada on-line e "
             "antecipadamente: <b>€ 18</b>, e <b>30 minutos de tolerância</b> depois "
             "do horário — passou, perdeu. Das 7h às 9h30 o parque é dos vizinhos; a "
             "visita turística vai das 9h30 às 19h30, e o site não publica horário "
             "de inverno. A Casa-Museu Gaudí, lá dentro, está fechada temporariamente. "
             "<b>À tarde, Montjuïc, primeira subida:</b> o <b>MNAC</b>, no Palau "
             "Nacional, <b>não cobra os € 12 a partir das 15h de todo sábado</b> — "
             "reserve on-line a entrada gratuita. No inverno são três horas (até 18h); "
             "no verão, cinco (até 20h). O terraço-mirante do palácio dá a vista da "
             "cidade que vale a subida, e a entrada básica de € 2 existe para quem "
             "quer só ela.",
             ["Park Güell · € 18 · hora marcada",
              "30 minutos de tolerância · depois perde",
              "MNAC · sábado a partir das 15h · grátis",
              "Reserve a entrada gratuita on-line",
              "Inverno fecha 18h; verão 20h"]),

            ("Domingo — Passeig de Gràcia de manhã e o castelo de graça à tarde",
             "<b>De manhã, a Casa Batlló</b>, no Passeig de Gràcia: <b>desde € 29</b>, "
             "e é “desde” porque o preço muda com a data e a antecedência — o site diz "
             "que comprar antes economiza até € 15, e não publica a tabela. Menor de 12 "
             "anos não paga. <b>À tarde, Montjuïc de novo, agora até o alto:</b> o "
             "<b>Castell de Montjuïc</b> <b>não cobra os € 12 a partir das 15h de todo "
             "domingo</b>, e no primeiro domingo do mês o dia inteiro. Suba pelo "
             "<b>funicular</b>, que está dentro do bilhete simples da TMB de € 2,90 — "
             "o teleférico até a porta do castelo é outra empresa e outro bilhete. De "
             "março a outubro a fortaleza fica aberta até 20h; de novembro a fevereiro, "
             "até 18h. <b>Se este domingo for o primeiro do mês, Picasso e MNAC também "
             "estão de graça o dia inteiro</b>, com reserva.",
             ["Casa Batlló · desde € 29 · preço muda com a data",
              "Montjuïc · domingo a partir das 15h · grátis",
              "Funicular · dentro do bilhete de € 2,90",
              "Teleférico é outra empresa",
              "1º domingo do mês: os três de graça"]),

            ("Segunda — o dia que fecha os museus fica para o que abre",
             "<b>Picasso e MNAC fecham toda segunda.</b> Por isso o último dia é de "
             "<b>La Pedrera</b>, que abre: a visita Essential custa <b>desde € 29</b> "
             "até 1º de novembro de 2026, das 9h às 17h30, com videoguia; a Sunset, "
             "das 17h30 às 20h30, desde € 25. Menor de 12 não paga, e o site não "
             "publica preço de estudante nem de maior de 65. <b>À tarde, o Museu do "
             "Barça</b>: <b>desde € 28</b>, com o “mirante das obras” — o Spotify Camp "
             "Nou segue em reforma e <b>o tour clássico do estádio não está à venda</b> "
             "na página oficial; a experiência com vista panorâmica custa desde € 69. "
             "A página não publica o horário do museu. <b>Quem vai pelo gramado, "
             "troca este ponto</b> pelo Sant Pau, se não foi na sexta, ou pela "
             "entrada básica de € 2 do MNAC — que, numa segunda, também está fechado. "
             "Fica o Sant Pau.",
             ["La Pedrera · desde € 29 · até 1/11/2026",
              "Sunset · desde € 25 · 17h30–20h30",
              "Museu do Barça · desde € 28 · mirante das obras",
              "Tour do estádio não está à venda",
              "Picasso e MNAC fechados na segunda"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de "
                   "custos, apurados em 18 de outubro de 2026 nas páginas oficiais de "
                   "cada monumento e museu, na TMB, na Agència Tributària de Catalunya e "
                   "no INE. <b>Quatro coisas ficaram sem resposta, e estão ditas nas "
                   "fichas:</b> o preço do Aerobus, que o site oficial só publica em "
                   "imagem; as tarifas reduzidas do Palau de la Música; o horário do "
                   "museu do Barça, cuja página de informação prática devolveu 404; e o "
                   "valor final dos ingressos vendidos como “a partir de”. "
                   "<b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
