# -*- coding: utf-8 -*-
"""Aruba: o trigesimo destino, em catorze pontos e tres grupos.

Mesmo molde do florianopolis/dados.py, lido por novos/gera.py com VNL_DADOS=aruba.
Precos na moeda em que sao cobrados: dolar (US$) e florim (Afl.). Sem conversao.

O ACHADO PRINCIPAL: A ED CARD E GRATIS, MAS A TAXA DE US$ 20 VEM JUNTO
----------------------------------------------------------------------
aruba.com (Aruba Tourism Authority), lido em 15/11/2026: desde 1o/jul/2024 a
Sustainability Fee de US$ 20 e paga no proprio formulario de entrada (ED
card), so no cartao de credito, antes do check-in do voo. Isentos: menores
de 8 anos e quem volta no mesmo ano civil - mas "the system is not capable
of recognizing repeat visitors": quem volta paga de novo e pede reembolso,
e "Refunds will not be granted after more than 60 days".

O SEGUNDO: A CONTA DO HOTEL TEM 12,5% E MAIS US$ 3 POR QUARTO POR NOITE
----------------------------------------------------------------------
Landsverordening toeristenheffing, art. 5: 12,5% do valor pago pelo quarto
(no all-inclusive, sobre 50% do pacote, minimo de Afl. 178,52 por dia). E
a BBV do impuesto.aw: Afl. 5,37 (US$ 3) por noite por quarto ocupado. A
diaria media de 2025 foi US$ 408,99 (Banco Central de Aruba).

O QUE FICOU SEM RESPOSTA
----------------------------------------------------------------------
    Renaissance Island   day pass de nao hospede: preco e regra
    Fort Zoutman         preco e horario do museu
    Alto Vista, Bushiribana, Natural Bridge   cobranca e horario
    Arikok               forma de pagamento; o site tem dois horarios
    taxi                 tarifa por destino alem das quatro do aeroporto
    permanencia          o numero de dias do brasileiro: "determinado na
                         imigracao"

Apuracao de 15 de novembro de 2026.
"""

APURACAO = "15 de novembro de 2026"
APURACAO_CURTA = "15/nov/2026"

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


LACUNA = FLAG % "Lacuna declarada"

# =====================================================================
#  ARUBA
# =====================================================================
ARUBA = {
    "slug": "aruba",
    "nome": "Aruba",
    "pais": "Aruba (Reino dos Países Baixos)",
    "regiao": "america-do-norte",
    "titulo": "Aruba: 14 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 14 pontos de Aruba, com a taxa de US$ 20 que vem "
                  "no formulário de entrada e os 12,5% mais US$ 3 por noite que não estão na "
                  "diária do hotel."),
    "abertura": ("Catorze pontos de Aruba com preço, horário e fonte conferidos em 15 de "
                 "novembro de 2026 — e duas cobranças que os guias não somam: <b>o formulário "
                 "de entrada é grátis, mas a taxa de US$ 20 por pessoa vem dentro dele</b>, só "
                 "no cartão e antes do check-in do voo; e <b>a conta do hotel leva 12,5% de "
                 "imposto e mais US$ 3 por quarto por noite</b>, por cima de uma diária média de "
                 "US$ 408,99. A praia, pela política oficial da ilha, é pública."),
    "busca": ("aruba caribe reino dos paises baixos ed card sustainability fee taxa de "
              "sustentabilidade arikok parque nacional natural pool conchi natural bridge baby "
              "bridge bushiribana donkey sanctuary eagle beach fofoti palm beach baby beach "
              "renaissance island flamingo beach california lighthouse farol butterfly farm "
              "oranjestad fort zoutman arubus taxi toeristenheffing imposto hospedagem florim "
              "dolar"),
    "grupos": [
        {"id": "g1", "titulo": "O Arikok e a costa norte",
         "intro": ("O parque nacional que cobra US$ 22 e manda a piscina natural só de 4x4, "
                   "a costa selvagem do lado oposto aos hotéis, e o santuário que vive de "
                   "doação.")},
        {"id": "g2", "titulo": "As praias",
         "intro": ("Públicas pela política oficial da ilha — com a regra de 2026 sobre a "
                   "cadeira do hotel, e a única praia famosa em que você não entra.")},
        {"id": "g3", "titulo": "O noroeste, Oranjestad e a conta",
         "intro": ("O farol de US$ 5, a fazenda de borboletas que deixa voltar, a capital sem "
                   "preço publicado no museu — e as três cobranças que chegam antes, durante e "
                   "depois da diária.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - Arikok e a costa norte
        # =============================================================
        {
            "id": "arikok",
            "foto": {"arq": "aruba/arikok.webp",
                     "alt": "A pedra com o nome Parke Nacional Arikok na entrada do parque, entre cactos altos",
                     "cred": "Ginelly.Q · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Parque Nacional Arikok",
            "tag": "Parque nacional",
            "preco_val": "US$ 22",
            "preco_nota": "adulto; menor de 17 não paga",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de experiências da <b>Aruba Conservation Foundation</b> "
                 "(acf.aw), que administra o parque, consultada em 15/nov/2026.<br>"
                 "<i>“Adults: USD22 per person”</i>; <i>“Children (&lt;17): Free”</i>. "
                 "<i>“A valid conservation pass is required to enter the park.”</i><br>"
                 "Compra-se nas entradas de <b>San Fuego</b> e <b>Vader Piet</b>. O endereço "
                 "antigo do parque (arubanationalpark.org) hoje redireciona para a fundação.<br>"
                 + LACUNA + "a página não diz se aceita cartão ou só dinheiro, nem o preço do "
                 "passe anual."),
                ("Dias e horários",
                 "O site diz <i>“Open Daily”</i>. O centro de visitantes de San Fuego abre "
                 "das 8h às 15h30.<br>"
                 + FLAG % "Fontes divergem" + "para Vader Piet o mesmo site dá 8h30 às 15h "
                 "numa página e 9h às 15h na outra."),
                ("O que não pode",
                 "<b>ATV, UTV e moto são proibidos</b> nas áreas protegidas (acf.aw)."),
                ("Onde fica",
                 mapa("Arikok National Park San Fuego visitor center, Aruba")),
            ],
        },
        {
            "id": "natural-pool",
            "grupo": "g1",
            "nome": "Natural Pool (Conchi)",
            "tag": "Piscina natural",
            "preco_val": "US$ 22",
            "preco_nota": "o passe do Arikok; só de 4x4",
            "campos": [
                ("O que se paga, e como se chega",
                 "Fonte: página oficial da <b>Aruba Tourism Authority</b> (aruba.com), "
                 "consultada em 15/nov/2026.<br>"
                 "Não tem ingresso próprio: <i>“An entrance pass to Arikok National Park is "
                 "required.”</i><br>"
                 "<i>“Accessible only by 4x4 vehicle.”</i> <b>É regra do parque, não conselho "
                 "de guia</b>: com o carro comum de locadora você não chega. As outras opções "
                 "são tour de 4x4, cavalgada ou a trilha a pé, de três a quatro horas, ida e "
                 "volta."),
                ("Quando nadar",
                 "<i>“Swimming is only safe when ocean conditions are calm.”</i> Siga os "
                 "guardas; sapatilha de água é recomendada. Não é indicado para quem tem "
                 "mobilidade reduzida.<br>"
                 + LACUNA + "horário próprio e dias de fechamento, que dependem do mar."),
                ("Onde fica",
                 mapa("Natural Pool Conchi, Arikok National Park, Aruba")),
            ],
        },
        {
            "id": "costa-norte",
            "foto": {"arq": "aruba/costa-norte.webp",
                     "alt": "A costa norte de Aruba, seca e de pedras escuras, com o mar batendo e a trilha de terra ao longe",
                     "cred": "Rarends297 · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Costa norte: Bushiribana e a ponte que caiu",
            "tag": "Costa",
            "preco_val": "—",
            "preco_nota": "cobrança e horário não publicados",
            "campos": [
                ("A Natural Bridge não existe mais",
                 "Fonte: aruba.com, consultado em 15/nov/2026. <i>“Before collapsing in 2005, "
                 "the largest and most photographed of these bridges was the famous Natural "
                 "Bridge.”</i> <b>A que está de pé, ao lado, é a Baby Bridge.</b> Foto antiga "
                 "em folheto não é a ponte de hoje."),
                ("As ruínas de Bushiribana",
                 "O moinho de ouro fica no caminho da ponte: a corrida do ouro em Aruba começou "
                 "em <i>“the year 1824”</i>, segundo a mesma fonte, e a exploração foi até "
                 "1916.<br>"
                 + LACUNA + "nenhuma das duas páginas oficiais fala de cobrança ou horário. "
                 "Não escrevemos “grátis” no lugar."),
                ("Onde fica",
                 "Na costa norte, entre as ruínas de Bushiribana e Andicuri Beach — o lado "
                 "oposto ao dos hotéis.<br>" +
                 mapa("Bushiribana Gold Mill Ruins, Aruba")),
            ],
        },
        {
            "id": "donkey-sanctuary",
            "grupo": "g1",
            "nome": "Donkey Sanctuary",
            "tag": "Santuário",
            "preco_val": "Grátis",
            "preco_nota": "aceita doação",
            "campos": [
                ("Valor e horário",
                 "Fonte: site oficial do santuário (arubandonkey.org), consultado em "
                 "15/nov/2026.<br>"
                 "<i>“There is no admission fee, though your generous donations are greatly "
                 "appreciated.”</i><br>"
                 "Todos os dias, <b>das 9h às 16h</b>. <i>“Closed only on January 1st.”</i>"),
                ("Como chegar",
                 "Fica no fim de uma estrada de terra, pela Route 4a até o French Man's Pass. "
                 "<b>As coordenadas de GPS do próprio site têm erro</b> — os minutos passam de "
                 "60 —, então use o nome do lugar no mapa."),
                ("Onde fica",
                 mapa("Donkey Sanctuary Aruba")),
            ],
        },
        # =============================================================
        #  g2 - praias
        # =============================================================
        {
            "id": "eagle-beach",
            "foto": {"arq": "aruba/eagle-beach.webp",
                     "alt": "Uma árvore fofoti torta na areia branca da Eagle Beach, com o mar azul ao fundo",
                     "cred": "Rarends297 · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Eagle Beach",
            "tag": "Praia",
            "preco_val": "Grátis",
            "preco_nota": "praia pública; a cadeira do hotel é do hotel",
            "campos": [
                ("A praia é pública — e a regra de 2026",
                 "Fonte: governo de Aruba (gobierno.aw, 24/02/2026): <i>“All beaches remain "
                 "public and accessible to both Aruban residents and visitors.”</i><br>"
                 "Mas a diretriz da Aruba Tourism Authority de 29/04/2026: palapa e "
                 "espreguiçadeira montadas pelo hotel <i>“are considered in use, even if the "
                 "guest steps away”</i>. E há trechos com permissão de uso do hotel, que "
                 "<i>“are not part of the public beach”</i>. A areia junto ao mar continua de "
                 "todos.<br>"
                 + FLAG % "Política, não lei" + "o governo fala em política de praias, sem "
                 "citar o artigo de lei."),
                ("O que tem ali",
                 "Estacionamento público, sombra e ônibus (aruba.com). <i>“Most turtle nests "
                 "are found on Eagle Beach”</i> — e é onde ficam as árvores fofoti mais "
                 "fotografadas da ilha."),
                ("Onde fica",
                 mapa("Eagle Beach, Aruba")),
            ],
        },
        {
            "id": "palm-beach",
            "grupo": "g2",
            "nome": "Palm Beach",
            "tag": "Praia",
            "preco_val": "Grátis",
            "preco_nota": "praia pública, a dos hotéis altos",
            "campos": [
                ("Valor, e onde a regra pesa mais",
                 "Pública, com estacionamento e ônibus (aruba.com, 15/nov/2026). É a praia "
                 "dos hotéis <i>“high-rise”</i> — e por isso é <b>onde mais pesa a diretriz de "
                 "2026</b>: a espreguiçadeira montada pelo hotel conta como “em uso” mesmo "
                 "vazia. Leve a sua toalha, ou alugue."),
                ("Onde fica",
                 mapa("Palm Beach, Aruba")),
            ],
        },
        {
            "id": "baby-beach",
            "foto": {"arq": "aruba/baby-beach.webp",
                     "alt": "A água turquesa e rasa da Baby Beach, com pedras na beira e o horizonte limpo",
                     "cred": "Todd42013 · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Baby Beach",
            "tag": "Praia",
            "preco_val": "Grátis",
            "preco_nota": "cabanas grátis; cadeira e snorkel alugados",
            "campos": [
                ("O que não se paga, e o que se aluga",
                 "Fonte: aruba.com, consultado em 15/nov/2026. Entrada sem custo e "
                 "<i>“Complimentary huts”</i> — cabanas de sombra de graça. Cama de praia, "
                 "quebra-vento e snorkel são alugados, <i>“at a rental fee”</i>.<br>"
                 + LACUNA + "o valor do aluguel."),
                ("A regra, e a distância",
                 "<i>“For your safety please stay within the marked snorkel area.”</i> Fica no "
                 "extremo sul, perto de San Nicolas — <b>cerca de 45 minutos dos hotéis de Palm "
                 "Beach</b>, no lado oposto da ilha. É dia inteiro."),
                ("Onde fica",
                 mapa("Baby Beach, San Nicolas, Aruba")),
            ],
        },
        {
            "id": "renaissance-island",
            "grupo": "g2",
            "nome": "Renaissance Island e a Flamingo Beach",
            "tag": "Ilha privada",
            "preco_val": "—",
            "preco_nota": "só para hóspedes; day pass sem preço publicado",
            "campos": [
                ("Quem entra",
                 "Fonte: aruba.com, consultado em 15/nov/2026. A ilha é <i>“only available "
                 "to guests of Renaissance Wind Creek Aruba Resort”</i>, das 7h às 19h, com "
                 "water taxi a cada 15 minutos.<br>"
                 "<b>É a praia dos flamingos das fotos — e a única desta lista em que você não "
                 "entra sem estar hospedado.</b>"),
                ("O day pass que ninguém publica",
                 LACUNA + "nem a autoridade de turismo nem o site do resort publicam day pass "
                 "para quem não é hóspede, preço ou regra de reserva. A página da rede hoteleira "
                 "respondeu 403, e não contornamos bloqueio. Valores de blog e de agregador não "
                 "foram usados.<br>"
                 + FLAG % "Fontes divergem" + "o próprio resort diz, numa frase, que a "
                 "Flamingo Beach é só para adultos e, noutra, que crianças entram numa janela "
                 "de manhã."),
                ("Onde fica",
                 mapa("Renaissance Island, Aruba")),
            ],
        },
        # =============================================================
        #  g3 - noroeste, Oranjestad e a conta
        # =============================================================
        {
            "id": "california-lighthouse",
            "foto": {"arq": "aruba/california-lighthouse.webp",
                     "alt": "O alto do farol California, branco, contra o céu azul",
                     "cred": "NoTalkMan · CC0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "California Lighthouse",
            "tag": "Farol",
            "preco_val": "US$ 5",
            "preco_nota": "para subir; sem reserva",
            "campos": [
                ("Valor e horário",
                 "Fonte: aruba.com, consultado em 15/nov/2026. <i>“$5 admission fee no "
                 "reservations required.”</i> Sobe-se até o topo.<br>"
                 "<i>“Open everyday from 9:00 am - 7:00 pm.”</i><br>"
                 "<b>É o ingresso mais barato da ilha</b> — e aparece embutido em pacotes de "
                 "agência como se fosse caro.<br>"
                 + LACUNA + "quem não paga e a forma de pagamento."),
                ("Onde fica",
                 "No extremo noroeste, depois dos hotéis de Palm Beach.<br>" +
                 mapa("California Lighthouse, Aruba")),
            ],
        },
        {
            "id": "butterfly-farm",
            "grupo": "g3",
            "nome": "Butterfly Farm",
            "tag": "Jardim",
            "preco_val": "US$ 19",
            "preco_nota": "adulto; o ingresso deixa voltar na viagem",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de informação ao visitante do site oficial "
                 "(thebutterflyfarm.com), consultada em 15/nov/2026.<br>"
                 "<i>“$19.00 Adults”</i>; <i>“$16.00 Seniors and Students (ID required)”</i>; "
                 "<i>“$10.00 Children 4-17 years old”</i>. Menor de 4 não paga."),
                ("O ingresso que vale a viagem",
                 "<i>“Entrance includes a free return pass for the duration of your vacation, "
                 "valid for one month maximum.”</i> <b>Paga uma vez e volta quantas vezes "
                 "quiser.</b> Vale ir de manhã cedo, quando as borboletas estão mais ativas, e "
                 "voltar outro dia.<br>"
                 "<i>“Open all year, daily 8.30am - 4.30pm”</i>; o último tour guiado é às 16h."),
                ("Onde fica",
                 mapa("The Butterfly Farm, Palm Beach, Aruba")),
            ],
        },
        {
            "id": "oranjestad",
            "grupo": "g3",
            "nome": "Oranjestad: o Forte Zoutman e o bonde",
            "tag": "Capital",
            "preco_val": "—",
            "preco_nota": "museu sem preço publicado; o bonde, “From $0”",
            "campos": [
                ("O forte e o museu",
                 "O Fort Zoutman é o prédio mais antigo de Oranjestad; a torre Willem III foi "
                 "farol e relógio público, e <i>“the light in the tower was extinguished in "
                 "1963”</i> (aruba.com, 15/nov/2026).<br>"
                 + LACUNA + "a página atual não publica preço nem horário do museu. O único "
                 "valor oficial achado é de um manual de 2014, velho demais para valer."),
                ("O bonde do centro",
                 "Liga o terminal de cruzeiros ao centro pela Main Street, com seis paradas. A "
                 "autoridade de turismo mostra <i>“From $0”</i>.<br>"
                 + LACUNA + "a página não diz com todas as letras que é grátis, nem o horário "
                 "e o operador."),
                ("Onde fica",
                 mapa("Fort Zoutman, Oranjestad, Aruba")),
            ],
        },
        {
            "id": "entrada",
            "grupo": "g3",
            "nome": "A entrada: ED card e a taxa de US$ 20",
            "tag": "Conta, não lugar",
            "preco_val": "US$ 20",
            "preco_nota": "por pessoa, de avião; menor de 8 não paga",
            "campos": [
                ("O formulário é grátis, a taxa vem junto",
                 "Fonte: páginas da <b>Aruba Tourism Authority</b> sobre a Sustainability Fee "
                 "(aruba.com, em inglês e em português), consultadas em 15/nov/2026.<br>"
                 "<i>“Starting July 1st, 2024, Aruba will implement a $20 Sustainability Fee "
                 "for visitors arriving by air.”</i> A página em português diz que a taxa "
                 "<i>“será permanente”</i>.<br>"
                 "É paga <b>no próprio ED card</b>, o formulário de entrada on-line, e <b>só no "
                 "cartão de crédito</b>: <i>“A taxa deve ser paga antes do check-in da "
                 "companhia aérea, para obter sua liberação.”</i> Não se paga na chegada."),
                ("Quem não paga, e o erro do sistema",
                 "<b>Isentos: menor de 8 anos</b>, quem chega e sai no mesmo dia, residente — e "
                 "quem volta no mesmo ano civil. Mas: <i>“the system is not capable of "
                 "recognizing repeat visitors”</i>. Quem volta <b>paga de novo e pede "
                 "reembolso</b> por e-mail, e <i>“Refunds will not be granted after more than "
                 "60 days.”</i><br>"
                 "<b>O ED card é obrigatório até para bebê</b> — ele preenche, mas não paga. "
                 "Preencha entre 7 dias e 4 horas antes do voo, no portal oficial "
                 "(edcardaruba.aw). A própria autoridade avisa: <i>“No pagues más de $20 "
                 "dólares de tasa de sostenibilidad”</i> — há sites que cobram para "
                 "“ajudar”."),
                ("Visto e passaporte",
                 "<b>Brasileiro não precisa de visto</b>: o Brasil está na lista de isentos da "
                 "página oficial. Visto americano ou Schengen não muda nada para o brasileiro — "
                 "essa regra vale só para passaportes bolivianos e jamaicanos. O passaporte "
                 "precisa de <b>6 meses de validade</b> além da data de saída.<br>"
                 + LACUNA + "o número de dias de permanência: <i>“O período de admissão será "
                 "determinado na imigração.”</i>"),
            ],
        },
        {
            "id": "transporte",
            "grupo": "g3",
            "nome": "Ônibus e táxi",
            "tag": "Transporte",
            "preco_val": "US$ 2,60",
            "preco_nota": "a viagem de ônibus; passe do dia US$ 15",
            "campos": [
                ("O ônibus",
                 "Fonte: tarifas do site oficial do <b>Arubus</b> (arubus.com), consultadas em "
                 "15/nov/2026.<br>"
                 "Viagem simples: <b>AWG 4.50 ou $2.60</b>. Ida e volta: AWG 8.75 ou $5.00. "
                 "<b>Passe do dia: AWG 26.25 ou $15.00</b> — muito material ainda diz US$ 10.<br>"
                 "<i>“You can pay cash on our buses.”</i> A <b>Linha 2 vai ao aeroporto</b>."),
                ("O táxi, com tabela nova",
                 "O governo publica a tabela em <b>taxi.aw</b>: <i>“The tariffs took effect on "
                 "May 20, 2026.”</i> Corrida mínima de US$ 10; a tarifa cobre de 1 a 4 "
                 "passageiros; US$ 5 a mais aos domingos, feriados, à noite e de 24/dez a "
                 "1º/jan; <b>US$ 3 por mala extra</b>.<br>"
                 "Do aeroporto, pela autoridade de turismo, sem sobretaxas: <b>Oranjestad "
                 "$26</b>, Eagle Beach $37, hotéis altos de Palm Beach <b>$40 e $41</b>.<br>"
                 + FLAG % "Fontes divergem" + "a mesma página da autoridade de turismo ainda "
                 "cobra a mala extra a US$ 2; o taxi.aw, que é do governo, diz US$ 3."),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem, e o que vem por cima",
            "tag": "Conta, não lugar",
            "preco_val": "US$ 408,99",
            "preco_nota": "diária média de 2025; mais 12,5% e US$ 3 por noite",
            "campos": [
                ("A diária",
                 "Fonte: <b>Banco Central de Aruba</b>, <i>State of the Economy 2025 "
                 "Retrospective</i>, Tabela 1, consultado em 15/nov/2026: <i>“the ADR for "
                 "hotels, which climbed from US$ 364.28 in 2024 to US$ 408.99 in 2025.”</i> "
                 "<b>12,3% de alta em um ano</b>, com ocupação de 76,4%. O banco atribui parte "
                 "da alta aos hotéis de alto padrão abertos em 2025.<br>"
                 + LACUNA + "se a média inclui pacotes all-inclusive, e os meses de 2026."),
                ("O que vem por cima da diária",
                 "<b>Imposto de hospedagem: 12,5%</b> do valor pago pelo quarto — "
                 "<i>“12,5 percent van de vergoeding”</i>, art. 5 da lei (Landsverordening "
                 "toeristenheffing). No all-inclusive, a base é metade do pacote, com mínimo de "
                 "Afl. 178,52 por dia.<br>"
                 "<b>Taxa ambiental: Afl. 5,37 (US$ 3) por noite, por quarto ocupado</b>, "
                 "quantas pessoas forem (impuesto.aw).<br>"
                 + FLAG % "Não somado" + "a taxa de serviço é de cada hotel, e não há fonte "
                 "oficial dizendo que os 7% de impostos sobre faturamento aparecem na sua "
                 "conta. Não somamos."),
                ("O brasileiro em Aruba",
                 "O mesmo relatório põe o Brasil entre os mercados que mais cresceram em 2025: "
                 "<i>“Brazil (+11,402 visitors; +65.7%)”</i>."),
            ],
        },
    ],
}

DESTINOS = [ARUBA]
