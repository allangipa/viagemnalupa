# -*- coding: utf-8 -*-
"""Paris: onze pontos, com fonte e data em cada numero.

Mesmo molde do roma/dados.py. O renderizador e o novos/gera.py, chamado
com VNL_DADOS=paris.

POR QUE PARIS, E POR QUE AGORA
------------------------------
Primeira da fila que a home publica no bloco "Roteiro de publicacao".

O ACHADO: PARIS PASSOU A COBRAR MAIS DE QUEM NAO E EUROPEU - E CADA
LUGAR FAZ ISSO DE UM JEITO DIFERENTE
--------------------------------------------------------------------
Cinco regras distintas, na mesma cidade, para a mesma pessoa:

  Louvre            preco por passaporte: 22 euros para o Espaco
                    Economico Europeu, 32 EUROS PARA O RESTO DO MUNDO,
                    desde 14 de janeiro de 2026. E 45% a mais.

  Versalhes         tambem separa, mas por 3 euros: 35 normal, 32 para
                    a Franca e o EEE.

  Monumentos        Arco do Triunfo, Sainte-Chapelle e as torres de
  nacionais         Notre-Dame anunciam "gratuito para menores de 26
                    anos". A gratuidade de 18 a 25 e para quem RESIDE
                    no EEE. Brasileiro de vinte anos paga inteira.

  Torre Eiffel      nao separa por nacionalidade nenhuma. A tarifa
                    jovem e de 12 a 24 anos, por idade.

  Catacumbas        da cidade de Paris, nao do Estado: tarifa reduzida
                    de 18 a 26 anos, tambem por idade.

O contraste que resume a cidade: um brasileiro de 20 anos paga METADE
na Torre Eiffel e INTEIRA no Arco do Triunfo, a tres quilometros dali.

E o espelho invertido de Madri, onde o passaporte brasileiro DA direito
a entrada gratuita no Palacio Real. Aqui ele tira.

O QUE MAIS ESTA APURACAO ACHOU
------------------------------

1. O CENTRE POMPIDOU ESTA FECHADO ATE 2030. Fechou em 22 de setembro de
   2025; a obra comeca em abril de 2026. Continua em praticamente todo
   guia de Paris. A colecao esta espalhada por outros museus, no
   programa Constellation.

2. O LOUVRE NAO E MAIS GRATIS NO PRIMEIRO DOMINGO. Passou a ser a
   PRIMEIRA SEXTA do mes, depois das 18h - e nao vale em julho e agosto.
   O Orsay, ao lado, continua no primeiro DOMINGO. Dois museus de porte
   parecido, dois dias diferentes, e nenhum guia separa.

3. O ELEVADOR DO ARCO DO TRIUNFO ESTA EM MANUTENCAO por tempo
   indeterminado. So se sobe a pe.

4. NOTRE-DAME CONTINUA GRATUITA. Houve proposta de cobrar de
   estrangeiros e ela foi descartada. A reserva e gratuita e
   facultativa; sem ela, a espera chega a duas ou tres horas.

5. OS JARDINS DE VERSALHES SAO PAGOS NA ALTA TEMPORADA (1 de abril a 31
   de outubro) e gratuitos de 1 de novembro a 31 de marco.

6. AS CATACUMBAS CUSTAM 31 EUROS, audioguia incluido - mais caro que o
   Louvre para quem e europeu.

O QUE ESTA APURACAO NAO TEM, E FICA ESCRITO
-------------------------------------------
TRES FONTES OFICIAIS RECUSARAM LEITURA:

  notredamedeparis.fr        403 ao cliente HTTP
  toureiffel.paris           403 ao cliente HTTP; ABRIU no navegador, e
                             e de la que vem a tabela de precos
  musee-orsay.fr             "Acces refuse" na pagina de tarifas, tanto
                             por URL direta quanto clicando o link a
                             partir da home

Nao contornamos bloqueio. O PRECO DO ORSAY NAO ESTA NESTA FICHA: a
bilheteria oficial so revela valor depois de escolher data, e a pagina
de tarifas nega acesso. O que o proprio site publica em faixa - o
primeiro domingo gratuito e a obra ate 2028 - esta aqui.

A TAXA DE ESTADIA veio SO DE FONTES SECUNDARIAS CONVERGENTES. A pagina
da prefeitura deu 404 e a tabela oficial da DGFiP e um arquivo de dados
para download, nao uma pagina citavel. A ficha diz isso na linha.

Tambem nao apuramos: preco do domo do Sacre-Coeur, tarifa de metro,
diaria media de hospedagem, nem o Paris Museum Pass.

Apuracao de 30 de setembro de 2026.
"""

APURACAO = "30 de setembro de 2026"
APURACAO_CURTA = "30/set/2026"

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
#  PARIS
# =====================================================================
PARIS = {
    "slug": "paris",
    "nome": "Paris",
    "pais": "França",
    "regiao": "europa",
    "titulo": "Paris: 11 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 11 pontos de Paris, com o Louvre que "
                  "cobra € 32 de quem não é europeu desde janeiro de 2026."),
    "abertura": ("Onze pontos com preço em euro, horário e fonte conferidos em 30 de "
                 "setembro de 2026 — e a mudança que ainda não chegou aos guias: "
                 "<b>Paris começou a cobrar mais de quem não é europeu, e cada lugar "
                 "faz isso de um jeito diferente. No Louvre o seu passaporte custa "
                 "€ 10 a mais; na Torre Eiffel, a três quilômetros dali, ele não muda "
                 "nada.</b>"),
    "busca": ("paris frança france europa louvre museu do louvre musee du louvre orsay "
              "musee d orsay torre eiffel tour eiffel notre dame catedral sainte chapelle "
              "arco do triunfo arc de triomphe sacre coeur montmartre catacumbas "
              "catacombes versalhes versailles chateau de versailles trianon centre "
              "pompidou beaubourg fechado taxa de estadia taxe de sejour espaco economico "
              "europeu eee tarifa estrangeiro primeira sexta primeiro domingo gratuito"),
    "grupos": [
        {"id": "g1", "titulo": "Onde o seu passaporte muda o preço",
         "intro": ("Os três grandes museus e palácios, e a conta que passou a depender "
                   "de onde você mora — em cada um de um jeito.")},
        {"id": "g2", "titulo": "O que não cobra, e o que cobra de você",
         "intro": ("Quatro lugares onde a entrada é livre ou barata — e onde a frase "
                   "“gratuito para menores de 26 anos” quer dizer outra coisa.")},
        {"id": "g3", "titulo": "O alto, o fundo, o que fechou e a conta da cama",
         "intro": ("A torre e as catacumbas, o museu que sumiu do mapa até 2030, e a "
                   "cobrança que não aparece no preço da reserva.")},
    ],
    "pontos": [

        # ---------------------------------------------------------- g1
        {
            "id": "louvre",
            "grupo": "g1",
            "nome": "Museu do Louvre",
            "tag": "Museu",
            "preco_val": "€ 32",
            "preco_nota": "quem não é do EEE; europeu paga € 22",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (louvre.fr), consultado em 30/set/2026.<br>"
                 "<b>O Louvre tem dois preços, e a diferença é o seu passaporte.</b><br>"
                 "<b>€ 22</b> para cidadãos <b>ou</b> residentes do Espaço Econômico "
                 "Europeu — os 27 da União Europeia mais Islândia, Liechtenstein e "
                 "Noruega.<br>"
                 "<b>€ 32 para todos os outros</b>, o que inclui o Brasil. "
                 "<b>São € 10 a mais, ou 45%.</b><br>"
                 "A cobrança separada <b>começou em 14 de janeiro de 2026</b>, e o museu "
                 "anunciou que espera arrecadar de 15 a 20 milhões de euros por ano com "
                 "ela.<br>"
                 "<b>Não paga:</b> menor de 18 anos, <b>de qualquer nacionalidade</b>, "
                 "mediante documento com foto. E <b>menor de 26 anos que seja cidadão ou "
                 "residente do EEE</b> — residente precisa de título de permanência de "
                 "mais de 90 dias, com nome e foto.<br>"
                 "<b>Grupo guiado de fora do EEE paga € 28 por pessoa</b>, em grupos de "
                 "até 20."),
                ("Quando é de graça",
                 "<b>Primeira sexta-feira do mês, depois das 18h, para todo mundo — "
                 "exceto em julho e agosto.</b><br>"
                 + FLAG % "Mudou e o guia não acompanhou" +
                 "por anos o Louvre foi gratuito no <b>primeiro domingo</b>, de outubro a "
                 "março. <b>Não é mais.</b> O Musée d’Orsay, do outro lado do rio, "
                 "continua no primeiro domingo — os dois museus têm dias diferentes, e "
                 "quem confia num roteiro velho perde os dois.<br>"
                 "O museu recomenda <b>reservar horário mesmo para entrada gratuita</b>."),
                ("Dias em que não funciona",
                 "<b>Fecha às terças.</b><br>"
                 "<b>Segunda, quinta, sábado e domingo: 9h às 18h.</b><br>"
                 "<b>Quarta e sexta: 9h às 21h.</b><br>"
                 "<b>Última entrada uma hora antes de fechar</b>, e as salas começam a ser "
                 "esvaziadas 30 minutos antes.<br>"
                 "<b>Fecha em 1º de janeiro, 1º de maio e 25 de dezembro.</b> Nos demais "
                 "feriados abre, a não ser que caiam numa terça."),
                ("Cuidado com bilhete falso",
                 "O próprio museu publica um alerta sobre <b>sites espelho</b> que se "
                 "passam por oficiais e sobre venda de rua. <b>Bilhete comprado assim "
                 "pode ter a entrada recusada.</b> A bilheteria oficial é o louvre.fr."),
                ("Onde fica", mapa("Musée du Louvre, Rue de Rivoli, 75001 Paris, França")),
            ],
        },
        {
            "id": "versalhes",
            "grupo": "g1",
            "nome": "Palácio de Versalhes",
            "tag": "Palácio e jardins",
            "preco_val": "€ 35",
            "preco_nota": "Passaporte, alta temporada; europeu paga € 32",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página “Tarification 2026” do site oficial "
                 "(chateauversailles.fr), consultada em 30/set/2026.<br>"
                 "<b>Versalhes também separa europeu de não europeu — mas por € 3, não "
                 "por € 10 como o Louvre.</b> A redução vale para cidadãos do EEE "
                 "<b>qualquer que seja a residência</b>, e para residentes <b>qualquer "
                 "que seja a nacionalidade</b>.<br>"
                 "<b>O bilhete Passaporte é o único que entra no palácio</b>, com horário "
                 "marcado, e dá acesso ao domínio inteiro:<br>"
                 "<b>Alta temporada (1º/abr a 31/out): € 35, ou € 32 para França e EEE.</b><br>"
                 "<b>Baixa temporada (1º/nov a 31/mar): € 25, ou € 22 para França e EEE.</b><br>"
                 "<b>Há um Passaporte de fim de dia</b>, com entrada no palácio a partir "
                 "das 16h na alta e das 15h na baixa: <b>€ 28 (€ 25 EEE) na alta</b> e "
                 "<b>€ 18 (€ 15 EEE) na baixa</b>.<br>"
                 "<b>Só o domínio de Trianon</b> — Grande Trianon, Pequeno Trianon e a "
                 "Aldeia da Rainha — custa <b>€ 15, ou € 12 para França e EEE</b>, o ano "
                 "inteiro."),
                ("O jardim é pago, e depende do mês",
                 "<b>De 1º de abril a 31 de outubro o acesso aos Jardins de Versalhes é "
                 "pago.</b><br>"
                 "<b>De 1º de novembro a 31 de março é gratuito para todos.</b><br>"
                 "É a inversão do que a maioria imagina: o jardim custa justamente na "
                 "época em que ele está bonito."),
                ("Onde fica",
                 mapa("Château de Versailles, Place d'Armes, 78000 Versailles, França")),
            ],
        },
        {
            "id": "orsay",
            "grupo": "g1",
            "nome": "Musée d’Orsay",
            "tag": "Museu",
            "preco_val": "Não encontrado",
            "preco_nota": "fonte oficial recusou leitura",
            "campos": [
                ("Valor da entrada",
                 FLAG % "Fonte oficial não aberta" +
                 "<b>não publicamos o preço do Orsay porque não conseguimos lê-lo em "
                 "fonte oficial.</b><br>"
                 "A página de tarifas do musee-orsay.fr responde <b>“Accès refusé”</b> — "
                 "tanto por endereço direto quanto clicando o link a partir da página "
                 "inicial. A bilheteria oficial (billetterie.musee-orsay.fr) abre, mas "
                 "<b>só mostra valor depois de escolher data</b>.<br>"
                 "<b>Não contornamos bloqueio, e não copiamos o número de terceiros.</b> "
                 "Preferimos a lacuna escrita ao número sem fonte.<br>"
                 "O que o próprio site publica em faixa, e está conferido, vem abaixo."),
                ("Quando é de graça",
                 "<b>Primeiro domingo do mês, entrada gratuita para todos</b> — mas "
                 "<b>a reserva de um bilhete gratuito é obrigatória</b>, para a coleção "
                 "ou para as exposições.<br>"
                 "O site nomeava o próximo na data da consulta: <b>domingo, 4 de "
                 "outubro</b>.<br>"
                 "<b>É o oposto do Louvre</b>, que mudou para a primeira sexta à noite. "
                 "Os dois ficam a dez minutos um do outro, a pé pela ponte."),
                ("Obra em andamento",
                 "<b>De 10 de março de 2026 até o verão europeu de 2028, o Orsay está "
                 "reformando as áreas de recepção.</b> O próprio museu pede que se "
                 "confiram as condições de acesso antes de ir.<br>"
                 "Fonte: faixa de aviso do site oficial, 30/set/2026."),
                ("Onde fica",
                 mapa("Musée d'Orsay, Esplanade Valéry Giscard d'Estaing, 75007 Paris, França")),
            ],
        },

        # ---------------------------------------------------------- g2
        {
            "id": "notre-dame",
            "grupo": "g2",
            "nome": "Catedral de Notre-Dame",
            "tag": "Catedral",
            "preco_val": "Grátis",
            "preco_nota": "torres à parte, € 16",
            "campos": [
                ("Valor da entrada",
                 "<b>Entrar na catedral não se paga, para ninguém.</b><br>"
                 "Houve <b>proposta de cobrar de visitantes estrangeiros</b> e ela foi "
                 "<b>descartada</b>: a catedral segue gratuita.<br>"
                 "<b>A reserva é gratuita e facultativa</b>, pelo site oficial. Sem "
                 "reserva entra-se do mesmo jeito, mas <b>a espera chega a duas ou três "
                 "horas na alta temporada</b> — a catedral recebe cerca de 35 mil pessoas "
                 "por dia.<br>"
                 "<b>Nenhum terceiro está autorizado a vender ingresso de entrada.</b> "
                 "Quem estiver cobrando por isso está vendendo o que é de graça."),
                ("As torres são outra coisa, e são pagas",
                 "<b>€ 16</b> para subir às torres, que são administradas pelo Centre des "
                 "monuments nationaux — outro órgão, outra bilheteria.<br>"
                 + FLAG % "A frase do site engana" +
                 "a página oficial das torres diz <b>“gratuito para menores de 26 anos”</b> "
                 "sem qualificar. <b>Não é para qualquer menor de 26.</b> Pelo Ministério "
                 "da Cultura francês, a gratuidade de 18 a 25 anos vale para quem "
                 "<b>“reside regularmente num Estado membro da União Europeia ou do Espaço "
                 "Econômico Europeu”</b>. <b>Brasileiro de 20 anos paga os € 16 "
                 "cheios.</b><br>"
                 "<b>Menor de 18 não paga, de qualquer nacionalidade.</b><br>"
                 "Fonte: tours-notre-dame-de-paris.fr e culture.gouv.fr, 30/set/2026."),
                ("Fonte que não abriu",
                 FLAG % "Fonte oficial não aberta" +
                 "o site da catedral (notredamedeparis.fr) <b>recusou conexão com erro "
                 "403</b>. O que está acima vem da página oficial das torres, do "
                 "Ministério da Cultura e da imprensa francesa sobre a proposta "
                 "descartada."),
                ("Onde fica",
                 mapa("Cathédrale Notre-Dame de Paris, Parvis Notre-Dame, 75004 Paris, França")),
            ],
        },
        {
            "id": "sainte-chapelle",
            "grupo": "g2",
            "nome": "Sainte-Chapelle",
            "tag": "Capela gótica",
            "preco_val": "€ 22",
            "preco_nota": "menor de 18 não paga",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (sainte-chapelle.fr), do Centre des monuments "
                 "nationaux, consultado em 30/set/2026.<br>"
                 "<b>€ 22</b> a entrada inteira.<br>"
                 + FLAG % "A mesma frase, a mesma armadilha" +
                 "o site diz <b>“gratuito para menores de 26 anos”</b>. Vale o que vale "
                 "para todo monumento nacional francês: <b>menor de 18 não paga, de "
                 "qualquer nacionalidade</b>, mas a faixa de <b>18 a 25 anos só é gratuita "
                 "para quem reside regularmente no Espaço Econômico Europeu</b>.<br>"
                 "O documento aceito é identidade, passaporte ou título de residência com "
                 "foto — e, para o não europeu, residência de <b>mais de três meses</b> em "
                 "território francês."),
                ("Onde fica",
                 mapa("Sainte-Chapelle, 10 Boulevard du Palais, 75001 Paris, França")),
            ],
        },
        {
            "id": "arco-do-triunfo",
            "grupo": "g2",
            "nome": "Arco do Triunfo",
            "tag": "Monumento e mirante",
            "preco_val": "€ 16",
            "preco_nota": "e hoje só se sobe a pé",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (paris-arc-de-triomphe.fr), do Centre des monuments "
                 "nationaux, consultado em 30/set/2026.<br>"
                 "<b>€ 16</b> para subir ao terraço.<br>"
                 "Mesma regra de gratuidade dos outros monumentos nacionais: <b>menor de "
                 "18 não paga, de qualquer nacionalidade; de 18 a 25 só é gratuito para "
                 "residente do Espaço Econômico Europeu</b>."),
                ("O elevador está quebrado",
                 FLAG % "Obra em andamento" +
                 "o site oficial informa que <b>o elevador está em manutenção, até "
                 "segunda ordem</b>, e que <b>o acesso ao terraço se faz unicamente pelas "
                 "escadas</b>.<br>"
                 "<b>Quem tem mobilidade reduzida não consegue subir enquanto isso "
                 "durar.</b> A página não diz quando volta."),
                ("O contraste que vale € 12",
                 "<b>Um brasileiro de 20 anos paga os € 16 inteiros aqui</b> — e paga "
                 "<b>€ 11,80</b>, metade da tarifa adulta, na <b>Torre Eiffel</b>, a "
                 "pouco mais de três quilômetros.<br>"
                 "A Torre Eiffel não é monumento nacional: é administrada por uma empresa "
                 "da cidade, e a tarifa jovem dela é <b>por idade, de 12 a 24 anos</b>, "
                 "sem condição de nacionalidade ou residência."),
                ("Onde fica",
                 mapa("Arc de Triomphe, Place Charles de Gaulle, 75008 Paris, França")),
            ],
        },
        {
            "id": "sacre-coeur",
            "grupo": "g2",
            "nome": "Sacré-Cœur e Montmartre",
            "tag": "Basílica e bairro",
            "preco_val": "Grátis",
            "preco_nota": "a basílica; o domo é pago",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (sacre-coeur-montmartre.com), consultado em "
                 "30/set/2026.<br>"
                 "<b>Entrar na basílica é gratuito.</b><br>"
                 "<b>Abre todos os dias do ano, sem exceção, das 6h30 às 22h30.</b> É um "
                 "dos horários mais largos de Paris, e o único ponto desta ficha que não "
                 "fecha em feriado nenhum."),
                ("O que não apuramos",
                 FLAG % "Não encontrado" +
                 "<b>o preço da subida ao domo</b> não aparece nas páginas de informações "
                 "práticas nem de horários do site oficial. Há a visita do domo e o "
                 "percurso da cripta, mas <b>sem valor publicado nas páginas que "
                 "conseguimos ler</b>. Não pusemos número de terceiro no lugar."),
                ("Onde fica",
                 mapa("Basilique du Sacré-Cœur, 35 Rue du Chevalier de la Barre, 75018 Paris, França")),
            ],
        },

        # ---------------------------------------------------------- g3
        {
            "id": "torre-eiffel",
            "grupo": "g3",
            "nome": "Torre Eiffel",
            "tag": "Torre e mirante",
            "preco_val": "€ 23,50",
            "preco_nota": "2º andar de elevador; topo custa € 36,70",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de tarifas do site oficial (toureiffel.paris), consultada "
                 "em 30/set/2026.<br>"
                 "<b>São quatro bilhetes diferentes, e a diferença entre o mais barato e "
                 "o mais caro é de € 21,90.</b><br>"
                 "<b>2º andar, de elevador:</b> adulto <b>€ 23,50</b> · jovem de 12 a 24 "
                 "<b>€ 11,80</b> · criança de 4 a 11 <b>€ 6</b><br>"
                 "<b>Topo, de elevador:</b> adulto <b>€ 36,70</b> · jovem <b>€ 18,40</b> · "
                 "criança <b>€ 9,20</b><br>"
                 "<b>2º andar, pela escada:</b> adulto <b>€ 14,80</b> · jovem <b>€ 7,40</b> "
                 "· criança <b>€ 3,80</b><br>"
                 "<b>Topo, escada até o 2º e elevador depois:</b> adulto <b>€ 28</b> · "
                 "jovem <b>€ 14</b> · criança <b>€ 7</b><br>"
                 "<b>Menor de 4 anos não paga</b>, mas precisa de bilhete gratuito "
                 "emitido.<br>"
                 "<b>A escada economiza € 8,70 e não tem fila de elevador</b> — são 674 "
                 "degraus até o segundo andar."),
                ("Aqui o passaporte não muda nada",
                 "<b>A tarifa jovem é de 12 a 24 anos, por idade.</b> A página oficial "
                 "não condiciona a nacionalidade nem a residência, ao contrário dos "
                 "monumentos nacionais e do Louvre.<br>"
                 "<b>É o melhor negócio de Paris para um turista jovem de fora da "
                 "Europa.</b>"),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias, das 9h30 às 23h</b>, com <b>últimas subidas às "
                 "22h45</b>.<br>"
                 "<b>O topo e o acesso pela escada não são acessíveis a pessoas com "
                 "mobilidade reduzida.</b><br>"
                 "<b>A partir de 29 de setembro de 2026</b>, grupo de mais de 9 pessoas, "
                 "guia incluído, <b>tem de reservar on-line</b> — compra na bilheteria "
                 "passou a ser proibida para grupos."),
                ("Cuidado com bilhete falso",
                 "O site oficial publica alerta sobre <b>sites fraudulentos que se "
                 "apresentam como oficiais</b> e aparecem em buscadores e em plataformas "
                 "de inteligência artificial. A bilheteria oficial é o toureiffel.paris."),
                ("Onde fica",
                 mapa("Tour Eiffel, Champ de Mars, 5 Avenue Anatole France, 75007 Paris, França")),
            ],
        },
        {
            "id": "catacumbas",
            "grupo": "g3",
            "nome": "Catacumbas de Paris",
            "tag": "Ossuário subterrâneo",
            "preco_val": "€ 31",
            "preco_nota": "audioguia incluído",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (catacombes.paris.fr), consultado em 30/set/2026.<br>"
                 "<b>€ 31</b> a inteira, <b>com audioguia incluído</b>.<br>"
                 "<b>€ 25</b> a reduzida: <b>jovens de 18 a 26 anos</b>, estudantes, "
                 "professores e portadores de cartões parisienses.<br>"
                 "<b>€ 15</b> de 8 a 17 anos. <b>Até 7 anos não paga.</b><br>"
                 "<b>É mais caro que o Louvre para um europeu</b>, e quase o mesmo para "
                 "quem não é.<br>"
                 "<b>Aqui a redução de 18 a 26 é por idade</b>, como na Torre Eiffel e ao "
                 "contrário dos monumentos nacionais — as Catacumbas são da cidade de "
                 "Paris, não do Estado francês."),
                ("Dias em que não funciona",
                 "<b>De terça a domingo, das 9h45 às 20h30</b>, com <b>última entrada às "
                 "19h30</b>.<br>"
                 "<b>Fecha às segundas</b> e em <b>1º de janeiro, 1º de maio e 25 de "
                 "dezembro</b>.<br>"
                 "<b>A reserva on-line abre sete dias antes.</b> <b>Bilhete gratuito não "
                 "pode ser reservado</b>: só se consegue no local, no dia — e o audioguia, "
                 "nesse caso, custa <b>€ 5</b> à parte."),
                ("Onde fica",
                 mapa("Catacombes de Paris, 1 Avenue du Colonel Henri Rol-Tanguy, 75014 Paris, França")),
            ],
        },
        {
            "id": "centre-pompidou",
            "grupo": "g3",
            "nome": "Centre Pompidou",
            "tag": "Museu fechado",
            "preco_val": "Fechado",
            "preco_nota": "até 2030",
            "campos": [
                ("Por que está nesta ficha",
                 "<b>O Centre Pompidou está fechado, e continua em praticamente todo "
                 "guia de Paris.</b> Está aqui para você não montar um dia em volta "
                 "dele.<br>"
                 "Fonte: site oficial (centrepompidou.fr), consultado em 30/set/2026."),
                ("As datas",
                 "<b>O prédio fechou em 22 de setembro de 2025</b>, depois de um "
                 "fechamento progressivo ao longo daquele ano. Houve um evento de "
                 "despedida em <b>24 e 25 de outubro de 2025</b>.<br>"
                 "<b>A obra começa no início de 2026</b> — o próprio site fala em "
                 "abril — e envolve retirada de amianto de todas as fachadas, segurança "
                 "contra incêndio e acessibilidade.<br>"
                 "<b>A reabertura está prevista para 2030.</b> São cinco anos."),
                ("O que existe no lugar",
                 "<b>O programa Constellation</b> espalha a programação por outros museus, "
                 "na França e fora dela, desde abril de 2025.<br>"
                 "<b>A Biblioteca Pública de Informação mudou para o 12º arrondissement</b>, "
                 "no edifício Lumière, aberto em 25 de agosto de 2025.<br>"
                 "<b>O Centre Pompidou Francilien abre na primavera europeia de 2027</b>, "
                 "em Massy, fora de Paris."),
                ("Onde fica",
                 mapa("Centre Pompidou, Place Georges-Pompidou, 75004 Paris, França")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem e a taxa de estadia",
            "tag": "Conta, não lugar",
            "preco_val": "€ 3,25 a € 15,93",
            "preco_nota": "por pessoa, por noite, fora da diária",
            "campos": [
                ("O que é",
                 "<b>A taxe de séjour é cobrada por pessoa e por noite, e não vem no "
                 "preço da reserva.</b> Aparece no check-in ou no check-out, e surpreende "
                 "quem fechou a conta antes de viajar.<br>"
                 "O valor sobe com a categoria da hospedagem, e o total inclui a taxa "
                 "municipal mais adicionais departamental, regional e do transporte da "
                 "Île-de-France."),
                ("Os valores",
                 FLAG % "Só em fonte secundária" +
                 "<b>este é o único número desta ficha que não conseguimos em fonte "
                 "oficial aberta.</b> A página da prefeitura de Paris sobre a taxa "
                 "respondeu <b>404</b>, e a tabela oficial da administração fiscal "
                 "francesa é um arquivo de dados para download, não uma página "
                 "citável.<br>"
                 "O que segue vem de <b>fontes secundárias convergentes</b>, para "
                 "vigência a partir de <b>1º de janeiro de 2026</b>, por pessoa e por "
                 "noite, com adicionais incluídos:<br>"
                 "<b>Palace € 15,93</b> · <b>5 estrelas € 11,70</b> · "
                 "<b>4 estrelas € 8,45</b> · <b>3 estrelas € 5,53</b> · "
                 "<b>2 estrelas € 3,25</b><br>"
                 "<b>Aluguel de temporada não classificado</b> é calculado como percentual "
                 "da diária por pessoa, com <b>teto de € 15,93</b>.<br>"
                 "<b>Trate estes valores como ordem de grandeza, não como número "
                 "apurado</b> — e confira com o seu hotel antes de fechar a conta."),
                ("O que isso soma numa viagem",
                 "Num hotel <b>3 estrelas</b>, <b>duas pessoas</b>, <b>cinco noites</b>: "
                 "<b>€ 55,30</b> fora da diária.<br>"
                 "É mais que a entrada de duas pessoas no Louvre pagando a tarifa de "
                 "não europeu."),
            ],
        },
    ],
}

DESTINOS = [PARIS]
