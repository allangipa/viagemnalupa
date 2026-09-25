# -*- coding: utf-8 -*-
"""Roteiros de 5 dias de Bariloche e Punta Cana.

Reusa o renderizador de novos/gera_roteiro.py, como a ficha de custos faz.

O QUE ORGANIZA CADA UM DOS DOIS E DIFERENTE, E E O ASSUNTO DA PAGINA

Bariloche se organiza pela TAXA DO PARQUE, que e por dia e tem 50% de
desconto no segundo. Isso muda a ordem dos dias, e e a informacao que nao
esta em folheto nenhum. Alem disso o Circuito Chico nao passa por posto de
cobranca - da para fazer um dia inteiro de paisagem sem pagar taxa.

Punta Cana se organiza pela AUSENCIA DE HORARIO PUBLICADO. Cinco dos sete
pontos nao divulgam horario de funcionamento em fonte confiavel; o que
existe e agenda de operador. Entao o roteiro nao promete hora: promete
sequencia, e diz o que confirmar por escrito antes de pagar.

Uso
---
    python _build/novos2/gera_roteiro.py
    python _build/novos2/gera_roteiro.py --aplica
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_roteiro as base  # noqa: E402

ROTEIROS = {
    "bariloche": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Bariloche",
        "descricao": ("Cinco dias em Bariloche na ordem que aproveita os 50% de desconto "
                      "do segundo dia de parque — e o dia inteiro de paisagem que não "
                      "passa por posto de cobrança."),
        "abertura": ("Cinco dias organizados por uma coisa que folheto nenhum diz: "
                     "<b>a taxa do Parque Nacional é por dia</b>, e o segundo dia custa "
                     "metade."),
        "avisos": [
            ("b", "A taxa do parque é por dia, e é ela que decide a ordem",
             "<p>A entrada do Parque Nacional Nahuel Huapi custa <b>ARS 35.000 por dia</b> "
             "para estrangeiro, e <b>o segundo dia sai pela metade</b>. Não é passe de "
             "visita: é cobrança diária.</p>"
             "<p><b>Por isso os dias de lago vêm juntos aqui</b>, e não espalhados pela "
             "semana. <span class=\"flag\">O que não apuramos</span> quais atividades "
             "passam por posto de cobrança e quais não — sabemos que o Circuito Chico não "
             "passa, porque o próprio parque diz, e que Puerto Blest cobra à parte, porque "
             "o operador diz. Para as demais, confirme na bilheteria.</p>"),
            ("a", "O preço anunciado da Isla Victoria não é o que você paga",
             "<p>O anúncio mostra a excursão de adulto. <b>São três cobranças</b>: a "
             "excursão, a taxa portuária e a entrada do parque. Somadas, "
             "<b>ARS 182.600</b> — e é o número que mais surpreende quem só viu o "
             "primeiro.</p>"),
            ("c", "O museu fecha no meio do dia, e não abre domingo nem segunda",
             "<p>O <b>Museo de la Patagonia</b> fecha domingo e segunda. De terça a sexta "
             "abre das 10h às 12h30 e das 14h às 19h — <b>fecha no almoço</b>. Sábado é o "
             "único dia corrido, das 10h às 17h.</p>"
             "<p>Se os seus cinco dias caírem de sexta a terça, o museu só cabe na sexta ou "
             "no sábado.</p>"),
        ],
        "dias_lista": [
            ("A cidade, e o que ela não cobra",
             "Comece pelo <b>Centro Cívico</b>, que é o coração da cidade e não tem "
             "bilheteria. Ali mesmo fica o <b>Museo de la Patagonia</b>, de contribuição "
             "voluntária — <b>mas confira o dia</b>: fecha domingo e segunda, e de terça a "
             "sexta fecha das 12h30 às 14h. À tarde, <b>Colonia Suiza</b>. Se o seu dia cair "
             "numa quarta ou num domingo, você pega a feira; nos outros dias o vilarejo é "
             "bem mais parado, e vale saber disso antes de atravessar a cidade.",
             ["Museo de la Patagonia · contribuição · fecha dom e seg",
              "Museo · fecha 12h30 às 14h de terça a sexta",
              "Colonia Suiza · feira só quarta e domingo"]),
            ("Circuito Chico e Cerro Campanario — o dia de paisagem sem taxa",
             "Este é o dia que rende mais por menos. O <b>Circuito Chico</b> é estrada "
             "aberta o ano todo, sem horário e sem bilheteria, e <b>não passa por posto de "
             "cobrança do Parque Nacional</b> — dá para fazer o circuito inteiro sem pagar "
             "os ARS 35.000. No meio dele, no quilômetro 17,5 da Avenida Bustillo, sobe a "
             "aerossilha do <b>Cerro Campanario</b>, das 9h às 17h30, por ARS 18.000. "
             "<b>Dá para subir a pé pela trilha e não pagar nada</b>, se o joelho e o tempo "
             "ajudarem. Feche no <b>Punto Panorámico</b>, que também não cobra.",
             ["Circuito Chico · grátis, sem posto de cobrança",
              "Cerro Campanario · ARS 18.000 · 9h às 17h30",
              "Campanario a pé · trilha, sem custo"]),
            ("Puerto Blest — o primeiro dia de taxa",
             "Excursão de <b>dia inteiro</b>, com saída de manhã e retorno por volta das "
             "17h30. São <b>ARS 136.000</b> pela Turisur, com sinal de ARS 24.000 na reserva "
             "e o saldo no dia. <b>O valor não inclui a entrada do parque</b>, que é cobrada "
             "à parte — então este é o dia em que você paga os ARS 35.000 cheios. Inclui a "
             "navegação e a caminhada guiada por passarelas de madeira pela selva valdiviana "
             "até a <b>Cascada Los Cántaros</b>. Há um trecho opcional até o Lago Frías.",
             ["Puerto Blest · ARS 136.000 · dia inteiro",
              "Taxa do parque · ARS 35.000 à parte",
              "Retorno · por volta das 17h30"]),
            ("Isla Victoria e Bosque de Arrayanes — o segundo dia, pela metade",
             "Fazer este no dia seguinte ao de Puerto Blest é o que aproveita <b>os 50% do "
             "segundo dia de parque</b>. São <b>ARS 182.600</b> no total, com as três "
             "cobranças somadas. Há dois turnos: o <b>integral</b> tem transfer às 10h20, "
             "embarque às 11h40 e retorno às 18h30, com cerca de 2h30 na Isla Victoria e 45 "
             "minutos no Bosque de Arrayanes; o de <b>meio-dia</b> sai depois e é mais curto. "
             "Se for fazer os dois passeios de lago, <b>o integral é o que justifica o "
             "preço</b>.",
             ["Isla Victoria · ARS 182.600 · três cobranças",
              "Turno integral · 10h20 às 18h30",
              "Segundo dia de parque · 50% de desconto"]),
            ("O cerro — e o dia mais flexível dos cinco",
             "Escolha um. O <b>Cerro Catedral</b> tem passe pedestre de <b>ARS 90.000</b> e "
             "abre todos os dias das 8h às 16h, com bilheteria da base até as 16h30 — meia "
             "hora a mais que os meios de elevação, o que engana quem chega no limite. O "
             "<b>Teleférico Cerro Otto</b> sai por <b>ARS 60.000</b>, com base e bilheteria "
             "das 10h às 16h30, e tem <b>transporte gratuito da cidade até a base</b>, "
             "saindo do centro. <b>Otto é o mais barato e o mais fácil de alcançar sem "
             "carro</b>; Catedral é o mais alto. <span class=\"flag\">O que não apuramos</span> "
             "tabela de verão do Catedral — os valores publicados não separam temporada.",
             ["Cerro Catedral · ARS 90.000 · 8h às 16h",
              "Cerro Otto · ARS 60.000 · transporte grátis da cidade",
              "Catedral · bilheteria fecha 16h30, elevação às 16h"]),
        ],
        "fontes": ("Horários e tarifas das páginas oficiais do Parque Nacional Nahuel Huapi, "
                   "da Catedral Alta Patagonia, do Teleférico Cerro Otto e dos operadores da "
                   "Isla Victoria e de Puerto Blest, consultadas em 17 de setembro de 2026. "
                   "<b>A ordem dos dias é nossa</b>, e o motivo dela está dito em cada dia."),
    },

    "punta-cana": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Punta Cana",
        "descricao": ("Cinco dias em Punta Cana montados sobre o que dá para confirmar — e "
                      "a advertência de que cinco dos sete pontos não publicam horário."),
        "abertura": ("Cinco dias em sequência, não em horário. <b>Cinco dos sete pontos não "
                     "publicam horário de funcionamento</b> em fonte confiável, e este "
                     "roteiro diz isso em vez de inventar uma agenda."),
        "avisos": [
            ("b", "Aqui quase nada publica horário, e isso muda como se planeja",
             "<p>Em Cancún ou em Lisboa dá para montar o dia pela última entrada. "
             "<b>Em Punta Cana, não.</b> O Scape Park, a Reserva Ojos Indígenas, Altos de "
             "Chavón, a Isla Saona e Los Haitises <b>não divulgam horário</b> em fonte que "
             "tenhamos encontrado — o que existe é a agenda do operador que vende a "
             "excursão.</p>"
             "<p>Por isso este roteiro organiza <b>a sequência</b> e não a hora. Quem define "
             "a hora é quem vende o passeio, e é com ele que você confirma.</p>"),
            ("a", "Confirme por escrito antes de pagar",
             "<p>Como o preço não é tabelado e a agenda é do operador, peça por escrito, "
             "antes de pagar: <b>preço final, hora e local de embarque, e o que está "
             "incluído</b>. A Isla Saona varia de <b>US$ 75 a 135</b> conforme quem vende, e "
             "é a mesma ilha.</p>"),
            ("c", "A praia é pública por lei, inclusive em frente a resort",
             "<p>A legislação dominicana declara as praias de uso público. <b>Nenhum hotel "
             "pode fechar a faixa de areia.</b> O que o hotel cobra é o que é dele: "
             "espreguiçadeira, guarda-sol, bar, banheiro.</p>"
             "<p>Isso vale para <b>Bávaro</b> e para <b>Macao</b>, e é o que garante dois "
             "dos cinco dias sem custo de entrada.</p>"),
        ],
        "dias_lista": [
            ("Playa Bávaro — o dia que não depende de ninguém",
             "Comece pelo que está sempre aberto e não tem bilheteria. <b>Playa Bávaro</b> "
             "não tem horário nem portão, e o acesso é <b>garantido por lei</b> mesmo no "
             "trecho em frente aos resorts. Você paga se usar o que é do hotel — "
             "espreguiçadeira, guarda-sol, bar —, não pela areia. É o dia de ajustar o fuso "
             "e entender a geografia do lugar antes de comprar qualquer excursão.",
             ["Playa Bávaro · grátis · sempre aberta",
              "Acesso garantido por lei, inclusive em frente a resort",
              "O que se paga é o serviço do hotel, não a areia"]),
            ("Hoyo Azul e Scape Park — e vá cedo",
             "A <b>admissão geral do Scape Park custa US$ 129</b> e inclui o cenote e as "
             "demais atividades; <b>só o Hoyo Azul sai por US$ 65</b>, e para muita gente é "
             "o que interessa. <span class=\"flag\">Não apuramos o horário</span> nenhuma "
             "fonte consultada publicava abertura e fechamento. <b>A única recomendação "
             "consistente é chegar entre 8h e 9h</b>, para evitar fila — e é a que seguimos "
             "aqui ao pôr este dia cedo na semana, quando você ainda está acordando no "
             "horário de casa.",
             ["Scape Park completo · US$ 129",
              "Só o cenote · US$ 65",
              "Ir entre 8h e 9h · única indicação de horário que achamos"]),
            ("Isla Saona — dia inteiro, e o dia de ler o contrato",
             "Excursão compartilhada de <b>dia inteiro</b>, de <b>US$ 75 a 135</b> conforme o "
             "operador. <span class=\"flag\">Não há tarifa única</span> nem horário público "
             "do parque: cada operador tem o seu. É por isso que este é o dia em que vale "
             "<b>confirmar por escrito antes de pagar</b> — preço final, hora e local de "
             "embarque, e o que está incluído. Duas excursões de dia inteiro não cabem no "
             "mesmo dia, então esta e Los Haitises competem entre si.",
             ["Isla Saona · US$ 75 a 135 · dia inteiro",
              "Sem tarifa única · varia por operador",
              "Alternativa do mesmo dia · Los Haitises"]),
            ("Altos de Chavón — duas horas de estrada em cada sentido",
             "<b>US$ 60 por adulto</b> em excursão, US$ 35 para criança de 4 a 12 anos. "
             "<b>Não é bilheteria</b>: é o pacote de quem sai de Punta Cana, e o preço "
             "inclui o transporte de cerca de duas horas em cada sentido. A visita costuma "
             "incluir o anfiteatro. <span class=\"flag\">Não apuramos o horário</span> a vila "
             "não publica horário de visitação — quem vai em excursão segue o do operador.",
             ["Altos de Chavón · US$ 60 · criança US$ 35",
              "Cerca de 2h de estrada em cada sentido",
              "Horário · do operador, não publicado pela vila"]),
            ("Playa Macao, e o que sobrar",
             "Feche com <b>Playa Macao</b>, a praia pública mais aberta da região, sem "
             "horário e sem bilheteria. <b>Mas saiba o que vai encontrar</b>: o mar de Macao "
             "é bem mais agitado que o de Bávaro — é praia de onda, usada para surfe, e não "
             "a piscina calma dos folhetos. Se sobrar meio dia, a <b>Reserva Ecológica Ojos "
             "Indígenas</b> é curta e fica perto; <span class=\"flag\">as fontes divergem no "
             "preço</span>, US$ 50 numa e US$ 15 em outra, e se você estiver num dos hotéis "
             "do grupo a entrada não custa nada.",
             ["Playa Macao · grátis · praia de onda",
              "Ojos Indígenas · US$ 15 ou US$ 50, fontes divergem",
              "Hóspede do grupo · entrada sem custo"]),
        ],
        "fontes": ("Tarifas consultadas em 17 de setembro de 2026. <b>Punta Cana é o destino "
                   "com menos informação oficial publicada do site</b>: onde não há horário, "
                   "isso está dito; onde duas fontes divergem no preço, as duas ficam. A "
                   "ordem dos dias é nossa, e o motivo está em cada dia."),
    },
}

# O renderizador procura o destino na lista DESTINOS do novos/dados.py, e
# Bariloche e Punta Cana moram no novos2/dados.py. Sem trocar, ele levanta
# StopIteration sem dizer o que faltou.
#
# E NAO DA PARA FAZER ISSO COM `from dados import`: quando o renderizador foi
# importado acima, ele ja carregou o `dados` do novos e deixou em
# sys.modules. Um import normal devolveria o modulo errado, calado. Por isso
# o arquivo e carregado por CAMINHO, com nome proprio.
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location(
    "dados_novos2", os.path.join(AQUI, "dados.py"))
_d2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d2)
base.DESTINOS = _d2.DESTINOS
base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
