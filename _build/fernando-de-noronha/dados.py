# -*- coding: utf-8 -*-
"""Fernando de Noronha: o vigesimo quarto destino, em nove pontos e tres grupos.

Mesmo molde do foz-do-iguacu/dados.py.

O ACHADO PRINCIPAL: A TPA BARATEIA ATE O 10o DIA E DISPARA NO 11o
------------------------------------------------------------------
A tabela oficial da Taxa de Preservacao Ambiental de 2026 (noronha.pe.gov.br,
lida em 29/10/2026) cobra R$ 105,79 por um dia e R$ 901,36 por dez - R$ 90,14
por dia. O 11o dia leva o total a R$ 1.028,31: so ele custa R$ 126,95, mais
que o primeiro. Trinta dias: R$ 7.460,56. E o dia excedente nao agendado e
cobrado em dobro (Lei 11.704, art. 86).

O SEGUNDO: DUAS COBRANCAS ANTES DE QUALQUER PASSEIO
--------------------------------------------------------------------------
TPA (Distrito, estadual) e ingresso do Parque Nacional Marinho (ICMBio,
federal) sao coisas diferentes. Cinco dias: R$ 520,50 + R$ 192,00 =
R$ 712,50 por pessoa so para estar na ilha e entrar no Parque.

O TERCEIRO: O INGRESSO DO PARQUE MUDA EM 1o DE NOVEMBRO
--------------------------------------------------------------------------
A pagina do ICMBio diz R$ 192 (Portaria 4.423/2025). A imprensa (Brasilturis,
27/10/2026), citando o ICMBio, da R$ 196,50 a partir de 1/11/2026. A ficha
usa o da pagina oficial e diz o outro.

O QUE FICOU SEM RESPOSTA, E ESTA DITO EM CADA FICHA
--------------------------------------------------------------------------
    hospedagem     nenhum orgao publica diaria media de Noronha
    contagem da    a pagina da TPA nao diz se chegada e saida contam como
    TPA            dias; a ficha usa 5 dias para 4 noites, o maior
    onibus         sem tarifa em fonte oficial; guias citam R$ 5
    condutor e     o servico e privado e nao tem tabela publicada pelo
    barco          ICMBio

Fontes guardadas em _build/fernando-de-noronha/fontes/. Apuracao de 29 de
outubro de 2026.
"""

APURACAO = "29 de outubro de 2026"
APURACAO_CURTA = "29/out/2026"

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


NORONHA = {
    "slug": "fernando-de-noronha",
    "nome": "Fernando de Noronha",
    "pais": "Brasil",
    "regiao": "brasil",
    "titulo": "Fernando de Noronha: 9 pontos com preço e horário verificados",
    "descricao": ("Preço, horário e fonte de 9 pontos de Fernando de Noronha, com a taxa "
                  "ambiental que barateia até o 10º dia e dispara no 11º, e as duas "
                  "cobranças que vêm antes de qualquer passeio."),
    "abertura": ("Nove pontos de Fernando de Noronha com preço, horário e fonte conferidos "
                 "em 29 de outubro de 2026 — e duas coisas que os guias não dizem: <b>a "
                 "Taxa de Preservação Ambiental fica mais barata por dia até o 10º dia e "
                 "dispara no 11º</b>, que sozinho custa R$ 126,95, mais que o primeiro. "
                 "<b>E há duas cobranças antes de qualquer passeio</b>: em cinco dias, "
                 "R$ 520,50 de taxa e R$ 192 de ingresso do Parque — R$ 712,50 por pessoa "
                 "só para estar na ilha."),
    "busca": ("fernando de noronha noronha pernambuco pe brasil tpa taxa de preservacao "
              "ambiental parque nacional marinho icmbio baia do sancho baia dos porcos "
              "baia dos golfinhos praia do leao sueste atalaia capim acu cacimba do padre "
              "mergulho"),
    "grupos": [
        {"id": "g1", "titulo": "As duas cobranças de quem chega",
         "intro": ("Uma é do Distrito, por dia de permanência; a outra é do ICMBio, por dez "
                   "dias de Parque. São coisas diferentes, e as duas vêm antes de qualquer "
                   "praia paga.")},
        {"id": "g2", "titulo": "O Parque: o que o ingresso abre",
         "intro": ("O Sancho com a escada de horário marcado, o Leão e o Sueste, onde o "
                   "banho está proibido, e as trilhas de piscina natural que só abrem com "
                   "agendamento e maré baixa.")},
        {"id": "g3", "titulo": "O que não cobra, o transporte e a cama",
         "intro": ("Oito praias de acesso livre, o ônibus e o barco sem tabela oficial, e a "
                   "hospedagem sem diária publicada.")},
    ],
    "pontos": [
        # =============================================================
        #  g1 - as duas cobrancas
        # =============================================================
        {
            "id": "tpa",
            "grupo": "g1",
            "nome": "Taxa de Preservação Ambiental (TPA)",
            "tag": "Taxa",
            "preco_val": "R$ 105,79",
            "preco_nota": "o 1º dia; 5 dias R$ 520,50; o 11º dia custa R$ 126,95",
            "campos": [
                ("A tabela, e onde ela vira",
                 "Fonte: <b>Administração do Distrito Estadual de Fernando de Noronha</b>, "
                 "portal oficial (noronha.pe.gov.br), tabela de permanência da TPA 2026, "
                 "consultada em 29/out/2026.<br>"
                 "<b>1 dia: R$ 105,79 · 3 dias: R$ 317,38 · 5 dias: R$ 520,50 · 7 dias: "
                 "R$ 672,85 · 10 dias: R$ 901,36.</b> Até aqui, cada dia a mais custa menos: "
                 "dez dias saem a R$ 90,14 por dia.<br>"
                 "<b>No 11º dia a conta vira</b>: R$ 1.028,31 — só esse dia custa R$ 126,95, "
                 "mais que o primeiro. Quinze dias: R$ 1.747,71. Trinta: R$ 7.460,56.<br>"
                 "<b>Ficar além do previsto sai em dobro</b>: <i>“O valor da Taxa de "
                 "Preservação Ambiental que se referir aos dias excedentes ao período "
                 "inicialmente previsto, será cobrado em dobro”</i>, quando a permanência "
                 "não foi agendada e autorizada (Lei 11.704, art. 86)."),
                ("Como pagar",
                 "Pela internet antes do embarque, com cartão de crédito ou boleto, ou no "
                 "desembarque. <b>Cartão emitido fora do Brasil só paga no balcão do "
                 "aeroporto da ilha.</b> A cobrança é individual e vale para todo "
                 "visitante não residente."),
                ("O que a página não diz",
                 FLAG % "Lacuna declarada" +
                 "<b>a tabela fala em “dias de permanência” e não diz se o dia da "
                 "chegada e o da partida contam.</b> Uma viagem de 4 noites pode ser cobrada "
                 "como 4 dias (R$ 423,17) ou como 5 (R$ 520,50). A ficha de custos usa 5, o "
                 "maior. Na hora de pagar, o site pede as datas e calcula."),
            ],
        },
        {
            "id": "ingresso-do-parque",
            "foto": {"arq": "fernando-de-noronha/ingresso-do-parque.webp",
                     "alt": "O Morro Dois Irmãos e a Baía dos Porcos, com a água verde-azulada entre as pedras",
                     "cred": "Elder Virginio · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g1",
            "nome": "Ingresso do Parque Nacional Marinho",
            "tag": "Ingresso",
            "preco_val": "R$ 192",
            "preco_nota": "brasileiro, vale 10 dias; R$ 196,50 a partir de 1º/nov",
            "campos": [
                ("Valor e validade",
                 "Fonte: <b>ICMBio</b>, página de visitação do Parque "
                 "(parnanoronha.com.br/visitante), consultada em 29/out/2026, conforme a "
                 "Portaria ICMBio nº 4.423, de 14/10/2025.<br>"
                 "<b>Público geral: R$ 384,00. Brasileiro: R$ 192,00</b>, 50% de desconto. "
                 "<b>Vale 10 dias.</b><br>"
                 + FLAG % "Muda em 1º de novembro" +
                 "<b>a imprensa, citando o ICMBio, dá R$ 196,50 para brasileiro e R$ 393 "
                 "para estrangeiro a partir de 1º/11/2026</b> (Brasilturis, 27/out/2026). "
                 "Em 29 de outubro a página oficial ainda dizia R$ 192."),
                ("Quem não paga",
                 "<b>Menor de 12 anos e brasileiro acima de 60</b>, com documento. Também "
                 "morador regularizado da ilha e parentes de 1º grau."),
                ("O que o ingresso abre, e onde comprar",
                 "<b>Sancho, Baía dos Porcos, Baía dos Golfinhos, Leão, Sueste</b>, Ponta "
                 "das Caracas, Forte do Sueste, Caieira, as trilhas agendadas e os pontos "
                 "de mergulho. O Parque é 70% do arquipélago.<br>"
                 "Compra online, com QR Code, ou na bilheteria do <b>Centro de Visitantes, "
                 "no Boldró, das 8h às 19h</b>."),
                ("Onde fica",
                 mapa("Centro de Visitantes ICMBio, Boldró, Fernando de Noronha, PE")),
            ],
        },
        # =============================================================
        #  g2 - o Parque
        # =============================================================
        {
            "id": "baia-do-sancho",
            "foto": {"arq": "fernando-de-noronha/baia-do-sancho.webp",
                     "alt": "A Baía do Sancho vista do alto, com a faixa de areia e o mar azul-turquesa",
                     "cred": "Osaki · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Baía do Sancho, dos Golfinhos e dos Porcos",
            "tag": "Praia do Parque",
            "preco_val": "no ingresso",
            "preco_nota": "a escada do Sancho tem horário de descer e de subir",
            "campos": [
                ("A escada de horário marcado",
                 "Fonte: <b>ICMBio</b>, página de atrativos do Parque, consultada em "
                 "29/out/2026.<br>"
                 "<b>Sancho: 8h às 18h.</b> A praia se alcança por uma escada de marinheiro "
                 "com <b>intervalos para descer e para subir</b>: livre das 8h às 8h50; "
                 "descida 9h–10h20; subida 10h30–11h20; descida 11h30–12h20; subida "
                 "12h30–13h20; descida 13h30–14h20; subida 14h30–15h20; descida "
                 "15h30–16h20; livre 16h30–17h20; só subida 17h30–18h.<br>"
                 "<b>De manhã pode haver fila longa</b>; à tarde o movimento costuma ser "
                 "menor, diz a página."),
                ("Os golfinhos, só de cima",
                 "<b>Baía dos Golfinhos: 6h30 às 18h30</b>, mirante. Os golfinhos rotadores "
                 "descansam ali, principalmente no início da manhã — e por isso <b>não é "
                 "permitido descer, nadar nem passar de barco</b> na baía."),
                ("A Baía dos Porcos",
                 "O acesso é por uma trilha no canto esquerdo da <b>Cacimba do Padre</b>, "
                 "que é de acesso livre. A baía é do Parque: o ingresso é conferido."),
                ("Onde fica",
                 mapa("Baía do Sancho, Fernando de Noronha, PE")),
            ],
        },
        {
            "id": "praia-do-leao",
            "foto": {"arq": "fernando-de-noronha/praia-do-leao.webp",
                     "alt": "A Praia do Leão com as ondas quebrando e o morro ao fundo",
                     "cred": "Rafa Tecchio · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Praia do Leão e Ponta das Caracas",
            "tag": "Praia do Parque",
            "preco_val": "no ingresso",
            "preco_nota": "desova de tartaruga de dezembro a maio; correntes fortes",
            "campos": [
                ("O Leão",
                 "Fonte: ICMBio, página de atrativos, consultada em 29/out/2026.<br>"
                 "<b>Praia do Leão: 8h às 18h.</b> É o principal ponto de desova da "
                 "tartaruga-verde, <b>de dezembro a maio</b>. A página avisa: <i>“Esta praia "
                 "está sujeita a fortes correntes marítimas.”</i> Não se caminha sobre os "
                 "recifes nem se sobe nas ilhas da frente."),
                ("A Ponta das Caracas",
                 "<b>Mirante da Ponta das Caracas: 8h às 18h</b>, entre o Leão e o Sueste, "
                 "pelo mesmo portão — a página o indica para ver aves marinhas e o pôr do "
                 "sol."),
                ("Onde fica",
                 mapa("Praia do Leão, Fernando de Noronha, PE")),
            ],
        },
        {
            "id": "baia-do-sueste",
            "foto": {"arq": "fernando-de-noronha/baia-do-sueste.webp",
                     "alt": "A estrada que desce para a Baía do Sueste, entre a mata, com o mar ao fundo",
                     "cred": "MTur Destinos · domínio público · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "Baía do Sueste",
            "tag": "Praia do Parque",
            "preco_val": "no ingresso",
            "preco_nota": "o banho está proibido",
            "campos": [
                ("Só para olhar",
                 "Fonte: ICMBio, página de atrativos, consultada em 29/out/2026.<br>"
                 "<b>Faixa de areia das 9h às 16h</b>; o posto de controle, até 17h.<br>"
                 "<b>“Atualmente, não é permitido banho na praia do Sueste.”</b> É "
                 "obrigatório assistir a um vídeo ou palestra antes de entrar. O Sueste "
                 "guarda o único mangue em ilhas oceânicas do Atlântico Sul, e o mangue não "
                 "é aberto à visita."),
                ("Onde fica",
                 mapa("Baía do Sueste, Fernando de Noronha, PE")),
            ],
        },
        {
            "id": "trilhas-agendadas",
            "foto": {"arq": "fernando-de-noronha/trilhas-agendadas.webp",
                     "alt": "A Praia da Atalaia, com o morro verde e o mar batendo nas pedras",
                     "cred": "Elder Virginio · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g2",
            "nome": "As trilhas de piscina natural",
            "tag": "Trilha agendada",
            "preco_val": "no ingresso",
            "preco_nota": "agendamento e maré baixa; 4 delas exigem condutor pago",
            "campos": [
                ("Por que agendar",
                 "Fonte: ICMBio, páginas de visitação e de atrativos, consultadas em "
                 "29/out/2026.<br>"
                 "As piscinas naturais têm <b>vagas por dia</b>, e o horário segue a <b>maré "
                 "baixa</b>, que dura em média 4 horas. <b>Sem o número do ingresso não se "
                 "agenda.</b> Exigem agendamento: Atalaia, Capim-Açu, Enseada do Abreu, "
                 "Pontinha–Caieira, Atalaia–Pontinha–Caieira e Morro São José."),
                ("Atalaia: a que dispensa condutor",
                 "<b>3 km ida e volta</b>, cerca de 30 minutos para cada lado, dificuldade "
                 "média. <b>Colete, máscara e snorkel obrigatórios</b>, e não se pode ficar "
                 "em pé na piscina. <b>Protetor solar é proibido antes do banho.</b>"),
                ("As que exigem condutor",
                 "<b>Capim-Açu</b> (7,5 km, a mais longa), <b>Pontinha–Caieira</b>, "
                 "<b>Atalaia–Pontinha–Caieira</b> e o <b>Morro São José a nado</b> só com "
                 "condutor credenciado pelo ICMBio. No Capim-Açu, o trecho até o farol se "
                 "faz sem condutor.<br>"
                 + FLAG % "Lacuna declarada" +
                 "<b>o condutor é contratado à parte, e o ICMBio não publica o preço.</b> "
                 "A página indica a associação de condutores (ACITUR FN), com estande no "
                 "Centro de Visitantes."),
                ("Onde fica",
                 mapa("Praia da Atalaia, Fernando de Noronha, PE")),
            ],
        },
        # =============================================================
        #  g3 - o gratis, o transporte e a cama
        # =============================================================
        {
            "id": "praias-da-apa",
            "foto": {"arq": "fernando-de-noronha/praias-da-apa.webp",
                     "alt": "A Cacimba do Padre no fim da tarde, com surfistas na areia e as ondas ao fundo",
                     "cred": "Firedrop Marendo Müller · CC BY-SA 3.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "As praias de acesso livre",
            "tag": "Gratuito",
            "preco_val": "Grátis",
            "preco_nota": "fora do Parque; a TPA continua valendo",
            "campos": [
                ("A lista oficial",
                 "Fonte: <b>ICMBio</b>, página de visitação, consultada em 29/out/2026: "
                 "<i>“Não é necessário comprar o ingresso para acessar”</i>:<br>"
                 "<b>Cacimba do Padre, Praia do Bode, Praia do Americano, Praia do Boldró, "
                 "Praia da Conceição, Praia do Meio, Praia do Cachorro e Porto de Santo "
                 "Antônio.</b><br>"
                 "Ficam na Área de Proteção Ambiental, fora do Parque. <b>Não cobram "
                 "ingresso — mas a TPA vale para todo dia na ilha</b>, em qualquer praia."),
                ("Onde fica",
                 mapa("Cacimba do Padre, Fernando de Noronha, PE")),
            ],
        },
        {
            "id": "transporte",
            "foto": {"arq": "fernando-de-noronha/transporte.webp",
                     "alt": "O Porto de Santo Antônio visto do alto, com barcos ancorados na baía",
                     "cred": "Adelano Lázaro · CC BY-SA 4.0 · via Wikimedia Commons · recortada"},
            "grupo": "g3",
            "nome": "Ônibus, barco e mergulho",
            "tag": "Transporte",
            "preco_val": "sem tabela oficial",
            "preco_nota": "nenhum dos três tem preço em fonte oficial",
            "campos": [
                ("O ônibus",
                 FLAG % "Só em fonte secundária" +
                 "<b>não achamos tarifa do ônibus em página da Administração.</b> Guias de "
                 "viagem citam R$ 5, pagos ao motorista, e uma linha que vai do Porto ao "
                 "Sueste — o mais recente que vimos é de 2024. Não entra na conta."),
                ("O passeio de barco e o mergulho",
                 "Só <b>empresas autorizadas pelo Parque</b> fazem o passeio de barco e o "
                 "mergulho autônomo, e <b>o ingresso do Parque é conferido no quiosque do "
                 "Porto de Santo Antônio</b>. No Sancho, só 4 barcos param ao mesmo tempo, "
                 "diz o ICMBio.<br>"
                 + FLAG % "Lacuna declarada" +
                 "<b>o preço é de cada empresa, e não há tabela oficial.</b> Fora da conta."),
                ("Onde fica",
                 mapa("Porto de Santo Antônio, Fernando de Noronha, PE")),
            ],
        },
        {
            "id": "hospedagem",
            "grupo": "g3",
            "nome": "Hospedagem",
            "tag": "Conta, não lugar",
            "preco_val": "sem dado oficial",
            "preco_nota": "nenhum órgão publica a diária",
            "campos": [
                ("Por que não há diária nesta ficha",
                 FLAG % "Lacuna declarada" +
                 "<b>Nenhum órgão publica a diária média de Fernando de Noronha.</b> O "
                 "Panorama da Hotelaria Brasileira (FOHB/HotelInvest) não traz a ilha, e a "
                 "Administração do Distrito publica a TPA, não o preço das pousadas.<br>"
                 "<b>A regra desta casa é não estimar.</b> A ficha de custos mostra o total "
                 "sem a hospedagem, e diz isso no rótulo — como em Foz do Iguaçu e "
                 "Gramado."),
            ],
        },
    ],
}

DESTINOS = [NORONHA]
