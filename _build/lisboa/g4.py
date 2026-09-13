# -*- coding: utf-8 -*-
from lib import mapa, flag, ul

ROCA = ("Clima pela série verificada mais próxima: <b>normais do IPMA 1991–2020, estação Cabo da "
  "Roca</b> — o IPMA não publica ficha para a vila de Sintra, e esta é muito melhor que usar a de "
  "Lisboa. Mês mais frio <b>janeiro, 12,1 °C</b> de média; mais chuvoso <b>novembro, 77,4 mm</b>; "
  "mais quente <b>agosto, 19,2 °C</b>. <b>A máxima média nunca passa de 21,9 °C, nem em agosto</b> — "
  "Sintra é fresca o ano inteiro e a serra segura nevoeiro. Leve corta-vento mesmo em julho: isso "
  "não é folclore, está na tabela.")

INCENDIO = ("<b>Fecho por risco de incêndio — a regra mais séria e a mais ignorada.</b> Quando o "
  "Governo declara Situação de Alerta e manda fechar o perímetro florestal da Serra de Sintra, "
  "fecham quatro monumentos de uma vez: <b>Pena, Castelo dos Mouros, Monserrate e Convento dos "
  "Capuchos</b>. Aconteceu em agosto de 2025, com prolongamentos sucessivos por cerca de duas "
  "semanas. Quem tinha bilhete pediu reembolso por formulário, e a própria Parques de Sintra avisou "
  "que o processamento seria demorado pelo volume de pedidos. <b>Se você vai a Sintra entre julho e "
  "setembro, cheque o site na véspera e na manhã do dia.</b> Não é paranoia — fechou duas semanas.")

G4 = {
 "titulo": "Sintra e arredores",
 "intro": "O bate-volta clássico de Lisboa, e o que mais derruba viagem por detalhe burocrático: "
   "hora marcada sem tolerância na Pena, estrada fechada a carros, e a serra inteira podendo fechar "
   "por risco de incêndio no auge do verão.",
 "pontos": [
{
 "id":"palacio-da-pena","nome":"Palácio Nacional da Pena","tag":"Palácio","img":"pena",
 "preco":"€ 20","preconota":"hora marcada, sem tolerância de atraso",
 "campos":{
 "Endereço":"Estrada da Pena, 2710-609 Sintra. <b>Não tem “rua” no sentido "
   "convencional</b> — o palácio fica no alto da serra e chega-se por estrada de montanha.<br>"
   "<b>E há um detalhe que importa na prática:</b> a Parques de Sintra publica coordenadas de "
   "<b>duas entradas diferentes</b>, a Principal e a dos Lagos. <b>O autocarro 434 para na Entrada "
   "Principal</b> — se a sua hora marcada está apertada, é nela que você quer descer."
   +mapa("Palácio Nacional da Pena","Palacio Nacional da Pena, Estrada da Pena, Sintra"),
 "Valor da entrada":"<b>Primeiro, desfazendo um mito:</b> a Pena <b>não tem preço dinâmico</b>. Nas "
   "páginas oficiais não há qualquer menção a variação por data ou horário, e os valores da tabela "
   "batem com os da bilheteira online. O que confunde é outra coisa — <b>são cinco produtos "
   "diferentes com nomes parecidos e preços de € 20 a € 95</b>. É catálogo de experiências, não "
   "preço dinâmico. Se alguém disser que o preço da Pena sobe conforme a data, isso não está "
   "confirmado em fonte oficial.<br>"
   "<b>Visita Essencial: € 20</b> adulto de 18 a 64 (≈ R$ 119), <b>€ 18</b> jovem de 6 a 17 e sénior "
   "a partir de 65, <b>€ 65</b> a família de dois adultos e dois jovens. <b>Visita Total: € 45</b> "
   "adulto. <b>Só o Parque: € 12.</b> Há ainda Visita Guiada a € 75 e Visita Encenada a € 95.<br>"
   "<b>Gratuito para residentes em Portugal aos domingos e feriados</b>, cerca de 60 dias por ano — "
   "mas <b>presencialmente, na bilheteira, no dia, com documento</b>. Pessoas com deficiência têm "
   "50%. Há ainda 5% a 10% de desconto comprando de 2 a 6 monumentos na mesma compra.<br>"
   +flag("Não encontrado")+" tarifa de residente em Sintra e preçário de grupo.<br>"
   "<b>Lisboa Card: só 10% de desconto para adulto</b>, e não entrada livre. "+flag("Fontes divergem")+
   " as páginas oficiais do Turismo de Lisboa deram erro na consulta e as duas fontes comerciais "
   "discordam entre si.<br>"
   "<b>Dentro do parque há um circuito hop-on hop-off a € 4,50 por dia</b>, que é o transporte entre "
   "o portão e o palácio — é o que poupa a subida final.",
 "Pontos de referência":"A <b>Cruz Alta</b>, o ponto mais alto da Serra de Sintra, a 528 metros, "
   "dentro do próprio Parque da Pena. O <b>Chalet e Jardim da Condessa d'Edla</b>, também dentro do "
   "parque e — atenção — <b>já incluído no bilhete do parque</b>; muita gente paga e não sabe que "
   "tem direito. O <b>Castelo dos Mouros</b>, o muro serpenteando o morro ao lado. E a <b>Vila "
   "Sassetti</b>, a meio caminho na descida para a vila, com <b>entrada gratuita</b>.",
 "Metrô mais próximo":"<b>Não há metro em Sintra.</b> De Lisboa chega-se de <b>comboio, na Linha de "
   "Sintra, partindo do Rossio</b>, em 38 a 43 minutos, com partidas a cada 20 a 30 minutos.<br>"
   "Da estação de Sintra até a Pena, o <b>autocarro 434, o “Circuito da Pena”</b>, faz "
   "Estação → Palácio Nacional de Sintra → Castelo dos Mouros → Pena → Biester. <b>Bilhete diário "
   "€ 13,50</b>, válido 24 horas a partir da primeira validação, em sistema hop-on hop-off, e "
   "<b>cobre também o circuito 435</b>. Comprando online há 8% de desconto, cerca de € 10,96. "
   "Autocarros a cada 10 minutos.<br>"
   "<b>Subir a pé é viável, e aqui a Parques de Sintra publica os tempos</b> — ao contrário do que "
   "se costuma dizer: da Igreja de Santa Maria ao Castelo dos Mouros, <b>cerca de 45 minutos</b>; da "
   "entrada do Parque da Pena até o palácio, <b>cerca de 30 minutos</b>; a descida pela Vila "
   "Sassetti, <b>30 minutos</b>. Dificuldade classificada oficialmente como “média, algumas "
   "subidas”. "+flag("Sem desnível nem quilometragem")+" a Parques de Sintra não publica.<br>"
   "<b>De carro, esqueça:</b> a própria Parques de Sintra afirma que o acesso ao Castelo dos Mouros "
   "e ao Palácio da Pena é <b>impossível para veículos privados</b>.<br>"
   "<b>E o detalhe que derruba hora marcada:</b> o bilhete marca a entrada <b>no interior do "
   "palácio</b>, não no parque — e a Parques de Sintra manda contar <b>cerca de 30 minutos</b> entre "
   "um e outro. Se a sua hora é 14h, esteja no portão às 13h30.",
 "Visitantes por ano":"<b>1,9 milhão de visitantes em 2025.</b> O conjunto da Parques de Sintra "
   "somou 3,1 milhões no ano, contra 3,4 milhões em 2024 — e a queda foi atribuída oficialmente pelo "
   "presidente da empresa à <b>introdução de limites diários</b>, mais mau tempo e restrições por "
   "risco de incêndio.<br>"
   "<b>A lotação é de 6.000 visitantes por dia</b>, metade do pico anterior, de 12.000. "
   +flag("Via imprensa")+" o número foi divulgado pela Parques de Sintra à imprensa; não obtivemos o "
   "relatório de contas com o valor auditado.",
 "Menor visitação e temperatura":"<b>A Parques de Sintra não publica série mensal de visitantes.</b> "
   +flag("Sem dado mensal")+" Procuramos nas notícias, na secção institucional e na página de "
   "estatísticas: o que existe são divulgações anuais. <b>Não é possível dizer com fonte qual é o mês "
   "mais vazio da Pena</b>, e não vamos inventar um.<br>"+ROCA+"<br>"
   +flag("Nota metodológica")+" a estação do Cabo da Roca fica a 141 metros de altitude; <b>o "
   "Palácio da Pena está acima dos 400 e a Cruz Alta a 528</b>. A Pena é sistematicamente mais fria "
   "e mais húmida do que esta tabela mostra — mas não aplicamos gradiente térmico, porque isso seria "
   "estimativa.",
 "Curiosidades":ul([
   "<b>A Cruz Alta já foi destruída duas vezes.</b> A primeira, de D. João III por volta de 1522, "
   "caiu numa tempestade; a segunda, de D. Fernando II, foi destruída por um relâmpago em 1997. A "
   "atual é de 2008, com 3,5 metros e cerca de 1.700 quilos.",
   "<b>As cores que você fotografa foram repostas em 1994.</b> Durante boa parte do século XX o "
   "palácio esteve acinzentado; o restauro devolveu o rosa-velho ao antigo mosteiro e o ocre ao "
   "Palácio Novo.",
   "O parque tem mais de 200 hectares e mais de 500 espécies de árvores — é descrito como o parque "
   "europeu com o conjunto arbóreo mais rico e invulgar. <b>O palácio é a fotografia, mas o parque é "
   "a obra.</b>",
   "Foi classificado Monumento Nacional em 1910, o mesmo ano da implantação da República."]),
 "Fatos históricos":"Em <b>1511</b> D. Manuel I manda erguer no local o mosteiro de monges "
   "Jerónimos de Nossa Senhora da Pena. Em 1834 o convento é abandonado com a extinção das ordens "
   "religiosas, e em <b>1838 D. Fernando II</b> — o rei-artista — compra a ruína. A ampliação começa "
   "por volta de 1843, sob direção do <b>Barão Wilhelm Ludwig von Eschwege</b>, entre 1842 e 1854, e "
   "as grandes obras concluem-se em meados da década de 1860.<br>"
   "<b>Monumento Nacional em 1910</b>; restauro cromático em 1994; integrado em <b>1995 na Paisagem "
   "Cultural de Sintra, Património Mundial da UNESCO</b>, critérios (ii), (iv) e (v), numa área de "
   "946 hectares com zona tampão de 3.641. A inscrição engloba Pena, Castelo dos Mouros, Palácio "
   "Nacional de Sintra, Monserrate, Quinta da Regaleira e mais. Nas palavras da UNESCO, Sintra "
   "tornou-se no século XIX <b>o primeiro centro da arquitetura romântica europeia</b>.<br>"
   "<b>Nota que liga os dois monumentos:</b> o mesmo von Eschwege que fez a Pena foi quem D. "
   "Fernando II encarregou de restaurar o Castelo dos Mouros. É o mesmo projeto romântico, em dois "
   "monumentos.",
 "Dias em que não funciona":"<b>Não há fecho semanal</b> — abre todos os dias. <b>Parque das 9h às "
   "19h</b>, com último bilhete às 18h. <b>Palácio das 9h30 às 18h30</b>, com último bilhete às 17h30 "
   "e última entrada às 18h. "+flag("Não encontrado")+" horário de inverno distinto e lista de "
   "feriados de encerramento — a página de horários não publica nem um nem outro.<br>"
   "<b>Hora marcada, e sem tolerância.</b> O texto oficial é literal: <b>“não existe "
   "tolerância de atraso”</b>. Perdeu a hora, perdeu o bilhete — sem reembolso e sem "
   "remarcação. Chegar cedo também não adianta: só se entra na janela atribuída.<br>"+INCENDIO+"<br>"
   "<b>Fecho por mau tempo:</b> há registo de encerramento em 22 de janeiro de 2026, com monumentos "
   "fechados e praias interditadas. A serra tem vento forte e árvores caem.<br>"
   "<b>E a lotação de 6.000 por dia não é fila, é teto.</b> Quando enche, acabou.",
 "Pontos turísticos próximos":"Castelo dos Mouros, vizinho imediato e no mesmo circuito do 434. "
   "Chalet da Condessa d'Edla e Cruz Alta, dentro do parque. Vila Sassetti, gratuita, na descida. "
   "Palácio Nacional de Sintra, na vila, com jardins de entrada livre. Palácio Biester, que tem "
   "bilhete combinado com a Pena. Quinta da Regaleira e Monserrate, no circuito 435. E o Convento "
   "dos Capuchos."}
},
{
 "id":"quinta-da-regaleira","nome":"Quinta da Regaleira","tag":"Quinta e jardim","img":"regaleira",
 "preco":"€ 20","preconota":"uma hora de tolerância no bilhete",
 "campos":{
 "Endereço":"Quinta da Regaleira, 9, 2710-567 Sintra — ou Rua Barbosa du Bocage, 2710-567 Sintra. "
   "<b>As duas grafias são oficiais e do mesmo conjunto</b>, cada uma numa fonte diferente.<br>"
   "Fica a caminho de Monserrate, saindo do centro histórico pela estrada que passa em frente ao "
   "Palácio de Seteais. <b>É dos poucos monumentos de Sintra que dá para alcançar a pé do centro sem "
   "subir a serra</b> — está na estrada, não no topo. O portão de visitantes é na via principal e "
   "tem fila visível."+mapa("Quinta da Regaleira","Quinta da Regaleira, Sintra"),
 "Valor da entrada":"Tarifário oficial de 2026. <b>Adulto de 18 a 64: € 20</b> (≈ R$ 119). <b>Jovem "
   "de 6 a 17 e sénior a partir de 65: € 15.</b> <b>Criança até 5 anos: grátis.</b> Pessoa com "
   "deficiência e acompanhante: € 12. <b>Família, dois adultos e dois jovens, máximo quatro "
   "pessoas: € 60.</b><br>"
   "<b>E há uma gratuidade que a Parques de Sintra não tem:</b> <b>munícipes de Sintra</b>, com "
   "domicílio fiscal no concelho, entram de graça — assim como profissionais do turismo registados e "
   "antigos combatentes.<br>"
   "<b>Mas atenção à pegadinha que custa caro:</b> a Regaleira <b>não participa</b> na gratuidade de "
   "domingos para residentes em Portugal. <b>No mesmo domingo em que a Pena está de graça para quem "
   "mora em Portugal, aqui se paga os € 20 cheios.</b><br>"
   "<b>Lisboa Card: só 20% de desconto</b>, não entrada livre.<br>"
   "<b>Cuidado com bilhete de revenda:</b> o próprio site oficial alerta que muitos visitantes "
   "chegam com bilhetes de vendedores não autorizados.",
 "Pontos de referência":"O Palácio de Seteais, na mesma estrada, a poucos minutos a pé. O centro "
   "histórico de Sintra e a Volta do Duche — que desde julho de 2026 é <b>o único local autorizado "
   "para largada de passageiros com destino à Regaleira</b>. O Palácio de Monserrate, mais adiante "
   "na mesma via. E o Palácio Nacional de Sintra, com as duas chaminés cónicas, na vila.",
 "Metrô mais próximo":"<b>Não há metro.</b> De Lisboa, comboio da Linha de Sintra a partir do "
   "Rossio. Da estação de Sintra, o <b>autocarro 435, o “Circuito Regaleira / "
   "Monserrate”</b>, faz Estação → Regaleira → Seteais → Monserrate, com o <b>mesmo bilhete "
   "diário de € 13,50</b> que cobre o 434.<br>"
   "<b>A pé é o monumento mais caminhável de Sintra</b>, porque está na estrada e não no alto da "
   "serra. "+flag("Sem tempo a pé")+" nem a Cultursintra nem a Parques de Sintra publicam a "
   "caminhada do centro até aqui, e não estimamos.<br>"
   "<b>De carro, regra nova:</b> desde 8 de julho de 2026 a largada de passageiros com destino à "
   "Regaleira está <b>restrita à Volta do Duche</b>.",
 "Visitantes por ano":flag("Não encontrado")+" a Fundação Cultursintra <b>não publica</b> número "
   "anual de visitantes. Procuramos no site oficial, na bilheteira oficial, no portal da Câmara de "
   "Sintra e em busca dirigida.<br>"
   "<b>O que existe e é verificável é a lotação diária, não o total:</b> a Regaleira recebia até "
   "<b>9.000 visitantes por dia</b>, e em setembro de 2024 a Câmara Municipal de Sintra <b>cortou "
   "esse máximo pela metade, para cerca de 4.500</b>, alegando queixas de residentes e comerciantes "
   "sobre a pressão turística no centro histórico.",
 "Menor visitação e temperatura":"<b>Nem série mensal, nem total anual.</b> "+flag("Sem dado")+
   " Como nem o número do ano existe publicamente, não há como falar em mês de menor visitação com "
   "base em fonte.<br>"+ROCA+"<br>"
   "<b>Nota específica desta visita:</b> ela é quase toda ao ar livre, num jardim com gruta, túneis "
   "e o Poço Iniciático — que são <b>escadas de pedra em espiral, húmidas</b>. Com a chuva de "
   "outubro a dezembro, o piso fica escorregadio. Isso é consequência direta da tabela do IPMA, não "
   "opinião.",
 "Curiosidades":ul([
   "<b>A quinta deve o nome a uma baronesa, não ao construtor famoso.</b> D. Ermelinda Allen, "
   "Baronesa da Regaleira, foi proprietária entre 1830 e 1892 e deu o nome ao conjunto. Carvalho "
   "Monteiro só comprou depois.",
   "<b>Esteve fechada e nas mãos de uma empresa japonesa por quase uma década.</b> Entre 1988 e 1997 "
   "pertenceu à Aoki Corporation, que a manteve encerrada — o monumento que hoje é o cartão-postal "
   "esotérico de Sintra passou nove anos inacessível.",
   "<b>O arquiteto era cenógrafo de teatro</b>, não arquiteto de formação: Luigi Manini, italiano, "
   "tinha acabado de trabalhar no Hotel Palace do Buçaco. Isso explica muito do efeito teatral do "
   "conjunto.",
   "O Aquário está fechado para obras de conservação, e isso não aparece na maioria dos guias."]),
 "Fatos históricos":"Proprietários documentados desde 1697. Entre 1830 e 1892 a propriedade passa a "
   "<b>D. Ermelinda Allen</b>, futura Baronesa da Regaleira, que lhe dá o nome. Em <b>1892</b> "
   "compra-a o <b>Dr. António Augusto de Carvalho Monteiro</b>, apelidado <b>“Monteiro dos "
   "Milhões”</b>, e é dele a transformação que a tornou célebre — o conjunto, de <b>Luigi "
   "Manini</b>, conclui-se em <b>1910</b>. Entre 1942 e 1988 pertence a Waldemar d'Orey; de 1988 a "
   "1997, à Aoki Corporation; desde 1997 é da Câmara Municipal de Sintra, com gestão da Fundação "
   "Cultursintra. Estilo <b>ecléctico-revivalista</b>, com jardins de quatro hectares.<br>"
   "<b>Um cuidado de precisão:</b> a Regaleira é <b>Imóvel de Interesse Público</b>, classificação "
   "de <b>2002</b> — grau <b>inferior</b> a Monumento Nacional, que é o que têm a Pena e o Castelo "
   "dos Mouros. Está incluída, sim, na Paisagem Cultural de Sintra da UNESCO desde 1995, mas são "
   "camadas diferentes. <b>Não escreva “Monumento Nacional” sobre a Regaleira, porque "
   "não é.</b><br>"
   +flag("Não publicado")+" a profundidade e o número de patamares do Poço Iniciático. Circulam "
   "números em sites de revenda e blogs, mas não conseguimos confirmar em fonte primária — e por "
   "isso não os publicamos.",
 "Dias em que não funciona":"<b>Não há fecho semanal.</b> Encerra em <b>1 de janeiro, 24, 25 e 31 "
   "de dezembro</b>.<br>"
   "<b>Verão, de abril a setembro:</b> jardins das 9h às 19h30; palácio, capela e espaços "
   "expositivos das 10h às 19h. <b>Inverno:</b> abertura às 10h e encerramento às 18h30. <b>Última "
   "entrada às 17h30</b> nos dois casos, com slots de 30 em 30 minutos.<br>"
   "<b>E aqui a Regaleira é muito mais generosa que a Pena:</b> concede <b>tolerância máxima de uma "
   "hora de atraso</b> sobre a hora do bilhete. Contra <b>zero</b> na Pena. Se você vai fazer os dois "
   "no mesmo dia, é na Pena que o relógio não perdoa.<br>"
   "<b>Palácio, capela e espaços expositivos fecham 30 minutos antes dos jardins.</b> Quem entra às "
   "18h45 em julho vê jardim e não vê palácio.",
 "Pontos turísticos próximos":"Palácio de Seteais, na mesma estrada. Parque e Palácio de Monserrate, "
   "no circuito 435. Palácio Nacional de Sintra, na vila, com jardins gratuitos. Vila Sassetti, "
   "gratuita. Castelo dos Mouros e Palácio da Pena, no circuito 434. E o Convento dos Capuchos."}
},
{
 "id":"castelo-dos-mouros","nome":"Castelo dos Mouros","tag":"Castelo","img":"mouros",
 "preco":"€ 12","preconota":"sem hora marcada — o plano B da Pena",
 "campos":{
 "Endereço":"Estrada da Pena, 2710-609 Sintra. <b>Repare: é a mesma morada e o mesmo código postal "
   "do Palácio da Pena.</b> Não é erro — os dois ficam na mesma estrada de serra, e é por isso que "
   "fazem sentido juntos no mesmo dia.<br>"
   "O castelo está isolado num cume da Serra de Sintra: você o vê de baixo, da vila, como uma "
   "<b>muralha serpenteando o morro</b>. A entrada é pela Estrada da Pena, no mesmo eixo do 434."
   +mapa("Castelo dos Mouros","Castelo dos Mouros, Sintra"),
 "Valor da entrada":"<b>Adulto € 12</b> (≈ R$ 71). <b>Jovem e sénior € 10.</b> <b>Família € 33.</b> "
   "Valem as mesmas gratuidades da Parques de Sintra: <b>residentes em Portugal aos domingos e "
   "feriados</b>, na bilheteira, com documento.<br>"
   "<b>Não existe bilhete combinado com a Pena.</b> O que existe é o desconto de 5% por comprar dois "
   "locais na mesma compra: € 32 viram € 30,40 — <b>poupança de € 1,60</b>, e dizemos que é pouco. "
   "O combinado que realmente vale é outro: <b>“Viver Sintra: Palácios Reais”, a € 42</b>, "
   "que junta Pena, Palácio Nacional de Sintra <b>e o transporte de 24 horas</b>, contra € 46,50 "
   "comprando tudo avulso.",
 "Pontos de referência":"O Palácio da Pena, na mesma estrada, vizinho. A Vila Sassetti, gratuita, "
   "onde o percurso pedestre liga os dois níveis. A Igreja de Santa Maria, na vila, que é o ponto de "
   "partida oficial do percurso a pé. O centro histórico de Sintra, visível lá de cima. E, em dia "
   "limpo, <b>vê-se a linha de costa até o Cabo da Roca</b>.",
 "Metrô mais próximo":"<b>Não há metro.</b> Comboio da Linha de Sintra desde o Rossio, e depois o "
   "<b>autocarro 434</b>, que para no castelo — bilhete diário de € 13,50, cerca de € 10,96 online, "
   "com autocarros a cada 10 minutos.<br>"
   "<b>A pé, e aqui o tempo é oficial:</b> <b>cerca de 45 minutos</b> da Igreja de Santa Maria até o "
   "castelo, dificuldade “média, algumas subidas”. A página do monumento refere três "
   "percursos pedestres marcados, de 45 minutos a 1h30, conforme o trajeto.<br>"
   "<b>De carro, não:</b> a Parques de Sintra afirma que o acesso é impossível para veículos "
   "privados. Use os estacionamentos periféricos da vila.",
 "Visitantes por ano":"<b>409.000 visitantes em 2025.</b> Para comparar, no mesmo ano: Pena 1,9 "
   "milhão; Palácio Nacional de Sintra 400 mil; Monserrate 200 mil; Queluz 155 mil.<br>"
   "<b>Ou seja: o Castelo dos Mouros recebe cerca de um quinto do que recebe a Pena.</b> É o "
   "monumento mais respirável do circuito. "+flag("Via imprensa")+" número divulgado pela Parques de "
   "Sintra à imprensa, sem relatório auditado.",
 "Menor visitação e temperatura":"<b>A Parques de Sintra não publica série mensal.</b> "
   +flag("Sem dado mensal")+" Só há divulgação anual.<br>"+ROCA+"<br>"
   "<b>Aviso específico daqui:</b> a visita é <b>caminhar em cima de muralha exposta</b>, sem "
   "abrigo, num cume de serra. <b>Vento e nevoeiro são o problema real, mais do que a "
   "temperatura.</b> "+flag("Sem série de vento")+" o IPMA não publica vento para a Serra de Sintra "
   "em ficha de normais, então não damos número — registamos apenas que a exposição é total.",
 "Curiosidades":ul([
   "<b>Nem os investigadores concordam sobre quem o fundou.</b> A Câmara de Sintra regista que "
   "alguns propõem fundação visigótica no século VII, enquanto a maioria atribui aos séculos VIII ou "
   "IX, no período muçulmano. O nome “Castelo dos Mouros” é a hipótese dominante, não um "
   "facto fechado.",
   "<b>Ele pode não ter sido conquistado à força:</b> depois do cerco de Lisboa em 1147, o castelo "
   "<b>rendeu-se voluntariamente</b>, segundo a fonte municipal.",
   "<b>O castelo que você visita é, em boa parte, obra romântica do século XIX.</b> D. Fernando II "
   "encarregou o Barão von Eschwege de restaurar muralhas e torres. Você não está a ver ruína "
   "intocada — está a ver restauro oitocentista.",
   "<b>A bilheteira fecha para almoço, mas o castelo não.</b> Encerra das 12h às 13h, com venda "
   "automática disponível. Se chegar ao meio-dia, use a máquina."]),
 "Fatos históricos":"Fundação nos <b>séculos VIII ou IX</b>, na hipótese dominante, durante a "
   "ocupação muçulmana — com hipótese alternativa de fundação visigótica no século VII. Em "
   "<b>1147</b>, depois do cerco de Lisboa, passa a D. Afonso Henriques, segundo a fonte municipal "
   "por rendição voluntária. Em meados do século XIX D. Fernando II promove a recuperação romântica, "
   "com o <b>Barão Wilhelm Ludwig von Eschwege</b> a restaurar muralhas e torres — o mesmo arquiteto "
   "da Pena.<br>"
   "<b>Monumento Nacional</b>, e integrado em 1995 na Paisagem Cultural de Sintra da UNESCO. "
   +flag("Decreto não encontrado")+" a classificação está confirmada pela Parques de Sintra, mas as "
   "fichas da base de dados do património devolveram erro e <b>a data do decreto não foi obtida</b>. "
   "Não inventamos.",
 "Dias em que não funciona":"<b>Horário das 9h30 às 18h, todos os dias</b>, com último bilhete e "
   "última entrada às 17h30. <b>Não há fecho semanal.</b> A bilheteira encerra das 12h às 13h, com "
   "venda automática. "+flag("Não encontrado")+" horário sazonal distinto e lista de feriados de "
   "encerramento.<br>"
   "<b>E aqui está a vantagem decisiva deste ponto: não há hora marcada.</b> Ao contrário da Pena, "
   "o Castelo dos Mouros não exige bilhete com horário — <b>o que faz dele o plano B perfeito num "
   "dia em que a Pena esgotou</b>.<br>"+INCENDIO+"<br>"
   "<b>Fecho por mau tempo:</b> registo de encerramento em 22 de janeiro de 2026. <b>Muralha em cume "
   "de serra é dos primeiros sítios a fechar com vento forte.</b>",
 "Pontos turísticos próximos":"Palácio Nacional da Pena, vizinho e no mesmo bilhete de autocarro. "
   "Chalet da Condessa d'Edla, dentro do Parque da Pena. Vila Sassetti, gratuita, no percurso "
   "pedestre. Igreja de Santa Maria, início do percurso a pé. Palácio Nacional de Sintra, na vila. "
   "Quinta da Regaleira, Seteais e Monserrate, no circuito 435. E o Convento dos Capuchos."}
},
{
 "id":"cabo-da-roca","nome":"Cabo da Roca e Cascais","tag":"Mirante e vila","img":"caboroca",
 "preco":"Grátis","preconota":"o cabo; o farol abriu em julho e cobra € 5",
 "campos":{
 "Endereço":"Cabo da Roca, Azóia, 2705-001 Colares. <b>E aqui está um erro geográfico que quase "
   "todo guia comete: o Cabo da Roca não fica em Cascais.</b> Fica no <b>concelho de Sintra</b>, "
   "freguesia de Colares, lugar de Azóia — quem gere o posto de turismo é a Câmara Municipal de "
   "Sintra. Cascais é o vizinho, e é de onde muita gente chega, mas o cabo é de Sintra.<br>"
   "<b>Não há rua.</b> Chega-se pela EN-247, vindo de Cascais ou de Colares. É um promontório com "
   "farol, um cruzeiro de pedra, um posto de turismo e um estacionamento. Não tem como errar: <b>a "
   "estrada acaba ali.</b>"+mapa("Cabo da Roca","Cabo da Roca, Colares, Sintra"),
 "Valor da entrada":"<b>O acesso ao cabo e ao miradouro é gratuito.</b> Não há bilheteira para "
   "chegar ao cruzeiro e à falésia.<br>"
   "<b>Mas o farol abriu à visitação em 23 de julho de 2026, e esse paga.</b> O Centro "
   "Interpretativo do Farol do Cabo da Roca é gerido pela Parques de Sintra, com investimento "
   "superior a € 1,6 milhão, e tem centro interpretativo, exposições temporárias, cafetaria e loja.<br>"
   "<b>Visita Essencial: € 5</b> — e repare, <b>adulto, jovem e sénior pagam todos os mesmos € 5</b>. "
   "Não é erro de transcrição, é o que está na tabela oficial. Família de dois adultos e dois jovens: "
   "€ 15. <b>Visita Panorâmica</b>, que inclui a subida guiada à varanda: <b>€ 10</b> adulto, € 7,50 "
   "sénior, € 5 jovem, € 20 família. <b>Criança até 6 anos não paga.</b><br>"
   "<b>E o certificado de ponto mais ocidental da Europa tem preço oficial: € 11</b>, manuscrito em "
   "caligrafia francesa, na hora, com o seu nome. <b>Há versão em Braille por € 4,50</b> — informação "
   "que praticamente nenhum guia brasileiro traz.<br>"
   +flag("Não confirmado")+" se a gratuidade de domingos para residentes em Portugal se aplica ao "
   "farol: ele é gerido pela Parques de Sintra, mas <b>não consta da lista nominal de monumentos "
   "abrangidos</b>, provavelmente por ter aberto depois. "+flag("Não encontrado")+" referência ao "
   "farol nas listas do Lisboa Card, nem preçário de grupo.<br>"
   "<b>Cascais é vila, não monumento — não há bilhete de entrada.</b> "+flag("Não apurado")+" os "
   "museus de Cascais cobram individualmente, mas o portal oficial de turismo descreve genericamente "
   "“um bairro inteiro de museus” <b>sem publicar lista com morada, preço ou "
   "horário</b>. Não vamos preencher o que a fonte não dá.",
 "Pontos de referência":"O <b>farol</b>, torre de 22 metros com alcance luminoso de cerca de 48 km. "
   "O <b>cruzeiro de pedra</b> com a placa do ponto mais ocidental — é a foto obrigatória. O posto de "
   "turismo, que emite o certificado. E a <b>Praia da Ursa</b>, praia selvagem nas imediações, "
   "servida pelos mesmos autocarros. Desde 1989 o cabo integra um programa internacional de promoção "
   "da paz.<br>"
   "Entre o cabo e Cascais, na EN-247: Azóia, Almoçageme e Colares, e a <b>Praia do Guincho</b>.",
 "Metrô mais próximo":"<b>Não há metro.</b> E há uma armadilha de informação desatualizada: "
   "<b>o autocarro 403 não existe mais — foi extinto em 2023.</b> Hoje vai-se ao Cabo da Roca pelo "
   "<b>1253</b>, desde Sintra, em cerca de 45 minutos, ou pelo <b>1624</b>, desde Cascais, em cerca "
   "de 35. <b>Atenção: a linha 1623 não para no Cabo da Roca.</b><br>"
   "<b>Para Cascais</b>, de Lisboa: comboio da <b>Linha de Cascais, partindo do Cais do Sodré</b>, em "
   "38 a 42 minutos, com partidas a cada 20 a 30 minutos. O terminal rodoviário de Cascais fica "
   "colado à estação.<br>"
   +flag("Tarifa do comboio não fechada")+" o site da CP falhou por erro de certificado na apuração. "
   "Confirmamos no PDF oficial a escada de zonas, de € 1,50 a € 3,90, e o ida-e-volta Lisboa–Cascais "
   "a € 2,90 — <b>mas não a zona de Sintra</b>, e as fontes secundárias divergem. O passe de 24h "
   "Carris/Metro/CP, a € 11,40, cobre as duas linhas e resolve a dúvida.",
 "Visitantes por ano":flag("Não encontrado")+" e a razão é estrutural: <b>o acesso é livre, sem "
   "torniquete, logo não há contagem</b>. O farol abriu há menos de dois meses e ainda não tem "
   "número publicado.",
 "Menor visitação e temperatura":"<b>Sem série de visitação</b>, pelo motivo acima. "
   +flag("Não medida")+"<br>"
   "<b>Mas aqui o clima é o melhor dado de todo este guia, porque a estação do IPMA é literalmente "
   "ali.</b> Normais 1991–2020 da estação Cabo da Roca: <b>a máxima média nunca passa de 21,9 °C</b>, "
   "nem em agosto; janeiro tem 12,1 °C de média e novembro 77,4 mm de chuva. <b>O brasileiro chega "
   "de bermuda e passa frio</b> — é o ponto mais exposto ao Atlântico de todo o roteiro.",
 "Curiosidades":ul([
   "É o <b>ponto mais ocidental da Europa continental</b>, e o certificado que atesta a sua presença "
   "é escrito à mão, em caligrafia francesa.",
   "O farol tem <b>22 metros</b> e alcance luminoso de cerca de <b>48 quilómetros</b>, o equivalente "
   "a 26 milhas náuticas.",
   "<b>O farol só abriu à visitação em 23 de julho de 2026</b> — antes disso, quem ia ao cabo via a "
   "torre de fora e mais nada.",
   "Desde 1989 o Cabo da Roca integra um programa internacional de promoção da paz."]),
 "Fatos históricos":"O farol é um dos mais antigos de Portugal, mas "+flag("as fontes oficiais "
   "divergem em cinquenta anos")+": a <b>Parques de Sintra</b> fala em alvará de 1758 e entrada em "
   "operação em <b>1772</b>; a <b>Visit Sintra</b>, da Câmara Municipal, diz <b>1722</b>. São duas "
   "fontes oficiais portuguesas com meio século de diferença. Registamos, não arbitramos.<br>"
   "O <b>Centro Interpretativo</b> foi inaugurado em 22 de julho de 2026 e abriu ao público no dia "
   "23, com investimento superior a € 1,6 milhão.<br>"
   "Sobre o <b>verso de Camões</b> gravado no cruzeiro — “onde a terra acaba e o mar "
   "começa” — "+flag("não aparece em nenhuma fonte oficial")+" que conseguimos abrir. É o "
   "dado mais citado de todos os guias sobre o Cabo da Roca, e não o publicamos como verificado.",
 "Dias em que não funciona":"<b>O cabo em si não fecha:</b> é promontório de acesso livre, sem "
   "portão.<br>"
   "<b>O posto de turismo</b>, que emite o certificado, abre das <b>9h às 19h30 de 1 de maio a 30 de "
   "setembro</b> e das <b>9h às 18h30 de 1 de outubro a 30 de abril</b>. Encerra no Natal e no Ano "
   "Novo.<br>"
   "<b>O farol fecha às 17h30, com última entrada às 17h.</b><br>"
   "<b>E aqui está um encaixe de horário que vale a viagem:</b> o farol fecha às 17h30, mas o posto "
   "de turismo fica aberto até às 19h30 no verão. <b>Chegue antes das 17h para conseguir fazer as "
   "duas coisas</b> — subir ao farol e levar o certificado.",
 "Pontos turísticos próximos":"Praia da Ursa, nas imediações. Praia do Guincho, no eixo para "
   "Cascais. As povoações de Azóia, Almoçageme e Colares. Cascais, a cerca de 35 minutos de "
   "autocarro. E, do lado de Sintra, todo o circuito da serra. "+flag("Sem distância oficial")}
}]}
