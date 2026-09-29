# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Madri.

Reusa o renderizador de novos/gera_roteiro.py, como os demais.

O QUE ORGANIZA ESTE ROTEIRO
---------------------------
Uma corrente de segunda-feira que nenhum guia que abrimos publica. De
outubro a marco:

    12h-16h   Thyssen         14 EUR   gratis (patrocinio)
    16h-18h   Palacio Real    18 EUR   gratis (iberoamericano)
    18h-20h   Prado           15 EUR   gratis (2h antes de fechar)

Oito horas seguidas, 47 euros de bilhete, zero pago - e os tres ficam
perto o bastante para se fazer a pe. De abril a setembro a janela do
palacio vira 17h-19h e encosta na do Prado: ainda da, so mais apertado.

O QUARTO GRATIS NAO CABE NA MESMA SEGUNDA
-----------------------------------------
O Reina Sofia e gratis das 19h as 21h, que colide com o Prado. Entao ele
vai para outra noite - qualquer uma menos terca, que e quando fecha.

AS DUAS ARMADILHAS DO CALENDARIO, QUE SAO OPOSTAS
-------------------------------------------------
    Segunda   Debod FECHADO          (e o dia das janelas gratuitas)
    Terca     Reina Sofia FECHADO    (e Prado e Thyssen abrem)

Ou seja: o melhor dia para museu e o pior dia para Debod, e vice-versa.

E GRATIS NAO QUER DIZER ENTRA
-----------------------------
Dois pontos gratuitos exigem bilhete assim mesmo: o Reina Sofia pede
entrada reservada mesmo no horario gratuito, e o Templo de Debod avisa
que "sin reserva no se garantiza el acceso". Os dois sao de graca e os
dois deixam gente na porta.

Uso
---
    python _build/madri/gera_roteiro.py
    python _build/madri/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_madri", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "madri": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Madri",
        "descricao": ("Cinco dias em Madri montados em cima das quatro janelas "
                      "gratuitas — incluindo a corrente de segunda-feira que vale "
                      "€ 47 por pessoa e não aparece em guia nenhum."),
        "abertura": ("Cinco dias organizados por uma coisa que nenhum guia junta: "
                     "<b>três entradas gratuitas de Madri encadeiam na mesma "
                     "segunda-feira</b>, das 12h às 20h, e valem € 47 por pessoa."),
        "avisos": [
            ("a", "A segunda-feira vale € 47, e as três janelas encadeiam",
             "<p>De <b>outubro a março</b>, uma segunda-feira em Madri se organiza "
             "sozinha:</p>"
             "<p><b>12h às 16h — Museo Thyssen-Bornemisza</b>, € 14, grátis por "
             "patrocínio. E é o dia em que ele <b>só</b> abre nesse horário, então é de "
             "graça o tempo inteiro em que está aberto.<br>"
             "<b>16h às 18h — Palácio Real</b>, € 18, grátis para cidadão "
             "latino-americano.<br>"
             "<b>18h às 20h — Museo del Prado</b>, € 15, grátis nas duas horas antes de "
             "fechar.</p>"
             "<p><b>São € 47 por pessoa, em oito horas seguidas, sem pagar nada</b> — e "
             "os três ficam perto o bastante para se fazer a pé, com o palácio no meio "
             "do caminho.</p>"
             "<p><b>De abril a setembro</b> a janela do palácio vira <b>17h às 19h</b> e "
             "encosta na do Prado. Ainda dá: saia do palácio às 18h30 e entre no Prado, "
             "que fica aberto até as 20h.</p>"),
            ("b", "Leve o passaporte ao Palácio Real, e vá à bilheteria",
             "<p>A tarifa gratuita do Palácio Real <b>não é só para europeu</b>. O texto "
             "da Patrimonio Nacional concede entrada livre a cidadãos da UE <b>e a "
             "“ciudadanos iberoamericanos”</b> com prova de nacionalidade. "
             "<b>Brasileiro entra nessa lista</b>, e quase todo guia escreve só a parte "
             "da UE.</p>"
             "<p><b>Três condições anulam o direito se você não souber:</b> vale "
             "<b>só para visita livre</b> — visita guiada não entra; o bilhete <b>só sai "
             "na bilheteria física</b>, nunca online; e o acesso é permitido <b>até 60 "
             "minutos antes do fechamento</b>.</p>"
             "<p>E vale <b>de segunda a quinta</b> apenas. Sexta, sábado e domingo não "
             "têm janela gratuita para ninguém.</p>"),
            ("c", "As duas armadilhas do calendário são opostas",
             "<p><b>Segunda-feira:</b> o <b>Templo de Debod fecha</b>, inclusive quando "
             "cai feriado. É justo o dia das janelas gratuitas.</p>"
             "<p><b>Terça-feira:</b> o <b>Reina Sofía fecha</b> — e o Prado e o Thyssen "
             "não, o que faz muita gente marcar museu na terça e descobrir que perdeu o "
             "Guernica.</p>"
             "<p>Ou seja, o melhor dia para museu é o pior para Debod, e o contrário "
             "também. Por isso os dois estão em dias separados aqui.</p>"),
            ("b", "Grátis não quer dizer que você entra",
             "<p>Dois pontos gratuitos desta ficha exigem bilhete assim mesmo, e os dois "
             "deixam gente na porta:</p>"
             "<p><b>Reina Sofía</b> — a página oficial é literal: <i>“Durante el horario "
             "gratuito también necesitas una entrada”</i>. Reserve online antes de ir.</p>"
             "<p><b>Templo de Debod</b> — o aforo é limitado e a prefeitura escreve "
             "<b>“sin reserva no se garantiza el acceso”</b>. A reserva é gratuita, em "
             "<b>madrid.es/debodreservas</b>.</p>"),
        ],
        "dias_lista": [
            ("O Madri dos Áustrias — o dia sem relógio",
             "Dia de chegada, de propósito: <b>nada aqui tem hora marcada nem "
             "bilheteria</b>, então aguenta atraso de voo. Comece na <b>Puerta del "
             "Sol</b>, onde estão o marco do <b>quilômetro zero</b> das estradas "
             "espanholas e a estátua do <b>urso com o medronheiro</b>, que é o símbolo "
             "da cidade. Desça pela Calle Mayor até a <b>Plaza Mayor</b>, cinco minutos a "
             "pé — <b>sentar nas mesas da praça custa preço de zona turística</b>, e "
             "olhar não custa nada. Colado a ela fica o <b>Mercado de San Miguel</b>, de "
             "ferro e vidro: entrar é gratuito, e as bancas são caras para o padrão de "
             "Madri, com porções pequenas que fazem a conta subir sem parecer. Feche na "
             "<b>Catedral de la Almudena</b>, cuja nave é <b>gratuita</b>, com donativo "
             "sugerido de € 1. <b>Deixe o museu e a cúpula dela para outro dia</b> — eles "
             "só abrem de segunda a sábado, das 10h às 14h30.",
             ["Puerta del Sol e Plaza Mayor · grátis, 24 horas",
              "Mercado de San Miguel · entrar é grátis",
              "Catedral de la Almudena · grátis, donativo de € 1",
              "Museu e cúpula · só seg a sáb, 10h às 14h30"]),

            ("A segunda-feira de ouro — € 47 sem pagar nada",
             "<b>Se a sua viagem tiver uma segunda, é este o dia.</b> Comece ao meio-dia "
             "no <b>Museo Thyssen-Bornemisza</b>: às segundas ele abre das <b>12h às "
             "16h</b> e é <b>gratuito nesse período inteiro</b>, por patrocínio. A "
             "gratuidade cobre a coleção permanente, não as temporárias. Às 16h caminhe "
             "até o <b>Palácio Real</b> e entre pela <b>bilheteria física</b>, com o "
             "<b>passaporte na mão</b>: de outubro a março a tarifa gratuita para cidadão "
             "latino-americano vale das <b>16h às 18h</b>; de abril a setembro, das 17h "
             "às 19h. <b>Peça visita livre</b> — guiada não entra na gratuidade. Às 18h "
             "volte ao Paseo del Prado para o <b>Museo del Prado</b>, gratuito das "
             "<b>18h às 20h</b>. <b>Duas horas não dão para ver tudo</b>: escolha salas "
             "antes de entrar, porque a fila da janela gratuita se forma antes das 18h e "
             "come tempo. Somados, são <b>€ 47 de bilhete por pessoa</b>.",
             ["Thyssen · 12h às 16h · grátis segunda",
              "Palácio Real · 16h às 18h · grátis com passaporte",
              "Palácio Real · só bilheteria, só visita livre",
              "Prado · 18h às 20h · grátis",
              "€ 47 em bilhetes, € 0 pagos"]),

            ("Retiro de dia, Reina Sofía à noite — menos na terça",
             "Dia do Paseo del Arte que sobrou, e ele tem hora certa no fim. Passe a "
             "manhã e a tarde no <b>Parque del Retiro</b>, que é público e gratuito, com "
             "o <b>Palacio de Cristal</b> dentro — a estufa de ferro e vidro também não "
             "cobra nada e funciona como sala de exposição do Reina Sofía. O parque é "
             "<b>Patrimônio Mundial da UNESCO desde 2021</b>, e <b>fecha em episódios de "
             "vento forte</b>, por risco de queda de árvore. Ele sobe a ladeira atrás do "
             "Prado, então o deslocamento é a pé. Às 19h entre no <b>Museo Reina "
             "Sofía</b>, gratuito das <b>19h às 21h</b> — <b>mas reserve o bilhete "
             "antes</b>, porque mesmo de graça ele é exigido. <b>Não faça este dia numa "
             "terça</b>, que é quando o museu fecha. E <b>se for domingo, tudo muda</b>: "
             "o Reina Sofía fecha às 14h30 e a janela gratuita é das <b>12h30 às "
             "14h30</b>.",
             ["Parque del Retiro · grátis",
              "Palacio de Cristal · grátis",
              "Reina Sofía · grátis 19h às 21h",
              "Reina Sofía · FECHA terça",
              "Domingo · grátis 12h30 às 14h30, fecha 14h30"]),

            ("Templo de Debod e o pôr do sol — menos na segunda",
             "Dia mais curto e o mais fotogênico. O <b>Templo de Debod</b> é um templo "
             "egípcio do século II a.C., doado pelo Egito à Espanha em 1968 e remontado "
             "no <b>Parque del Oeste</b>. <b>A entrada é gratuita — e é o grátis mais "
             "traiçoeiro de Madri</b>: o aforo é limitado e a prefeitura escreve que "
             "<b>sem reserva o acesso não é garantido</b>. Reserve, de graça, em "
             "madrid.es/debodreservas. <b>Fecha todas as segundas</b>, inclusive "
             "feriados. De terça a domingo abre das 10h às 20h, com <b>última entrada 30 "
             "minutos antes</b>; no verão, de 15 de junho a 15 de setembro, fecha às 19h. "
             "<b>É o pôr do sol mais disputado da cidade</b>, com o templo refletido no "
             "espelho d'água e a serra ao fundo — e é por isso que o aforo enche no fim "
             "da tarde. Se sobrar tempo, complete com o museu e a cúpula da "
             "<b>Almudena</b>, € 7, lembrando que fecham às 14h30.",
             ["Templo de Debod · grátis, mas reserve",
              "Debod · FECHA segunda, inclusive feriado",
              "Ter a dom 10h às 20h · verão até 19h",
              "Última entrada · 30 min antes",
              "Almudena, museu e cúpula · € 7, até 14h30"]),

            ("Bernabéu — o dia que custa, e fica fora do eixo",
             "Último dia, e o único que exige deslocamento de verdade: o <b>Estadio "
             "Santiago Bernabéu</b> fica no Paseo de la Castellana, ao norte, <b>fora do "
             "eixo de todos os outros pontos desta ficha</b>. O tour custa <b>a partir de "
             "€ 35 comprando online e € 38 na bilheteria</b> — <b>é a única linha de todo "
             "o site em que o canal de compra muda o preço</b>, e são € 3 por deixar para "
             "a hora. É também <b>o ingresso mais caro da página</b>, mais que o dobro do "
             "Prado. Abre das <b>9h às 19h de segunda a sábado</b> e das 9h30 às 18h30 "
             "aos domingos e feriados, todos os dias do ano menos 25 de dezembro e 1º de "
             "janeiro. <b>O próprio clube avisa que o percurso e o horário mudam por "
             "causa dos eventos no estádio</b>, informando só no site, na bilheteria ou "
             "na porta — <b>evite marcar na véspera de jogo em casa</b>, quando o roteiro "
             "encolhe.",
             ["Bernabéu · € 35 online · € 38 na bilheteria",
              "Seg a sáb 9h às 19h · dom e feriado 9h30 às 18h30",
              "Fecha só 25/dez e 1º/jan",
              "Dia de jogo · percurso encolhe",
              "Fora do eixo · não é caminhada"]),
        ],
        "fontes": ("Tarifas e horários consultados em 29 de setembro de 2026, os mesmos da "
                   "ficha dos 10 pontos. <b>A corrente de segunda-feira é cálculo nosso</b>, "
                   "feito a partir das três janelas gratuitas publicadas por cada casa — "
                   "não é um produto anunciado por ninguém, e por isso vale conferir os "
                   "horários na véspera. <b>A exceção de procedência é o Prado</b>: a "
                   "página dele não abriu, por proteção anti-bot, e o que publicamos vem "
                   "da indexação do próprio domínio somada à ficha do esMadrid, portal "
                   "oficial de turismo da cidade. A ordem dos dias é nossa, e o motivo "
                   "está escrito em cada um."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
