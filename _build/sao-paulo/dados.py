# -*- coding: utf-8 -*-
"""Sao Paulo: o vigesimo nono destino, em catorze pontos e tres grupos.

Mesmo molde do florianopolis/dados.py, lido por novos/gera.py com VNL_DADOS=sao-paulo.

O ACHADO PRINCIPAL: CADA MUSEU TEM O SEU DIA GRATIS, E NENHUM COINCIDE
----------------------------------------------------------------------
Os sete museus pagos desta ficha somam R$ 261,20 de inteira, e todos tem
uma janela sem cobranca - em dias diferentes:
    terca      MASP (o dia todo), Lingua Portuguesa, Museu do Futebol
    quarta     Museu do Ipiranga, Museu Afro Brasil
    sexta      MASP a partir das 18h
    sabado     Pinacoteca
    domingo    MAM, Lingua Portuguesa; Pinacoteca no 2o domingo; Ipiranga no 1o
E a terca, que e o dia mais gratis da cidade, e o dia em que a Pinacoteca
FECHA: ela abre "de quarta a segunda", inclusive na segunda.

O SEGUNDO: O DOMINGO DA PAULISTA VAI ATE AS 16H, E O ONIBUS E DE GRACA
----------------------------------------------------------------------
A Subprefeitura Se: a Paulista fica so para pedestres "das 9h as 16h". E a
SPTrans: "Aos domingos, nao ha cobranca de tarifa nos onibus". Metro e trem
continuam cobrando R$ 5,40.

O QUE FICOU SEM RESPOSTA
----------------------------------------------------------------------
    Mercadao        horario oficial: o site mais citado diz nao ter vinculo
                    com orgao nenhum
    Ipiranga        o preco vem da plataforma de venda indicada pelo museu
                    (Fever); o site do museu nao publica valor em R$
    Expresso Aeroporto  sem tarifa propria publicada; o quadro da CPTM so
                    traz o unitario de R$ 5,40
    Beco do Batman  se a obra de requalificacao (mai/2026, ~5 meses) acabou
    Ibirapuera      o horario 5h a 0h vem de pagina oficial de 2022
    taxa turistica  nenhuma achada; ausencia nao se prova com documento

Apuracao de 15 de novembro de 2026. A diaria vem do Panorama da Hotelaria
Brasileira, 20a edicao (FOHB/HotelInvest), paginas 26 e 27, guardado em
fontes/fohb-panorama-20-sao-paulo.txt.
"""

APURACAO = "15 de novembro de 2026"
APURACAO_CURTA = "15/nov/2026"

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


LACUNA = FLAG % "Lacuna declarada"

# =====================================================================
#  SAO PAULO
# =====================================================================
SAO_PAULO = {
    "slug": "sao-paulo",
    "nome": "São Paulo",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "São Paulo: 14 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 14 pontos de São Paulo, com o dia grátis de cada "
                  "museu, que nunca coincide, e o domingo em que a Paulista fecha às 16h e o "
                  "ônibus não cobra."),
    "abertura": ("Catorze pontos de São Paulo com preço, horário e fonte conferidos em 15 de "
                 "novembro de 2026 — e a regra que decide a viagem: <b>os sete museus pagos "
                 "desta lista somam R$ 261,20 de inteira, e cada um tem o seu dia grátis, em "
                 "dias diferentes.</b> O MASP não cobra na terça, que é justamente o dia em que "
                 "a Pinacoteca fecha. E no domingo a Paulista é dos pedestres só até as 16h, "
                 "com o ônibus municipal de graça."),
    "busca": ("sao paulo sampa sp capital brasil masp pinacoteca museu da lingua portuguesa "
              "estacao da luz theatro municipal mercadao mercado municipal avenida paulista "
              "paulista aberta ibirapuera mam museu afro brasil museu do futebol pacaembu "
              "museu do ipiranga museu paulista beco do batman vila madalena metro cptm "
              "sptrans onibus gratis domingo guarulhos dia gratis"),
    "grupos": [
        {"id": "g1", "titulo": "O centro: a Luz, o Theatro e o Mercadão",
         "intro": ("Dois museus vizinhos na Luz com dias grátis diferentes, o teatro de 1911 "
                   "que se visita de graça com vaga liberada na véspera, e o mercado sem "
                   "horário oficial publicado.")},
        {"id": "g2", "titulo": "A Paulista e o Ibirapuera",
         "intro": ("O museu mais caro da lista, que é de graça na terça, a avenida que fecha "
                   "para carros aos domingos, e o parque com dois museus que não cobram no "
                   "mesmo dia.")},
        {"id": "g3", "titulo": "Fora do eixo, e a conta da cama",
         "intro": ("O futebol no Pacaembu, o museu que reabriu em 2022 no Ipiranga, o beco "
                   "em obra na Vila Madalena — e o transporte, com o ônibus grátis no "
                   "domingo, e a diária, que é mais barata nas férias.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - o centro
        # =============================================================
        {
            "id": "pinacoteca",
            "grupo": "g1",
            "nome": "Pinacoteca de São Paulo",
            "tag": "Museu",
            "preco_val": "R$ 40",
            "preco_nota": "grátis aos sábados; fecha às terças",
            "campos": [
                ("Valor da entrada",
                 "Fonte: páginas de ingresso e de visita do site oficial "
                 "(pinacoteca.org.br), consultadas em 15/nov/2026.<br>"
                 "<b>Inteira: R$ 40. Meia: R$ 20</b> — estudante, ID Jovem, aposentado, "
                 "professor de escola particular. On-line, <i>“Valor do ingresso + R$ 2,00 de "
                 "taxas”</i>.<br>"
                 "<b>Um ingresso vale para os três prédios no mesmo dia</b>: Pina Luz, Pina "
                 "Estação e Pina Contemporânea.<br>"
                 "<b>Não paga: maior de 60 anos</b>, criança até 10 anos, pessoa com deficiência "
                 "e acompanhante, professor da rede pública, guia de turismo, entre outros. "
                 "No MASP, o maior de 60 paga meia; aqui, não paga."),
                ("Quando é de graça",
                 "<i>“Pina Estação, Pina Luz, Pina Contemporânea têm entrada gratuita aos "
                 "sábados e segundos domingos do mês.”</i>"),
                ("Dias em que não funciona",
                 "<i>“De quarta a segunda, das 10h às 18h (entrada até 17h).”</i><br>"
                 "<b>Fecha às terças — e abre na segunda</b>, ao contrário de quase todo museu "
                 "da cidade. Quem monta “segunda é dia de museu fechado” perde a Pinacoteca de "
                 "graça; quem vai na terça, o dia mais gratuito de São Paulo, encontra a porta "
                 "fechada."),
                ("Onde fica",
                 "Pina Luz: Praça da Luz, 2. Do outro lado da praça fica o Museu da Língua "
                 "Portuguesa, na Estação da Luz.<br>" +
                 mapa("Pinacoteca de São Paulo, Praça da Luz 2, São Paulo, SP")),
            ],
        },
        {
            "id": "museu-da-lingua-portuguesa",
            "grupo": "g1",
            "nome": "Museu da Língua Portuguesa",
            "tag": "Museu",
            "preco_val": "R$ 25",
            "preco_nota": "grátis às terças e aos domingos",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de horários e ingressos do site oficial "
                 "(museudalinguaportuguesa.org.br), consultada em 15/nov/2026.<br>"
                 "<b>Inteira: R$ 25. Meia: R$ 12,50</b> — estudante, ID Jovem, aposentado, "
                 "maior de 60. Não paga: criança até 7 anos, professor, pessoa com deficiência e "
                 "acompanhante, guia com Cadastur, entre outros.<br>"
                 "<b>Comprando o Museu do Futebol pelo Sympla, este sai com 50% de desconto</b>, "
                 "<i>“Válida até 30 de dezembro de 2026”</i>."),
                ("Quando é de graça, e a regra que mudou",
                 "<i>“Grátis às terças-feiras e aos domingos.”</i><br>"
                 "<b>Mudou e o guia não acompanhou:</b> por anos o dia grátis foi o sábado, e "
                 "uma página antiga do próprio museu ainda mostra isso, com o preço velho de "
                 "R$ 20. <b>Hoje, sábado se paga.</b><br>"
                 "<i>“É obrigatória a emissão de ingressos, mesmo por quem tem direito à "
                 "gratuidade.”</i> O museu recomenda comprar antes, pelo Sympla."),
                ("Dias em que não funciona",
                 "<b>Fecha às segundas</b>, e em 24, 25 e 31/dez e 1º/jan. De terça a domingo, "
                 "<i>“Das 9h às 16h30 (permanência permitida até 18h)”</i>.<br>"
                 "O auditório e a Praça da Língua, no 3º andar, pedem senha no dia: <i>“a "
                 "compra de ingresso não garante automaticamente o acesso a esses "
                 "espaços”</i>."),
                ("Onde fica",
                 mapa("Museu da Língua Portuguesa, Estação da Luz, São Paulo, SP")),
            ],
        },
        {
            "id": "theatro-municipal",
            "foto": {"arq": "sao-paulo/theatro-municipal.webp",
                     "alt": "A fachada do Theatro Municipal de São Paulo iluminada ao anoitecer, com as estátuas no alto e prédios em volta",
                     "cred": "Wilfredor · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Theatro Municipal",
            "tag": "Teatro",
            "preco_val": "Grátis",
            "preco_nota": "visita guiada; a vaga sai na véspera, às 10h",
            "campos": [
                ("Valor, e a regra da véspera",
                 "Fonte: página de visitas educativas do site oficial "
                 "(theatromunicipal.org.br), consultada em 15/nov/2026.<br>"
                 "<b>A visita guiada é gratuita</b>, com ingresso pela plataforma INTI. Os "
                 "ingressos saem <i>“sempre no dia anterior à data da visita, a partir das "
                 "10h”</i>, sujeitos à vaga. <b>Quem decide no dia não entra no dia.</b>"),
                ("Os horários, e o fim de semana sem português",
                 "Em português: <b>terça às 10h, 11h e 17h; quarta a sexta às 11h, 13h, 15h e "
                 "17h</b>. Não há visita em feriados.<br>"
                 "<b>Sábado, domingo e segunda não têm visita em português.</b> A de sábado, às "
                 "11h, é em inglês, só para estrangeiros, com passaporte.<br>"
                 "Sem reserva, existe o <b>Theatro de Portas Abertas</b>, de terça a sábado: "
                 "concerto gratuito ao meio-dia no foyer. A página avisa que os horários "
                 "<i>“estão sujeitos a alterações”</i>."),
                ("O que não está publicado",
                 LACUNA + "a duração da visita e o ponto de encontro."),
                ("Onde fica",
                 "Praça Ramos de Azevedo, s/nº, no Anhangabaú.<br>" +
                 mapa("Theatro Municipal de São Paulo, Praça Ramos de Azevedo, São Paulo, SP")),
            ],
        },
        {
            "id": "mercadao",
            "grupo": "g1",
            "nome": "Mercado Municipal (Mercadão)",
            "tag": "Mercado",
            "preco_val": "Grátis",
            "preco_nota": "entrar; horário oficial não publicado",
            "campos": [
                ("Valor da entrada",
                 "Entrar não custa nada; paga-se o que se consome. A Prefeitura entregou a "
                 "restauração da fachada, dos pilares, do piso e do telhado em <b>20 de janeiro "
                 "de 2025</b>, e a administração é da concessionária Mercado SP SPE S.A. "
                 "Fonte: prefeitura.sp.gov.br, consultada em 15/nov/2026."),
                ("O horário que ninguém oficial publica",
                 LACUNA + "o site que aparece como “oficial” nas buscas "
                 "(mercadomunicipalsp.com) se declara <i>“sem vínculo com órgão público ou "
                 "privado”</i>, e o da concessionária não foi achado. <b>Não publicamos "
                 "horário que não conferimos.</b> Confirme antes de ir, principalmente no "
                 "domingo e nos feriados."),
                ("Onde fica",
                 "Rua da Cantareira, 306, no centro.<br>" +
                 mapa("Mercado Municipal Paulistano, Rua da Cantareira 306, São Paulo, SP")),
            ],
        },
        # =============================================================
        #  g2 - Paulista e Ibirapuera
        # =============================================================
        {
            "id": "masp",
            "foto": {"arq": "sao-paulo/masp.webp",
                     "alt": "O MASP na Avenida Paulista, a caixa de vidro suspensa entre os pilares vermelhos, com o vão livre embaixo",
                     "cred": "Wilfredor · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "MASP — Museu de Arte de São Paulo",
            "tag": "Museu",
            "preco_val": "R$ 85",
            "preco_nota": "grátis às terças e na sexta depois das 18h",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de visita do site oficial (masp.org.br), consultada em "
                 "15/nov/2026.<br>"
                 "<b>Inteira: R$ 85,00. Meia: R$ 42,00</b> — estudante, professor e maior de 60 "
                 "anos. Não paga: criança até 10 anos, pessoa com deficiência e acompanhante.<br>"
                 "<b>É o ingresso mais caro desta lista</b> — e o que mais tem horário "
                 "grátis."),
                ("Quando é de graça",
                 "<i>“TERÇA GRATUITA NUBANK: entrada gratuita para todos os visitantes, sem "
                 "necessidade de ser cliente Nubank.”</i><br>"
                 "<i>“SEXTA GRATUITA B3: Todas as sextas-feiras a partir das 18h.”</i><br>"
                 "<b>O agendamento on-line é obrigatório também nos dias grátis</b>: <i>“O "
                 "agendamento online, inclusive para os dias gratuitos, continua sendo "
                 "obrigatório.”</i> Não há reagendamento: cancela-se e compra-se de novo."),
                ("Dias em que não funciona",
                 "<b>Fecha às segundas</b>, e em 24, 25 e 31/dez e 1º/jan. Terça, 10h às 20h "
                 "(entrada até 19h); sexta, 10h às 21h (entrada até 20h); quarta, quinta, "
                 "sábado e domingo, 10h às 18h (entrada até 17h).<br>"
                 + FLAG % "Fontes divergem" +
                 "a própria página diz, num lugar, sexta grátis “das 18h às 20h”, e no outro "
                 "horário aberto até 21h com entrada até 20h."),
                ("Onde fica",
                 "Avenida Paulista, 1578, na Bela Vista. O vão livre embaixo do prédio é "
                 "público e não cobra nada.<br>" +
                 mapa("MASP, Avenida Paulista 1578, São Paulo, SP")),
            ],
        },
        {
            "id": "paulista-aberta",
            "grupo": "g2",
            "nome": "Avenida Paulista aberta",
            "tag": "Rua",
            "preco_val": "Grátis",
            "preco_nota": "domingos e feriados, das 9h às 16h",
            "campos": [
                ("Quando, e até que horas",
                 "Fonte: Subprefeitura Sé, página do programa Ruas Abertas "
                 "(prefeitura.sp.gov.br), consultada em 15/nov/2026.<br>"
                 "Aos <b>domingos e feriados</b>, a Paulista fica <i>“aberta exclusivamente para "
                 "pedestres, das 9h às 16h”</i>, da Praça do Ciclista à Praça Oswaldo Cruz.<br>"
                 "<b>Os guias falam em 17h, e notícia antiga da Prefeitura, em 19h.</b> O horário "
                 "publicado hoje acaba às 16h."),
                ("O domingo em que ela não abre",
                 "O programa é suspenso em dia de grande evento. Em 24/mai/2026, por exemplo: "
                 "<i>“Programa suspenso em virtude da realização do evento ‘Virada Cultural "
                 "2026’”</i>. Também houve suspensão no Carnaval e no 1º de maio, com o "
                 "programa seguindo só na Liberdade.<br>"
                 + LACUNA + "a programação de cada domingo; confira na semana."),
                ("Onde fica",
                 mapa("Avenida Paulista, São Paulo, SP")),
            ],
        },
        {
            "id": "ibirapuera",
            "foto": {"arq": "sao-paulo/ibirapuera.webp",
                     "alt": "Alameda arborizada do Parque Ibirapuera, com árvores altas dos dois lados",
                     "cred": "Wilfredor · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Parque Ibirapuera",
            "tag": "Parque",
            "preco_val": "Grátis",
            "preco_nota": "o parque; os museus dentro dele cobram",
            "campos": [
                ("Valor e horário",
                 "Entrada gratuita. A administração é da concessionária Urbia "
                 "(prefeitura.sp.gov.br, consultado em 15/nov/2026).<br>"
                 "<i>“O horário de funcionamento do Parque Ibirapuera é das 5h à 0h”</i> — "
                 + FLAG % "Fonte de 2022" +
                 "a frase é da Secretaria do Verde, numa página de agosto de 2022. Não achamos "
                 "confirmação de 2026."),
                ("Os museus dentro dele",
                 "O MAM e o Museu Afro Brasil ficam no parque e <b>não cobram no mesmo "
                 "dia</b>: o Afro Brasil é grátis na quarta, o MAM no domingo. <b>Os dois fecham "
                 "na segunda.</b> Cada um tem ficha própria abaixo.<br>"
                 + LACUNA + "a exposição em cartaz na Oca."),
                ("Onde fica",
                 mapa("Parque Ibirapuera, São Paulo, SP")),
            ],
        },
        {
            "id": "mam",
            "grupo": "g2",
            "nome": "MAM — Museu de Arte Moderna",
            "tag": "Museu",
            "preco_val": "R$ 40",
            "preco_nota": "+ taxa de R$ 1,20; grátis aos domingos",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de visita do site oficial (mam.org.br), consultada em "
                 "15/nov/2026.<br>"
                 "<i>“Ingresso integral: R$ 40,00 (quarenta reais) + taxa da Eventim de R$ "
                 "1,20.”</i> Meia: R$ 20 + R$ 0,60. Não paga: criança até 10 anos, pessoa com "
                 "deficiência e acompanhante."),
                ("Quando é de graça",
                 "<i>“Aos domingos, a entrada é gratuita para todos os públicos.”</i>"),
                ("Dias em que não funciona",
                 "<i>“Terça-feira a domingo, das 10h às 18h, com entrada até 17h30.”</i> "
                 "<b>Fecha às segundas.</b>"),
                ("Onde fica",
                 "Av. Pedro Álvares Cabral, s/nº, dentro do Ibirapuera, sob a marquise.<br>" +
                 mapa("MAM São Paulo, Parque Ibirapuera, São Paulo, SP")),
            ],
        },
        {
            "id": "museu-afro-brasil",
            "grupo": "g2",
            "nome": "Museu Afro Brasil Emanoel Araujo",
            "tag": "Museu",
            "preco_val": "R$ 15",
            "preco_nota": "grátis às quartas",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página “Planeje sua visita” do site oficial (museuafrobrasil.org.br), "
                 "consultada em 15/nov/2026.<br>"
                 "<b>Inteira: R$ 15. Meia: R$ 7,50</b> — estudante, maior de 60, aposentado, "
                 "ID Jovem. Pessoa com deficiência e acompanhante não pagam.<br>"
                 "<b>É o museu mais barato desta lista.</b>"),
                ("Quando é de graça",
                 "<i>“Grátis às quartas-feiras.”</i> Há guias que ainda dizem sábado; a "
                 "página oficial diz quarta."),
                ("Dias em que não funciona",
                 "<i>“3ª feira a domingo – das 10h às 17h (permanência até 18h).”</i> A segunda "
                 "não aparece entre os dias abertos."),
                ("Onde fica",
                 "Dentro do Ibirapuera, no Portão 10.<br>" +
                 mapa("Museu Afro Brasil, Parque Ibirapuera Portão 10, São Paulo, SP")),
            ],
        },
        # =============================================================
        #  g3 - fora do eixo, transporte e cama
        # =============================================================
        {
            "id": "museu-do-futebol",
            "grupo": "g3",
            "nome": "Museu do Futebol",
            "tag": "Museu",
            "preco_val": "R$ 25",
            "preco_nota": "grátis às terças",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de horários e ingressos do site oficial "
                 "(museudofutebol.org.br), consultada em 15/nov/2026.<br>"
                 "<b>Inteira: R$ 25. Meia: R$ 12,50.</b> <i>“Grátis para crianças até 7 "
                 "anos.”</i> Bilheteria aceita dinheiro, cartão e Pix; on-line, pelo Sympla. "
                 "Comprando aqui pelo Sympla, o Museu da Língua Portuguesa sai pela metade, até "
                 "30/dez/2026."),
                ("Quando é de graça, e a terça que vai até as 21h",
                 "<i>“Grátis para todos às terças-feiras.”</i><br>"
                 "<b>Na primeira terça de cada mês, o museu fica aberto das 9h às 21h</b>, com "
                 "entrada até 20h — é a única noite da semana, e cai no dia grátis."),
                ("Dias em que não funciona",
                 "<i>“De terça a domingo, das 9h às 18h (entrada permitida até as 17h).”</i> "
                 "<b>Fecha às segundas</b>, e em 24, 25 e 31/dez e 1º/jan."),
                ("Onde fica",
                 "Praça Charles Miller, s/nº, no Estádio do Pacaembu.<br>" +
                 mapa("Museu do Futebol, Praça Charles Miller, São Paulo, SP")),
            ],
        },
        {
            "id": "museu-do-ipiranga",
            "foto": {"arq": "sao-paulo/museu-do-ipiranga.webp",
                     "alt": "A fachada do Museu do Ipiranga sob céu azul, com o chafariz à direita",
                     "cred": "VictorAyabe · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Museu do Ipiranga",
            "tag": "Museu",
            "preco_val": "R$ 30",
            "preco_nota": "grátis às quartas, só na bilheteria e no dia",
            "campos": [
                ("Valor da entrada",
                 FLAG % "Plataforma de venda indicada pelo museu" +
                 "o site do museu não publica o valor em reais; a plataforma para onde ele "
                 "manda (Fever) dá <b>R$ 30 a inteira e R$ 15 a meia</b>, <i>“Sem taxas de "
                 "reserva”</i>, consultada em 15/nov/2026.<br>"
                 "Não paga sempre: criança até 6 anos, profissional da educação pública de SP, "
                 "guia credenciado, entre outros (museudoipiranga.org.br)."),
                ("O dia grátis que não se reserva",
                 "<i>“A entrada no Museu do Ipiranga é gratuita todas as quartas-feiras, no "
                 "primeiro domingo de cada mês”</i> e em datas avulsas.<br>"
                 "<i>“O ingresso deve ser retirado na bilheteria, no próprio dia da visita, sem "
                 "possibilidade de agendamento pelo site.”</i> <b>É o oposto do MASP</b>, onde "
                 "até o grátis exige agendamento. Os ingressos grátis saem a cada 15 minutos, "
                 "em número limitado."),
                ("Dias em que não funciona",
                 "<i>“Operamos de terça a domingo, das 10h às 17h, com última entrada às "
                 "16h.”</i> <b>Fecha às segundas</b> — mas <b>os jardins são grátis todos os "
                 "dias, das 5h às 20h</b>, inclusive segunda."),
                ("Onde fica",
                 "Rua dos Patriotas, 100, no Ipiranga.<br>" +
                 mapa("Museu do Ipiranga, Rua dos Patriotas 100, São Paulo, SP")),
            ],
        },
        {
            "id": "beco-do-batman",
            "grupo": "g3",
            "nome": "Beco do Batman",
            "tag": "Rua",
            "preco_val": "Grátis",
            "preco_nota": "rua pública; obra iniciada em maio de 2026",
            "campos": [
                ("Valor, e a obra",
                 "É rua pública, sem bilheteria, na Vila Madalena.<br>"
                 "A Prefeitura começou em maio de 2026 a requalificação do beco — drenagem, "
                 "jardins de chuva, calçadas acessíveis, bancos e um mirante —, e escreveu: "
                 "<i>“A previsão é de que as obras sejam concluídas em aproximadamente cinco "
                 "meses.”</i> (prefeitura.sp.gov.br, notícia de 21/05/2026, consultada em "
                 "15/nov/2026).<br>"
                 + LACUNA + "se a obra já foi entregue e se o beco ficou aberto durante "
                 "ela."),
                ("Como chegar no domingo sem pagar",
                 "A Secretaria de Turismo indica linhas de ônibus que passam perto — e "
                 "<b>no domingo o ônibus municipal não cobra</b> (ficha do transporte, "
                 "abaixo)."),
                ("Onde fica",
                 "Entre as ruas Gonçalo Afonso e Medeiros de Albuquerque, na Vila "
                 "Madalena.<br>" +
                 mapa("Beco do Batman, Vila Madalena, São Paulo, SP")),
            ],
        },
        {
            "id": "transporte",
            "grupo": "g3",
            "nome": "Metrô, ônibus e o aeroporto",
            "tag": "Transporte",
            "preco_val": "R$ 5,40",
            "preco_nota": "metrô e trem; o ônibus é grátis no domingo",
            "campos": [
                ("As tarifas de 2026",
                 "Desde <b>6 de janeiro de 2026</b>: <b>metrô e trem (CPTM), R$ 5,40</b> "
                 "(governo do estado e quadro de tarifas da CPTM); <b>ônibus municipal, "
                 "R$ 5,30</b>; integração ônibus e metrô, R$ 9,38 (SPTrans, Portaria SMT nº "
                 "005/2026). Consultados em 15/nov/2026.<br>"
                 "Para quem vai andar muito: <b>Bilhete 24 horas, R$ 20,50</b>; integrado com "
                 "ônibus, R$ 27,04 (quadro da CPTM)."),
                ("O domingo do ônibus grátis",
                 "SPTrans: <i>“Aos domingos, não há cobrança de tarifa nos ônibus da rede de "
                 "linhas noturnas e diurnas”</i>, das 0h às 23h59. <b>Metrô e trem continuam "
                 "cobrando</b> R$ 5,40 no domingo."),
                ("Do aeroporto de Guarulhos",
                 "<b>Trem: Linha 13-Jade da CPTM</b>, pela tarifa de R$ 5,40 do quadro "
                 "oficial. " + FLAG % "Sem tarifa própria publicada" +
                 "o Expresso Aeroporto não tem valor separado em página oficial de 2026; a "
                 "imprensa diz que é a mesma tarifa. A estação fica fora dos terminais.<br>"
                 "<b>Ônibus executivo da EMTU (Airport Bus Service): R$ 45,50</b> na página do "
                 "serviço — " + FLAG % "Fontes divergem" + "páginas de linha da própria EMTU "
                 "mostram valores maiores, como R$ 50,75. Confira a da sua linha.<br>"
                 "<b>Ônibus comum (linhas 257 e 299) até o Metrô Tatuapé: R$ 5,55</b>."),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem, e a taxa que não existe",
            "tag": "Conta, não lugar",
            "preco_val": "R$ 602",
            "preco_nota": "diária média de 2025, por quarto",
            "campos": [
                ("A diária, e de onde ela vem",
                 "Fonte: <b>FOHB e HotelInvest</b>, <i>Panorama da Hotelaria Brasileira</i>, "
                 "20ª edição, páginas 26 e 27, consultado em 15/nov/2026 — a mesma fonte das "
                 "fichas do Rio e de Salvador.<br>"
                 "<b>Diária média dos hotéis de São Paulo em 2025: R$ 602 por quarto</b>, com "
                 "62,6% de ocupação, em valores corrigidos para dez/2025. Fica perto da do "
                 "Rio (R$ 610) e bem acima da de Salvador (R$ 473), na mesma fonte.<br>"
                 "A série mensal vai de <b>R$ 508 em janeiro</b> a <b>R$ 706 em novembro</b>: "
                 "o relatório diz que os melhores meses ficam entre setembro e novembro, pelo "
                 "calendário de feiras e congressos. <b>Na capital paulista, o fim do ano e as "
                 "férias são os meses baratos</b> — o contrário das praias."),
                ("Por segmento, e o aluguel por temporada",
                 "No mesmo relatório: econômico <b>R$ 407</b>, midscale <b>R$ 609</b>, upscale "
                 "<b>R$ 906</b>. O aluguel por temporada tem diária média perto de <b>R$ 233</b>, "
                 "com 62% de ocupação.<br>"
                 + FLAG % "Ressalva" + "é a média dos hotéis do painel, da cidade inteira, sem "
                 "recorte por bairro."),
                ("A taxa que não existe",
                 "<b>Não achamos taxa turística na capital</b> — nem por hóspede, nem por "
                 "visitante. " + LACUNA + "ausência não se prova com documento; as taxas "
                 "de 2026 que aparecem no estado são de outras cidades, como Guarujá e Campos "
                 "do Jordão, e incidem sobre veículos."),
            ],
        },
    ],
}

DESTINOS = [SAO_PAULO]
