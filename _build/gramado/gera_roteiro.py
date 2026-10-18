# -*- coding: utf-8 -*-
"""Roteiro de 4 dias em Gramado e Canela, montado pelo calendario.

Mesmo molde do barcelona/gera_roteiro.py.

O QUE O CALENDARIO DECIDE
-------------------------
    quarta   Snowland e Mundo a Vapor fecham (o calendario de compra da
             Snowland marca todas as quartas de outubro de 2026 como
             "Parque Fechado"; o Mundo a Vapor diz "fechado nas
             quartas-feiras"). O roteiro comeca na quinta.
    sexta,   a Parada de Natal (gratis) so acontece sexta, sabado e
    sabado,  domingo as 15h, na Borges de Medeiros
    domingo
    fim de   o Caracol abre ate 18h (entrada ate 17h30), uma hora a
    semana   mais que nos dias uteis - por isso Canela fica no sabado

POR QUE QUINTA, SEXTA, SABADO E DOMINGO
---------------------------------------
    quinta   o centro a pe: Lago Negro, Rua Coberta, Mini Mundo, e o
             Show de Acendimento as 20h, de graca
    sexta    Snowland de manha (10h-17h), Dreamland a tarde
    sabado   Canela: Caracol (ate 18h no fim de semana) e Mundo a Vapor
    domingo  GramadoZoo de manha (ultima entrada 16h), Parada de Natal
             as 15h, e o Grande Desfile se houver sessao naquela noite

A ARMADILHA QUE MAIS PEGA
--------------------------
O Caracol cobra R$ 134,90 de quem nao e do RS e R$ 67,00 de gaucho, e
morador de Canela e Gramado nao paga. Quem e do RS e compra pela aba
errada paga o dobro. O aviso "a" existe por isso.

Uso
---
    python _build/gramado/gera_roteiro.py
    python _build/gramado/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_gramado_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "gramado": {
        "dias": 4,
        "titulo": "Roteiro de 4 dias em Gramado",
        "descricao": ("Quatro dias em Gramado e Canela na ordem que o calendário "
                      "permite: a quarta-feira que fecha dois parques, o Caracol no fim "
                      "de semana e as atrações gratuitas do Natal Luz."),
        "abertura": ("Quatro dias de quinta a domingo, porque <b>a quarta-feira fecha a "
                     "Snowland e o Mundo a Vapor</b> e porque a Parada de Natal, que é "
                     "de graça, só acontece de sexta a domingo. <b>E uma conta que muda "
                     "pela origem:</b> o Parque do Caracol cobra R$ 134,90 de quem vem "
                     "de fora do RS e R$ 67,00 de gaúcho."),
        "avisos": [
            ("a", "O Caracol tem três preços para o mesmo bilhete — compre na aba certa",
             "<p>A página de compra oficial do Parque do Caracol tem <b>três abas de "
             "categoria</b>, e o preço muda com ela:</p>"
             "<p><b>“Brasileiros e Estrangeiros”:</b> Bilhete Caracol, <b>inteira a "
             "partir de R$ 134,90</b>.</p>"
             "<p><b>“Gaúchos e Residentes do RS”:</b> Bilhete Gaúcho, <b>adulto a partir "
             "de R$ 67,00</b> — nascido ou morador do RS, com comprovação.</p>"
             "<p><b>“Canelense e Gramadense”:</b> <b>grátis</b>, com comprovante de "
             "residência e documento com foto.</p>"
             "<p><b>Quem é do RS e compra pela primeira aba paga o dobro.</b> E quem não é "
             "e compra pela segunda leva a diferença cobrada na bilheteria, porque a "
             "comprovação é exigida.</p>"),
            ("b", "A quarta-feira fecha dois parques — por isso o roteiro começa na quinta",
             "<p>O <b>Mundo a Vapor</b>, em Canela, diz no próprio site: <b>“fechado nas "
             "quartas-feiras”</b>.</p>"
             "<p>A <b>Snowland</b> diz que abre todos os dias, das 10h às 17h — mas <b>o "
             "calendário de compra de outubro de 2026 marca as quatro quartas como "
             "“Parque Fechado”</b>. Confira o dia no calendário antes de contar com "
             "ele.</p>"
             "<p><b>Se a sua viagem incluir uma quarta</b>, ponha nela o centro a pé, os "
             "lagos e o Mini Mundo, que abre todos os dias.</p>"),
            ("a", "A taxa de turismo foi revogada — a Room Tax que ficou é voluntária",
             "<p>A <b>Taxa de Turismo Sustentável</b>, de <b>R$ 3,43 por dia e por "
             "apartamento</b>, teve a revogação aprovada pela Câmara de Gramado em "
             "<b>13 de abril de 2026</b>, depois de acordo com o Ministério Público do "
             "RS. Não achamos a sanção publicada.</p>"
             "<p>No lugar, o <b>Gramado Canela Convention & Visitors Bureau</b> anunciou "
             "a volta da <b>Room Tax</b>, cobrada no check-out pelos hotéis, no mesmo "
             "valor — e, segundo a reportagem de maio, <b>“será opcional o pagamento por "
             "parte dos hóspedes”</b>.</p>"
             "<p><b>Se a linha aparecer na sua conta, você pode pedir para tirar.</b></p>"),
            ("b", "Natal Luz: quatro espetáculos cobram, cinco atrações não",
             "<p>De <b>22 de outubro de 2026 a 17 de janeiro de 2027</b>. Os pagos: o "
             "<b>Grande Desfile</b> (inteira R$ 420), o <b>Nativitaten</b> (R$ 360) e dois "
             "shows no Palácio dos Festivais (R$ 120 cada). <b>O lote com 5% de "
             "desconto acaba em 21 de outubro.</b></p>"
             "<p>Os gratuitos: a <b>Vila de Natal</b> (todo dia, 9h às 21h), o <b>Show de "
             "Acendimento</b> (todo dia, 20h), a <b>Parada de Natal</b> (sexta a domingo, "
             "15h), o <b>palco da Rua Coberta</b> (terça a domingo, 18h30) e o "
             "<b>Caminho de Luzes</b> (terças, 18h30).</p>"
             "<p><b>O mesmo site diz que a Vila e o Acendimento vão só até 10 de "
             "janeiro</b>, uma semana antes do fim do evento.</p>"),
            ("a", "O que este roteiro não alcança, e está dito",
             "<p><b>A hospedagem.</b> Nenhum órgão publica a diária média de Gramado, e a "
             "ficha de custos fica sem ela em vez de estimar.</p>"
             "<p><b>O calendário das noites do Grande Desfile e do Nativitaten</b>, que "
             "não estava na página inicial do site oficial — o domingo deste roteiro só "
             "tem desfile se houver sessão naquela noite.</p>"
             "<p><b>O Le Jardin, parque de lavanda</b>: o site recusou a conexão, e ele "
             "ficou de fora.</p>"
             "<p><b>Os preços “a partir de”</b> — Snowland, Dreamland, Bustour — e o "
             "Mundo a Vapor, que mostra dois números sem dizer qual vale.</p>"),
        ],
        "dias_lista": [
            ("Quinta — o centro a pé, o Mini Mundo e o Acendimento de graça",
             "<b>Comece pelo que a Secretaria de Turismo lista como gratuito.</b> O "
             "<b>Lago Negro</b> tem acesso livre, aberto 24 horas; o pedalinho, das 8h30 "
             "às 18h, cobra — e o valor não está publicado. Volte ao centro pela Borges "
             "de Medeiros até a <b>Rua Coberta</b>, de acesso e horário livres. À tarde, "
             "o <b>Mini Mundo</b>: <b>R$ 156</b> a inteira e <b>R$ 78 de 3 a 15 anos</b> e "
             "acima de 60 — a meia de criança aqui vai até 15. Abre todo dia, 9h às 17h, "
             "e não fecha por chuva. <b>Às 20h, o Show de Acendimento do Natal Luz</b>, "
             "no Palácio dos Festivais, é de graça todo dia; a <b>Vila de Natal</b>, na "
             "Praça das Etnias, fica aberta até 21h.",
             ["Lago Negro · grátis · 24h",
              "Pedalinho · 8h30–18h · valor não publicado",
              "Mini Mundo · R$ 156 · meia até 15 anos",
              "Show de Acendimento · 20h · grátis",
              "Vila de Natal · até 21h · grátis"]),

            ("Sexta — a Snowland de manhã e o Museu de Cera à tarde",
             "<b>Snowland às 10h</b>, quando abre: <b>a partir de R$ 144,50</b> numa "
             "quinta de média temporada, com o kit de botas, calça, jaqueta e luvas "
             "incluído — e o preço muda com a data, em quatro temporadas. Meia e "
             "morador da serra: R$ 86,70, com documento original. <b>A bilheteria não "
             "tem o desconto de compra antecipada</b>: compre antes. À tarde, de volta à "
             "Av. das Hortênsias, o <b>Dreamland Museu de Cera</b> a partir de "
             "<b>R$ 89,99</b>. O passaporte com mais seis atrações do mesmo grupo, a "
             "partir de R$ 219,99, só compensa a partir da terceira. <b>Às 15h de sexta "
             "há a Parada de Natal</b> na Borges de Medeiros — de graça, se der para "
             "encaixar.",
             ["Snowland · desde R$ 144,50 · 10h–17h",
              "Kit de roupas incluído",
              "Bilheteria sem desconto antecipado",
              "Museu de Cera · desde R$ 89,99",
              "Parada de Natal · 15h · grátis"]),

            ("Sábado — Canela: a cascata e o Mundo a Vapor",
             "<b>O Parque do Caracol abre das 9h às 18h no fim de semana</b>, uma hora a "
             "mais que nos dias úteis, com entrada até 17h30. <b>Compre na aba certa:</b> "
             "R$ 134,90 para quem é de fora do RS, <b>R$ 67,00 para gaúcho</b>, grátis "
             "para morador de Canela e Gramado. Corajoso e Ousado são à parte. Depois, "
             "o <b>Mundo a Vapor</b>, também em Canela, das 9h às 18h30: o passaporte "
             "adulto aparece por <b>R$ 129 e R$ 149</b> na mesma página, sem dizer qual "
             "vale — e inclui a visita guiada às dez salas, o trem no bosque e a "
             "roda-gigante. <b>É sábado porque o Mundo a Vapor fecha na quarta</b> e "
             "porque o Caracol rende mais com a hora extra. O <b>Bustour</b>, desde "
             "R$ 78 o dia, liga as duas cidades.",
             ["Caracol · R$ 134,90 · gaúcho R$ 67",
              "Morador de Canela/Gramado · grátis",
              "Fim de semana até 18h",
              "Mundo a Vapor · R$ 129 ou R$ 149 · fecha quarta",
              "Bustour · desde R$ 78 o dia"]),

            ("Domingo — o zoológico cedo, a Parada às 15h e o Desfile se houver",
             "<b>GramadoZoo de manhã</b>: abre às 10h, e <b>16h é a última entrada</b>. "
             "Ingresso único de <b>R$ 115</b>, menor de 3 não paga, estacionamento "
             "R$ 20 — e chuva forte pode fechar sem aviso. <b>Às 15h, a Parada de "
             "Natal</b> na Av. Borges de Medeiros, de graça. <b>À noite, o Grande "
             "Desfile de Natal</b>, na Expogramado — <b>inteira R$ 420</b>, meia a partir "
             "de R$ 210 — <b>se houver sessão nesse domingo</b>: o calendário das noites "
             "não estava na página inicial do site oficial, e o desfile não acontece "
             "todo dia. Sem desfile, o Acendimento das 20h e a Vila de Natal continuam "
             "de graça.",
             ["GramadoZoo · R$ 115 · última entrada 16h",
              "Estacionamento · R$ 20",
              "Parada de Natal · 15h · grátis",
              "Grande Desfile · R$ 420 · confira a noite",
              "Acendimento · 20h · grátis"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de "
                   "custos, apurados em 18 de outubro de 2026 nas lojas e páginas "
                   "oficiais de cada parque, no site oficial do Natal Luz e no portal "
                   "da Secretaria de Turismo de Gramado. <b>Quatro coisas ficaram sem "
                   "resposta, e estão ditas nas fichas:</b> a diária de hospedagem, que "
                   "ninguém publica; o calendário das noites do Natal Luz; qual dos dois "
                   "preços do Mundo a Vapor vale; e o valor do pedalinho do Lago Negro. "
                   "<b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
