# -*- coding: utf-8 -*-
"""Miami: nove pontos, com fonte e data em cada numero.

Mesmo molde do sevilha/dados.py e do porto/dados.py. O renderizador e o
novos/gera.py, chamado com VNL_DADOS=miami.

POR QUE MIAMI, E POR QUE AGORA
------------------------------
Orlando ja esta no site, e brasileiro quase nunca faz Orlando sem Miami.
Este destino nao abre frente nova - fecha um buraco. E nao repete nenhum
ponto de Orlando: la sao os parques, aqui sao praia, art deco, museus da
baia, Everglades e os bairros.

O QUE ESTA APURACAO ACHOU
-------------------------

1. O EVERGLADES PASSOU A COBRAR US$ 100 A MAIS DE QUEM NAO MORA NOS EUA,
   e essa e a maior mudanca de preco do ano para o viajante brasileiro.
   Desde 1 de janeiro de 2026, onze parques nacionais cobram adicional de
   nao-residente. O Everglades e um dos onze - conferido na lista da
   propria pagina central do NPS, que os nomeia: Acadia, Bryce Canyon,
   Everglades, Glacier, Grand Canyon, Grand Teton, Rocky Mountain,
   Sequoia & Kings Canyon, Yellowstone, Yosemite e Zion.

   Para um casal brasileiro de carro, a conta sai de US$ 35 para US$ 235.

2. AS DUAS PAGINAS OFICIAIS DO NPS SE CONTRADIZEM SOBRE O PASSE, e a
   diferenca custa dinheiro real. A pagina de tarifas do proprio
   Everglades diz que o adicional nao se aplica a quem usa "an Annual or
   America the Beautiful Pass". A pagina central do NPS sobre o adicional
   diz que so o "America the Beautiful Non-Resident Annual Pass", de
   US$ 250, dispensa - e nao abre excecao para o passe comum de US$ 70.

   Quem comprar o de US$ 70 confiando na primeira pagina pode ser cobrado
   assim mesmo. Registramos as duas e nao escolhemos nenhuma.

3. OS DIAS DE ENTRADA GRATUITA DEIXARAM DE VALER PARA ESTRANGEIRO. Sao
   oito por ano, e o texto do NPS e literal: "Beginning in 2026, free
   entrance on these days will be for US citizens and residents only.
   Nonresidents will pay the regular entrance fee and any applicable
   nonresident fees."

4. O PAMM FECHA DOIS DIAS POR SEMANA, terca E quarta - e quase todo guia
   escreve so a terca. E de graca as quintas depois das 17h.

5. O ZOO MIAMI MUDA DE PRECO EM 1 DE OUTUBRO DE 2026, dois dias depois
   desta apuracao. Publicamos os dois precos, com a data da virada.

6. A TAXA DE HOTEL DE MIAMI BEACH TEM COMPOSICAO DIFERENTE DO RESTO DO
   CONDADO. Nao e so "mais cara": e outra pilha de impostos.

O QUE ESTA APURACAO NAO TEM, E FICA ESCRITO
-------------------------------------------
Vizcaya e Wynwood Walls nao publicam tabela de preco em pagina estatica -
as duas vendem por widget de reserva. Nao ha numero fixo para citar, e
nao inventamos um. As duas fichas dizem isso, e as duas ficam fora do
total da calculadora.

Campos como "Visitantes por ano" e "Fatos historicos" so aparecem onde ha
fonte. Onde nao apuramos, o campo nao existe - em vez de existir vazio.

Apuracao de 29 de setembro de 2026.
"""

APURACAO = "29 de setembro de 2026"
APURACAO_CURTA = "29/set/2026"

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
#  MIAMI
# =====================================================================
MIAMI = {
    "slug": "miami",
    "nome": "Miami",
    "pais": "Estados Unidos",
    "regiao": "america-do-norte",
    "titulo": "Miami: 9 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 9 pontos de Miami, com o adicional de "
                  "US$ 100 que os Everglades passaram a cobrar de quem não mora nos "
                  "EUA e a taxa de hotel que muda conforme o bairro."),
    "abertura": ("Nove pontos com preço em dólar, horário e fonte conferidos em 29 de "
                 "setembro de 2026 — e a mudança que reescreve a conta do ano: <b>os "
                 "Everglades passaram a cobrar US$ 100 por pessoa de quem não mora nos "
                 "Estados Unidos, e os dias de entrada gratuita deixaram de valer para "
                 "estrangeiro</b>."),
    "busca": ("miami florida estados unidos eua south beach miami beach art deco ocean drive "
              "everglades parque nacional wynwood walls little havana calle ocho vizcaya "
              "perez art museum pamm frost science zoo miami biscayne bay coconut grove "
              "resort fee taxa de hotel dolar nao residente nonresident fee"),
    "grupos": [
        {"id": "g1", "titulo": "Os museus da baía",
         "intro": ("Os três ficam no mesmo eixo da Biscayne Bay, e os três têm regra de "
                   "horário que derruba roteiro — incluindo um que fecha dois dias por "
                   "semana.")},
        {"id": "g2", "titulo": "Os bairros e a praia",
         "intro": ("Onde está quase tudo o que Miami tem de graça — e os dois pontos que "
                   "cobram sem publicar quanto.")},
        {"id": "g3", "titulo": "Fora da cidade, e a conta da cama",
         "intro": ("O parque nacional que ficou muito mais caro para estrangeiro em 2026, "
                   "o zoológico que muda de preço nesta semana, e a pilha de taxas que "
                   "não está na diária que você comparou.")},
    ],
    "pontos": [

        # ---------------------------------------------------------- g1
        {
            "id": "perez-art-museum",
            "foto": {"arq": "miami/pamm.webp",
                     "alt": ("A varanda coberta do Pérez Art Museum Miami, com as colunas do "
                             "beiral, as palmeiras do parque e o skyline da cidade ao fundo"),
                     "cred": "osseous · CC BY 2.0 · via Wikimedia Commons"},
            "grupo": "g1",
            "nome": "Pérez Art Museum Miami (PAMM)",
            "tag": "Museu de arte",
            "preco_val": "US$ 18",
            "preco_nota": "adulto; grátis quinta após 17h",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página oficial de visita do museu (pamm.org), consultada em "
                 "29/set/2026.<br>"
                 "<b>Adulto US$ 18.</b> <b>Sênior de 62 anos ou mais</b>, com documento, "
                 "<b>US$ 14</b>. <b>Estudante</b> com carteira, <b>US$ 14</b>. <b>Jovem "
                 "de 7 a 18 anos, US$ 14</b>. <b>Criança de até 6 anos não paga.</b> "
                 "Associado entra de graça.<br>"
                 "<b>É gratuito para todos nas quintas depois das 17h</b> — e como o "
                 "museu fecha às 21h na quinta, são quatro horas de entrada livre por "
                 "semana. É a maior economia possível entre os três museus desta ficha.<br>"
                 "Também não pagam: militares e veteranos americanos, profissionais de "
                 "saúde e socorristas, educadores da Flórida, e visitantes com "
                 "deficiência mais um acompanhante — todos com documento."),
                ("Dias em que não funciona",
                 "<b>Fecha terça E quarta-feira.</b> São dois dias por semana, e essa é a "
                 "armadilha: quase todo guia escreve só a terça. Um roteiro que marque o "
                 "PAMM para uma quarta perde o dia inteiro.<br>"
                 "<b>Segunda:</b> 11h às 18h. <b>Quinta:</b> 11h às 21h. <b>Sexta, sábado "
                 "e domingo:</b> 11h às 18h.<br>"
                 "<b>A bilheteria para de vender 30 minutos antes de fechar</b>, e o museu "
                 "avisa que o ingresso está sujeito à lotação e <b>pode esgotar</b> — por "
                 "isso recomenda compra antecipada."),
                ("Pontos de referência",
                 "Fica no Maurice A. Ferré Park, na beira da Biscayne Bay, colado ao "
                 "Frost Science — os dois dividem o mesmo parque. O Kaseya Center fica ao "
                 "lado, e o Bayside Marketplace com o Bayfront Park ficam ao sul, na "
                 "mesma orla.<br>" + mapa("Perez Art Museum Miami, 1103 Biscayne Blvd, Miami, FL")),
            ],
        },
        {
            "id": "frost-science",
            "grupo": "g1",
            "nome": "Phillip and Patricia Frost Museum of Science",
            "tag": "Museu, aquário e planetário",
            "preco_val": "a partir de US$ 29,95",
            "preco_nota": "adulto; o preço muda conforme o dia",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (frostscience.org), consultado em 29/set/2026.<br>"
                 "<b>Adulto a partir de US$ 29,95.</b> <b>Jovem de 4 a 11 anos, a partir "
                 "de US$ 24,95.</b> <b>Criança de até 3 anos não paga.</b><br>"
                 + FLAG % "Preço variável" +
                 "o museu escreve que <b>o valor muda conforme o dia da visita</b>. Os "
                 "números acima são o piso publicado, não o preço de uma data qualquer — "
                 "confira no checkout da sua.<br>"
                 "<b>O ingresso é um só e cobre as três coisas:</b> todas as exposições, "
                 "o aquário e <b>uma</b> sessão do planetário, conforme disponibilidade. "
                 "Não se paga o planetário à parte, mas também não se assiste a duas "
                 "sessões com o mesmo bilhete."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias, das 10h às 17h.</b> É o único dos três museus "
                 "desta ficha sem dia de fechamento semanal — o que faz dele o plano B "
                 "natural de uma terça ou de uma quarta, quando o PAMM e o Vizcaya estão "
                 "fechados.<br>"
                 + FLAG % "Feriados não publicados" +
                 "a página de ingressos não lista datas de encerramento anual. Ausência "
                 "de informação não é garantia de que não existam."),
                ("Pontos de referência",
                 "Divide o Maurice A. Ferré Park com o PAMM, a poucos minutos de "
                 "caminhada. Se o seu dia tem os dois, eles se resolvem no mesmo "
                 "deslocamento — e é a única dupla desta ficha em que isso acontece.<br>"
                 + mapa("Frost Science Museum, 1101 Biscayne Blvd, Miami, FL")),
            ],
        },
        {
            "id": "vizcaya",
            "foto": {"arq": "miami/vizcaya.webp",
                     "alt": ("A barca de pedra de Vizcaya na Baía de Biscayne, com as "
                             "esculturas na balaustrada e a vegetação da villa ao fundo"),
                     "cred": "Jacklee · CC BY-SA 3.0 · via Wikimedia Commons"},
            "grupo": "g1",
            "nome": "Vizcaya Museum and Gardens",
            "tag": "Casa-museu e jardins",
            "preco_val": "—",
            "preco_nota": "sem tabela fixa publicada",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (vizcaya.org), consultado em 29/set/2026.<br>"
                 + FLAG % "Sem tabela publicada" +
                 "<b>o Vizcaya não publica preço por faixa etária numa tabela estática.</b> "
                 "A venda é por tipo de visita, num widget de reserva, e a própria página "
                 "descreve a faixa como <b>US$ 24 a US$ 39</b> conforme o ingresso "
                 "escolhido. <b>Não há um número único para citar, e não inventamos um</b> "
                 "— por isso este ponto fica fora do total da ficha de custos.<br>"
                 "O que está publicado com clareza: <b>associado paga US$ 10</b> e "
                 "<b>criança de até 5 anos não paga</b>.<br>"
                 "<b>Descontos que existem mas quase não servem ao turista:</b> morador de "
                 "Miami-Dade com 62 anos ou mais entra de graça às segundas e quartas, "
                 "pelo programa Golden Tickets; e o Culture Shock Miami vende ingresso a "
                 "US$ 5 para quem tem de 13 a 22 anos, com direito a um segundo a US$ 5 "
                 "para um acompanhante de qualquer idade. <b>Os dois pedem residência ou "
                 "vínculo local.</b>"),
                ("Dias em que não funciona",
                 "<b>Fecha às terças-feiras.</b> Abre nos outros seis dias, <b>das 9h30 "
                 "às 16h30</b> — e repare que <b>fecha mais cedo que qualquer outro ponto "
                 "pago desta ficha</b>. Fim de tarde no Vizcaya não existe: às 16h30 o "
                 "portão está fechado."),
                ("Pontos de referência",
                 "Fica em Coconut Grove, na Biscayne Bay, ao sul do centro. Do outro lado "
                 "da South Miami Avenue fica o Vizcaya Village, a antiga parte de serviço "
                 "da propriedade.<br>"
                 + mapa("Vizcaya Museum and Gardens, 3251 S Miami Ave, Miami, FL")),
            ],
        },

        # ---------------------------------------------------------- g2
        {
            "id": "wynwood-walls",
            "foto": {"arq": "miami/wynwood-walls.webp",
                     "alt": ("O pórtico de entrada do Wynwood Walls, com o nome em letras "
                             "altas sobre a estrutura e os murais coloridos do recinto atrás"),
                     "cred": "Dan Lundberg · CC BY-SA 2.0 · via Wikimedia Commons"},
            "grupo": "g2",
            "nome": "Wynwood Walls",
            "tag": "Arte de rua",
            "preco_val": "—",
            "preco_nota": "cobra, mas não publica quanto",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de admissões do site oficial (thewynwoodwalls.com), "
                 "consultada em 29/set/2026.<br>"
                 + FLAG % "Preço não publicado" +
                 "<b>a página de admissões não mostra valor.</b> O formulário de reserva "
                 "exibe um total zerado até que se escolha data e quantidade, e não há "
                 "tabela por categoria em lugar nenhum do site. <b>Cobra-se entrada, mas "
                 "o quanto só aparece no checkout</b> — e por isso este ponto também fica "
                 "fora do total da ficha.<br>"
                 "O que está publicado: <b>criança de menos de 12 anos não paga, mas ainda "
                 "precisa de ingresso emitido</b> para entrar.<br>"
                 "<b>Vale distinguir o que é pago do que não é:</b> o Wynwood Walls é um "
                 "recinto fechado, com mais de 40 murais, 12 esculturas e 3 galerias. "
                 "<b>O bairro de Wynwood em volta é rua aberta e não custa nada</b>, e tem "
                 "mural em quase todo quarteirão. Muita gente paga sem saber que a "
                 "caminhada externa é gratuita."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias, das 10h30 às 18h30.</b> Não há dia de fechamento "
                 "semanal publicado. As portas fecham 10 minutos antes do encerramento, e "
                 "o próprio site avisa que o horário está sujeito a mudança."),
                ("Endereço",
                 "2516 NW 2nd Ave, Miami, FL 33127. Quem comprou antecipado entra pelo "
                 "Welcome Center, nesse mesmo número.<br>"
                 + mapa("Wynwood Walls, 2516 NW 2nd Ave, Miami, FL")),
            ],
        },
        {
            "id": "little-havana",
            "foto": {"arq": "miami/little-havana.webp",
                     "alt": ("Uma fachada de comércio na Calle Ocho, em Little Havana, com "
                             "mural colorido e bandeiras cubanas sobre a porta"),
                     "cred": "Phillip Pessar · CC BY 2.0 · via Wikimedia Commons"},
            "grupo": "g2",
            "nome": "Little Havana e a Calle Ocho",
            "tag": "Bairro",
            "preco_val": "Grátis",
            "preco_nota": "a rua; o que se consome, não",
            "campos": [
                ("Valor da entrada",
                 "<b>Não existe bilhete.</b> Little Havana é bairro, e a Calle Ocho — a "
                 "SW 8th Street — é via pública. Caminhar, olhar e fotografar não custa "
                 "nada, a qualquer hora.<br>"
                 "<b>O que custa é o que você consome:</b> café, charuto, almoço e as "
                 "casas de dominó. O Parque do Dominó, no cruzamento com a SW 15th "
                 "Avenue, é público.<br>"
                 + FLAG % "Preços de consumo não apurados" +
                 "não levantamos cardápio de restaurante nem preço de charuto: são "
                 "estabelecimentos privados, sem tabela publicada, e variam demais para "
                 "virar número nesta ficha."),
                ("Dias em que não funciona",
                 "<b>A rua não fecha.</b> Os estabelecimentos têm horário próprio, cada "
                 "um o seu.<br>"
                 "<b>A exceção que vale planejar:</b> a <b>Viernes Culturales</b> acontece "
                 "na última sexta-feira de cada mês, à noite, com galerias abertas e "
                 "música na rua. Se a sua viagem pega uma última sexta, é o melhor "
                 "momento possível para este bairro."),
                ("Pontos de referência",
                 "O eixo é a SW 8th Street entre a 12ª e a 17ª avenidas. O Parque do "
                 "Dominó (Máximo Gómez Park), o Tower Theater e a Calle Ocho Walk of Fame "
                 "estão todos nesse trecho, a pé.<br>"
                 + mapa("Calle Ocho, Little Havana, Miami, FL")),
            ],
        },
        {
            "id": "south-beach-art-deco",
            "foto": {"arq": "miami/south-beach.webp",
                     "alt": ("Guarita de salva-vidas pintada em rosa e laranja na areia de "
                             "South Beach, em Miami, com a praia vazia, rastros de pneu na "
                             "areia e o skyline de hotéis ao fundo"),
                     "cred": "Cristo Vlahos · CC BY-SA 4.0 · via Wikimedia Commons"},
            "grupo": "g2",
            "nome": "South Beach e o Art Deco District",
            "tag": "Praia e arquitetura",
            "preco_val": "Grátis",
            "preco_nota": "a praia e a rua; a visita guiada é paga",
            "campos": [
                ("Valor da entrada",
                 "<b>A praia é pública e não se cobra por areia.</b> A Ocean Drive, a "
                 "Collins Avenue e a Lincoln Road também são via pública — o conjunto art "
                 "déco se vê de graça, andando.<br>"
                 "<b>O que é pago</b> é a visita guiada da Miami Design Preservation "
                 "League, que sai do Art Deco Welcome Center, na 1001 Ocean Drive. "
                 + FLAG % "Preço não apurado" +
                 "não confirmamos a tarifa atual da caminhada guiada em fonte oficial, e "
                 "por isso ela não entra na conta.<br>"
                 "<b>O que custa dinheiro sem aviso, e pega muito turista:</b> cadeira e "
                 "guarda-sol de praia são concessão privada dos hotéis da orla, e a conta "
                 "de restaurante na Ocean Drive costuma vir com <b>gorjeta de serviço já "
                 "incluída</b> — confira antes de somar outra por cima."),
                ("Dias em que não funciona",
                 "<b>Nem a praia nem as ruas fecham.</b> O Art Deco Welcome Center tem "
                 "horário próprio.<br>"
                 "<b>O que fecha é o estacionamento fácil:</b> South Beach é a zona mais "
                 "disputada de Miami para estacionar, e quase tudo ali é pago, por "
                 "aplicativo ou parquímetro."),
                ("Pontos de referência",
                 "O trecho tombado vai da 5ª à 23ª rua, entre a Ocean Drive e a Collins. "
                 "O Art Deco Welcome Center fica na 1001 Ocean Drive. A Lincoln Road "
                 "Mall, calçadão de pedestres, corta o bairro a norte.<br>"
                 + mapa("Art Deco Welcome Center, 1001 Ocean Dr, Miami Beach, FL")),
            ],
        },

        # ---------------------------------------------------------- g3
        {
            "id": "everglades",
            "foto": {"arq": "miami/everglades.webp",
                     "alt": ("A planície de sawgrass do Everglades ao pôr do sol, com nuvens "
                             "altas e a vegetação baixa estendida até o horizonte"),
                     "cred": "evergladesnps · Public domain · via Wikimedia Commons"},
            "grupo": "g3",
            "nome": "Everglades National Park",
            "tag": "Parque nacional",
            "preco_val": "US$ 135",
            "preco_nota": "brasileiro sozinho de carro; US$ 35 é só para morador",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de tarifas do parque (nps.gov/ever) e página central do "
                 "NPS sobre o adicional de não-residente, ambas consultadas em "
                 "29/set/2026.<br>"
                 "<b>A tarifa base:</b> <b>US$ 35 por veículo particular</b>, válida "
                 "<b>7 dias corridos</b> em todas as entradas do parque. Motocicleta "
                 "US$ 30. Pedestre ou ciclista de 16 anos ou mais, US$ 20. Menor de 16 "
                 "não paga.<br>"
                 "<b>E o que muda tudo para você:</b> desde <b>1º de janeiro de 2026</b>, "
                 "quem <b>não mora nos Estados Unidos</b> e tem 16 anos ou mais paga "
                 "<b>US$ 100 a mais, por pessoa</b>. O Everglades é um dos <b>onze "
                 "parques</b> com essa cobrança — ao lado de Grand Canyon, Yellowstone, "
                 "Yosemite, Zion e outros.<br>"
                 "<b>A conta real, então:</b> uma pessoa de carro paga <b>US$ 135</b>. "
                 "Um casal paga <b>US$ 235</b>. Quatro adultos pagam <b>US$ 435</b>.<br>"
                 "<b>Existe um passe de não-residente, a US$ 250</b>, que cobre o "
                 "adicional do portador e de mais três não-residentes de 16 anos ou mais. "
                 "<b>Ele só compensa a partir de três adultos</b> — para casal, sai mais "
                 "caro que pagar o adicional.<br>"
                 "<b>O parque não aceita dinheiro.</b> Só cartão ou passe digital."),
                ("Dias em que não funciona",
                 "<b>O parque não fecha.</b> As entradas têm horários próprios, e os "
                 "centros de visitantes variam com a estação.<br>"
                 "<b>Os oito dias de entrada gratuita do ano não servem para você.</b> "
                 "O texto do NPS é literal: a partir de 2026, a gratuidade desses dias "
                 "vale <b>apenas para cidadãos e residentes americanos</b>, e o "
                 "não-residente paga a tarifa normal <b>mais</b> o adicional. É o único "
                 "ponto desta ficha em que um dia grátis anunciado <b>não</b> é grátis "
                 "para o leitor deste site."),
                ("Antes de comprar o passe, leia isto",
                 FLAG % "Fontes oficiais divergem" +
                 "e a diferença custa dinheiro. <b>A página do próprio Everglades</b> diz "
                 "que o adicional não se aplica a quem usa <i>\"an Annual or America the "
                 "Beautiful Pass\"</i> — o que leria como se o passe anual comum, de "
                 "US$ 70, isentasse. <b>A página central do NPS sobre o adicional</b> diz "
                 "outra coisa: que apenas o <b>America the Beautiful Non-Resident Annual "
                 "Pass</b>, de <b>US$ 250</b>, dispensa a cobrança, e <b>não abre exceção "
                 "para o passe comum</b>.<br>"
                 "<b>São duas páginas oficiais do mesmo órgão, com respostas diferentes, "
                 "sobre uma diferença de US$ 180.</b> Registramos as duas e não "
                 "escolhemos nenhuma. Se for comprar o passe de US$ 70 contando com a "
                 "isenção, confirme na entrada antes — porque a leitura mais restritiva "
                 "é a da página que trata especificamente do assunto."),
                ("Pontos de referência",
                 "Três entradas, longe umas das outras: <b>Shark Valley</b>, na US-41 a "
                 "oeste de Miami, é a mais próxima da cidade e a do passeio de bicicleta "
                 "e do trenzinho. <b>Ernest F. Coe</b>, perto de Homestead, é a entrada "
                 "principal ao sul. <b>Gulf Coast</b>, em Everglades City, fica no "
                 "noroeste e é a das ilhas.<br>"
                 "<b>O bilhete de 7 dias vale nas três</b> — não se paga de novo ao "
                 "trocar de entrada.<br>"
                 + mapa("Everglades National Park Shark Valley Visitor Center, Miami, FL")),
            ],
        },
        {
            "id": "zoo-miami",
            "grupo": "g3",
            "nome": "Zoo Miami",
            "tag": "Zoológico",
            "preco_val": "US$ 30",
            "preco_nota": "adulto, a partir de 1º/out/2026",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial (zoomiami.org), consultado em 29/set/2026.<br>"
                 "<b>Esta ficha pega o zoológico na semana da virada de preço.</b><br>"
                 "<b>Até 30 de setembro de 2026:</b> adulto <b>US$ 25,95 mais imposto</b>, "
                 "criança de 3 a 12 anos <b>US$ 21,95 mais imposto</b>.<br>"
                 "<b>A partir de 1º de outubro de 2026:</b> adulto <b>US$ 30</b> e criança "
                 "de 3 a 12 <b>US$ 26</b>, agora <b>com o imposto já incluído</b>. A "
                 "mudança não é só de valor: é também de forma de anunciar, e por isso o "
                 "aumento real é menor do que a diferença bruta sugere.<br>"
                 "<b>Criança de até 2 anos não paga.</b> <b>Sênior de 65 anos ou mais tem "
                 "25% de desconto</b>, com documento com data de nascimento apresentado na "
                 "compra.<br>"
                 "<b>A ficha de custos usa o preço novo</b>, porque ele passa a valer "
                 "dois dias depois desta apuração e vale para qualquer viagem futura."),
                ("Dias em que não funciona",
                 FLAG % "Horário não confirmado" +
                 "não localizamos o horário de funcionamento em página oficial durante "
                 "esta apuração, e não vamos publicar um horário que não conferimos. "
                 "Confirme no site antes de ir.<br>"
                 "<b>O que se sabe do lugar:</b> são cerca de 300 hectares e mais de 6 km "
                 "de caminhos. É um zoológico grande o bastante para que o calor do meio "
                 "do dia seja o problema principal — e Miami é quente o ano inteiro."),
                ("Pontos de referência",
                 "Fica no sul do condado, em Richmond Heights, bem longe da praia e do "
                 "centro. <b>Não é um ponto de encaixe fácil</b>: não dá para combinar com "
                 "South Beach nem com os museus da baía no mesmo dia sem atravessar a "
                 "cidade duas vezes.<br>"
                 + mapa("Zoo Miami, 12400 SW 152nd St, Miami, FL")),
            ],
        },
        {
            "id": "hospedagem-e-taxas",
            "grupo": "g3",
            "nome": "Hospedagem e as taxas que não estão na diária",
            "tag": "A conta da cama",
            "preco_val": "13% a 14%",
            "preco_nota": "de imposto, mais a resort fee diária",
            "campos": [
                ("O que se soma à diária",
                 "Fonte: página de Tourist and Restaurant Taxes do condado de Miami-Dade "
                 "(miamidade.gov), consultada em 29/set/2026.<br>"
                 "<b>A pilha de impostos muda conforme o bairro, e não é só questão de ser "
                 "mais caro — é outra composição.</b><br>"
                 "<b>No condado em geral</b>, inclusive na cidade de Miami: <b>3%</b> de "
                 "Convention Development Tax, <b>2%</b> de Tourist Development Tax e "
                 "<b>1%</b> de Professional Sports Facilities Franchise Tax. São <b>6%</b> "
                 "de taxas de condado.<br>"
                 "<b>Em Miami Beach</b>: paga os <b>3%</b> de Convention Development, mas "
                 "<b>não</b> paga os outros dois — e no lugar deles entra um <b>resort tax "
                 "municipal de 4%</b> sobre a diária. São <b>7%</b>.<br>"
                 "<b>Surfside e Bal Harbour</b> ficam de fora da maior parte dessas "
                 "cobranças de condado.<br>"
                 "<b>E o imposto estadual da Flórida incide por cima disso</b>, o que leva "
                 "o total para a casa dos <b>13% a 14%</b>. "
                 + FLAG % "Alíquota estadual não conferida" +
                 "a página do condado não publica a parte estadual, e não a apuramos em "
                 "fonte própria — por isso damos a faixa, não um número exato."),
                ("A resort fee, que é o item mais mal explicado de Miami",
                 "<b>Quase todo hotel de área turística cobra uma taxa diária obrigatória</b> "
                 "— chamada de <i>resort fee</i>, <i>destination fee</i> ou <i>amenity "
                 "fee</i> — <b>por cima da diária e por cima dos impostos</b>.<br>"
                 "<b>Em Miami Beach a média fica perto de US$ 25 por noite</b>, e nos "
                 "hotéis de luxo vai de <b>US$ 40 a US$ 60</b>, às vezes mais. Numa estadia "
                 "de cinco noites, isso é de <b>US$ 125 a US$ 300</b> que não estavam na "
                 "diária que você comparou.<br>"
                 "<b>A boa notícia, e ela é recente:</b> desde <b>maio de 2025</b> a regra "
                 "federal americana obriga hotéis e plataformas de reserva a <b>exibir o "
                 "preço total com as taxas obrigatórias já incluídas</b>, logo na busca. "
                 "Ou seja, a resort fee deixou de ser legalmente escondível.<br>"
                 "<b>O que isso muda na prática:</b> o preço que aparece hoje deve já "
                 "contê-la — mas <b>confirme</b>, porque a cobrança continua existindo e "
                 "continua sendo diária. Se o valor anunciado parecer bom demais perto dos "
                 "concorrentes, é o primeiro lugar para olhar."),
                ("Diária média",
                 FLAG % "Sem ADR oficial apurado" +
                 "<b>esta ficha sai sem linha de hospedagem no total</b>, pelo mesmo motivo "
                 "de Fortaleza, Bariloche e Punta Cana: não apuramos diária média publicada "
                 "por órgão oficial para Miami nesta rodada.<br>"
                 "Usar média de agregador seria furar a regra da casa <b>justamente na "
                 "linha mais cara da viagem</b> — e seria pior aqui do que em qualquer "
                 "outro destino, porque em Miami a diária anunciada não é o que se paga: "
                 "faltam os impostos e falta a resort fee."),
            ],
        },
    ],
}

DESTINOS = [MIAMI]
