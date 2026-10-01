# -*- coding: utf-8 -*-
"""Ficha de custos de Paris.

Reusa o renderizador de novos/gera_custos.py, como os demais.

OS SEIS PAGOS SOMAM 159,50 EUROS - E 13 DELES SAO O SEU PASSAPORTE
-------------------------------------------------------------------
    Versalhes, Passaporte alta   35,00   europeu paga 32,00
    Louvre                       32,00   europeu paga 22,00
    Catacumbas                   31,00   igual para todos
    Torre Eiffel, 2o andar       23,50   igual para todos
    Sainte-Chapelle              22,00   igual para todos
    Arco do Triunfo              16,00   igual para todos
    --------------------------------------------------------
                                159,50   europeu: 146,50

A diferenca de 13 euros nao e enorme. O que esta ficha existe para
mostrar e que ELA EXISTE, e que a REGRA MUDA DE LUGAR PARA LUGAR -
porque nenhum guia separa isso.

O ORSAY NAO TEM LINHA DE VALOR, E ISSO E DE PROPOSITO
-----------------------------------------------------
A pagina de tarifas do musee-orsay.fr responde "Acces refuse", por URL
direta e clicando o link a partir da home. A bilheteria oficial so
revela preco depois de escolher data. Nao contornamos bloqueio e nao
copiamos numero de terceiro: a linha entra com a lacuna escrita e FICA
FORA DO TOTAL.

Entao o total de 159,50 e o de SEIS pontos pagos, nao de sete. Quem
visitar o Orsay vai gastar mais do que esta ficha soma, e a ficha diz.

AS DUAS JANELAS DE GRACA NAO CAEM NO MESMO DIA
----------------------------------------------
    Louvre   PRIMEIRA SEXTA do mes, depois das 18h - nao vale em
             julho nem agosto. Corta 32.
    Orsay    PRIMEIRO DOMINGO do mes, com reserva obrigatoria.
             Corta um valor que nao sabemos.

Os dois museus ficam a dez minutos um do outro, a pe pela ponte, e tem
dias diferentes. Por anos o Louvre foi o do primeiro domingo; mudou, e
muito roteiro antigo manda a pessoa no dia errado.

O JARDIM DE VERSALHES INVERTE A LOGICA
--------------------------------------
Pago de 1 de abril a 31 de outubro; gratuito de 1 de novembro a 31 de
marco. Custa justamente quando esta bonito. O Passaporte ja inclui, mas
quem compra so o bilhete do castelo paga o jardim a parte na alta.

O QUE FICA FORA DO TOTAL: a taxe de sejour, a hospedagem e o
transporte. A taxa e por pessoa e por noite e nao vem no preco da
reserva.
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_custos as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_paris_custos", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.APURACAO = _d.APURACAO

FICHAS = {
    "paris": {
        "nome": "Paris", "dias": 5, "moeda": "€", "dec": 2,
        "titulo": "Quanto custa 5 dias em Paris em 2026",
        "descricao": ("O custo de 5 dias em Paris, por pessoa, com o Louvre que cobra "
                      "€ 32 de quem não é europeu desde janeiro de 2026."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 30 de setembro de 2026. <b>Sem a hospedagem</b> — e a página "
                     "explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em euro. "
                  "Mude as datas e o número de pessoas, desmarque o que você não vai "
                  "fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Os € 159,50 são o que um brasileiro paga. "
            "Um europeu paga € 146,50 pelos mesmos seis pontos.</b> A diferença são "
            "€ 10 no Louvre e € 3 em Versalhes — e a regra muda de lugar para lugar: "
            "a Torre Eiffel não separa por nacionalidade nenhuma, e a gratuidade de 18 "
            "a 25 anos dos monumentos nacionais vale só para quem mora na União "
            "Europeia. "
            "<b style=\"color:var(--gelo)\">O Musée d’Orsay está na tabela sem valor e "
            "fora do total</b>: a página de tarifas dele recusa acesso e a bilheteria só "
            "mostra preço depois de escolher data. Quem for ao Orsay vai gastar mais do "
            "que esta conta soma. "
            "<b>Desmarque o Louvre</b> e você vê a <b>primeira sexta do mês depois das "
            "18h</b>, que corta € 32 — mas não vale em julho nem agosto. <b>O primeiro "
            "domingo é do Orsay</b>, não do Louvre, e os dois nunca caem no mesmo dia. "
            "<b>A taxe de séjour tem linha própria e fica fora do total</b>: é por "
            "pessoa por noite, varia com a categoria do hotel, e esta calculadora não "
            "modela isso. <b>Esta ficha também não tem hospedagem</b>, por falta de "
            "diária média oficial apurada."),
        "linhas": [
            ("ingresso", 35, "Palácio de Versalhes — Passaporte", "€ 35",
             "<b>Alta temporada, de 1º de abril a 31 de outubro: € 35.</b> Na baixa, de "
             "1º de novembro a 31 de março, <b>€ 25</b>. <b>O europeu paga € 3 a menos</b> "
             "— € 32 e € 22 —, e a redução vale tanto para cidadão do EEE, qualquer que "
             "seja a residência, quanto para residente, qualquer que seja a "
             "nacionalidade. <b>O Passaporte é o único bilhete que entra no castelo</b>, "
             "com horário marcado, e cobre o domínio inteiro. <b>Há um Passaporte de fim "
             "de dia</b>, com entrada a partir das 16h na alta: <b>€ 28</b>. "
             "<b>Fecha às segundas</b>, mais 25/dez, 1º/jan e 1º/mai. O castelo abre às "
             "9h; <b>o domínio de Trianon só às 12h</b>. Fonte: página “Tarification "
             "2026” e informações práticas do site oficial, 30/set/2026."),
            ("ingresso", 32, "Museu do Louvre", "€ 32",
             "<b>€ 32 para quem não é cidadão nem residente do Espaço Econômico "
             "Europeu</b>; <b>€ 22 para quem é</b>. A cobrança separada começou em "
             "<b>14 de janeiro de 2026</b> e representa <b>45% a mais</b>. <b>Grupo "
             "guiado de fora do EEE paga € 28</b>, em grupos de até 20. <b>Não paga: "
             "menor de 18 anos de qualquer nacionalidade</b>, e menor de 26 que seja "
             "cidadão ou residente do EEE. <b>Gratuito para todos na primeira sexta do "
             "mês, depois das 18h — exceto em julho e agosto.</b> <b>Fecha às terças.</b> "
             "Segunda, quinta, sábado e domingo das 9h às 18h; quarta e sexta até as 21h; "
             "<b>última entrada uma hora antes</b>. Fonte: louvre.fr, 30/set/2026."),
            ("ingresso", 31, "Catacumbas de Paris", "€ 31",
             "<b>€ 31 com audioguia incluído.</b> <b>Reduzida € 25</b> para jovens de 18 "
             "a 26 anos, estudantes e professores — <b>aqui a redução é por idade</b>, "
             "como na Torre Eiffel e ao contrário dos monumentos nacionais, porque as "
             "Catacumbas são da cidade de Paris e não do Estado francês. <b>€ 15 de 8 a "
             "17 anos; até 7 não paga.</b> <b>De terça a domingo, das 9h45 às 20h30, "
             "última entrada às 19h30. Fecha às segundas</b>, mais 1º/jan, 1º/mai e "
             "25/dez. <b>A reserva on-line abre sete dias antes</b>, e <b>bilhete "
             "gratuito não pode ser reservado</b>: só no local, no dia. Fonte: "
             "catacombes.paris.fr, 30/set/2026."),
            ("ingresso", 23.5, "Torre Eiffel — 2º andar, elevador", "€ 23,50",
             "<b>O 2º andar de elevador custa € 23,50; o topo, € 36,70.</b> <b>Pela "
             "escada o 2º andar sai por € 14,80</b> — economiza € 8,70 e pula a fila do "
             "elevador, em troca de 674 degraus. <b>Aqui o passaporte não muda nada</b>: "
             "a <b>tarifa jovem é de 12 a 24 anos, por idade</b>, sem condição de "
             "nacionalidade nem de residência, e sai por <b>€ 11,80</b>. <b>Criança de 4 "
             "a 11 paga € 6; menor de 4 não paga</b>, mas precisa de bilhete emitido. "
             "<b>Abre todos os dias das 9h30 às 23h, últimas subidas às 22h45.</b> O topo "
             "e a escada não são acessíveis a quem tem mobilidade reduzida. Fonte: "
             "toureiffel.paris, 30/set/2026."),
            ("ingresso", 22, "Sainte-Chapelle", "€ 22",
             "<b>€ 22.</b> O site diz “gratuito para menores de 26 anos”, e <b>isso "
             "engana</b>: pelo Ministério da Cultura francês, <b>menor de 18 não paga, de "
             "qualquer nacionalidade</b>, mas a faixa de <b>18 a 25 anos só é gratuita "
             "para quem reside regularmente no Espaço Econômico Europeu</b>. O documento "
             "aceito é identidade, passaporte ou título de residência com foto — e, para "
             "o não europeu, residência de <b>mais de três meses</b> na França. Fonte: "
             "sainte-chapelle.fr e culture.gouv.fr, 30/set/2026."),
            ("ingresso", 16, "Arco do Triunfo", "€ 16",
             "<b>€ 16 para subir ao terraço</b>, com a mesma regra de gratuidade da "
             "Sainte-Chapelle. <b>O elevador está em manutenção, até segunda ordem</b>, e "
             "<b>o acesso se faz unicamente pelas escadas</b> — quem tem mobilidade "
             "reduzida não consegue subir enquanto isso durar, e a página não diz quando "
             "volta. <b>É aqui que o contraste aparece inteiro</b>: um brasileiro de 20 "
             "anos paga os € 16 cheios aqui e <b>€ 11,80</b> na Torre Eiffel, a três "
             "quilômetros. Fonte: paris-arc-de-triomphe.fr, 30/set/2026."),
            ("ingresso", None, "Musée d’Orsay", "Não encontrado",
             "<b>Esta linha não tem valor, e fica fora do total.</b> A página de tarifas "
             "do musee-orsay.fr responde <b>“Accès refusé”</b> — por endereço direto e "
             "clicando o link a partir da home —, e a bilheteria oficial <b>só mostra "
             "preço depois de escolher data</b>. <b>Não contornamos bloqueio e não "
             "copiamos número de terceiro.</b> <b>Quem for ao Orsay vai gastar mais do "
             "que esta ficha soma.</b> O que o próprio site publica e está conferido: "
             "<b>entrada gratuita para todos no primeiro domingo do mês, com reserva "
             "obrigatória</b>, e <b>reforma das áreas de recepção de 10 de março de 2026 "
             "até o verão europeu de 2028</b>. Fonte: faixa de aviso do site oficial, "
             "30/set/2026."),
            ("ingresso", 0, "Catedral de Notre-Dame", "Grátis",
             "<b>Entrar não se paga, para ninguém.</b> Houve proposta de cobrar de "
             "estrangeiros e ela foi <b>descartada</b>. <b>A reserva é gratuita e "
             "facultativa</b>; sem ela a espera chega a <b>duas ou três horas</b> na alta "
             "temporada. <b>Nenhum terceiro está autorizado a vender ingresso de "
             "entrada</b> — quem cobra por isso está vendendo o que é de graça. "
             "<b>As torres são outra coisa e custam € 16</b>, por outro órgão, com a "
             "regra de gratuidade dos monumentos nacionais."),
            ("ingresso", 0, "Sacré-Cœur e Montmartre", "Grátis",
             "<b>A basílica é gratuita e abre todos os dias do ano, sem exceção, das "
             "6h30 às 22h30</b> — é o horário mais largo desta ficha e o único ponto que "
             "não fecha em feriado nenhum. <b>A subida ao domo é paga, e o valor não "
             "aparece</b> nas páginas de informações práticas nem de horários do site "
             "oficial; não pusemos número de terceiro no lugar."),
            ("ingresso", 0, "Centre Pompidou", "Fechado",
             "<b>Não custa nada porque não abre.</b> O prédio <b>fechou em 22 de setembro "
             "de 2025</b> e a <b>reabertura está prevista para 2030</b> — cinco anos de "
             "obra, com retirada de amianto das fachadas. <b>Está nesta ficha porque "
             "continua em praticamente todo guia de Paris</b>, e para você não montar um "
             "dia em volta dele. A programação está espalhada em outros museus, pelo "
             "programa Constellation. Fonte: centrepompidou.fr, 30/set/2026."),
            ("ingresso", None, "Taxe de séjour", "€ 3,25 a € 15,93 por noite",
             "<b>Cobrada por pessoa e por noite, e não vem no preço da reserva</b> — "
             "aparece no check-in ou no check-out. <b>Este é o único número desta ficha "
             "que não conseguimos em fonte oficial aberta</b>: a página da prefeitura "
             "respondeu 404 e a tabela da administração fiscal é um arquivo de dados para "
             "download, não uma página citável. De <b>fontes secundárias convergentes</b>, "
             "para vigência a partir de 1º de janeiro de 2026, por pessoa e por noite, "
             "com adicionais incluídos: <b>Palace € 15,93 · 5 estrelas € 11,70 · 4 "
             "estrelas € 8,45 · 3 estrelas € 5,53 · 2 estrelas € 3,25</b>. Aluguel de "
             "temporada não classificado tem <b>teto de € 15,93</b>. <b>Trate como ordem "
             "de grandeza, não como número apurado.</b> Num 3 estrelas, duas pessoas, "
             "cinco noites: <b>€ 55,30</b> fora da diária."),
            ("ingresso", 0, "Hospedagem",
             "Não apurada",
             "<b>Esta ficha não tem hospedagem</b> porque não apuramos diária média "
             "oficial para Paris. Preferimos a lacuna escrita ao número estimado. "
             "<b>A taxe de séjour, acima, incide sobre ela e é cobrada à parte.</b>"),
            ("ingresso", 0, "Transporte urbano",
             "Não apurado",
             "<b>Não apuramos tarifa de metrô nem de RER para esta ficha.</b> "
             "<b>Versalhes fica fora de Paris</b> e exige deslocamento que não está "
             "nesta conta."),
        ],
        "rodape_tabela": ("Valores em euro, por pessoa, apurados em 30 de setembro de "
                          "2026. <b>Quatro linhas estão fora do total</b>: o Orsay, que "
                          "não conseguimos apurar, a taxe de séjour, a hospedagem e o "
                          "transporte. <b>Os € 159,50 são o que paga quem não é "
                          "europeu; um europeu paga € 146,50 pelos mesmos seis "
                          "pontos.</b>"),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": ("Cada linha traz a fonte e a data no próprio campo. <b>Três sites "
                   "oficiais franceses recusaram leitura nesta apuração</b> — "
                   "notredamedeparis.fr e toureiffel.paris devolveram erro 403 ao cliente "
                   "HTTP, e musee-orsay.fr responde “Accès refusé” na página de tarifas. "
                   "<b>A Torre Eiffel abriu no navegador</b>, e é de lá que vem a tabela "
                   "de preços dela. <b>O Orsay não abriu de jeito nenhum, e por isso a "
                   "linha dele está sem valor.</b> Não contornamos bloqueio. <b>A taxe de "
                   "séjour é o único número que veio só de fontes secundárias "
                   "convergentes</b>, e a linha dela diz isso."),
    },
}

base.CIDADES = base.CIDADES + [
    ("bariloche", "Bariloche"), ("punta-cana", "Punta Cana"),
    ("porto", "Porto"), ("sevilha", "Sevilha"), ("miami", "Miami"),
    ("salvador", "Salvador"), ("madri", "Madri"), ("roma", "Roma"),
    ("paris", "Paris"),
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
