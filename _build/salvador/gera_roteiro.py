# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Salvador.

Reusa o renderizador de novos/gera_roteiro.py, como os demais.

O QUE ORGANIZA ESTE ROTEIRO
---------------------------
A quarta-feira. Sete equipamentos municipais nao cobram nada as
quartas, e tres deles estao nesta ficha - Casa do Carnaval, Espacos do
Forte e Casa do Rio Vermelho, R$ 20 cada.

E A ESCOLHA QUE A QUARTA IMPOE, QUE E O ACHADO DO ROTEIRO
----------------------------------------------------------
Os tres nao ficam juntos. Casa do Carnaval e os Espacos do Forte estao
no Centro Historico, a pe um do outro. A Casa do Rio Vermelho esta em
outro bairro.

    So os dois do centro, na quarta     economiza R$ 40, tudo a pe
    Os tres na quarta                   economiza R$ 60, mas o dia
                                        atravessa a cidade

Nao existe resposta certa, e o roteiro diz isso em vez de fingir que os
tres cabem confortavelmente. O dia 2 faz os dois do centro; o dia 5 fica
com o Rio Vermelho, e quem quiser os R$ 60 troca a ordem.

A SEGUNDA-FEIRA E O OPOSTO
--------------------------
Os museus municipais fecham segunda. O Farol da Barra nao e da
prefeitura, abre os sete dias, e por isso e o unico ponto pago que salva
uma segunda.

Uso
---
    python _build/salvador/gera_roteiro.py
    python _build/salvador/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_roteiro as base  # noqa: E402

# Carregado por caminho, e com a troca de APURACAO junto: o rodape
# imprime essa data, e sem a troca sairia a do novos/dados.py.
_s = importlib.util.spec_from_file_location(
    "dados_salvador", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "salvador": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Salvador",
        "descricao": ("Cinco dias em Salvador montados em cima da quarta-feira, quando "
                      "sete museus municipais não cobram nada — e desviando da segunda, "
                      "quando quase todos fecham."),
        "abertura": ("Cinco dias organizados por uma regra que a prefeitura publica e "
                     "quase nenhum guia usa: <b>às quartas-feiras, sete museus "
                     "municipais não cobram entrada</b> — de morador e de turista."),
        "avisos": [
            ("a", "A quarta-feira vale R$ 40 a R$ 60 por pessoa",
             "<p>A Prefeitura de Salvador mantém <b>entrada gratuita às quartas-feiras</b> "
             "em sete equipamentos culturais, e é <b>regra permanente, não promoção</b>. "
             "Três deles estão neste roteiro: <b>Casa do Carnaval</b>, os <b>Espaços "
             "Pierre Verger e Carybé</b> e a <b>Casa do Rio Vermelho</b>, a R$ 20 cada.</p>"
             "<p><b>Mas eles não ficam juntos, e aí está a escolha.</b> Os dois primeiros "
             "são no Centro Histórico, a pé um do outro. A Casa do Rio Vermelho é em "
             "outro bairro. Fazer os dois do centro na quarta economiza <b>R$ 40</b> sem "
             "esforço; incluir o terceiro economiza <b>R$ 60</b>, mas transforma o dia "
             "numa travessia da cidade.</p>"
             "<p>O roteiro abaixo faz os dois do centro no dia 2. Se você quiser os "
             "R$ 60, troque o dia 5 de lugar e feche a quarta no Rio Vermelho.</p>"),
            ("b", "A segunda-feira fecha quase tudo",
             "<p><b>Os museus municipais fecham às segundas.</b> Casa do Carnaval, Casa "
             "do Rio Vermelho e, muito provavelmente, os Espaços do Forte — "
             "<span class=\"flag\">a prefeitura não publica a grade individual deles</span>, "
             "e por isso não afirmamos.</p>"
             "<p><b>O que salva a segunda é o Farol da Barra.</b> Ele é do Museu Náutico, "
             "não da prefeitura: <b>abre os sete dias, das 9h às 18h</b> — e, pelo mesmo "
             "motivo, <b>é o único que continua cobrando R$ 20 na quarta</b>. As duas "
             "coisas são a mesma coisa vista de dois lados.</p>"),
            ("c", "A Igreja de São Francisco está fechada, e o seu guia não sabe",
             "<p>A página oficial da prefeitura carimba <b>“FECHADA PARA RESTAURO”</b> no "
             "próprio título do verbete, <b>sem data de reabertura</b>. É o ponto mais "
             "vendido do Pelourinho — o da talha dourada — e <b>segue listado como aberto "
             "em quase todo guia e em plataformas de passeio</b>.</p>"
             "<p><b>Cuidado com a confusão de nomes:</b> a <b>Igreja da Ordem Terceira de "
             "São Francisco</b>, de fachada em pedra lavrada, é outro prédio, ao lado. "
             "Não é a que você viu na foto, e não está fechada.</p>"),
            ("b", "O Elevador Lacerda: três tarifas, e as oficiais são as erradas",
             "<p>O portal de turismo da prefeitura e a secretaria de Mobilidade publicam "
             "<b>R$ 0,15</b>. A imprensa apurou que o elevador reabriu depois de cerca de "
             "dez meses fechado, com obra de mais de <b>R$ 14 milhões</b>, e que "
             "<b>segue gratuito por tempo limitado</b>. A tarifa anunciada para o fim da "
             "gratuidade é <b>R$ 1,00</b>.</p>"
             "<p><b>São duas páginas oficiais da mesma prefeitura contra o que a própria "
             "prefeitura entregou.</b> Leve moeda: se a gratuidade tiver acabado, R$ 1,00 "
             "resolve. E é transporte público de verdade — cerca de 6 mil pessoas por "
             "dia —, então a fila do fim da tarde é de gente voltando do trabalho.</p>"),
        ],
        "dias_lista": [
            ("Pelourinho, o Elevador e a Cidade Baixa",
             "Dia de chegada e dia sem bilheteria. O <b>Pelourinho</b> é rua pública, "
             "Patrimônio Mundial da UNESCO desde 1985 e o maior conjunto de arquitetura "
             "colonial portuguesa das Américas — ver o conjunto não custa nada. Comece "
             "pelo <b>Terreiro de Jesus</b> e pelo <b>Largo do Pelourinho</b>. "
             "<b>Passe na frente da Igreja de São Francisco sabendo que ela está "
             "fechada</b>, para não perder a manhã tentando entrar. Depois desça pelo "
             "<b>Elevador Lacerda</b>, que hoje é gratuito, leva 22 segundos e vence 72 "
             "metros — e desemboca no <b>Mercado Modelo</b>, onde entrar também não "
             "custa nada e a negociação de preço é esperada. Da varanda do mercado "
             "você vê o <b>Forte de São Marcelo</b>, no meio da água.",
             ["Pelourinho · grátis, rua pública",
              "Igreja de São Francisco · FECHADA para restauro",
              "Elevador Lacerda · grátis hoje, R$ 1,00 anunciado",
              "Mercado Modelo · entrar é grátis"]),

            ("A quarta-feira de graça — dois museus, nenhum bilhete",
             "<b>Ponha este dia numa quarta, se puder.</b> A <b>Casa do Carnaval da "
             "Bahia</b>, na Praça Ramos de Queirós, custa R$ 20 em dia normal e "
             "<b>nada na quarta</b> — e o terraço com vista para a Baía de Todos os "
             "Santos já vem no bilhete. Abre das 9h às 17h, com <b>última entrada às "
             "16h</b>, uma hora antes de fechar. Depois suba a pé até o <b>Forte de "
             "Santo Antônio Além do Carmo</b>, onde ficam o <b>Espaço Pierre Verger da "
             "Fotografia Baiana</b> e o <b>Espaço Carybé de Artes</b>: <b>um bilhete só "
             "dá acesso aos dois</b>, também R$ 20, também grátis na quarta. Verger "
             "fotografou o candomblé e a ligação entre a Bahia e a África; Carybé "
             "ilustrou Jorge Amado. <b>São R$ 40 economizados sem sair do Centro "
             "Histórico.</b> Se a sua viagem não tiver quarta, o dia funciona igual — "
             "só não o faça numa <b>segunda</b>.",
             ["Casa do Carnaval · R$ 20 · grátis quarta",
              "Casa do Carnaval · última entrada 16h",
              "Pierre Verger + Carybé · um bilhete para os dois",
              "Os dois espaços · R$ 20 · grátis quarta",
              "Todos fecham segunda"]),

            ("A Barra: o farol, o museu e a praia da baía",
             "Dia de orla, e o único ponto pago que <b>não</b> tem quarta gratuita. O "
             "<b>Farol da Barra</b> abriga o <b>Museu Náutico da Bahia</b>, dentro do "
             "Forte de Santo Antônio da Barra: <b>R$ 20 a inteira</b>, R$ 10 a meia para "
             "estudante, professor e maior de 60. Não pagam menores de 7 anos, "
             "museólogos, arqueólogos, aluno de escola pública, militares, policiais e "
             "pessoa com deficiência com acompanhante. <b>Abre todos os dias, das 9h às "
             "18h</b> — é o que salva uma segunda-feira. A poucos minutos a pé fica a "
             "<b>Praia do Porto da Barra</b>, de acesso livre: ela está <b>dentro da "
             "Baía de Todos os Santos</b>, não no mar aberto, e por isso tem água calma "
             "e rasa. É a praia urbana mais protegida da cidade, e a mais cheia no fim "
             "de semana. Cadeira e guarda-sol são das barracas, e custam.",
             ["Farol da Barra · R$ 20 · abre todo dia 9h às 18h",
              "Farol · NÃO tem quarta gratuita",
              "Porto da Barra · grátis, 24 horas",
              "Água calma · fica dentro da baía"]),

            ("Bonfim e a Península Itapagipana",
             "Dia fora do centro, e o mais devocional do roteiro. A <b>Basílica do "
             "Senhor do Bonfim</b> é <b>gratuita</b> e abre todos os dias — <b>mas o "
             "horário muda</b>: de segunda a quinta e no sábado, das 6h30 às 18h; "
             "<b>na sexta e no domingo abre às 5h30</b>, uma hora mais cedo, porque "
             "<b>sexta é o dia do Senhor do Bonfim</b> e o movimento de fiéis é muito "
             "maior. <b>Escolha conforme o que você quer ver:</b> a igreja com calma, "
             "evite a sexta; a devoção acontecendo, é exatamente o dia. Reserve tempo "
             "para a <b>Sala dos Milagres</b>, com os ex-votos, e para o <b>mirante dos "
             "fundos</b>, com vista para a baía, que quase ninguém inclui. As fitinhas "
             "são vendidas por ambulantes no largo, a preço de rua — <b>não há tabela "
             "oficial</b>. E lembre que é santuário em uso: entre em silêncio.",
             ["Basílica do Senhor do Bonfim · grátis",
              "Seg a qui e sáb · 6h30 às 18h",
              "Sexta e domingo · abre 5h30",
              "Sexta · dia do Bonfim, muito mais cheio",
              "Fitinhas · preço de ambulante, sem tabela"]),

            ("Rio Vermelho: a casa de Jorge Amado e a noite",
             "Último dia, e o de melhor encaixe entre tarde e noite. A <b>Casa do Rio "
             "Vermelho</b> é onde <b>Jorge Amado e Zélia Gattai viveram mais de "
             "cinquenta anos</b>, e onde os dois estão enterrados, sob a mangueira do "
             "jardim. R$ 20 a inteira, R$ 10 a meia, <b>gratuita às quartas</b>, e o "
             "acervo tem mais de 30 horas de vídeo e projeções. Abre de <b>terça a "
             "domingo, das 9h às 17h, com última entrada às 16h</b>, e <b>fecha "
             "segunda</b> — mesma grade da Casa do Carnaval. <b>O encaixe:</b> ela fecha "
             "às 17h e o Rio Vermelho começa logo depois — é o bairro dos bares e da "
             "vida noturna de Salvador, e você já está nele. <b>Se quiser economizar os "
             "R$ 60 inteiros da quarta</b>, é este o dia que troca de lugar: faça a Casa "
             "do Rio Vermelho na quarta também, aceitando atravessar a cidade.",
             ["Casa do Rio Vermelho · R$ 20 · grátis quarta",
              "Ter a dom · 9h às 17h · última entrada 16h",
              "Fecha segunda",
              "Fecha 17h · o bairro começa depois"]),
        ],
        "fontes": ("Tarifas e horários consultados em 29 de setembro de 2026, os mesmos da "
                   "ficha dos 10 pontos. <b>A quarta-feira gratuita é regra permanente "
                   "publicada pela Prefeitura de Salvador</b>, e vale para sete "
                   "equipamentos municipais. O Elevador Lacerda é o caso oposto: duas "
                   "páginas oficiais da mesma prefeitura publicam uma tarifa que não é "
                   "mais a praticada, e o guia registra as três versões. A ordem dos dias "
                   "é nossa, e o motivo está escrito em cada um."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
