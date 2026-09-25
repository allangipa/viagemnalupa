# -*- coding: utf-8 -*-
"""Apuracao do Porto - SEGUNDA FATIA, os onze restantes.

Junta-se a primeira fatia (fatia1.py, cinco pontos centrais) e fecha o
destino em DEZESSEIS pontos. Importa a fatia1 POR CAMINHO, nao por
nome, pela mesma razao que o novos2/gera_roteiro.py: existem varios
dados.py em _build e o sys.modules devolve o errado.

ESTE arquivo chama-se dados.py porque e o nome que os geradores da casa
procuram - o novos/gera.py faz "from dados import DESTINOS" na pasta que
a variavel VNL_DADOS aponta. A fatia 1 mora ao lado, em fatia1.py, e
continua legivel sozinha.

    VNL_DADOS=porto python _build/novos/gera.py --aplica

OS ONZE
-------
    Ponte Dom Luis I          Sao Bento            Serralves
    Centro Historico/Ribeira  Capela das Almas     Casa da Musica
    Teleferico de Gaia        Se do Porto          Palacio de Cristal
    Caves do Vinho do Porto                        Mercado do Bolhao

SEIS COISAS QUE ESTA FATIA ACHOU, E QUE OS GUIAS CONTAM ERRADO
--------------------------------------------------------------

1. A PONTE DOM LUIS I NAO E DE GUSTAVE EIFFEL. E o erro mais repetido
   sobre o Porto em portugues do Brasil. A ficha do DGPC diz quem foi:
   o engenheiro frances Theophile Seyrig, pela casa belga Willebroeck.
   Seyrig FOI socio de Eiffel - na Ponte D. Maria, que e outra ponte,
   essa sim de Eiffel, construida oito anos antes. Confundir as duas e
   facil; publicar a confusao e que nao da.

2. OS AZULEJOS DA CAPELA DAS ALMAS SAO DE 1929, NAO DO SECULO XVIII.
   Eles imitam os do XVIII de proposito, e a ficha do DGPC diz isso com
   essas palavras. Sao de Eduardo Leite, feitos na Viuva Lamego, em
   Lisboa. E a mesma ficha registra que o autor MISTUROU Santa Catarina
   de Siena com Santa Catarina de Alexandria - a propria DGPC escreve
   "curiosamente".

3. O PALACIO DE CRISTAL NAO EXISTE. Foi demolido em 1951. Quem vai ao
   endereco procurando o palacio de ferro e vidro de 1865 encontra o
   Pavilhao Rosa Mota, que e outra coisa. O nome ficou nos jardins.

4. A SE PUBLICA UM PRECO SO, E NAO DIZ DO QUE. A fonte oficial (DRC
   Norte) publica "bilhete geral: 3 EUR" e nao discrimina nave,
   claustro, torre nem museu. Os agregadores dizem que a nave e
   gratuita e que os 3 EUR sao do claustro. NAO confirmamos isso.

5. AS CAVES DE GAIA QUASE NAO PUBLICAM PRECO. Taylor's publica horario,
   idiomas e os tres vinhos da degustacao, e NAO publica tarifa.
   Graham's tambem nao. Calem tem loja em botao de JavaScript. E o
   mesmo caso de Punta Cana, anotado no novos2/dados.py: nao e defeito
   da apuracao, e como o setor funciona.

6. OS COMBINADOS SAO A MELHOR CONTA DO PORTO, e agora da para provar:

       Clerigos + Serralves          27,20 EUR   contra 34,00  -6,80
       Casa da Musica + Serralves    28,80 EUR   contra 36,00  -7,20
       Clerigos + Bolsa + MMIPO      25,00 EUR   contra 24,00  +1,00 (e ganha o MMIPO)

   Os dois primeiros valem um quinto do preco. Nenhum guia soma isso.

Apuracao de 24 e 25 de setembro de 2026 - a virada de dia pegou
esta fatia no meio, e por isso as fontes daqui levam o intervalo
"24-25/set/2026" em vez de um dia so. A fatia 1 e toda de 24/set.
"""
import importlib.util
import os

AQUI = os.path.dirname(os.path.abspath(__file__))

_spec = importlib.util.spec_from_file_location(
    "porto_fatia1", os.path.join(AQUI, "fatia1.py"))
_d1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d1)

APURACAO = "24 e 25 de setembro de 2026"
APURACAO_CURTA = "24–25/set/2026"
mapa = _d1.mapa


# =====================================================================
#  GRUPOS DA SEGUNDA FATIA
# =====================================================================
GRUPOS2 = [
    {"id": "g4", "titulo": "O rio e as duas margens",
     "intro": ("O Douro separa Porto de Vila Nova de Gaia, e a travessia é "
               "metade do programa: a pé pela ponte, de cabine pelo teleférico "
               "ou parando nas caves do outro lado.")},
    {"id": "g5", "titulo": "Azulejo, que aqui é documento",
     "intro": ("Três fachadas e um átrio que valem por museu — e em dois deles a "
               "data que todo mundo repete está errada.")},
    {"id": "g6", "titulo": "Fora da baixa, e o mercado",
     "intro": ("Quatro paradas que pedem deslocamento, três delas ligadas por "
               "bilhete combinado que sai bem mais barato.")},
]


# =====================================================================
#  PONTOS DA SEGUNDA FATIA
# =====================================================================
PONTOS2 = [
    # -----------------------------------------------------------------
    {
        "id": "ponte-dom-luis", "grupo": "g4",
        "nome": "Ponte Dom Luís I", "tag": "Monumento",
        "preco_val": "Grátis",
        "preco_nota": "travessia a pé nos dois tabuleiros",
        "campos": [
            ("Não é de Gustave Eiffel — e a fonte oficial diz de quem é",
             "Fonte: ficha do Património Cultural / DGPC, "
             "<i>Ponte de D. Luís</i> (imovel.patrimoniocultural.gov.pt, ficha "
             "74503), consultada em 24–25/set/2026.<br>"
             "<b>O projeto é do engenheiro francês Théophile Seyrig "
             "(1844–1923)</b>, apresentado pela <b>Sociedade anónima de "
             "construção e oficinas de Willebroeck</b>, da Bélgica, que venceu o "
             "concurso aberto em <b>1880</b>.<br>"
             "<b>A confusão tem origem real:</b> Seyrig <b>foi sócio de Gustave "
             "Eiffel</b> — na <b>Ponte D. Maria</b>, essa sim projetada por "
             "Eiffel e construída entre <b>1876 e 1877</b> para a linha férrea "
             "do Norte. São duas pontes diferentes, sobre o mesmo rio, a oito "
             "anos de distância.<br>"
             "O anteprojeto do concurso foi do engenheiro <b>João Joaquim de "
             "Matos</b>, e foi ele que impôs a exigência que dá à ponte a cara "
             "que ela tem: <b>dois tabuleiros</b>, para ligar as partes "
             "ribeirinha e alta das duas cidades. A obra foi supervisionada por "
             "<b>Artur Maury</b>, pela Willebroeck, e fiscalizada pelo "
             "engenheiro português <b>José Macedo Araújo Júnior</b>."),
            ("As medidas, e a data de inauguração",
             "Mesma fonte, mesma data.<br>"
             "<b>Arco central de rótula, biarticulado, com vão de 180 metros.</b><br>"
             "<b>Tabuleiro superior: 391,25 metros</b> de extensão.<br>"
             "<b>Tabuleiro inferior: 174 metros.</b><br>"
             "<b>Ambos com 5 metros de largura.</b><br>"
             "<b>Inaugurada em maio de 1886.</b><br>"
             "O tabuleiro superior é hoje por onde passa o metro, e o inferior "
             "liga o Cais da Ribeira à zona das caves em Gaia — os dois têm "
             "passeio para pedestre, e é por isso que a travessia não custa nada."),
            ("O que havia antes, e por que a ponte foi feita",
             "Mesma fonte, mesma data. A Dom Luís I é a <b>terceira</b> travessia "
             "fixa nesse trecho do Douro:<br>"
             "<b>Ponte das Barcas</b>, inaugurada em <b>1806</b>.<br>"
             "<b>Ponte Pênsil</b>, aberta ao trânsito em <b>1843</b> — foi a "
             "<b>primeira ponte metálica lançada em território português</b>, e "
             "a DGPC atribui isso à atividade comercial da cidade e à "
             "comunidade britânica que aí residia de longa data.<br>"
             "A Dom Luís I foi a concurso justamente <b>para substituir a Ponte "
             "Pênsil</b>. Os dois pilares que sustentavam a pênsil ainda estão "
             "lá, e constam da própria ficha como elemento protegido."),
            ("A classificação, que tem duas camadas",
             "Mesma fonte, mesma data. E é mais sutil do que parece:<br>"
             "<b>Classificada como IIP — Imóvel de Interesse Público</b>, pelo "
             "<b>Decreto n.º 28/82, DR, I Série, n.º 47, de 26-02-1982</b>.<br>"
             "<b>Mas conta como Monumento Nacional</b>, porque está abrangida "
             "pelo conjunto inscrito na Lista do Património Mundial da UNESCO — "
             "e o <b>n.º 7 do artigo 15.º da Lei n.º 107/2001, de 8 de setembro</b>, "
             "equipara automaticamente a MN tudo o que esteja nessa situação.<br>"
             "Ou seja: o decreto diz IIP, a lei diz MN, e as duas coisas estão "
             "certas ao mesmo tempo."),
            ("Onde fica", mapa("Ponte Dom Luís I, Porto, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "centro-historico-ribeira", "grupo": "g4",
        "nome": "Centro Histórico e Ribeira", "tag": "Património Mundial",
        "preco_val": "Grátis",
        "preco_nota": "é a cidade; não há bilhete",
        "campos": [
            ("A data e o critério da UNESCO",
             "Fonte: ficha do Património Cultural / DGPC, <i>Centro Histórico do "
             "Porto, Ponte Luiz I e Mosteiro da Serra do Pilar</i> "
             "(imovel.patrimoniocultural.gov.pt, ficha 11871408), consultada em "
             "24–25/set/2026.<br>"
             "<b>Inscrito na Lista do Património Mundial em 5 de dezembro de "
             "1996</b>, na <b>20.ª sessão do Comité do Património Mundial</b>, "
             "reunida em <b>Mérida, no México</b>.<br>"
             "<b>Critério IV</b>, que a própria ficha transcreve: <i>&#8220;exemplo "
             "excecional de um tipo de construção ou de conjunto arquitetónico, "
             "tecnológico ou paisagístico que ilustra um, ou mais períodos "
             "significativos da história da humanidade&#8221;</i>.<br>"
             "<b>Classificado como MN — Monumento Nacional.</b> O "
             "<b>Aviso n.º 15173/2010, DR, 2.ª série, n.º 147, de 30-07-2010</b> "
             "tornou pública a inscrição e a equiparação a Monumento Nacional "
             "para todos os efeitos."),
            ("O nome mudou em 2016, e isso explica a grafia estranha",
             "Mesma fonte, mesma data.<br>"
             "<b>Até 2016 o bem chamava-se apenas &#8220;Centro Histórico do "
             "Porto&#8221;.</b> Na <b>40.ª sessão do Comité do Património "
             "Mundial, em julho e outubro de 2016</b>, a denominação passou a "
             "<b>&#8220;Centro Histórico do Porto, Ponte Luiz I e Mosteiro da "
             "Serra do Pilar&#8221;</b> — a ponte e o mosteiro entraram no nome.<br>"
             "<b>Repare no <i>Luiz</i>, com z.</b> A designação UNESCO grafa "
             "assim; a ficha da própria ponte, na mesma base de dados, grafa "
             "<b>&#8220;Ponte de D. Luís&#8221;</b>. As duas formas são oficiais, "
             "em documentos diferentes, e é por isso que o nome aparece escrito "
             "de dois jeitos por aí."),
            ("A zona de proteção, que foi a tribunal",
             "Mesma fonte, mesma data. Vale saber porque delimita onde as regras "
             "de obra apertam:<br>"
             "A zona tampão foi aprovada pela UNESCO na mesma 20.ª sessão, em "
             "dezembro de 1996, e equiparada a ZEP pelo Aviso n.º 15173/2010.<br>"
             "<b>Ficou sem efeito por sentença de 10-12-2010 do Tribunal "
             "Administrativo e Fiscal do Porto</b>, confirmada em 18-03-2011 pelo "
             "Tribunal Central Administrativo Norte, e de novo em 14-11-2012.<br>"
             "<b>A ZEP foi reposta pelo Aviso n.º 19137/2018, DR, 2.ª série, "
             "n.º 245, de 20-12-2018.</b>"),
            ("Onde fica", mapa("Cais da Ribeira, Porto, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "teleferico-de-gaia", "grupo": "g4",
        "nome": "Teleférico de Gaia", "tag": "Teleférico",
        "preco_val": "€ 10,00",
        "preco_nota": "ida e volta adulto; só ida € 7,00",
        "campos": [
            ("Valor do bilhete",
             "Fonte: página de preços e horários do site oficial "
             "(gaiacablecar.com), consultada em 24–25/set/2026. Valores com IVA "
             "incluído.<br>"
             "<b>Ida e volta:</b> adulto <b>€ 10,00</b>; criança de <b>5 a 12 "
             "anos</b>, <b>€ 5,00</b>.<br>"
             "<b>Só ida:</b> adulto <b>€ 7,00</b>; criança de 5 a 12 anos, "
             "<b>€ 3,50</b>.<br>"
             "<b>Família — 2 adultos + 2 crianças, ida e volta: € 22,50</b>. "
             "Comprado à parte, isso daria € 30,00, então a família economiza "
             "<b>€ 7,50</b>.<br>"
             "<b>Passe mensal:</b> adulto <b>€ 39,00</b>, criança <b>€ 19,50</b>, "
             "com direito a 4 viagens por dia.<br>"
             "<b>Todos os bilhetes valem 30 dias</b> a contar da compra — não é "
             "obrigatório usar no dia."),
            ("Horário, que muda cinco vezes no ano",
             "Mesma fonte, mesma data. O operador divide o ano em época baixa, "
             "média e alta:<br>"
             "<b>1 jan – 23 mar:</b> 10h–18h<br>"
             "<b>24 mar – 25 abr:</b> 10h–19h<br>"
             "<b>26 abr – 24 set:</b> 10h–20h — com uma exceção, "
             "<b>23 de junho: 10h–19h</b><br>"
             "<b>25 set – 24 out:</b> 10h–19h<br>"
             "<b>25 out – 31 dez:</b> 10h–18h<br>"
             "<b>Aberto todos os dias</b>, com um único fechamento no ano: "
             "<b>o dia de Natal</b>."),
            ("Quem opera, e onde se compra",
             "Mesma fonte, mesma data. O operador é a <b>Telef — Transportes por "
             "cabo e concessões S.A.</b>, com sede na <b>Calçada da Serra n.º 143, "
             "4430-236 Vila Nova de Gaia</b>, NIF 508237548.<br>"
             "Há venda de bilhete eletrónico no site e bilheteira no local."),
            ("Onde fica", mapa("Teleférico de Gaia, Calçada da Serra, Vila Nova de Gaia, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "caves-vinho-do-porto", "grupo": "g4",
        "nome": "Caves do Vinho do Porto", "tag": "Caves",
        "preco_val": None,
        "preco_nota": "as caves quase não publicam tarifa",
        "campos": [
            ("Por que não há um preço nesta linha",
             "<span class=\"flag\">Não existe tarifa única, e as próprias caves "
             "quase não publicam a delas</span> as caves de Vila Nova de Gaia são "
             "dezenas de operadores privados, cada um com o seu preço, e "
             "conferimos as três mais procuradas em 24–25/set/2026:<br>"
             "<b>Taylor's</b> (taylor.pt) — publica horário, os 13 idiomas do "
             "audioguia e até <b>quais</b> os três vinhos da degustação, e "
             "<b>não publica o preço</b>. A página remete para "
             "visit@taylor.pt e +351 223 772 973.<br>"
             "<b>Graham's</b> (grahams-port.com) — descreve a visita guiada com "
             "degustação e harmonização, e <b>não publica preço</b>. Telefone "
             "+351 220 930 417.<br>"
             "<b>Cálem</b> (tour.calem.pt) — tem as modalidades <i>Tour &amp; "
             "Taste</i> e <i>Tour, Taste &amp; Fado</i> descritas, e <b>a venda "
             "sai por um botão que não abre tabela</b>. Avenida Diogo Leite, 344; "
             "tour@calem.pt, +351 916 113 451.<br>"
             "<b>É o mesmo caso de Punta Cana</b>, já anotado neste site: onde o "
             "setor é de operador privado sem tarifa publicada, a ficha diz isso "
             "em vez de copiar número de agregador. <b>Confirme direto com a cave "
             "antes de ir.</b>"),
            ("O único valor oficial que conseguimos amarrar",
             "Fonte: página de visitas guiadas do site oficial da Casa da Música "
             "(casadamusica.com), consultada em 24–25/set/2026.<br>"
             "<b>Combinado Casa da Música + Caves Ferreira: € 27,20.</b><br>"
             "É o único número desta linha publicado por uma instituição em "
             "página própria. <b>Não dá para deduzir dele o preço da cave "
             "sozinha</b>, porque combinado é preço com desconto — e inventar "
             "essa subtração seria exatamente o que esta ficha não faz."),
            ("O que a Taylor's publica, e vale para planejar o dia",
             "Fonte: página das caves no site oficial da Taylor's (taylor.pt), "
             "consultada em 24–25/set/2026. Preço não, mas isto sim:<br>"
             "<b>Cave: 10h–18h15.</b> <b>Sala de degustação: 10h–19h30.</b> "
             "<b>Loja do Porto: 10h–14h e 15h–19h.</b> Todos os dias.<br>"
             "<b>Audioguia em 13 idiomas</b> — inglês, português, espanhol, "
             "francês, alemão, italiano, japonês, dinamarquês, mandarim, "
             "holandês, polaco, coreano e russo.<br>"
             "<b>A degustação inclui três vinhos nomeados:</b> Taylor's Chip Dry, "
             "Taylor's Late Bottled Vintage (LBV) e 10-Year-Old Tawny.<br>"
             "<span class=\"flag\">A duração não está publicada</span> a página "
             "oficial não informa quanto tempo leva a visita, e por isso não "
             "colocamos um número aqui."),
            ("Onde fica", mapa("Avenida de Diogo Leite, Vila Nova de Gaia, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "se-do-porto", "grupo": "g5",
        "nome": "Sé do Porto", "tag": "Catedral",
        "preco_val": "€ 3",
        "preco_nota": "bilhete geral",
        "campos": [
            ("Valor da entrada",
             "Fonte: ficha oficial da <b>Direção Regional de Cultura do Norte</b>, "
             "no portal do Governo (culturaportugal.gov.pt), consultada em "
             "24–25/set/2026.<br>"
             "<b>Bilhete geral: € 3.</b><br>"
             "<span class=\"flag\">A fonte oficial não diz do que é o bilhete</span> "
             "a ficha publica esse valor único e <b>não discrimina nave, "
             "claustro, torre nem museu</b>, nem informa descontos ou "
             "gratuidades. Agregadores de turismo afirmam que a entrada na nave é "
             "gratuita e que os € 3 valem para o claustro — <b>não confirmamos "
             "isso em fonte oficial</b>, e depois do que aconteceu com a Torre dos "
             "Clérigos nesta mesma apuração, não repetimos número de agregador."),
            ("Horário",
             "Mesma fonte, mesma data. Este a ficha publica com detalhe, "
             "inclusive o fecho antecipado da torre:<br>"
             "<b>Novembro a março: 9h–17h30</b>, e <b>a torre encerra às 17h</b>.<br>"
             "<b>Abril a outubro: 9h–18h30</b>, e <b>a torre encerra às 18h</b>.<br>"
             "<b>Segunda-feira a domingo.</b><br>"
             "Ou seja: quem quer subir a torre tem meia hora menos do que quem "
             "só entra."),
            ("Endereço e contactos",
             "<b>Terreiro da Sé, 4050-573 Porto.</b><br>"
             "Telefones <b>+351 222 059 028</b> e <b>+351 226 197 080</b> (DRC "
             "Norte). E-mail catedraldoporto@gmail.com e "
             "geral@culturanorte.gov.pt.<br>"
             "Fonte: ficha oficial da DRC Norte, 24–25/set/2026."),
            ("Onde fica", mapa("Sé do Porto, Terreiro da Sé, Porto, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "estacao-sao-bento", "grupo": "g5",
        "nome": "Estação de São Bento", "tag": "Estação e azulejo",
        "preco_val": "Grátis",
        "preco_nota": "é estação em funcionamento",
        "campos": [
            ("Os vinte mil azulejos, e quem os pintou",
             "Fonte: ficha do Património Cultural / DGPC "
             "(imovel.patrimoniocultural.gov.pt, ficha 72342), consultada em "
             "24–25/set/2026.<br>"
             "<b>O átrio principal tem cerca de vinte mil azulejos</b>, a branco "
             "e azul, executados pelo pintor <b>Jorge Colaço (1864–1942)</b>, "
             "formado nos meios académicos parisienses, onde foi discípulo do "
             "mestre Cormon.<br>"
             "<b>Colaço rodeou os painéis de um friso multicolor onde se historia "
             "a viação</b> — é o detalhe que quase ninguém repara, porque toda "
             "gente fotografa só os painéis grandes.<br>"
             "A ficha situa a obra na corrente <b>historicista e tardo-romântica</b> "
             "que atravessaria quase todo o século XX, com preferência por "
             "episódios e personalidades emblemáticos da história portuguesa."),
            ("O prédio: 1900, 1916, e o convento que havia antes",
             "Mesma fonte, mesma data.<br>"
             "<b>Projeto do arquiteto portuense José Marques da Silva "
             "(1869–1947)</b>, cujo curso em Paris explica, segundo a ficha, a "
             "influência da arquitetura da <i>École des Beaux-Arts</i> nas "
             "soluções do edifício. Por fora, linhas de fundo <b>neoclássico "
             "tardio</b>.<br>"
             "<b>D. Carlos I lançou a primeira pedra em 1900.</b><br>"
             "<b>Inaugurada em 1916</b>, depois da abertura da Ponte D. Maria "
             "Pia, com uma gare de <b>oito linhas terminais e cinco cais de "
             "embarque</b>.<br>"
             "<b>Antes ali havia um convento:</b> o das freiras beneditinas de "
             "<b>São Bento de Ave Maria</b>, erguido no século XVI, "
             "<b>destruído por um incêndio em 1783</b>, reconstruído no início do "
             "século seguinte e demolido já bastante degradado. O nome da estação "
             "vem dele."),
            ("Classificação",
             "Mesma fonte, mesma data. A designação oficial é longa de propósito, "
             "porque nomeia o que está protegido: <b>&#8220;Estação dos Caminhos "
             "de Ferro de São Bento, também denominada «Estação de São Bento», "
             "incluindo a gare metálica, os painéis de azulejos e a boca de "
             "entrada no túnel&#8221;</b>.<br>"
             "<b>Classificada como IIP — Imóvel de Interesse Público</b>, pelo "
             "<b>Decreto n.º 67/97, DR, I Série-B, n.º 301, de 31-12-1997</b>.<br>"
             "Endereço: <b>Praça de Almeida Garrett</b>, com acessos também pela "
             "Rua do Loureiro e Rua da Madeira."),
            ("Onde fica", mapa("Estação de São Bento, Praça de Almeida Garrett, Porto, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "capela-das-almas", "grupo": "g5",
        "nome": "Capela das Almas", "tag": "Capela e azulejo",
        "preco_val": None,
        "preco_nota": "sem tarifa publicada em fonte oficial",
        "campos": [
            ("Os azulejos são de 1929, e imitam o século XVIII de propósito",
             "Fonte: ficha do Património Cultural / DGPC, <i>Capela das Almas, "
             "também denominada «Capela de Santa Catarina»</i> "
             "(imovel.patrimoniocultural.gov.pt, ficha 74379), consultada em "
             "24–25/set/2026.<br>"
             "<b>Em 1929 as fachadas foram inteiramente revestidas a azulejos "
             "que imitam os do século XVIII.</b> A frase é da própria ficha. Não "
             "são setecentistas: são de 1929, feitos para parecer.<br>"
             "<b>Autoria do ceramista Eduardo Leite</b>, e <b>executados na "
             "fábrica &#8220;Viúva Lamego&#8221;, em Lisboa</b> — não no Porto.<br>"
             "Os painéis, azuis e brancos, representam passos das vidas de "
             "<b>Santa Catarina</b> e de <b>São Francisco de Assis</b>.<br>"
             "<b>E há um erro célebre dentro da obra.</b> A DGPC registra assim: "
             "<i>&#8220;curiosamente, o autor misturou cenas da vida de Santa "
             "Catarina de Siena com as da virgem e mártir, Santa Catarina de "
             "Alexandria&#8221;</i>. São duas santas diferentes, na mesma fachada."),
            ("A capela em si, que é bem mais antiga que a fachada",
             "Mesma fonte, mesma data.<br>"
             "<b>Construída em inícios do século XVIII</b>, e a ficha descreve o "
             "edifício como de <b>grande simplicidade</b> — o que faz sentido, "
             "porque o que impressiona hoje foi colado dois séculos depois.<br>"
             "<b>Em 1801 sofreu obras de ampliação e restauro que lhe "
             "modificaram o estilo original.</b><br>"
             "Sobre a porta há um <b>vitral representando as almas</b>, do "
             "terceiro quartel do século XIX, do pintor <b>Amândio Silva</b>. No "
             "tímpano, um brasão bipartido com os atributos de São Francisco e de "
             "Santa Catarina.<br>"
             "<b>O retábulo do altar-mor representa a Ascensão de Cristo</b> e é "
             "do pintor <b>Joaquim Rafael</b>. Altar-mor e altares da nave já têm "
             "características neoclássicas.<br>"
             "A torre sineira, de dois andares, ergue-se à esquerda, coberta por "
             "cúpula encimada por cruz de ferro."),
            ("Horário e entrada",
             "<span class=\"flag\">Não apuramos, e não há fonte oficial</span> a "
             "capela é um <b>templo em funcionamento</b>, não um museu, e "
             "<b>não encontramos site oficial da paróquia com horário ou "
             "tarifa</b> em 24–25/set/2026. A ficha da DGPC trata da classificação e "
             "da obra, não do funcionamento.<br>"
             "Os horários que circulam vêm todos de agregadores de turismo e "
             "<b>divergem entre si</b>. Por isso não publicamos nenhum. "
             "<b>Sendo igreja em uso, conte com fecho durante missa</b>, e "
             "confirme no local."),
            ("Classificação e endereço",
             "Fonte: ficha da DGPC, 24–25/set/2026.<br>"
             "<b>Classificada como IIP — Imóvel de Interesse Público</b>, pelo "
             "<b>Decreto n.º 45/93, DR, I Série-B, n.º 280, de 30-11-1993</b>.<br>"
             "<b>Rua de Santa Catarina, n.º 426–428, Porto.</b> Fica na rua de "
             "comércio mais movimentada da cidade, junto à estação de metro do "
             "Bolhão."),
            ("Onde fica", mapa("Capela das Almas, Rua de Santa Catarina 428, Porto, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "serralves", "grupo": "g6",
        "nome": "Serralves", "tag": "Museu e parque",
        "preco_val": "€ 24,00",
        "preco_nota": "bilhete geral; só parque € 15,00",
        "campos": [
            ("Valor da entrada",
             "Fonte: bilheteira oficial da Fundação de Serralves "
             "(serralves.byblueticket.pt), consultada em 24–25/set/2026.<br>"
             "<b>Bilhete Geral: € 24,00</b>, e <b>€ 20,00 para residentes</b>.<br>"
             "<b>Inclui acesso a todos os espaços da fundação:</b> Museu de Arte "
             "Contemporânea, Parque de Serralves, <b>Treetop Walk</b>, Casa de "
             "Serralves e Casa do Cinema Manoel de Oliveira.<br>"
             "<b>Bilhete Só Parque: € 15,00</b>, e <b>€ 12,00 para residentes</b> "
             "— dá o parque e o TreeTop Walk, sem os museus.<br>"
             "<b>Os dois valem até 30 dias após a data de emissão</b>, e são de "
             "<b>utilização única</b>: não se entra duas vezes com o mesmo "
             "bilhete."),
            ("Descontos e gratuidades",
             "Mesma fonte, mesma data.<br>"
             "<b>Não pagam:</b> <b>crianças até aos 11 anos</b>, Amigos de "
             "Serralves e portadores de Cartão BPI. O bilhete tem de ser "
             "levantado na Receção, com o comprovativo.<br>"
             "<b>Têm desconto:</b> jovem de <b>12 a 17 anos</b>, estudante "
             "<b>até 25 anos e até ao grau de mestrado</b>, e sénior "
             "<b>com mais de 65</b>. No dia da visita é preciso apresentar "
             "documento de identificação e comprovativo à entrada.<br>"
             "<span class=\"flag\">Os valores com desconto não estão publicados</span> "
             "a bilheteira informa que eles <b>só aparecem no momento de "
             "finalização da encomenda online</b>. Não há tabela pública, e por "
             "isso não damos os números aqui.<br>"
             "<b>Venda exclusiva na Receção</b>, sem compra online: Serralves em "
             "Família, Serralves em Grupo e Serralves ao Fim da Tarde."),
            ("O parque, que é metade do motivo de ir",
             "Mesma fonte, mesma data.<br>"
             "<b>O Parque de Serralves tem 18 hectares</b>, com jardins formais, "
             "matas e uma quinta tradicional.<br>"
             "<b>Os jardins são projeto de Jacques Gréber, dos anos 30 do século "
             "XX</b>, e a bilheteira oficial chama-lhes &#8220;referência única "
             "no património paisagístico português&#8221;.<br>"
             "O parque funciona também como espaço museográfico, com esculturas "
             "da Coleção da Fundação em exposição permanente, e o <b>TreeTop "
             "Walk</b> é um passadiço ao nível da copa das árvores."),
            ("Os dois combinados, e quanto poupam de verdade",
             "Fontes: bilheteira dos Clérigos (torredosclerigos.pt) e página de "
             "visitas guiadas da Casa da Música (casadamusica.com), as duas "
             "consultadas em 24–25/set/2026.<br>"
             "<b>Clérigos + Serralves: € 27,20.</b> À parte dariam 10,00 + 24,00 "
             "= <b>€ 34,00</b>. Poupa <b>€ 6,80</b>.<br>"
             "<b>Casa da Música + Serralves: € 28,80.</b> À parte dariam 12,00 + "
             "24,00 = <b>€ 36,00</b>. Poupa <b>€ 7,20</b>.<br>"
             "<b>São os dois melhores descontos que achamos no Porto</b> — cerca "
             "de um quinto do preço, em qualquer dos dois. E nenhum dos dois "
             "aparece somado nos guias."),
            ("Onde fica", mapa("Fundação de Serralves, Rua Dom João de Castro, Porto, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "casa-da-musica", "grupo": "g6",
        "nome": "Casa da Música", "tag": "Sala de concertos",
        "preco_val": "€ 12",
        "preco_nota": "visita guiada; € 9 com Porto Card",
        "campos": [
            ("Valor da visita guiada",
             "Fonte: página de visitas guiadas do site oficial "
             "(casadamusica.com), consultada em 24–25/set/2026.<br>"
             "<b>Bilhete normal: € 12</b><br>"
             "<b>Jovem de 13 a 18 anos: € 5</b><br>"
             "<b>Menores de 12 anos: gratuito</b>, desde que acompanhados por um "
             "adulto pagante<br>"
             "<b>Porto Card: € 9</b><br>"
             "<b>Combinados:</b> Casa da Música + Fundação de Serralves "
             "<b>€ 28,80</b>; Casa da Música + Caves Ferreira <b>€ 27,20</b>."),
            ("Horário, idiomas e lotação",
             "Mesma fonte, mesma data.<br>"
             "<b>Visitas diárias às 11h e às 15h</b>, em <b>português, espanhol, "
             "francês e italiano</b>. <b>Inglês sujeito a disponibilidade.</b><br>"
             "<b>Duração aproximada de uma hora.</b><br>"
             "<b>Lotação máxima de 35 pessoas por visita</b> — é o número que "
             "importa em dia cheio, porque a visita fecha e a seguinte é três "
             "ou quatro horas depois.<br>"
             "<b>Grupos escolares e grupos de 15 pessoas ou mais</b> podem "
             "combinar visitas personalizadas, por contacto prévio."),
            ("Duas coisas que podem estragar o dia",
             "Mesma fonte, mesma data.<br>"
             "<b>O acesso aos espaços depende da programação do dia.</b> A Casa "
             "da Música é uma sala de concertos em funcionamento: se houver "
             "ensaio ou espetáculo, parte do edifício fica fora da visita. "
             "<b>Confirme na bilheteira quais os espaços disponíveis</b> antes de "
             "comprar.<br>"
             "<span class=\"flag\">Fontes divergem sobre onde se compra</span> a "
             "página oficial indica compra <b>na bilheteira, online ou por "
             "telefone</b> (220 120 210 / 220 120 233). Outras páginas afirmam "
             "que o bilhete <b>só pode ser adquirido no próprio dia, "
             "presencialmente, nas bilheteiras do piso 1</b>. <b>Não conseguimos "
             "fechar qual das duas vale</b> — se o seu roteiro depende de ter "
             "lugar garantido, ligue antes."),
            ("Onde fica", mapa("Casa da Música, Avenida da Boavista 604, Porto, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "jardins-palacio-cristal", "grupo": "g6",
        "nome": "Jardins do Palácio de Cristal", "tag": "Jardim",
        "preco_val": "Grátis",
        "preco_nota": "acesso livre, por condição de venda ao município",
        "campos": [
            ("O Palácio de Cristal não existe mais",
             "Fonte: página oficial do município, no portal do Ambiente da Câmara "
             "Municipal do Porto (ambiente.cm-porto.pt), consultada em "
             "24–25/set/2026.<br>"
             "<b>O palácio foi demolido em 1951.</b> Quem chega ao endereço "
             "procurando o edifício de ferro e vidro encontra o <b>Pavilhão Rosa "
             "Mota</b>, que é outra construção. <b>O nome ficou nos jardins.</b><br>"
             "O original abriu em <b>1865</b>, projeto de <b>Thomas Dillens "
             "Jones</b>, com os jardins românticos desenhados por <b>Émil "
             "David</b>. A página municipal descreve-o como o "
             "<i>&#8220;imponente Palácio construído em ferro e vidro com 70 "
             "metros de largura por 150 metros de comprimento&#8221;</i>.<br>"
             "<b>A cidade adquiriu a propriedade em 1933</b> e demoliu o palácio "
             "em 1951.<br>"
             "Antes de tudo isso, o lugar chamava-se <b>Campo da Torre da Marca</b>, "
             "nome registrado em <b>1542</b>, e em <b>1854</b> ali se construiu a "
             "capela do Rei Carlos Alberto."),
            ("Entrada e horário",
             "Mesma fonte, mesma data.<br>"
             "<b>Acesso gratuito</b> — e não por simpatia: a página municipal "
             "registra que <b>a propriedade foi vendida à Câmara com a condição "
             "de se tornar espaço verde público</b>, de jardins e pequena mata, "
             "de acesso livre.<br>"
             "<b>Abril a setembro: 8h–21h</b><br>"
             "<b>Outubro a março: 8h–19h</b><br>"
             "Endereço: <b>Rua de D. Manuel II</b>."),
            ("O que há dentro",
             "Mesma fonte, mesma data. Jardins formais e informais, em estilo de "
             "mata, com <b>vários miradouros sobre o Douro</b> — é um dos "
             "melhores pontos de vista gratuitos da cidade.<br>"
             "Há esculturas, fontes, <b>camélias por todo o terreno</b>, "
             "incluindo um <b>Bosque das Camélias</b> dedicado, e uma "
             "<b>biblioteca pública com galeria de exposições de entrada "
             "gratuita</b>.<br>"
             "<span class=\"flag\">A área não está publicada</span> a página "
             "municipal não informa quantos hectares tem o jardim, e por isso não "
             "damos o número."),
            ("Onde fica", mapa("Jardins do Palácio de Cristal, Rua de Dom Manuel II, Porto, Portugal")),
        ],
    },
    # -----------------------------------------------------------------
    {
        "id": "mercado-do-bolhao", "grupo": "g6",
        "nome": "Mercado do Bolhão", "tag": "Mercado",
        "preco_val": None,
        "preco_nota": "o site oficial não publica tarifa de entrada",
        "campos": [
            ("Horário, que é diferente para o mercado e para a comida",
             "Fonte: site oficial do Mercado do Bolhão (mercadobolhao.pt), "
             "consultado em 24–25/set/2026. São dois horários, e confundi-los é "
             "chegar e achar fechado:<br>"
             "<b>Mercado:</b> segunda a sexta <b>8h–20h</b>; sábado "
             "<b>8h–18h</b>; <b>domingo fechado</b>.<br>"
             "<b>Restauração:</b> segunda a sábado <b>8h–24h</b>; "
             "<b>domingo fechado</b>.<br>"
             "<b>Fecha domingo nos dois casos</b> — é a informação mais útil "
             "desta linha, porque muito roteiro de fim de semana põe o Bolhão no "
             "domingo de manhã."),
            ("Entrada",
             "<span class=\"flag\">O site oficial não publica tarifa de "
             "entrada</span> conferido em 24–25/set/2026: o site do mercado divulga "
             "horários, bancas e serviços, e <b>não menciona bilhete nem preço de "
             "acesso</b>.<br>"
             "<b>É um mercado municipal em funcionamento</b>, com bancas de "
             "comércio, não um museu. Mas como a fonte oficial não escreve "
             "&#8220;entrada gratuita&#8221;, <b>não afirmamos aqui que é</b> — a "
             "regra desta casa vale igual para número alto e para número zero."),
            ("Onde fica",
             "O site oficial indica o mercado pelo mapa e menciona a <b>Rua "
             "Formosa</b> a propósito do balcão de informações. "
             "<span class=\"flag\">Não publica o endereço em texto</span><br>"
             + mapa("Mercado do Bolhão, Rua Formosa, Porto, Portugal")),
        ],
    },
]


# =====================================================================
#  O DESTINO COMPLETO: fatia 1 + fatia 2
# =====================================================================
PORTO = dict(_d1.PORTO)
PORTO["grupos"] = list(_d1.PORTO["grupos"]) + GRUPOS2
PORTO["pontos"] = list(_d1.PORTO["pontos"]) + PONTOS2

# Titulo, descricao e abertura falavam de cinco pontos. Agora sao 16.
PORTO["titulo"] = "Porto: 16 pontos com preço e horário verificados"
PORTO["descricao"] = (
    "Preço, horário e fonte oficial de 16 pontos do Porto — com a entrada da "
    "Livraria Lello que volta como crédito em livro, os dois combinados que "
    "poupam um quinto do valor e o engenheiro que de fato assina a Ponte Dom "
    "Luís I.")
PORTO["abertura"] = (
    "Dezesseis pontos com preço, horário e fonte oficial — e o que os guias "
    "contam errado: <b>a Ponte Dom Luís I não é de Eiffel, e os azulejos da "
    "Capela das Almas são de 1929, não do século XVIII</b>.")

DESTINOS = [PORTO]
