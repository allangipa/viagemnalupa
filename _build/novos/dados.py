# -*- coding: utf-8 -*-
"""Apuracao de Cancun e Fortaleza, com fonte e data em cada numero.

Regra desta casa, aplicada aqui: nada entra sem fonte; onde a fonte nao
existe, a lacuna fica escrita com <span class="flag">; onde duas fontes
divergem, as duas aparecem e nenhuma e escolhida por conveniencia.

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


CANCUN = {
    "slug": "cancun",
    "nome": "Cancún",
    "pais": "México",
    "regiao": "america-do-norte",
    "titulo": "Cancún: 6 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e endereço de 6 pontos de Cancún e da Riviera Maya, "
                  "com o reajuste que dobrou Tulum em 2026 e as duas bilheterias de "
                  "Chichén Itzá."),
    "abertura": ("Seis pontos com preço, horário e endereço conferidos em 17 de setembro "
                 "de 2026 — e o detalhe que muda a conta: <b>as ruínas têm duas "
                 "bilheterias, e só uma delas aparece nos guias</b>."),
    "busca": ("cancun cancún mexico méxico quintana roo caribe america do norte chichen itza "
              "chichén itzá tulum zona arqueologica maya museo maya san miguelito isla mujeres "
              "ultramar ferry xcaret playa delfines zona hotelera riviera maya inah peso mexicano"),
    "grupos": [
        {"id": "g1", "titulo": "As ruínas maias",
         "intro": ("Os três sítios que o turista de Cancún visita — e o que mudou de preço "
                   "em 2026, porque mudou muito.")},
        {"id": "g2", "titulo": "Cancún, a cidade e o mar",
         "intro": ("O que dá para fazer sem sair da região, incluindo a praia que não "
                   "cobra nada e o parque que custa mais que um voo doméstico.")},
    ],
    "pontos": [
        {
            "id": "chichen-itza", "grupo": "g1",
            "nome": "Chichén Itzá", "tag": "Zona arqueológica",
            "preco_val": "MX$ 697", "preco_nota": "duas bilheterias somadas",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página oficial do INAH para a zona arqueológica, consultada em "
                 "17/set/2026.<br><b>São duas cobranças, e é isso que pega o visitante "
                 "desavisado:</b> MX$ 105 do INAH, que é a taxa federal, mais <b>MX$ 592 "
                 "da taxa estadual de Yucatán</b> para estrangeiro. Dá <b>MX$ 697</b>. "
                 "O mexicano paga MX$ 105 + MX$ 205.<br>"
                 "<span class=\"flag\">Fontes divergem</span> a imprensa mexicana publicou "
                 "em janeiro de 2026 que a taxa estadual seria de MX$ 571, e a página do "
                 "INAH diz MX$ 592. <b>Não conseguimos conciliar as duas</b>, e por isso "
                 "as duas estão aqui. Leve o valor maior."),
                ("Dias em que não funciona",
                 "<b>Abre todos os dias</b>, de segunda a domingo, das <b>8h às 16h</b>.<br>"
                 "<b>O domingo gratuito não vale para você.</b> A isenção dominical do INAH "
                 "é para mexicanos e estrangeiros <b>residentes no México</b>, com "
                 "documento. O turista brasileiro paga integral todos os dias."),
                ("Onde fica",
                 "A <b>115 km de Mérida</b> pela rodovia 180, junto à localidade de Piste, "
                 "a 2 km do sítio. Há transporte público até Piste.<br>"
                 "<b>De Cancún são cerca de 200 km</b>, o que faz deste o bate-volta mais "
                 "longo do guia. Telefone: 985 851 0137.<br>"
                 + mapa("Chichen Itza, Yucatan, Mexico")),
                ("Quem não paga",
                 "Maiores de 60 anos, menores de 13, aposentados, pensionistas, pessoas com "
                 "deficiência, docentes e estudantes em atividade são isentos da taxa do "
                 "INAH.<br><span class=\"flag\">Não confirmado</span> se a isenção vale "
                 "também para a taxa estadual de Yucatán, que é a parte cara. A página do "
                 "INAH não trata dela."),
            ],
        },
        {
            "id": "tulum", "grupo": "g1",
            "nome": "Tulum", "tag": "Zona arqueológica",
            "preco_val": "MX$ 210", "preco_nota": "dobrou de preço em 2026",
            "campos": [
                ("Valor da entrada",
                 "Fonte: INAH, consultado em 17/set/2026.<br><b>MX$ 210 de segunda a "
                 "sábado</b> para estrangeiro. Mexicano e estrangeiro residente no México "
                 "pagam MX$ 105.<br><b>Repare no que mudou:</b> em 2025 a entrada custava "
                 "cerca de MX$ 104. O reajuste de 2026 <b>praticamente dobrou o valor</b>. "
                 "Qualquer guia escrito antes deste ano está errado por metade."),
                ("Dias e horários",
                 "<b>8h às 17h, com última entrada às 15h30.</b> Chegar às 16h é chegar "
                 "depois do portão fechar para novas entradas, mesmo com o sítio ainda "
                 "aberto."),
                ("Onde fica",
                 "Dentro do <b>Parque del Jaguar</b>, em Quintana Roo, a cerca de 130 km de "
                 "Cancún.<br><span class=\"flag\">Não apurado</span> o Parque del Jaguar "
                 "pode cobrar taxa própria, somada à do INAH, como acontece em Chichén "
                 "Itzá com a taxa estadual. <b>Não achamos o valor em fonte oficial</b> e "
                 "não vamos publicar um número que não confirmamos.<br>"
                 + mapa("Zona Arqueologica de Tulum, Quintana Roo, Mexico")),
                ("Fatos históricos",
                 "Tulum é <b>a única cidade maia construída na beira do mar</b> entre as "
                 "que o turista de Cancún alcança, e era murada — o nome em maia ioucateque "
                 "significa justamente cerca ou muralha.<br>"
                 "<span class=\"flag\">Não confirmado</span> as datas de fundação e "
                 "abandono que circulam variam bastante entre fontes, e não achamos uma "
                 "referência oficial do INAH que as feche. Ficam de fora até fecharem."),
            ],
        },
        {
            "id": "museo-maya", "grupo": "g1",
            "nome": "Museo Maya de Cancún e San Miguelito", "tag": "Museu e sítio",
            "preco_val": "MX$ 210", "preco_nota": "museu e ruínas no mesmo bilhete",
            "campos": [
                ("Valor da entrada",
                 "Fonte: INAH, consultado em 17/set/2026.<br><b>MX$ 210 para estrangeiro</b>, "
                 "MX$ 105 para mexicano. <b>O bilhete vale para os dois:</b> o museu e a "
                 "zona arqueológica de San Miguelito, que fica no mesmo terreno.<br>"
                 "<b>É o melhor custo do guia:</b> duas visitas pelo preço de uma entrada "
                 "de Tulum, sem sair da Zona Hoteleira."),
                ("Dias em que não funciona",
                 "<b>Fecha às segundas.</b> Abre de terça a domingo, das 9h às 18h.<br>"
                 "<b>E há dois relógios diferentes:</b> a última entrada no museu é às 17h, "
                 "mas <b>em San Miguelito é às 16h30</b>. Quem chega às 16h45 pega só o "
                 "museu."),
                ("Onde fica",
                 "Boulevard Kukulcán, km 16,5, esquina com San Miguelito, <b>dentro da Zona "
                 "Hoteleira</b> de Cancún. É o único ponto deste guia que não exige "
                 "bate-volta.<br>" + mapa("Museo Maya de Cancun, Boulevard Kukulcan, Cancun")),
                ("Quem não paga",
                 "Menores de 13 anos, estudantes e docentes com credencial mexicana, "
                 "pensionistas, aposentados, maiores de 60 com credencial INAPAM e pessoas "
                 "com deficiência. Domingo é gratuito para mexicanos e residentes — "
                 "<b>não para o turista brasileiro</b>."),
            ],
        },
        {
            "id": "isla-mujeres", "grupo": "g2",
            "nome": "Isla Mujeres, de ferry", "tag": "Ilha e travessia",
            "preco_val": "MX$ 580", "preco_nota": "ida e volta, por adulto",
            "campos": [
                ("Valor da entrada",
                 "Fonte: tabela de tarifas da Ultramar, consultada em 17/set/2026.<br>"
                 "<b>MX$ 290 a ida e MX$ 580 ida e volta</b> para adulto. Criança paga "
                 "MX$ 220 e MX$ 440.<br><b>Atenção à regra de altura, não de idade:</b> "
                 "<b>criança acima de 1,20 m paga tarifa de adulto</b>. Menor de 1 ano não "
                 "paga, mas precisa de cartão de embarque.<br><b>Entrar na ilha é de "
                 "graça</b> — o que se paga é a travessia."),
                ("Onde fica",
                 "Sai de <b>Puerto Juárez</b> ou da <b>Playa Tortugas</b>, na Zona "
                 "Hoteleira, <b>pelo mesmo preço</b>. De Puerto Juárez a travessia leva "
                 "cerca de 20 minutos.<br><span class=\"flag\">Horário não apurado</span> "
                 "a Ultramar informa que as tarifas e os horários podem mudar sem aviso e "
                 "não publica a grade completa na página de tarifas. Reconfira no dia.<br>"
                 + mapa("Puerto Juarez Ultramar, Cancun, Quintana Roo")),
                ("Estacionamento",
                 "O terminal de Puerto Juárez cobra estacionamento.<br>"
                 "<span class=\"flag\">Fontes divergem</span> os valores que circulam são "
                 "MX$ 20 por hora e MX$ 324 por 24 horas, mas não estão na tabela oficial "
                 "da Ultramar que consultamos. <b>Trate como ordem de grandeza.</b>"),
            ],
        },
        {
            "id": "xcaret", "grupo": "g2",
            "nome": "Xcaret", "tag": "Parque temático",
            "preco_val": "MX$ 1.890 a 2.480", "preco_nota": "não tem preço, tem sistema",
            "campos": [
                ("Valor da entrada",
                 "<b>Xcaret não tem um preço; tem uma faixa que muda com a data e o tipo "
                 "de bilhete.</b> É o mesmo mecanismo dos parques de Orlando.<br>"
                 "<span class=\"flag\">Fontes divergem</span> apuramos <b>três valores "
                 "diferentes</b> em 17/set/2026 para a entrada de adulto: MX$ 1.890, "
                 "MX$ 2.180 e MX$ 2.480, conforme a fonte e o tipo de bilhete (básico ou "
                 "plus). <b>Criança aparece a MX$ 1.660.</b><br><b>Não escolhemos um dos "
                 "três.</b> O preço real é o que o site oficial mostrar para a sua data — "
                 "e é por isso que ele não entra fechado na ficha de custos."),
                ("Dias e horários",
                 "<b>Abre todos os dias, das 8h30 às 22h.</b> O show noturno "
                 "<i>México Espectacular</i> é o fecho do dia e acontece no fim da noite — "
                 "quem sai às 18h paga o dia inteiro e perde a parte que justifica o "
                 "horário estendido."),
                ("Onde fica",
                 "Na Riviera Maya, a cerca de 70 km de Cancún, perto de Playa del Carmen.<br>"
                 + mapa("Parque Xcaret, Riviera Maya, Quintana Roo, Mexico")),
            ],
        },
        {
            "id": "playa-delfines", "grupo": "g2",
            "nome": "Playa Delfines", "tag": "Praia pública",
            "preco_val": "Grátis", "preco_nota": "praia é federal no México",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga.</b> No México <b>toda praia é federal e de acesso "
                 "público</b> — nenhum hotel pode fechar a faixa de areia. Playa Delfines é "
                 "a maior praia pública da Zona Hoteleira e a que tem acesso mais fácil "
                 "para quem não está hospedado na orla.<br>"
                 "<span class=\"flag\">Sem preço apurado</span> não levantamos valor de "
                 "cadeira, guarda-sol ou estacionamento, e por isso nada disso entra na "
                 "ficha de custos."),
                ("Onde fica",
                 "Boulevard Kukulcán, no trecho alto da Zona Hoteleira — é o mirante de "
                 "onde se vê a faixa inteira de areia.<br>"
                 + mapa("Playa Delfines, Boulevard Kukulcan, Cancun")),
                ("Dias e horários",
                 "<b>Aberta sempre.</b><br><span class=\"flag\">Não apurado</span> se há "
                 "horário de guarda-vidas ou restrição de bandeira em dia de mar grosso. "
                 "Não achamos a informação em fonte oficial do município."),
            ],
        },
    ],
}


FORTALEZA = {
    "slug": "fortaleza",
    "nome": "Fortaleza",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "Fortaleza: 7 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e endereço de 7 pontos de Fortaleza e do Ceará, com a "
                  "taxa de Jericoacoara que a Justiça suspendeu e os espaços do Dragão do "
                  "Mar que estão fechados."),
    "abertura": ("Sete pontos com preço, horário e endereço conferidos em 17 de setembro de "
                 "2026 — e o detalhe que muda a conta: <b>a taxa mais falada do Ceará está "
                 "suspensa pela Justiça, e muito guia ainda a cobra na conta</b>."),
    "busca": ("fortaleza ceara ceará brasil nordeste beach park aquiraz porto das dunas "
              "insano arvorar dragao do mar dragão centro cultural theatro jose de alencar "
              "burle marx mercado central catedral metropolitana sao jose praia do futuro "
              "barracas jericoacoara jijoca parque nacional icmbio taxa turismo sustentavel"),
    "grupos": [
        {"id": "g1", "titulo": "O centro histórico, a pé",
         "intro": ("Três endereços a distância de caminhada no Centro — e os três fecham ou "
                   "mudam de horário em dias diferentes da semana.")},
        {"id": "g2", "titulo": "Praia, parque e o bate-volta",
         "intro": ("O que exige carro, barco ou dia inteiro. Aqui está a taxa que a Justiça "
                   "suspendeu e o parque cujo preço muda conforme a data que você escolher.")},
    ],
    "pontos": [
        {
            "id": "theatro-jose-de-alencar", "grupo": "g1",
            "nome": "Theatro José de Alencar", "tag": "Teatro histórico",
            "preco_val": "R$ 10", "preco_nota": "visita guiada; meia a R$ 5",
            "campos": [
                ("Valor da entrada",
                 "Apurado em 17/set/2026.<br><b>R$ 10 a inteira e R$ 5 a meia.</b> "
                 "<b>Criança até 5 anos e pessoa acima de 60 não pagam.</b><br>"
                 "<b>É o ingresso mais barato deste guia</b>, e dá acesso guiado a seis "
                 "espaços cênicos, ao prédio de 1910 e aos jardins."),
                ("Dias em que não funciona",
                 "<b>Fecha às segundas.</b> Abre de terça a sábado das 8h às 18h e "
                 "<b>domingo só de manhã</b>, das 9h às 13h.<br>"
                 "<b>A visita guiada tem hora marcada</b>, não é livre: 9h, 10h30, 14h e "
                 "16h de terça a sábado; <b>aos domingos, só 9h e 10h30</b>. Recomenda-se "
                 "chegar 20 minutos antes."),
                ("Onde fica",
                 "Praça José de Alencar, no Centro de Fortaleza. Fica a distância de "
                 "caminhada do Mercado Central e da Catedral.<br>"
                 + mapa("Theatro Jose de Alencar, Fortaleza, Ceara")),
                ("Fatos históricos",
                 "Inaugurado em <b>17 de junho de 1910</b>. As obras começaram em "
                 "<b>6 de junho de 1908</b> e levaram dois anos.<br>"
                 "<b>A estrutura metálica veio de Glasgow, na Escócia</b>, fundida pela "
                 "<b>Walter MacFarlane &amp; Company</b> e importada pela Casa Boris — é "
                 "ferro escocês montado em praça cearense, e está à vista, sem "
                 "revestimento.<br><b>Os jardins de Burle Marx não são originais.</b> O "
                 "projeto de 1908 já imaginava um teatro-jardim, mas a parte verde e a "
                 "estatuária só vieram <b>na reforma de 1975</b>, 65 anos depois da "
                 "inauguração.<br><b>Tombado pelo IPHAN desde 1964.</b>"),
            ],
        },
        {
            "id": "mercado-central", "grupo": "g1",
            "nome": "Mercado Central", "tag": "Mercado de artesanato",
            "preco_val": "Grátis", "preco_nota": "entrar; paga-se o que se leva",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga para entrar.</b> São <b>mais de 600 lojas em cinco "
                 "andares</b>, com rede, renda, bordado, cachaça, rapadura e castanha.<br>"
                 "<span class=\"flag\">Sem preço apurado</span> não levantamos faixa de "
                 "preço de rede nem de artesanato, e por isso nada disso entra na ficha de "
                 "custos."),
                ("Dias e horários",
                 "<b>Abre todos os dias, com três horários diferentes:</b> segunda a sexta "
                 "das 8h às 18h, <b>sábado até as 17h</b> e <b>domingo só até as 13h</b>.<br>"
                 "<b>Quem deixa o mercado para o domingo à tarde não entra.</b>"),
                ("Onde fica",
                 "Av. Alberto Nepomuceno, 199, Centro. Telefone (85) 3454-8586.<br>"
                 + mapa("Mercado Central de Fortaleza, Avenida Alberto Nepomuceno, Fortaleza")),
            ],
        },
        {
            "id": "catedral-metropolitana", "grupo": "g1",
            "nome": "Catedral Metropolitana de São José", "tag": "Igreja",
            "preco_val": "Grátis", "preco_nota": "visitação em horário próprio",
            "campos": [
                ("Valor da entrada",
                 "<b>Não se paga.</b> A catedral tem <b>capacidade para cinco mil "
                 "pessoas</b> e ocupa boa parte da Praça Pedro II, no Centro."),
                ("Dias e horários",
                 "<b>Visitação de segunda a sexta, das 8h às 12h e das 13h às 17h; "
                 "sábado só de manhã</b>, das 8h às 12h.<br><b>Repare que há um intervalo "
                 "no meio do dia</b> — quem chega ao meio-dia pega a porta fechada.<br>"
                 "<b>Missas:</b> domingo às 10h, 12h e 18h30; de segunda a sexta ao "
                 "meio-dia.<br><span class=\"flag\">Não apurado</span> se a visitação "
                 "turística é permitida durante a missa."),
                ("Onde fica",
                 "Praça Pedro II, Centro — a poucos quarteirões do Mercado Central.<br>"
                 + mapa("Catedral Metropolitana de Fortaleza, Praca Pedro II, Fortaleza")),
                ("Fatos históricos",
                 "<b>Inaugurada em 1978, depois de quase quarenta anos de obra.</b> É uma "
                 "das construções mais longas da cidade e a razão de o estilo parecer de "
                 "outra época: o projeto é muito anterior à entrega."),
            ],
        },
        {
            "id": "praia-do-futuro", "grupo": "g2",
            "nome": "Praia do Futuro", "tag": "Praia urbana",
            "preco_val": "Grátis", "preco_nota": "a areia; as barracas cobram consumo",
            "campos": [
                ("Valor da entrada",
                 "<b>A praia não cobra nada.</b> São <b>mais de 7 km</b> de faixa larga, "
                 "areia clara e mar aberto.<br><b>O que cobra é a barraca:</b> as "
                 "estruturas da orla oferecem mesa, chuveiro, banheiro e refeição, e "
                 "algumas têm acesso livre com consumo.<br>"
                 "<span class=\"flag\">Sem preço apurado</span> não levantamos valor de "
                 "consumação mínima nem de aluguel de mesa nas barracas, e por isso isso "
                 "não entra na ficha de custos."),
                ("Onde fica",
                 "Leste de Fortaleza, ao longo da Av. Zezé Diogo.<br>"
                 + mapa("Praia do Futuro, Fortaleza, Ceara")),
                ("Dias e horários",
                 "<b>Aberta sempre.</b> As barracas têm horário próprio, cada uma o seu.<br>"
                 "<span class=\"flag\">Não apurado</span> horário de guarda-vidas e "
                 "sinalização de banho. <b>O mar da Praia do Futuro é aberto e tem "
                 "correnteza</b> — e isso é relevante o bastante para não ser publicado "
                 "sem fonte oficial."),
            ],
        },
        {
            "id": "beach-park", "grupo": "g2",
            "nome": "Beach Park", "tag": "Parque aquático",
            "preco_val": "A partir de R$ 250", "preco_nota": "o preço muda conforme a data",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial de ingressos do Beach Park, consultado em "
                 "17/set/2026.<br><b>Aqua Park a partir de R$ 250.</b> O <b>Parque "
                 "Arvorar</b>, que é o parque de animais e tem mais de 250 bichos, "
                 "<b>a partir de R$ 129</b>.<br><b>Não existe um preço fechado:</b> o valor "
                 "muda conforme a data escolhida e a antecedência da compra.<br>"
                 "<span class=\"flag\">Fontes divergem</span> sites de terceiros publicam "
                 "faixa de R$ 210 a R$ 325 e prometem R$ 210 com 44 dias de antecedência. "
                 "<b>O site oficial anuncia a partir de R$ 250.</b> Ficam os dois — e o "
                 "oficial é o que vale no checkout."),
                ("Quando é barato e quando é caro",
                 "<b>Antecipar baixa o preço</b>, é a regra declarada pelo próprio parque. "
                 "Há desconto para pagamento em Pix no Aqua Park.<br>"
                 "<b>Hóspede dos resorts do Beach Park entra no Aqua Park uma hora mais "
                 "cedo</b> — o que, num parque de fila, vale mais que desconto."),
                ("Dias e horários",
                 "<b>Aqua Park:</b> bilheteria abre às 10h30 e o parque opera das "
                 "<b>11h às 17h</b>.<br><b>Parque Arvorar:</b> das <b>9h às 17h</b>.<br>"
                 "<span class=\"flag\">Não apurado</span> os dias de fechamento anual e "
                 "eventuais manutenções. O site não publica calendário."),
                ("Quem não paga",
                 "<b>Criança de até 1 metro de altura</b>, acompanhada de adulto pagante, "
                 "<b>não paga</b>. Acima de 1 metro e até 12 anos paga ingresso infantil.<br>"
                 "<b>A régua é altura, não idade</b> — e é a mesma lógica do ferry de Isla "
                 "Mujeres, em Cancún."),
                ("Onde fica",
                 "Praia de Porto das Dunas, em <b>Aquiraz</b>, a <b>27 km</b> de "
                 "Fortaleza.<br><b>Cabanas:</b> a Continente, para 8 pessoas, a partir de "
                 "R$ 890 a diária; a Ilha, para 16, R$ 1.090.<br>"
                 + mapa("Beach Park, Porto das Dunas, Aquiraz, Ceara")),
            ],
        },
        {
            "id": "dragao-do-mar", "grupo": "g1",
            "nome": "Centro Dragão do Mar", "tag": "Centro cultural",
            "preco_val": "Grátis", "preco_nota": "cerca de 90% da programação",
            "campos": [
                ("Valor da entrada",
                 "Fonte: Instituto Dragão do Mar, consultado em 17/set/2026.<br>"
                 "<b>Cerca de 90% das atividades são gratuitas ou de preço simbólico</b>, "
                 "segundo o próprio instituto.<br><b>O cinema custa de R$ 8 a R$ 16</b>, e "
                 "<b>às terças cai para R$ 5 a R$ 10</b>.<br>São 14.500 m² com dois museus, "
                 "cinema, teatro, planetário e galerias."),
                ("Dias em que não funciona",
                 "<b>Fecha às segundas.</b> Abre de terça a domingo, das 9h às 21h.<br>"
                 "<b>Os museus têm horário próprio</b>, mais curto: de quarta a sábado das "
                 "9h às 19h, domingo e feriado das 10h às 19h. <b>Quem for numa terça pega "
                 "o centro aberto e os museus fechados.</b>"),
                ("O que está fechado agora",
                 "<b>O teatro e o planetário estão sem programação, em manutenção</b>, "
                 "segundo o Instituto Dragão do Mar em 17/set/2026.<br><b>São justamente "
                 "os dois espaços mais citados em guia de viagem.</b> Quem for pelo "
                 "planetário vai encontrar porta fechada — e isso não aparece na maioria "
                 "das listas de o-que-fazer.<br><span class=\"flag\">Sem data de "
                 "reabertura</span> não há previsão publicada."),
                ("Onde fica",
                 "Rua Dragão do Mar, 81, Praia de Iracema — na virada do Centro para a "
                 "orla.<br>" + mapa("Centro Dragao do Mar de Arte e Cultura, Fortaleza")),
            ],
        },
        {
            "id": "jericoacoara", "grupo": "g2",
            "nome": "Jericoacoara", "tag": "Parque nacional",
            "preco_val": "R$ 41,50", "preco_nota": "e não R$ 91,50 — leia abaixo",
            "campos": [
                ("Valor da entrada",
                 "Apurado em 17/set/2026.<br><b>A única taxa obrigatória é a Taxa de "
                 "Turismo Sustentável, de R$ 41,50 por pessoa</b>, cobrada pela Prefeitura "
                 "de Jijoca de Jericoacoara.<br><b>A taxa de R$ 50 do ICMBio está "
                 "suspensa.</b> A concessão do Parque Nacional previa somar R$ 50 aos "
                 "R$ 41,50 municipais, <b>mas a Justiça Federal suspendeu a cobrança</b> "
                 "até que o ICMBio e a concessionária apresentem plano detalhado. Em "
                 "dezembro de 2025 o <b>TRF-5 rejeitou o recurso do ICMBio pela segunda "
                 "vez</b>, e a suspensão continua.<br><b>Traduzindo para a sua conta:</b> "
                 "muito roteiro publicado soma R$ 91,50. <b>Hoje são R$ 41,50.</b>"),
                ("Dias e horários",
                 "<span class=\"flag\">Não apurado</span> horário de entrada de veículo na "
                 "vila e restrição de tráfego nas dunas. <b>O acesso final é por areia e "
                 "depende de 4x4 ou transfer</b>, mas não achamos a regra oficial "
                 "publicada."),
                ("Onde fica",
                 "Vila de Jericoacoara, em <b>Jijoca de Jericoacoara</b>, a cerca de 300 km "
                 "de Fortaleza.<br><b>É bate-volta longo</b> — a maior parte de quem vai "
                 "dorme lá.<br>" + mapa("Jericoacoara, Jijoca de Jericoacoara, Ceara")),
            ],
        },
    ],
}


DESTINOS = [CANCUN, FORTALEZA]
