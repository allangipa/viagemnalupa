# -*- coding: utf-8 -*-
from lib import mapa, flag, ul

IPMA = ("Clima pelas normais de 30 anos do IPMA, estação Lisboa / Instituto Geofísico, série "
  "1991–2020: <b>janeiro</b> é o mês mais frio (média de 11,8 °C e mínima média de 8,6 °C), "
  "<b>novembro</b> o mais chuvoso (133,9 mm), <b>agosto</b> o mais quente (23,8 °C de média, "
  "28,8 °C de máxima) e <b>julho</b> o mais seco — 2,6 mm no mês inteiro.")

G2 = {
 "titulo": "Centro histórico e miradouros",
 "intro": "Aqui está a notícia que reescreve qualquer roteiro de Lisboa escrito antes de 2026: "
   "os ascensores históricos da cidade estão parados, o Elevador de Santa Justa incluído. O que "
   "sobra de pé — castelo, praça e miradouros — continua de graça ou quase.",
 "pontos": [
{
 "id":"castelo-sao-jorge","nome":"Castelo de São Jorge","tag":"Castelo","img":"castelo",
 "preco":"€ 17","preconota":"acabou a gratuidade para lisboeta",
 "campos":{
 "Endereço":"Rua de Santa Cruz do Castelo, 1100-129 Lisboa. <b>O endereço não ajuda</b>: o castelo "
   "não tem fachada de rua. A referência que funciona é o <b>Miradouro das Portas do Sol</b> — de "
   "lá você olha para cima e vê a muralha ameada. Sobe-se pela Rua do Chão da Feira."
   +mapa("Castelo de São Jorge","Castelo de Sao Jorge, Rua de Santa Cruz do Castelo, Lisboa"),
 "Valor da entrada":"Fonte: site oficial, consultado em 13/set/2026. <b>Adulto € 17</b> (≈ R$ 101). "
   "<b>Jovem de 13 a 25 anos: € 8,50.</b> <b>Sénior a partir de 65: € 14.</b> Pessoas com "
   "necessidades específicas e profissionais da cultura: € 12. Funcionários da Câmara e protocolo "
   "com ensino superior: € 13. Grupos escolares: € 1,50 por aluno.<br>"
   "<b>Gratuito</b> para crianças <b>até 12 anos</b>, portadores do Lisboa Card, associados da EGEAC "
   "com um acompanhante, acompanhante de pessoa com necessidades específicas, antigos combatentes e "
   "membros de ICOM, ICOMOS, APOM e APAC. "+flag("Não existe")+" bilhete de família na tabela "
   "oficial. <b>Preço fixo</b>, sem variação por data ou procura. "+flag("Não encontrado")+" dia "
   "ou horário gratuito na tabela em vigor.<br>"
   "<b>E aqui está a mudança que quase ninguém sabe: acabou a entrada gratuita para morador de "
   "Lisboa.</b> Os lisboetas entravam de graça <b>desde 2005</b>. Por decisão do Tribunal Central "
   "Administrativo Sul, com efeito a <b>3 de julho de 2025</b>, essa gratuidade caiu. A EGEAC "
   "recorreu, <b>mas o recurso não suspende a cobrança</b>. Hoje o lisboeta paga os mesmos € 17 que "
   "você. "+flag("Estado do recurso não encontrado")+"<br>"
   "<b>Pegadinha do Lisboa Card que a própria loja oficial admite:</b> a entrada é livre com o "
   "cartão <b>exceto para crianças de 13 a 15 anos</b>, que pagam os € 8,50 mesmo assim.",
 "Pontos de referência":"Miradouro das Portas do Sol e Miradouro de Santa Luzia, logo abaixo. O "
   "Largo do Chão da Feira, onde fica a entrada. A Costa do Castelo contornando a colina. E os "
   "bairros que o cercam: Alfama, Mouraria e a Sé.",
 "Metrô mais próximo":"<b>Martim Moniz — Linha Verde</b>, com acessos na Rua Martim Moniz, aberta "
   "das 6h30 à 1h. Alternativa: <b>Baixa-Chiado</b>, nas linhas Azul e Verde. <b>Elétricos 28E e "
   "12E</b>, paragem <b>Portas do Sol</b>. Autocarro 737. "+flag("Sem tempo a pé")+" a fonte oficial "
   "não publica, e não estimamos — mas é subida de calçada em qualquer caminho que você escolha.",
 "Visitantes por ano":"<b>1.758.813</b> — e é preciso dizer o que esse número é: trata-se da "
   "<b>previsão oficial para 2025</b>, no campo “Público Previsional” do documento de "
   "gestão da EGEAC, <b>não do realizado</b>. "+flag("Realizado não encontrado")+" o documento "
   "equivalente do ano seguinte devolveu erro.<br>"
   "A imprensa refere 1,7 milhão em 2024, com <b>apenas 1,1% de residentes</b> usando a gratuidade — "
   "é o dado que dimensiona a polémica judicial descrita acima.",
 "Menor visitação e temperatura":"<b>Não existe série mensal publicada.</b> "+flag("Sem dado mensal")+
   " Nem a EGEAC nem o monumento divulgam mês a mês, então <b>não é possível apontar o mês de menor "
   "movimento com fonte</b>.<br>"+IPMA+"<br>"
   "<b>E aqui o clima pesa mais que na média:</b> a visita ao castelo é quase toda em muralha "
   "exposta, sem cobertura. Novembro e outubro, os dois meses mais chuvosos, são os que estragam a "
   "visita.",
 "Curiosidades":ul([
   "A EGEAC classifica-o como o Monumento Nacional mais visitado do país.",
   "Câmara Escura e Sítio Arqueológico só se visitam com visita guiada.",
   "<b>As visitas guiadas “À Descoberta do Castelo” já vêm incluídas no bilhete</b> — "
   "muita gente paga tour por fora sem saber que não precisava.",
   "Cães não entram, exceto cães-guia.",
   "A origem do sítio é islâmica, o que a própria EGEAC afirma."]),
 "Fatos históricos":"Origem islâmica. A EGEAC afirma a classificação como <b>Monumento "
   "Nacional</b>, mas "+flag("não confirmamos")+" o diploma e a data: a consulta por código na base "
   "de Património Imóvel devolveu o registo de outro imóvel, no Porto, e não inventamos decreto. "
   +flag("Também não encontrado")+" descrição, em fonte oficial do monumento, do dano específico "
   "causado pelo terramoto de 1755.<br>"
   "A mudança recente concreta e documentada é outra: <b>o fim da gratuidade a residentes, em 3 de "
   "julho de 2025</b>, por decisão judicial.",
 "Dias em que não funciona":"<b>Não há fecho semanal</b> — abre todos os dias. Encerra em <b>1 de "
   "janeiro, 1 de maio, 24, 25 e 31 de dezembro</b>; a 31 fecha a partir das 12h30.<br>"
   "<b>Verão, de 1 de março a 31 de outubro: 9h às 21h</b>, com última admissão às 20h30. "
   "<b>Inverno, de 1 de novembro ao fim de fevereiro: 9h às 18h</b>, última admissão às 17h30.<br>"
   "<b>A armadilha número um está aqui, e não é o horário do portão:</b> os <b>adarves e torres "
   "fecham antes do monumento</b>. No verão podem fechar <b>entre as 18h e as 21h</b>, conforme a "
   "luz e o tempo; no inverno, às 17h30. Entrar às 19h30 em agosto com bilhete válido pode "
   "significar encontrar a muralha — a parte fotogénica — já fechada.<br>"
   +flag("Não publicado")+" se o bilhete tem hora marcada ou vale o dia todo: as três páginas "
   "oficiais não mencionam sessão nem faixa horária, e não afirmamos nem que vale nem que não vale. "
   +flag("Sem limite publicado")+" também não há lotação máxima ou aviso de esgotamento.<br>"
   "<b>O problema real documentado não é esgotar, é fila mal sinalizada:</b> há duas entradas, uma "
   "para quem comprou online e outra para a bilheteira, e a de online costuma estar vazia enquanto a "
   "outra tem fila — porque o castelo recomenda comprar online mas não comunica isso no local. "
   "<b>Compre online antes de subir</b>, não para garantir lugar, mas para entrar pela porta certa.",
 "Pontos turísticos próximos":"Portas do Sol e Santa Luzia, Sé de Lisboa, Alfama, Mouraria, Largo "
   "da Graça e Senhora do Monte, São Vicente de Fora, Panteão Nacional, Feira da Ladra e a Baixa. "
   +flag("Sem distância oficial")}
},
{
 "id":"elevador-santa-justa","nome":"Elevador de Santa Justa","tag":"Ascensor — fechado","img":"santajusta",
 "preco":"Fechado","preconota":"cabine e miradouro, sem data de reabertura",
 "campos":{
 "Endereço":"Rua de Santa Justa, junto ao Largo do Carmo, Santa Maria Maior. "+flag("Fontes divergem")+
   " o Turismo de Lisboa dá “Rua de Santa Justa, 1150”, código postal incompleto, e a "
   "ficha patrimonial dá coordenadas mas não o código. Na rua é impossível errar: é uma <b>torre de "
   "ferro neogótico de 45 metros encaixada entre prédios da Baixa</b>."
   +mapa("Elevador de Santa Justa","Elevador de Santa Justa, Rua de Santa Justa, Lisboa"),
 "Valor da entrada":"<b>Hoje não se vende bilhete: está encerrado.</b> A tarifa publicada pela "
   "Carris, em vigor desde 1/jan/2026, é de <b>€ 6,20</b> a bordo, válida para até duas viagens.<br>"
   "<b>Para dimensionar o quanto isso é caro:</b> € 6,20 é quase o preço do <b>passe Carris/Metro "
   "de 24 horas inteiro, que custa € 7,25</b> e dá metro, autocarro e elétrico ilimitados o dia "
   "todo. Por uma subida de menos de um minuto. A fama de caro é merecida, e agora está documentada "
   "com a tabela ao lado.<br>"
   "O bilhete só do miradouro do topo era <b>€ 5</b>, apenas com cartão e lotação de 20 pessoas — "
   "mas "+flag("esse é valor de 2025")+" e o de 2026 não está publicado. Não escrevemos € 5 como se "
   "fosse atual.<br>"
   +flag("Lacuna estrutural")+" não existem faixas de criança, jovem, sénior, família ou grupo — "
   "o elevador é tarifado como transporte público, não como monumento.<br>"
   "<b>Lisboa Card:</b> a viagem é livre, <b>mas o miradouro do topo fica de fora do cartão</b>. O "
   "cartão paga a subida, não a varanda.",
 "Pontos de referência":"O Rossio e a Praça da Figueira, a Rua Augusta, o Largo do Carmo com o "
   "Convento do Carmo no topo, e o Chiado.",
 "Metrô mais próximo":"<b>Baixa-Chiado — linhas Azul e Verde</b>, das 6h30 à 1h, com saídas no "
   "Largo do Chiado e na Rua do Crucifixo. <b>Rossio — Linha Verde.</b><br>"
   +flag("Listagem oficial desatualizada")+" a ficha da estação no site do metro <b>ainda lista o "
   "Elevador de Santa Justa e o Elevador da Bica como ligações à superfície, sem qualquer aviso de "
   "que estão encerrados</b>. Se você planejou Lisboa por essa página, planejou com informação "
   "incompleta.",
 "Visitantes por ano":flag("Não encontrado")+" procuramos no site da Carris, no Turismo de Lisboa "
   "e na ficha patrimonial. A cifra de “cerca de 1 milhão” circula na imprensa <b>sem "
   "origem oficial</b>, e por isso não a publicamos.",
 "Menor visitação e temperatura":"<b>Não existe série mensal</b> — a Carris não divulga contagem "
   "por mês. "+flag("Sem dado mensal")+"<br>"+IPMA,
 "Curiosidades":ul([
   "É o único ascensor <b>vertical</b> de Lisboa — todos os outros são funiculares, que sobem "
   "encostas em plano inclinado.",
   "Funcionou a vapor de 1902 a 1907, e só depois foi eletrificado.",
   "São 45 metros de altura e capacidade para 29 passageiros.",
   "O nome oficial na base patrimonial vem primeiro como <b>“Elevador do Carmo”</b>: a "
   "ficha diz “Elevador do Carmo ou de Santa Justa”.",
   "<b>Tradição, não fato:</b> repete-se em toda parte, inclusive na imprensa portuguesa, que Raul "
   "Mesnier du Ponsard foi discípulo de Eiffel. <b>A ficha oficial do património não afirma isso</b> "
   "— atribui o projeto a Mesnier du Ponsard, a mecânica a Lambert d'Argent e os desenhos a Jacinto "
   "Augusto Mariares, e não menciona Eiffel em lugar nenhum."]),
 "Fatos históricos":"Projetado em 1900 e <b>inaugurado em 1902</b>, a vapor, eletrificado em 1907. "
   "Autor: <b>Raul Mesnier du Ponsard</b>. Duas torres metálicas de 45 metros com ornamentação "
   "neogótica. <b>Monumento Nacional pelo Decreto n.º 5/2002</b>, publicado no <i>Diário da "
   "República</i> de 19 de fevereiro de 2002.<br>"
   "O terramoto de 1755 não se aplica — o elevador é 147 anos posterior. Mas o Largo do Carmo, onde "
   "ele desemboca, guarda a <b>ruína do Convento do Carmo</b>, que é o monumento-cicatriz do "
   "terramoto. Houve renovação em 2017 e, em 2025, a lotação do miradouro foi reduzida a 20 pessoas. "
   "Desde setembro de 2025 está parado.",
 "Dias em que não funciona":"<b>Nenhum, porque não funciona nenhum dia.</b> Cabine e miradouro "
   "encerrados, sem data de reabertura publicada.<br>"
   "<b>O motivo é grave e vale contexto:</b> em <b>3 de setembro de 2025 o Ascensor da Glória "
   "descarrilou e matou 16 pessoas</b>, deixando 24 feridos. A Carris suspendeu preventivamente "
   "todos os ascensores históricos. Um ano depois, o quadro é este: a <b>Glória</b> não será "
   "reparada e sim substituída por equipamento novo, com concurso internacional até ao primeiro "
   "trimestre de 2027 e operação estimada para o primeiro semestre de 2029; a <b>Bica</b> e o "
   "<b>Lavra</b> seguem fechados sem data; o <b>Santa Justa</b> segue fechado; e apenas o "
   "<b>Funicular da Graça</b> voltou, em 30 de abril de 2026.<br>"
   +flag("Fontes oficiais divergem sobre o motivo")+" a Carris fala em suspensão preventiva de "
   "segurança; a loja oficial do Turismo de Lisboa diz que está fechado “para obras de "
   "restauro”. São duas fontes oficiais com duas explicações. Registramos as duas.<br>"
   "<b>A alternativa gratuita, com a ressalva honesta:</b> o <b>Largo do Carmo é público</b> e "
   "chega-se a ele a pé pelo Chiado sem pagar nada — a passagem superior do elevador desemboca ali, "
   "e é por isso que o nome oficial do bem é “Elevador do Carmo”. <b>Mas não leva ao "
   "mesmo lugar que o bilhete levava.</b> Os € 5 davam acesso à plataforma no <b>topo da torre</b>, "
   "acima do nível da passagem, subida por escada em caracol — é dali que sai a foto. A passagem do "
   "Carmo é o andar de baixo; a plataforma paga é o de cima. Hoje as duas estão fechadas. Vá ao "
   "Largo do Carmo de graça, fique encostado à torre de ferro e visite as Ruínas do Carmo ao lado — "
   "<b>não é a mesma vista, e não vamos dizer que é</b>.",
 "Pontos turísticos próximos":"Convento e Museu Arqueológico do Carmo, Rossio, Praça da Figueira, "
   "Rua Augusta, Arco da Rua Augusta, Praça do Comércio e Chiado. "+flag("Sem distância oficial")}
},
{
 "id":"praca-do-comercio","nome":"Praça do Comércio e o Arco da Rua Augusta","tag":"Praça e mirante","img":"comercio",
 "preco":"Grátis","preconota":"a praça; subir ao arco é pago",
 "campos":{
 "Endereço":"Praça do Comércio, também chamada Terreiro do Paço, em Santa Maria Maior. "
   +flag("Fontes divergem")+" o Turismo de Lisboa dá para o arco “Rua Augusta, 2, 1100-053” "
   "e o operador dá “Rua Augusta 2-10, 1100-148”. Dois códigos postais para o mesmo "
   "arco; não escolhemos.<br>"
   "<b>O arco é a referência — mas a porta da visita não fica no arco central.</b> Fica "
   "lateralmente, na Rua Augusta, num átrio pequeno. Quem procura porta no meio do arco não acha."
   +mapa("Praça do Comércio","Praca do Comercio, Terreiro do Paco, Lisboa"),
 "Valor da entrada":"<b>A praça é pública: não se paga nada, não tem porta nem horário.</b> "
   "Paga-se para subir ao arco.<br>"
   "<b>E aqui temos de ser francos: </b>"+flag("o preço do arco não está confirmado em fonte oficial")+
   ". O Turismo de Lisboa tem ficha do ponto mas <b>não publica preço</b>; o domínio próprio do arco "
   "<b>não resolve</b>; os revendedores só mostram valor “a partir de” em dólar, e um deles "
   "marca a experiência como indisponível. Guias em português falam em “cerca de € 4 a "
   "€ 4,50” — <b>rejeitamos, porque é estimativa sem fonte</b>. Leve cartão e confirme na "
   "bilheteira.<br>"
   "Crianças pequenas não pagam — duas fontes secundárias convergem em gratuidade abaixo dos 5 anos, "
   "mas <b>a idade de corte não está confirmada oficialmente</b>. "+flag("Não encontrado")+" faixas "
   "de jovem, estudante, sénior, família ou grupo, nem desconto de residente.<br>"
   "<b>Lisboa Card: entrada livre</b>, e isso está confirmado tanto pelo Turismo de Lisboa quanto "
   "pela loja oficial. <b>Como o preço avulso não está publicado mas a gratuidade está, o arco é "
   "justamente onde o cartão resolve a incerteza.</b>",
 "Pontos de referência":"O Cais das Colunas, descendo até a água. A estátua equestre de D. José I "
   "no centro. A Rua Augusta saindo pelo arco. O Lisboa Story Centre e o Pátio da Galé, nas alas. E "
   "as ruas do Ouro e da Prata, paralelas.",
 "Metrô mais próximo":"<b>Terreiro do Paço — Linha Azul</b>, das 6h30 à 1h, com saída à superfície "
   "no Cais da Alfândega, três acessos e elevador. Também serve <b>Baixa-Chiado</b>, nas linhas Azul "
   "e Verde. Elétricos 15E, 25E e 28E servem a zona.<br>"
   "<b>Esta é uma das raras estações de Lisboa onde você emerge dentro do ponto turístico</b> — a "
   "estação abre diretamente na praça. Há ainda o <b>terminal fluvial do Terreiro do Paço</b> na "
   "própria praça; o passe de 24h que inclui o barco custa € 10,35.",
 "Visitantes por ano":flag("Não encontrado")+" nem para a praça nem para o arco. A praça é espaço "
   "público <b>sem controlo de entrada</b> — não tem nem pode ter contagem. O arco tem bilheteira, "
   "logo tem contagem interna, <b>mas o operador não publica</b>. As avaliações do Tripadvisor "
   "citadas na ficha oficial não são estatística de visitação e não as apresentamos como tal.",
 "Menor visitação e temperatura":"<b>Não existe série mensal publicada.</b> "+flag("Sem dado mensal")+
   "<br>"+IPMA+"<br>"
   "<b>Nota prática:</b> a praça é <b>totalmente aberta e virada ao Tejo, sem sombra</b>. Em julho e "
   "agosto o sol do meio-dia ali é castigo; em novembro e dezembro é onde a chuva com vento do rio "
   "apanha em cheio.",
 "Curiosidades":ul([
   "A praça foi desenhada como uma cidade nova: Eugénio dos Santos traçou oito ruas no sentido "
   "norte-sul cruzando nove no sentido este-oeste.",
   "<b>O arco demorou cerca de um século.</b> Foi projetado no pós-terramoto e só concluído na "
   "década de 1860, por Veríssimo José da Costa.",
   "A estátua de D. José I foi concluída em 1775 por Machado de Castro — vinte anos exatos depois "
   "do terramoto.",
   "Os pavilhões de esquina repetem o desenho de uma torre do antigo Paço Real: é uma citação "
   "arquitetónica do palácio que o terramoto derrubou."]),
 "Fatos históricos":"Antes de 1755 chamava-se <b>Terreiro do Paço</b> e tinha um <b>Paço Real desde "
   "o século XVI</b>. O <b>terramoto de 1755</b> destruiu tudo, e a reconstrução coube a Sebastião "
   "José de Carvalho e Melo, o futuro Marquês de Pombal, com plano de <b>Eugénio dos Santos</b>: "
   "três blocos de três pisos, arcadas térreas, sacadas no piso intermédio e remate em cornija. O "
   "arco é projeto do mesmo Eugénio dos Santos, concluído nos anos 1860 por Veríssimo José da Costa, "
   "com esculturas de Antoine Calmels e Vítor Bastos.<br>"
   "<b>Monumento Nacional, classificada em 16 de junho de 1910.</b> De pátio de palácio real a praça "
   "cívica pombalina; hoje as alas abrigam ministérios.",
 "Dias em que não funciona":"<b>A praça não fecha:</b> é via pública, 24 horas, sem bilhete.<br>"
   "<b>A subida ao arco é outra história, e as fontes divergem.</b> O Turismo de Lisboa indicava "
   "10h às 19h; o operador diz 10h às 19h com última admissão 15 minutos antes, às 18h45; um "
   "revendedor diz 18h30. "+flag("Última entrada: 18h45 ou 18h30")+" e nenhuma dessas fontes é o "
   "monumento. Se for no fim do dia, chegue às 18h15.<br>"
   "Para feriados, as fontes secundárias indicam 24 e 31 de dezembro das 10h às 17h, <b>25 de "
   "dezembro encerrado</b> e 1 de janeiro das 10h às 17h — "+flag("não confirmado")+". "
   +flag("Não encontrado")+" fecho semanal e horário de verão.<br>"
   "<b>A regra que derruba a visita:</b> a subida termina em <b>escada estreita</b> e o mirante é "
   "pequeno; quem precisa de acessibilidade <b>tem de sinalizar no momento da reserva</b> — é "
   "“imprescindível indicar ao fazer a reserva”. Não dá para simplesmente aparecer.",
 "Pontos turísticos próximos":"Cais das Colunas, Rua Augusta, Elevador de Santa Justa (fechado), "
   "Rossio, Praça da Figueira, Lisboa Story Centre, MUDE, Sé, Time Out Market e o terminal fluvial. "
   +flag("Sem distância oficial")}
},
{
 "id":"miradouros-alfama","nome":"Miradouros de Alfama","tag":"Mirantes","img":"miradouros",
 "preco":"Grátis","preconota":"Portas do Sol e Senhora do Monte",
 "campos":{
 "Endereço":"<b>Portas do Sol:</b> Largo das Portas do Sol, em Alfama. <b>Senhora do Monte:</b> "
   "Rua da Senhora do Monte à Graça. "+flag("Código postal não encontrado")+" a ficha da Câmara "
   "devolveu erro de acesso e a página do Turismo de Lisboa devolveu página inexistente; nenhuma "
   "fonte alternativa publica.<br>"
   "<b>Nas Portas do Sol, a referência é a estátua branca de São Vicente</b>, segurando um barco com "
   "dois corvos; o 28E passa colado. Logo abaixo fica o <b>Miradouro de Santa Luzia</b>, com pérgula "
   "e azulejos — são dois miradouros vizinhos e diferentes, e quase todo mundo confunde. <b>Na "
   "Senhora do Monte, a referência é a pequena ermida branca</b>: o miradouro é literalmente o adro "
   "da capela."+mapa("Miradouro das Portas do Sol","Miradouro das Portas do Sol, Alfama, Lisboa"),
 "Valor da entrada":"<b>Grátis, os dois.</b> São espaços públicos ao ar livre, sem bilheteira. Por "
   "consequência não há faixas, não há inteira nem meia, não há preço fixo nem dinâmico, não há "
   "desconto de residente — e <b>não estão “incluídos no Lisboa Card” simplesmente porque "
   "não há entrada a pagar</b>. O que custa dinheiro ali é o quiosque e subir de transporte.",
 "Pontos de referência":"<b>Nas Portas do Sol:</b> a estátua de São Vicente, o Miradouro de Santa "
   "Luzia, a Igreja de Santa Luzia, o Museu de Artes Decorativas, a subida ao castelo e a vista "
   "sobre as cúpulas de São Vicente de Fora e do Panteão. <b>Na Senhora do Monte:</b> a ermida, o "
   "Largo da Graça, o Miradouro da Graça, o Convento da Graça e o topo do Caracol da Graça.",
 "Metrô mais próximo":"<b>Elétrico 28E, paragem Portas do Sol</b>, colada ao miradouro; o 12E serve "
   "a mesma zona. De metro, <b>Martim Moniz — Linha Verde</b>.<br>"
   "<b>E há uma boa notícia neste bloco: o Funicular da Graça, o 55E, está aberto</b> — é o único "
   "ascensor de Lisboa a funcionar. Liga a Rua dos Lagares, na Mouraria, ao Largo da Graça, e "
   "poupa-lhe o Caracol da Graça a caminho da Senhora do Monte. Reabriu em 30 de abril de 2026, com "
   "horário reduzido das <b>9h às 17h</b>, 14 pessoas por viagem, cerca de 90 segundos de subida e "
   "quatro partidas por hora. Custa <b>€ 4,30</b> até duas viagens e é <b>grátis com passe "
   "Navegante</b> — e atenção: <b>quem tem Navegante embarca primeiro</b>; o turista com bilhete "
   "avulso entra depois.<br>"
   +flag("Sem tempo a pé")+" ninguém publica. O que é verificável: <b>das Portas do Sol até a "
   "Senhora do Monte é subida contínua em calçada</b>. Não é passeio plano.",
 "Visitantes por ano":flag("Não existe")+" para nenhum dos dois. São espaços sem bilheteira e sem "
   "contagem — o número é estruturalmente inexistente, não apenas não publicado.",
 "Menor visitação e temperatura":"<b>Não existe série mensal — nem poderia, sem controlo de "
   "entrada.</b> Fica explicitamente escrito: não é possível apontar o mês de menor movimento com "
   "base em dado publicado.<br>"+IPMA+"<br>"
   "Os dois miradouros são <b>descobertos</b>. Julho e agosto somam 2,6 e 5,4 mm de chuva — quase "
   "garantia de céu limpo para o pôr do sol, e também de calor sem sombra. Novembro e outubro, com "
   "133,9 e 110,6 mm, são o que estraga a visita.",
 "Curiosidades":ul([
   "<b>“Portas do Sol” é nome literal:</b> ali existiu uma porta da muralha moura "
   "virada ao nascente, arruinada no terramoto de 1755.",
   "A estátua de São Vicente parece medieval, mas é de 1949, de Raul Xavier.",
   "A Senhora do Monte é onde D. Afonso Henriques teria montado acampamento para a conquista de "
   "Lisboa, em 1147 — <b>marcado como tradição histórica</b>, porque não a encontramos sustentada em "
   "fonte primária documental.",
   "A ermida foi fundada em 1147 e consagrada a São Gens, bispo que <b>segundo a tradição</b> ali "
   "foi martirizado — daí o antigo nome Monte de São Gens. A parte do martírio é explicitamente "
   "tradição, não fato documentado."]),
 "Fatos históricos":"<b>Portas do Sol:</b> é o sítio da antiga Porta do Sol da cerca moura, "
   "arruinada em 1755; a estátua é de 1949. "+flag("Não encontrada")+" a data de criação do "
   "miradouro atual, e "+flag("não encontrada")+" classificação patrimonial própria.<br>"
   "<b>Senhora do Monte:</b> ermida de 1147, com duas remodelações no século XX. A menção a "
   "<b>Imóvel de Interesse Público</b> circula, mas "+flag("o diploma e a data não foram "
   "confirmados")+" — a ficha não foi localizada na base patrimonial, e não inventamos decreto.",
 "Dias em que não funciona":"<b>Não há dia de fecho, horário, última entrada nem portão.</b> "
   "Nenhuma fonte oficial publica horário de encerramento, e os dois seguem abertos 24 horas.<br>"
   "<b>Mas a regra que derruba a noite está em vigor:</b> desde meados de <b>fevereiro de 2026</b>, "
   "Lisboa proíbe em toda a cidade a <b>venda de bebidas alcoólicas para consumo no exterior dos "
   "estabelecimentos</b> — de domingo a quinta das 23h às 8h, e às sextas, sábados e vésperas de "
   "feriado da meia-noite às 8h. As coimas vão a € 1.000 para pessoas e € 3.000 para empresas, e a "
   "regra abrange bares, cafés, restaurantes, casas de fado, lojas de conveniência e postos de "
   "combustível.<br>"
   +flag("Venda ou consumo?")+" as fontes não são claras: um veículo titula “consumir” "
   "e escreve “venda” no corpo; outro titula “venda”. São coisas "
   "juridicamente diferentes, e não conseguimos abrir o edital municipal para resolver. <b>Para o "
   "turista o efeito prático é o mesmo:</b> depois das 23h você não compra a cerveja para levar ao "
   "miradouro.<br>"
   +flag("Não existe")+" regra municipal de horário, ruído ou fecho noturno específica para os "
   "miradouros de Alfama — procuramos e não achamos. O precedente existe noutra zona: o Miradouro do "
   "Adamastor foi gradeado e passou a ter horário em 2019. <b>O modelo existe em Lisboa, foi "
   "aplicado uma vez, e não foi estendido às Portas do Sol nem à Senhora do Monte.</b> O que mudou "
   "em 2026 não foi o acesso — foi a bebida.",
 "Pontos turísticos próximos":"Castelo de São Jorge, Miradouro de Santa Luzia, Museu de Artes "
   "Decorativas, Sé, Alfama, São Vicente de Fora, Panteão Nacional, Feira da Ladra, Largo da Graça, "
   "Convento da Graça e Mouraria. "+flag("Sem distância oficial")}
}]}
