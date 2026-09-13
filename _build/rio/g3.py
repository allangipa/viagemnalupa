# -*- coding: utf-8 -*-
from lib import mapa, flag, ul

G3 = {
 "titulo": "Centro e cultura",
 "intro": "Quatro endereços a distância de caminhada entre si — e cada um fecha num dia diferente. "
   "Dois museus fecham na quarta, o Real Gabinete fecha o fim de semana inteiro e o Theatro só faz "
   "visita de quarta a sábado. Montar o dia errado aqui custa a viagem toda.",
 "pontos": [
{
 "id":"museu-do-amanha","nome":"Museu do Amanhã","tag":"Museu de ciências","img":"museuamanha",
 "preco":"R$ 40","preconota":"R$ 10 todo dia 10; grátis em feriado nacional",
 "campos":{
 "Endereço":"Praça Mauá, 1 — Centro, CEP 20081-240. É o prédio branco em balanço sobre o espelho "
   "d'água no Píer Mauá, na ponta da praça voltada para a Baía de Guanabara, do lado oposto ao MAR. "
   "Não tem como confundir: a estrutura de “espinhas” metálicas móveis no telhado é "
   "visível de toda a Orla Conde."+mapa("Museu do Amanhã","Museu do Amanhã, Praça Mauá 1, Rio de Janeiro"),
 "Valor da entrada":"Fonte: site oficial do museu, consultado em 13/set/2026. <b>Inteira R$ 40</b> "
   "(≈ US$ 8), <b>meia R$ 20</b>.<br>"
   "<b>Todo dia 10 do mês o ingresso custa R$ 10</b>, promoção dos 10 anos do museu, nas palavras do "
   "próprio site. Não é cumulativa com a meia-entrada.<br>"
   "<b>A regra da gratuidade mudou e muita gente ainda usa a informação velha.</b> As terças-feiras "
   "<b>não são mais gratuitas</b>: desde abril de 2025 a gratuidade migrou para <b>todos os feriados "
   "nacionais</b>, e nas terças a bilheteria opera com preços populares, entre R$ 15 e R$ 30 "
   "(Diário do Rio e Mercado&amp;Eventos, 27/mar/2025). Se você encontrar “terça é de graça no "
   "Museu do Amanhã”, é informação de antes de 2025.<br>"
   "<b>Gratuidade permanente</b> para 60+, crianças até 5 anos, alunos e professores da rede pública, "
   "guias de turismo, funcionários de museus, acompanhantes de pessoa com deficiência e populações "
   "vulneráveis — sempre com documentação comprobatória. "+flag("Lista via imprensa")+" a seção de "
   "gratuidades do site oficial carrega por JavaScript e não foi possível ler o conteúdo na fonte "
   "primária; a lista acima vem das reportagens de março de 2025.<br>"
   +flag("Não existe")+" faixa de morador do Rio aqui — nenhuma fonte oficial menciona. Dos quatro "
   "pontos desta seção, só o MAR tem essa faixa.",
 "Pontos de referência":"Praça Mauá e o Píer Mauá. O MAR, do lado oposto da praça. A Orla Conde e "
   "o Boulevard Olímpico, colados. A escultura <i>Puffed Star II</i>, de Frank Stella, na área "
   "externa do próprio museu.",
 "Metrô mais próximo":"<b>O acesso natural é o VLT, não o metrô.</b> A <b>Parada dos Museus, "
   "Linha 1 do VLT Carioca</b>, serve o museu diretamente, a cerca de 2 minutos a pé; a linha liga o "
   "Santos Dumont ao Terminal Gentileza. De metrô, a estação mais próxima é <b>Uruguaiana — Linhas 1 "
   "e 2</b>, com caminhada de 15 a 20 minutos; o trajeto usual é descer em Uruguaiana ou Carioca e "
   "completar de VLT. "+flag("Sem tempo oficial")+" o MetrôRio não publica a caminhada.",
 "Visitantes por ano":"<b>815.800 visitantes de janeiro a julho de 2026</b>, segundo o balanço da "
   "Secretaria Municipal de Cultura do Rio (via Brasil em Folhas, 2/set/2026). <b>7 milhões "
   "acumulados</b> desde a inauguração, marca atingida em 31/jan/2025.<br>"
   +flag("Não encontrado")+" total de um ano-calendário fechado: o que se divulga é sempre acumulado "
   "ou parcial. Procuramos no site oficial, no portal da Secretaria Municipal de Cultura e na imprensa.",
 "Menor visitação e temperatura":"<b>De junho a agosto</b>, o vale da baixa temporada carioca, "
   "também os meses mais secos e frios: julho tem mínima média de 15 °C e máxima de 25 °C, e agosto é "
   "o mais seco, com 35 mm de chuva (Climatempo, série de 30 anos). "+flag("Sem dado mensal")+" o "
   "museu não publica série de visitação por mês — a correlação com a baixa temporada é do turismo da "
   "cidade, não medida na bilheteria. O que existe de dado interno é antigo: em 2023, quando as "
   "terças eram gratuitas, o museu informou que elas recebiam de 5 a 6 mil pessoas contra “3 mil "
   "e poucos” nos demais dias — número anterior à mudança de 2025.",
 "Curiosidades":ul([
   "A cobertura tem placas solares móveis que acompanham o sol como asas, e a climatização usa água "
   "da Baía de Guanabara, depois devolvida aos espelhos d'água.",
   "A forma do prédio foi inspirada nas bromélias do Jardim Botânico do Rio.",
   "A escultura <i>Puffed Star II</i>, de Frank Stella — uma estrela de 20 pontas com 6 metros de "
   "diâmetro — foi doada ao museu em 2015 e fica na área externa, de graça para quem só passa."]),
 "Fatos históricos":"Inaugurado em <b>17 de dezembro de 2015</b>, recebeu 25 mil visitantes no "
   "primeiro fim de semana. Projeto do arquiteto espanhol <b>Santiago Calatrava</b>, com obra de "
   "cerca de R$ 230 milhões, 15.000 m² de edifício e cerca de 30.000 m² de entorno com jardins, "
   "espelhos d'água e ciclovia. É a peça-âncora da revitalização do Porto Maravilha e se descreve "
   "como um museu de ciências de terceira geração — voltado a cenários de futuro em vez de acervo "
   "do passado.",
 "Dias em que não funciona":"<b>Fecha às quartas-feiras.</b> Abre de quinta a terça, das <b>10h às "
   "18h</b>, com última entrada às 17h, <b>feriados inclusive</b> — e feriado nacional é justamente "
   "o dia gratuito. "+flag("Não encontrado")+" calendário de fechamento por manutenção: não havia "
   "aviso no site na data da consulta.",
 "Pontos turísticos próximos":"MAR, na mesma praça, do lado oposto. Orla Conde e Boulevard "
   "Olímpico, colados. Mural Etnias, de Kobra, pelo Boulevard. AquaRio e o Cais do Valongo, "
   "patrimônio mundial da UNESCO, ambos a uma caminhada curta pelo Porto. "+flag("Sem distância oficial")+
   " os tempos a pé não são publicados por nenhuma das instituições."}
},
{
 "id":"mar","nome":"MAR — Museu de Arte do Rio","tag":"Museu de arte","img":"mar",
 "preco":"R$ 20","preconota":"terça é grátis para todos",
 "campos":{
 "Endereço":"Praça Mauá, 5 — Centro, CEP 20081-240. Telefone (21) 3031-2741. São <b>dois prédios "
   "interligados</b> por uma cobertura ondulada branca, no lado da praça oposto ao Museu do Amanhã: "
   "o <b>Palacete Dom João VI</b>, eclético e tombado, e um antigo terminal rodoviário modernista. A "
   "“onda” de concreto no topo é a referência visual."
   +mapa("Museu de Arte do Rio","Museu de Arte do Rio, Praça Mauá, Rio de Janeiro"),
 "Valor da entrada":"Fonte: site oficial, consultado em 13/set/2026. <b>Inteira R$ 20</b> "
   "(≈ US$ 4), <b>meia R$ 10</b>, e <b>terça-feira gratuita para todos</b>.<br>"
   "<b>Gratuidade permanente</b>, no texto do próprio museu: alunos da rede pública de ensino "
   "fundamental e médio; crianças até 5 anos; pessoas a partir de 60 anos; professores da rede "
   "pública do município do Rio; funcionários de museus; vizinhos do MAR; guias de turismo.<br>"
   "<b>Meia-entrada:</b> pessoas até 21 anos; pessoas de 15 a 29 anos com ID Jovem; estudantes; "
   "professores particulares; pessoas com deficiência e acompanhantes; e — <b>este é o único dos "
   "quatro pontos com faixa de morador</b> — <b>pessoas nascidas na cidade do Rio de Janeiro e "
   "moradores da cidade do Rio de Janeiro</b>. Documentação comprobatória exigida em todos os casos.<br>"
   "O museu também faz gratuidades extraordinárias: em março de 2026, pelos 13 anos, <b>todos os "
   "sábados do mês foram gratuitos</b>. Vale olhar a seção de notícias do site antes de ir.",
 "Pontos de referência":"Praça Mauá, o Museu do Amanhã do outro lado, a Orla Conde e o Boulevard "
   "Olímpico. O Palacete Dom João VI, que é metade do próprio museu, é ele mesmo um marco "
   "arquitetônico da praça.",
 "Metrô mais próximo":"<b>VLT Carioca — Parada dos Museus, Linha 1</b>, a mesma do Museu do "
   "Amanhã, a cerca de 3 minutos a pé. De metrô, <b>Uruguaiana — Linhas 1 e 2</b> é a mais próxima. "
   +flag("Sem tempo oficial")+" o tempo a pé não foi confirmado em fonte oficial.",
 "Visitantes por ano":"<b>230.242 visitantes de janeiro a julho de 2026</b>, pelo balanço da "
   "Secretaria Municipal de Cultura. <b>Mais de 5 milhões acumulados</b> desde 2013.<br>"
   "Para escala: a rede cultural pública do Rio recebeu <b>3.000.877 visitas de janeiro a julho de "
   "2026</b>, alta de 21,5% sobre o mesmo período de 2025. "+flag("Não encontrado")+" total de um "
   "ano-calendário fechado.",
 "Menor visitação e temperatura":"Mesmo padrão do vizinho: vale de junho a agosto, com julho a "
   "15 °C e 25 °C e agosto o mais seco, 35 mm de chuva (Climatempo). "+flag("Sem dado mensal")+
   " a série mensal do MAR não é publicada. Dentro da semana, a terça-feira gratuita é "
   "previsivelmente a mais cheia.",
 "Curiosidades":ul([
   "O museu ocupa dois prédios de épocas e estilos opostos — o Palacete Dom João VI, eclético e "
   "tombado, e um antigo terminal rodoviário modernista — costurados por uma laje ondulada.",
   "Foi inaugurado em 1º de março de 2013, no aniversário da cidade do Rio de Janeiro.",
   "Desde janeiro de 2021 a gestão é da Organização dos Estados Ibero-americanos; o museu nasceu de "
   "parceria entre a Prefeitura do Rio e a Fundação Roberto Marinho.",
   "Fotografia é permitida sem flash na maior parte do acervo, com restrições sinalizadas em obras "
   "específicas."]),
 "Fatos históricos":"Inaugurado em <b>1º de março de 2013</b>, projeto do escritório carioca "
   "<b>Bernardes + Jacobsen Arquitetura</b>. São 15.000 m² de complexo, oito salas de exposição "
   "somando cerca de 2.400 m² em quatro andares, mais a <b>Escola do Olhar</b>, que ocupa o prédio "
   "modernista. Faz parte do programa de revitalização do Porto Maravilha.",
 "Dias em que não funciona":"<b>Fecha às quartas-feiras.</b> Visitação das <b>11h às 18h</b>, com "
   "última entrada às 17h.<br>"+flag("Fontes oficiais divergem")+" sobre o horário: a página de "
   "horários e ingressos diz 11h às 18h; a de dúvidas frequentes do mesmo museu diz 10h30 às 17h, de "
   "quinta a terça; e a notícia dos 13 anos diz 11h às 18h, de terça a domingo. <b>As três concordam "
   "que o fechamento semanal é na quarta-feira</b> — adotamos aqui o horário da página mais "
   "específica, e a abertura de segunda-feira fica em dúvida. Confirme por telefone: (21) 3031-2741.<br>"
   "<b>Acessibilidade:</b> três cadeiras de rodas e três carrinhos de bebê disponíveis na bilheteria, "
   "bancos de descanso em todos os andares, banheiros e bebedouros por andar, cães-guia e animais de "
   "suporte emocional permitidos com documentação.",
 "Pontos turísticos próximos":"Museu do Amanhã, na mesma praça. Mural Etnias, de Kobra. Cais do "
   "Valongo, patrimônio mundial da UNESCO. AquaRio. Mosteiro de São Bento. Todos a poucos minutos a "
   "pé pelo Porto. "+flag("Sem distância oficial")}
},
{
 "id":"theatro-municipal","nome":"Theatro Municipal","tag":"Teatro e visita guiada","img":"theatro",
 "preco":"R$ 20","preconota":"visita guiada; só na bilheteria, no dia",
 "campos":{
 "Endereço":"Praça Floriano, s/nº — Centro, CEP 20031-050. Fica na <b>Cinelândia</b>, no quarteirão "
   "entre a Avenida Rio Branco e a Praça Floriano, de frente para a praça, entre a Biblioteca "
   "Nacional e o Museu Nacional de Belas Artes, do lado oposto à Câmara Municipal. A fachada com "
   "cúpulas douradas e as águias de bronze é a referência. <b>A bilheteria das visitas guiadas fica "
   "na entrada lateral, pelo Boulevard, na Av. 13 de Maio.</b>"
   +mapa("Theatro Municipal do Rio de Janeiro","Theatro Municipal do Rio de Janeiro, Praça Floriano, Cinelândia"),
 "Valor da entrada":"<b>Visita guiada: R$ 20 a inteira e R$ 10 a meia-entrada.</b> Há ainda a "
   "<b>meia-entrada solidária</b>: paga-se R$ 10 doando <b>1 kg de alimento não perecível</b>.<br>"
   "<b>Os ingressos são vendidos exclusivamente de forma presencial, na bilheteria, no próprio dia "
   "da visita.</b> Não há venda online nem agendamento prévio para a visita regular. A bilheteria "
   "abre <b>a partir das 10h</b>, na entrada lateral pelo Boulevard (Av. 13 de Maio). Formas de "
   "pagamento: dinheiro, Pix ou cartão de crédito e débito. <b>Limite de um ingresso por pessoa.</b><br>"
   "<b>Chegue cedo.</b> Sem venda antecipada e com uma unidade por pessoa, a fila da bilheteria é o "
   "único caminho, e as sessões esgotam.<br>"
   +flag("Não encontrado")+" dia de gratuidade para a visita guiada.",
 "Pontos de referência":"A Praça Floriano e a Cinelândia, em frente. A Biblioteca Nacional e o "
   "Museu Nacional de Belas Artes, vizinhos imediatos. A Câmara Municipal, no Palácio Pedro Ernesto, "
   "do outro lado da praça. A Avenida Rio Branco corre ao lado.",
 "Metrô mais próximo":"<b>Cinelândia — Linhas 1 e 2</b>, saída para a Avenida Rio Branco: o teatro "
   "fica praticamente na saída da estação, <b>menos de 2 minutos a pé</b>. Esta é uma das poucas "
   "orientações de acesso que o próprio MetrôRio publica. De VLT, a <b>Parada Cinelândia, Linha 1</b>, "
   "fica a cerca de 2 minutos, e a Parada Carioca a cerca de 5.",
 "Visitantes por ano":flag("Não encontrado")+" o Theatro é equipamento <b>estadual</b>, não "
   "municipal, então não aparece no balanço da Secretaria Municipal de Cultura, que é a fonte que "
   "publica números do Museu do Amanhã e do MAR. Procuramos no site oficial, na Secretaria de Estado "
   "de Cultura e na imprensa: nenhum número de público anual nem de visitantes da visita guiada foi "
   "localizado.",
 "Menor visitação e temperatura":"Aqui a regra geral da baixa temporada <b>pode não valer</b>. "
   "Julho é mês de férias escolares e o Theatro costuma reforçar a programação no período — ou seja, "
   "o mês mais barato da cidade é justamente um dos mais movimentados aqui. No clima, julho tem "
   "15 °C de mínima e 25 °C de máxima, e agosto é o mês mais seco, com 35 mm (Climatempo). "
   +flag("Sem dado mensal")+" não há série de visitação publicada.",
 "Curiosidades":ul([
   "As três cúpulas foram restauradas com 219 mil folhas de ouro na reforma de 2009–2010.",
   "No subsolo funciona o Restaurante Assírius, com decoração em estilo assírio — um ambiente "
   "temático raríssimo em teatros de ópera.",
   "A capacidade mudou três vezes: 1.739 lugares na inauguração, em 1909; 2.205 depois da reforma de "
   "1934; e 2.361 lugares hoje.",
   "Passaram por este palco Maria Callas, Arturo Toscanini, Sarah Bernhardt e Igor Stravinsky."]),
 "Fatos históricos":"Inaugurado em <b>14 de julho de 1909</b>, na presidência de Nilo Peçanha — o "
   "teatro completou 117 anos em julho de 2026. Projeto de <b>Francisco de Oliveira Passos</b>, filho "
   "do prefeito Pereira Passos, responsável pela reforma urbana da época, com colaboração do francês "
   "<b>Albert Guilbert</b>, inspirado na Ópera de Paris de Charles Garnier. Ampliado em 1934, quando "
   "a capacidade foi a 2.205 lugares. Fechou integralmente para restauro de <b>19 de outubro de 1975 "
   "a 15 de março de 1978</b>, e passou por nova restauração em 2009–2010, com reinauguração em 27 de "
   "maio de 2010.",
 "Dias em que não funciona":"<b>A visita guiada acontece de quarta a sábado</b>, com esta grade:<br>"
   "<b>Quarta:</b> 16h. <b>Quinta:</b> 11h, 14h e 16h. <b>Sexta:</b> 11h, 14h e 16h, com turmas "
   "extras às 14h15 em espanhol e às 16h15 em inglês, ambas com mínimo de 2 pessoas. "
   "<b>Sábado:</b> 11h e 12h15.<br>"
   "<b>Não há visitas de domingo a terça-feira.</b> A terça é reservada a instituições com "
   "agendamento prévio por e-mail (visitaguiada.tmrj@gmail.com). A visita dura cerca de 45 minutos, "
   "conduzida por educador, passando por salões, escadarias e a sala de espetáculos.<br>"
   +flag("Não encontrado")+" calendário de fechamento por feriado, manutenção ou conflito com "
   "ensaios e montagens de ópera e balé. A programação pode mudar sem aviso prévio, e o site oficial "
   "estava inacessível na apuração.",
 "Pontos turísticos próximos":"Museu Nacional de Belas Artes e Biblioteca Nacional, os dois a "
   "poucos passos, do outro lado da Av. Rio Branco. Praça Floriano e a Cinelândia, em frente. "
   "Confeitaria Colombo, na matriz da Rua Gonçalves Dias. Real Gabinete Português de Leitura e os "
   "Arcos da Lapa, ambos a uma caminhada curta pelo Centro. "+flag("Sem distância oficial")}
},
{
 "id":"real-gabinete","nome":"Real Gabinete Português de Leitura","tag":"Biblioteca","img":"gabinete",
 "preco":"Grátis","preconota":"fechado sábado, domingo e feriado",
 "campos":{
 "Endereço":"Rua Luís de Camões, 30 — Centro. É uma transversal curta e estreita que sai da Praça "
   "Tiradentes, ao lado do Largo de São Francisco de Paula. A fachada é inconfundível: <b>calcário "
   "lavrado importado de Lisboa</b>, em estilo neomanuelino, com estátuas de navegadores e escritores "
   "portugueses. É fácil passar reto — a rua é pequena e a fachada fica quase colada à calçada, sem "
   "recuo."+mapa("Real Gabinete Português de Leitura","Real Gabinete Português de Leitura, Rua Luís de Camões 30, Rio de Janeiro"),
 "Valor da entrada":"<b>Gratuita</b> para a visitação regular. Não há inteira, meia, faixa de "
   "criança, 60+ nem morador do Rio, porque não há cobrança — e, por consequência, <b>não existe "
   "“dia de gratuidade”</b>: todos os dias úteis são gratuitos.<br>"
   "<b>Visitas guiadas pagas e opcionais</b> são oferecidas pelo próprio Gabinete, <b>terças às "
   "10h30 e quintas às 15h</b>, com cerca de 1 hora de duração, apenas em português, e início "
   "pontual — chegue 10 minutos antes. "+flag("Preço não encontrado")+" a página oficial de venda "
   "não exibia valor na consulta de 13/set/2026.<br>"
   +flag("Fontes divergem")+" sobre os idiomas: o canal oficial de venda diz “apenas em "
   "português”; um guia de terceiros afirma haver visitas em português, inglês e espanhol. "
   "Prevalece o canal oficial.",
 "Pontos de referência":"Praça Tiradentes e o Largo de São Francisco de Paula, com a igreja de "
   "mesmo nome, ambos a poucos passos. A Confeitaria Colombo, na matriz, fica perto. Do lado de "
   "dentro, o marco é o salão de leitura: três andares de estantes em ferro fundido sob uma clarabóia "
   "em vitral com motivos marítimos.",
 "Metrô mais próximo":"<b>Uruguaiana — Linhas 1 e 2</b> é a estação de referência, a 5 a 8 minutos "
   "a pé. <b>Carioca — Linhas 1 e 2</b> é a alternativa, cerca de 10 minutos. De VLT, a <b>Parada "
   "Praça Tiradentes, Linha 2</b>, é a mais próxima. "+flag("Sem tempo oficial")+" o MetrôRio não "
   "publica a caminhada.",
 "Visitantes por ano":flag("Não encontrado")+" <b>o Real Gabinete é uma associação privada "
   "luso-brasileira</b>, não integra a rede pública municipal e não tem obrigação de divulgar "
   "estatística de público — por isso não aparece no balanço da Secretaria Municipal de Cultura. "
   "Procuramos no site oficial, no portal Visite Museus do IBRAM e na imprensa brasileira e "
   "portuguesa. Nenhum número confiável foi localizado.",
 "Menor visitação e temperatura":"Baixa temporada de junho a agosto, com julho a 15 °C e 25 °C e "
   "agosto o mais seco, 35 mm (Climatempo). "+flag("Sem dado mensal")+"<br>"
   "<b>A dica aqui é de dia e hora, e essa dá para defender sem número:</b> como o Gabinete só abre "
   "em dias úteis, a janela com menos gente é o <b>horário de abertura, às 10h, numa segunda, quarta "
   "ou sexta</b> — porque as terças e as quintas concentram os grupos das visitas guiadas, às 10h30 "
   "e às 15h.",
 "Curiosidades":ul([
   "É Depósito Legal da Biblioteca Nacional de Portugal desde 1935 — recebe exemplares de tudo o que "
   "se publica em Portugal, o que faz dele a biblioteca com o maior acervo português fora de Portugal.",
   "Guarda uma primeira edição de <i>Os Lusíadas</i>, de Camões, e o manuscrito de <i>Amor de "
   "Perdição</i>, de Camilo Castelo Branco.",
   "Recebeu o título de “Real” em 1906, concedido pelo rei D. Carlos de Portugal; antes "
   "disso era apenas Gabinete Português de Leitura.",
   "A fachada em calcário foi lavrada em Lisboa e trazida por navio, pedra a pedra, para montagem "
   "no Rio."]),
 "Fatos históricos":"Fundado em <b>maio de 1837</b> por 43 imigrantes portugueses no Rio de "
   "Janeiro, para preservar e difundir a língua e a cultura portuguesas. O edifício foi construído "
   "entre 1880 e 1887 e <b>inaugurado em dezembro de 1888</b>, na presença da princesa Isabel e do "
   "conde d'Eu. Projeto do arquiteto português <b>Rafael da Silva e Castro</b>, em estilo "
   "<b>neomanuelino</b>, evocando a Era dos Descobrimentos, com esculturas do Infante D. Henrique, "
   "Vasco da Gama, Pedro Álvares Cabral e Camões, por Simões de Almeida. Tornou-se biblioteca aberta "
   "ao público em 1900; ganhou o título Real em 1906; recebeu em 1921 a doação de mais de 4.000 "
   "volumes da coleção da mãe de João do Rio; e virou Depósito Legal de Portugal em 1935. O acervo "
   "passa de <b>350 mil obras</b>. "+flag("Fontes divergem")+" uma fonte fala em cerca de 400 mil "
   "volumes; ficamos com o número mais conservador.",
 "Dias em que não funciona":"<b>Fechado aos sábados, domingos e feriados.</b> Funciona de <b>segunda "
   "a sexta, das 10h às 17h</b>. <b>Este é o ponto mais restritivo do Centro</b> e talvez a "
   "informação mais valiosa deste guia: quem monta o roteiro de Centro para o fim de semana não entra "
   "aqui. "+flag("Não encontrado")+" calendário de fechamento por manutenção.<br>"
   "<b>Fotografia:</b> permitida sem flash, sem tripé e em silêncio — é uma biblioteca em "
   "funcionamento, não um museu, e há leitores trabalhando nas mesas. "+flag("Não confirmado na fonte primária")+
   " o site oficial estava inacessível na apuração; a regra acima vem de fonte secundária que declara "
   "usar o site do Gabinete. Regras de foto mudam, e o Gabinete é conhecido por restringir ensaios "
   "comerciais — confirme na portaria.",
 "Pontos turísticos próximos":"Largo de São Francisco de Paula e a igreja de mesmo nome, a poucos "
   "passos. Praça Tiradentes, na esquina. Confeitaria Colombo, na matriz. Centro Cultural Banco do "
   "Brasil, Theatro Municipal e a Rua do Lavradio, todos a uma caminhada pelo Centro. "
   +flag("Sem distância oficial")}
}]}
