# -*- coding: utf-8 -*-
"""Madri: dez pontos, com fonte e data em cada numero.

Mesmo molde do miami/dados.py e do salvador/dados.py. O renderizador e o
novos/gera.py, chamado com VNL_DADOS=madri.

POR QUE MADRI, E POR QUE AGORA
------------------------------
Porque a home promete. O bloco "Roteiro de publicacao" lista Madri, Roma,
Paris e Granada, nessa ordem, e diz "um destino novo por semana". Madri
era a proxima da fila.

Tambem da corpo a Espanha, que ate agora tinha so Sevilha numa ficha de
tres dias, e forma viagem iberica com Lisboa e Porto.

O ACHADO: A ENTRADA DE GRACA DO PALACIO REAL E SUA
--------------------------------------------------
A Patrimonio Nacional concede entrada gratuita ao Palacio Real de Madrid,
de segunda a quinta, a "ciudadanos de la Union Europea, residentes... Y
CIUDADANOS IBEROAMERICANOS" com documento que prove a nacionalidade.

Brasileiro entra nessa lista. E quase todo guia escreve "gratis para
cidadaos da UE", o que faz o leitor daqui concluir que nao tem direito -
e pagar os 18 euros por nada.

Conferido na pagina oficial da Patrimonio Nacional em 29/set/2026.

A ARITMETICA QUE ORGANIZA A FICHA
---------------------------------
Os seis pontos pagos somam 101 euros. Quatro deles tem janela gratuita:

    Prado           15 EUR    gratis 18h-20h de seg a sab
    Reina Sofia     12 EUR    gratis 19h-21h, e 12h30-14h30 no domingo
    Thyssen         14 EUR    gratis segunda, 12h-16h
    Palacio Real    18 EUR    gratis seg a qui, para latino-americano

Sao 59 euros que podem virar zero. A conta cai de 101 para 42.

E TRES DELAS ENCADEIAM NUMA SEGUNDA
-----------------------------------
De outubro a marco:

    12h-16h   Thyssen         14 EUR
    16h-18h   Palacio Real    18 EUR
    18h-20h   Prado           15 EUR

Oito horas seguidas, 47 euros de bilhete, zero pago. De abril a setembro
a janela do palacio e 17h-19h e encosta na do Prado - ainda da, mais
apertado. Nenhum guia que abrimos publica essa corrente.

O QUE ESTA APURACAO NAO TEM, E FICA ESCRITO
-------------------------------------------
A pagina de horarios e precos do Museo del Prado esta atras de protecao
anti-bot da Cloudflare e NAO ABRIU para conferencia direta - nem por
leitura de pagina nem por navegador. Nao contornamos protecao anti-bot.

O que publicamos do Prado vem de duas fontes que abriram: a indexacao do
proprio dominio do museu, e a ficha do esMadrid, que e o portal oficial
de turismo da cidade de Madri. As duas batem. Esta dito na ficha dele.

E o mesmo tipo de lacuna que Sevilha anotou quando o TUSSAM ficou atras
da Cloudflare e o Metro devolveu 401.

Nao apuramos tarifa de metro, de trem ao aeroporto, nem diaria media de
hospedagem com fonte oficial.

Apuracao de 29 de setembro de 2026.
"""

APURACAO = "29 de setembro de 2026"
APURACAO_CURTA = "29/set/2026"

FLAG = '<span class="flag">%s</span> '


def mapa(consulta):
    """Link para o Google Maps no padrao da casa."""
    import urllib.parse
    q = urllib.parse.quote(consulta)
    return ('<a class="mapa" href="https://www.google.com/maps/search/?api=1&query=%s"'
            ' target="_blank" rel="noopener" aria-label="Abrir %s no Google Maps">'
            '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
            '<path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z" stroke="currentColor"'
            ' stroke-width="1.8" stroke-linejoin="round"></path><circle cx="12" cy="10" r="2.5"'
            ' stroke="currentColor" stroke-width="1.8"></circle></svg><span>Ver no mapa</span></a>'
            % (q, consulta.split(",")[0]))


# =====================================================================
#  MADRI
# =====================================================================
MADRI = {
    "slug": "madri",
    "nome": "Madri",
    "pais": "Espanha",
    "regiao": "europa",
    "titulo": "Madri: 10 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 10 pontos de Madri — com a entrada "
                  "gratuita do Palácio Real que vale para brasileiro e as janelas "
                  "de graça que encadeiam numa segunda-feira."),
    "abertura": ("Dez pontos com preço em euro, horário e fonte conferidos em 29 de "
                 "setembro de 2026 — e o direito que quase todo guia esconde do leitor "
                 "brasileiro: <b>a entrada gratuita do Palácio Real não é só para "
                 "europeu. Cidadão latino-americano com passaporte entra de graça, e "
                 "são € 18 por pessoa.</b>"),
    "busca": ("madri madrid espanha europa paseo del arte museo del prado reina sofia "
              "guernica thyssen bornemisza palacio real patrimonio nacional almudena "
              "plaza mayor puerta del sol mercado de san miguel parque del retiro "
              "palacio de cristal templo de debod bernabeu real madrid entrada gratuita "
              "iberoamericano gratis"),
    "grupos": [
        {"id": "g1", "titulo": "O Paseo del Arte",
         "intro": ("Os três grandes museus, em menos de um quilômetro de avenida — e os "
                   "três têm horário em que não cobram nada. As janelas não coincidem, "
                   "e é isso que decide a ordem dos dias.")},
        {"id": "g2", "titulo": "O Madri dos Áustrias",
         "intro": ("O palácio, a catedral e as duas praças. Aqui está o achado desta "
                   "página, e ele vale € 18 por pessoa para quem tem passaporte "
                   "brasileiro.")},
        {"id": "g3", "titulo": "Parques, vistas e o estádio",
         "intro": ("O que se faz ao ar livre, o pôr do sol mais disputado da cidade — "
                   "que precisa de reserva mesmo sendo grátis — e o ingresso mais caro "
                   "da ficha.")},
    ],
    "pontos": [

        # ---------------------------------------------------------- g1
        {
            "id": "museo-del-prado",
            "grupo": "g1",
            "nome": "Museo Nacional del Prado",
            "tag": "Museu",
            "preco_val": "€ 15",
            "preco_nota": "grátis nas duas horas antes de fechar",
            "campos": [
                ("Valor da entrada",
                 "<b>Inteira € 15.</b> <b>Reduzida € 7,50.</b> Com guia oficial impresso, "
                 "€ 24; audioguia custa € 5 à parte.<br>"
                 "<b>E é gratuito nas duas horas antes de fechar, todos os dias:</b> "
                 "<b>de segunda a sábado, das 18h às 20h</b>; <b>domingos e feriados, das "
                 "17h às 19h</b>. Não é promoção nem dia específico — é a grade normal, o "
                 "ano inteiro.<br>"
                 "Fontes: indexação do próprio domínio do museu e ficha do <b>esMadrid</b>, "
                 "o portal oficial de turismo da cidade, consultadas em 29/set/2026. As "
                 "duas coincidem nos preços e nos horários.<br>"
                 + FLAG % "Fonte oficial não aberta" +
                 "<b>a página de horários e preços do próprio Prado está atrás de "
                 "proteção anti-bot da Cloudflare e não abriu para conferência direta</b> "
                 "— nem por leitura de página, nem por navegador. Não contornamos esse "
                 "tipo de proteção. Por isso citamos as duas fontes que abriram, e "
                 "dizemos qual não abriu."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias.</b> <b>Segunda a sábado, das 10h às 20h</b>; "
                 "<b>domingos e feriados, das 10h às 19h</b>. A bilheteria abre às 9h45.<br>"
                 "<b>A janela gratuita é a mais disputada do dia</b>, com fila que se "
                 "forma antes das 18h. Duas horas também não são muito para um acervo "
                 "deste tamanho: quem vai de graça escolhe salas em vez de ver tudo."),
                ("Pontos de referência",
                 "Fica no eixo do <b>Paseo del Prado</b>, com o <b>Real Jardín Botánico</b> "
                 "ao lado e o <b>Parque del Retiro</b> subindo a ladeira atrás. O "
                 "<b>Thyssen</b> fica a poucos minutos a pé ao norte e o <b>Reina "
                 "Sofía</b> ao sul — os três formam o Paseo del Arte e se fazem "
                 "andando.<br>"
                 + mapa("Museo del Prado, Paseo del Prado, Madrid")),
            ],
        },
        {
            "id": "reina-sofia",
            "grupo": "g1",
            "nome": "Museo Nacional Centro de Arte Reina Sofía",
            "tag": "Museu",
            "preco_val": "€ 12",
            "preco_nota": "grátis à noite; fecha terça",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página oficial de horários e tarifas do museu, consultada em "
                 "29/set/2026.<br>"
                 "<b>Entrada geral € 12.</b> Há bilhete de duas visitas por € 18, válido "
                 "por um ano.<br>"
                 "<b>A janela gratuita, e ela muda no domingo:</b> de <b>segunda e de "
                 "quarta a sábado, das 19h às 21h</b>. <b>No domingo, das 12h30 às "
                 "14h30</b> — muito mais cedo, porque o museu fecha às 14h30 nesse dia. "
                 "Quem chega domingo às 19h encontra a porta fechada.<br>"
                 "<b>Mesmo de graça você precisa de bilhete.</b> A página é literal: "
                 "<i>“Durante el horario gratuito también necesitas una entrada”</i>, e "
                 "dá para reservar online. É o detalhe que mais derruba gente na porta.<br>"
                 "<b>A gratuidade do horário vale só para visitante individual</b>, não "
                 "para grupo. E há <b>entrada gratuita permanente</b> para menores de 18, "
                 "maiores de 65 e estudantes — mas <b>só na bilheteria</b>, não online."),
                ("Dias em que não funciona",
                 "<b>Fecha às terças-feiras</b> — e essa é a armadilha de Madri, porque "
                 "o Prado e o Thyssen abrem nesse dia. Um roteiro que marque o Reina "
                 "Sofía para terça perde o Guernica.<br>"
                 "<b>Segunda e de quarta a sábado:</b> 10h às 21h. <b>Domingo:</b> 10h "
                 "às 14h30.<br>"
                 "<b>Fecha também</b> em 1 e 6 de janeiro, 1 de maio, 15 de maio, 9 de "
                 "novembro, 24, 25 e 31 de dezembro. O museu avisa que 15 de maio e 9 de "
                 "novembro podem mudar conforme o calendário laboral da Comunidade de "
                 "Madri.<br>"
                 "<b>Dias de entrada gratuita o dia inteiro:</b> 18 de abril, 18 e 22 de "
                 "maio, 12 de outubro e 6 de dezembro."),
                ("Pontos de referência",
                 "Na <b>Ronda de Atocha</b>, colado à estação de Atocha — é o museu mais "
                 "fácil de encaixar em dia de chegada ou de partida de trem. O museu "
                 "recomenda entrar pelo <b>Edifício Nouvel</b> quem já comprou "
                 "online.<br>"
                 + mapa("Museo Reina Sofia, Calle de Santa Isabel 52, Madrid")),
            ],
        },
        {
            "id": "thyssen",
            "grupo": "g1",
            "nome": "Museo Nacional Thyssen-Bornemisza",
            "tag": "Museu",
            "preco_val": "€ 14",
            "preco_nota": "grátis segunda, 12h às 16h",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página oficial de horários e preços, consultada em "
                 "29/set/2026.<br>"
                 "<b>Inteira € 14.</b> <b>Reduzida € 10</b> para maiores de 65, "
                 "pensionistas e estudantes.<br>"
                 "<b>É gratuito às segundas-feiras, das 12h às 16h</b>, por patrocínio "
                 "da Mastercard — e nesse horário <b>não é preciso comprar bilhete "
                 "nenhum</b>.<br>"
                 "<b>A ressalva que importa:</b> a gratuidade cobre a <b>Coleção "
                 "Permanente</b>, não as exposições temporárias. Se você foi por uma "
                 "temporária específica, a segunda não resolve.<br>"
                 "<b>E repare no encaixe:</b> a segunda é justamente o dia em que o "
                 "museu só abre das 12h às 16h. Ou seja, <b>na segunda o Thyssen é de "
                 "graça durante todo o tempo em que está aberto</b>."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias, com grade que muda por estação.</b><br>"
                 "<b>De 1º de setembro a 30 de junho:</b> segunda 12h às 16h; de terça a "
                 "sexta e domingo, 10h às 19h; <b>sábado até as 23h</b>.<br>"
                 "<b>De 1º de julho a 31 de agosto:</b> segunda 12h às 16h; de terça a "
                 "sexta 10h às 21h; sábado 10h às 23h; domingo 10h às 19h.<br>"
                 "<b>O sábado até as 23h é a grade mais generosa do Paseo del Arte</b> — "
                 "nenhum dos outros dois abre à noite.<br>"
                 "<b>Fecha</b> em 1º de janeiro, 1º de maio e 25 de dezembro."),
                ("Pontos de referência",
                 "No <b>Paseo del Prado</b>, em frente à fonte de Netuno, entre o Prado e "
                 "a Gran Vía. É o museu do meio do Paseo del Arte, e o mais rápido de "
                 "percorrer dos três.<br>"
                 + mapa("Museo Thyssen-Bornemisza, Paseo del Prado 8, Madrid")),
            ],
        },

        # ---------------------------------------------------------- g2
        {
            "id": "palacio-real",
            "grupo": "g2",
            "nome": "Palacio Real de Madrid",
            "tag": "Palácio",
            "preco_val": "€ 18",
            "preco_nota": "e grátis para brasileiro, seg a qui",
            "campos": [
                ("Valor da entrada",
                 "Fonte: <b>Patrimonio Nacional</b>, página oficial de tarifa gratuita, "
                 "consultada em 29/set/2026.<br>"
                 "<b>Inteira € 18. Reduzida € 7.</b> Menores de 5 anos não pagam.<br>"
                 "<b>E aqui está o achado desta página.</b> A tarifa gratuita do palácio "
                 "não é só para europeu. O texto oficial concede entrada livre a "
                 "cidadãos da União Europeia, residentes e portadores de autorização de "
                 "trabalho na UE <b>e a “ciudadanos iberoamericanos”</b> que apresentem "
                 "prova de nacionalidade — <b>documento de identidade, passaporte ou "
                 "carteira de motorista</b>.<br>"
                 "<b>Brasileiro está nessa lista.</b> São € 18 por pessoa que quase todo "
                 "guia faz você pagar, porque escreve só “grátis para cidadãos da UE”.<br>"
                 "<b>Quando:</b> de <b>segunda a quinta</b>, das <b>16h às 18h de outubro "
                 "a março</b> e das <b>17h às 19h de abril a setembro</b>.<br>"
                 "<b>As três condições que anulam o direito se você não souber:</b> a "
                 "entrada gratuita vale <b>só para visita livre</b> — visita guiada não "
                 "entra; o bilhete <b>só sai na bilheteria física</b>, não online; e o "
                 "acesso é permitido <b>até 60 minutos antes do fechamento</b>.<br>"
                 "<b>Leve o passaporte.</b> Sem documento que prove a nacionalidade, não "
                 "há gratuidade.<br>"
                 "Há ainda entrada livre em <b>18 de maio</b>, Dia Internacional dos "
                 "Museus, e em <b>12 de outubro</b>, festa nacional da Espanha."),
                ("Dias em que não funciona",
                 FLAG % "Grade completa não apurada" +
                 "não levantamos a grade de horários dia a dia do palácio nesta rodada, "
                 "e não vamos publicar horário que não conferimos.<br>"
                 "<b>O que está confirmado</b> é a janela da tarifa gratuita, acima, e "
                 "que ela vale <b>de segunda a quinta</b> — ou seja, <b>sexta, sábado e "
                 "domingo não têm entrada gratuita</b>, nem para brasileiro nem para "
                 "europeu.<br>"
                 "<b>O palácio fecha em dias de ato oficial</b>, sem aviso longo, porque "
                 "é residência de Estado em uso. Confira na véspera."),
                ("Pontos de referência",
                 "Na <b>Plaza de Oriente</b>, com a <b>Catedral de la Almudena</b> do "
                 "outro lado da praça — os dois se fazem na mesma tarde, e a catedral é "
                 "gratuita. O <b>Jardín de Sabatini</b> fica na lateral norte, aberto e "
                 "sem bilheteria.<br>"
                 + mapa("Palacio Real de Madrid, Calle de Bailen, Madrid")),
            ],
        },
        {
            "id": "almudena",
            "grupo": "g2",
            "nome": "Catedral de la Almudena",
            "tag": "Catedral",
            "preco_val": "Grátis",
            "preco_nota": "a nave; museu e cúpula € 7",
            "campos": [
                ("Valor da entrada",
                 "<b>Entrar na catedral não custa nada</b>, e pede-se <b>donativo "
                 "voluntário de € 1</b> por pessoa, para manutenção do prédio.<br>"
                 "<b>O que é pago é o museu com a cúpula: € 7 a inteira</b>, € 5 a "
                 "reduzida e € 3 a de estudante. São coisas separadas — dá para ver a "
                 "catedral inteira sem pagar e sem subir.<br>"
                 "<b>A cripta</b> se visita à parte, também com donativo sugerido de "
                 "€ 1.<br>"
                 + FLAG % "Fonte não oficial" +
                 "os valores acima não vieram da página da própria catedral, e sim de "
                 "fontes secundárias que coincidem entre si. Confirme na porta."),
                ("Dias em que não funciona",
                 "<b>A catedral abre todos os dias</b>: de <b>setembro a junho, das 10h "
                 "às 20h30</b>; em <b>julho e agosto, das 10h às 21h</b>.<br>"
                 "<b>O museu e a cúpula têm grade muito mais curta: de segunda a sábado, "
                 "das 10h às 14h30.</b> Fecham no domingo e fecham à tarde — quem "
                 "combinar a catedral com o Palácio Real na janela gratuita das 16h "
                 "<b>já perdeu a cúpula</b> naquele dia.<br>"
                 "<b>A cripta</b> abre de segunda a domingo, das 10h às 14h e das 16h30 "
                 "às 20h."),
                ("Pontos de referência",
                 "De frente para o <b>Palácio Real</b>, na Calle de Bailén. A "
                 "<b>Plaza Mayor</b> fica a poucos minutos a pé a leste, e o "
                 "<b>Mercado de San Miguel</b> no caminho entre os dois.<br>"
                 + mapa("Catedral de la Almudena, Calle de Bailen 10, Madrid")),
            ],
        },
        {
            "id": "plaza-mayor-sol",
            "grupo": "g2",
            "nome": "Plaza Mayor e Puerta del Sol",
            "tag": "Praças",
            "preco_val": "Grátis",
            "preco_nota": "as duas; o que se consome, não",
            "campos": [
                ("Valor da entrada",
                 "<b>Não existe bilhete.</b> As duas são via pública, abertas 24 horas, "
                 "sem portão e sem horário.<br>"
                 "<b>O que custa é sentar.</b> As mesas na Plaza Mayor cobram preço de "
                 "praça turística, e "
                 + FLAG % "não apuramos cardápio" +
                 "porque são estabelecimentos privados sem tabela publicada.<br>"
                 "<b>Na Puerta del Sol</b> ficam o marco do <b>quilômetro zero</b> das "
                 "estradas espanholas e a estátua do <b>urso com o medronheiro</b>, que "
                 "é o símbolo da cidade — os dois de graça, os dois com fila para "
                 "foto."),
                ("Dias em que não funciona",
                 "<b>Nunca fecham.</b><br>"
                 "<b>O que muda é a lotação</b>, e de forma extrema: a Puerta del Sol é "
                 "onde Madri se reúne na virada do ano para comer as doze uvas. Se a sua "
                 "viagem pega 31 de dezembro, a praça não é um ponto turístico naquela "
                 "noite — é um evento com controle de acesso."),
                ("Pontos de referência",
                 "As duas ficam a cinco minutos de caminhada uma da outra, ligadas pela "
                 "Calle Mayor. O <b>Mercado de San Miguel</b> está colado à Plaza Mayor, "
                 "e a <b>Gran Vía</b> sobe a partir da Sol.<br>"
                 + mapa("Plaza Mayor, Madrid")),
            ],
        },
        {
            "id": "mercado-san-miguel",
            "grupo": "g2",
            "nome": "Mercado de San Miguel",
            "tag": "Mercado",
            "preco_val": "Grátis",
            "preco_nota": "entrar; as bancas, não",
            "campos": [
                ("Valor da entrada",
                 "<b>Entrar não custa nada.</b> É um mercado coberto de estrutura de "
                 "ferro e vidro, do começo do século XX, hoje inteiramente dedicado a "
                 "bancas de comida e bebida.<br>"
                 + FLAG % "Preços de banca não apurados" +
                 "cada banca é um negócio próprio, sem tabela publicada e com preço que "
                 "varia muito. Não inventamos uma média.<br>"
                 "<b>O que vale saber antes:</b> é <b>caro para o padrão de Madri</b> e "
                 "funciona por porções pequenas — a conta sobe rápido sem parecer que "
                 "subiu. Vale como passagem e prova, não como jantar."),
                ("Dias em que não funciona",
                 FLAG % "Horário não confirmado em fonte oficial" +
                 "não localizamos página oficial do mercado com horário publicado nesta "
                 "apuração, e não vamos imprimir um horário que não conferimos.<br>"
                 "<b>O que é seguro dizer:</b> abre todos os dias e vai até tarde, e as "
                 "bancas têm horários próprios dentro do horário do mercado."),
                ("Pontos de referência",
                 "Colado à <b>Plaza Mayor</b>, na Plaza de San Miguel. Está no caminho "
                 "natural entre a Plaza Mayor e o Palácio Real.<br>"
                 + mapa("Mercado de San Miguel, Plaza de San Miguel, Madrid")),
            ],
        },

        # ---------------------------------------------------------- g3
        {
            "id": "parque-del-retiro",
            "grupo": "g3",
            "nome": "Parque del Retiro e o Palacio de Cristal",
            "tag": "Parque",
            "preco_val": "Grátis",
            "preco_nota": "o parque e o palácio de vidro",
            "campos": [
                ("Valor da entrada",
                 "<b>O parque é público e não se cobra entrada.</b> O <b>Palacio de "
                 "Cristal</b>, a estufa de ferro e vidro no meio dele, também é "
                 "<b>gratuito</b> — e funciona como sala de exposição do Reina Sofía, "
                 "com mostras que mudam.<br>"
                 "<b>O que custa</b> é alugar barco no lago, e "
                 + FLAG % "não apuramos a tarifa" +
                 "do aluguel.<br>"
                 "O Retiro é <b>Patrimônio Mundial da UNESCO desde 2021</b>, no conjunto "
                 "“Paisaje de la Luz” junto com o Paseo del Prado."),
                ("Dias em que não funciona",
                 FLAG % "Horário do parque não apurado" +
                 "o Retiro tem horário de abertura e fechamento que muda com a estação, "
                 "e não o confirmamos em fonte oficial nesta rodada.<br>"
                 "<b>O que é conhecido e vale como aviso:</b> o parque <b>fecha em "
                 "episódios de vento forte</b>, por risco de queda de árvore, e isso "
                 "acontece de verdade em Madri. O <b>Palacio de Cristal</b> tem grade "
                 "própria, mais curta que a do parque."),
                ("Pontos de referência",
                 "Sobe a ladeira atrás do <b>Museo del Prado</b> — os dois se fazem no "
                 "mesmo dia sem transporte, e é o encaixe mais natural do Paseo del "
                 "Arte. O <b>Real Jardín Botánico</b> fica entre um e outro, e esse "
                 "cobra entrada.<br>"
                 + mapa("Parque del Retiro, Madrid")),
            ],
        },
        {
            "id": "templo-de-debod",
            "grupo": "g3",
            "nome": "Templo de Debod",
            "tag": "Templo egípcio",
            "preco_val": "Grátis",
            "preco_nota": "mas peça reserva antes",
            "campos": [
                ("Valor da entrada",
                 "Fonte: Ayuntamiento de Madrid, consultado em 29/set/2026.<br>"
                 "<b>A entrada é gratuita.</b> É um templo egípcio do século II a.C., "
                 "desmontado e doado pelo Egito à Espanha em 1968, e remontado aqui.<br>"
                 "<b>E aqui está a pegadinha do grátis:</b> <b>o aforo é limitado</b>, e "
                 "a prefeitura é explícita — <b>“sin reserva no se garantiza el "
                 "acceso”</b>. A reserva é gratuita e se faz em "
                 "<b>madrid.es/debodreservas</b>.<br>"
                 "<b>Grátis sem reserva não é grátis com entrada garantida.</b> Em hora "
                 "de pico há espera, e pode não entrar."),
                ("Dias em que não funciona",
                 "<b>Fecha todas as segundas-feiras</b>, inclusive segundas que sejam "
                 "feriado.<br>"
                 "<b>De terça a domingo e feriados:</b> das 10h às 20h, com <b>última "
                 "entrada 30 minutos antes de fechar</b>. <b>No verão, de 15 de junho a "
                 "15 de setembro:</b> das 10h às 19h.<br>"
                 "<b>Fecha também</b> em 1 e 6 de janeiro, 1º de maio, 24, 25 e 31 de "
                 "dezembro.<br>"
                 "<b>Repare no conflito de agenda:</b> a segunda-feira é o dia em que o "
                 "Thyssen é de graça e o Palácio Real abre a janela gratuita — e é "
                 "justamente o dia em que Debod está fechado."),
                ("Pontos de referência",
                 "No <b>Parque del Oeste</b>, perto da Plaza de España. <b>É o pôr do sol "
                 "mais disputado de Madri</b>, com o templo refletido no espelho d'água e "
                 "a serra ao fundo — e é por isso que o aforo enche no fim da tarde. O "
                 "<b>Teleférico de Madrid</b> parte dali e cobra à parte.<br>"
                 + mapa("Templo de Debod, Calle Ferraz 1, Madrid")),
            ],
        },
        {
            "id": "bernabeu",
            "grupo": "g3",
            "nome": "Estadio Santiago Bernabéu",
            "tag": "Estádio",
            "preco_val": "€ 35",
            "preco_nota": "online; € 38 na bilheteria",
            "campos": [
                ("Valor da entrada",
                 "Fonte: Real Madrid C.F., site oficial do Tour Bernabéu, consultado em "
                 "29/set/2026.<br>"
                 "<b>A partir de € 35 comprando online</b>, e <b>€ 38 na bilheteria</b>. "
                 "<b>São € 3 de diferença por comprar na hora</b>, e é a única linha "
                 "desta ficha em que o canal de compra muda o preço.<br>"
                 "<b>É o ingresso mais caro da página</b> — mais que o dobro do Prado, e "
                 "quase o dobro do Palácio Real.<br>"
                 "<b>O “a partir de” é real:</b> o tour tem modalidades diferentes, e o "
                 "valor acima é o piso da entrada Classic, de visita livre."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias do ano, exceto 25 de dezembro e 1º de "
                 "janeiro.</b><br>"
                 "<b>De segunda a sábado:</b> das 9h às 19h. <b>Domingos e feriados:</b> "
                 "das 9h30 às 18h30.<br>"
                 "<b>E o aviso que o próprio clube publica:</b> por causa dos eventos no "
                 "estádio, <b>o tour pode mudar de percurso e de horário</b>, avisando no "
                 "site, na bilheteria ou na porta. <b>Em dia de jogo o roteiro encolhe</b> "
                 "— confira antes, e evite marcar o tour para a véspera de partida em "
                 "casa."),
                ("Pontos de referência",
                 "Na <b>Avenida de Concha Espina</b>, no Paseo de la Castellana, ao norte "
                 "do centro. <b>Não é caminhada desde o Paseo del Arte</b> — é "
                 "deslocamento, e fica fora do eixo de todos os outros pontos desta "
                 "ficha.<br>"
                 + mapa("Estadio Santiago Bernabeu, Avenida de Concha Espina 1, Madrid")),
            ],
        },
    ],
}

DESTINOS = [MADRI]
