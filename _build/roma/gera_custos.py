# -*- coding: utf-8 -*-
"""Ficha de custos de Roma.

Reusa o renderizador de novos/gera_custos.py, como os demais.

OS CINCO PAGOS SOMAM 78 EUROS, E OS DOIS DOMINGOS CORTAM DIFERENTE
------------------------------------------------------------------
    Museus Vaticanos      25    gratis no ULTIMO domingo
    Coliseu/Foro/Palatino 18    gratis no PRIMEIRO domingo
    Galleria Borghese     18    gratis no PRIMEIRO - menos 2 de reserva
    Cupola de Sao Pedro   10    sem gratuidade
    Panteao                7    gratis no PRIMEIRO domingo
    ------------------------------------------------------------
                          78

    Primeiro domingo   corta 41 (18 + 7 + 16)   sobra 37
    Ultimo domingo     corta 25                 sobra 53

Os dois nao se somam: sao domingos diferentes do mesmo mes, e uma viagem
de cinco dias pega no maximo um. Qual domingo cai na viagem vale 16 euros
de diferenca - e essa e a pergunta que a ficha existe para fazer.

A ARMADILHA DO BORGHESE
-----------------------
No primeiro domingo ele e "gratuito", mas a reserva e obrigatoria para
todas as categorias e custa 2 euros. Entao o domingo de graca corta 16,
nao 18. O valor da linha considera isso.

O VATICANO ENTRA COM 25, NAO COM 20
-----------------------------------
20 e a tarifa de bilheteria, sem reserva. 25 e com o Salta la fila
online. Quem planeja do Brasil nao aposta na fila da porta - mesma
logica do Bernabeu em Madri, que entrou com o preco online.

O QUE FICA FORA DO TOTAL
------------------------
Hospedagem e transporte, por falta de fonte oficial apurada. O
contributo di soggiorno tem linha propria, com valor, mas fica FORA do
total: e por pessoa por noite e depende da classificacao do hotel, que a
calculadora nao modela.

Uso
---
    python _build/roma/gera_custos.py
    python _build/roma/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_roma_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "roma": {
        "nome": "Roma", "dias": 5, "moeda": "€", "dec": 2,
        "titulo": "Quanto custa 5 dias em Roma em 2026",
        "descricao": ("O custo de 5 dias em Roma, por pessoa, com os dois domingos "
                      "gratuitos que cortam a conta de formas diferentes."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 29 de setembro de 2026. <b>Sem a hospedagem</b> — e a página "
                     "explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em euro. "
                  "Mude as datas e o número de pessoas, desmarque o que você não vai "
                  "fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Roma tem dois domingos gratuitos por mês, e "
            "eles cortam coisas diferentes.</b> Desmarque Coliseu, Panteão e Galleria "
            "Borghese e você vê o <b>primeiro domingo</b>. <b>A calculadora vai mostrar "
            "€ 35, e o valor real é € 37</b> — ela desliga a linha inteira do Borghese, "
            "mas <b>os € 2 de reserva continuam devidos mesmo quando a entrada é "
            "grátis</b>, e a calculadora não sabe separar a reserva do ingresso. "
            "Desmarque só os Museus Vaticanos e você vê o <b>último domingo</b>: corta "
            "€ 25 e sobra € 53, esse sem ressalva. "
            "<b style=\"color:var(--gelo)\">Os dois não se somam</b> — são domingos "
            "diferentes, e uma viagem de cinco dias pega no máximo um. "
            "<b>O contributo di soggiorno tem linha própria e fica fora do total</b>: é "
            "por pessoa por noite, varia de € 3 a € 10 conforme a estrutura, e esta "
            "calculadora não modela isso. <b>Esta ficha também não tem hospedagem</b>, "
            "por falta de diária média oficial apurada."),
        "linhas": [
            ("ingresso", 25, "Museus Vaticanos e Capela Sistina", "€ 25",
             "<b>€ 20 na bilheteria, sem reserva, ou € 20 + € 5 de taxa = € 25 online</b> "
             "com o <i>Salta la fila</i>. A ficha usa € 25 porque a fila do Vaticano é uma "
             "das maiores da Europa e quem planeja de longe não aposta nela. <b>O bilhete "
             "vale só no dia da emissão e não é reembolsável.</b> <b>Fecha aos domingos, "
             "exceto o último do mês</b>, quando é gratuito das 9h às 14h, com última "
             "admissão às 12h30. <b>O museu avisa que há sites com domínio parecido "
             "cobrando bem mais</b> — o oficial é tickets.museivaticani.va."),
            ("ingresso", 18, "Coliseu, Fórum Romano e Palatino", "€ 18",
             "<b>Um bilhete cobre os três e vale 24 horas</b> a partir da primeira "
             "picotada — dá para ver o Coliseu à tarde e o Fórum na manhã seguinte. "
             "<b>Reserva de horário obrigatória para o Coliseu</b>, com vendas abrindo 30 "
             "dias antes, e <b>permanência limitada a 75 minutos</b> lá dentro. "
             "<b>Atenção: a meia de € 2 é só para cidadão da UE de 18 a 24 anos</b> — "
             "brasileiro de vinte anos paga os € 18 cheios. <b>Gratuito no primeiro "
             "domingo do mês</b>, pela Domenica al Museo, mas ainda com reserva."),
            ("ingresso", 18, "Galleria Borghese", "€ 18",
             "<b>€ 16 de ingresso + € 2 de reserva obrigatória.</b> Há turno noturno às "
             "18h45 por € 13. <b>E o primeiro domingo do mês não é totalmente grátis "
             "aqui:</b> a entrada é gratuita, mas <b>os € 2 de reserva continuam "
             "devidos</b>, porque ela é obrigatória para todas as categorias. <b>Visita "
             "em turno fixo de duas horas</b> (9h, 11h, 13h, 15h e 17h), sem entrada fora "
             "do turno. <b>Fecha segunda.</b> É o ponto menos improvisável de Roma."),
            ("ingresso", 10, "Cúpula da Basílica de São Pedro", "€ 10",
             "<b>€ 10 pela escada, € 15 com elevador</b>, na bilheteria no dia. <b>E o "
             "elevador não resolve o que parece:</b> são 551 degraus, ele poupa os 231 "
             "primeiros e <b>deixa 320 a pé</b>, numa escada em caracol que aperta. A "
             "ficha usa € 10. <b>A basílica em si é gratuita</b> e tem linha própria "
             "abaixo. Cúpula aberta das 7h30 às 18h no verão, às 17h no inverno."),
            ("ingresso", 7, "Panteão", "€ 7",
             "<b>Era gratuito havia séculos.</b> Passou a cobrar € 5 em 2023 e <b>subiu "
             "para € 7 em 1º de julho de 2026</b> — muito guia ainda escreve “entrada "
             "franca”. Jovem de 18 a 25 paga € 2, menor de 18 não paga, morador de Roma "
             "não paga. <b>Gratuito no primeiro domingo do mês.</b> E como é também uma "
             "basílica em funcionamento, <b>o acesso durante as celebrações é livre, para "
             "culto</b>. Abre 9h às 19h, última entrada 18h30, <b>bilheteria fecha às "
             "18h</b>."),
            ("ingresso", 0, "Basílica de São Pedro", "Grátis",
             "Entrar não custa nada e não precisa de bilhete — o que há é fila de "
             "segurança, que pode ser longa. <b>A entrada da basílica não é a mesma dos "
             "Museus Vaticanos</b>: são portões diferentes, a uns quinze minutos de "
             "caminhada um do outro. Quem vai para a fila errada perde a hora marcada."),
            ("ingresso", 0, "Fontana di Trevi e Piazza Navona", "Grátis",
             "As duas são via pública, sem bilheteria. Entrar na água da Trevi é proibido "
             "e multado. <span class=\"flag\">Regras de fluxo não apuradas</span> houve "
             "nos últimos anos restrições e propostas de acesso controlado na Trevi, e "
             "<b>não confirmamos qual regime vigora hoje</b> — o site do Comune di Roma "
             "recusou conexão. Nos cafés da Navona, o preço no balcão costuma ser menor "
             "que na mesa, e a diferença deve estar afixada."),
            ("ingresso", 0, "Piazza di Spagna", "Grátis",
             "<b>Estar ali não custa nada — sentar na escadaria custa € 250.</b> O "
             "regulamento de polícia urbana trata a escadaria de Trinità dei Monti como "
             "monumento e proíbe sentar e deitar; a multa chega a <b>€ 400</b> por sujar "
             "ou danificar. A polícia municipal aborda quem senta. <b>É exatamente o que "
             "todo turista faz na foto que todo mundo tira.</b>"),
            ("ingresso", None, "Contributo di soggiorno", "€ 3 a € 10 por noite",
             "<span class=\"flag\">Fora do total</span> <b>é por pessoa por noite e varia "
             "com a classificação da estrutura</b>, e esta calculadora não modela isso. "
             "<b>Hotel chega a € 10; B&B e aluguel de curta duração, € 6.</b> Cobra-se no "
             "máximo <b>10 noites consecutivas</b> na mesma estrutura. <b>Um casal, cinco "
             "noites em hotel: € 100 fora do preço da reserva</b> — duas vezes e meia a "
             "taxa de Lisboa. <span class=\"flag\">Só fontes secundárias</span> o site do "
             "Comune di Roma recusou conexão; as fontes consultadas convergem, mas "
             "confirme no ato da reserva."),
            ("ingresso", 0, "Hospedagem",
             "<span class=\"flag\">Não apurada</span>",
             "<b>Não apuramos diária média publicada por órgão oficial para Roma</b> nesta "
             "rodada. Usar média de agregador seria furar a regra da casa na linha mais "
             "cara da viagem — e aqui seria pior, porque a diária anunciada ainda não "
             "inclui o contributo da linha acima."),
            ("ingresso", 0, "Transporte urbano",
             "<span class=\"flag\">Não apurado</span>",
             "Não apuramos tarifa de metrô, ônibus nem do trem ao aeroporto. <b>Registre o "
             "que a geografia dá de presente:</b> Panteão, Trevi, Navona e Piazza di "
             "Spagna formam um circuito a pé no centro, e só o Panteão cobra. O Vaticano e "
             "o Coliseu ficam em pontas opostas desse circuito."),
        ],
        "rodape_tabela": ("Valores em euro, por pessoa, apurados em 29 de setembro de 2026. "
                          "<b>Três linhas estão fora do total</b>: o contributo di "
                          "soggiorno, a hospedagem e o transporte. <b>E o total de € 78 "
                          "cai para € 37 num primeiro domingo ou para € 53 num último</b> "
                          "— nunca para os dois, porque são domingos diferentes."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": ("Cada linha traz a fonte e a data no próprio campo. <b>Vários sites "
                   "oficiais italianos recusaram conexão direta</b> nesta apuração — "
                   "colosseo.it, o ticketing do Coliseu, museivaticani.va e comune.roma.it "
                   "—, e o navegador também foi negado no ticketing. Não contornamos "
                   "bloqueio. O que publicamos vem da indexação dos próprios domínios "
                   "oficiais, e está dito ponto a ponto. <b>O contributo di soggiorno é o "
                   "único número que veio só de fontes secundárias convergentes</b>, e a "
                   "linha dele diz isso."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
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
