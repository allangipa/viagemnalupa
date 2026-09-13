# -*- coding: utf-8 -*-
from lib import mapa, flag, ul

MMP_FAIXAS = ("<b>Criança até 12 anos: grátis.</b> <b>Jovem de 13 a 24 anos</b> e <b>sénior a "
  "partir de 65</b>: metade. <b>Família</b>, no critério da casa “pelo menos um adulto mais "
  "um menor”: metade por pessoa. Não há tarifa de grupo turístico — o desconto por volume "
  "é para operadores, a partir de 250 bilhetes.")

ACESSO52 = ("<b>Não existe mais o “domingo de manhã grátis” nesta rede, e isso pega "
  "muito turista.</b> O que existe hoje é o <b>Acesso 52</b>: quem <b>reside em Portugal</b> tem "
  "52 entradas gratuitas por ano, em qualquer dia da semana, apresentando Cartão de Cidadão — e o "
  "bilhete só sai na bilheteira física, nunca online. <b>Se você não mora em Portugal, não há dia "
  "grátis aqui.</b> Não vá no domingo de manhã esperando entrar de graça.")

G1 = {
 "titulo": "Belém: o conjunto monumental",
 "intro": "Quatro endereços a distância de caminhada, e três deles fecham na segunda-feira. "
   "É o bairro onde o roteiro mais dá errado por detalhe de horário — e onde as regras mudaram "
   "quase todas nos últimos dezoito meses.",
 "pontos": [
{
 "id":"mosteiro-jeronimos","nome":"Mosteiro dos Jerónimos","tag":"Monumento","img":"jeronimos",
 "preco":"€ 18","preconota":"o mais caro da rede nacional",
 "campos":{
 "Endereço":"Praça do Império, 1400-206 Lisboa. Telefone +351 213 620 034. Você não tem como "
   "errar, e esse é justamente o ponto: são mais de 300 metros de fachada de pedra bege, de frente "
   "para um jardim retangular gigante com chafariz no meio. Se você chegou pela Rua de Belém, a dos "
   "pastéis, o mosteiro é o prédio imenso logo depois da pastelaria.<br>"
   "<b>A referência que resolve a confusão:</b> a fachada tem <b>duas portas grandes e elas levam a "
   "lugares diferentes</b>. A portada sul, a lateral enorme cheia de esculturas virada para o rio, "
   "é a entrada da <b>igreja</b>. A entrada do <b>claustro</b> — a parte paga — fica mais à "
   "esquerda, na ala virada para a praça, junto da bilheteira. Quem entra só pela portada sul vê a "
   "igreja, sai achando que viu o mosteiro, e não viu o claustro."
   +mapa("Mosteiro dos Jerónimos","Mosteiro dos Jeronimos, Praca do Imperio, Lisboa"),
 "Valor da entrada":"Fonte: Museus e Monumentos de Portugal, consultado em 13/set/2026.<br>"
   "<b>Inteira € 18</b> (≈ R$ 107). É o <b>monumento mais caro da rede nacional</b> — está sozinho "
   "nesse patamar; Torre de Belém, Batalha, Alcobaça, Mafra e Coches ficam todos em € 15.<br>"
   +MMP_FAIXAS+" Aplicando o percentual oficial ao preço oficial, jovem, sénior e família saem a "
   "<b>€ 9</b>.<br>"+ACESSO52+"<br>"
   "<b>Preço fixo</b>, sem variação por data ou procura. "+flag("Atenção ao checkout")+" a "
   "bilheteira online exibe o intervalo “entre 0 € e 19,11 €”, acima dos € 18 de tabela, "
   "e <b>a plataforma não explica em texto o que é essa diferença</b> — provavelmente encargo de "
   "serviço. Registramos o fato, não a explicação.<br>"
   "<b>Lisboa Card: entrada livre, não desconto.</b> Existe um produto dedicado na bilheteira "
   "oficial, emitido a € 0,00, em que se reserva a sessão e se paga zero informando o código do "
   "cartão.",
 "Pontos de referência":"O Jardim da Praça do Império, entre o mosteiro e o rio, com chafariz "
   "central — é a referência visual mais óbvia de Belém. Os <b>Pastéis de Belém</b>, na Rua de "
   "Belém 84 a 92, abertos todos os dias das 8h às 21h (até 22h de julho a setembro), a poucos "
   "metros na mesma calçada. O Centro Cultural de Belém, o bloco de pedra clara moderno do outro "
   "lado da praça. O Palácio de Belém, o palácio rosa da Presidência, a leste. E o Jardim Botânico "
   "Tropical, com entrada discreta atrás do conjunto.<br>"
   "<b>O Museu Nacional de Arqueologia funciona dentro da ala oeste do próprio mosteiro e está "
   "fechado</b> para obras, sem data de reabertura publicada. Se ele estava no seu roteiro, refaça "
   "o roteiro.",
 "Metrô mais próximo":"<b>Não há metro em Belém.</b> Nem no Restelo. O bairro é servido por "
   "elétrico, autocarro, comboio e barco — e essa é uma das primeiras coisas que surpreende quem "
   "chega.<br>"
   "<b>Elétrico 15E</b> (Praça da Figueira ↔ Algés), com paragem de nome literal: "
   "<b>“Mosteiro Jerónimos”</b>. <b>Autocarros 714, 727, 728, 729 e 751</b> servem o eixo "
   "de Belém; o 728 liga a Cais do Sodré, Praça do Comércio, Santa Apolónia e Oriente. <b>Comboio:</b> "
   "estação de Belém, na Linha de Cascais, com partida no Cais do Sodré — mas a bilheteira da "
   "estação só abre em dias úteis, das 10h15 às 13h15 e das 14h às 17h45, e <b>fecha aos fins de "
   "semana e feriados</b>. "+flag("Sem tempo a pé")+" nem a MMP, nem a Carris, nem a CP publicam.",
 "Visitantes por ano":"<b>1.040.203 visitantes em 2025</b>, contra 946.014 em 2024. É o monumento "
   "mais visitado da rede nacional e <b>o único que passou de um milhão</b>. Fonte: MMP, balanço "
   "publicado em 29/abr/2026, e o relatório de estatísticas de 2024.<br>"
   "Para dimensionar: a rede toda somou 4.843.299 visitantes em 2025, queda de 4,38% sobre 2024; "
   "56% eram turistas estrangeiros; e o Acesso 52 gerou 892.637 visitas gratuitas, 18% do total.",
 "Menor visitação e temperatura":"<b>A MMP não publica série mensal de visitação.</b> "
   +flag("Sem dado mensal")+" Conferimos o relatório de estatísticas da própria instituição: ele "
   "traz apenas totais anuais, de 2017 a 2024. <b>Não é possível dizer, com fonte, qual é o mês "
   "mais vazio no Jerónimos</b>, e não vamos inventar um.<br>"
   "O que dá para entregar com fonte é o clima, pelas normais de 30 anos do IPMA (estação Lisboa / "
   "Instituto Geofísico, série 1991–2020): o mês mais frio é <b>janeiro</b>, com média de 11,8 °C e "
   "mínima média de 8,6 °C; o mais chuvoso é <b>novembro</b>, com 133,9 mm; e o mais quente é "
   "<b>agosto</b>, com 23,8 °C de média e máxima média de 28,8 °C. Julho e agosto são radicalmente "
   "secos — 2,6 mm e 5,4 mm.",
 "Curiosidades":ul([
   "O mosteiro foi pago com o dinheiro das especiarias, e há um número: o Turismo de Portugal "
   "escreve que D. Manuel I canalizou para a obra cerca de 5% das receitas do comércio com a África "
   "e o Oriente, o equivalente a 70 kg de ouro por ano.",
   "O Tratado de Lisboa da União Europeia foi assinado aqui, em 13 de dezembro de 2007, durante a "
   "presidência portuguesa do Conselho.",
   "Fernando Pessoa está sepultado no claustro, na ala norte — ou seja, o túmulo do poeta está na "
   "parte <b>paga</b>, não na igreja. Registramos que esta é a única curiosidade da ficha sem fonte "
   "primária oficial: não achamos a confirmação em página da MMP nem do Património Cultural.",
   "A obra levou cerca de um século e passou por quatro mestres: Diogo de Boitaca definiu a "
   "implantação, João de Castilho assumiu a partir de 1517, Diogo de Torralva entre 1540 e 1551, e "
   "Jerónimo de Ruão concluiu, entre 1563 e 1601."]),
 "Fatos históricos":"D. Manuel I pediu autorização à Santa Sé em 1496 e a construção começou em "
   "<b>1501</b>, prolongando-se por cerca de um século. "+flag("Fontes divergem")+" a Comissão "
   "Nacional da UNESCO e o Turismo de Portugal dizem 1501; outra fonte diz 1502. Era a casa da "
   "<b>Ordem de São Jerónimo</b> — daí o nome —, com a função de rezar pela alma do rei e assistir "
   "aos navegantes que partiam da praia do Restelo.<br>"
   "<b>Monumento Nacional</b> pelo Decreto de 10/jan/1907, reclassificado pelo Decreto de "
   "16/jun/1910. <b>Património Mundial da UNESCO desde dezembro de 1983</b>, em bem seriado com a "
   "Torre de Belém, critérios (iii) e (vi), com área inscrita de 2,66 hectares e zona tampão de 103.<br>"
   "O claustro foi secularizado no século XIX. Vasco da Gama e Camões têm sepulturas no monumento — "
   "<b>e aqui há uma divergência de natureza que não resolvemos</b>: umas fontes falam em túmulos, o "
   "Turismo de Portugal chama de cenotáfios. Há ainda obra de conservação em curso financiada pelo "
   "PRR, com € 3,7 milhões e conclusão prevista para o primeiro trimestre de 2026; "+flag("não confirmamos")+
   " em fonte oficial se já foi dada por concluída.",
 "Dias em que não funciona":"<b>Fecha às segundas-feiras.</b> Fecha também em 1 de janeiro, "
   "domingo de Páscoa, 1 de maio, <b>13 de junho</b> (Santo António, feriado municipal de Lisboa) e "
   "25 de dezembro.<br>"
   "<b>Claustro</b>, a parte paga: terça a domingo, <b>9h30 às 17h30</b>, com última entrada às 17h. "
   "<b>Igreja</b>: terça a sábado das 10h30 às 17h; domingos e feriados religiosos das 14h às 17h. "
   "Não há horário de verão diferenciado — a MMP não publica nenhum.<br>"
   "<b>A bilheteira fecha às 16h30, uma hora antes do monumento.</b> Chegar às 16h45 achando que dá "
   "tempo é o erro mais banal e mais fatal de Belém.<br>"
   "<b>E a fila é real:</b> a própria ficha oficial do produto na bilheteira admite que a "
   "arquitetura do monumento gera “filas de espera superiores a 2 horas em períodos de pico "
   "de visitantes”. Isso está escrito pela casa, não por um blog. A bilheteira online vende "
   "por sessão, mas "+flag("não encontrado")+" em nenhuma fonte oficial a frase explícita de que a "
   "hora marcada é obrigatória aqui.",
 "Pontos turísticos próximos":"Torre de Belém, Padrão dos Descobrimentos, Museu Nacional dos "
   "Coches, Museu de Marinha, Centro Cultural de Belém, MAAT, Jardim Botânico Tropical, Palácio de "
   "Belém, Pastéis de Belém e a Doca de Belém. O Museu Nacional de Arqueologia, dentro do próprio "
   "mosteiro, está fechado. "+flag("Sem distância oficial")}
},
{
 "id":"torre-de-belem","nome":"Torre de Belém","tag":"Monumento","img":"torrebelem",
 "preco":"€ 15","preconota":"teto de 900 visitantes por dia",
 "campos":{
 "Endereço":"Av. Brasília, 1400-038 Lisboa. A torre está <b>dentro da água</b>, a poucos metros "
   "da margem, ligada à terra por uma <b>passarela de madeira estreita</b>. Você vai vê-la de longe: "
   "é a única torre branca de pedra rendilhada plantada no rio. Da Praça do Império caminha-se para "
   "oeste com o rio à esquerda, passando pelo Padrão e por um jardim com um monumento em forma de "
   "avião.<br><b>A referência que resolve:</b> a fila <b>não se forma na torre</b> — forma-se em "
   "terra, antes da passarela. Se você não está vendo a passarela, você ainda não chegou."
   +mapa("Torre de Belém","Torre de Belem, Av. Brasilia, Lisboa"),
 "Valor da entrada":"Fonte: MMP, consultada em 13/set/2026. <b>Inteira € 15</b> (≈ R$ 89).<br>"
   +MMP_FAIXAS+" Jovem, sénior e família saem a <b>€ 7,50</b>. "+flag("Nota de rigor")+" a MMP "
   "publica o percentual e o preço de tabela, não a lista de valores absolutos; os € 7,50 são "
   "aritmética declarada, não estimativa.<br>"+ACESSO52+"<br>"
   "<b>Preço fixo.</b> A bilheteira online exibe “entre 0 € e 15,92 €”, acima da tabela, "
   "sem explicação em texto.<br>"
   "<b>Lisboa Card: entrada livre</b>, com produto dedicado a € 0,00. <b>Mas leia a letra miúda "
   "oficial:</b> o bilhete “só será válido após validação correta do Lisboa Card no "
   "equipamento dedicado instalado na Torre de Belém”. Ou seja, <b>o cartão físico tem de ser "
   "validado na chegada</b>, e a sessão precisa ser reservada do mesmo jeito.",
 "Pontos de referência":"O Padrão dos Descobrimentos, a leste, na mesma frente de rio. O memorial "
   "aos aviadores Gago Coutinho e Sacadura Cabral, o monumento em forma de avião entre os dois. O "
   "jardim em frente, onde a fila se organiza. O Forte do Bom Sucesso, ao lado. A Ponte 25 de Abril, "
   "visível rio acima. E o MAAT, a leste, na margem.",
 "Metrô mais próximo":"<b>Não há metro em Belém</b> — vale o mesmo da ficha anterior. "
   "<b>Elétrico 15E</b>, com a paragem mais próxima em <b>“Lg. Princesa”</b>; "
   "“Altinho (MAAT)” também serve o troço oeste. <b>Autocarros 714, 727, 728, 729 e "
   "751.</b> <b>Comboio:</b> estação de Belém, Linha de Cascais.<br>"
   +flag("Sem tempo a pé")+" nenhuma fonte publica. O que registramos é um fato útil: <b>a torre é "
   "o ponto mais a oeste do conjunto</b> — é a mais afastada das paragens centrais de Belém.",
 "Visitantes por ano":"<b>387.379 visitantes em 2024</b>, pelo relatório de estatísticas da MMP.<br>"
   "Em 2025 foram <b>127.791</b> — e o número baixo <b>não é queda de procura</b>: o monumento fechou "
   "em maio de 2025 para obras. É ano incompleto, e apresentá-lo como tendência seria enganar.<br>"
   "2026 ainda não tem número publicado: a torre só reabriu em maio e o balanço anual da MMP sai por "
   "volta de abril do ano seguinte.",
 "Menor visitação e temperatura":"<b>A MMP não publica série mensal</b>, e aqui a lacuna é ainda "
   "mais séria. "+flag("Sem dado mensal")+" Há um agravante honesto: <b>mesmo que a série existisse, "
   "2025 e 2026 estariam distorcidos pelo ano de fechamento.</b> Qualquer “mês mais vazio” "
   "calculado sobre esses dois anos seria lixo estatístico.<br>"
   "Clima pelas normais do IPMA: janeiro é o mês mais frio (11,8 °C de média), novembro o mais "
   "chuvoso (133,9 mm), agosto o mais quente (23,8 °C).<br>"
   "<b>E há uma coisa que a tabela de clima não captura:</b> a torre fica <b>dentro do rio</b>, "
   "exposta. Vento e chuva batem ali muito mais forte do que numa rua de Belém — e a estação "
   "meteorológica que gera esses números está a 77 metros de altitude, no interior da cidade.",
 "Curiosidades":ul([
   "A gárgula do rinoceronte é considerada a primeira representação escultórica de um rinoceronte "
   "feita na Europa. Liga-se ao rinoceronte Ganda, que chegou a Lisboa em 20 de maio de 1515 como "
   "presente a D. Manuel I — o mesmo animal que inspirou a célebre gravura de Dürer, feita sem que "
   "o artista jamais o tivesse visto.",
   "A torre não nasceu monumento bonito: nasceu arma. Foi concebida como baluarte artilhado de "
   "defesa da entrada do Tejo, dentro de um plano de três pontos articulado com Cascais e com a "
   "fortaleza de São Sebastião na outra margem.",
   "Foi prisão, aquartelamento, alfândega e farol. As masmorras guardaram presos de estatuto "
   "elevado, e a função prisional manteve-se durante as invasões francesas.",
   "A limpeza de 2025 e 2026 revelou ornamentos que ninguém via — esferas armilares e escudos com "
   "pormenores que eram impossíveis de enxergar antes."]),
 "Fatos históricos":"Construída por ordem de D. Manuel I, com início em <b>1514</b>. "
   +flag("Fontes oficiais divergem")+" o Património Cultural I.P. e a Comissão Nacional da UNESCO "
   "dizem que ficou concluída em <b>1520</b>; a página da própria MMP, que gere o monumento, diz "
   "<b>1514–1519</b>. São duas fontes oficiais portuguesas com anos diferentes, e não escolhemos "
   "uma.<br>Autor: <b>Francisco de Arruda</b>, documentado como mestre do Baluarte de Belém. São "
   "duas partes — uma torre esbelta com quatro câmaras abobadadas e um baluarte mais largo com "
   "casamata para artilharia — decoradas com cordas e nós, esferas armilares, cruzes da Ordem de "
   "Cristo e elementos de inspiração mourisca. <b>Património Mundial da UNESCO desde 1983</b>, em "
   "bem seriado com os Jerónimos. "+flag("Não confirmado")+" a ficha individual de Monumento "
   "Nacional não abriu na base de Património Imóvel.<br>"
   "<b>A obra de 2025–2026 foi a primeira intervenção de fundo desde 1998</b>: quatro pisos, o "
   "terraço e os 93 degraus da escada em caracol, com limpeza e consolidação da pedra, tratamento "
   "de madeiras e renovação elétrica. Custou mais de € 1 milhão, financiada pelo PRR.",
 "Dias em que não funciona":"<b>Fecha às segundas-feiras</b>, mais 1 de janeiro, domingo de "
   "Páscoa, 1 de maio, 13 de junho e 25 de dezembro. Horário de terça a domingo, <b>9h30 às 17h30</b>, "
   "sem diferença entre verão e inverno.<br>"
   "<b>Última entrada às 17h</b> — "+flag("origem em imprensa")+" a página oficial da MMP <b>não "
   "publica</b> última entrada nem hora de fecho da bilheteira; esse horário vem do despacho de "
   "agência sobre a reabertura. Registramos a origem para você saber o peso do dado.<br>"
   "<b>As regras novas, que são o mais importante desta ficha:</b> a torre esteve fechada cerca de "
   "um ano e reabriu em <b>maio de 2026</b> com um sistema de entrada inteiramente novo. Qualquer "
   "guia ou vídeo anterior a isso está errado.<br>"
   "<b>Lotação máxima de 900 visitantes por dia</b> — não é “costuma encher”, é teto "
   "rígido: quando acaba, acabou. <b>Entrada por sessões de 30 em 30 minutos, com 60 pessoas por "
   "sessão.</b> A espera máxima estimada pela MMP é de 20 minutos — é a promessa da casa, não uma "
   "medição independente.<br>"
   "<b>E há um detalhe operacional que muda o seu dia:</b> o bilhete da torre também se compra na "
   "<b>bilheteira do Mosteiro dos Jerónimos</b>. Dá para resolver a torre enquanto você está no "
   "mosteiro.<br>"
   "<b>São 93 degraus em escada de caracol, sem elevador.</b> Isso condiciona a acessibilidade e é "
   "parte do motivo de existir limite. "+flag("Datas divergem")+" a MMP fala em reabertura a 26 de "
   "maio, com cerimónia; outra fonte diz que a abertura ao público foi a 27.",
 "Pontos turísticos próximos":"Padrão dos Descobrimentos, memorial aos aviadores, Forte do Bom "
   "Sucesso, MAAT, Centro Cultural de Belém, Mosteiro dos Jerónimos, Museu Nacional dos Coches, "
   "Pastéis de Belém, Jardim Botânico Tropical e Doca de Belém. "+flag("Sem distância oficial")}
},
{
 "id":"padrao-descobrimentos","nome":"Padrão dos Descobrimentos","tag":"Monumento e mirante","img":"padrao",
 "preco":"€ 10","preconota":"completo; € 5 só a exposição",
 "campos":{
 "Endereço":"Av. Brasília, 1400-038 Lisboa. Telefone +351 213 031 950. <b>Atenção:</b> o Padrão e "
   "a Torre de Belém <b>partilham o mesmo código postal e a mesma avenida</b> — não tente "
   "distinguir os dois por endereço, distinga por forma.<br>"
   "É o monumento de pedra clara em forma de <b>proa de caravela</b>, com 56 metros, apontando para "
   "o rio, com 32 figuras esculpidas subindo pelas duas rampas laterais. <b>A referência está no "
   "chão:</b> diante da entrada há uma enorme <b>rosa-dos-ventos em calçada portuguesa</b>, com um "
   "mapa-múndi desenhado. Você literalmente pisa nela antes de chegar à porta. Vindo do mosteiro, é "
   "preciso atravessar a linha férrea e a avenida — há passagem pedonal."
   +mapa("Padrão dos Descobrimentos","Padrao dos Descobrimentos, Av. Brasilia, Lisboa"),
 "Valor da entrada":"<b>Este monumento não é do Estado: é da EGEAC, a empresa municipal de "
   "Lisboa.</b> Preços, gratuidades e regras são completamente diferentes dos dois anteriores — não "
   "assuma nada por analogia. Fonte: bilheteira oficial, consultada em 13/set/2026.<br>"
   "<b>E há dois bilhetes diferentes, que é a primeira coisa a entender.</b><br>"
   "<b>Bilhete completo</b>, com mirante, exposição e filme: <b>inteira € 10</b>; jovem de 13 a 25 "
   "anos não residente em Lisboa e estudante do superior até 25 anos, € 5; estudante do superior a "
   "partir de 26, € 8; pessoas com necessidades específicas e profissionais das artes performativas, "
   "€ 7; <b>sénior a partir de 65 anos</b> não residente em Lisboa, <b>€ 8,50</b>.<br>"
   "<b>Bilhete só da exposição</b>: inteira € 5; jovem e estudante até 25, € 2,50; estudante a "
   "partir de 26, € 4; necessidades específicas e artes performativas, € 3,50; sénior, € 4,30.<br>"
   "<b>Se você quer só a vista, tem de comprar o completo</b> — não existe bilhete de mirante avulso. "
   "E o de € 5 não sobe: muita gente compra o barato e descobre lá dentro.<br>"
   +flag("Lacunas na tabela oficial")+" não existe bilhete de família, não há tarifa de grupo "
   "publicada, e entre a gratuidade até os 12 anos e a faixa jovem a partir dos 13 não há faixa "
   "intermediária.<br>"
   "<b>Aqui existe horário gratuito — mas não é para você.</b> Residentes <b>no concelho de "
   "Lisboa</b> entram de graça aos domingos e feriados até às 14h. É recorte municipal, mais estreito "
   "que “residente em Portugal”: duas faixas da tabela estão explicitamente marcadas como "
   "“não residentes em Lisboa”, porque o lisboeta dessas idades entra pelo Cultura Pass.<br>"
   "<b>Lisboa Card: entrada gratuita</b>, constando na lista oficial de gratuidades. Preço fixo, "
   "sem variação por data.",
 "Pontos de referência":"A rosa-dos-ventos e o mapa-múndi em calçada, diante da entrada — oferta "
   "da África do Sul, em 1960. A Torre de Belém a oeste, na mesma frente de rio. O Jardim da Praça "
   "do Império e o mosteiro a norte, atravessando a linha férrea. A Doca de Belém a leste. A Ponte "
   "25 de Abril, visível. E o Cristo Rei, na outra margem do Tejo, visível do mirante.",
 "Metrô mais próximo":"<b>Não há metro em Belém.</b> <b>Elétrico 15E</b>, paragens "
   "“Mosteiro Jerónimos” e “Lg. Princesa”. <b>Autocarros 714, 727, 728, "
   "729 e 751.</b> <b>Comboio:</b> estação de Belém, Linha de Cascais.<br>"
   +flag("Lacuna declarada")+" o site oficial do Padrão e a página da EGEAC <b>não publicam</b> "
   "seção de como chegar com números de linha. As linhas acima vêm da Carris e da CP, não do "
   "monumento — e nenhuma das três publica tempo a pé.",
 "Visitantes por ano":flag("Não encontrado")+" não existe número oficial e recente de visitantes "
   "anuais do Padrão dos Descobrimentos.<br>"
   "Procuramos no site oficial, no site da EGEAC, nos relatórios de atividades disponíveis, e no "
   "relatório da rede nacional — que não serve, porque o Padrão não pertence a essa rede. <b>A razão "
   "da lacuna é estrutural:</b> a EGEAC é municipal e não publica relatório de visitantes por "
   "equipamento no formato anual e aberto que a rede do Estado publica. Há notícias antigas com "
   "estimativas em contexto orçamental, mas não são dado apurado e por isso não os usamos.",
 "Menor visitação e temperatura":flag("Não existe série")+" nem mensal, nem anual recente. <b>É a "
   "lacuna mais larga deste guia</b>, e dizemos isso em vez de preencher.<br>"
   "Clima pelas normais do IPMA: janeiro é o mais frio (11,8 °C), novembro o mais chuvoso (133,9 mm), "
   "agosto o mais quente (23,8 °C).<br>"
   "<b>Nota prática:</b> o mirante é ao ar livre, a 56 metros de altura, sobre o rio. Em dia de "
   "vento ou chuva a experiência muda radicalmente — e o valor do bilhete completo está quase todo "
   "nessa subida.",
 "Curiosidades":ul([
   "O monumento que você vê é a segunda versão, e a primeira era descartável: foi erguido em 1940 "
   "em versão temporária, com materiais perecíveis e esculturas em gesso, para a Exposição do Mundo "
   "Português. A versão definitiva só veio vinte anos depois.",
   "A rosa-dos-ventos do chão foi presente da África do Sul, em 1960 — não faz parte do projeto "
   "original do monumento, é oferta diplomática.",
   "São 32 figuras, e o Infante D. Henrique vai à frente: navegadores, cartógrafos, guerreiros, "
   "colonizadores, missionários, cronistas e artistas.",
   "O mirante e o auditório não são de 1960, são de 1985 — vieram com o Centro Cultural das "
   "Descobertas, do arquiteto Fernando Ramalho. O monumento passou 25 anos sem a função de mirante "
   "que hoje é o motivo número um da visita."]),
 "Fatos históricos":"Versão temporária em <b>1940</b>, para a Exposição do Mundo Português. "
   "Versão permanente construída entre 1958 e 1960 e <b>inaugurada a 9 de agosto de 1960</b>, em "
   "betão e alvenaria de pedra de Leiria, de tom rosado, com as esculturas em calcário de Sintra. "
   "Remodelação em 1985. Arquiteto <b>José Ângelo Cottinelli Telmo</b> e escultor <b>Leopoldo de "
   "Almeida</b>. São 56 metros e 32 figuras.<br>"
   "<b>O dado que quase todo guia erra: o Padrão dos Descobrimentos NÃO é Património Mundial da "
   "UNESCO.</b> A inscrição de 1983 abrange apenas o Mosteiro dos Jerónimos e a Torre de Belém. O "
   "Padrão está dentro da <b>zona tampão</b>, o que é outra coisa — proteção do enquadramento, não "
   "inscrição.<br>"
   "<b>E ele ainda nem está classificado: está em vias de classificação.</b> O processo corre desde "
   "2021 e, em 20 de novembro de 2025, foi publicado em <i>Diário da República</i> o anúncio que "
   "propõe a classificação como <b>Monumento de Interesse Público</b>, abrangendo o monumento e o "
   "pavimento envolvente com a rosa-dos-ventos. A lei dá prazo máximo de um ano. "
   +flag("Não confirmado")+" se a classificação foi concluída até hoje.",
 "Dias em que não funciona":"<b>Não há fecho semanal: abre todos os dias.</b> É a grande vantagem "
   "prática deste monumento — <b>ele resolve a segunda-feira</b>, o dia em que Jerónimos, Torre e "
   "Coches estão todos fechados.<br>"
   "<b>É também o único dos quatro com horário sazonal declarado:</b> de outubro a fevereiro, das "
   "10h às 18h, com última entrada às 17h30; de março a setembro, das 10h às 19h, com última entrada "
   "às 18h30.<br>"
   "<b>Encerra em 1 de janeiro, 1 de maio, 24, 25 e 31 de dezembro.</b> Repare na diferença: o "
   "Padrão <b>não fecha</b> a 13 de junho nem no domingo de Páscoa, mas <b>fecha</b> a 24 e 31 de "
   "dezembro, dias em que os monumentos do Estado não anunciam encerramento. São calendários "
   "distintos — não generalize.<br>"
   +flag("Não publicado")+" o site não anuncia bilhete com hora marcada nem limite de lotação, e "
   "também não publica nada sobre o funcionamento do elevador ou a acessibilidade do percurso até o "
   "mirante. Ausência de informação não é garantia de que não exista.",
 "Pontos turísticos próximos":"Torre de Belém, Mosteiro dos Jerónimos, Museu Nacional dos Coches, "
   "MAAT, Centro Cultural de Belém, Museu de Marinha, Doca de Belém, Jardim da Praça do Império, "
   "Pastéis de Belém e o memorial aos aviadores. "+flag("Sem distância oficial")}
},
{
 "id":"museu-dos-coches","nome":"Museu Nacional dos Coches","tag":"Museu","img":"coches",
 "preco":"€ 15","preconota":"Picadeiro Real fechado desde set/2025",
 "campos":{
 "Endereço":"Avenida da Índia, 136, 1300-300 Lisboa. Telefone +351 210 732 319.<br>"
   "<b>E aqui há uma armadilha real: o museu tem dois endereços, porque são dois edifícios.</b> O "
   "<b>museu novo</b>, na Avenida da Índia 136, está <b>aberto</b>. O <b>Picadeiro Real</b>, o "
   "salão histórico decorado onde os coches ficavam antigamente, fica na <b>Praça Afonso de "
   "Albuquerque</b>, colado ao Palácio de Belém, do outro lado da rua — e <b>está fechado</b>. Se "
   "você for à Praça Afonso de Albuquerque procurando o museu, chegou ao endereço errado e "
   "fechado.<br>"
   "<b>A referência do edifício aberto:</b> é o bloco de betão branco, comprido e elevado sobre "
   "pilares, do lado do rio da Avenida da Índia. Arquitetura contemporânea, nada de manuelino. "
   "Sobe-se uma rampa para entrar."
   +mapa("Museu Nacional dos Coches","Museu Nacional dos Coches, Avenida da India 136, Lisboa"),
 "Valor da entrada":"Fonte: MMP, consultada em 13/set/2026. <b>Inteira € 15</b> (≈ R$ 89) — o "
   "museu partilha o patamar dos grandes monumentos, ao lado da Torre de Belém, Alcobaça, Batalha e "
   "Mafra. Houve aumento generalizado na rede em 2025, com subidas noticiadas de até € 7.<br>"
   +MMP_FAIXAS+" Jovem, sénior e família saem a <b>€ 7,50</b>, por aplicação do percentual oficial.<br>"
   +ACESSO52+"<br>"
   "<b>Preço fixo.</b><br>"
   "<b>Lisboa Card: </b>"+flag("não confirmado")+" o museu <b>não aparece</b> na lista de atrações "
   "do cartão que conseguimos ler, ao contrário de Jerónimos, Torre e Padrão, que aparecem "
   "explicitamente. <b>Não dizemos que está incluído nem que está excluído</b> — ausência de menção "
   "não é prova de exclusão. Confirme antes de contar com ele.",
 "Pontos de referência":"O Palácio de Belém, o palácio <b>rosa</b> da Presidência da República, na "
   "Praça Afonso de Albuquerque, em frente ao Picadeiro Real. A própria praça, com coreto e "
   "monumento central. A estação de Belém, no mesmo eixo da linha férrea. A Doca de Belém e o Padrão "
   "a sul e oeste. Os Pastéis de Belém e o mosteiro, a oeste.",
 "Metrô mais próximo":"<b>Não há metro em Belém.</b> <b>Elétrico 15E</b>, e aqui a paragem tem o "
   "nome do museu: <b>“Belém (Museu Coches)”</b> — é a mais direta possível. "
   "<b>Autocarros 714, 727, 728, 729 e 751.</b> <b>Comboio:</b> estação de Belém, Linha de Cascais — "
   "e este é o ponto mais próximo da estação entre os quatro de Belém, já que o museu fica sobre a "
   "Avenida da Índia. "+flag("Sem tempo a pé")+" nenhuma fonte publica.",
 "Visitantes por ano":"<b>193.614 visitantes em 2025</b>, contra <b>219.506 em 2024</b>. O número "
   "é contabilizado somando museu e Picadeiro Real. Fonte: MMP.<br>"
   "<b>Leitura honesta da queda de 12%:</b> não afirmamos a causa. Registramos dois fatos que "
   "coexistem — o Picadeiro Real fechou em 29 de setembro de 2025, e os preços da rede subiram no "
   "mesmo ano. <b>A MMP não publica a decomposição do número entre os dois espaços</b>, então não é "
   "possível dizer com dado quanto da queda veio de cada coisa.",
 "Menor visitação e temperatura":"<b>A MMP não publica série mensal.</b> "+flag("Sem dado mensal")+
   " E agrava-se aqui o mesmo problema da Torre: o número de 2025 mistura dois espaços, um dos quais "
   "fechou no meio do ano.<br>"
   "Clima pelas normais do IPMA: janeiro o mais frio, novembro o mais chuvoso, agosto o mais quente.<br>"
   "<b>Mas há uma nota prática que só vale para este dos quatro:</b> o Museu dos Coches é "
   "inteiramente coberto. <b>É o único ponto de Belém que funciona bem em dia de chuva</b> — e, "
   "olhando a normal, novembro, outubro, dezembro e janeiro somam mais de 100 mm cada. É neles que "
   "este museu vira a carta na manga do roteiro.",
 "Curiosidades":ul([
   "O museu foi fundado por uma rainha, em 1905: D. Amélia criou-o para salvar a coleção de "
   "viaturas de gala da Casa Real.",
   "A coleção é apresentada oficialmente como a mais importante do mundo no seu género — mais de 70 "
   "veículos históricos, abrangendo quatro séculos e mais de sete países.",
   "Há coches diplomáticos feitos para impressionar um papa: o Coche do Papa Clemente XI e o Coche "
   "dos Oceanos, de 1716, ligados à embaixada portuguesa a Roma.",
   "<b>O edifício atual é de um arquiteto brasileiro vencedor do Pritzker.</b> O museu funciona num "
   "prédio de <b>Paulo Mendes da Rocha</b>, inaugurado em 2015 — o lugar que guarda os coches dos "
   "reis de Portugal foi desenhado por um paulistano."]),
 "Fatos históricos":"Fundado em <b>1905</b> por iniciativa da Rainha D. Amélia, para preservar a "
   "coleção de viaturas de gala da Casa Real. O espaço original era o <b>Picadeiro Real</b>, junto "
   "ao Palácio de Belém. Em <b>2015</b> o acervo principal mudou-se para o edifício novo, de Paulo "
   "Mendes da Rocha, e os dois espaços passaram a funcionar em conjunto — até o <b>Picadeiro fechar "
   "em 29 de setembro de 2025</b> para obras do PRR.<br>"
   +flag("Não encontrado")+" ficha de classificação patrimonial específica, nem para o museu nem "
   "para o edifício do Picadeiro, na base de Património Imóvel. Vale o contexto: um museu é uma "
   "instituição, não necessariamente um bem classificado — a classificação, quando existe, incide "
   "sobre o imóvel.",
 "Dias em que não funciona":"<b>Fecha às segundas-feiras</b>, mais 1 de janeiro, 1 de maio, "
   "domingo de Páscoa, 13 de junho e 25 de dezembro. Horário de terça a domingo, <b>10h às 18h</b>, "
   "sem diferença entre verão e inverno.<br>"
   "<b>Última entrada: </b>"+flag("não publicada")+" na página do museu. A página do Picadeiro Real "
   "publica “última entrada às 17h30”, e como os dois partilham horário é provável que "
   "valha o mesmo — <b>mas a fonte não diz isso para o museu, e por isso não afirmamos</b>.<br>"
   "<b>O Picadeiro Real está fechado desde 29 de setembro de 2025</b> para obras, e <b>a MMP não "
   "publica previsão de reabertura</b>. Se você planejava ver o salão histórico, não vai ver.<br>"
   "Repare ainda que este fecha às 18h, mais cedo que o Padrão no verão, e abre às 10h, mais tarde "
   "que Jerónimos e Torre. <b>E a segunda-feira em Belém é um problema geral:</b> Jerónimos, Torre e "
   "Coches fecham todos — só o Padrão abre.",
 "Pontos turísticos próximos":"Palácio de Belém, Picadeiro Real (fechado), Mosteiro dos Jerónimos, "
   "Pastéis de Belém, Padrão dos Descobrimentos, Torre de Belém, Museu de Marinha, Museu Nacional de "
   "Arqueologia (fechado), Jardim Botânico Tropical, MAAT, Centro Cultural de Belém e Doca de Belém. "
   +flag("Sem distância oficial")}
}]}
