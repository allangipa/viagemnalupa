# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Miami.

Reusa o renderizador de novos/gera_roteiro.py, como os demais.

O QUE ORGANIZA ESTE ROTEIRO
---------------------------
Duas alavancas que folheto nenhum usa, e as duas saem da apuracao:

1. O PAMM E DE GRACA NAS QUINTAS DEPOIS DAS 17h, e fica aberto ate as
   21h nesse dia. Sao quatro horas de entrada livre por semana. Quem
   encaixa a quinta a noite tira US$ 18 da conta - e como o museu FECHA
   terca E quarta, a quinta ja era o dia natural de qualquer forma.

2. O BILHETE DO EVERGLADES VALE 7 DIAS CORRIDOS NAS TRES ENTRADAS. Nao
   e ingresso de uma visita: e passe de uma semana. Quem quer Shark
   Valley e Ernest Coe pode fazer os dois em dias diferentes e pagar uma
   vez so. Quase ninguem sabe, e e a maior economia possivel aqui.

A ARMADILHA QUE DERRUBA MAIS ROTEIRO
------------------------------------
O PAMM fecha DOIS dias por semana, terca e quarta, e quase todo guia
escreve so a terca. O Vizcaya fecha terca. Entao numa terca fecham os
dois, e numa quarta fecha um. O Frost Science abre todo dia e e o plano
B das duas datas.

Uso
---
    python _build/miami/gera_roteiro.py
    python _build/miami/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_roteiro as base  # noqa: E402

# O renderizador procura o destino na lista DESTINOS do novos/dados.py, e
# Miami mora em miami/dados.py. Carregado por CAMINHO pelo mesmo motivo
# anotado no porto/gera_roteiro.py e repetido no de Sevilha: o import
# normal devolveria o `dados` que o renderizador ja deixou em
# sys.modules, calado.
#
# E a troca de APURACAO nao e opcional: o rodape imprime essa data, que
# no renderizador e a do novos (17/set) e aqui e 29/set. Sem ela a pagina
# sairia datada errado - a armadilha que o Porto encontrou e anotou.
_s = importlib.util.spec_from_file_location(
    "dados_miami", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "miami": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Miami",
        "descricao": ("Cinco dias em Miami na ordem que aproveita a quinta-feira "
                      "gratuita do PAMM e os sete dias de validade do bilhete do "
                      "Everglades — e que desvia dos dois dias em que os museus fecham."),
        "abertura": ("Cinco dias organizados por duas coisas que folheto nenhum diz: "
                     "<b>o museu de arte da baía é de graça nas quintas depois das 17h</b>, "
                     "e <b>o bilhete do Everglades vale sete dias, não um</b>."),
        "avisos": [
            ("b", "A terça e a quarta derrubam metade dos museus",
             "<p><b>O Pérez Art Museum fecha terça E quarta-feira.</b> São dois dias por "
             "semana, e quase todo guia escreve só a terça. <b>O Vizcaya fecha terça.</b> "
             "Ou seja: numa terça você perde os dois, e numa quarta perde um.</p>"
             "<p><b>O Frost Science abre todos os dias</b>, das 10h às 17h, e é o plano B "
             "natural dessas duas datas. Se a sua viagem for curta e cair no meio da "
             "semana, é ele que salva o dia de museu.</p>"),
            ("a", "A quinta à noite vale US$ 18 por pessoa",
             "<p>O <b>PAMM é gratuito para todos nas quintas depois das 17h</b>, e fica "
             "aberto até as 21h nesse dia. São quatro horas de entrada livre por semana, "
             "e é a maior economia programável desta cidade.</p>"
             "<p><b>Por isso o dia dos museus da baía está na quinta aqui</b>, e não "
             "espalhado pela semana. Se os seus cinco dias incluírem uma quinta, ponha "
             "esse dia nela — a ordem dos outros quatro é bem mais flexível.</p>"),
            ("c", "O bilhete do Everglades vale sete dias, e quase ninguém usa",
             "<p>Os <b>US$ 35 do veículo valem 7 dias corridos</b>, e valem nas "
             "<b>três entradas</b> do parque: Shark Valley, Ernest Coe e Gulf Coast. "
             "<b>Não é ingresso de uma visita — é passe de uma semana.</b></p>"
             "<p>Quem quiser ver mais de um lado do parque pode voltar noutro dia sem "
             "pagar de novo o veículo. <b>O adicional de não-residente, de US$ 100 por "
             "pessoa, também é cobrado uma vez só nesse período.</b></p>"
             "<p><span class=\"flag\">Confirme na entrada</span> a leitura acima é a do "
             "texto de tarifas do parque. Como há divergência entre páginas oficiais do "
             "NPS sobre passes, vale confirmar na bilheteria antes de contar com a "
             "segunda visita.</p>"),
            ("b", "Duas coisas que não se resolvem sem carro",
             "<p><b>Everglades e Zoo Miami ficam longe e não têm ligação fácil por "
             "transporte público.</b> Os dois exigem carro, e é o mesmo carro que paga os "
             "US$ 35 da entrada do parque.</p>"
             "<p>O resto do roteiro — praia, art déco, Wynwood, Little Havana e os museus "
             "da baía — se resolve a pé, de Metromover ou com corrida curta. "
             "<span class=\"flag\">Tarifas de transporte não apuradas</span> não "
             "levantamos valor de Metromover, Metrorail, ônibus nem diária de locadora, e "
             "nada disso está na ficha de custos.</p>"),
        ],
        "dias_lista": [
            ("South Beach e o Art Deco — o dia sem relógio",
             "Dia de chegada, de propósito: <b>nada aqui tem bilhete nem hora marcada</b>, "
             "então ele aguenta atraso de voo. A praia é pública e ninguém cobra por areia. "
             "O conjunto art déco tombado vai da <b>5ª à 23ª rua</b>, entre a Ocean Drive e "
             "a Collins, e se vê andando, de graça. O <b>Art Deco Welcome Center</b>, na "
             "1001 Ocean Drive, é de onde saem as visitas guiadas da Miami Design "
             "Preservation League — essas são pagas, e não apuramos a tarifa. Feche na "
             "<b>Lincoln Road</b>, calçadão de pedestres a norte. <b>Duas coisas custam "
             "sem avisar:</b> cadeira e guarda-sol na areia são concessão privada dos "
             "hotéis, e a conta de restaurante na Ocean Drive costuma vir com <b>serviço "
             "já incluído</b> — confira antes de somar gorjeta por cima.",
             ["Praia e ruas · grátis, sem horário",
              "Art Deco District · 5ª à 23ª rua",
              "Visita guiada da MDPL · paga, tarifa não apurada",
              "Cadeira de praia · concessão privada, custa"]),

            ("Wynwood e Little Havana — e a distinção que economiza",
             "Dois bairros, e em ambos vale saber o que é pago e o que não é. Em "
             "<b>Wynwood</b>, o <b>Wynwood Walls é um recinto fechado e cobra</b> — mas "
             "não publica quanto: o valor só aparece no checkout. <b>O bairro em volta é "
             "rua aberta e não custa nada</b>, e tem mural em quase todo quarteirão. Muita "
             "gente paga sem saber que a caminhada externa é gratuita; decida qual das "
             "duas coisas você quer. Abre todos os dias, 10h30 às 18h30. À tarde, "
             "<b>Little Havana</b>: a <b>Calle Ocho</b> é via pública, o Parque do Dominó "
             "também, e não existe bilheteria. <b>Se o seu dia for a última sexta do "
             "mês</b>, você pega a <b>Viernes Culturales</b>, à noite, com galerias "
             "abertas e música na rua — é o melhor momento possível para este bairro, e "
             "acontece uma vez por mês.",
             ["Wynwood Walls · cobra, valor só no checkout",
              "Bairro de Wynwood · rua aberta, grátis",
              "Calle Ocho e Parque do Dominó · grátis",
              "Viernes Culturales · última sexta do mês, à noite"]),

            ("Everglades — o dia de carro, e o dia caro",
             "O dia mais caro da viagem, e o que mais surpreende brasileiro. <b>A tarifa "
             "do veículo é US$ 35 e vale 7 dias</b> — mas, desde 1º de janeiro de 2026, "
             "<b>cada pessoa de 16 anos ou mais que não mora nos Estados Unidos paga "
             "US$ 100 a mais</b>. Uma pessoa de carro sai por <b>US$ 135</b>; um casal, "
             "por <b>US$ 235</b>. <b>O parque não aceita dinheiro</b>, só cartão ou passe "
             "digital. <b>Shark Valley</b>, na US-41 a oeste da cidade, é a entrada mais "
             "próxima e a do trenzinho e das bicicletas; <b>Ernest F. Coe</b>, perto de "
             "Homestead, é a principal ao sul. Como o bilhete vale a semana, dá para "
             "voltar noutro dia na outra entrada sem pagar de novo. <b>E não conte com os "
             "dias de entrada gratuita:</b> desde 2026 eles valem apenas para cidadãos e "
             "residentes americanos.",
             ["Veículo · US$ 35 · vale 7 dias, 3 entradas",
              "Adicional de não-residente · US$ 100 por pessoa",
              "Casal de carro · US$ 235 no total",
              "Não aceita dinheiro · só cartão",
              "Dia grátis do NPS · não vale para estrangeiro"]),

            ("Os museus da baía — de preferência numa quinta",
             "<b>Ponha este dia numa quinta, se puder.</b> O <b>Pérez Art Museum</b> custa "
             "US$ 18, mas é <b>gratuito para todos depois das 17h</b> na quinta, e fica "
             "aberto até as 21h só nesse dia. Comece então pelo <b>Frost Science</b>, no "
             "mesmo parque, a poucos minutos a pé: das 10h às 17h, a partir de US$ 29,95, "
             "e <b>um ingresso só cobre exposições, aquário e uma sessão do planetário</b> "
             "— escolha a sessão ao entrar, porque é uma por bilhete. Atravesse para o "
             "PAMM às 17h e entre de graça. <b>Se a sua viagem não tiver quinta</b>, o dia "
             "ainda funciona — só não faça numa <b>terça ou quarta</b>, quando o PAMM está "
             "fechado. A bilheteria dele para de vender 30 minutos antes de fechar, e o "
             "ingresso pode esgotar.",
             ["Frost Science · 10h às 17h · a partir de US$ 29,95",
              "PAMM · US$ 18 · grátis quinta após 17h",
              "PAMM · fecha terça E quarta",
              "Os dois · mesmo parque, a pé"]),

            ("Vizcaya e Coconut Grove — e a troca para quem tem criança",
             "Último dia, ao sul. O <b>Vizcaya</b> <b>fecha às terças</b> e abre das 9h30 "
             "às <b>16h30</b> — <b>mais cedo que qualquer outro ponto pago desta ficha</b>. "
             "Fim de tarde ali não existe: às 16h30 o portão fecha. Vá de manhã. O preço "
             "não está publicado em tabela: a casa vende por tipo de visita, numa faixa de "
             "<b>US$ 24 a US$ 39</b>, e criança de até 5 anos não paga. Em volta fica "
             "<b>Coconut Grove</b>, para o resto da tarde. <b>A troca:</b> se a viagem for "
             "com criança, o <b>Zoo Miami</b> substitui este dia — US$ 30 o adulto e "
             "US$ 26 a criança de 3 a 12, a partir de 1º de outubro de 2026. Mas ele fica "
             "no sul do condado, longe da praia e da baía, e <b>não combina com mais nada "
             "no mesmo dia</b>. É um dia inteiro, e é de carro.",
             ["Vizcaya · fecha terça · 9h30 às 16h30",
              "Vizcaya · US$ 24 a US$ 39, sem tabela fixa",
              "Coconut Grove · o entorno, de graça",
              "Zoo Miami · US$ 30 · troca o dia inteiro"]),
        ],
        "fontes": ("Tarifas e horários consultados em 29 de setembro de 2026, os mesmos da "
                   "ficha dos 9 pontos. <b>O adicional de não-residente do Everglades é a "
                   "maior mudança do ano para quem viaja daqui</b>, e há divergência entre "
                   "duas páginas oficiais do NPS sobre qual passe o dispensa — o guia "
                   "registra as duas. A ordem dos dias é nossa, e o motivo está escrito em "
                   "cada um."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
