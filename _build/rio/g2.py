# -*- coding: utf-8 -*-
from lib import mapa, flag, ul

BANDEIRAS = ("<b>Bandeiras do Corpo de Bombeiros</b>, válidas num raio de 300 m em torno de cada "
  "posto de guarda-vidas: verde, risco mínimo; amarela, atenção redobrada por ondas e correntes; "
  "vermelha, local não adequado ao banho; preta, área sem guarda-vidas; vermelha dupla, praia "
  "fechada; roxa, animais marinhos perigosos. O CBMERJ registrou <b>8.255 salvamentos no mar</b> no "
  "estado do Rio entre janeiro e abril de 2026 (Agência Brasil, 26/abr/2026). As orientações "
  "oficiais: nadar perto dos postos, não beber álcool antes do banho, atenção às correntes de "
  "retorno (aquelas faixas de água que puxam o banhista para longe da areia), não nadar à "
  "noite nem perto de pedras e costões.")

G2 = {
 "titulo": "Praias e natureza",
 "intro": "Praia no Rio não tem catraca nem contagem oficial — o que existe de verificável é preço "
   "de cadeira, horário de guarda-vidas, boletim oficial de água própria para banho e, desde 2026, "
   "horário de fechar no Arpoador.",
 "pontos": [
{
 "id":"copacabana","nome":"Praia de Copacabana","tag":"Praia","img":"copacabana",
 "preco":"Grátis","preconota":"cadeira R$ 15–20, guarda-sol R$ 50–100",
 "campos":{
 "Endereço":"Avenida Atlântica, s/nº — Copacabana e Leme. A praia acompanha toda a extensão da "
   "avenida, entre o Morro do Leme, ao norte, e o Forte de Copacabana, ao sul. O calçadão de ondas "
   "em pedra portuguesa corre ao longo de tudo: é impossível errar. Os pontos fixos de orientação "
   "são o <b>Copacabana Palace</b> (Av. Atlântica, 1702), no trecho central, e o <b>Forte de "
   "Copacabana</b> (Praça Coronel Eugênio Franco, 1), na ponta sul. A areia é dividida por <b>postos "
   "de salvamento numerados de 1 a 6</b> — Leme tem os postos 1 e 2 — e carioca marca encontro por "
   "número de posto, nunca por endereço. O calçadão tem <b>4.110 metros</b> (cadastro Monumentos "
   "Rio, Prefeitura do Rio)."+mapa("Praia de Copacabana","Praia de Copacabana, Rio de Janeiro"),
 "Valor da entrada":"<b>Gratuito, 24 horas, sem catraca.</b> No Brasil a praia é bem público: ninguém "
   "pode cobrar para você pisar na areia, entrar no mar ou usar o calçadão.<br>"
   "<b>O que se paga são os serviços privados na areia</b> (faixas observadas pela Agência O Globo, "
   "10/jan/2026): guarda-sol <b>R$ 50 a R$ 100</b> a diária em Copacabana; cadeira de praia <b>R$ 15 "
   "a R$ 20</b>, com promoções de R$ 7 a R$ 10; espreguiçadeira o dia todo até <b>R$ 100</b> "
   "(R$ 70 com desconto); água de coco <b>R$ 12</b>.<br>"
   "<b>Não existe tabelamento oficial de preços nas praias do Rio.</b> Em 12/jan/2026 a Prefeitura "
   "<i>avaliava</i> adotar teto após denúncias de cobrança abusiva, mas nada foi aprovado até esta "
   "apuração. Niterói, a cidade vizinha, já tem teto de R$ 21,73 para o conjunto mesa + cadeiras + "
   "guarda-sol, e a fiscalização falha. "+flag("Faixa observada, não teto legal")+"<br>"
   "<b>O que a lei municipal garante a você:</b> o decreto de ordenamento da orla, de 16/mai/2025, "
   "determina que quiosques e barracas mantenham “de forma clara e visível as informações sobre "
   "preços, cardápio, condições de venda, taxas adicionais e demais serviços”. <b>Peça a tabela "
   "antes de sentar.</b> O mesmo decreto proíbe na areia caixa de som, garrafa de vidro, "
   "“cercadinhos”, ambulante não licenciado e acampamento.",
 "Pontos de referência":"Copacabana Palace, na altura dos postos 3 e 4 — o prédio branco art déco "
   "é o marco visual do trecho central. Forte de Copacabana, fechando a praia ao sul. As estátuas de "
   "Carlos Drummond de Andrade, sentado num banco na altura do Posto 6, e de Dorival Caymmi. Túnel "
   "Novo e Túnel Velho (Alaor Prata), as ligações históricas com Botafogo. Morro e Pedra do Leme ao "
   "norte. A Avenida e a Rua Nossa Senhora de Copacabana, paralelas onde está o comércio do bairro.",
 "Metrô mais próximo":"<b>Linha 1, três estações servem a orla:</b> <b>Cardeal Arcoverde</b> "
   "atende o trecho Leme e Posto 2; <b>Siqueira Campos</b> atende o trecho central, postos 3 e 4; "
   "<b>Cantagalo</b> atende os postos 5 e 6 e o Forte. Todas ficam a poucos minutos da areia. "
   +flag("Sem tempo oficial")+" o MetrôRio não publica o tempo a pé de nenhuma delas até a praia.",
 "Visitantes por ano":flag("Não existe")+" praia é espaço público sem catraca, então ninguém conta quem entra — nem a "
   "Prefeitura, nem a Riotur, nem a Orla Rio publicam esse número. Procuramos em "
   "prefeitura.rio, riotur.rio, orlario.com.br e nos dados abertos municipais.<br>"
   "<b>Os números oficiais que existem e servem de escala:</b> o Réveillon da virada de 2025 para "
   "2026 reuniu <b>2,6 milhões de pessoas só em Copacabana</b> e mais de 5,1 milhões na cidade "
   "inteira, em 13 palcos (Prefeitura do Rio, 1/jan/2026). E a cidade recebeu <b>12,5 milhões de "
   "visitantes em 2025</b>, dos quais 2,1 milhões internacionais, movimentando R$ 27,2 bilhões "
   "(Instituto Fecomércio de Pesquisas e Análises com a Riotur, 19/jan/2026).",
 "Menor visitação e temperatura":"<b>Junho a agosto</b>, com o vale em julho: é quando a cidade "
   "recebe menos turista de lazer, a água esfria e a areia esvazia nos dias de semana. Julho é o mês "
   "mais frio (15 °C de mínima, 25 °C de máxima) e junho, julho e agosto os mais secos — 38 mm, "
   "37 mm e 35 mm de chuva, contra 236 mm em janeiro (Climatempo, série de 30 anos). Para "
   "comparação, na alta temporada de janeiro e fevereiro a mínima média é 22 °C e a máxima 31 °C. "
   +flag("Sem contagem de público")+" não há número mensal de banhistas para cravar o mês mais vazio.",
 "Curiosidades":ul([
   "A praia que você pisa hoje é artificial na largura. O alargamento foi contratado em 1965, "
   "estudado pelo Laboratório Nacional de Engenharia Civil de Portugal e inaugurado em 15 de março "
   "de 1971: a praia ganhou cerca de 80 metros de largura em toda a extensão, com 3,3 milhões de "
   "metros cúbicos de areia dragada da Baía de Guanabara.",
   "O calçadão de ondas tem data e autor. O primeiro trecho, 1.100 metros no Leme, foi inaugurado "
   "em 16 de setembro de 1970, projeto de Roberto Burle Marx; o restante da Av. Atlântica saiu em "
   "15 de março de 1971. São 4.110 metros de pedra portuguesa, tombados pelo INEPAC em 1991.",
   "O nome veio da Bolívia e substituiu um nome tupi. A praia se chamava Sacopenapã, “caminho de "
   "socós”. O nome atual vem de uma capela erguida no século XVII por comerciantes de prata peruanos "
   "e bolivianos, com uma réplica de Nossa Senhora de Copacabana, a santa do santuário às margens do "
   "Titicaca. A capela foi demolida em 1914 para dar lugar ao Forte."]),
 "Fatos históricos":"Século XVII: ergue-se a capela de Nossa Senhora de Copacabana no rochedo da "
   "ponta sul, e o nome substitui o tupi Sacopenapã. <b>1892:</b> abertura do Túnel Velho, que conecta "
   "Copacabana ao resto da cidade e transforma a vila de pescadores isolada em bairro acessível. "
   "<b>1906:</b> primeiro calçadão, obra do prefeito Pereira Passos. <b>1914:</b> a capela é demolida "
   "e constrói-se o Forte. <b>1923:</b> inauguração do Copacabana Palace, que consolida o bairro como "
   "destino internacional. <b>1965–1971:</b> o grande alargamento e o calçadão de Burle Marx. "
   "<b>1991:</b> tombamento estadual do calçadão. <b>1992:</b> primeiro grande show de Réveillon na "
   "praia, com Jorge Benjor e Tim Maia — origem da tradição que hoje reúne milhões.",
 "Dias em que não funciona":"<b>Não fecha nunca.</b> Praia e calçadão são de acesso livre 24 horas, "
   "todos os dias do ano. O que muda é o horário dos serviços: os salva-vidas do Corpo de Bombeiros "
   "atuam em horário diurno, e no verão a Operação Verão da Polícia Militar mantém <b>policiamento "
   "reforçado até as 22h</b>, com mais de 1.620 policiais nas praias das Zonas Sul e Oeste, viatura "
   "de comando no Arpoador e centrais no 19º BPM (Copacabana) e 23º BPM (Leblon). A Operação Verão "
   "municipal 2025/2026 colocou mais de 1.000 agentes na orla, com regra explícita: não são "
   "permitidos acampamentos, garrafas de vidro, churrasqueiras e caixas de som na areia.<br>"+BANDEIRAS+
   "<br><b>A água está própria para banho?</b> O INEA, órgão ambiental do estado, publica toda semana "
   "um boletim que classifica cada praia como própria ou imprópria — é o chamado boletim de "
   "balneabilidade. No boletim de 16/jan/2026 Copacabana "
   "apareceu como <b>própria, com exceção do trecho em frente à Rua Francisco Otaviano</b>, que é a "
   "divisa com o Arpoador. Regra de ouro do próprio instituto: <b>não entrar no mar nas 24 horas "
   "seguintes à chuva</b> nem perto de saídas de galeria. "+flag("Muda semana a semana")+" consulte "
   "o boletim atualizado em inea.rj.gov.br antes de ir.",
 "Pontos turísticos próximos":"<b>Forte de Copacabana</b>, na ponta sul, com acesso direto pela "
   "areia: abre de terça a domingo e feriados, das 10h às 19h, fechado às segundas; inteira R$ 10 e "
   "meia R$ 5 para estudantes, professores e maiores de 60 anos; gratuito para militares e "
   "dependentes, maiores de 80 anos, crianças até 6 anos, pessoas com deficiência e guias de turismo. "
   "<b>Só aceita dinheiro em espécie — não aceita cartão nem Pix</b>, e não tem estacionamento "
   "(Visite Museus / IBRAM, 12/set/2026).<br>Praia do Leme, continuação imediata ao norte, é a mesma "
   "faixa de areia. Praia do Arpoador, logo após o Forte. Copacabana Palace, do outro lado da rua. "
   "Bondinho do Pão de Açúcar e Praia Vermelha, a poucos quilômetros pela Urca."}
},
{
 "id":"ipanema-arpoador","nome":"Ipanema e o Arpoador","tag":"Praia e mirante","img":"ipanema",
 "preco":"Grátis","preconota":"pedra fecha 21h desde jan/2026",
 "campos":{
 "Endereço":"Avenida Vieira Souto, s/nº — Ipanema, entre a Praia do Arpoador, a leste, e o Canal "
   "do Jardim de Alah, a oeste, onde vira Leblon. Cerca de 2 km de extensão. O <b>Arpoador</b> fica "
   "na Avenida Francisco Bhering, s/nº, entre o Forte de Copacabana e Ipanema; o acesso à "
   "<b>Pedra do Arpoador</b> é pelo portão na praia e pelo <b>Parque Garota de Ipanema, na Rua "
   "Francisco Otaviano</b>.<br>A orientação aqui também é por posto: o <b>Posto 8</b> fica na altura "
   "da Rua Farme de Amoedo e o <b>Posto 9</b> na Rua Vinicius de Moraes — este é o ponto de encontro "
   "mais movimentado da praia. Do lado de terra, as duas praças de referência são a Nossa Senhora da "
   "Paz, de bares e restaurantes, e a General Osório, da Feira Hippie aos domingos."
   +mapa("Praia de Ipanema","Praia de Ipanema, Rio de Janeiro"),
 "Valor da entrada":"<b>Gratuito.</b> Praia de Ipanema, Praia do Arpoador, Pedra do Arpoador e "
   "Parque Garota de Ipanema não cobram ingresso.<br>"
   "<b>Serviços privados na areia, valores apurados em Ipanema</b> (Agência O Globo, 10/jan/2026): "
   "cadeira de praia <b>R$ 15 a R$ 20</b>, com promoções de R$ 7 a R$ 10; guarda-sol comum "
   "<b>R$ 25</b> e maior <b>R$ 50</b>; espreguiçadeira o dia inteiro <b>R$ 100</b> entre os postos 8 "
   "e 9, ou R$ 70 com desconto; água de coco <b>R$ 12</b>. "+flag("Faixa observada, não teto legal")+
   " não há tabelamento oficial; o decreto municipal de 16/mai/2025 obriga a exibir preços, cardápio "
   "e taxas adicionais de forma clara e visível.",
 "Pontos de referência":"Pedra do Arpoador e Parque Garota de Ipanema, na ponta leste — o mirante "
   "do pôr do sol. Praça Nossa Senhora da Paz, arborizada, a duas quadras da praia. Praça General "
   "Osório, sede da Feira Hippie. As ruas Farme de Amoedo e Vinicius de Moraes, que dão nome aos "
   "trechos de areia. Canal do Jardim de Alah, o marco que separa Ipanema de Leblon. Morro Dois "
   "Irmãos, o paredão duplo que fecha o horizonte a oeste e é a imagem mais fotografada do pôr do "
   "sol. Praia do Diabo, a pequena enseada encaixada entre o Arpoador e o Forte.",
 "Metrô mais próximo":"<b>General Osório — Linha 1</b> é a mais útil: fica na Praça General "
   "Osório, no miolo de Ipanema, e serve tanto a praia quanto o Arpoador. <b>Nossa Senhora da Paz — "
   "Linha 4</b> atende os postos 9 e 10; <b>Jardim de Alah — Linha 4</b> atende a ponta oeste, junto "
   "ao canal. Para chegar ao Parque Garota de Ipanema pela Rua Francisco Otaviano, a estação mais "
   "próxima é <b>Cantagalo — Linha 1</b>. "+flag("Sem tempo oficial")+" o MetrôRio não publica "
   "tempos a pé.",
 "Visitantes por ano":flag("Não existe")+" mesma razão de Copacabana: praia de acesso livre, sem "
   "controle.<br><b>Dado oficial correlato:</b> em 3/jan/2026 a Prefeitura anunciou que a Comlurb "
   "destacaria <b>61 garis para as praias dos postos 7 e 8 e Praia do Diabo</b> e 30 garis para os "
   "acessos da Pedra do Arpoador, num pacote motivado pela lotação noturna do lugar. Em um único dia "
   "da operação especial, a Comlurb recolheu <b>mais de 2 toneladas de lixo</b> no Arpoador.<br>"
   "Em 17/fev/2026, Ipanema ficou em <b>23º lugar no ranking global de melhores praias do "
   "Tripadvisor</b>, única brasileira na lista.",
 "Menor visitação e temperatura":"<b>Junho a agosto</b>, com vale em julho — mesmo padrão de toda "
   "a orla. Junho tem 16 °C de mínima e 25 °C de máxima, com 38 mm de chuva; julho, 15 °C e 25 °C "
   "com 37 mm, o mês mais frio; agosto, 16 °C e 26 °C com 35 mm (Climatempo).<br>"
   "<b>Aqui a dica útil é de horário, não de mês:</b> mesmo no inverno a Pedra do Arpoador lota no "
   "fim da tarde por causa do pôr do sol. Para a pedra vazia, vá de manhã cedo — o portão abre "
   "às 4h. "+flag("Sem contagem de público")+" não há número mensal.",
 "Curiosidades":ul([
   "O nome “Ipanema” não tem nada a ver com a água daqui. O bairro leva o título do "
   "fundador, José Antônio Moreira Filho, II Barão de Ipanema, cujo título homenageia a freguesia "
   "paulista de São João de Ipanema, onde funcionou a primeira fábrica de ferro do Brasil. Em "
   "tupi-guarani <i>ipanema</i> significa “água ruim” — mas a referência é ao rio "
   "paulista, não ao mar carioca (dossiê APAC Ipanema, Secretaria Municipal das Culturas).",
   "O Arpoador tem horário de fechar desde 2026, e isso é novo. Em 3 de janeiro de 2026 a "
   "Prefeitura e a Polícia Militar anunciaram regras de uso noturno; a resolução conjunta foi "
   "publicada em 5 de janeiro. A pedra abre às 4h e fecha ao público às 21h.",
   "A canção que batizou a praia no mundo nasceu ali, em 1962: “Garota de Ipanema”, de "
   "Tom Jobim e Vinicius de Moraes. A concessionária oficial da orla registra que a praia ganhou "
   "fama mundial por essa composição. Os detalhes narrativos — o Bar Veloso, a identificação da musa "
   "— circulam sem fonte primária oficial e ficam aqui como tradição, não como dado verificado."]),
 "Fatos históricos":"<b>1886:</b> José Antônio Moreira Filho, II Barão de Ipanema, adquire os "
   "terrenos da região. <b>26 de abril de 1894:</b> assinatura do termo de fundação da Vila Ipanema, "
   "com abertura de 19 ruas e duas praças; os sócios do empreendimento — Coronel Antônio José Silva, "
   "José Luís Guimarães Caipora e Constante Ramos — batizam ruas do bairro até hoje. O topônimo vem "
   "do título nobiliárquico do fundador. Fonte de todos esses itens: dossiê APAC Ipanema, da "
   "Secretaria Municipal das Culturas. <b>1962:</b> composição de “Garota de Ipanema”, que "
   "projeta o bairro internacionalmente. <b>Janeiro de 2026:</b> a Prefeitura institui pela primeira "
   "vez horários oficiais de abertura e fechamento para a Pedra do Arpoador e o Parque Garota de "
   "Ipanema, com controle de acesso e fiscalização.",
 "Dias em que não funciona":"<b>A areia e o mar são de acesso livre 24 horas. A pedra, não — e "
   "essa regra é de 2026.</b><br>"
   "<b>Pedra do Arpoador:</b> abre às <b>4h</b>, fecha ao público às <b>21h</b>, com saída assistida "
   "por agentes das 21h às 23h; das 23h às 4h o acesso fica restrito para a limpeza da Comlurb.<br>"
   "<b>Parque Garota de Ipanema:</b> <b>6h às 20h</b>, entrada por acessos oficiais controlados.<br>"
   "<b>Areia dos postos 7 e 8 e Praia do Diabo:</b> livre, com limpeza mecanizada das 2h às 4h.<br>"
   "Depois que o parque fecha, só se entra pelo portão da praia; a saída é direcionada pela Alameda "
   "Via Peti. Guarda Municipal e Polícia Militar montam pontos de bloqueio para coibir ambulante não "
   "autorizado e som irregular. Fonte: Prefeitura do Rio, 3/jan/2026, com os horários do parque "
   "confirmados pela Panrotas em 5/jan/2026. "+flag("Não encontrado")+" o número do decreto: a "
   "comunicação oficial informa que a resolução seria publicada em 5/jan/2026, mas não cita o ato, e "
   "nenhuma fonte traz o número.<br>"
   "<b>O Arpoador exige cuidado redobrado na água.</b> No boletim do INEA de 16/jan/2026, Ipanema "
   "constava como <b>própria</b> e <b>o Arpoador como imprópria</b> para banho; no mesmo boletim "
   "Copacabana estava própria exceto no trecho da Rua Francisco Otaviano, que é a divisa. "
   +flag("Muda semana a semana")+" cheque em inea.rj.gov.br antes de ir. O CBMERJ orienta "
   "expressamente evitar nadar perto de pedras e costões, onde a correnteza pode arremessar o "
   "banhista — recomendação que se aplica direto ao Arpoador e à Praia do Diabo.<br>"+BANDEIRAS,
 "Pontos turísticos próximos":"Pedra do Arpoador e Parque Garota de Ipanema, na ponta leste, com "
   "acesso direto. Praia do Diabo, colada no Arpoador. Feira Hippie de Ipanema, na Praça General "
   "Osório. Praça Nossa Senhora da Paz. Forte de Copacabana, a uma caminhada do Arpoador. Praia do "
   "Leblon, do outro lado do Canal do Jardim de Alah. Lagoa Rodrigo de Freitas, subindo da Av. Vieira "
   "Souto. "+flag("Sem distância oficial")+" nenhuma fonte pública publica tempos a pé entre eles."}
},
{
 "id":"jardim-botanico","nome":"Jardim Botânico","tag":"Jardim e museu","img":"jardimbotanico",
 "preco":"R$ 40","preconota":"residente no Brasil; R$ 80 estrangeiro",
 "campos":{
 "Endereço":"Rua Jardim Botânico, 1008 — Jardim Botânico, CEP 22470-180. O portão principal fica "
   "<b>em frente ao Jockey Club Brasileiro</b> (Rua Jardim Botânico, 1003), que inclusive oferece "
   "estacionamento com desconto para visitantes do Jardim. Da rua, o que se vê é o alinhamento das "
   "palmeiras imperiais entrando pelo terreno.<br>"
   "<b>São quatro portões, e nem todos vendem ingresso:</b> Rua Jardim Botânico 1008 tem bilheteria "
   "todos os dias, estacionamento para PcD, bicicletário e desembarque para mobilidade reduzida; "
   "Rua Jardim Botânico 920 só vende <b>nos fins de semana e feriados</b>; Rua Pacheco Leão 101 "
   "vende todos os dias; <b>Rua Pacheco Leão 915 não vende ingresso</b> — serve só a quem já comprou "
   "online, sócios e funcionários."+mapa("Jardim Botânico do Rio de Janeiro","Jardim Botânico do Rio de Janeiro, Rua Jardim Botânico 1008"),
 "Valor da entrada":"Fonte: JBRJ, página oficial de ingressos, consultada em 12/set/2026.<br>"
   "<b>Visitante estrangeiro: R$ 80</b> (≈ US$ 16). <b>Residente no Brasil: R$ 40</b>, com desconto "
   "de 50%. <b>Meia-entrada: R$ 20</b>, para estudante matriculado, pessoa com deficiência, jovem "
   "até 21 anos, jovem de baixa renda de 15 a 29 anos com Identidade Jovem, e pessoa a partir de 60 "
   "anos. <b>Gratuito</b> para crianças até 5 anos e para estudantes da rede pública e professores "
   "acompanhantes em visita escolar agendada. O <b>Museu do Jardim Botânico e a Casa Pacheco Leão "
   "são gratuitos</b>, mediante retirada de ingresso em jbrj.eleventickets.com.<br>"
   +flag("Fontes oficiais divergem")+" sobre o valor da meia. A página de ingressos do JBRJ lista as "
   "categorias com direito a “meia entrada (50%)” <b>sem dizer o valor em reais</b>; o "
   "Portal Gov.br de serviços diz “meia entrada: R$ 40,00”; a cobertura do reajuste "
   "(BandNews FM, 16/jul/2025) diz R$ 20. <b>Confirme na bilheteria.</b><br>"
   "<b>Quando mudou:</b> o reajuste entrou em vigor em <b>14 de julho de 2025</b>, levando o ingresso "
   "de brasileiros de R$ 18 para R$ 40 e criando a tarifa de R$ 80 para estrangeiros. O reajuste "
   "anterior tinha sido em 2023, de R$ 17 para R$ 18. <b>Não há tarifa de morador do município do "
   "Rio</b> — o desconto é por residência no Brasil, não por cidade. Também não há diferença de alta "
   "e baixa temporada.<br>"
   "<b>Pagamento:</b> na bilheteria física, <b>só Pix e dinheiro — não aceita cartão</b>. Online, "
   "Pix ou cartão de crédito, em jbrj.eleventickets.com.",
 "Pontos de referência":"Jockey Club Brasileiro, bem em frente ao portão principal, com "
   "estacionamento com desconto para visitantes. Praça Santos Dumont, a praça de referência do "
   "bairro, com Rio Rotativo e ponto de aluguel de bicicletas. Lagoa Rodrigo de Freitas, a poucos "
   "quarteirões. Rua Pacheco Leão, a rua dos fundos, onde ficam dois dos quatro portões. Parque Lage, "
   "vizinho, subindo a Rua Jardim Botânico em direção ao Corcovado.",
 "Metrô mais próximo":"<b>Não há estação na porta.</b> A recomendação oficial do MetrôRio é "
   "desembarcar em <b>Botafogo — Linhas 1 ou 2</b>, pegar um ônibus de integração sentido Gávea e "
   "saltar em frente ao Jardim Botânico. "+flag("Sem tempo oficial")+" o MetrôRio não publica a "
   "duração desse trecho de ônibus.<br>"
   "<b>Linhas municipais que param no Jardim Botânico</b> (lista oficial do JBRJ): 105, 112, 309, "
   "410, 439, 538, 548, 583 e 584. <b>Intermunicipais:</b> 755D, 775D, 1775D, 2755D e 2775D.<br>"
   "Alternativas: estacionamento do Jockey Club com desconto para visitantes; Rio Rotativo na Praça "
   "Santos Dumont; aluguel de bicicleta na esquina da Rua Jardim Botânico com a Rua Lopes Quintas.",
 "Visitantes por ano":flag("Não encontrado")+" o Jardim Botânico não publica total anual. "
   "Procuramos em gov.br/jbrj (cujas páginas de notícia retornam “conteúdo restrito”), "
   "gov.br/mma, Portal Gov.br de serviços e imprensa.<br>"
   "<b>Os recortes oficiais que existem</b>, todos de janeiro a maio, publicados pela Agência Brasil "
   "em 13/jun/2022: <b>221,7 mil em 2019</b>, 114,6 mil em 2021 e 173,1 mil em 2022. São recortes de "
   "cinco meses, não totais anuais — não extrapolamos. Antes da pandemia, até cerca de 40% do "
   "público era estrangeiro, segundo a então presidente da instituição.<br>"
   "<b>Do Museu, que é um subconjunto:</b> 150 mil visitantes desde a inauguração em março de 2024, "
   "marca noticiada em 25/nov/2025.",
 "Menor visitação e temperatura":"<b>Dias de semana de junho e agosto</b> — julho também é baixa "
   "temporada turística, mas é mês de férias escolares brasileiras, então fins de semana e feriados "
   "seguem cheios. Junho tem 16 °C e 25 °C com 38 mm de chuva; julho, 15 °C e 25 °C com 37 mm; "
   "agosto, 16 °C e 26 °C com 35 mm, o mais seco do ano — trilha seca e céu limpo, condição ideal "
   "para o Arboreto (Climatempo).<br>"
   "<b>Aqui há uma dica de dia baseada em regra oficial, não em palpite:</b> a <b>quarta-feira</b> é "
   "o dia de menor movimento previsível, porque o Arboreto só abre às 11h — fecha das 8h às 11h para "
   "manutenção — e o Museu fica fechado. Quem chega às 11h numa quarta pega o jardim recém-aberto. "
   +flag("Sem dado mensal")+" não há estatística de visitação por mês.",
 "Curiosidades":ul([
   "Existe uma janela oficial para correr dentro do Jardim, e só ela: a norma do JBRJ determina que "
   "atividades físicas, corrida inclusive, são permitidas das 8h às 9h e das 16h às 18h. Fora desses "
   "dois blocos, é caminhada contemplativa. Sócios da Associação de Amigos têm janela ampliada.",
   "O Jardim nasceu ao lado de uma fábrica de pólvora. A decisão do Príncipe Regente D. João, em 13 "
   "de junho de 1808, foi instalar no local uma fábrica de pólvora <i>e</i> um jardim de aclimatação "
   "de espécies vindas de outras partes do mundo. As duas coisas juntas (Fundação Biblioteca Nacional).",
   "A primeira palmeira imperial teria sido plantada por D. João em pessoa, em 1809, chegado a "
   "38,70 metros e derrubada por um raio em 1972; o tronco estaria exposto no Museu Botânico. "
   "Registramos com ressalva: este é o único item do verbete cuja fonte não é oficial — as páginas "
   "institucionais do JBRJ estavam inacessíveis na apuração."]),
 "Fatos históricos":"<b>13 de junho de 1808:</b> criação por decisão do Príncipe Regente D. João, "
   "futuro D. João VI, como fábrica de pólvora e jardim de aclimatação, no engenho das terras da "
   "Lagoa Rodrigo de Freitas (Fundação Biblioteca Nacional). <b>1995:</b> a instituição recebe o nome "
   "atual, Instituto de Pesquisas Jardim Botânico do Rio de Janeiro, hoje autarquia federal ligada ao "
   "Ministério do Meio Ambiente e um dos principais centros mundiais de pesquisa em botânica e "
   "conservação. <b>Março de 2024:</b> inauguração do Museu do Jardim Botânico. <b>14 de julho de "
   "2025:</b> entra em vigor o reajuste dos ingressos.<br>"
   "O tombamento pelo IPHAN em 1937 e o reconhecimento da UNESCO como Reserva da Biosfera em 1991 "
   "circulam amplamente, mas "+flag("não confirmamos")+" nem no IPHAN nem na UNESCO.<br>"
   "<b>Área e número de espécies: não publicamos.</b> Circulam 54 hectares de área geral, 57 de "
   "Arboreto e cerca de 6.500 espécies, mas só localizamos essas cifras em fonte não oficial — as "
   "páginas do JBRJ que trariam o dado bloquearam a leitura na apuração. "+flag("Não confirmado"),
 "Dias em que não funciona":"<b>O Arboreto e o Museu têm horários diferentes, e a quarta-feira é a "
   "armadilha.</b><br>"
   "<b>Arboreto, o jardim em si:</b> de quinta a terça, <b>8h às 17h</b>; na <b>quarta-feira, 11h às "
   "17h</b> — fecha das 8h às 11h para manutenção.<br>"
   "<b>Museu do Jardim Botânico:</b> de quinta a terça, <b>10h às 18h</b>, com última entrada às 17h; "
   "<b>na quarta-feira fica fechado</b>.<br>"
   "Enquanto o Arboreto está fechado nas manhãs de quarta, o Corredor Cultural continua acessível "
   "pela entrada da Rua Jardim Botânico. Sócios da Associação de Amigos entram de quinta a terça das "
   "6h às 18h, e nas quartas das 11h às 18h.<br>"
   "<b>Feriados:</b> funcionamento normal. <b>Fim de ano:</b> 24/12 e 31/12 das 8h às 14h; "
   "<b>25/12 e 1º/01 fechado</b>.<br>"
   "Centro de Visitantes: (21) 3874-1808 e (21) 3874-1214, cvis@jbrj.gov.br.",
 "Pontos turísticos próximos":"Jockey Club Brasileiro, do outro lado da rua. Praça Santos Dumont, "
   "uma caminhada curta. Lagoa Rodrigo de Freitas, a poucos quarteirões. Parque Lage, cerca de "
   "1,5 km subindo a mesma rua. Praia do Leblon, a cerca de 2,5 km. O acesso à Vista Chinesa e ao "
   "Corcovado sai daqui, pela Rua Pacheco Leão e a Estrada Dona Castorina. "
   +flag("Sem distância oficial")+" os tempos a pé não são publicados."}
},
{
 "id":"floresta-da-tijuca","nome":"Floresta da Tijuca","tag":"Floresta urbana","img":"tijuca",
 "preco":"Grátis","preconota":"600 carros por dia, 300 de manhã",
 "campos":{
 "Endereço":"Estrada da Cascatinha, 850 — Alto da Boa Vista, CEP 20531-590, que é o endereço do "
   "Centro de Visitantes do Setor Floresta. <b>A entrada fica na Praça Afonso Viseu</b> — é esse o "
   "nome que se procura na rua; o portão principal está ali. Chega-se à praça pela <b>Estrada das "
   "Furnas</b>, vindo da Barra e do Itanhangá, ou pela <b>Avenida Edson Passos</b>, vindo da Tijuca. "
   "A Cascatinha Taunay aparece a poucos metros do portão: se você já ouve água caindo, chegou.<br>"
   "Atenção para não confundir: o parque tem um segundo endereço geral, Estrada das Paineiras, s/nº, "
   "em Santa Teresa — esse é o Setor Serra da Carioca, não a Floresta."
   +mapa("Floresta da Tijuca","Praça Afonso Viseu, Alto da Boa Vista, Rio de Janeiro"),
 "Valor da entrada":"<b>Gratuita.</b> A administração é explícita: “a entrada do Parque é "
   "gratuita”. A <b>única exceção tarifada em todo o Parque Nacional da Tijuca é o "
   "Corcovado</b>, que fica em outro setor. Não há meia-entrada, tarifa de morador nem diferença de "
   "temporada, porque não há cobrança. Fonte: FAQ oficial do Parque Nacional da Tijuca, consultado "
   "em 12/set/2026. Também não há cobrança de estacionamento informada em fonte oficial — mas há "
   "limite de vagas, e é isso que importa aqui.",
 "Pontos de referência":"<b>Cascatinha Taunay</b>, a cachoeira mais alta do parque, a poucos "
   "metros do portão principal, com uma ponte de pedra em arco romano construída em 1860. <b>Capela "
   "Mayrink</b>, a capela rosa de 1855. <b>Açude da Solidão</b>, o lago mais conhecido do setor. "
   "<b>Bom Retiro</b>, área de lazer com playground. Os restaurantes <b>A Floresta</b> e <b>Os "
   "Esquilos</b>, as duas opções de refeição dentro do setor. O <b>Centro de Visitantes</b>, logo "
   "após a entrada. E o <b>Pico da Tijuca</b>, ponto mais alto do parque, a 1.022 metros. No entorno "
   "imediato, o bairro do Alto da Boa Vista.",
 "Metrô mais próximo":"<b>Não há metrô, trem nem VLT no Alto da Boa Vista.</b> O acesso por "
   "transporte público é exclusivamente por ônibus: as linhas <b>301, 302 e 345</b> servem a entrada "
   "na Praça Afonso Viseu, segundo o próprio parque. "+flag("Não encontrado")+" o tempo a pé do "
   "ponto de ônibus até o portão — nenhuma fonte oficial publica. De carro, pela Estrada das Furnas "
   "ou pela Avenida Edson Passos. Contato do parque: (61) 2028-8757, parnatijuca@icmbio.gov.br.",
 "Visitantes por ano":"<b>O parque inteiro recebeu mais de 4,9 milhões de visitantes em 2025</b>, "
   "líder nacional pelo 18º ano consecutivo, contra mais de 4,6 milhões em 2024 — que sozinhos "
   "representaram mais de um terço de todas as visitas às unidades de conservação federais do Brasil "
   "naquele ano. Dados do ICMBio.<br>"
   +flag("Não encontrado")+" o número só do Setor Floresta: o ICMBio divulga por unidade de "
   "conservação, não por setor, e os 4,9 milhões incluem Corcovado, Serra da Carioca, Pedra "
   "Bonita/Pedra da Gávea e Floresta — sendo que o Corcovado sozinho responde por mais da metade, com "
   "2,8 milhões.<br>"+flag("Fonte desatualizada")+" a página do Ministério do Turismo ainda informa "
   "“aproximadamente dois milhões de visitantes por ano”, número muito anterior aos "
   "balanços do ICMBio de 2024 e 2025.",
 "Menor visitação e temperatura":"<b>Junho a agosto, e aqui a baixa temporada coincide com a "
   "melhor época para caminhar:</b> é o trimestre mais seco do ano no Rio, o que significa trilha "
   "firme, menos lama e menos risco de tempestade de verão. O movimento cai principalmente nos dias "
   "de semana. Junho tem 16 °C e 25 °C com 38 mm; julho, 15 °C e 25 °C com 37 mm; agosto, 16 °C e "
   "26 °C com 35 mm, o mês mais seco (Climatempo).<br>"
   +flag("Não encontrado")+" temperatura medida dentro da floresta: não há estação meteorológica com "
   "normais publicadas para o Alto da Boa Vista. Os números acima são do município. Na prática a mata "
   "e a altitude deixam o ar sensivelmente mais fresco e úmido que na orla, mas não há número oficial "
   "para quantificar a diferença — então não afirmamos um valor.",
 "Curiosidades":ul([
   "A Tijuca virou floresta protegida uma década antes de Yellowstone virar parque nacional. "
   "D. Pedro II declarou as florestas da Tijuca e das Paineiras como “Florestas "
   "Protetoras” em 1861; Yellowstone foi criado em 1872.",
   "A floresta foi replantada à mão por treze pessoas, onze delas escravizadas — e o Estado do Rio "
   "reconheceu isso oficialmente em 2025. O reflorestamento foi comandado pelo Major Manuel Gomes "
   "Archer com 11 homens escravizados; nos 13 anos iniciais plantaram mais de 100 mil árvores. Em 25 "
   "de março de 2025 a Assembleia Legislativa aprovou a inclusão dos 11 nomes no Livro dos Heróis "
   "do Estado.",
   "Os Portinaris da Capela Mayrink que você vê são réplicas. Candido Portinari pintou quatro obras "
   "para a capela; os originais estão sob custódia do Museu Nacional de Belas Artes, e no altar estão "
   "as cópias.",
   "É proibido tomar banho sob a queda principal da Cascatinha Taunay. O banho só é permitido no "
   "poço abaixo da ponte de arco romano, conhecido como poço do Job de Alcântara."]),
 "Fatos históricos":"<b>1817:</b> o pintor Nicolas Antoine Taunay estabelece residência junto à "
   "cachoeira e a imortaliza em suas telas; a casa foi demolida em 1946, mas o nome Cascatinha Taunay "
   "ficou. <b>1855:</b> construção da Capela Mayrink pelo Visconde Antônio Alves Souto. <b>1860:</b> "
   "o engenheiro Job de Alcântara constrói a ponte de pedra em arco romano sobre a Cascatinha, por "
   "ordem do Governo Imperial. <b>1861:</b> D. Pedro II declara as florestas Protetoras e entrega o "
   "reflorestamento ao Major Archer. Depois dele, o Barão d'Escragnolle assume e desenvolve o "
   "paisagismo com o francês Auguste Glaziou. <b>Anos 1940:</b> Raymundo Ottoni de Castro Maya "
   "promove a revitalização, com projetos de Roberto Burle Marx. <b>1961:</b> criação do Parque "
   "Nacional do Rio de Janeiro, com 33 km². <b>8 de fevereiro de 1967:</b> renomeado Parque Nacional "
   "da Tijuca pelo Decreto Federal nº 60.183. <b>4 de julho de 2004:</b> decreto amplia os limites "
   "incorporando o Parque Lage, a Serra dos Pretos Forros e o Morro da Covanca.<br>"
   +flag("Fontes oficiais se contradizem")+" sobre a área total: a página do parque informa "
   "39,51 km² após 2004; a do Ministério do Turismo apresenta 72,51 km². Não publicamos um número.",
 "Dias em que não funciona":"<b>Não fecha em nenhum dia da semana</b> — abre diariamente, fins de "
   "semana e feriados inclusive, das 8h às 17h. Mas o Setor Floresta tem horários diferentes por tipo "
   "de visitante: <b>pedestres e ciclistas entram das 6h às 17h</b> e podem permanecer até 18h; "
   "<b>veículos motorizados entram das 8h às 17h</b>, com permanência até 18h.<br>"
   "<b>O limite de veículos é o que faz chegar cedo importar:</b> são permitidos por dia até "
   "<b>600 carros — 300 de manhã e 300 à tarde — e 80 motos</b>, 40 em cada período.<br>"
   "<b>Restrições viárias dentro do parque:</b> a Estrada do Redentor é fechada 24 horas a veículos "
   "motorizados, liberada a pedestres e ciclistas; a Estrada Dona Castorina não permite veículos "
   "entre 7h e 9h nos dias úteis e entre 7h e 19h aos fins de semana e feriados.<br>"
   "<b>Horários dos atrativos:</b> a Capela Mayrink abre diariamente <b>das 14h às 16h</b>, com missa "
   "às 12h todo primeiro domingo do mês; a Cascatinha Taunay, das 8h às 17h, com banho permitido só "
   "no poço abaixo da ponte.<br>"
   "Para referência de outros setores: na Pedra da Gávea a trilha só pode ser iniciada até as 14h, e "
   "na Pedra Bonita até as 16h.",
 "Pontos turísticos próximos":"Cascatinha Taunay, a poucos metros do portão principal — este é "
   "dado oficial. Centro de Visitantes, logo após a entrada. Capela Mayrink, perto do Centro de "
   "Visitantes, com acesso pela Trilha dos Estudantes ou pela Estrada da Cascatinha. Açude da "
   "Solidão, Bom Retiro e o Pico da Tijuca, todos dentro do setor. Vista Chinesa e Mirante Dona "
   "Marta, no Setor Serra da Carioca, a algumas dezenas de minutos de carro.<br>"
   +flag("Sem distância oficial")+" a administração não publica distâncias nem tempos de trilha "
   "entre os atrativos do Setor Floresta. Não estimamos. Quem for fazer trilha deve pegar o mapa no "
   "Centro de Visitantes."}
}]}
