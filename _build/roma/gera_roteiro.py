# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Roma.

Reusa o renderizador de novos/gera_roteiro.py, como os demais.

O QUE ORGANIZA ESTE ROTEIRO
---------------------------
A pergunta "qual domingo cai na sua viagem", que vale 16 euros e que
guia nenhum faz, porque quase todos tratam "domingo gratuito de Roma"
como se fosse uma coisa so.

    PRIMEIRO domingo   Estado italiano. Corta 41 euros:
                       Coliseu 18, Panteao 7, Borghese 16
    ULTIMO domingo     Vaticano. Corta 25 euros.
                       E e o UNICO domingo em que ele abre.

Os dois nunca caem na mesma viagem de cinco dias. Por isso o dia 5 deste
roteiro e o dia que se move, e ele diz exatamente para onde em cada
cenario - inclusive no cenario sem domingo nenhum.

O BILHETE DE 24 HORAS DO COLISEU E O QUE SALVA O DIA 5
------------------------------------------------------
Ele cobre Coliseu, Foro e Palatino e vale 24 horas a partir da primeira
picotada. Quem entra no Coliseu no fim da tarde do dia 2 ainda tem o
Foro e o Palatino na manha do dia 3 - sem pagar de novo. Numa viagem sem
domingo, e isso que da conteudo ao dia que sobra.

Uso
---
    python _build/roma/gera_roteiro.py
    python _build/roma/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_roma", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "roma": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Roma",
        "descricao": ("Cinco dias em Roma organizados pela pergunta que nenhum guia faz: "
                      "qual dos dois domingos gratuitos cai na sua viagem — e o que "
                      "fazer se não cair nenhum."),
        "abertura": ("Cinco dias organizados por uma distinção que quase todo guia "
                     "apaga: <b>Roma tem dois domingos gratuitos por mês, e eles não são "
                     "o mesmo domingo</b>. O primeiro corta € 41 da conta; o último "
                     "corta € 25 — e é o único em que o Vaticano abre."),
        "avisos": [
            ("a", "Dois domingos gratuitos, e eles nunca caem juntos",
             "<p><b>Primeiro domingo do mês — Estado italiano.</b> É a "
             "<b>Domenica al Museo</b>, do Ministério da Cultura, e libera mais de 480 "
             "sítios estatais. Nesta ficha: <b>Coliseu, Fórum e Palatino (€ 18), Panteão "
             "(€ 7) e Galleria Borghese (€ 16 dos € 18)</b>. Corta <b>€ 41</b>.</p>"
             "<p><b>Último domingo do mês — Vaticano</b>, que é outro país e outro "
             "calendário. Libera os <b>Museus Vaticanos e a Capela Sistina (€ 25)</b>, "
             "das <b>9h às 14h</b>, com última admissão às 12h30. Corta <b>€ 25</b>.</p>"
             "<p><b>Uma viagem de cinco dias pega no máximo um dos dois.</b> Por isso o "
             "dia 5 deste roteiro é o dia que se move — e ele diz para onde, em cada "
             "caso.</p>"),
            ("b", "O Vaticano fecha aos domingos — menos no último",
             "<p>É o erro de agenda que mais derruba viagem a Roma, porque o resto da "
             "cidade funciona normalmente no domingo. <b>Os Museus Vaticanos fecham em "
             "todos os domingos do mês, exceto o último.</b></p>"
             "<p>E o último domingo, que é o gratuito, abre <b>metade do horário</b> — "
             "das 9h às 14h, contra 9h às 18h dos dias normais — e é <b>o dia mais cheio "
             "do mês</b>. Grátis ali custa fila.</p>"
             "<p><b>A basílica é outra coisa:</b> é gratuita, tem entrada separada dos "
             "museus, e abre no domingo. <b>Quem confunde os dois portões perde a hora "
             "marcada</b> — eles ficam a uns quinze minutos de caminhada um do outro.</p>"),
            ("c", "Grátis não quer dizer sem reserva — e às vezes nem sem custo",
             "<p><b>Coliseu no primeiro domingo:</b> a entrada é gratuita, mas o bilhete "
             "continua sendo reservado pelo site de bilheteria. Em domingo gratuito a "
             "procura supera a lotação, e sem bilhete você não entra.</p>"
             "<p><b>Galleria Borghese no primeiro domingo:</b> a entrada é gratuita e "
             "<b>os € 2 de reserva continuam devidos</b>, porque a reserva é obrigatória "
             "para todas as categorias. <b>O domingo de graça custa € 2 ali</b>, e os "
             "bilhetes saem só 10 dias antes.</p>"
             "<p><b>E o Borghese é o ponto menos improvisável da cidade:</b> visita em "
             "turno fixo de duas horas (9h, 11h, 13h, 15h, 17h), sem entrada fora do "
             "turno, e <b>fecha às segundas</b>.</p>"),
            ("b", "Sentar na escadaria da Piazza di Spagna custa € 250",
             "<p>O regulamento de polícia urbana trata a escadaria de Trinità dei Monti "
             "como <b>monumento</b>, e <b>proíbe sentar e deitar</b>. A multa é de "
             "<b>€ 250</b>, chegando a <b>€ 400</b> por sujar, pichar ou danificar. A "
             "polícia municipal aborda quem senta e manda levantar.</p>"
             "<p><b>É exatamente o que todo turista faz na foto que todo mundo tira</b> — "
             "e é a regra mais fácil de infringir sem saber em toda esta ficha.</p>"),
        ],
        "dias_lista": [
            ("O centro a pé — o dia sem hora marcada",
             "Dia de chegada, de propósito: quase nada aqui tem bilhete, e o que tem não "
             "exige reserva. <b>Panteão, Fontana di Trevi, Piazza Navona e Piazza di "
             "Spagna formam um circuito de caminhada curta</b>, e <b>só o Panteão "
             "cobra</b>. Comece por ele: <b>€ 7</b> desde 1º de julho de 2026 — <b>era "
             "gratuito havia séculos e muito guia ainda escreve “entrada franca”</b>. "
             "Abre das 9h às 19h, <b>mas a bilheteria fecha às 18h e a última entrada é "
             "18h30</b>: três horários diferentes para a mesma tarde. Siga para a "
             "<b>Fontana di Trevi</b>, que não cobra — <b>entrar na água é proibido e "
             "multado</b> — e depois para a <b>Piazza Navona</b>, com as três fontes de "
             "Bernini. Feche na <b>Piazza di Spagna</b>, lembrando que <b>sentar na "
             "escadaria custa € 250</b>. Nos cafés dessas praças, o preço no balcão "
             "costuma ser menor que o da mesa, e a diferença deve estar afixada.",
             ["Panteão · € 7 · bilheteria fecha 18h",
              "Fontana di Trevi · grátis",
              "Piazza Navona · grátis",
              "Piazza di Spagna · grátis, mas não sente na escada",
              "Balcão é mais barato que a mesa"]),

            ("Coliseu, Fórum e Palatino — e o bilhete que dura 24 horas",
             "Um bilhete de <b>€ 18</b> cobre os três, e <b>vale 24 horas a partir da "
             "primeira picotada</b> — é a validade mais generosa desta ficha, e o roteiro "
             "vai usá-la. <b>A reserva de horário é obrigatória para o Coliseu</b>, com "
             "vendas abrindo <b>30 dias antes</b>; o Fórum e o Palatino você visita sem "
             "hora marcada, antes ou depois. <b>A permanência dentro do Coliseu é "
             "limitada a 75 minutos</b>, então não planeje a tarde inteira lá dentro. "
             "<b>Uma armadilha para quem lê daqui:</b> a meia-entrada de € 2 é <b>só para "
             "cidadão da União Europeia de 18 a 24 anos</b> — brasileiro de vinte anos "
             "paga os € 18 cheios. <b>Marque o Coliseu para o fim da tarde</b> e guarde o "
             "Fórum e o Palatino para a manhã seguinte: o mesmo bilhete ainda vale, e as "
             "ruínas ao sol da manhã são melhores que ao meio-dia. Os <b>Fori "
             "Imperiali</b>, na avenida, se veem de graça da calçada.",
             ["Coliseu, Fórum e Palatino · € 18 · um bilhete",
              "Vale 24 horas desde a primeira picotada",
              "Coliseu · hora marcada obrigatória · 75 min",
              "Meia de € 2 · só cidadão da UE de 18 a 24",
              "Fori Imperiali · de graça, da calçada"]),

            ("O Vaticano — e a segunda metade do bilhete de ontem",
             "Comece pelo <b>Fórum Romano e o Palatino</b>, se você seguiu a dica de "
             "ontem: <b>o bilhete de € 18 ainda está valendo</b>, e não se paga de novo. "
             "Depois atravesse para o Vaticano. <b>Os Museus Vaticanos custam € 20 na "
             "bilheteria ou € 25 online</b>, com o <i>Salta la fila</i> — e a ficha usa "
             "€ 25 porque quem vem de longe não aposta na fila da porta. <b>O bilhete "
             "vale só no dia e não é reembolsável.</b> <b>Cuidado com o site</b>: o museu "
             "avisa que existem domínios parecidos cobrando bem mais; o oficial é "
             "tickets.museivaticani.va. Depois dos museus, a <b>Basílica de São Pedro</b>, "
             "que é <b>gratuita</b> — mas por <b>outro portão</b>, a uns quinze minutos "
             "de caminhada. A <b>cúpula</b> custa <b>€ 10 pela escada ou € 15 com "
             "elevador</b>, e <b>o elevador poupa 231 dos 551 degraus: sobram 320 a "
             "pé</b>. <b>Não faça este dia num domingo comum</b> — os museus fecham.",
             ["Fórum e Palatino · mesmo bilhete de ontem",
              "Museus Vaticanos · € 25 online · € 20 na porta",
              "Fecha domingo, exceto o último do mês",
              "Basílica · grátis, mas é outro portão",
              "Cúpula · € 10 escada · € 15 elevador e 320 degraus"]),

            ("Villa Borghese e a Galleria — turno de duas horas, nunca na segunda",
             "Dia do parque e da galeria, e o mais amarrado do roteiro. A <b>Villa "
             "Borghese</b> é parque público e <b>gratuito</b>, e do <b>Pincio</b>, dentro "
             "dele, sai uma das vistas mais conhecidas da cidade — também de graça. A "
             "<b>Galleria Borghese</b>, o prédio pago no meio do parque, custa <b>€ 16 + "
             "€ 2 de reserva obrigatória</b>. <b>A visita é em turno fixo de exatamente "
             "duas horas</b> — 9h, 11h, 13h, 15h ou 17h — e às duas horas a sala é "
             "esvaziada para o turno seguinte. <b>Não há entrada fora do turno, e a "
             "reserva é obrigatória para todo mundo, inclusive para quem tem direito a "
             "entrada gratuita.</b> <b>Fecha às segundas.</b> Se o seu dia 4 for uma "
             "segunda, troque com o dia 1, que não tem nada marcado. Há ainda um "
             "<b>turno noturno às 18h45 por € 13</b>, que é a entrada mais barata da "
             "galeria.",
             ["Villa Borghese e Pincio · grátis",
              "Galleria Borghese · € 16 + € 2 de reserva",
              "Turno fixo de 2 horas · 9, 11, 13, 15 e 17h",
              "FECHA segunda",
              "Turno noturno 18h45 · € 13"]),

            ("O dia que se move — e para onde, conforme o seu domingo",
             "Este é o dia que muda de lugar, e o que você faz com ele depende de qual "
             "domingo caiu na sua viagem.<br><br>"
             "<b>Se a viagem pega um PRIMEIRO domingo do mês:</b> mova para ele o dia 2 "
             "(Coliseu) e, se couber, a Galleria Borghese. <b>Corta € 41</b> — € 18 do "
             "Coliseu, € 7 do Panteão e € 16 dos € 18 do Borghese. <b>Reserve os bilhetes "
             "gratuitos assim mesmo</b>, e com antecedência: no Coliseu a procura supera "
             "a lotação, e no Borghese os € 2 de reserva continuam devidos.<br><br>"
             "<b>Se a viagem pega um ÚLTIMO domingo:</b> mova para ele o dia 3, o do "
             "Vaticano. <b>Corta € 25</b> — mas o horário é <b>metade</b>, das 9h às 14h, "
             "com última admissão às 12h30, e é o dia mais cheio do mês. <b>Chegue antes "
             "das 9h.</b><br><br>"
             "<b>Se a viagem não pega domingo nenhum:</b> use este dia para o que o "
             "circuito a pé do centro pede numa segunda passada — o <b>Campo de' "
             "Fiori</b>, com feira de manhã, e a <b>Piazza Navona</b> sem a multidão do "
             "meio-dia. <b>O Castel Sant'Angelo</b> fica no caminho do Vaticano e cobra à "
             "parte, mas <span class=\"flag\">não apuramos a tarifa dele</span>.",
             ["Primeiro domingo · corta € 41 · reserve assim mesmo",
              "Último domingo · corta € 25 · só 9h às 14h",
              "Sem domingo · centro de novo, Campo de' Fiori",
              "Castel Sant'Angelo · tarifa não apurada"]),
        ],
        "fontes": ("Tarifas e horários consultados em 29 de setembro de 2026, os mesmos da "
                   "ficha dos 9 pontos. <b>Vários sites oficiais italianos recusaram "
                   "conexão direta</b> nesta apuração — o do Coliseu, o do ticketing dele, "
                   "o dos Museus Vaticanos e o do Comune di Roma —, e o navegador também "
                   "foi negado no ticketing. Não contornamos bloqueio: o que publicamos "
                   "vem da indexação dos próprios domínios oficiais, e está dito ponto a "
                   "ponto na ficha. <b>A conta dos dois domingos é cálculo nosso</b>, "
                   "somando as tarifas publicadas por cada casa. A ordem dos dias é nossa, "
                   "e o motivo está escrito em cada um."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
