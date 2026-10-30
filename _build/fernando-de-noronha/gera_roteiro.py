# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Fernando de Noronha, montado pelo relogio.

Mesmo molde do foz-do-iguacu/gera_roteiro.py.

O QUE DECIDE A ORDEM
--------------------
Em Noronha quem manda nao e o dia da semana - nenhum atrativo do Parque
fecha num dia fixo -, e sim o relogio e a mare:

    6h30   a Baia dos Golfinhos abre; os rotadores descansam ali
           "principalmente no inicio da manha"
    8h     o Sancho abre, e a escada fica livre ate 8h50; de 9h em diante
           alterna descida e subida, com fila de manha
    mare   a Atalaia e as outras piscinas abrem pela mare baixa, com vaga
    baixa  agendada - por isso o ingresso e o agendamento vem no dia 1
    9h-16h a faixa de areia do Sueste, sem banho

POR QUE ESTA ORDEM
------------------
    dia 1  chegada: TPA paga, ingresso e agendamento no Centro de
           Visitantes (8h-19h), praias de acesso livre
    dia 2  Golfinhos as 6h30, Sancho as 8h, Baia dos Porcos pela Cacimba
    dia 3  Atalaia no horario da mare; Leao e Caracas a tarde
    dia 4  Sueste (9h-16h) e o barco, de empresa autorizada
    dia 5  praias livres e a volta

Uso
---
    python _build/fernando-de-noronha/gera_roteiro.py
    python _build/fernando-de-noronha/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_noronha_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "fernando-de-noronha": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Fernando de Noronha",
        "descricao": ("Cinco dias em Fernando de Noronha na ordem que o relógio e a maré "
                      "permitem: os golfinhos às 6h30, a escada do Sancho às 8h e as "
                      "piscinas naturais com hora marcada."),
        "abertura": ("Cinco dias, porque é a permanência que a tabela da TPA cobra por "
                     "R$ 520,50 — e porque em Noronha quem manda não é o dia da semana, "
                     "é <b>o relógio e a maré</b>: os golfinhos de manhã cedo, a escada "
                     "do Sancho que alterna descida e subida, e as piscinas naturais que "
                     "só abrem na maré baixa, com vaga agendada."),
        "avisos": [
            ("a", "A TPA barateia até o 10º dia — e o 11º custa mais que o primeiro",
             "<p>A tabela oficial de 2026: <b>1 dia R$ 105,79 · 5 dias R$ 520,50 · 10 "
             "dias R$ 901,36</b>. Dez dias saem a R$ 90,14 por dia.</p>"
             "<p><b>No 11º dia, R$ 1.028,31</b>: só esse dia custa R$ 126,95. Trinta dias "
             "chegam a R$ 7.460,56.</p>"
             "<p><b>E ficar além do previsto sai em dobro</b>, se a permanência não foi "
             "agendada. A página não diz se o dia da chegada e o da partida contam; o "
             "site de pagamento pede as datas.</p>"),
            ("b", "Compre o ingresso e agende as trilhas no primeiro dia",
             "<p>As piscinas naturais — Atalaia, Capim-Açu, Abreu, Pontinha–Caieira, "
             "Morro São José — têm <b>vagas por dia</b> e horário pela <b>maré baixa</b>. "
             "<b>Sem o número do ingresso, não se agenda.</b></p>"
             "<p>O ingresso (R$ 192, vale 10 dias) se compra online ou no <b>Centro de "
             "Visitantes do Boldró, das 8h às 19h</b>, onde também se agenda.</p>"
             "<p><b>A partir de 1º de novembro de 2026, R$ 196,50</b>, segundo a imprensa "
             "citando o ICMBio.</p>"),
            ("a", "A escada do Sancho tem horário de descer e de subir",
             "<p>Das 8h às 8h50 a escada é livre. Depois alterna: <b>descida às 9h, "
             "11h30, 13h30 e 15h30; subida às 10h30, 12h30 e 14h30</b>, em janelas de "
             "50 a 80 minutos. Das 16h30 às 17h20, livre de novo; das 17h30 às 18h, só "
             "subida.</p>"
             "<p>A página do ICMBio avisa que de manhã pode haver fila longa, e que à "
             "tarde o movimento costuma ser menor. <b>Quem desce às 9h só sobe às "
             "10h30.</b></p>"),
            ("b", "O que este roteiro não alcança, e está dito",
             "<p><b>A hospedagem</b>, que nenhum órgão publica.</p>"
             "<p><b>O preço do barco, do mergulho e do condutor das trilhas longas</b>: "
             "são serviços de empresas autorizadas, sem tabela oficial.</p>"
             "<p><b>A tarifa do ônibus</b>, que só achamos em guias de viagem.</p>"
             "<p><b>O horário de cada trilha agendada</b>, que muda todo dia com a maré e "
             "só aparece na hora de agendar.</p>"),
        ],
        "dias_lista": [
            ("Dia 1 — a chegada, o ingresso e as praias livres",
             "<b>A TPA</b> se paga pela internet antes do embarque ou no desembarque; "
             "cinco dias, <b>R$ 520,50</b>. Com a bagagem deixada, vá ao <b>Centro de "
             "Visitantes do ICMBio, no Boldró</b> (8h às 19h): compre o ingresso do "
             "Parque, <b>R$ 192</b>, e <b>agende a Atalaia</b> para o horário de maré "
             "baixa que houver. O resto do dia é nas praias que não pedem ingresso: "
             "<b>Cacimba do Padre, Conceição, Boldró</b> — da lista oficial de acesso "
             "livre.",
             ["TPA · R$ 520,50 · 5 dias",
              "Ingresso do Parque · R$ 192 · 10 dias",
              "Centro de Visitantes · 8h–19h",
              "Agende a Atalaia",
              "Praias da APA · grátis"]),

            ("Dia 2 — golfinhos cedo, o Sancho e a Baía dos Porcos",
             "<b>Baía dos Golfinhos às 6h30</b>, quando abre: os rotadores descansam ali "
             "principalmente no início da manhã — e não se desce nem se nada na baía. "
             "<b>Sancho às 8h</b>: a escada é livre até 8h50; depois disso, descida às 9h "
             "e subida só às 10h30. À tarde, a <b>Baía dos Porcos</b>, pela trilha no "
             "canto esquerdo da Cacimba do Padre. Tudo dentro do ingresso.",
             ["Golfinhos · 6h30 · só mirante",
              "Sancho · escada livre 8h–8h50",
              "Descida 9h · subida 10h30",
              "Baía dos Porcos · pela Cacimba",
              "Tudo no ingresso"]),

            ("Dia 3 — a piscina da Atalaia e o Leão",
             "<b>Atalaia no horário agendado</b>, que segue a maré baixa: 3 km ida e "
             "volta, colete, máscara e snorkel obrigatórios, <b>sem protetor solar antes "
             "do banho</b> e sem ficar em pé na piscina. Depois, a <b>Praia do Leão</b> "
             "(8h às 18h), com correntes fortes — avalie o mar antes de entrar. De "
             "dezembro a maio é a época de desova da tartaruga-verde. O pôr do sol é no "
             "<b>Mirante da Ponta das Caracas</b>, até as 18h.",
             ["Atalaia · horário da maré",
              "Sem protetor solar antes",
              "Leão · 8h–18h · correntes",
              "Caracas · pôr do sol",
              "Tudo no ingresso"]),

            ("Dia 4 — o Sueste e o mar de barco",
             "<b>Sueste de manhã</b>: a faixa de areia abre das 9h às 16h, com vídeo ou "
             "palestra obrigatórios antes — e <b>o banho está proibido</b>. É para ver, "
             "não para nadar. À tarde, o <b>passeio de barco</b>, só com empresa "
             "autorizada pelo Parque, saindo do Porto de Santo Antônio, onde o ingresso "
             "é conferido. <b>O preço é de cada empresa</b>, e não há tabela oficial.",
             ["Sueste · 9h–16h · banho proibido",
              "Vídeo obrigatório",
              "Barco · empresa autorizada",
              "Preço · sem tabela oficial",
              "Ingresso conferido no porto"]),

            ("Dia 5 — as praias livres e a volta",
             "Antes do voo, as praias que não pedem ingresso e que ainda faltam: "
             "<b>Americano, Bode, Meio, Cachorro</b> e o <b>Porto de Santo Antônio</b>. "
             "<b>Confira as datas da TPA</b>: ficar além do que foi pago sem agendar sai "
             "em dobro.",
             ["Praias da APA · grátis",
              "Americano, Bode, Meio, Cachorro",
              "Porto de Santo Antônio",
              "Dia a mais sem agendar · em dobro"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de "
                   "custos, apurados em 29 de outubro de 2026 na tabela oficial da TPA "
                   "e nas páginas do ICMBio do Parque Nacional Marinho. <b>Quatro coisas "
                   "ficaram sem resposta, e estão ditas nas fichas:</b> a diária de "
                   "hospedagem; o preço do barco, do mergulho e do condutor; a tarifa do "
                   "ônibus; e o horário de cada trilha, que muda com a maré. <b>Nenhum "
                   "valor veio de agregador de viagem.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
