# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Sao Paulo, montado pelos dias gratis.

Mesmo molde do florianopolis/gera_roteiro.py.

O QUE O CALENDARIO DECIDE
-------------------------
Cada um dos sete museus pagos tem uma janela gratis, em dias diferentes.
De quarta a domingo, o roteiro pega seis delas:
    quarta   Ipiranga (so na bilheteria, no dia) e Afro Brasil
    quinta   o centro e o Theatro (vaga liberada na vespera, as 10h)
    sexta    Vila Madalena e o MASP gratis a partir das 18h
    sabado   a Pinacoteca gratis, e o Mercadao
    domingo  Lingua Portuguesa e MAM gratis, a Paulista fechada ate as
             16h e o onibus sem tarifa
So o Museu do Futebol fica pago (R$ 25): ele so nao cobra na terca - e a
terca e o dia em que a Pinacoteca fecha.

Uso
---
    python _build/sao-paulo/gera_roteiro.py
    python _build/sao-paulo/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_sao_paulo_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "sao-paulo": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em São Paulo",
        "descricao": ("Cinco dias em São Paulo, de quarta a domingo, montados pelos dias "
                      "grátis de cada museu: dos R$ 261,20 de ingressos, sobram R$ 25."),
        "abertura": ("Cinco dias de quarta a domingo, montados por uma regra: <b>cada um dos "
                     "sete museus pagos tem o seu dia grátis, e nenhum coincide</b>. Nesta "
                     "ordem, os ingressos caem de <b>R$ 261,20 para R$ 25</b> — só o Museu do "
                     "Futebol, que não cobra apenas na terça. E o domingo fecha a Paulista "
                     "para carros até as 16h, com o ônibus de graça."),
        "avisos": [
            ("a", "Cada museu tem o seu dia grátis — e a terça fecha a Pinacoteca",
             "<p><b>Terça:</b> MASP (o dia todo), Língua Portuguesa e Museu do Futebol. "
             "<b>Quarta:</b> Ipiranga e Afro Brasil. <b>Sexta a partir das 18h:</b> MASP. "
             "<b>Sábado:</b> Pinacoteca. <b>Domingo:</b> MAM e Língua Portuguesa; Pinacoteca "
             "no segundo, Ipiranga no primeiro.</p>"
             "<p><b>A terça, o dia mais grátis da cidade, é o dia em que a Pinacoteca "
             "fecha</b> — ela abre <i>“de quarta a segunda”</i>, inclusive na segunda. Por "
             "isso este roteiro começa na quarta.</p>"),
            ("b", "Grátis com agendamento, grátis sem agendamento",
             "<p><b>MASP:</b> <i>“O agendamento online, inclusive para os dias gratuitos, "
             "continua sendo obrigatório.”</i></p>"
             "<p><b>Ipiranga:</b> o contrário — o grátis <i>“deve ser retirado na "
             "bilheteria, no próprio dia da visita, sem possibilidade de agendamento pelo "
             "site”</i>. Chegue cedo: os ingressos saem a cada 15 minutos, em número "
             "limitado.</p>"
             "<p><b>Theatro Municipal:</b> a visita é grátis, mas a vaga só sai <i>“no dia "
             "anterior à data da visita, a partir das 10h”</i>.</p>"
             "<p><b>Língua Portuguesa:</b> ingresso obrigatório mesmo no dia grátis.</p>"),
            ("a", "O domingo: a Paulista até as 16h, e o ônibus sem tarifa",
             "<p>A Subprefeitura Sé: a Paulista fica só para pedestres <b>das 9h às 16h</b>, "
             "não até 17h ou 19h como dizem os guias. E é suspensa em dia de grande evento.</p>"
             "<p>SPTrans: <i>“Aos domingos, não há cobrança de tarifa nos ônibus”</i>, o dia "
             "inteiro. <b>Metrô e trem continuam cobrando R$ 5,40.</b></p>"),
            ("b", "A diária é mais barata nas férias",
             "<p>Pela FOHB, a diária média dos hotéis de São Paulo em 2025 foi <b>R$ 602</b>, "
             "de <b>R$ 508 em janeiro</b> a <b>R$ 706 em novembro</b>. A cidade vive de feira "
             "e congresso: <b>o fim do ano e as férias são os meses baratos</b>, o contrário "
             "das praias.</p>"),
            ("a", "O que este roteiro não alcança, e está dito",
             "<p><b>O horário do Mercadão</b>, que nenhuma fonte oficial publica.</p>"
             "<p><b>A tarifa própria do Expresso Aeroporto</b>, que não aparece em página "
             "oficial de 2026.</p>"
             "<p><b>Se a obra do Beco do Batman</b>, começada em maio de 2026, já terminou.</p>"
             "<p><b>O preço do Museu do Ipiranga</b> vem da plataforma de venda que o museu "
             "indica, não do site dele.</p>"),
        ],
        "dias_lista": [
            ("Quarta — o Ipiranga e o Ibirapuera, de graça",
             "Comece no <b>Museu do Ipiranga</b>, que é grátis às quartas — mas <b>só "
             "retirando na bilheteria, no dia</b>: ela abre às 10h nos dias grátis, e os "
             "ingressos saem a cada 15 minutos. A última entrada é às 16h, e os jardins são "
             "abertos e grátis. À tarde, o <b>Parque Ibirapuera</b> e o <b>Museu Afro "
             "Brasil</b>, grátis às quartas, até as 17h. E às 10h, de onde estiver, reserve a "
             "<b>visita do Theatro Municipal para amanhã</b>: as vagas saem na véspera.",
             ["Ipiranga · grátis · só bilheteria",
              "Última entrada 16h",
              "Afro Brasil · grátis às quartas",
              "Ibirapuera · grátis",
              "10h · reserve o Theatro de amanhã"]),

            ("Quinta — o Theatro, o centro e o futebol",
             "De manhã, a <b>visita guiada do Theatro Municipal</b>, grátis, com a vaga "
             "reservada ontem; em português há horários às 11h, 13h, 15h e 17h. Ao meio-dia, "
             "se perder a visita, o <b>concerto grátis no foyer</b> não pede reserva. À "
             "tarde, o <b>Museu do Futebol</b>, no Pacaembu: <b>R$ 25</b>, o único ingresso "
             "pago deste roteiro — ele só não cobra na terça. Fecha às 18h, com entrada até "
             "as 17h.",
             ["Theatro · visita grátis reservada",
              "Concerto do meio-dia · sem reserva",
              "Museu do Futebol · R$ 25",
              "Futebol · entrada até 17h",
              "Metrô · R$ 5,40"]),

            ("Sexta — a Vila Madalena e o MASP à noite",
             "De dia, a <b>Vila Madalena</b> e o <b>Beco do Batman</b>, rua pública — com "
             "a ressalva de que a Prefeitura começou uma obra ali em maio de 2026, prevista "
             "para cinco meses. No fim da tarde, a <b>Avenida Paulista</b> e, <b>a partir das "
             "18h, o MASP de graça</b>, até as 21h — com o horário agendado on-line antes, "
             "porque o grátis também exige agendamento. A inteira seria R$ 85.",
             ["Beco do Batman · grátis · obra em 2026",
              "MASP · grátis a partir das 18h",
              "Agende o MASP antes",
              "MASP · entrada até 20h",
              "Vão livre do MASP · público"]),

            ("Sábado — a Pinacoteca e o Mercadão",
             "<b>A Pinacoteca é grátis aos sábados</b>, e um ingresso vale para os três "
             "prédios — Pina Luz, Pina Estação e Pina Contemporânea —, das 10h às 18h, com "
             "entrada até as 17h. Do outro lado da praça fica o Museu da Língua Portuguesa: "
             "<b>no sábado ele cobra</b>, então deixe para amanhã. Depois, o <b>Mercadão</b>, "
             "que não cobra entrada — confirme o horário, que nenhuma fonte oficial "
             "publica.",
             ["Pinacoteca · grátis aos sábados",
              "Um ingresso, três prédios",
              "Língua Portuguesa · cobra no sábado",
              "Mercadão · entrada livre",
              "Horário do Mercadão · confirme"]),

            ("Domingo — a Língua, a Paulista aberta e o MAM",
             "<b>O ônibus municipal não cobra hoje</b>, o dia inteiro. Comece às 9h no "
             "<b>Museu da Língua Portuguesa</b>, grátis aos domingos, com ingresso emitido. "
             "Depois, a <b>Avenida Paulista aberta</b> para pedestres — <b>só até as "
             "16h</b>. Feche no Ibirapuera com o <b>MAM</b>, grátis aos domingos, com entrada "
             "até 17h30. Metrô e trem cobram R$ 5,40 mesmo no domingo.",
             ["Ônibus · grátis o dia todo",
              "Língua Portuguesa · grátis aos domingos",
              "Paulista aberta · 9h às 16h",
              "MAM · grátis aos domingos",
              "Metrô · cobra no domingo"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de custos, "
                   "apurados em 15 de novembro de 2026 nas páginas oficiais de cada museu, "
                   "do Theatro Municipal, da Subprefeitura Sé, da SPTrans, da CPTM e do "
                   "governo do estado. <b>O preço do Museu do Ipiranga vem da plataforma de "
                   "venda que o próprio museu indica</b>, e está marcado. A diária vem da "
                   "FOHB. <b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
