# -*- coding: utf-8 -*-
"""Apuracao de Bariloche e Punta Cana, com fonte e data em cada numero.

Regra desta casa, aplicada aqui: nada entra sem fonte; onde a fonte nao
existe, a lacuna fica escrita com <span class="flag">; onde duas fontes
divergem, as duas aparecem e nenhuma e escolhida por conveniencia.

UMA DIFERENCA ENTRE OS DOIS DESTINOS, QUE VALE DIZER NA PAGINA

Bariloche tem tarifa publica de verdade. O Parque Nacional Nahuel Huapi
publica a tabela de acesso no proprio site do parque; o Cerro Catedral e
o Teleferico Cerro Otto publicam a deles; o operador da Isla Victoria
publica tarifa, horario e as taxas que NAO estao incluidas. Da para
montar a conta com numero oficial em quase toda linha.

Punta Cana e o oposto. Quase tudo la e operador privado de excursao, com
preco que varia por quem vende, e sem tarifa oficial publicada. O
Ministerio de Medio Ambiente nao publica tarifa de Los Haitises; nao
existe tarifa unica para a Isla Saona; e o Parque Ojos Indigenas aparece
a US$ 50 numa fonte e a US$ 15 em outra.

Isso nao e defeito da apuracao - e como o destino funciona. Mas muda o
que a ficha pode prometer, e esta dito nas duas paginas.

Apuracao de 17 de setembro de 2026.
"""

APURACAO = "17 de setembro de 2026"
APURACAO_CURTA = "17/set/2026"


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
#  BARILOCHE
# =====================================================================
BARILOCHE = {
    "slug": "bariloche",
    "nome": "Bariloche",
    "pais": "Argentina",
    "regiao": "america-do-sul",
    "titulo": "Bariloche: 9 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 9 pontos de Bariloche, com a taxa do "
                  "Parque Nacional que não vem no valor da excursão e as duas "
                  "cobranças que aparecem só no porto."),
    # A abertura e o gancho, em UMA frase - como nos outros onze
    # destinos, que vao de 110 a 222 caracteres. A nota de moeda, que
    # antes estava aqui dentro e levava isto a 944, virou bloco proprio
    # logo abaixo.
    "abertura": ("Nove pontos com preço em peso argentino, horário e fonte conferidos "
                 "em 17 de setembro de 2026 — e o detalhe que muda a conta: <b>a "
                 "excursão mais vendida de Bariloche tem duas cobranças que não estão "
                 "no preço anunciado, e as duas se pagam em dinheiro, no porto</b>."),
    "aviso_moeda": {
        "titulo": "Os preços aqui estão em peso argentino",
        "corpo": (
            "<p><b>Nenhum valor desta página está em real ou em dólar.</b> A inflação "
            "argentina deixa os números com muitos dígitos — a entrada do Parque "
            "Nacional custa <b>ARS 35.000</b> — e seis algarismos são fáceis de ler "
            "como se fossem dólares.</p>"
            "<p><span class=\"flag\">Não convertemos os valores</span> a conversão "
            "automática pela PTAX do Banco Central existe em outras fichas do site e "
            "<b>não pode entrar aqui: o Banco Central publica a cotação de dez moedas, "
            "e o peso argentino não está entre elas</b> — conferimos a lista da API do "
            "PTAX em 17/set/2026.</p>"
            "<p>Para dar ordem de grandeza sem fingir precisão: <b>ARS 1.000 ficavam "
            "perto de R$ 3,40</b> em 17/set/2026, segundo cotação de mercado publicada "
            "pela Wise e pelo Investing.com. <b>Não é taxa oficial e muda todo dia</b> "
            "— use só para dimensionar.</p>"),
    },
    "busca": ("bariloche san carlos de bariloche argentina patagonia rio negro nahuel huapi "
              "parque nacional cerro catedral cerro otto cerro campanario isla victoria "
              "bosque de arrayanes puerto blest cascada los cantaros circuito chico "
              "colonia suiza centro civico museo de la patagonia llao llao peso argentino"),
    "grupos": [
        {"id": "g1", "titulo": "O parque e os cerros",
         "intro": ("Quase tudo em Bariloche está dentro do Parque Nacional Nahuel Huapi "
                   "— e a taxa de acesso é cobrada à parte, em pontos específicos.")},
        {"id": "g2", "titulo": "As navegações",
         "intro": ("As duas excursões de barco clássicas, e as taxas que aparecem "
                   "só quando você chega no porto.")},
        {"id": "g3", "titulo": "A cidade e o que não se paga",
         "intro": ("O centro, o museu e os miradouros do Circuito Chico — onde está "
                   "a maior parte do que Bariloche tem de graça.")},
    ],
    "pontos": [
        {
            "id": "parque-nahuel-huapi",
            "foto": {"arq": "bariloche/parque-nahuel-huapi.webp",
                     "alt": "Floresta de araucárias do Parque Nacional Nahuel Huapi, com picos nevados ao fundo em dia de céu limpo",
                     "cred": "Storyblocks · licença royalty-free · SBI-357934593"}, "grupo": "g1",
            "nome": "Parque Nacional Nahuel Huapi", "tag": "Parque nacional",
            "preco_val": "ARS 35.000", "preco_nota": "estrangeiro, por dia",
            "campos": [
                ("Valor da entrada",
                 "Fonte: tabela de tarifas publicada no site oficial do parque "
                 "(nahuelhuapi.gov.ar), consultada em 17/set/2026.<br>"
                 "<b>Estrangeiro paga ARS 35.000.</b> Residente argentino paga "
                 "<b>ARS 15.000</b>, estudante <b>ARS 12.000</b> e residente da província "
                 "de Río Negro, <b>ARS 8.000</b>. Residente local não paga.<br>"
                 "<b>Não pagam:</b> aposentados e pensionistas, menores de 6 anos, "
                 "pessoas com deficiência e seu acompanhante.<br>"
                 "<b>Há 50% de desconto no segundo dia</b> — a tarifa acima vale para "
                 "o primeiro dia de visita.<br>"
                 "<span class=\"flag\">Fontes divergem na data</span> a imprensa "
                 "patagônica noticiou que esses valores passaram a valer em <b>1º de "
                 "junho de 2026</b>, com alta de 75% sobre os ARS 20.000 anteriores. "
                 "<b>A página oficial mostra a tabela sem informar data de vigência.</b> "
                 "Os valores são os mesmos nas duas fontes; só a data não se confirma."),
                ("Onde a taxa é cobrada",
                 "<b>Não se paga na entrada da cidade.</b> A cobrança acontece em "
                 "pontos específicos: na área de Mascardi, no caminho do Cerro "
                 "Tronador; em <b>Puerto Pañuelo</b>, para quem embarca rumo ao Bosque "
                 "de Arrayanes, Isla Victoria ou Puerto Blest; e na entrada da "
                 "Península Quetrihué.<br>"
                 "<b>Quem fica no Circuito Chico e nos cerros próximos da cidade "
                 "normalmente não passa por posto de cobrança</b> — e é por isso que "
                 "muita gente visita Bariloche sem nunca pagar a taxa."),
                ("Onde fica", mapa("Parque Nacional Nahuel Huapi, Río Negro, Argentina")),
            ],
        },
        {
            "id": "cerro-catedral", "grupo": "g1",
            "nome": "Cerro Catedral", "tag": "Centro de esqui",
            "preco_val": "ARS 90.000", "preco_nota": "passe pedestre; esqui custa ARS 160.000",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de tarifas da Catedral Alta Patagonia "
                 "(catedralaltapatagonia.com), consultada em 17/set/2026. A própria "
                 "página rotula os valores como <b>TARIFAS 2026</b>.<br>"
                 "<b>Passe Pedestre: ARS 90.000.</b> É o que serve para quem vai subir "
                 "para ver a vista, não para esquiar — inclui subida e descida pela "
                 "Telecabina Amancay ou pelo Cabo Carril.<br>"
                 "<b>Passe Esquiador, diário: ARS 160.000.</b><br>"
                 "<b>O ChipCard custa ARS 7.000 à parte e não está incluído</b> em "
                 "nenhum dos dois. É o suporte do passe.<br>"
                 "Crianças de 0 a 5 anos não pagam. Os preços incluem IVA, e o centro "
                 "aceita pagamento em pesos ou em dólares."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias, das 8h às 16h.</b> As bilheterias da base "
                 "atendem das 9h às 16h30 — meia hora a mais que os meios de elevação.<br>"
                 "<span class=\"flag\">O que não apuramos</span> o Cerro Catedral opera "
                 "em duas temporadas muito diferentes, e <b>não encontramos tabela "
                 "separada de verão</b>. Os valores acima são os publicados como tarifa "
                 "2026, sem distinção de estação na própria página."),
                ("Onde fica", mapa("Cerro Catedral, San Carlos de Bariloche, Argentina")),
            ],
        },
        {
            "id": "cerro-otto", "grupo": "g1",
            "nome": "Teleférico Cerro Otto", "tag": "Teleférico",
            "preco_val": "ARS 60.000", "preco_nota": "maior de 13 anos",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de tarifas e horários do próprio teleférico "
                 "(telefericobariloche.com.ar), consultada em 17/set/2026.<br>"
                 "<b>Maior de 13 anos: ARS 60.000.</b> Criança de 6 a 12 anos, maior de "
                 "65 anos e residente pagam <b>ARS 30.000</b>. Menor de 5 anos não paga.<br>"
                 "<b>Existe um bilhete só do teleférico, a ARS 30.000</b>, para quem não "
                 "quer o complexo inteiro — metade do preço da entrada completa."),
                ("Dias em que não funciona",
                 "<b>A base e a bilheteria funcionam das 10h às 16h30</b>; o complexo "
                 "opera até as 18h15 e as áreas externas, das 9h30 às 17h.<br>"
                 "<b>O transporte da cidade até a base é gratuito</b>, saindo da esquina "
                 "de Mitre com Villegas, no centro. O estacionamento na base também não "
                 "se paga.<br>"
                 "<span class=\"flag\">Atenção ao consultar</span> no dia da apuração a "
                 "página oficial marcava todos os setores como <b>Cerrada</b>. Isso "
                 "costuma ser manutenção ou fechamento de temporada — <b>reconfira na "
                 "véspera</b>."),
                ("Onde fica", mapa("Teleférico Cerro Otto, San Carlos de Bariloche, Argentina")),
            ],
        },
        {
            "id": "cerro-campanario", "grupo": "g1",
            "nome": "Cerro Campanario", "tag": "Aerossilha",
            "preco_val": "ARS 18.000", "preco_nota": "adulto; criança de 6 a 12, ARS 10.000",
            "campos": [
                ("Valor da entrada",
                 "<b>ARS 18.000 para adulto</b> e <b>ARS 10.000 para criança de 6 a 12 anos</b>, "
                 "pela aerossilha que sobe ao mirante.<br>"
                 "<span class=\"flag\">Fonte não oficial</span> este é o único ponto "
                 "desta ficha cujo preço <b>não saiu da página do próprio operador</b>. "
                 "O valor vem de portais de turismo de Bariloche consultados em "
                 "17/set/2026, que coincidem entre si. <b>Trate como ordem de grandeza, "
                 "não como tarifa confirmada.</b><br>"
                 "É de longe o mirante mais barato da cidade — o Cerro Otto custa mais "
                 "de três vezes isso."),
                ("Dias em que não funciona",
                 "<b>A aerossilha opera das 9h às 17h30.</b><br>"
                 "Fica no <b>quilômetro 17,5 da Avenida Bustillo</b>, com estacionamento "
                 "no acesso. Há confeitaria no topo.<br>"
                 "<b>Dá para subir a pé</b>, por trilha, sem pagar a aerossilha — a "
                 "subida é curta e íngreme."),
                ("Onde fica", mapa("Cerro Campanario, Avenida Bustillo km 17.5, Bariloche")),
            ],
        },
        {
            "id": "isla-victoria", "grupo": "g2",
            "nome": "Isla Victoria e Bosque de Arrayanes", "tag": "Navegação",
            "preco_val": "ARS 182.600", "preco_nota": "as três cobranças somadas",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de horários e tarifas do operador "
                 "(islavictoriayarrayanes.com), consultada em 17/set/2026. A página "
                 "informa vigência a partir de <b>1º de junho de 2026</b>.<br>"
                 "<b>São três cobranças, e só a primeira aparece no anúncio:</b><br>"
                 "• Excursão, adulto: <b>ARS 140.000</b> (menor: ARS 70.000)<br>"
                 "• Taxa de acesso ao Parque Nacional: <b>ARS 35.000</b> "
                 "(residente argentino: ARS 15.000; menor de 5 anos: grátis)<br>"
                 "• Taxa de embarque: <b>ARS 7.600</b><br>"
                 "Total para estrangeiro adulto: <b>ARS 182.600</b>.<br>"
                 "<b>As duas taxas se pagam em dinheiro, no Puerto Pañuelo</b>, e não "
                 "entram na reserva. É a pegadinha mais cara de Bariloche.<br>"
                 "<span class=\"flag\">Fontes divergem</span> revendedores anunciavam a "
                 "excursão a <b>ARS 152.000</b> na mesma data em que o operador publicava "
                 "<b>ARS 140.000</b>. Usamos o valor do operador; <b>o do revendedor pode "
                 "embutir transfer</b>, que o operador cobra à parte a ARS 22.000."),
                ("Dias em que não funciona",
                 "<b>Saídas diárias, em dois turnos.</b><br>"
                 "<b>Turno integral:</b> transfer às 10h20, embarque às 11h40, saída às "
                 "12h15, retorno às 18h30. Fica cerca de <b>2h30 na Isla Victoria</b> e "
                 "45 minutos no Bosque de Arrayanes.<br>"
                 "<b>Turno meio-dia:</b> transfer às 12h20, embarque às 13h20, saída às "
                 "13h55, retorno às 18h30. <b>Só 1 hora na Isla Victoria</b>, com os "
                 "mesmos 45 minutos no bosque.<br>"
                 "<b>Dois operadores fazem o mesmo passeio</b> — Turisur, com o barco "
                 "Modesta Victoria, e Espacio, com o catamarã Cau Cau. Horário, preço e "
                 "roteiro são os mesmos; muda o barco."),
                ("Onde fica", mapa("Puerto Pañuelo, Península Llao Llao, Bariloche")),
            ],
        },
        {
            "id": "puerto-blest", "grupo": "g2",
            "nome": "Puerto Blest e Cascada Los Cántaros", "tag": "Navegação",
            "preco_val": "ARS 136.000", "preco_nota": "sem a taxa do parque",
            "campos": [
                ("Valor da entrada",
                 "<b>ARS 136.000 por adulto</b>, pela Turisur, operadora do passeio. "
                 "Consultado em 17/set/2026.<br>"
                 "O operador informa <b>sinal de ARS 24.000 na reserva</b> e o saldo de "
                 "<b>ARS 112.000 no dia da excursão</b>.<br>"
                 "<b>Não inclui a chegada ao porto, as taxas nem as refeições.</b> Como "
                 "o embarque também é no Puerto Pañuelo, <b>valem as mesmas duas "
                 "cobranças da Isla Victoria</b> — taxa do parque e taxa de embarque.<br>"
                 "<span class=\"flag\">O que não apuramos</span> <b>não confirmamos o "
                 "valor da taxa de embarque especificamente para este passeio</b>. Para "
                 "a Isla Victoria, saindo do mesmo porto, ela é de ARS 7.600."),
                ("Dias em que não funciona",
                 "<b>Excursão de dia inteiro</b>, com saída de manhã e retorno por volta "
                 "das <b>17h30</b>.<br>"
                 "Inclui navegação e caminhada guiada por passarelas de madeira pela "
                 "selva valdiviana até a <b>Cascada Los Cántaros</b>.<br>"
                 "<b>Há um trecho opcional até o Lago Frías</b>, de águas verdes de "
                 "origem glaciária, cobrado à parte."),
                ("Onde fica", mapa("Puerto Blest, Parque Nacional Nahuel Huapi, Argentina")),
            ],
        },
        {
            "id": "circuito-chico",
            "foto": {"arq": "bariloche/circuito-chico.webp",
                     "alt": "Vista do lago Nahuel Huapi a partir do Punto Panorámico, com a península coberta de mata e a cordilheira nevada ao fundo",
                     "cred": "Storyblocks · licença royalty-free · SBI-357309567"}, "grupo": "g3",
            "nome": "Circuito Chico e Punto Panorámico", "tag": "Estrada cênica",
            "preco_val": "Grátis", "preco_nota": "Parque Municipal Llao Llao",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga nada.</b> Todos os pontos do Circuito Chico estão "
                 "dentro do <b>Parque Municipal Llao Llao</b>, de acesso livre. "
                 "Consultado em 17/set/2026.<br>"
                 "<b>O que se paga é opcional:</b> a aerossilha do Cerro Campanario, se "
                 "você quiser subir sem caminhar.<br>"
                 "<b>O Punto Panorámico</b> fica a <b>945 metros de altitude</b>, na "
                 "área do Lago Moreno, e é o ponto mais distante do percurso — com vista "
                 "do lago, do hotel Llao Llao e da capela San Eduardo."),
                ("Dias em que não funciona",
                 "<b>Estrada aberta o ano todo</b>, sem horário nem bilheteria.<br>"
                 "<b>Não passa por posto de cobrança do Parque Nacional</b> — é por isso "
                 "que dá para fazer o Circuito Chico inteiro sem pagar a taxa de "
                 "ARS 35.000.<br>"
                 "Excursões guiadas que percorrem o circuito custavam de "
                 "<b>ARS 40.000 a ARS 80.000</b> conforme incluíssem o Campanario ou a "
                 "Colonia Suiza. <span class=\"flag\">Fonte não oficial</span> essa "
                 "faixa vem de portais de turismo, não de tabela publicada."),
                ("Onde fica", mapa("Circuito Chico, San Carlos de Bariloche, Argentina")),
            ],
        },
        {
            "id": "colonia-suiza", "grupo": "g3",
            "nome": "Colonia Suiza", "tag": "Vilarejo",
            "preco_val": "Grátis", "preco_nota": "feira às quartas e domingos",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga para entrar.</b> Consultado em 17/set/2026.<br>"
                 "É um vilarejo de montanha a <b>25 km de Bariloche</b>, dentro do "
                 "percurso do Circuito Chico.<br>"
                 "<b>A Feira Regional acontece às quartas-feiras e aos domingos</b>, com "
                 "produtos artesanais. É o motivo pelo qual vale escolher o dia.<br>"
                 "<span class=\"flag\">O que não apuramos</span> <b>não levantamos preço "
                 "de nada que se venda na feira</b> nem do <i>curanto</i>, o prato "
                 "cozido em buraco no chão que é a especialidade do lugar."),
                ("Dias em que não funciona",
                 "<b>O vilarejo está aberto todo dia.</b> A feira, só <b>quarta e "
                 "domingo</b> — nos outros dias o lugar é bem mais parado."),
                ("Onde fica", mapa("Colonia Suiza, San Carlos de Bariloche, Argentina")),
            ],
        },
        {
            "id": "museo-patagonia", "grupo": "g3",
            "nome": "Museo de la Patagonia", "tag": "Museu",
            "preco_val": "Contribuição", "preco_nota": "bônus voluntário, sem valor fixo",
            "campos": [
                ("Valor da entrada",
                 "<b>Não há tarifa fixa publicada.</b> O museu é do Parques Nacionales e "
                 "cobra <b>bônus de contribuição não obrigatório</b>. Consultado em "
                 "17/set/2026.<br>"
                 "<span class=\"flag\">Não achamos o valor oficial</span> tentamos o site "
                 "do museu (museodelapatagonia.nahuelhuapi.gov.ar) e ele respondeu com "
                 "erro de servidor no dia da apuração. <b>Relatos de visitantes de 2026 "
                 "mencionam ARS 3.000 de contribuição</b>, e guias antigos ainda repetem "
                 "<b>ARS 300</b>, valor que a inflação argentina tornou implausível.<br>"
                 "<b>Não escolhemos entre os dois.</b> O que dá para afirmar é que a "
                 "contribuição não é obrigatória."),
                ("Dias em que não funciona",
                 "<b>Fecha domingo e segunda.</b><br>"
                 "<b>De terça a sexta:</b> das 10h às 12h30 e das 14h às 19h — "
                 "<b>fecha no meio do dia</b>.<br>"
                 "<b>Sábado:</b> das 10h às 17h, sem intervalo.<br>"
                 "Fica no <b>Centro Cívico</b>, e tem salas de pré-história, história "
                 "étnica, história regional e ciências naturais."),
                ("Onde fica", mapa("Museo de la Patagonia, Centro Cívico, Bariloche")),
            ],
        },
    ],
}


# =====================================================================
#  PUNTA CANA
# =====================================================================
PUNTA_CANA = {
    "slug": "punta-cana",
    "nome": "Punta Cana",
    "pais": "República Dominicana",
    # O indice nao tem filtro "caribe": Cancun, que tambem e Caribe, esta
    # em america-do-norte. Seguir a taxonomia que existe em vez de criar
    # uma categoria com um destino so.
    "regiao": "america-do-norte",
    "titulo": "Punta Cana: 7 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 7 pontos de Punta Cana — e por que "
                  "quase nenhum deles tem tarifa oficial publicada, ao contrário "
                  "do que acontece no México ou na Argentina."),
    "abertura": ("Sete pontos apurados em 17 de setembro de 2026 — e uma diferença "
                 "que muda como esta página pode ser lida: <b>em Punta Cana quase "
                 "nada tem tarifa oficial publicada</b>. O que existe é preço de "
                 "operador, e ele varia por quem vende."),
    "busca": ("punta cana republica dominicana dominicana caribe bavaro macao playa "
              "hoyo azul scape park cap cana isla saona cotubanama los haitises "
              "ojos indigenas altos de chavon la romana casa de campo tarjeta de turista "
              "peso dominicano dolar"),
    "grupos": [
        {"id": "g1", "titulo": "O que tem preço publicado",
         "intro": ("Os pontos em que encontramos valor divulgado por quem opera o "
                   "lugar — e mesmo aqui, as fontes nem sempre concordam.")},
        {"id": "g2", "titulo": "O que só tem preço de excursão",
         "intro": ("Parques nacionais e ilhas onde o Estado não publica tarifa e "
                   "quem define o preço é o operador que te leva.")},
        {"id": "g3", "titulo": "O que a lei garante de graça",
         "intro": ("As praias — e a lei dominicana que impede qualquer resort de "
                   "cobrar por elas ou fechar o acesso.")},
    ],
    "pontos": [
        {
            "id": "hoyo-azul", "grupo": "g1",
            "nome": "Hoyo Azul e Scape Park", "tag": "Cenote e parque",
            "preco_val": "US$ 129", "preco_nota": "admissão geral; só o cenote, US$ 65",
            "campos": [
                ("Valor da entrada",
                 "Consultado em 17/set/2026 nas páginas do parque e de operadores "
                 "autorizados.<br>"
                 "<b>Admissão geral: a partir de US$ 129</b> por adulto. "
                 "<b>Criança de 5 a 12 anos: US$ 69.</b> Menor de 5 anos não paga.<br>"
                 "<b>Só o Hoyo Azul, sem o parque: a partir de US$ 65.</b><br>"
                 "A admissão geral inclui o cenote, as <b>cuevas taínas</b>, as cachoeiras "
                 "Iguabonita, o Iguanaland e o cenote indígena.<br>"
                 "<span class=\"flag\">Preço de partida, não preço</span> todas as fontes "
                 "dizem <b>\"a partir de\"</b>. Não encontramos tabela fechada, e os "
                 "pacotes com transporte e almoço iam de <b>US$ 119 a US$ 159</b> no "
                 "mesmo dia, conforme o revendedor."),
                ("Dias em que não funciona",
                 "<span class=\"flag\">Não apuramos o horário</span> <b>nenhuma das "
                 "fontes consultadas publicava horário de abertura e fechamento.</b> "
                 "O que aparece é recomendação de ir <b>entre 8h e 9h</b> para evitar "
                 "fila, e a informação de que opera o ano todo.<br>"
                 "<b>Reconfira o horário antes de ir</b> — esta é uma lacuna real desta "
                 "ficha, não um esquecimento."),
                ("Onde fica", mapa("Scape Park Cap Cana, Punta Cana, República Dominicana")),
            ],
        },
        {
            "id": "ojos-indigenas", "grupo": "g1",
            "nome": "Reserva Ecológica Ojos Indígenas", "tag": "Reserva privada",
            "preco_val": "US$ 15 ou US$ 50", "preco_nota": "as duas fontes, sem escolher",
            "campos": [
                ("Valor da entrada",
                 "Consultado em 17/set/2026.<br>"
                 "<span class=\"flag\">Fontes divergem, e muito</span> uma fonte publica "
                 "<b>US$ 15 por adulto e US$ 8 por criança de 6 a 12 anos</b>, com menor "
                 "de 6 grátis. Outra publica <b>US$ 50 por visitante</b>. <b>É mais de "
                 "três vezes de diferença, e não conseguimos conciliar.</b> As duas ficam "
                 "aqui; leve o valor maior.<br>"
                 "<b>Quem está hospedado em hotel do grupo não paga</b> — entre eles o "
                 "Westin Puntacana e o Four Points by Sheraton — e ainda tem transporte "
                 "gratuito até a reserva.<br>"
                 "A reserva é <b>privada</b>, da Fundación Ecológica Puntacana, criada em "
                 "1994. Não é área pública, e por isso pode cobrar o que definir."),
                ("Dias em que não funciona",
                 "<span class=\"flag\">Não apuramos os horários</span> <b>não encontramos "
                 "horário de funcionamento publicado em fonte confiável.</b><br>"
                 "Se você está em um dos hotéis do grupo, a recepção resolve isso e a "
                 "entrada não custa nada."),
                ("Onde fica", mapa("Reserva Ecológica Ojos Indígenas, Punta Cana")),
            ],
        },
        {
            "id": "altos-de-chavon", "grupo": "g1",
            "nome": "Altos de Chavón", "tag": "Vila e anfiteatro",
            "preco_val": "US$ 60", "preco_nota": "excursão; criança de 4 a 12, US$ 35",
            "campos": [
                ("Valor da entrada",
                 "Consultado em 17/set/2026.<br>"
                 "<b>US$ 60 por adulto e US$ 35 por criança de 4 a 12 anos</b>, com menor "
                 "de 4 grátis.<br>"
                 "<span class=\"flag\">Isso é preço de excursão, não de entrada</span> o "
                 "valor sai de operadores que levam de Punta Cana, e <b>inclui o "
                 "transporte de ida e volta, que são cerca de 2 horas de estrada em cada "
                 "sentido</b>. Não é bilheteria.<br>"
                 "<b>E há uma restrição séria de acesso:</b> Altos de Chavón fica dentro "
                 "do resort <b>Casa de Campo</b>, que reserva o direito de admissão e "
                 "declara permitir entrada <b>apenas a hóspedes com reserva confirmada</b> "
                 "no hotel ou em villa do complexo. <b>Ir por conta própria pode não "
                 "funcionar</b> — a excursão organizada existe também por isso."),
                ("Dias em que não funciona",
                 "<span class=\"flag\">Não apuramos os horários</span> <b>a vila não "
                 "publica horário de visitação</b> em fonte que tenhamos encontrado. "
                 "Quem vai em excursão segue o horário do operador.<br>"
                 "A visita costuma incluir o <b>anfiteatro</b>, a galeria de arte, o "
                 "<b>museu arqueológico</b> e a vista do rio Chavón."),
                ("Onde fica", mapa("Altos de Chavón, La Romana, República Dominicana")),
            ],
        },
        {
            "id": "isla-saona",
            "foto": {"arq": "punta-cana/isla-saona.webp",
                     "alt": "Praia da Isla Saona vista do alto, com água rasa turquesa e a linha de coqueiros acompanhando a costa",
                     "cred": "Storyblocks · licença royalty-free · SBI-357989562"}, "grupo": "g2",
            "nome": "Isla Saona", "tag": "Ilha em parque nacional",
            "preco_val": "US$ 75 a 135", "preco_nota": "excursão compartilhada",
            "campos": [
                ("Valor da entrada",
                 "Consultado em 17/set/2026.<br>"
                 "<b>Não existe tarifa oficial única.</b> A ilha fica dentro do "
                 "<b>Parque Nacional Cotubanamá</b>, e o que se paga é a excursão, não "
                 "uma bilheteria.<br>"
                 "<b>Excursão compartilhada: US$ 75 a US$ 135 por pessoa</b>, conforme o "
                 "operador, o ponto de saída, o tipo de embarcação e o que inclui de "
                 "comida.<br>"
                 "<b>Lancha privada: a partir de US$ 650</b> para 4 a 10 pessoas. "
                 "<b>Catamarã privado de dia inteiro: a partir de US$ 1.500.</b><br>"
                 "<span class=\"flag\">A variação é o dado</span> uma faixa de US$ 75 a "
                 "US$ 135 para o mesmo destino <b>não é imprecisão da nossa apuração</b> "
                 "— é como o mercado funciona ali. O que muda o preço é o que está "
                 "incluído, e isso precisa estar por escrito antes de pagar."),
                ("Dias em que não funciona",
                 "<span class=\"flag\">Depende do operador</span> <b>não há horário "
                 "público do parque</b>; cada excursão tem o seu, e todas são de dia "
                 "inteiro.<br>"
                 "<b>Confirme por escrito, antes de pagar:</b> preço final, hora e local "
                 "de embarque, o que está incluído, política de cancelamento e o que "
                 "acontece se o tempo virar."),
                ("Onde fica", mapa("Isla Saona, Parque Nacional Cotubanamá, República Dominicana")),
            ],
        },
        {
            "id": "los-haitises", "grupo": "g2",
            "nome": "Parque Nacional Los Haitises", "tag": "Parque nacional",
            "preco_val": "Sem tarifa publicada", "preco_nota": "excursão a partir de € 115",
            "campos": [
                ("Valor da entrada",
                 "Consultado em 17/set/2026 no portal do <b>Ministerio de Medio Ambiente "
                 "y Recursos Naturales</b> (ambiente.gob.do).<br>"
                 "<span class=\"flag\">O ministério não publica a tarifa</span> o parque "
                 "tem página oficial no ministério, <b>mas sem tabela de preços</b>. "
                 "Procuramos e não encontramos valor de entrada divulgado pelo Estado "
                 "dominicano.<br>"
                 "<b>O que existe é preço de excursão: a partir de € 115 por adulto</b>, "
                 "de operador privado.<br>"
                 "<b>Isso é diferente do México e da Argentina</b>, onde o INAH e o "
                 "Parques Nacionales publicam tabela. Aqui, quem define o preço é quem "
                 "te leva."),
                ("Dias em que não funciona",
                 "<span class=\"flag\">Não apuramos</span> <b>não encontramos horário de "
                 "visitação publicado.</b> As excursões saem de manhã e são de dia "
                 "inteiro.<br>"
                 "O parque é de <b>mogotes cársticos, manguezais e cavernas com arte "
                 "rupestre taína</b> — a visita é de barco, e a parte terrestre depende "
                 "da maré."),
                ("Onde fica", mapa("Parque Nacional Los Haitises, Sabana de la Mar, República Dominicana")),
            ],
        },
        {
            "id": "playa-bavaro",
            "foto": {"arq": "punta-cana/playa-bavaro.webp",
                     "alt": "Faixa de areia da Playa Bávaro vista do alto, com o mar turquesa quebrando na praia e coqueiros na orla",
                     "cred": "Storyblocks · licença royalty-free · SBI-358012617"}, "grupo": "g3",
            "nome": "Playa Bávaro", "tag": "Praia",
            "preco_val": "Grátis", "preco_nota": "acesso garantido por lei",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga, e isso não é cortesia dos hotéis — é lei.</b> "
                 "Consultado em 17/set/2026.<br>"
                 "O <b>artigo 15 da Constituição dominicana</b> estabelece que praias e "
                 "costas pertencem ao domínio público e são de <b>livre acesso</b>.<br>"
                 "A <b>Lei 305-68</b> cria uma <b>faixa marítimo-terrestre de 60 metros</b> "
                 "contados da linha de preamar, onde é proibido construir sem autorização "
                 "do Poder Executivo.<br>"
                 "<b>Ninguém pode cercar a praia, colocar barreira ou impedir a passagem</b> "
                 "— e <b>a segurança de um hotel não tem poder para barrar você</b> dentro "
                 "dessa faixa. Violar a lei 305-68 prevê pena de dois meses a um ano ou "
                 "multa."),
                ("Dias em que não funciona",
                 "<b>Sempre aberta.</b> Não há bilheteria, horário nem portão.<br>"
                 "<b>O que o hotel pode cobrar</b> é o uso do que é dele: espreguiçadeira, "
                 "guarda-sol, bar, banheiro. <b>A areia dentro dos 60 metros, não.</b>"),
                ("Onde fica", mapa("Playa Bávaro, Punta Cana, República Dominicana")),
            ],
        },
        {
            "id": "playa-macao", "grupo": "g3",
            "nome": "Playa Macao", "tag": "Praia",
            "preco_val": "Grátis", "preco_nota": "a praia pública mais aberta da região",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga.</b> Vale a mesma base legal da Playa Bávaro: artigo 15 "
                 "da Constituição e Lei 305-68. Consultado em 17/set/2026.<br>"
                 "<b>Macao é a praia da região com menos resort em cima dela</b> — é onde "
                 "o acesso público é mais evidente na prática, não só no papel.<br>"
                 "<span class=\"flag\">O que não apuramos</span> <b>não levantamos preço "
                 "de estacionamento, de aula de surfe nem de barraca</b> na praia. São "
                 "serviços privados, com preço que varia por fornecedor."),
                ("Dias em que não funciona",
                 "<b>Sempre aberta</b>, sem horário nem bilheteria.<br>"
                 "<b>O mar de Macao é bem mais agitado que o de Bávaro</b> — é praia de "
                 "onda, usada para surfe, e não a piscina calma que a maioria dos "
                 "folhetos de Punta Cana mostra."),
                ("Onde fica", mapa("Playa Macao, Punta Cana, República Dominicana")),
            ],
        },
    ],
}

DESTINOS = [BARILOCHE, PUNTA_CANA]
