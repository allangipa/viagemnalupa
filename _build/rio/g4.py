# -*- coding: utf-8 -*-
from lib import mapa, flag, ul

G4 = {
 "titulo": "Bairros e esporte",
 "intro": "A parte do Rio que não cabe em cartão-postal: uma escadaria feita por um chileno, um "
   "bonde de 130 anos que passa por cima de um aqueduto de 1750, e o estádio cujo horário depende "
   "da tabela do Brasileirão.",
 "pontos": [
{
 "id":"escadaria-selaron","nome":"Escadaria Selarón","tag":"Obra de arte urbana","img":"selaron",
 "preco":"Grátis","preconota":"rua pública tombada, sem bilheteria",
 "campos":{
 "Endereço":"Rua Joaquim Silva, s/nº — Lapa. A escadaria liga a Rua Joaquim Silva, na Lapa, à Rua "
   "Pinto Martins, já em Santa Teresa. A Riotur informa que fica <b>a cinco minutos a pé dos Arcos "
   "da Lapa</b>: desça a Rua Joaquim Silva a partir da Av. Mem de Sá e a escadaria nasce no fim da "
   "rua. A Sala Cecília Meireles e a Rua Visconde de Maranguape — onde a Prefeitura construiu a baia "
   "de embarque de vans e ônibus turísticos — são as referências imediatas."
   +mapa("Escadaria Selarón","Escadaria Selarón, Rua Joaquim Silva, Lapa, Rio de Janeiro"),
 "Valor da entrada":"<b>Gratuito.</b> A escadaria é rua pública, tombada como patrimônio: não há "
   "bilheteria, catraca nem taxa de espécie alguma, e a Riotur não lista preço nem horário. "+flag("Não encontrado")+" "
   "qualquer ato normativo da Prefeitura instituindo cobrança — procuramos em riotur.rio, "
   "prefeitura.rio e infraestrutura.prefeitura.rio.<br>"
   "<b>Atenção:</b> há vendedores e pessoas oferecendo serviço de guia ou de foto no local. É "
   "atividade particular, não ingresso — ninguém precisa pagar para subir os degraus.",
 "Pontos de referência":"Arcos da Lapa, a cinco minutos. Sala Cecília Meireles, contígua, na Rua "
   "Visconde de Maranguape. Rua Teotônio Regadas. Todos eles estão no eixo do <b>Boulevard "
   "Selarón</b>, obra de R$ 1,7 milhão iniciada em julho de 2026, com 227 m de novo pavimento e "
   "114 m de calçada requalificada.",
 "Metrô mais próximo":"<b>Cinelândia — Linhas 1 e 2.</b> O MetrôRio orienta expressamente descer "
   "em Cinelândia para chegar à Lapa. "+flag("Sem tempo oficial")+" o MetrôRio não publica a "
   "caminhada de Cinelândia até a escadaria nem até os Arcos. O VLT Carioca também serve a "
   "Cinelândia, mas não localizamos página da concessionária listando o ponto.",
 "Visitantes por ano":"<b>Mais de 1,5 milhão de visitantes por ano</b>, número divulgado pela "
   "<b>Prefeitura do Rio em 3/jul/2026</b>, no lançamento do Boulevard Selarón. É apontada como o "
   "<b>terceiro ponto turístico mais visitado do Rio</b>, atrás do Pão de Açúcar e do Corcovado. "
   "O prefeito Eduardo Cavaliere declarou na ocasião que a escadaria “se tornou tão procurada "
   "nas redes sociais quanto o Cristo Redentor”. "+flag("Sem série histórica")+" não há "
   "contagem ano a ano — é espaço aberto, sem catraca.",
 "Menor visitação e temperatura":flag("Não existe medição")+" nem a Prefeitura, nem a Riotur, nem "
   "o Data.Rio contam visitantes da escadaria.<br>"
   "Pelo clima do município, os meses mais frios e secos são junho (16 °C a 25 °C, 38 mm), julho "
   "(15 °C a 25 °C, 37 mm) e agosto (16 °C a 26 °C, 35 mm); os mais quentes e chuvosos são janeiro e "
   "fevereiro, a 22 °C e 31 °C (Climatempo). Como referência de fluxo, o Rio recebeu "
   "<b>1.211.748 turistas internacionais de janeiro a maio de 2026</b>, alta de 17% sobre 2025, "
   "segundo dados da Polícia Federal divulgados pelo Ministério do Turismo. "+flag("Sem série mensal")+
   " a série mês a mês que permitiria apontar o mês mais vazio não está publicada.",
 "Curiosidades":ul([
   "Selarón pintou à mão cerca de 300 azulejos com a imagem de uma mulher africana grávida, motivo "
   "que se repete por toda a escadaria.",
   "Os azulejos vieram de mais de 60 países, em boa parte doados por visitantes, além de sobras de "
   "obra e entulho urbano.",
   "Em 2006, Snoop Dogg e Pharrell Williams gravaram ali o clipe de <i>Beautiful</i>.",
   "Painéis de mosaico assinados por Selarón também existem nos Arcos da Lapa, e foram preservados "
   "na restauração municipal de 2022."]),
 "Fatos históricos":"O autor é <b>Jorge Selarón</b>, pintor e ceramista <b>chileno</b> radicado no "
   "Rio, morador da Lapa. Começou em <b>1990</b>, reformando por conta própria a escadaria degradada "
   "em frente à sua casa, e nunca parou: “este sonho louco e único só terminará no dia da "
   "minha morte”, dizia. Foi encontrado morto na própria escadaria em <b>janeiro de 2013, aos "
   "65 anos</b>; a causa permanece objeto de versões conflitantes e "+flag("não localizamos")+" a "
   "conclusão oficial da investigação em fonte primária. Selarón recebeu o título de cidadão "
   "honorário do Rio de Janeiro.<br>"
   "<b>Tombamento:</b> "+flag("duas datas em circulação")+" maio de 2005, segundo parte da imprensa, "
   "e a <b>Lei municipal 5.297</b>, publicada e noticiada em agosto de 2015. Não localizamos a ficha "
   "do bem no IRPH para conciliar as duas.<br>"
   "<b>Número de degraus:</b> "+flag("fontes divergem")+" 215 em uma, 250 degraus e 125 metros em "
   "outra, e <b>não há número oficial da Prefeitura</b>. As fontes convergem em “mais de "
   "2.000 azulejos”. Ficamos com <b>mais de 200 degraus</b>.<br>"
   "<b>O que mudou em 2026:</b> a Prefeitura iniciou em julho o Boulevard Selarón e criou o "
   "<b>Distrito de Arte e Cultura da Lapa</b>, abrangendo Lapa, Glória e Santa Teresa.",
 "Dias em que não funciona":"<b>Nenhum.</b> Logradouro público, sem portão e sem horário — a "
   "Riotur não publica horário de funcionamento.<br>"
   "<b>Ressalva de 2026:</b> as obras do Boulevard Selarón podem gerar interdições parciais no "
   "entorno. "+flag("Não encontrado")+" calendário de interdição publicado.",
 "Pontos turísticos próximos":"<b>Arcos da Lapa, a 5 minutos a pé</b> — este é dado oficial da "
   "Riotur, um dos poucos tempos a pé publicados no Rio. Sala Cecília Meireles, contígua. E Santa "
   "Teresa: a escadaria desemboca na Rua Pinto Martins, já dentro do bairro. "
   +flag("Sem distância oficial")+" para os demais."}
},
{
 "id":"santa-teresa-bonde","nome":"Santa Teresa e o bonde","tag":"Bairro e transporte histórico","img":"bonde",
 "preco":"R$ 20","preconota":"ida e volta no mesmo dia",
 "campos":{
 "Endereço":"Embarque na <b>Estação Carioca</b>, oficialmente Estação Motorneiro Nelson Corrêa da "
   "Silva, no <b>Largo da Carioca, no fim da Rua Lélio Gama</b>, Centro. Para achar: saia do metrô "
   "na Estação Carioca, caminhe em direção ao edifício-sede da Petrobras, na Avenida Chile, e ao "
   "chegar ao prédio entre na Rua Lélio Gama — a estação está no fim dela."
   +mapa("Bonde de Santa Teresa","Estação Carioca do Bonde de Santa Teresa, Largo da Carioca, Rio de Janeiro"),
 "Valor da entrada":"<b>Tarifa única R$ 20</b> (≈ US$ 4), e ela <b>inclui ida e volta</b> — um "
   "embarque em cada sentido no mesmo dia. <b>Gratuito</b> para moradores de Santa Teresa "
   "previamente cadastrados (limitados a 6 assentos por veículo), estudantes de escola pública "
   "uniformizados e com carteirinha, idosos a partir de 65 anos e portadores do Vale Social.<br>"
   "Fonte: anúncio da Secretaria de Estado de Transporte e Mobilidade Urbana, de março de 2025, com "
   "vigência reafirmada em reportagem de 1/set/2026, pelos 130 anos do bonde. A tarifa de R$ 20 foi "
   "instituída em novembro de 2016. "+flag("Sem tabela em site oficial")+" as páginas de tarifa e "
   "horário do governo estadual não estavam acessíveis na apuração; os valores vêm de imprensa "
   "especializada reproduzindo o anúncio oficial.",
 "Pontos de referência":"No embarque: Largo da Carioca, edifício da Petrobras na Av. Chile, "
   "Catedral Metropolitana e a Rua Lélio Gama. <b>No trajeto, o bonde atravessa os Arcos da Lapa</b> "
   "— é o único transporte que circula sobre o aqueduto desde 1896. No bairro: Largo dos Guimarães, "
   "Largo das Neves, Largo da França e o Curvelo.",
 "Metrô mais próximo":"<b>Carioca — Linhas 1 e 2</b>, a estação de baldeação do Centro, no mesmo "
   "largo da estação do bonde. O percurso é Largo da Carioca → Av. Chile → Rua Lélio Gama, de poucos "
   "quarteirões. "+flag("Sem tempo oficial")+" nem o MetrôRio nem a Setram publicam a caminhada. O "
   "VLT também atende a região da Carioca e da Cinelândia.",
 "Visitantes por ano":"<b>702.768 passageiros em 2025</b>, cerca de 23% acima de 2024 — dado do "
   "<b>Data.Rio</b>, da Prefeitura do Rio, que mantém série histórica desde 1990. No parcial de "
   "janeiro a agosto de 2025 foram 473.456 passageiros contra 357.953 no mesmo período de 2024, alta "
   "de 30%, com <b>recorde diário de 3.441 embarques em julho de 2025</b> (Setram). A bilheteria "
   "gera cerca de R$ 400 mil por mês ao sistema estadual.",
 "Menor visitação e temperatura":flag("Sem série mensal")+" o Data.Rio publica o consolidado "
   "anual, não o mês a mês.<br>"
   "<b>E aqui a intuição falha:</b> o pico registrado foi em <b>julho de 2025</b>, com o recorde "
   "diário de 3.441 embarques — ou seja, julho é <b>alta</b> temporada para o bonde, apesar de ser "
   "inverno. Férias escolares brasileiras pesam mais que o clima neste caso.<br>"
   "Santa Teresa é um bairro elevado e tipicamente mais fresco que o nível do mar, mas "
   +flag("não há")+" série termométrica específica do bairro publicada pelo INMET ou pelo Alerta "
   "Rio. Pela climatologia do município, as mínimas ficam em 15 a 16 °C de junho a agosto.",
 "Curiosidades":ul([
   "A bitola é de 1.100 mm, medida incomum no Brasil, adotada justamente para que o bonde coubesse "
   "sobre a estrutura dos Arcos da Lapa.",
   "A frota caiu de um pico de 35 veículos para 8 em operação em 2026; cinco bondes históricos "
   "seguem abandonados na Estação Barão de Mauá aguardando remoção.",
   "A estação do Largo da Carioca leva o nome do motorneiro Nelson Corrêa da Silva, morto no "
   "acidente de 2011.",
   "A revitalização do Ramal Silvestre usou cerca de 667 toneladas de trilhos novos, 27.800 m² de "
   "pavimentação e quase 6 km de rede elétrica aérea."]),
 "Fatos históricos":"<b>1872:</b> a Companhia Ferro-Carril de Santa Teresa obtém a concessão das "
   "linhas entre a Praça XV e os morros de Santa Teresa e Paula Mattos; o serviço começa com tração "
   "animal. <b>1º de setembro de 1896:</b> inauguração do sistema elétrico, com os bondes passando "
   "sobre o Aqueduto da Carioca — <b>em setembro de 2026 o bonde completou 130 anos</b>.<br>"
   "<b>27 de agosto de 2011:</b> uma falha no sistema de freios causou descarrilamento e capotamento "
   "na Rua Joaquim Murtinho. <b>Morreram 6 pessoas</b>, entre elas o motorneiro Nelson Corrêa da "
   "Silva, e mais de 50 ficaram feridas. O serviço foi totalmente suspenso. Dois meses antes, em "
   "junho, um turista francês já havia morrido ao cair do bonde enquanto viajava no estribo.<br>"
   "Depois de quatro anos de obras, o sistema reabriu em <b>27 de julho de 2015</b>, com veículos "
   "novos, gradil de segurança e <b>proibição do embarque no estribo</b>. As expansões vieram em "
   "dezembro de 2015 até o Largo dos Guimarães, outubro de 2018 até o Largo da França e janeiro de "
   "2019 até Dois Irmãos. Em março de 2025 o Ramal Paula Mattos voltou a operar todos os dias, e em "
   "<b>11 de junho de 2026</b> reabriu o <b>Ramal Silvestre</b>, parado por mais de 20 anos, com "
   "5,84 km.",
 "Dias em que não funciona":"<b>Os ramais Dois Irmãos e Paula Mattos operam todos os dias</b>, sem "
   "fechamento semanal fixo:<br>"
   "<b>Dois Irmãos</b> (Carioca ↔ Dois Irmãos): dias úteis das 8h às 17h, com intervalo de 20 "
   "minutos; sábados, domingos e feriados das 9h às 17h.<br>"
   "<b>Paula Mattos</b> (Carioca ↔ Largo das Neves): dias úteis das 8h às 17h, com intervalo de "
   "1 hora; sábados, domingos e feriados das 9h às 17h.<br>"
   "<b>Ramal Silvestre: somente de segunda a sexta</b>, com partidas da Estação Carioca às <b>10h, "
   "11h, 14h e 15h</b> — quatro viagens por dia. <b>Não opera aos sábados, domingos e feriados.</b><br>"
   +flag("Fontes divergem")+" há uma grade alternativa em circulação (segunda a sexta 8h às 17h40, "
   "sábado 10h às 17h40, domingo e feriados 11h às 16h40). Adotamos a grade anunciada pela Setram. "
   "Em feriados prolongados e no Réveillon o Governo do Estado publica grade especial — confirme "
   "no dia.",
 "Pontos turísticos próximos":"<b>Parque das Ruínas</b>, centro cultural municipal na Rua Murtinho "
   "Nobre, 169: <b>gratuito</b>, de terça a domingo das 8h às 18h, <b>fechado às segundas</b>. "
   "<b>Museu da Chácara do Céu</b>, dos Museus Castro Maya, na mesma rua, no nº 93: <b>gratuito</b>, "
   "das 10h às 16h30, <b>fechado às terças, domingos e feriados</b>, além de Carnaval, Natal e Ano "
   "Novo. Os dois são vizinhos e vale combinar a visita num dia que sirva aos dois — quarta a sábado.<br>"
   "Largo dos Guimarães e Largo das Neves são paradas do próprio bonde. E os Arcos da Lapa, por "
   "onde ele passa por cima."}
},
{
 "id":"lapa-arcos","nome":"Lapa e os Arcos","tag":"Monumento e vida noturna","img":"lapa",
 "preco":"Grátis","preconota":"por cima, só de bonde (R$ 20)",
 "campos":{
 "Endereço":"Praça Cardeal Câmara, s/nº — Lapa. A praça fica no encontro da Av. Mem de Sá com a "
   "Rua do Lavradio e a Av. República do Paraguai, <b>entre o Circo Voador e a Fundição "
   "Progresso</b>, as duas casas de música que a Riotur cita como vizinhas do monumento. O arco é "
   "visível de longe: são 270 metros de extensão e 18 de altura. Coordenadas do catálogo municipal "
   "Monumentos Rio: -22,91280 / -43,17990."
   +mapa("Arcos da Lapa","Arcos da Lapa, Praça Cardeal Câmara, Rio de Janeiro"),
 "Valor da entrada":"<b>Gratuito.</b> Monumento público a céu aberto, em praça pública; o catálogo "
   "municipal o classifica como obra pública e a Riotur não lista preço nem horário.<br>"
   "<b>A única cobrança relacionada à estrutura é a passagem do bonde, R$ 20</b>, que atravessa os "
   "Arcos por cima — é assim que se “visita” o aqueduto. As casas noturnas do entorno, "
   "Circo Voador e Fundição Progresso, cobram ingresso próprio: são estabelecimentos privados, não "
   "o monumento.",
 "Pontos de referência":"Circo Voador e Fundição Progresso, colados. A Praça Cardeal Câmara, cujo "
   "piso e passeios de pedra portuguesa foram restaurados pela Prefeitura em 2022. A Catedral "
   "Metropolitana, na Av. Chile, na mesma faixa entre a Lapa e o Largo da Carioca. E a Sala Cecília "
   "Meireles, no eixo do Boulevard Selarón.",
 "Metrô mais próximo":"<b>Cinelândia — Linhas 1 e 2.</b> A orientação é explícita no site do "
   "MetrôRio para chegar aos Arcos. "+flag("Sem tempo oficial")+" a caminhada não é publicada. O "
   "VLT Carioca também atende Cinelândia. <b>Para ver os Arcos por cima, o caminho é o bonde</b>, "
   "com embarque na Estação Carioca, no Largo da Carioca.",
 "Visitantes por ano":flag("Não existe")+" é praça pública sem controle de acesso. Procuramos em "
   "riotur.rio, prefeitura.rio, monumentos.rio.br e Data.Rio.<br>"
   "O único número correlato é o do bonde: os <b>702.768 passageiros de 2025</b> são pessoas que "
   "efetivamente cruzaram o aqueduto. É um piso, não o total de quem visitou a praça.",
 "Menor visitação e temperatura":flag("Não medida")+" não há contagem mensal nem anual.<br>"
   "Pelo clima do município: mínima de 15 °C em julho, máxima de 31 °C em janeiro e fevereiro, e "
   "agosto como mês mais seco, com 35 mm de chuva (Climatempo). Vale lembrar que a Lapa é um "
   "destino que muda de caráter por horário, não por estação — de dia é monumento e praça, à noite "
   "é vida noturna.",
 "Curiosidades":ul([
   "São 42 arcos duplos, com aberturas circulares na parte superior — número registrado tanto pela "
   "Prefeitura quanto pela Riotur.",
   "A Prefeitura o descreve como a maior obra de engenharia do Brasil no século XVIII.",
   "Na restauração de 2022, alpinistas industriais trabalharam a mais de 17 metros de altura para "
   "raspar e caiar a estrutura com cal virgem, técnica tradicional. Foram preservados dois painéis "
   "do artista Selarón integrados ao monumento."]),
 "Fatos históricos":"É um <b>aqueduto colonial</b>, construído para levar a água das nascentes do "
   "Rio Carioca até o abastecimento da cidade, <b>inaugurado em 1750</b>. Também é chamado Arcos da "
   "Carioca e Aqueduto da Carioca. São cerca de 270 metros de extensão e 18 metros de altura — ou "
   "17,6, conforme o catálogo municipal —, em estilo romano, de pedra e cal. <b>Tombado pelo IPHAN, "
   "processo nº 100-T-1938.</b><br>"
   "<b>O projeto não tem autor documentado:</b> o próprio catálogo Monumentos Rio registra "
   "“sem autoria” e “data imprecisa”. Desconfie de qualquer texto que "
   "atribua a obra a um arquiteto — não há atribuição oficial. "+flag("Sem autoria documentada")+"<br>"
   "<b>Desde 1896</b> o aqueduto deixou de conduzir água e passou a servir de via do Bonde de Santa "
   "Teresa. Em 2022 passou por restauração de cerca de R$ 1,3 milhão e cinco meses de obra, "
   "concluída em 8 de julho, com remoção de pichação, limpeza, raspagem e caiação. Em julho de 2026 "
   "passou a integrar o novo Distrito de Arte e Cultura da Lapa.",
 "Dias em que não funciona":"<b>Nenhum.</b> Praça pública, aberta 24 horas, sem horário de "
   "funcionamento publicado.<br>"
   "<b>O acesso por cima é outra história:</b> só se faz pelo bonde, e portanto fica limitado à "
   "grade dele — dias úteis das 8h às 17h e fins de semana das 9h às 17h nos ramais Dois Irmãos e "
   "Paula Mattos.",
 "Pontos turísticos próximos":"<b>Escadaria Selarón, a 5 minutos a pé</b> — dado oficial da "
   "Riotur. Circo Voador e Fundição Progresso, imediatamente ao lado. A estação do bonde, no Largo "
   "da Carioca. A Catedral Metropolitana, na Av. Chile. "+flag("Sem distância oficial")+" para os "
   "demais."}
},
{
 "id":"maracana","nome":"Maracanã","tag":"Estádio e tour","img":"maracana",
 "preco":"R$ 115","preconota":"tour; horário muda em dia de jogo",
 "campos":{
 "Endereço":"Av. Rei Pelé, s/nº — <b>Portão 2</b>, lado da Radial Oeste, CEP 20271-130, Maracanã. "
   "O nome oficial do estádio é <b>Estádio Jornalista Mário Filho</b>, e a antiga Av. Maracanã foi "
   "rebatizada de Av. Rei Pelé. <b>O acesso do tour é pelo Portão 2</b> — parte da imprensa indica "
   "Portão A, mas o site oficial diz Portão 2; siga o oficial. Pela Rua Prof. Eurico Rabelo chega-se "
   "aos portões B e C; pela Av. Prof. Manuel de Abreu, ao portão A; pela Rua Mata Machado, aos "
   "portões E e F; e pela Av. Maracanã, ao portão D."
   +mapa("Maracanã","Estádio do Maracanã, Av. Rei Pelé, Rio de Janeiro"),
 "Valor da entrada":"Fonte: site oficial do Maracanã Tour, consultado em 13/set/2026. "
   "<b>Inteira R$ 115</b> (≈ US$ 23), <b>meia R$ 57,50</b>. <b>Gratuito</b> para crianças até 2 anos "
   "com documento e para guias de turismo credenciados.<br>"
   "<b>Meia-entrada</b> para estudantes com carteirinha e documento; crianças de 3 a 11 anos com "
   "documento; idosos a partir de 60 anos; pessoas com deficiência, pela Lei Estadual 4.240/2003; e "
   "professores e profissionais de ensino da rede pública municipal do Rio. <b>A meia não vale para "
   "grupos.</b><br>"
   "<b>Estacionamento:</b> carro ou van R$ 35, ônibus R$ 45, moto R$ 15, das 9h às 17h. Bilheteria "
   "das 8h30 às 16h30.<br>"
   +flag("Cuidado com preço desatualizado")+" reportagens de 2026 ainda publicam R$ 94 de inteira e "
   "R$ 47 de meia. Esses valores estão vencidos — o site oficial pratica R$ 115 e R$ 57,50. Há "
   "também sites que imitam o oficial e declaram no rodapé não ter vínculo com o estádio.",
 "Pontos de referência":"A UERJ, colada ao complexo. O Estádio de Atletismo Célio de Barros e o "
   "Parque Aquático Júlio Delamare, dentro do complexo esportivo. A Radial Oeste, que corta o "
   "entorno. E as estações de metrô e trem, praticamente encostadas no estádio.",
 "Metrô mais próximo":"<b>Rei Pelé – Maracanã — Linha 2</b>, que dá acesso aos portões B e C, pela "
   "Rua Prof. Eurico Rabelo, e ao portão A, pela Av. Prof. Manuel de Abreu. A alternativa é <b>São "
   "Cristóvão — Linha 2</b>, com acesso aos portões E e F e ao portão D. A estação Maracanã é "
   "integrada metrô + trem da SuperVia. "+flag("Sem tempo oficial")+" o MetrôRio descreve os acessos "
   "como diretos, mas não publica distância nem tempo de caminhada até os portões.",
 "Visitantes por ano":"<b>421.484 visitantes em 2025</b>, recorde histórico do Maracanã Tour, "
   "contra 356.444 em 2023, que era o recorde anterior. "+flag("Via imprensa")+" a reportagem não "
   "identifica o órgão ou consórcio que divulgou os números e não localizamos o release original do "
   "operador do estádio. Procuramos no site do tour, na bilheteria online e em busca ampla.",
 "Menor visitação e temperatura":"<b>Aqui a variável não é a estação do ano, é a tabela de "
   "jogos.</b> O tour fecha ou tem horário reduzido em dia de jogo, e chega a fechar por dias "
   "seguidos em eventos de grande montagem — de 21 a 30 de agosto de 2026, por exemplo, ficou "
   "integralmente fechado por causa da NFL. A menor disponibilidade coincide com calendário "
   "esportivo cheio, como as finais de Brasileirão e Libertadores.<br>"
   +flag("Sem série mensal")+" não há série de visitantes do tour por mês. Pelo clima do município, "
   "as mínimas ficam em 15 a 16 °C em junho e julho e as máximas em 31 °C em janeiro e fevereiro. O "
   "Maracanã fica na Zona Norte, historicamente mais quente que a orla, mas "+flag("não há")+" série "
   "termométrica específica do bairro publicada.",
 "Curiosidades":ul([
   "O acervo exibe peças de Pelé, Garrincha e Zico, incluindo itens da Copa de 1962 e do milésimo "
   "gol de Pelé. As peças não são do museu: ficam emprestadas por quem as "
   "guarda, e a coleção pessoal de Zico — camisas, troféus e equipamentos — é parte disso.",
   "O roteiro inclui zona mista, vestiário dos jogadores, área de aquecimento, sala de entrevistas "
   "coletivas e o gramado.",
   "Há experiências pagas à parte: “Gol de Placa”, que é a foto no gol, "
   "“Foto Lembrança” e o tour de aniversário.",
   "Guias de turismo credenciados entram de graça — é política oficial de gratuidade."]),
 "Fatos históricos":"O estádio passou por reforma em 2013, para a Copa do Mundo de 2014. A avenida "
   "de acesso foi rebatizada de <b>Av. Rei Pelé</b>, e o MetrôRio já adota <b>Rei Pelé – Maracanã</b> "
   "como nome da estação.<br>"
   +flag("Não confirmado")+" a inauguração em 1950 e a capacidade atual de 78.838 lugares aparecem "
   "em fontes secundárias, mas não localizamos página institucional do estádio ou do consórcio "
   "gestor com esses números. Não publicamos como verificados.",
 "Dias em que não funciona":"<b>Não há fechamento fixo semanal.</b> O horário padrão, no FAQ "
   "oficial, é <b>diariamente das 9h às 16h</b>, “apenas em dias de jogos esse horário pode "
   "ser alterado”. A bilheteria funciona das 8h30 às 16h30. "+flag("Fontes divergem")+" a "
   "imprensa publica 9h às 17h com última entrada às 16h30; adotamos o horário oficial.<br>"
   "<b>A regra de dia de jogo é o que mais derruba visita, e ela é contraintuitiva:</b> no texto "
   "oficial, “em dias de jogos a última visita terminará cinco horas antes da abertura dos "
   "portões”. Ou seja, <b>o encerramento é calculado para trás a partir da abertura dos "
   "portões do jogo</b>, não de um horário fixo. Quanto mais cedo o jogo, mais cedo o tour fecha — "
   "e pode, na prática, não abrir.<br>"
   "Exemplos reais da grade publicada na home do tour em setembro de 2026: 8h às 12h30 com última "
   "entrada às 11h30 num dia; 9h às 15h30 com última entrada às 14h30 em outro; 9h às 13h30 com "
   "última entrada às 12h30 num terceiro.<br>"
   "<b>A regra prática:</b> confira a home do site do tour <b>no dia anterior</b> — é lá que a grade "
   "do dia é publicada. Comprar sem checar é o erro clássico. A própria página avisa que alterações "
   "de grade podem exigir remarcação ou reembolso.",
 "Pontos turísticos próximos":"UERJ, contígua ao complexo. Estádio de Atletismo Célio de Barros e "
   "Parque Aquático Júlio Delamare, dentro do complexo do Maracanã. "+flag("Sem distância oficial")+
   " o entorno imediato é esportivo e universitário; os pontos turísticos clássicos do Centro e da "
   "Zona Sul ficam a uma viagem de metrô."}
}]}
