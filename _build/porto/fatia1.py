# -*- coding: utf-8 -*-
"""Apuracao do Porto - PRIMEIRA FATIA, os cinco pontos centrais.

Pedido do Allan: "Pode fatiar, faz a apuracao dos cinco centrais."

Os cinco desta fatia, e por que sao estes:

    Livraria Lello        o ponto mais buscado da cidade, e o de tarifa
                          mais mal explicada em portugues do Brasil
    Torre dos Clerigos    o cartao-postal, e a fonte que desmente o
                          numero que circula nos agregadores
    Palacio da Bolsa      visita guiada obrigatoria, o que muda o
                          planejamento do dia
    Igreja e Museu de
    Sao Francisco         o caso em que a fonte oficial NAO publica preco
    Metro do Porto        a linha que atravessa todas as outras, porque
                          define como se circula

Falta apurar, e esta escrito de proposito: Se do Porto, Ponte Dom Luis I,
Ribeira, Mercado do Bolhao, Casa da Musica, Serralves, Palacio de
Cristal, Caves de Gaia, Teleferico de Gaia, Capela das Almas, Estacao de
Sao Bento. Essa e a segunda fatia.

O QUE ESTA APURACAO ACHOU, E QUE NAO ESTAVA EM LUGAR NENHUM
-----------------------------------------------------------

1. A Torre dos Clerigos NAO custa 6 EUR. O resumo de busca que
   aparece primeiro diz isso. A bilheteira oficial diz 10,00 EUR
   pelo pack Torre + Museu, que e o unico bilhete diurno que existe.
   Esse foi o unico numero desta fatia em que fonte oficial e resumo
   de busca discordaram - e o resumo estava errado em 40%.

2. O bilhete da Livraria Lello e DEDUTIVEL num livro. Quem compra uma
   edicao da casa paga 15,95 EUR pelo livro e a entrada sai de graca.
   Nenhum guia em portugues do Brasil explica isso, e e a diferenca
   entre "caro para entrar numa livraria" e "livro com visita inclusa".

3. O Palacio da Bolsa so se visita com guia, em visita de cerca de 30
   minutos, e o idioma e definido por ordem de chegada. Isso nao e
   detalhe de conforto: e o que impede encaixar o Palacio num intervalo
   curto do roteiro.

4. Sao Francisco publica horario e NAO publica preco. Nao ha bilheteira
   online, nao ha tabela no site, e o unico valor que circula vem de
   agregador. Fica como lacuna declarada, nao como numero chutado.

5. O combinado Clerigos + Palacio da Bolsa + MMIPO custa 25,00 EUR.
   Os dois primeiros, separados, dao 24,00 EUR. Ou seja: o terceiro
   museu entra por 1,00 EUR. E a melhor conta desta fatia.

Apuracao de 24 de setembro de 2026.
"""

APURACAO = "24 de setembro de 2026"
APURACAO_CURTA = "24/set/2026"


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
#  PORTO - fatia 1 de 2
# =====================================================================
PORTO = {
    "slug": "porto",
    "nome": "Porto",
    "pais": "Portugal",
    "regiao": "europa",
    "titulo": "Porto: preço e horário verificados na fonte oficial",
    "descricao": ("Preço, horário e fonte de cinco pontos centrais do Porto — com a "
                  "entrada da Livraria Lello que volta como crédito em livro, o valor "
                  "real da Torre dos Clérigos e o combinado que soma três museus."),
    "abertura": ("Cinco pontos centrais com preço, horário e fonte conferidos em 24 de "
                 "setembro de 2026 — e o detalhe que muda a conta: <b>os € 15,95 da "
                 "Livraria Lello voltam como crédito num livro da casa</b>."),
    "busca": ("porto portugal douro ribeira livraria lello torre dos clerigos palacio da bolsa "
              "igreja de sao francisco metro do porto andante cartao porto ponte dom luis "
              "carmelitas ferreira borges infante dom henrique sao filipe de nery "
              "talha dourada barroco patrimonio mundial unesco andante tour andante azul"),
    "grupos": [
        {"id": "g1", "titulo": "A livraria e a torre",
         "intro": ("Os dois pontos mais procurados do Porto ficam a duzentos metros um do "
                   "outro, e os dois têm tarifa que os agregadores contam errado.")},
        {"id": "g2", "titulo": "Barroco e comércio",
         "intro": ("Dois monumentos vizinhos na baixa, com regras de visita opostas: um só "
                   "abre com guia, o outro não publica preço.")},
        {"id": "g3", "titulo": "Como circular",
         "intro": ("O Porto se caminha, mas o aeroporto não. O Andante é o mesmo bilhete "
                   "para metro, ônibus e trem urbano.")},
    ],
    "pontos": [
        # -------------------------------------------------------------
        {
            "id": "livraria-lello", "grupo": "g1",
            "foto": {"arq": "porto/livraria-lello.webp",
                     "alt": "Teto de madeira entalhada da Livraria Lello visto de baixo, com a galeria do piso superior e o vitral ao fundo",
                     "cred": "John Samuel · CC BY-SA 4.0 · via Wikimedia Commons"},
            "nome": "Livraria Lello", "tag": "Livraria histórica",
            "preco_val": "€ 15,95",
            "preco_nota": "dedutível num livro da casa",
            "campos": [
                ("Valor da entrada",
                 "Fonte: loja oficial de bilhetes da própria livraria "
                 "(tickets.livrarialello.pt), consultada em 24/set/2026.<br>"
                 "<b>Ticket-Voucher Livraria Lello: € 15,95</b>, visita livre.<br>"
                 "<b>O valor é dedutível num livro Edições Livraria Lello</b> — é a "
                 "informação que muda a conta e que quase nenhum guia traz. Quem compra "
                 "uma edição da casa usa os € 15,95 como crédito, e a entrada sai de "
                 "graça. Quem não compra nada paga os € 15,95 e pronto.<br>"
                 "<b>Não é ingresso comum, é voucher</b> — a própria loja chama assim."),
                ("As outras quatro tarifas, e o que cada uma inclui",
                 "Mesma fonte, mesma data. A loja oficial vende cinco produtos "
                 "diferentes, e três deles <b>não</b> são a visita padrão:<br>"
                 "<b>Combinado Livraria Lello + Fundação Livraria Lello: desde € 29,95</b>, "
                 "com entrada prioritária. A Fundação fica no <b>Mosteiro de Leça do "
                 "Balio</b>, fora do centro, e abre de quarta a domingo, das 10h às "
                 "18h30. Inclui empréstimo de um de dois livros, devolvidos no fim.<br>"
                 "<b>Ticket-Voucher Gema: € 100,00</b>, visita guiada à Sala Gema — "
                 "coleção pessoal de Amy Winehouse e uma primeira edição de <i>The "
                 "Picture of Dorian Gray</i> assinada por Oscar Wilde. Valor dedutível "
                 "em edições especiais.<br>"
                 "<b>Ticket-Voucher Ai Weiwei: € 8,00</b> — e atenção: <b>não inclui "
                 "acesso ao edifício histórico da livraria</b>. É só a exposição A4. "
                 "Quem comprar este achando que é a entrada barata não entra na "
                 "livraria.<br>"
                 "<b>Ticket-Voucher Porto.: € 15,95</b>, com entrada prioritária, "
                 "<b>exclusivo para residentes do município do Porto</b>."),
                ("Horário",
                 "Fonte: rodapé da loja oficial, consultado em 24/set/2026.<br>"
                 "<b>Todos os dias, das 9h às 19h30.</b>"),
                ("Endereço",
                 "Rua das Carmelitas, 144 — 4050-161 Porto. "
                 "Fonte: loja oficial, 24/set/2026."),
                ("Onde fica", mapa("Livraria Lello, Rua das Carmelitas 144, Porto, Portugal")),
            ],
        },
        # -------------------------------------------------------------
        {
            "id": "torre-dos-clerigos", "grupo": "g1",
            "foto": {"arq": "porto/torre-dos-clerigos.webp",
                     "alt": "A Torre dos Clérigos erguida acima dos telhados de telha vermelha do centro do Porto, contra o céu limpo",
                     "cred": "Krzysztof Golik · CC BY-SA 4.0 · via Wikimedia Commons"},
            "nome": "Torre dos Clérigos", "tag": "Torre e museu",
            "preco_val": "€ 10,00",
            "preco_nota": "pack Torre + Museu; € 7,00 estudante",
            "campos": [
                ("Valor da entrada",
                 "Fonte: bilheteira oficial da Irmandade dos Clérigos "
                 "(torredosclerigos.pt/bilheteira), consultada em 24/set/2026.<br>"
                 "<b>Bilhete Diurno, 9h–19h, pack Torre + Museu: € 10,00 geral</b> e "
                 "<b>€ 7,00 estudantes</b>, com apresentação de identificação.<br>"
                 "<b>Crianças até 10 anos não pagam.</b><br>"
                 "<span class=\"flag\">O número que circula está errado</span> "
                 "agregadores e resumos de busca dão a entrada como <b>€ 6</b>. A "
                 "bilheteira oficial não tem nenhum bilhete diurno nesse valor: o pack "
                 "Torre + Museu é o único, e custa € 10,00. Conferido na página oficial "
                 "em 24/set/2026."),
                ("O bilhete noturno, que só existe em três épocas",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Bilhete Noturno, 19h–23h: € 5,00</b>, visita à Torre, crianças até "
                 "10 anos gratuito.<br>"
                 "<b>Só funciona na Páscoa, no verão e na época de Natal</b> — não é "
                 "opção de qualquer dia do ano, e é por isso que ele não entra na conta "
                 "do roteiro."),
                ("Os combinados, e o que compensa",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Clérigos + Palácio da Bolsa + MMIPO: € 25,00</b><br>"
                 "<b>Clérigos + Serralves: € 27,20</b><br>"
                 "<b>Clérigos + SPIRITUS (videomapping): € 19,00</b><br>"
                 "<b>A conta que importa:</b> Clérigos (€ 10,00) mais Palácio da Bolsa "
                 "(€ 14,00) dão <b>€ 24,00</b> comprados à parte. O combinado custa "
                 "€ 25,00 e ainda inclui o <b>MMIPO</b> — ou seja, o terceiro museu "
                 "entra por <b>€ 1,00</b>. É a melhor relação desta apuração."),
                ("Descontos e gratuidades",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Cartão Porto.: 50% de desconto</b> no bilhete diurno, para "
                 "munícipes com domicílio fiscal no Porto.<br>"
                 "<b>Entrada gratuita, com identificação:</b> clero, escuteiros, "
                 "exército, marinha, força aérea, PSP, GNR e antigos combatentes — "
                 "estes devem apresentar-se devidamente uniformizados, com reserva "
                 "prévia obrigatória.<br>"
                 "<b>Incapacidade igual ou superior a 60%: gratuito</b>, e o "
                 "acompanhante paga 50%."),
                ("Horário",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Todos os dias, das 9h às 19h.</b> Na Páscoa, no verão e na época de "
                 "Natal, o mesmo horário.<br>"
                 "<b>Exceções:</b> 24/12 e 31/12, das 9h às 14h; 25/12 e 01/01, das 11h "
                 "às 19h.<br>"
                 "<b>Última entrada sempre 30 minutos antes do encerramento.</b><br>"
                 "Missas: sábados às 17h, em inglês; domingos às 21h30."),
                ("Endereço",
                 "Rua de São Filipe de Nery, 4050-546 Porto. Telefone +351 220 145 489. "
                 "Fonte: site oficial, 24/set/2026."),
                ("Onde fica", mapa("Torre dos Clérigos, Rua de São Filipe de Nery, Porto, Portugal")),
            ],
        },
        # -------------------------------------------------------------
        {
            "id": "palacio-da-bolsa", "grupo": "g2",
            "foto": {"arq": "porto/palacio-da-bolsa.webp",
                     "alt": "Fachada neoclássica do Palácio da Bolsa vista da praça, com o monumento ao Infante Dom Henrique em primeiro plano",
                     "cred": "Alexkom000 · CC BY 4.0 · via Wikimedia Commons"},
            "nome": "Palácio da Bolsa", "tag": "Palácio",
            "preco_val": "€ 14,00",
            "preco_nota": "visita guiada obrigatória, ~30 min",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de turismo do site oficial do Palácio da Bolsa "
                 "(palaciodabolsa.com/turismo), consultada em 24/set/2026.<br>"
                 "<b>Individual: € 14</b><br>"
                 "<b>Estudante, escolas e sénior: € 9,50</b><br>"
                 "<b>Menores de 12 anos acompanhados de adultos não pagam</b> — com uma "
                 "exceção escrita na própria página: <b>grupos de crianças pagam</b>."),
                ("A visita é guiada, e isso muda o planejamento",
                 "Mesma fonte, mesma data.<br>"
                 "<b>A visita é obrigatoriamente guiada e dura cerca de 30 minutos.</b> "
                 "Não existe visita livre.<br>"
                 "<b>O idioma é definido por ordem de chegada</b>, entre português, "
                 "espanhol, francês e inglês. Quem chega e a próxima turma é em francês, "
                 "espera a seguinte.<br>"
                 "Por isso o Palácio não encaixa em intervalo curto: some o tempo de "
                 "espera pela turma no idioma ao tempo da visita."),
                ("Horário",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Visitas das 9h às 18h30.</b><br>"
                 "O expediente administrativo do Palácio é outro horário, das 9h30 às 13h "
                 "e das 14h às 17h30 — não é o horário de visita.<br>"
                 "<span class=\"flag\">Há dias indisponíveis, e eles variam</span> o "
                 "site publica um calendário de datas disponíveis para visita, com dias "
                 "marcados como indisponíveis. <b>Confira o calendário oficial na data "
                 "da sua viagem</b> — o Palácio fecha para eventos, e em 2026 já houve "
                 "um fechamento de 19 a 27 de fevereiro."),
                ("Acessibilidade",
                 "Mesma fonte, mesma data. A página lista: <b>entrada lateral com rampa, "
                 "WC preparado para pessoas com mobilidade reduzida, elevador preparado "
                 "para acomodar cadeiras de rodas e atendimento prioritário.</b><br>"
                 "É a descrição mais detalhada de acessibilidade entre os cinco pontos "
                 "desta fatia."),
                ("Endereço",
                 "Rua Ferreira Borges, 4050-253 Porto. Telefone do turismo "
                 "+351 223 399 013. Fonte: site oficial, 24/set/2026."),
                ("Onde fica", mapa("Palácio da Bolsa, Rua Ferreira Borges, Porto, Portugal")),
            ],
        },
        # -------------------------------------------------------------
        {
            "id": "igreja-sao-francisco", "grupo": "g2",
            "foto": {"arq": "porto/igreja-sao-francisco.webp",
                     "alt": "Fachada da Igreja de São Francisco, com a rosácea gótica sobre o portal barroco em pedra",
                     "cred": "John Samuel · CC BY-SA 4.0 · via Wikimedia Commons"},
            "nome": "Igreja e Museu de São Francisco", "tag": "Monumento Nacional",
            "preco_val": None,
            "preco_nota": "a fonte oficial não publica preço",
            "campos": [
                ("Valor da entrada",
                 "<span class=\"flag\">Não apuramos o preço, e a lacuna é da fonte</span> "
                 "o site oficial da Venerável Ordem Terceira de São Francisco do Porto "
                 "(ordemsaofranciscoporto.pt/igrejas) publica o horário da bilheteira e "
                 "<b>não publica tarifa nenhuma</b>. Conferido em 24/set/2026, incluindo "
                 "a varredura de todos os links da página: <b>não existe bilheteira "
                 "online nem página de preçário</b>.<br>"
                 "Valores que circulam em agregadores de turismo <b>não entram aqui</b> — "
                 "é a mesma regra que fez a Torre dos Clérigos aparecer a € 10,00 e não "
                 "aos € 6 do resumo de busca. <b>Confirme na bilheteira, no local.</b>"),
                ("Horário",
                 "Fonte: site oficial da Venerável Ordem Terceira de São Francisco do "
                 "Porto, consultado em 24/set/2026. Isto a fonte publica, e com "
                 "precisão:<br>"
                 "<b>Horário de verão, entre 1º de abril e 30 de setembro: 9h às 20h</b><br>"
                 "<b>Horário de inverno, entre 1º de outubro e 31 de março: 9h às 19h</b><br>"
                 "<b>Todos os dias</b>, com um único fechamento no ano: "
                 "<b>encerrado em 25 de dezembro</b>."),
                ("O que a visita inclui",
                 "Mesma fonte, mesma data. Não é só a igreja:<br>"
                 "<b>Igreja do Convento de São Francisco</b> — Monumento Nacional desde "
                 "1910, na zona histórica que é património mundial da UNESCO desde 1996. "
                 "Considerada um dos mais ricos repositórios de talha dourada de "
                 "Portugal, com o contraste entre a ornamentação barroca e a sobriedade "
                 "da arquitetura gótica. O <b>retábulo da Árvore de Jessé</b>, de Filipe "
                 "da Silva e António Gomes, século XVIII, é o mais citado.<br>"
                 "<b>Igreja dos Terceiros de São Francisco</b> — construção iniciada em "
                 "1792, classicista.<br>"
                 "<b>Percurso museológico na Casa do Despacho</b>, projeto de Nicolau "
                 "Nasoni: Sala do Tesouro, Sala das Sessões e Sala do Despacho.<br>"
                 "<b>Cemitério catacumbal</b> — entre 1749 e 1866 todos os benfeitores "
                 "da Ordem foram sepultados ali, e nas catacumbas se vê o ossário, com "
                 "milhares de ossos expostos. É a parte que ninguém espera."),
                ("Endereço",
                 "A igreja fica na Rua do Infante Dom Henrique, ao lado do Palácio da "
                 "Bolsa. A sede da Ordem é na Rua da Bolsa, 80 — 4050-116 Porto, "
                 "telefone +351 222 062 100. Fonte: site oficial, 24/set/2026."),
                ("Onde fica", mapa("Igreja de São Francisco, Rua do Infante Dom Henrique, Porto, Portugal")),
            ],
        },
        # -------------------------------------------------------------
        {
            "id": "metro-do-porto", "grupo": "g3",
            "foto": {"arq": "porto/metro-do-porto.webp",
                     "alt": "Composição amarela do Metro do Porto parada na estação, vista da plataforma",
                     "cred": "Barcex · CC BY-SA 3.0 · via Wikimedia Commons"},
            "nome": "Metro do Porto", "tag": "Transporte",
            "preco_val": "€ 1,40",
            "preco_nota": "Andante Azul Z2, mais € 0,60 do cartão",
            "campos": [
                ("Quanto custa cada viagem",
                 "Fonte: página de preços do site oficial do Metro do Porto "
                 "(metrodoporto.pt), consultada em 24/set/2026. A própria página diz "
                 "<b>&#8220;tarifário em vigor a partir do dia 1 de janeiro de "
                 "2026&#8221;</b>, com IVA incluído.<br>"
                 "<b>Andante Azul</b>, cartão recarregável para quem viaja "
                 "ocasionalmente. O preço depende de quantas zonas se cruza:<br>"
                 "<b>Z2 — € 1,40</b> · validade de viagem 1h00<br>"
                 "<b>Z3 — € 1,85</b> · 1h00<br>"
                 "<b>Z4 — € 2,30</b> · 1h15<br>"
                 "<b>Z5 — € 2,80</b> · 1h30<br>"
                 "<b>Z6 — € 3,25</b> · 1h45<br>"
                 "<b>Z7 — € 3,75</b> · 2h00<br>"
                 "<b>Z8 — € 4,20</b> · 2h15<br>"
                 "<b>Z9 — € 4,65</b> · 2h30<br>"
                 "<b>O cartão custa € 0,60 à parte</b> e não está incluído em nenhum "
                 "valor acima.<br>"
                 "<b>Carregando 10 títulos iguais, o 11º é grátis</b> — Z2 sai a € 14,00 "
                 "as onze viagens. Dá para carregar de 1 a 30 viagens do mesmo tipo.<br>"
                 "A validade não é por viagem, é por tempo: <b>depois da primeira "
                 "validação, e durante o período da tabela, pode validar quantas vezes "
                 "precisar.</b>"),
                ("Os títulos de turista, que costumam sair mais barato",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Andante Tour 1: € 7,75</b> — válido 24 horas consecutivas após a "
                 "primeira validação.<br>"
                 "<b>Andante Tour 3: € 16,55</b> — válido 72 horas consecutivas.<br>"
                 "A vantagem não é só o preço: o Andante Tour <b>circula sem limites por "
                 "toda a rede Andante</b>, sem contar zonas. É cartão de papel, não "
                 "personalizado e <b>não recarregável</b>.<br>"
                 "<b>Andante 24</b>, a alternativa por zonas, viaja 24 horas "
                 "consecutivas nas zonas compradas: <b>Z2 € 5,35</b>, Z3 € 6,85, "
                 "<b>Z4 € 8,55</b>, Z5 € 10,25, Z6 € 12,20, Z7 € 13,90, Z8 € 15,60, "
                 "Z9 € 17,30. Cartão € 0,60 à parte, recarregável com qualquer título "
                 "ocasional.<br>"
                 "<b>A conta:</b> o Andante Tour 3 a € 16,55 equivale a pouco menos de "
                 "doze viagens Z2 soltas, e cobre a rede inteira por três dias."),
                ("Quantas zonas eu preciso — e por que não respondemos",
                 "<span class=\"flag\">Não apuramos o zonamento, e a fonte oficial está "
                 "quebrada</span> o Metro do Porto publica, na própria página de preços, "
                 "um link para descobrir de quantas zonas você precisa. Em 24/set/2026 "
                 "esse link <b>devolve erro 404 no próprio site do Metro</b> "
                 "(metrodoporto.pt/pages/289). O mapa de zonamento existe em PDF, mas é "
                 "<b>imagem sem texto</b>, e o site linhandante.com não respondeu.<br>"
                 "<b>Por isso não afirmamos aqui em que zona está o aeroporto.</b> É um "
                 "número que circula em todo guia e que não conseguimos confirmar na "
                 "fonte.<br>"
                 "<b>O contorno prático:</b> o <b>Andante Tour</b> não usa zonas — vale "
                 "para a rede toda, aeroporto incluído. Quem não quer resolver conta de "
                 "zona compra o Tour 1 ou o Tour 3 e pronto. Na estação há <b>Lista de "
                 "Destinos</b> afixada, que diz a zona de cada parada."),
                ("O passe mensal, para quem fica muito tempo",
                 "Mesma fonte, mesma data. Os <b>Passes Andante</b> são assinatura "
                 "mensal, em cartão personalizado com nome e fotografia, válidos num "
                 "conjunto de zonas escolhido. <b>O cartão custa € 6,00.</b><br>"
                 "<span class=\"flag\">A tabela do passe não está na mesma data</span> a "
                 "página informa que os valores do passe estão <b>em vigor a partir de "
                 "1º de janeiro de 2024</b>, enquanto os títulos ocasionais são de "
                 "<b>1º de janeiro de 2026</b>. <b>Não copiamos os valores do passe</b> "
                 "por causa dessa diferença de dois anos na vigência."),
                ("Onde fica", mapa("Estação Trindade, Metro do Porto, Porto, Portugal")),
            ],
        },
    ],
}

DESTINOS = [PORTO]
