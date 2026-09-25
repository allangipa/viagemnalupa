# -*- coding: utf-8 -*-
"""Sevilha completa: a fatia 1 mais os sete pontos da fatia 2.

Mesmo molde do porto/dados.py. A fatia 1 mora em fatia1.py e e carregada
POR CAMINHO - import normal devolveria o `dados` que outro gerador ja
deixou em sys.modules, calado.

O QUE A FATIA 2 ACHOU
---------------------

1. A TORRE DEL ORO E DE GRACA, E QUASE TODO MUNDO PUBLICA QUE CUSTA 3
   EUROS. A pagina oficial da Fundacion Museo Naval nao tem UM UNICO
   simbolo de euro - conferido, zero ocorrencias - e diz: "El acceso al
   museo es libre, aunque se solicita una aportacion voluntaria para su
   sostenimiento". Os 3 euros vem de agregador.

   E o mesmo tipo de achado da Torre dos Clerigos no Porto, so que ao
   contrario: la o agregador barateava, aqui ele encarece.

2. DOIS PALACIOS COBRAM POR ANDAR, COMO O ALCAZAR. A Casa de Pilatos
   vende a planta baja por 12 e a alta por 6 - quem quer a casa inteira
   paga 18, e nao 12. E o mesmo desenho do Cuarto Real Alto do Alcazar,
   que a fatia 1 ja tinha achado. Nao e coincidencia: e como os palacios
   privados de Sevilha vendem.

3. A SEGUNDA DE GRACA DAS DUENAS CUSTA UM EURO. A partir das 16h a
   entrada vale 0 euro - mais "1 euro de taxa administrativa". Gratis com
   taxa nao e gratis, e a linha diz isso.

4. O MUSEU DE BELAS ARTES E GRATIS PARA QUEM TEM PASSAPORTE DA UNIAO
   EUROPEIA. Brasileiro paga 1,50. E a unica linha desta apuracao em que
   a nacionalidade do leitor muda o preco, e por isso ela esta escrita do
   ponto de vista de quem le este site.

5. A PRACA DE TOUROS TEM UMA EXCECAO SEM PRECO. A propria tabela oficial
   diz "estas tarifas no son aplicables el miercoles de 17:30 a 21:30" e
   NAO publica qual tarifa se aplica. Lacuna da fonte, escrita como
   lacuna.

6. A ENTRADA DA CATEDRAL JA INCLUI OUTRA IGREJA. A pagina de horarios e
   tarifas da Catedral diz que a visita geral "incluye la entrada
   gratuita a Iglesia de El Salvador". Quem paga os 13 euros tem a
   segunda igreja no mesmo bilhete e costuma nao saber.

O QUE FICOU DE FORA, E POR QUE
------------------------------
    Basilica de la Macarena      o site da Hermandad nao publica preco
    Hospital de los Venerables   o dominio da Fundacion Focus nao resolve
    Antiquarium                  sem pagina de preco propria; o site das
                                 Setas ja e citado na fatia 1 por isso

Nenhum dos tres entrou com numero de terceiro. Ponto sem fonte oficial
nao vira linha.

AS FOTOS DESTA FATIA NAO FORAM LEVANTADAS
-----------------------------------------
Os cinco pontos da fatia 1 tem foto; os sete desta nao. O aviso da ficha
conta as fotos e vai dizer isso sozinho - foi para isso que ele passou a
contar, depois de tres paginas publicadas afirmando "nasce sem foto"
tendo foto.

Apuracao de 25 de setembro de 2026.
"""
import importlib.util
import os

AQUI = os.path.dirname(os.path.abspath(__file__))

_spec = importlib.util.spec_from_file_location(
    "sevilha_fatia1", os.path.join(AQUI, "fatia1.py"))
_d1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d1)

APURACAO = _d1.APURACAO
APURACAO_CURTA = _d1.APURACAO_CURTA
mapa = _d1.mapa

GRUPOS2 = [
    {"id": "g4", "titulo": "Os dois palácios que cobram por andar",
     "intro": "A Casa de Pilatos e as Dueñas repetem o desenho do Alcázar: o preço "
              "anunciado não é o da casa inteira. Somar os andares muda a conta em "
              "50% num caso e em nada no outro — e só dá para saber lendo a tabela."},
    {"id": "g5", "titulo": "Três que não cobram nada — e um deles desmente o que você leu",
     "intro": "Dois são de graça por serem públicos. O terceiro é de graça e aparece "
              "cobrando três euros em quase todo lugar que não seja o site oficial."},
    {"id": "g6", "titulo": "O museu de € 1,50 e a praça de touros",
     "intro": "Um deles é o único ponto desta apuração em que o seu passaporte muda o "
              "preço. O outro tem uma exceção de tarifa que a própria fonte não "
              "explica."},
]

PONTOS2 = [
    # ------------------------------------------------------------------ g4
    {
        "id": "casa-de-pilatos", "grupo": "g4",
        "nome": "Casa de Pilatos", "tag": "Palácio",
        "preco_val": "€ 12",
        "preco_nota": "a planta alta custa € 6 à parte; a casa inteira sai € 18",
        "campos": [
            ("Valor da entrada, que tem dois andares e dois preços",
             "Fonte: página da Casa de Pilatos no site da Fundación Casa Ducal de "
             "Medinaceli (fundacionmedinaceli.org), consultada em 25/set/2026.<br>"
             "<b>Planta baja: € 12,00.</b><br>"
             "<b>Planta alta: € 6,00</b>, cobrada <b>à parte</b>.<br>"
             "<b>A casa inteira custa € 18,00</b> — 50% acima do valor que aparece "
             "anunciado. É o mesmo desenho do Cuarto Real Alto do Alcázar, e não é "
             "coincidência: é como os palácios privados de Sevilha vendem."),
            ("Quem paga menos, e quem não paga",
             "Mesma fonte, mesma data.<br>"
             "<b>Grupos escolares: € 8,00.</b><br>"
             "<b>Crianças até 11 anos: grátis</b>, acompanhadas de um adulto.<br>"
             "<b>Deficiência acima de 50%: metade do preço.</b> "
             "<b>Acima de 65%: grátis.</b> Nos dois casos, mediante comprovação."),
            ("Horário",
             "Mesma fonte, mesma data.<br>"
             "<b>Todos os dias da semana, das 9h às 18h.</b><br>"
             "<span class=\"flag\">A página não publica hora de última entrada</span> "
             "e nem a lista de dias fechados no ano. Os outros palácios desta "
             "apuração publicam as duas coisas; este não."),
            ("Onde fica", mapa("Casa de Pilatos, Sevilha, Espanha")),
        ],
    },
    {
        "id": "palacio-de-las-duenas", "grupo": "g4",
        "nome": "Palacio de las Dueñas", "tag": "Palácio",
        "preco_val": "€ 15",
        "preco_nota": "com audioguia incluída; segunda à tarde sai € 1",
        "campos": [
            ("Valor da entrada",
             "Fonte: página <i>Info al visitante</i> do site oficial do Palacio de las "
             "Dueñas (lasduenas.es), consultada em 25/set/2026.<br>"
             "<b>Visita geral com audioguia: € 15,00.</b> A audioguia <b>já está "
             "incluída</b> — o que não acontece na Catedral, onde ela custa € 5,00 à "
             "parte.<br>"
             "<b>Reduzida: € 11,00</b> — menores de 25 anos, maiores de 65, pessoas com "
             "deficiência, desempregados e docentes, com comprovação.<br>"
             "<b>Residentes em Sevilha: € 10,00.</b> "
             "<b>Menores de 6 anos: grátis.</b>"),
            ("A segunda-feira grátis que custa um euro",
             "Mesma fonte, mesma data.<br>"
             "<b>Às segundas, a partir das 16h e até o fechamento, a entrada vale "
             "€ 0,00</b> — e o site cobra <b>€ 1,00 de taxa administrativa</b> sobre "
             "ela.<br>"
             "<b>Grátis com taxa não é grátis</b>, e é a diferença entre chegar sabendo "
             "e chegar achando que não ia pagar nada. O valor é pequeno; a surpresa, "
             "não."),
            ("As outras visitas, que são outro preço",
             "Mesma fonte, mesma data. O palácio vende cinco produtos além da entrada "
             "comum, e os preços não se parecem:<br>"
             "<b>Visita guiada: € 35,00</b>, ou <b>€ 28,00</b> reduzida.<br>"
             "<b>Visita com guia oficial: € 22,00.</b><br>"
             "<b>Visita noturna guiada: € 25,00.</b><br>"
             "<b>Ópera Carmen: € 49,00</b>, ou <b>€ 59,00</b> premium."),
            ("Horário, e o desalojo que começa antes do fechamento",
             "Mesma fonte, mesma data.<br>"
             "<b>Verão, de abril a setembro: 10h às 19h</b>, com acesso até <b>18h15</b>.<br>"
             "<b>Inverno, de outubro a março: 10h às 18h</b>, com acesso até <b>17h15</b>.<br>"
             "<b>O desalojo começa 45 minutos antes do fechamento</b> — a mesma regra do "
             "Real Alcázar, e o segundo ponto desta apuração a ter hora de sair "
             "diferente da hora de fechar.<br>"
             "<b>Fechado:</b> 25 de dezembro, 1º e 6 de janeiro. Em 24 e 31 de dezembro "
             "e 5 de janeiro, <b>fecha às 15h</b>."),
            ("Onde fica", mapa("Palacio de las Dueñas, Sevilha, Espanha")),
        ],
    },
    # ------------------------------------------------------------------ g5
    {
        "id": "torre-del-oro", "grupo": "g5",
        "nome": "Torre del Oro", "tag": "Torre e museu",
        "preco_val": "Grátis",
        "preco_nota": "contribuição voluntária; agregadores publicam € 3",
        "campos": [
            ("A entrada de € 3 que o site oficial não cobra",
             "Fonte: página do Museo Marítimo <i>Torre del Oro</i> no site da Fundación "
             "Museo Naval (fundacionmuseonaval.com), consultada em 25/set/2026.<br>"
             "<b>A página diz, textualmente: \"El acceso al museo es libre, aunque se "
             "solicita una aportación voluntaria para su sostenimiento\".</b><br>"
             "<b>Não há um único símbolo de euro na página inteira</b> — conferimos, "
             "são zero ocorrências. Não há tabela, não há tarifa reduzida, não há dia "
             "gratuito, porque não há cobrança.<br>"
             "<b>E quase todo agregador publica € 3,00</b>, com reduzida de € 1,50 e "
             "segunda-feira grátis. Nenhum desses números aparece na fonte oficial. "
             "Leve algum dinheiro para a contribuição, se quiser contribuir — mas não "
             "vá contando com uma bilheteira."),
            ("Horário, com uma hora de fechamento no meio do fim de semana",
             "Mesma fonte, mesma data.<br>"
             "<b>Segunda a sexta: 9h30 às 19h</b>, com <b>último acesso às 18h30</b>.<br>"
             "<b>Sábados, domingos e feriados: 10h30 às 19h</b>, mesmo último acesso.<br>"
             "<b>Aos sábados e domingos o museu fecha das 14h às 15h.</b> É uma hora "
             "morta no meio do dia, justamente quando mais gente circula pelo "
             "Guadalquivir.<br>"
             "<b>Em 5 de janeiro fecha às 14h</b>, com último acesso às 13h45.<br>"
             "<b>Fechado:</b> 1º e 6 de janeiro, Sexta-feira Santa, 1º de maio e 25 de "
             "dezembro."),
            ("O que se vê lá dentro",
             "Mesma fonte, mesma data. São <b>duas plantas visitáveis e um terraço "
             "panorâmico</b>.<br>"
             "A torre é do <b>século XIII</b>, almóada, e tem 36 metros. O nome vem do "
             "brilho dourado sobre o rio — e <b>a restauração de 2005 mostrou que o "
             "brilho não vinha de azulejo</b>, como se dizia, mas de uma argamassa de "
             "cal com palha prensada.<br>"
             "Antes de ser museu, o prédio foi capela, prisão de nobres e depósito de "
             "pólvora."),
            ("Onde fica", mapa("Torre del Oro, Sevilha, Espanha")),
        ],
    },
    {
        "id": "archivo-de-indias", "grupo": "g5",
        "nome": "Archivo General de Indias", "tag": "Arquivo",
        "preco_val": "Grátis",
        "preco_nota": "acesso livre à área monumental",
        "campos": [
            ("Valor da entrada",
             "Fonte: página de <i>Visitas</i> do Archivo General de Indias no site do "
             "Ministerio de Cultura de Espanha (cultura.gob.es), consultada em "
             "25/set/2026.<br>"
             "<b>A visita turística é gratuita e de acesso livre à área monumental.</b> "
             "Não há bilheteira, não há reserva obrigatória para a visita comum.<br>"
             "Fica a duzentos metros da Catedral e do Alcázar, no mesmo quarteirão — e "
             "é o ponto mais barato de fazer no intervalo entre os dois."),
            ("Horário",
             "Mesma fonte, mesma data.<br>"
             "<b>Terça a sábado: 9h30 às 17h</b>, com <b>última entrada às 16h30</b>.<br>"
             "<b>Domingos e feriados: 10h às 14h</b>, com <b>última entrada às 13h30</b>.<br>"
             "<b>Segunda-feira fechado.</b><br>"
             "<b>Fechado também:</b> 1º e 6 de janeiro, Quinta-feira Santa, Sexta-feira "
             "Santa, 24, 25 e 31 de dezembro."),
            ("Onde fica", mapa("Archivo General de Indias, Sevilha, Espanha")),
        ],
    },
    {
        "id": "iglesia-del-salvador", "grupo": "g5",
        "nome": "Iglesia Colegial del Salvador", "tag": "Igreja",
        "preco_val": "Grátis",
        "preco_nota": "para quem já pagou a entrada da Catedral",
        "campos": [
            ("A igreja que já está paga no bilhete da Catedral",
             "Fonte: página de <i>Horarios y tarifas</i> do site oficial da Catedral de "
             "Sevilha (catedraldesevilla.es), consultada em 25/set/2026.<br>"
             "<b>A página diz que a visita geral à Catedral \"incluye la entrada "
             "gratuita a Iglesia de El Salvador\".</b><br>"
             "Ou seja: <b>quem paga os € 13,00 da Catedral tem uma segunda igreja no "
             "mesmo bilhete</b> — e costuma não saber. É a maior igreja de Sevilha "
             "depois da Catedral, barroca, a dez minutos a pé.<br>"
             "<span class=\"flag\">Não achamos o preço avulso nem o horário próprio</span> "
             "a página da Catedral remete a uma página de horários e tarifas da "
             "própria Iglesia del Salvador que não conseguimos abrir. Quem não for "
             "visitar a Catedral fica sem saber quanto custa entrar só aqui."),
            ("Onde fica", mapa("Iglesia Colegial del Salvador, Sevilha, Espanha")),
        ],
    },
    # ------------------------------------------------------------------ g6
    {
        "id": "museo-bellas-artes", "grupo": "g6",
        "nome": "Museo de Bellas Artes", "tag": "Museu",
        "preco_val": "€ 1,50",
        "preco_nota": "grátis para cidadãos da União Europeia; brasileiro paga",
        "campos": [
            ("Valor da entrada, e a única linha em que o seu passaporte muda o preço",
             "Fonte: página de <i>Información general</i> do Museo de Bellas Artes de "
             "Sevilla, no portal Museos de Andalucía da Junta de Andalucía "
             "(museosdeandalucia.es), consultada em 25/set/2026.<br>"
             "<b>Preço: € 1,50.</b><br>"
             "<b>Gratuita para cidadãos da União Europeia acreditados</b> e para "
             "membros do ICOM.<br>"
             "<b>Quem lê este site paga.</b> É a única linha desta apuração em que a "
             "nacionalidade do visitante muda o valor, e por isso ela está escrita do "
             "ponto de vista de quem viaja do Brasil: € 1,50, com documento em mãos "
             "caso você tenha também passaporte europeu."),
            ("Os dias em que não se paga",
             "Mesma fonte, mesma data. Além da gratuidade para a União Europeia, o "
             "museu não cobra de ninguém em cinco ocasiões:<br>"
             "<b>28 de fevereiro</b>, Día de Andalucía.<br>"
             "<b>18 de maio</b>, Dia Internacional dos Museus.<br>"
             "<b>27 de setembro</b>, Dia Mundial do Turismo.<br>"
             "<b>4 de dezembro</b>, Día de la Bandera Andaluza.<br>"
             "<b>E nas Jornadas Europeas del Patrimonio</b>, cuja data muda a cada ano."),
            ("Horário, e os três avisos antes de fechar",
             "Mesma fonte, mesma data.<br>"
             "<b>Terça a sábado: 9h às 21h.</b> "
             "<b>Domingos e feriados: 9h às 15h.</b><br>"
             "<b>Segunda-feira fechado</b>, exceto segunda véspera de feriado, que abre "
             "com horário de feriado.<br>"
             "<b>Fechado:</b> 1º e 6 de janeiro, 1º de maio, 24, 25 e 31 de dezembro.<br>"
             "<b>E a saída tem três estágios, não um:</b> 45 minutos antes do "
             "fechamento vendem-se as <b>últimas 25 entradas</b>, se a lotação "
             "permitir; <b>30 minutos antes fecham os acessos às salas</b>; "
             "<b>15 minutos antes começa o desalojo</b>. É o ponto com a regra de "
             "fechamento mais detalhada de toda esta apuração."),
            ("Onde fica", mapa("Museo de Bellas Artes de Sevilla, Sevilha, Espanha")),
        ],
    },
    {
        "id": "plaza-de-toros", "grupo": "g6",
        "nome": "Plaza de Toros de la Real Maestranza", "tag": "Praça de touros",
        "preco_val": "€ 12",
        "preco_nota": "exceto quarta-feira à tarde, que a fonte não explica",
        "campos": [
            ("Valor da entrada",
             "Fonte: página de <i>Horarios y Tarifas</i> do site oficial da visita à "
             "Plaza de Toros de Sevilha (visitaplazadetorosdesevilla.com), consultada "
             "em 25/set/2026.<br>"
             "<b>Entrada geral: € 12,00.</b><br>"
             "<b>€ 7,00</b> para maiores de 65 anos e pensionistas, estudantes de 17 a "
             "25 anos com carteira, e jovens de 12 a 16 anos.<br>"
             "<b>Crianças de 7 a 11 anos: € 4,00.</b><br>"
             "<b>Família: € 29,00</b> — dois adultos e as crianças até 16 anos.<br>"
             "Grupos pagam tarifa a consultar, que a página não publica."),
            ("A quarta-feira à tarde, que tem outra tarifa e nenhum número",
             "Mesma fonte, mesma data.<br>"
             "<b>A própria tabela traz a ressalva: \"estas tarifas no son aplicables el "
             "miércoles de 17:30 h. a 21:30 h.\"</b><br>"
             "<span class=\"flag\">E não publica qual tarifa se aplica nesse horário</span> "
             "não diz se é mais cara, mais barata ou gratuita. A página declara a "
             "exceção e não a resolve.<br>"
             "<b>Se a sua visita cair numa quarta depois das 17h30, pergunte o preço "
             "antes de entrar na fila.</b>"),
            ("Horário, e o que muda em dia de corrida",
             "Mesma fonte, mesma data.<br>"
             "<b>Segunda a domingo: 9h30 às 21h30</b>, com a <b>bilheteira fechando 30 "
             "minutos antes</b>.<br>"
             "<b>Em dia de espetáculo taurino: 9h30 às 15h.</b> A visita encolhe pela "
             "metade, e é o tipo de coisa que só se descobre na porta.<br>"
             "<b>Durante a Feria de San Miguel</b> — em 2026, os dias 24 a 27 de "
             "setembro — o horário também é de <b>9h30 às 15h</b>."),
            ("Onde fica", mapa("Plaza de Toros de la Real Maestranza, Sevilha, Espanha")),
        ],
    },
]

SEVILHA = dict(_d1.SEVILHA)
SEVILHA["grupos"] = list(_d1.SEVILHA["grupos"]) + GRUPOS2
SEVILHA["pontos"] = list(_d1.SEVILHA["pontos"]) + PONTOS2

DESTINOS = [SEVILHA]
