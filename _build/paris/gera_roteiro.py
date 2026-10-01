# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Paris.

Reusa o renderizador de novos/gera_roteiro.py, como os demais.

O QUE ORGANIZA ESTE ROTEIRO
---------------------------
O calendario, e ele e assimetrico de um jeito que derruba viagem:

    SEGUNDA   fecha VERSALHES e as CATACUMBAS - os dois pontos que
              pedem o dia inteiro e o unico que fica debaixo da terra
    TERCA     fecha o LOUVRE

    PRIMEIRA SEXTA, depois das 18h   Louvre de graca
                                     NAO vale em julho nem agosto
    PRIMEIRO DOMINGO                 Orsay de graca, com reserva

Os dois dias ruins sao seguidos, e as duas janelas de graca NUNCA caem
no mesmo dia. Numa viagem de cinco dias isso define a ordem inteira.

TUDO ISSO FOI APURADO. O QUE NAO FOI, NAO ESTA AQUI
---------------------------------------------------
O dia de fechamento do MUSEE D'ORSAY nao foi apurado: a pagina de
tarifas e horarios dele recusa acesso. Este roteiro nao afirma em que
dia ele fecha - diz o que sabe, que e o primeiro domingo gratuito, e
manda conferir.

O DIA 5 E O DIA QUE SE MOVE
---------------------------
Porque depende de duas coisas que mudam com a semana do visitante: se a
viagem pega um primeiro domingo, e se pega uma segunda-feira.
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_paris_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "paris": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Paris",
        "descricao": ("Cinco dias em Paris na ordem que o calendário permite: segunda "
                      "fecha Versalhes e as Catacumbas, terça fecha o Louvre."),
        "abertura": ("Cinco dias organizados pelo calendário, que em Paris é "
                     "assimétrico: <b>segunda fecha Versalhes e as Catacumbas, terça "
                     "fecha o Louvre — e as duas janelas de entrada gratuita nunca caem "
                     "no mesmo dia.</b>"),
        "avisos": [
            ("a", "Dois dias fecham coisas, e eles são seguidos",
             "<p><b>Segunda-feira fecha o Palácio de Versalhes e as Catacumbas.</b> São "
             "justamente o passeio que pede o dia inteiro e o único ponto que fica "
             "debaixo da terra — e os dois somem no mesmo dia.</p>"
             "<p><b>Terça-feira fecha o Museu do Louvre.</b></p>"
             "<p>Como os dois dias são seguidos, uma viagem que chega no domingo perde "
             "pouco e uma que chega no sábado perde muito. <b>Este roteiro começa pelo "
             "centro a pé justamente porque esse dia funciona em qualquer dia da "
             "semana.</b></p>"),
            ("b", "As duas entradas gratuitas não caem no mesmo dia",
             "<p><b>O Louvre é gratuito para todos na primeira sexta-feira do mês, "
             "depois das 18h — e isso não vale em julho nem em agosto.</b></p>"
             "<p><b>O Musée d’Orsay é gratuito no primeiro domingo do mês</b>, para "
             "todos, <b>mas com reserva obrigatória</b> de um bilhete gratuito.</p>"
             "<p><b>Por anos o Louvre foi o museu do primeiro domingo. Não é mais.</b> "
             "Muito roteiro antigo ainda manda a pessoa ao Louvre no domingo, onde ela "
             "paga, em vez da sexta à noite, onde não pagaria. Os dois museus ficam a "
             "dez minutos um do outro, a pé pela ponte.</p>"),
            ("a", "A gratuidade de 18 a 25 anos provavelmente não é sua",
             "<p>Arco do Triunfo, Sainte-Chapelle e as torres de Notre-Dame anunciam "
             "<b>“gratuito para menores de 26 anos”</b>. <b>Não é para qualquer menor de "
             "26.</b></p>"
             "<p>Pelo Ministério da Cultura francês, <b>menor de 18 anos não paga, de "
             "qualquer nacionalidade</b>; mas a faixa de <b>18 a 25 anos só é gratuita "
             "para quem reside regularmente na União Europeia ou no Espaço Econômico "
             "Europeu</b>. <b>Um brasileiro de 20 anos paga inteira.</b></p>"
             "<p><b>E a regra muda de lugar para lugar na mesma cidade:</b> a Torre "
             "Eiffel cobra <b>€ 11,80</b> de qualquer pessoa de 12 a 24 anos, por idade, "
             "e as Catacumbas cobram <b>€ 25</b> de qualquer pessoa de 18 a 26. São "
             "administrações diferentes, e só os monumentos do Estado exigem "
             "residência.</p>"),
            ("b", "Duas coisas que o guia que você leu provavelmente ainda tem",
             "<p><b>O Centre Pompidou está fechado desde 22 de setembro de 2025 e só "
             "reabre em 2030.</b> Não monte um dia em volta dele.</p>"
             "<p><b>O elevador do Arco do Triunfo está em manutenção, até segunda "
             "ordem.</b> O acesso ao terraço se faz unicamente pelas escadas — quem tem "
             "mobilidade reduzida não sobe enquanto isso durar.</p>"),
        ],
        "dias_lista": [
            ("A ilha e o centro a pé — o dia que funciona em qualquer dia",
             "Dia de chegada, de propósito: <b>nada aqui depende do dia da semana</b>. "
             "Comece pela <b>Catedral de Notre-Dame</b>, que é <b>gratuita</b> — a "
             "reserva de horário também é gratuita e facultativa, mas <b>sem ela a "
             "espera chega a duas ou três horas na alta temporada</b>, porque a catedral "
             "recebe cerca de 35 mil pessoas por dia. <b>Ninguém está autorizado a vender "
             "ingresso de entrada</b>: quem estiver cobrando por isso na rua está "
             "vendendo o que é de graça. Atravesse a ilha até a <b>Sainte-Chapelle</b>, "
             "que custa <b>€ 22</b> e é o oposto da catedral em escala — uma capela "
             "pequena cujas paredes são quase inteiramente vitral. <b>Vá com o sol "
             "alto</b>: é a luz que faz o lugar. Feche caminhando pelas pontes, que não "
             "cobram nada.",
             ["Notre-Dame · grátis · reserve o horário",
              "Sainte-Chapelle · € 22 · vá com sol",
              "Torres de Notre-Dame · € 16 · à parte",
              "As pontes e as margens · grátis"]),

            ("O Louvre — e o dia em que ele não abre",
             "<b>O Louvre fecha às terças.</b> Se a sua terça for hoje, troque este dia "
             "com qualquer outro — é o único ponto do roteiro com essa restrição. "
             "<b>A entrada custa € 32 para quem não é cidadão nem residente do Espaço "
             "Econômico Europeu, e € 22 para quem é</b>; a cobrança separada começou em "
             "<b>14 de janeiro de 2026</b>. <b>Menor de 18 anos não paga, de qualquer "
             "nacionalidade.</b> <b>Se a sua viagem pegar a primeira sexta do mês, venha "
             "depois das 18h e não pague nada</b> — mas isso não vale em julho nem em "
             "agosto, e o museu recomenda reservar horário mesmo para a entrada "
             "gratuita. <b>Quarta e sexta ele vai até as 21h</b>; nos outros dias fecha "
             "às 18h, com <b>última entrada uma hora antes</b> e salas sendo esvaziadas "
             "30 minutos antes. <b>Cuidado com o bilhete</b>: o próprio museu alerta "
             "sobre sites espelho e venda de rua, e quem compra assim pode ter a entrada "
             "recusada.",
             ["Louvre · € 32 · fecha às TERÇAS",
              "Europeu paga € 22 · menor de 18 não paga",
              "1ª sexta do mês, após 18h · grátis",
              "Não vale em julho nem agosto",
              "Quarta e sexta até 21h"]),

            ("Versalhes, o dia inteiro — e nunca numa segunda",
             "<b>Versalhes fecha às segundas</b>, mais 25 de dezembro, 1º de janeiro e 1º "
             "de maio. É passeio de dia inteiro e fica fora de Paris. <b>O bilhete "
             "Passaporte é o único que entra no castelo</b>, com horário marcado, e cobre "
             "o domínio inteiro: <b>€ 35 na alta temporada, de 1º de abril a 31 de "
             "outubro, e € 25 na baixa</b>. <b>O europeu paga € 3 a menos</b> — e aqui a "
             "redução vale tanto por cidadania quanto por residência. <b>O castelo abre "
             "às 9h, mas o domínio de Trianon só às 12h</b>: comece pelo castelo e deixe "
             "o Grande Trianon, o Pequeno Trianon e a Aldeia da Rainha para a tarde. "
             "<b>Os jardins são pagos de abril a outubro e gratuitos de novembro a "
             "março</b> — custam justamente na época em que estão bonitos. Se o tempo "
             "apertar, <b>há um Passaporte de fim de dia por € 28</b>, com entrada no "
             "castelo a partir das 16h.",
             ["Versalhes · € 35 na alta · fecha SEGUNDAS",
              "Europeu paga € 32 · baixa custa € 25",
              "Castelo abre 9h · Trianon só às 12h",
              "Jardins pagos de abril a outubro",
              "Passaporte de fim de dia · € 28"]),

            ("A torre, o arco e Montmartre — o dia de subir",
             "Três subidas, e <b>nenhuma delas fecha em dia nenhum</b>. Comece pela "
             "<b>Torre Eiffel</b>: <b>€ 23,50 até o segundo andar de elevador, € 36,70 "
             "até o topo</b> — ou <b>€ 14,80 pela escada até o segundo andar</b>, que "
             "economiza € 8,70 e pula a fila do elevador em troca de 674 degraus. "
             "<b>Aqui a tarifa jovem é por idade</b>, de 12 a 24 anos, por <b>€ 11,80</b>, "
             "sem condição de nacionalidade. Abre das <b>9h30 às 23h</b>, com últimas "
             "subidas às 22h45. Siga para o <b>Arco do Triunfo</b>, <b>€ 16</b> — e "
             "<b>lembre que o elevador está quebrado</b>: só se sobe a pé. Feche em "
             "<b>Montmartre</b>, com o <b>Sacré-Cœur</b>, que é <b>gratuito e abre todos "
             "os dias do ano, das 6h30 às 22h30</b>. É o horário mais largo da sua "
             "viagem, e o lugar certo para o fim da tarde.",
             ["Torre Eiffel · € 23,50 · ou € 14,80 a pé",
              "Jovem 12 a 24 · € 11,80 · por idade",
              "Arco do Triunfo · € 16 · só escada",
              "Sacré-Cœur · grátis · 6h30 às 22h30"]),

            ("O dia que se move — Orsay ou Catacumbas",
             "<b>Este dia depende da sua semana, e por isso ele é o último.</b><br>"
             "<b>Se a sua viagem pegar o primeiro domingo do mês</b>, use-o no "
             "<b>Musée d’Orsay</b>, que é <b>gratuito para todos nesse dia, com reserva "
             "obrigatória</b> de bilhete gratuito. <b>Não publicamos o preço normal do "
             "Orsay</b> porque a página de tarifas dele recusa acesso e a bilheteria só "
             "mostra valor depois de escolher data — <b>confira antes de ir</b>, e saiba "
             "que ele está <b>reformando as áreas de recepção de março de 2026 até o "
             "verão de 2028</b>.<br>"
             "<b>Se não pegar o primeiro domingo</b>, use o dia nas <b>Catacumbas</b>: "
             "<b>€ 31 com audioguia</b>, <b>de terça a domingo, das 9h45 às 20h30</b>, "
             "última entrada 19h30, <b>fechadas às segundas</b>. A reserva on-line abre "
             "<b>sete dias antes</b> e costuma esgotar. <b>São mais caras que o Louvre "
             "para um europeu</b>, e quase o mesmo para quem não é.<br>"
             "<b>Se a sua viagem pegar os dois</b> — primeiro domingo e um dia útil "
             "livre —, dá para fazer os dois, e esse é o melhor cenário possível.",
             ["1º domingo · Orsay grátis · reserve",
              "Orsay · preço normal não apurado",
              "Sem domingo · Catacumbas · € 31",
              "Catacumbas fecham SEGUNDAS",
              "Reserva abre 7 dias antes"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de "
                   "custos, apurados em 30 de setembro de 2026 em fonte oficial — "
                   "louvre.fr, chateauversailles.fr, toureiffel.paris, "
                   "catacombes.paris.fr, sainte-chapelle.fr, "
                   "paris-arc-de-triomphe.fr, sacre-coeur-montmartre.com e "
                   "culture.gouv.fr. <b>Três sites oficiais recusaram leitura</b>: "
                   "notredamedeparis.fr e toureiffel.paris devolveram erro 403 ao "
                   "cliente HTTP, e musee-orsay.fr responde “Accès refusé” na "
                   "página de tarifas. A Torre Eiffel abriu no navegador; o Orsay "
                   "não abriu de jeito nenhum, e por isso <b>este roteiro não diz "
                   "o preço dele nem em que dia ele fecha</b>. Não contornamos "
                   "bloqueio."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
