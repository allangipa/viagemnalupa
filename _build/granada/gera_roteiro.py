# -*- coding: utf-8 -*-
"""Roteiro de 3 dias em Granada, montado pelo calendario.

Mesmo molde do paris/gera_roteiro.py.

O ACHADO DESTE ROTEIRO E ARITMETICO, E SAI DA APURACAO
-------------------------------------------------------
Granada tem DUAS gratuidades em dias fixos da semana:

    QUARTA a tarde   Catedral e Capilla Real, por reserva nominativa
                     no site da diocese                    vale 17 EUR
    DOMINGO          monumentos andalusies, sem reserva      vale  2 EUR

De quarta a domingo vao CINCO dias. De domingo a quarta vao QUATRO.
Logo: UMA VIAGEM DE TRES DIAS NAO CABE AS DUAS. E preciso escolher, e
quatro dias comecando no domingo e a janela minima que pega as duas.

Nenhum guia que abrimos faz essa conta. Ela esta no aviso "a".

O SEGUNDO ACHADO: SEXTA E SABADO SAO AS UNICAS NOITES DO ANO INTEIRO
---------------------------------------------------------------------
A visita noturna aos Palacios Nazaries roda:

    15 out - 31 mar    sexta e sabado
    1 abr - 14 out     terca a sabado

A INTERSECAO das duas temporadas e sexta e sabado. Ou seja: so nesses
dois dias a noturna existe em QUALQUER epoca do ano. Por isso o terceiro
dia deste roteiro e uma sexta - ele funciona em janeiro e em julho.

Em qualquer outro arranjo de tres dias o leitor teria de conferir a
temporada antes de contar com a noturna.

POR QUE QUARTA, QUINTA E SEXTA
-------------------------------
    quarta   pega a gratuidade de 17 EUR, que e a maior das duas
    quinta   a Alhambra, com o Museo de la Alhambra aberto ate o fim
             da tarde (ele FECHA segunda e fecha 14h30 no domingo e na
             terca)
    sexta    a noturna, que nesse dia roda o ano inteiro

O que esse arranjo perde esta dito: Silla del Moro e Torres Bermejas so
abrem sabado e domingo, e ficam de fora. A linha diz isso em vez de
fingir que o roteiro cobre tudo.

A ARMADILHA DE PLANEJAMENTO QUE MAIS PEGA
------------------------------------------
A reserva gratuita FECHA 24 HORAS ANTES da visita. Quem descobre a
gratuidade ao chegar em Granada numa quarta de manha JA PERDEU - tinha de
ter reservado na terca. Por isso o aviso "b" existe, e por isso ele e o
segundo e nao o quinto.

Uso
---
    python _build/granada/gera_roteiro.py
    python _build/granada/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_granada_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "granada": {
        "dias": 3,
        "titulo": "Roteiro de 3 dias em Granada",
        "descricao": ("Três dias em Granada na ordem que o calendário permite: a "
                      "quarta-feira que não cobra, a Alhambra com hora marcada e a "
                      "única noite que funciona o ano inteiro."),
        "abertura": ("Três dias organizados pelo calendário, que em Granada decide mais "
                     "que o orçamento: <b>as duas entradas gratuitas da cidade caem em "
                     "quarta e em domingo, que ficam a cinco dias uma da outra — e por "
                     "isso uma viagem de três dias não cabe as duas.</b>"),
        "avisos": [
            ("a", "Três dias não cabem as duas gratuidades — e a conta diz qual escolher",
             "<p>Granada tem <b>duas</b> entradas gratuitas em dias fixos da semana, e "
             "elas não são vizinhas.</p>"
             "<p><b>Quarta-feira à tarde:</b> Catedral e Capilla Real, de graça, por "
             "reserva nominativa no site da diocese. <b>Vale € 17.</b></p>"
             "<p><b>Domingo:</b> os monumentos andalusíes — Bañuelo, Casa Horno de Oro, "
             "Dar al-Horra, Maristán — de graça, sem reserva. <b>Vale € 2</b> por "
             "monumento visitado.</p>"
             "<p><b>De quarta a domingo vão cinco dias; de domingo a quarta, quatro.</b> "
             "Uma viagem de três dias não alcança as duas, por nenhum arranjo. "
             "<b>Quatro dias começando num domingo é a janela mínima que pega as "
             "duas</b> — e ainda apanha o sábado e o domingo em que a Silla del Moro e "
             "as Torres Bermejas abrem.</p>"
             "<p><b>Se forem só três dias, escolha a quarta:</b> € 17 contra € 2 não é "
             "escolha difícil. É o que este roteiro faz.</p>"),
            ("b", "A reserva gratuita fecha 24 horas antes — então ela se faz de casa",
             "<p>As condições gerais do site de reservas da diocese são diretas: "
             "<b>“El periodo de reservas finalizará 24 horas antes de la visita.”</b></p>"
             "<p><b>Quem descobre a gratuidade ao chegar em Granada numa quarta de manhã "
             "já perdeu.</b> Tinha de ter reservado na terça. Reserve antes de viajar.</p>"
             "<p>E as regras são apertadas: <b>no máximo duas entradas por pessoa e por "
             "dia</b>, é <b>nominativa</b> e só vale mediante apresentação do documento "
             "do solicitante, há <b>15 minutos de tolerância</b> de atraso, <b>é "
             "proibido fotografar e gravar</b>, não vale para grupos e não inclui "
             "audioguia — que o bilhete pago inclui.</p>"
             "<p><b>São duas reservas separadas</b>, uma para a Catedral e outra para a "
             "Capilla Real, cada uma no seu formulário, e cada uma conta no limite de "
             "duas por pessoa. As sessões são diferentes: a Catedral às 15h15, 15h30, "
             "16h e 16h30; a Capilla Real às 15h15, 15h30, 16h30 e 17h.</p>"
             "<p><b>O calendário abre poucas datas por vez.</b> Na nossa consulta, em "
             "30 de setembro de 2026, havia três datas abertas para a Catedral e quatro "
             "para a Capilla Real — <b>todas quartas-feiras</b>. Confira antes de "
             "montar o dia em cima disso.</p>"),
            ("a", "A Alhambra se perde por meia hora de atraso, e não devolve dinheiro",
             "<p><b>É a regra mais dura de qualquer ponto deste site.</b></p>"
             "<p><b>O ingresso é nominativo</b>, pessoal e intransferível, e exige "
             "<b>documento de identidade original</b> na entrada, com conferência.</p>"
             "<p><b>Os Palacios Nazaríes têm hora marcada: 300 pessoas a cada meia "
             "hora.</b> E o site oficial é explícito sobre o atraso: <b>“Transcurrido "
             "dicho turno horario, se perderá el derecho a la visita de este "
             "espacio.”</b> <b>Perder o turno é perder os palácios</b> — que são a razão "
             "da visita. O resto do bilhete continua valendo.</p>"
             "<p><b>Não há devolução:</b> <b>“Cualquier compra de entradas tiene "
             "carácter definitivo y firme”</b>, e <b>data e hora não podem ser "
             "alteradas</b>. Troca de nome só a partir de cinco ingressos, só se não "
             "tiverem sido impressos, e até o dia anterior.</p>"
             "<p><b>Menor de 12 anos não paga</b>, de qualquer nacionalidade — mas "
             "precisa de ingresso emitido, tirado junto com os dos adultos.</p>"),
            ("b", "Sexta e sábado são as únicas noites que funcionam o ano inteiro",
             "<p>A visita noturna aos Palacios Nazaríes muda de dias conforme a "
             "temporada:</p>"
             "<p><b>De 15 de outubro a 31 de março: sexta e sábado, 20h às 21h30.</b><br>"
             "<b>De 1º de abril a 14 de outubro: terça a sábado, 22h às 23h30.</b></p>"
             "<p><b>O que as duas temporadas têm em comum é sexta e sábado</b> — e só. "
             "Em qualquer outro dia da semana a noturna depende do mês. <b>Por isso o "
             "terceiro dia deste roteiro é uma sexta:</b> ele funciona em janeiro e em "
             "julho sem mudar nada.</p>"
             "<p><b>A noturna dos jardins é outra coisa, e some justamente no verão:</b> "
             "ela roda de 1º de abril a 31 de maio e de 1º de setembro a 14 de outubro, "
             "de terça a sábado, e de 15 de outubro a 14 de novembro, sexta e sábado. "
             "<b>Junho, julho e agosto não aparecem na tabela</b>, nem de 15 de novembro "
             "a 31 de março.</p>"),
            ("a", "O que este roteiro não alcança, e está dito",
             "<p><b>Silla del Moro e Torres Bermejas só abrem sábado e domingo.</b> São "
             "dois miradouros da própria Alhambra, com <b>entrada gratuita</b> — e ficam "
             "de fora de um roteiro de quarta a sexta. Não há como ter as duas coisas em "
             "três dias.</p>"
             "<p><b>E as duas têm regras de domingo diferentes entre si:</b> a Silla del "
             "Moro fecha às <b>14h</b> no domingo nas duas temporadas; as Torres "
             "Bermejas seguem até <b>20h</b> no verão, igual ao sábado. São dois lugares "
             "do mesmo órgão, a vinte minutos de caminhada um do outro.</p>"
             "<p><b>A segunda-feira fecha o Museo de la Alhambra</b>, que é gratuito e "
             "fica dentro do recinto. <b>E domingo e terça ele fecha às 14h30</b>, cinco "
             "horas e meia antes do sábado de verão. Quem deixa esse museu para a tarde "
             "de domingo encontra porta fechada.</p>"),
        ],
        "dias_lista": [
            ("Quarta — o centro, e a tarde que não cobra",
             "<b>Comece pelo que é de graça todo dia:</b> o <b>Corral del Carbón</b>, "
             "pousada de mercadores do século XIV, tem entrada livre para todos por "
             "norma legal — o artigo 9.1 da ordem de preços da Alhambra — e é também "
             "onde fica o balcão de atendimento do Patronato. Dali o centro se faz a pé: "
             "a Alcaicería, a Plaza Bib-Rambla, a Gran Vía. <b>Guarde a tarde, porque "
             "ela é o motivo de este dia ser uma quarta.</b> Às <b>15h15</b> entre na "
             "<b>Catedral de Granada</b> com a reserva gratuita que você fez de casa — "
             "o interior é branco e luminoso, e a Capilla Mayor é o que se vai ver. "
             "Às <b>16h30</b>, a <b>Capilla Real</b>, colada à catedral, onde estão os "
             "túmulos de Isabel e Fernando. <b>Nas duas é proibido fotografar e o "
             "celular fica desligado</b>, e nenhuma das duas inclui audioguia. "
             "<b>Sem a reserva, o mesmo par custa € 17.</b>",
             ["Corral del Carbón · grátis sempre · por lei",
              "Catedral · 15h15 · grátis com reserva",
              "Capilla Real · 16h30 · grátis com reserva",
              "Reserve as duas ANTES de viajar",
              "Proibido fotografar nas duas"]),

            ("Quinta — a Alhambra, o dia inteiro, com hora marcada",
             "<b>Chegue cedo e com o documento original no bolso.</b> O bilhete é "
             "nominativo e há conferência de identidade. <b>A visita diurna geral custa "
             "€ 22,27 no site do monumento</b> — a lei fixa € 21, e o site avisa que a "
             "comissão ainda se soma, então trate esse valor como piso. "
             "<b>O horário dos Palacios Nazaríes é o único inegociável do roteiro:</b> "
             "são 300 pessoas a cada meia hora, e perder o turno é perder os palácios. "
             "Faça a <b>Alcazaba</b> e o <b>Partal</b> em volta do seu horário, e o "
             "<b>Generalife</b> com os jardins e o Pátio da Acequia. <b>E não saia sem "
             "o Museo de la Alhambra</b>, que fica dentro do Palacio de Carlos V, o "
             "palácio renascentista de pátio circular — <b>a entrada dele é livre, "
             "mesmo para quem não tem bilhete do monumento</b>, e numa quinta ele fica "
             "aberto até 18h no inverno e 20h no verão. Feche o dia subindo ao "
             "<b>Mirador de San Nicolás</b>, no Albaicín, no fim da tarde: a vista mais "
             "fotografada da cidade <b>não tem bilheteria nem horário</b>.",
             ["Alhambra · € 22,27 · hora marcada nos palácios",
              "Documento ORIGINAL · sem ele não entra",
              "Museo de la Alhambra · grátis · até 18h/20h",
              "Mirador de San Nicolás · grátis · fim de tarde",
              "A torre ao lado do mirante custa € 3"]),

            ("Sexta — Sacromonte, o Albaicín e a noite nos palácios",
             "<b>Manhã no Sacromonte.</b> O <b>Museo Cuevas del Sacromonte</b> custa "
             "<b>€ 6,00</b> no caixa oficial — e não € 5, que é número de resenha — e "
             "abre <b>todos os dias</b>, 10h às 18h no inverno e 10h às 20h no verão. "
             "São onze cavernas de moradia, o jardim botânico e um mirador. <b>Não "
             "confunda com a Abadía del Sacromonte</b>, que é outro lugar, mais acima, e "
             "custa <b>€ 7,00</b>. Desça pelo <b>Albaicín</b> e entre em um dos "
             "<b>monumentos andalusíes</b> a <b>€ 2</b> cada: o <b>Bañuelo</b>, banhos "
             "árabes do século XI, ou o <b>Palacio de Dar al-Horra</b>. <b>No verão eles "
             "fecham das 14h30 às 17h</b>, que é justamente quando faz mais calor — "
             "planeje em volta disso. <b>E a noite é o fecho:</b> a <b>visita noturna "
             "aos Palacios Nazaríes</b> custa <b>€ 12,73</b>, entra no mesmo espaço da "
             "diurna com outra luz, e <b>na sexta ela roda em qualquer época do ano</b> "
             "— 20h às 21h30 no inverno, 22h às 23h30 no verão.",
             ["Museo Cuevas do Sacromonte · € 6 · todos os dias",
              "Abadía do Sacromonte é outro lugar · € 7",
              "Bañuelo ou Dar al-Horra · € 2 cada",
              "No verão fecham 14h30–17h",
              "Noturna nos Palacios · € 12,73 · sexta é segura"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de "
                   "custos, apurados em 30 de setembro de 2026 em fonte oficial — a "
                   "<b>Orden de 17 de julio de 2025</b> publicada no BOJA, a página de "
                   "horários e tarifas do Patronato da Alhambra, o site de reservas "
                   "gratuitas da diocese de Granada, o canal oficial de venda das "
                   "igrejas e o caixa do Museo Cuevas del Sacromonte. "
                   "<b>Três coisas ficaram sem resposta, e estão ditas nas fichas:</b> "
                   "o caixa da Alhambra está atrás de verificação anti-bot e não abriu, "
                   "então <b>o valor final do ingresso não está confirmado</b>; a "
                   "Capilla Real não publica horário por dia da semana e o próprio site "
                   "pede que se telefone; e a tapa grátis, que é tradição real de "
                   "Granada, <b>não tem norma, obrigação nem valor publicado</b> — e a "
                   "página da andalucia.org devolveu 403 à conferência. "
                   "<b>Não contornamos bloqueio.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
