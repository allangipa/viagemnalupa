# -*- coding: utf-8 -*-
"""Ficha de custos de Madri.

Reusa o renderizador de novos/gera_custos.py, como os demais.

O QUE ESTA FICHA EXISTE PARA MOSTRAR
------------------------------------
Os seis pontos pagos somam 101 euros. Quatro deles tem janela gratuita, e
somam 59. Desmarcando os quatro, a conta cai para 42 - e 18 desses 59 sao
direito de quem tem passaporte latino-americano, nao promocao para todos.

    Prado           15    gratis 18h-20h de seg a sab
    Reina Sofia     12    gratis 19h-21h; 12h30-14h30 no domingo
    Thyssen         14    gratis segunda, 12h-16h
    Palacio Real    18    gratis seg a qui, para iberoamericano
    ------------------------------------------------------------
                    59    o que da para nao pagar

Sobram Bernabeu (35) e o museu da Almudena (7), que nao tem janela.

A ARMADILHA DO BERNABEU, QUE E UNICA NO SITE
--------------------------------------------
E a unica linha de todas as fichas em que o CANAL DE COMPRA muda o preco:
35 euros online contra 38 na bilheteria. A tabela usa 35, e a observacao
diz por que.

O QUE FICA FORA DO TOTAL
------------------------
Hospedagem e transporte, por falta de fonte oficial apurada. Catedral,
Plaza Mayor, Sol, Mercado de San Miguel, Retiro e Debod entram como zero
porque sao mesmo gratuitos.

Uso
---
    python _build/madri/gera_custos.py
    python _build/madri/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base  # noqa: E402

# A armadilha do Porto: o rodape imprime base.APURACAO, que no
# renderizador e a data do novos/dados.py.
_s = importlib.util.spec_from_file_location(
    "dados_madri_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "madri": {
        "nome": "Madri", "dias": 5, "moeda": "€", "dec": 2,
        "titulo": "Quanto custa 5 dias em Madri em 2026",
        "descricao": ("O custo de 5 dias em Madri, por pessoa, com as quatro janelas "
                      "gratuitas que derrubam a conta de € 101 para € 42 — e a do "
                      "Palácio Real, que é direito de quem tem passaporte brasileiro."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 29 de setembro de 2026. <b>Sem a hospedagem</b> — e a página "
                     "explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em euro. "
                  "Mude as datas e o número de pessoas, desmarque o que você não vai "
                  "fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Quatro das seis linhas pagas têm horário em "
            "que não custam nada.</b> Desmarque Prado, Reina Sofía, Thyssen e Palácio "
            "Real e você vê o total de quem se organiza pelas janelas gratuitas: "
            "<b>€ 42</b>, contra € 101. Sobram só o Bernabéu e o museu da Almudena, que "
            "não têm janela nenhuma. "
            "<b style=\"color:var(--gelo)\">E € 18 desse desconto é seu por "
            "nacionalidade</b>: a tarifa gratuita do Palácio Real vale para cidadão "
            "latino-americano com documento, e não só para europeu. "
            "<b>Esta ficha não tem hospedagem</b>, e isso é deliberado: não apuramos "
            "diária média publicada por órgão oficial para Madri nesta rodada. Linhas "
            "marcadas como não apuradas continuam fora do total."),
        "linhas": [
            ("ingresso", 35, "Estádio Santiago Bernabéu, tour", "€ 35",
             "<b>A partir de € 35 online e € 38 na bilheteria</b> — <b>é a única linha de "
             "todo o site em que o canal de compra muda o preço</b>, e são € 3 por "
             "comprar na hora. O valor é o piso da entrada Classic, de visita livre. "
             "Abre todos os dias menos 25/dez e 1º/jan, das 9h às 19h (domingo e feriado "
             "9h30 às 18h30). <b>Em dia de jogo o percurso encolhe</b> e o clube avisa só "
             "no site ou na porta. Fonte: Real Madrid C.F., 29/set/2026."),
            ("ingresso", 18, "Palacio Real de Madrid", "€ 18",
             "Inteira; reduzida € 7; menor de 5 anos não paga. <b>E é gratuito para "
             "cidadão latino-americano</b> — o texto oficial diz "
             "<i>“ciudadanos iberoamericanos”</i> com prova de nacionalidade — <b>de "
             "segunda a quinta, das 16h às 18h de outubro a março e das 17h às 19h de "
             "abril a setembro</b>. <b>Só visita livre, só na bilheteria física, e leve o "
             "passaporte.</b> Quase todo guia escreve “grátis para cidadãos da UE” e faz "
             "o brasileiro pagar à toa. Fonte: Patrimonio Nacional, 29/set/2026."),
            ("ingresso", 15, "Museo del Prado", "€ 15",
             "Inteira; reduzida € 7,50. <b>Gratuito nas duas horas antes de fechar, todos "
             "os dias</b>: 18h às 20h de segunda a sábado, 17h às 19h aos domingos e "
             "feriados. Abre 10h às 20h (domingo até 19h). "
             "<span class=\"flag\">Fonte oficial não aberta</span> a página do próprio "
             "museu está atrás de proteção anti-bot e não abriu; os valores vêm da "
             "indexação do domínio dele e da ficha do esMadrid, portal oficial de turismo "
             "de Madri, que coincidem."),
            ("ingresso", 14, "Museo Thyssen-Bornemisza", "€ 14",
             "Inteira; reduzida € 10. <b>Gratuito às segundas, das 12h às 16h</b>, por "
             "patrocínio — e a segunda é justamente o dia em que o museu <b>só</b> abre "
             "das 12h às 16h, então na segunda ele é de graça o tempo todo em que está "
             "aberto. <b>A gratuidade cobre a coleção permanente, não as temporárias.</b> "
             "Sábado abre até as 23h, a grade mais generosa do Paseo del Arte. Fonte: "
             "site oficial, 29/set/2026."),
            ("ingresso", 12, "Museo Reina Sofía", "€ 12",
             "<b>Gratuito das 19h às 21h</b> na segunda e de quarta a sábado, e <b>das "
             "12h30 às 14h30 no domingo</b>, que fecha mais cedo. <b>Fecha às "
             "terças-feiras</b> — e o Prado e o Thyssen não, o que faz da terça a "
             "armadilha de Madri. <b>Mesmo de graça é preciso reservar bilhete</b>: a "
             "página é literal sobre isso. A gratuidade do horário vale só para visitante "
             "individual. Fonte: site oficial, 29/set/2026."),
            ("ingresso", 7, "Catedral de la Almudena, museu e cúpula", "€ 7",
             "Inteira; reduzida € 5; estudante € 3. <b>A catedral em si é gratuita</b>, "
             "com donativo sugerido de € 1 — o que se paga é o museu com a subida à "
             "cúpula. <b>Museu e cúpula abrem só de segunda a sábado, das 10h às "
             "14h30</b>: quem combinar a catedral com a janela gratuita do Palácio Real, "
             "às 16h, já perdeu a cúpula naquele dia. "
             "<span class=\"flag\">Fonte não oficial</span> valores de fontes secundárias "
             "que coincidem; confirme na porta."),
            ("ingresso", 0, "Catedral de la Almudena, a nave", "Grátis",
             "Entrar na catedral não custa nada, com donativo voluntário sugerido de "
             "€ 1. Abre todos os dias, das 10h às 20h30 (julho e agosto até 21h). A "
             "cripta também é de donativo."),
            ("ingresso", 0, "Templo de Debod", "Grátis",
             "<b>Mas reserve antes.</b> A prefeitura é explícita: <b>“sin reserva no se "
             "garantiza el acceso”</b>, porque o aforo é limitado. A reserva é gratuita, "
             "em madrid.es/debodreservas. <b>Fecha todas as segundas</b>, inclusive "
             "feriados — justo o dia das janelas gratuitas do Thyssen e do Palácio Real. "
             "Terça a domingo 10h às 20h; no verão até 19h. Fonte: Ayuntamiento de "
             "Madrid, 29/set/2026."),
            ("ingresso", 0, "Parque del Retiro e Palacio de Cristal", "Grátis",
             "Parque público, e o Palacio de Cristal também é gratuito — funciona como "
             "sala de exposição do Reina Sofía. Patrimônio Mundial da UNESCO desde 2021. "
             "<span class=\"flag\">Horário não apurado</span> muda com a estação, e o "
             "parque <b>fecha em vento forte</b>, por risco de queda de árvore. Alugar "
             "barco no lago é pago e não apuramos."),
            ("ingresso", 0, "Plaza Mayor, Puerta del Sol e Mercado de San Miguel", "Grátis",
             "As duas praças são via pública, 24 horas. Entrar no mercado também não "
             "custa nada. <b>O que custa é sentar e consumir</b>, e nos três casos o "
             "preço é de zona turística — o mercado é caro para o padrão de Madri e "
             "funciona por porções pequenas, o que faz a conta subir sem parecer."),
            ("ingresso", 0, "Hospedagem",
             "<span class=\"flag\">Não apurada</span>",
             "<b>Não apuramos diária média publicada por órgão oficial para Madri</b> "
             "nesta rodada. Usar média de agregador seria furar a regra da casa na linha "
             "mais cara da viagem. Mesma lacuna declarada de Fortaleza, Bariloche, Punta "
             "Cana, Miami e Salvador."),
            ("ingresso", 0, "Transporte urbano",
             "<span class=\"flag\">Não apurado</span>",
             "Não apuramos tarifa de metrô, de ônibus nem do trem ao aeroporto. "
             "<b>Registre o que a geografia obriga:</b> o Paseo del Arte, o palácio e as "
             "praças se fazem a pé, um do outro — <b>mas o Bernabéu não</b>, e Debod "
             "também fica fora desse eixo."),
        ],
        "rodape_tabela": ("Valores em euro, por pessoa, apurados em 29 de setembro de 2026. "
                          "<b>Duas linhas estão fora do total</b>, hospedagem e transporte, "
                          "por falta de fonte oficial. <b>E o total de € 101 cai para "
                          "€ 42</b> para quem encaixa as quatro janelas gratuitas — o "
                          "roteiro mostra como três delas encadeiam numa segunda-feira."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": ("Cada linha traz a fonte e a data no próprio campo. <b>A tarifa gratuita "
                   "do Palácio Real para cidadão latino-americano está no texto da "
                   "Patrimonio Nacional</b>, e é o número mais útil desta página para quem "
                   "lê daqui. <b>A exceção de procedência é o Prado</b>: a página dele não "
                   "abriu, por proteção anti-bot, e o que publicamos vem da indexação do "
                   "próprio domínio somada à ficha do esMadrid, portal oficial de turismo "
                   "da cidade. Está dito na linha dele, e não contornamos a proteção."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"),
    ("miami", "Miami"), ("salvador", "Salvador"), ("madri", "Madri"),
]
_vistos, _limpo = set(), []
for _slug, _nome in base.CIDADES:
    if _slug not in _vistos:
        _vistos.add(_slug)
        _limpo.append((_slug, _nome))
base.CIDADES = _limpo

base.FICHAS = FICHAS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
