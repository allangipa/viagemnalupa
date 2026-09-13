# -*- coding: utf-8 -*-
from lib import mapa, flag, ul

IPMA = ("Pelas normais de 30 anos do IPMA, estação Lisboa / Instituto Geofísico, série 1991–2020: "
  "<b>janeiro</b> é o mês mais frio, com média de 11,8 °C, máxima média de 15,1 °C e mínima média de "
  "8,6 °C, e ainda 103,8 mm de chuva. <b>Agosto</b> é o mais quente, com 23,8 °C de média, e "
  "<b>julho</b> o mais seco, com 2,6 mm no mês inteiro.")

G3 = {
 "titulo": "Museus, mercado e o elétrico",
 "intro": "O grupo onde as regras mudam mais depressa: o 28 não parte mais de onde todo guia diz, "
   "o Gulbenkian acabou de reabrir depois de quinze meses fechado, e o Oceanário cobra preços "
   "diferentes conforme a hora que você escolhe entrar.",
 "pontos": [
{
 "id":"eletrico-28","nome":"Elétrico 28","tag":"Transporte histórico","img":"tram28",
 "preco":"€ 1,72","preconota":"com cartão; € 3,30 pagando a bordo",
 "campos":{
 "Endereço":"<b>O ponto de partida mudou, e é o primeiro aviso desta ficha.</b> O terminal "
   "nominal é a Praça Martim Moniz, 1100-341 Lisboa — mas <b>desde 24 de agosto de 2026, às 8h, o "
   "elétrico não parte de lá</b>. O embarque real hoje é no <b>Largo da Graça</b>, no lado nascente, "
   "ao lado do Miradouro Sophia de Mello Breyner. A própria Carris já rotula a carreira como "
   "“Graça – Campo Ourique”. O outro terminal é Campo de Ourique, junto ao Cemitério "
   "dos Prazeres.<br>"
   "<b>Quando o serviço normalizar</b>, a paragem de Martim Moniz fica no lado da praça voltado para "
   "a Rua dos Cavaleiros — é onde se forma a fila, sempre visível, no sopé da colina do Castelo.<br>"
   "<b>O percurso clássico</b>, de 9 km e 35 paragens, vai de Martim Moniz à Graça, São Vicente de "
   "Fora, Alfama, Santa Luzia, Sé, Baixa, Chiado, Bica, Estrela e Campo de Ourique. "
   +flag("Extensão via fonte secundária")+" a Carris não publica esses dois números na página da "
   "carreira."+mapa("Elétrico 28 — Largo da Graça","Largo da Graca, Lisboa"),
 "Valor da entrada":"O 28 é transporte público: não tem bilheteira, tem tarifa. <b>E a diferença "
   "entre pagar a bordo e pagar com cartão é a maior armadilha de custo de Lisboa para o "
   "turista.</b> Tarifário Carris em vigor desde 1/jan/2026.<br>"
   "<b>A bordo, no elétrico: € 3,30</b> (≈ R$ 20). <b>Com zapping, o saldo em euros carregado no "
   "cartão: € 1,72</b> (≈ R$ 10), com uma hora de transbordo livre na rede. <b>É quase metade.</b><br>"
   "O cartão <b>Navegante Ocasional</b> custa <b>€ 0,50</b> uma única vez e vale um ano. Carrega-se "
   "saldo em euros, não viagens. <b>Se você vai andar de elétrico mais de uma vez, o cartão se paga "
   "na primeira viagem.</b><br>"
   "Outras opções: bilhete simples Carris/Metro carregado no cartão, € 1,90; passe de 24h "
   "Carris/Metro, € 7,25; com os barcos do Tejo, € 10,35; com comboio, € 11,40. <b>Preço fixo</b>, "
   "sem variação por hora ou procura.<br>"
   +flag("Não encontrado")+" tabela oficial de gratuidade por idade para o visitante ocasional — os "
   "descontos do sistema estão ligados a passes mensais com comprovação de residência em Portugal, e "
   "não fazem sentido para estada curta.<br>"
   "<b>Lisboa Card: viagem incluída.</b> O elétrico 28 entra no transporte gratuito do cartão.",
 "Pontos de referência":"<b>Em Martim Moniz:</b> a praça, a Rua da Palma e a Mouraria. <b>Ao longo "
   "da linha:</b> Miradouro da Graça, São Vicente de Fora, Panteão Nacional, Feira da Ladra, "
   "Miradouro de Santa Luzia, Portas do Sol, Sé de Lisboa, Baixa Pombalina, Chiado, Praça Luís de "
   "Camões, Elevador da Bica (fechado), Basílica e Jardim da Estrela, e o Cemitério dos Prazeres, no "
   "fim da linha.",
 "Metrô mais próximo":"<b>Martim Moniz — Linha Verde</b>, com saída direta na praça. "
   "<b>Baixa-Chiado — linhas Azul e Verde</b> serve o trecho central do percurso, e <b>Rossio — "
   "Linha Verde</b> fica a curta distância de Martim Moniz.<br>"
   "<b>O elétrico 12E partilha o troço Graça–Sé–Chiado</b> e costuma ir bem mais vazio: é a "
   "alternativa de quem quer o mesmo trajeto sem a fila. "+flag("Sem tempo a pé")+" a Carris não "
   "publica caminhadas entre estações de metro e paragens de elétrico.",
 "Visitantes por ano":flag("Não encontrado")+" a Carris <b>não publica número anual de passageiros "
   "por carreira</b>. Não existe, em fonte oficial, um “número de visitantes do elétrico "
   "28”. Procuramos na página institucional, nas notícias, nos tarifários e na página da "
   "própria carreira.",
 "Menor visitação e temperatura":"<b>Não existe série mensal de passageiros publicada para o "
   "28E.</b> "+flag("Sem dado mensal")+" Dizemos isso com todas as letras: qualquer ranking de "
   "“mês mais vazio do 28” que circula por aí não tem lastro em dado da Carris.<br>"
   +IPMA+"<br>"
   "<b>Leitura prática, e aqui o clima importa de um jeito específico:</b> o 28 é um carro de "
   "madeira sem aquecimento relevante, com janelas que os passageiros abrem. Em janeiro a viagem é "
   "fria e as vidraças embaçam, o que estraga justamente a foto que você foi fazer. Julho é o "
   "oposto — seco e limpo —, mas é quando a fila fica pior.",
 "Curiosidades":ul([
   "<b>A Carris foi fundada no Rio de Janeiro, não em Lisboa.</b> A Companhia Carris de Ferro de "
   "Lisboa nasceu em 18 de setembro de 1872, no Rio — está escrito na página de história da própria "
   "empresa.",
   "O elétrico de Lisboa começou puxado por animais: a primeira carreira abriu em 17 de novembro de "
   "1873 com tração animal, e a elétrica só entrou em serviço em 31 de agosto de 1901.",
   "Os carros que você vê são históricos por fora e modernos por dentro: a Carris concluiu em 1995 "
   "a modernização de 45 elétricos, mantendo o aspeto exterior e trocando a mecânica.",
   "O 28 é a única carreira que ainda usa três canais antigos — a linha Palma-Graça-São Vicente, a "
   "da Calçada de São Francisco e o canal do antigo Elevador da Estrela."]),
 "Fatos históricos":"A linha Rua da Conceição–Graça, matriz do percurso atual, foi inaugurada em "
   "<b>1906</b>. "+flag("Divergência registrada")+" é muito comum guias e blogues afirmarem que a "
   "carreira 28 foi criada em <b>1914</b> — <b>não conseguimos confirmar essa data em fonte oficial "
   "da Carris</b>, e a única data de origem que encontramos é 1906. Registramos a divergência em vez "
   "de escolher.<br>"
   "A operadora foi fundada em 1872, a eletrificação veio em 1901, e o material circulante é da "
   "série <b>Remodelado</b>, de 1995. A rede de elétricos encolheu drasticamente ao longo do século "
   "XX, e o 28 sobreviveu como carreira patrimonial <b>e como transporte real de moradores das "
   "colinas</b> — as duas coisas ao mesmo tempo, e é daí que vem boa parte do atrito com o turismo.<br>"
   "Os elevadores irmãos da Carris — Lavra de 1884, Glória de 1885, Bica de 1892 e o Santa Justa de "
   "1902 — foram classificados Monumento Nacional em 2002.",
 "Dias em que não funciona":"<b>Não há fecho semanal:</b> o 28E circula todos os dias, com partidas "
   "entre cerca de 6h e a meia-noite e frequência que varia de 5 a 15 minutos nas horas de maior "
   "procura.<br>"
   "<b>Mas o percurso está cortado agora, e isso derruba o passeio.</b> Desde 24 de agosto de 2026, "
   "o elétrico só circula entre <b>Graça e Prazeres</b>; o troço <b>Martim Moniz ↔ Graça é feito por "
   "autocarro</b>, por causa de um corte na Rua Forno do Tijolo. Há <b>integração tarifária no "
   "transbordo</b> — você não paga duas vezes —, feito no lado nascente do Largo da Graça. "
   +flag("Sem data de término")+" a Carris não publicou quando a alteração acaba. <b>Se o seu plano "
   "era pegar o 28 em Martim Moniz, ele não existe hoje: comece na Graça.</b><br>"
   "<b>Lotação:</b> o carro é pequeno. Em hora de ponta turística você viaja em pé e espremido, sem "
   "ver a rua — ou seja, paga para não ver o que veio ver.<br>"
   "<b>Greves:</b> houve greve geral em 3 de junho de 2026 com impacto no serviço. Em Portugal as "
   "greves são anunciadas com pré-aviso — confira o site da Carris na véspera.",
 "Pontos turísticos próximos":"Miradouro da Graça, Senhora do Monte, São Vicente de Fora, Panteão "
   "Nacional, Feira da Ladra, Castelo de São Jorge, Portas do Sol, Santa Luzia, Sé, Museu do Fado, "
   "Baixa Pombalina, Praça do Comércio, Chiado, Bairro Alto, Basílica da Estrela e Cemitério dos "
   "Prazeres. "+flag("Sem distância oficial")}
},
{
 "id":"gulbenkian","nome":"Museu Calouste Gulbenkian","tag":"Museu","img":"gulbenkian",
 "preco":"€ 16","preconota":"reabriu em julho de 2026",
 "campos":{
 "Endereço":"Av. de Berna, 45A, 1067-001 Lisboa. <b>Não é um prédio de rua com fachada de "
   "museu:</b> é um conjunto modernista de betão implantado dentro de um parque arborizado de 9 "
   "hectares, ocupando um quarteirão inteiro na zona de São Sebastião. A entrada do museu, com a "
   "Coleção do Fundador, é pela Av. de Berna. O <b>CAM — Centro de Arte Moderna</b> tem entrada "
   "própria, pela Rua Dr. Nicolau de Bettencourt, dentro do mesmo jardim: os dois edifícios ficam em "
   "pontas opostas do parque."+mapa("Museu Calouste Gulbenkian","Museu Calouste Gulbenkian, Av. de Berna 45A, Lisboa"),
 "Valor da entrada":"<b>O museu reabriu.</b> A Coleção do Fundador esteve fechada cerca de quinze "
   "meses, de 18 de março de 2025 a <b>18 de julho de 2026</b>. Quem viajou a Lisboa nesse intervalo "
   "não conseguiu vê-la. Agora consegue.<br>"
   "Tabela oficial, consultada em 13/set/2026: <b>Museu € 16</b> (≈ R$ 95), e a página oficial "
   "indica que esse bilhete <b>já inclui a entrada na coleção do CAM</b>. <b>All Inclusive, museu "
   "mais CAM: € 18.</b> Só CAM: € 12. Só as temporárias do CAM: € 8.<br>"
   "<b>Descontos:</b> menores de 30 anos, 25%; maiores de 65, 10%; <b>Lisboa Card, 20%</b>. Com o "
   "<b>Cartão Gulbenkian, que é de adesão gratuita</b>, os menores de 30 pagam metade, os maiores de "
   "65 têm 20% e a faixa dos 30 aos 64 tem 10%. <b>Vale a pena aderir antes de comprar.</b><br>"
   "<b>Gratuito aos domingos a partir das 14h</b>, e sempre para <b>menores de 18 anos</b>, membros "
   "de ICOM, AICA e APOM, cartão de imprensa e acompanhantes de pessoas com deficiência. Não há "
   "faixa intermediária de criança: é grátis até aos 18 e, a partir daí, entra-se no desconto de "
   "menores de 30.<br>"
   +flag("Não encontrado")+" bilhete de família, valores de grupo e desconto por residência em "
   "Portugal — os descontos são por idade, cartão e parceria, não por morada.<br>"
   "<b>Preço fixo</b>, sem variação por data ou hora — o oposto do Oceanário.<br>"
   "<b>Lisboa Card: só 20% de desconto, não é entrada livre.</b> Atenção: sites revendedores do "
   "cartão ainda listavam o Gulbenkian como “temporariamente encerrado”, informação "
   "vencida desde julho.",
 "Pontos de referência":"O jardim da própria Fundação, com 9 hectares e entrada livre. A Praça de "
   "Espanha e o El Corte Inglés. O Parque Eduardo VII e a Estufa Fria. A Praça Marquês de Pombal. O "
   "Campo Pequeno e a Av. da República.",
 "Metrô mais próximo":"<b>São Sebastião — linhas Azul e Vermelha</b>, que é estação de interface "
   "entre as duas. Também serve <b>Praça de Espanha — Linha Azul</b>. <b>Autocarros 716, 726 e "
   "756</b> param na Av. de Berna; 746, 713 e 742 servem a zona.<br>"
   "<b>De comboio:</b> estação de Entrecampos, que a própria Fundação indica estar a <b>cerca de 15 "
   "minutos a pé</b> — e este é um dos raros casos em Lisboa em que a fonte oficial publica um tempo "
   "de caminhada, por isso o reproduzimos.<br>"
   "Há estações de bicicleta compartilhada nas imediações e parque pago com acesso pela Av. de Berna.",
 "Visitantes por ano":"<b>Mais de 640 mil visitas em 2024</b>, somando museu, CAM e exposições "
   "temporárias. Fonte: Relatório e Contas 2024 da própria Fundação. O CAM reabriu em 21 de setembro "
   "de 2024 e fez mais de 111 mil visitantes em pouco mais de três meses.<br>"
   +flag("Número agregado")+" a Fundação <b>não desagrega</b> quantos foram especificamente à "
   "Coleção do Fundador — não existe, em fonte oficial, um número isolado do Museu Gulbenkian.<br>"
   "<b>E há uma ressalva de leitura que vale para os próximos anos:</b> como a Coleção do Fundador "
   "esteve fechada de março de 2025 a julho de 2026, os números de 2025 e 2026 <b>não serão "
   "comparáveis</b> com 2024. Qualquer comparação direta seria enganosa.",
 "Menor visitação e temperatura":"<b>A Fundação não publica série mensal de visitantes.</b> "
   +flag("Sem dado mensal")+" Conferimos o Relatório e Contas: há o agregado anual, não há quadro "
   "mês a mês.<br>"+IPMA+"<br>"
   "<b>Aqui o frio joga a seu favor.</b> O Gulbenkian é coberto e climatizado — e a renovação de "
   "2025 e 2026 incluiu justamente climatização otimizada. Janeiro é o mês em que o jardim está "
   "menos convidativo, mas as galerias ficam confortáveis e vazias. Para o jardim, que é um dos "
   "melhores ativos da Fundação, a janela boa é de abril a outubro.<br>"
   "<b>E uma armadilha:</b> se o seu objetivo é o museu vazio, <b>evite domingo depois das 14h</b> — "
   "é exatamente o horário gratuito, e portanto o mais cheio da semana.",
 "Curiosidades":ul([
   "A coleção tem cerca de <b>seis mil obras</b>, mas só umas centenas ficam expostas — a primeira "
   "montagem, de 1965, mostrava cerca de 300 peças.",
   "O testamento que criou tudo foi assinado em Lisboa, em 18 de junho de 1953. Em 2026 a Fundação "
   "completa 70 anos.",
   "O edifício e o parque são Monumento Nacional desde 2010.",
   "<b>A reabertura de 2026 foi uma viagem ao passado, não uma modernização.</b> A renovação "
   "recuperou de propósito o desenho original dos anos 1960 a partir de estudo de arquivo — "
   "incluindo repor a alcatifa esverdeada nas galerias de arte europeia e reposicionar o "
   "baixo-relevo assírio."]),
 "Fatos históricos":"A Fundação foi instituída por testamento de <b>Calouste Sarkis Gulbenkian</b>, "
   "assinado em 18 de junho de 1953. A primeira mostra pública da coleção foi em <b>20 de julho de "
   "1965</b>, e a instalação permanente no museu atual é de <b>1969</b>, com projeto de <b>Ruy Jervis "
   "d'Athouguia, Alberto Pessoa e Pedro Cid</b>. O jardim de 9 hectares é de <b>António Viana "
   "Barreto</b> e <b>Gonçalo Ribeiro Telles</b>.<br>"
   "A renovação de 2025–2026 foi do arquiteto francês <b>Frédéric Ladonne</b> com a arquiteta "
   "<b>Teresa Nunes da Ponte</b>, e trouxe novas vitrinas, melhor iluminação, climatização, "
   "recuperação dos materiais originais, nova sala de numismática, sala Lalique redesenhada e "
   "reintrodução de obras das reservas. A reabertura, em 18 de julho de 2026, teve <b>nove dias de "
   "entrada gratuita</b>.",
 "Dias em que não funciona":"<b>Fecha às terças-feiras</b> — é o erro clássico de quem monta "
   "roteiro em Lisboa. Fecha também em 1 de janeiro, domingo de Páscoa, 1 de maio, 24 e 25 de "
   "dezembro.<br>"
   "<b>Dias úteis das 10h às 18h. Sábados das 10h às 21h</b> — é a única noite da semana em que dá "
   "para ver a coleção com luz artificial e menos gente do que no domingo gratuito. <b>Última "
   "entrada 30 minutos antes do fecho.</b><br>"
   "<b>O jardim é outra história:</b> aberto todos os dias, do nascer ao pôr do sol, com entrada "
   "livre. Ou seja, <b>numa terça-feira você ainda pode entrar no parque</b> — só não nas galerias.",
 "Pontos turísticos próximos":"CAM — Centro de Arte Moderna, no mesmo campus. O jardim da Fundação. "
   "Parque Eduardo VII e Estufa Fria. Praça Marquês de Pombal e Avenida da Liberdade. Praça de "
   "Espanha, Culturgest, Campo Pequeno e a Casa-Museu Dr. Anastácio Gonçalves. "
   +flag("Sem distância oficial")}
},
{
 "id":"oceanario","nome":"Oceanário de Lisboa","tag":"Aquário","img":"oceanario",
 "preco":"€ 25 a € 29","preconota":"o preço muda conforme a hora",
 "campos":{
 "Endereço":"Esplanada Dom Carlos I, s/nº, 1990-005 Lisboa — na Doca dos Olivais, no Parque das "
   "Nações. "+flag("Ressalva de fonte")+" o logradouro e o código postal completos <b>não aparecem "
   "em destaque</b> na página oficial de visita; foram confirmados por registos de morada, e "
   "registramos essa fragilidade em vez de apresentá-los como se viessem do site.<br>"
   "<b>Como achar:</b> o Oceanário fica <b>sobre a água</b>, num edifício que parece uma plataforma "
   "ancorada, ligado à terra por um passadiço. Saindo da Estação do Oriente, atravesse o Centro "
   "Comercial Vasco da Gama e siga em direção ao rio. É impossível confundir: nenhum outro prédio "
   "ali está dentro da água."+mapa("Oceanário de Lisboa","Oceanario de Lisboa, Parque das Nacoes, Lisboa"),
 "Valor da entrada":"<b>O preço é dinâmico por faixa horária, e quase nenhum guia brasileiro "
   "explica isso.</b> Fonte: site oficial, consultado em 13/set/2026.<br>"
   "<b>Adulto de 13 a 64 anos:</b> € 29 entrando entre 10h e 11h30; <b>€ 27</b> entre 12h e 15h30; "
   "<b>€ 25</b> entre 16h e 18h30. <b>Criança de 3 a 12:</b> € 17, € 16 e € 15 nas mesmas faixas. "
   "<b>Sénior a partir de 65:</b> € 19, € 18 e € 17. <b>Até 2 anos é grátis.</b><br>"
   "<b>A diferença entre a pior e a melhor faixa é de € 4 por adulto.</b> Para uma família de dois "
   "adultos e duas crianças: € 92 às 10h contra € 80 às 16h — <b>€ 12 de diferença</b>, cerca de "
   "R$ 71, só por escolher a hora.<br>"
   "<b>FlexiTicket: € 41</b> por adulto, sem data e hora fixas, válido para uma visita dentro de 7 "
   "dias. É o bilhete de quem não quer se comprometer — custa € 16 a mais que o melhor horário.<br>"
   "Há <b>5% de desconto na compra online</b> com código promocional.<br>"
   "<b>Gratuito</b> para menores de 2 anos e para visitantes com deficiência certificada de 60% ou "
   "superior, cujo acompanhante tem 60% de desconto. "+flag("Não existe")+" dia gratuito — o que "
   "existe é a faixa das 16h, que é a mais barata. "+flag("Não encontrado")+" bilhete de família, "
   "preçário de grupo ou desconto por residência.<br>"
   "<b>Lisboa Card: só desconto, não é entrada livre.</b> O desconto divulgado é de 15%, mas "
   +flag("não confirmado em fonte primária")+" — esse número não aparece nem no site do Oceanário "
   "nem no do Turismo de Lisboa, vem de páginas comerciais. <b>O que é seguro afirmar: o Oceanário "
   "não está entre as entradas gratuitas do cartão.</b>",
 "Pontos de referência":"Todo o Parque das Nações: a Doca dos Olivais, o Centro Comercial Vasco da "
   "Gama, a Estação do Oriente projetada por Santiago Calatrava, a Torre Vasco da Gama, a Ponte "
   "Vasco da Gama, o Pavilhão de Portugal de Álvaro Siza, a Altice Arena, o Pavilhão do Conhecimento "
   "e o teleférico sobre o rio.",
 "Metrô mais próximo":"<b>Oriente — Linha Vermelha</b>, indicada pelo próprio Oceanário. A estação "
   "é também estação ferroviária da CP, com ligações urbanas, regionais e de longo curso — é um dos "
   "maiores interfaces de transporte de Portugal. <b>Autocarros 705, 708, 725, 728, 744, 750, 759, "
   "782 e 794.</b><br>"
   "Há cinco parques de estacionamento nas imediações, somando mais de 4.000 lugares, e o Oceanário "
   "informa manter percurso acessível entre o edifício e os dois parques mais próximos. "
   +flag("Sem tempo a pé")+" o site não publica a caminhada da Estação do Oriente.<br>"
   "<b>Duração da visita, pelo próprio Oceanário: 1h30 a 2h.</b>",
 "Visitantes por ano":"<b>1.467.580 visitantes em 2024</b>, alta de 6% sobre os 1.383.747 de 2023. "
   "Desse total, <b>806.314 estrangeiros e 661.266 portugueses</b>. Fonte: Relatório e Contas 2024 "
   "do próprio Oceanário — documento de prestação de contas, a fonte mais forte possível.<br>"
   "<b>Repare que mais de 45% dos visitantes são portugueses:</b> o Oceanário não é só atração de "
   "turista, é programa de família local.",
 "Menor visitação e temperatura":"<b>O Oceanário não publica série mensal de visitantes.</b> "
   +flag("Sem dado mensal")+" Conferimos o Relatório e Contas: há uma secção “mês a "
   "mês”, mas ela lista eventos e atividades, <b>sem números de visitação por período</b>.<br>"
   "<b>Uma pista, apresentada como pista e não como dado:</b> o relatório menciona campanhas "
   "comerciais concentradas em meses específicos, e há uma promoção de fim de verão em curso — o que "
   "sugere esforço de enchimento em épocas mais fracas. É inferência editorial, e está rotulada "
   "como tal.<br>"+IPMA+"<br>"
   "<b>Leitura prática:</b> o Oceanário é 100% coberto, então janeiro é excelente para o aquário — e "
   "péssimo para o passeio ao ar livre pela doca, que é metade da graça de ir até lá. Naquela zona o "
   "vento do Tejo é forte.",
 "Curiosidades":ul([
   "<b>O tanque central tem 5 milhões de litros</b>, num total de 7,5 milhões no edifício inteiro. A "
   "ideia arquitetónica é que os quatro habitats — Atlântico Norte, Antártico, Pacífico temperado e "
   "Índico tropical — parecem separados, mas são um único oceano contínuo.",
   "São mais de 8.000 organismos de cerca de 500 espécies, em mais de 30 aquários e 20.000 m².",
   "Foi eleito o melhor aquário do mundo pelo Tripadvisor duas vezes, em 2015 e em 2017.",
   "O edifício foi desenhado para parecer um navio ancorado — o arquiteto buscou uma estética "
   "ambígua, entre ilha e navio pronto a zarpar."]),
 "Fatos históricos":"Inaugurado em <b>22 de maio de 1998</b> como pavilhão temático da <b>Expo'98</b>, "
   "cujo tema foi “Os Oceanos, um Património para o Futuro”, e aberto "
   "permanentemente ao público em outubro do mesmo ano, depois de terminada a exposição mundial. "
   "Arquiteto: <b>Peter Chermayeff</b>, do escritório norte-americano Cambridge Seven Associates.<br>"
   "Um segundo edifício, o <b>Edifício do Mar</b>, abriu em 2011, com arquitetura de Pedro Campos "
   "Costa, acrescentando exposições temporárias, restaurante e auditório. A exposição temporária "
   "<b>“Florestas Submersas”, do aquapaisagista japonês Takashi Amano</b> — o maior "
   "aquário de água doce de plantas naturais do mundo — ficou em cartaz cerca de uma década, até "
   "2026. A atual é <b>“Monstros Marinhos”</b>, com modelos em tamanho real de gigantes "
   "marinhos antigos.",
 "Dias em que não funciona":"<b>Abre todos os dias do ano.</b> Não há fecho semanal e não há "
   "feriado de encerramento — o que é raro em Lisboa e é o grande trunfo logístico deste ponto: "
   "<b>é o plano B perfeito para uma terça-feira</b>, quando o Gulbenkian fecha, ou para o 1º de "
   "janeiro.<br>"
   "<b>Horário normal das 10h às 20h, com última entrada às 19h.</b> Em 24 e 31 de dezembro, das 10h "
   "às 19h com última entrada às 18h; em 25 de dezembro e 1 de janeiro, das 11h às 20h.<br>"
   "<b>O bilhete tem hora marcada:</b> você compra uma faixa horária e ela vale. Chegar fora da sua "
   "faixa é problema — o bilhete é vinculado ao horário. Quem quer liberdade compra o FlexiTicket.<br>"
   "<b>E atenção à conta do tempo:</b> a última entrada é às 19h, não às 20h. Como a visita leva "
   "1h30 a 2h pelos cálculos do próprio Oceanário, entrar às 19h significa visita apertada até o "
   "fecho.",
 "Pontos turísticos próximos":"Pavilhão do Conhecimento, teleférico do Parque das Nações, Torre "
   "Vasco da Gama, Ponte Vasco da Gama, Jardim Garcia de Orta, o passeio ribeirinho, a Estação do "
   "Oriente, o Pavilhão de Portugal, a Altice Arena e o Casino Lisboa. "+flag("Sem distância oficial")}
},
{
 "id":"time-out-market","nome":"Time Out Market","tag":"Mercado","img":"timeout",
 "preco":"Grátis","preconota":"entrar; prato de € 6,50 a € 18,40",
 "campos":{
 "Endereço":"Mercado da Ribeira, Av. 24 de Julho, 1200-479 Lisboa. É o grande edifício de mercado "
   "<b>com cúpula, em frente à Estação de Cais do Sodré</b>, na esquina com a Praça Dom Luís I. "
   "Saindo do metro ou do comboio, o mercado está literalmente do outro lado da rua — procure a "
   "cúpula.<br>"
   "<b>Metade do edifício continua a ser mercado tradicional</b> de peixe, fruta e legumes; a metade "
   "do Time Out é a das mesas comunitárias."+mapa("Time Out Market Lisboa","Time Out Market, Mercado da Ribeira, Av. 24 de Julho, Lisboa"),
 "Valor da entrada":"<b>Não cobra entrada.</b> É mercado público de acesso livre — nenhuma das "
   "páginas oficiais menciona bilhete, taxa ou consumação mínima. Por consequência não há faixas "
   "etárias, bilhete de família, grupos, dia gratuito nem desconto de residente, e <b>o Lisboa Card "
   "não dá “entrada livre” aqui porque não há entrada a pagar</b>.<br>"
   "<b>Então a pergunta útil não é quanto custa entrar, é quanto custa comer</b> — e aqui está, com "
   "fonte na página oficial de restaurantes, consultada em 13/set/2026.<br>"
   "<b>A faixa real de um prato vai de € 6,50 a € 18,40</b> (≈ R$ 39 a R$ 109), fora a churrascada "
   "de marisco para dois, a € 45. <b>O núcleo, onde está a maioria dos pratos de refeição, é de "
   "€ 12,50 a € 15,50.</b><br>"
   "<b>O melhor custo-benefício que encontramos:</b> o <b>prato do dia da chef Marlene Vieira, a "
   "€ 14,50 já com bebida e sobremesa</b>. Um prato isolado do Henrique Sá Pessoa, que tem duas "
   "estrelas Michelin, custa praticamente o mesmo — sem bebida nem sobremesa.<br>"
   "<b>O mais barato que enche:</b> sandes de croquete a € 6,50, ou hambúrguer a partir de € 8,95. E "
   "o <b>pastel de nata da Manteigaria sai a € 1</b>, ou € 6 a caixa de seis.<br>"
   "<b>Aviso de orçamento honesto:</b> os preços acima são por prato, sem bebida. Uma refeição "
   "completa com bebida fica acima de € 18 a € 20 por pessoa; para um casal, conte a partir de "
   "€ 40. <b>O Time Out Market não é o lugar barato de Lisboa</b> — é uma vitrine de chefs em "
   "formato de praça de alimentação, e o preço reflete isso. Uma tasca de bairro em Campo de Ourique "
   "ou na Graça serve prato do dia por metade.",
 "Pontos de referência":"A Estação de Cais do Sodré, com metro, comboio e cacilheiros. A Praça Dom "
   "Luís I. A Ribeira das Naus, caminhando para o Cais das Colunas e a Praça do Comércio. A Rua Nova "
   "do Carvalho, a “Rua Cor-de-Rosa”. O mercado tradicional, no mesmo edifício. E o "
   "Elevador da Bica, que sobe para o Bairro Alto — atualmente fechado.",
 "Metrô mais próximo":"<b>Cais do Sodré — Linha Verde</b>, o terminal sul da linha. <b>Confirmado "
   "operacional:</b> a estação esteve fechada de 8 a 26 de agosto de 2026, para obras de sinalização "
   "da futura Linha Circular, e <b>reabriu em 27 de agosto</b>, com a Linha Verde em circulação "
   "normal.<br>"
   "<b>Comboio:</b> Estação de Cais do Sodré, Linha de Cascais, com ligações para Belém, Algés, "
   "Oeiras, Estoril e Cascais. <b>Barco:</b> terminal fluvial no mesmo lugar, com ligações à margem "
   "sul. <b>Elétricos 15E, 25E e 18E</b> servem a zona.<br>"
   +flag("Sem tempo a pé")+" as fontes não publicam. O que dá para dizer sem estimar: o mercado e a "
   "estação estão em lados opostos da mesma avenida.",
 "Visitantes por ano":flag("Não encontrado")+" em fonte oficial atual. Os únicos números que "
   "localizamos são <b>antigos e de fonte secundária</b>: pouco mais de 3 milhões de visitantes em "
   "2016 e perto de 4 milhões em 2018 — dados com oito e dez anos de defasagem, que <b>não devem ser "
   "apresentados como número atual</b>. Procuramos no site oficial em português e em inglês, na "
   "página de eventos, em relatórios do grupo e na Câmara Municipal, que é a concedente do mercado.",
 "Menor visitação e temperatura":"<b>Não existe série mensal</b> — e nem sequer um número anual "
   "recente, quanto mais uma quebra por mês. "+flag("Sem dado mensal")+"<br>"+IPMA+"<br>"
   "<b>Mas aqui o clima tem efeito direto e mensurável no seu conforto, mesmo sem série de "
   "visitação.</b> O mercado tem <b>500 lugares interiores e 250 exteriores</b>. Em janeiro, com "
   "103,8 mm de chuva e mínimas de 8,6 °C, <b>os 250 lugares de fora saem de jogo</b>: a capacidade "
   "útil cai um terço e todo mundo se comprime dentro. Ou seja — <b>num janeiro chuvoso o mercado "
   "pode parecer mais cheio do que num julho seco</b>, mesmo com menos gente na cidade. É um efeito "
   "contraintuitivo que vale planear.",
 "Curiosidades":ul([
   "<b>O mercado é de 1882; o Time Out é um inquilino recente.</b> O Mercado da Ribeira abriu em 1º "
   "de janeiro de 1882, e o Time Out só chegou em 2014.",
   "Um incêndio destruiu metade do mercado onze anos depois de inaugurado, em 7 de junho de 1893.",
   "<b>Metade do edifício ainda é mercado de verdade.</b> Você pode almoçar num balcão de chef com "
   "estrela Michelin e, a vinte metros, ver alguém comprar carapau.",
   "O conceito nasceu aqui e foi exportado para o mundo: o Time Out Market Lisboa abriu em maio de "
   "2014 como o primeiro do gênero, e o modelo foi depois replicado em Londres, Nova Iorque e "
   "outras cidades."]),
 "Fatos históricos":"Mercado inaugurado em <b>1º de janeiro de 1882</b>, com incêndio em 1893 que "
   "destruiu o lado nascente. Em 2000 abandonou o comércio grossista; em 2001 ganhou o novo piso "
   "superior. A <b>Câmara Municipal de Lisboa atribuiu a exploração ao Time Out em 2010</b>, por "
   "concurso público, e o <b>Time Out Market abriu em 18 de maio de 2014</b>, com 30 restaurantes, "
   "3.000 m² e 750 lugares sentados. Hoje o site oficial descreve 26 restaurantes, 8 bares, 6 "
   "quiosques e 5 lojas, mais uma escola de cozinha e um espaço de eventos. Em 2026 completa 12 anos.<br>"
   +flag("Não encontrado")+" o arquiteto do projeto original de 1882 — nem as fontes oficiais nem "
   "as secundárias o identificam. E "+flag("fonte secundária")+" a cronologia acima: nem a Câmara "
   "nem o Time Out publicam histórico equivalente.",
 "Dias em que não funciona":"<b>Não fecha. Abre todos os dias</b>, e nenhuma fonte oficial indica "
   "dia de encerramento semanal.<br>"
   "<b>Mas as duas páginas oficiais do próprio Time Out divergem no horário, e a diferença é "
   "material.</b> A internacional publica <b>domingo a quarta das 10h à meia-noite e quinta a sábado "
   "das 10h às 2h</b>; a portuguesa publica <b>todos os dias das 10h à meia-noite</b>. São duas horas "
   "a mais nas noites de quinta, sexta e sábado, segundo uma delas. "+flag("Divergência não resolvida")+
   " <b>Se o seu plano depende de estar no mercado depois da meia-noite, assuma o horário mais "
   "restritivo e confirme no dia.</b> Não monte uma ceia de uma da manhã com base numa fonte que a "
   "outra fonte da mesma empresa contradiz.<br>"
   "<b>Não há reservas:</b> o modelo é de mesas comunitárias por ordem de chegada, e você não pode "
   "garantir lugar antecipadamente. <b>E cada banca tem o seu próprio horário de cozinha, que fecha "
   "antes do mercado</b> — o mercado pode estar aberto e a cozinha que você queria, fechada.<br>"
   "Há caixas eletrônicos no local, wi-fi, e aceita-se dinheiro e cartão.",
 "Pontos turísticos próximos":"Cais do Sodré, Ribeira das Naus, Praça do Comércio e Cais das "
   "Colunas, Arco da Rua Augusta, a Rua Cor-de-Rosa, Elevador da Bica (fechado), Bairro Alto, "
   "Chiado, Praça Luís de Camões e o Museu da Marioneta. "+flag("Sem distância oficial")}
}]}
