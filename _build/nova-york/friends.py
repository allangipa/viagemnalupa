# -*- coding: utf-8 -*-
"""Acrescenta o grupo de Friends a ficha de Nova York.

O pedido
--------
"Adicionar tambem na parte de nova york uma parte especial dedicada aos
fans da serie friends."

O que a apuracao mostrou, e que e o proprio assunto
---------------------------------------------------
Quase nada de Friends foi filmado em Nova York. O apartamento da Monica,
o dos rapazes e o Central Perk eram cenarios nos estudios da Warner Bros
em Burbank, California. O que existe na cidade e:

  1. a fachada que aparece na vinheta - um predio real, em que ninguem
     entra;
  2. uma cafeteria licenciada que abriu em Times Square, decada e meia
     depois do fim da serie;
  3. uma exposicao paga, tambem licenciada, com reconstituicao dos
     cenarios.

Nenhum dos tres e "onde Friends foi gravado". Dizer isso na cara e mais
util ao fa do que vender peregrinacao a cenario que nao existe - e e o
mesmo criterio que o site aplica a preco.

Uso
---
    python _build/nova-york/friends.py
    python _build/nova-york/friends.py --aplica
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ALVO = os.path.join(RAIZ, "destinos", "nova-york", "index.html")
MARCA = "<!-- grupo:friends -->"


def mapa(consulta, rotulo):
    import urllib.parse
    q = urllib.parse.quote(consulta)
    return ('<a class="mapa" href="https://www.google.com/maps/search/?api=1&query=%s"'
            ' target="_blank" rel="noopener" aria-label="Abrir %s no Google Maps">'
            '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
            '<path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z" stroke="currentColor"'
            ' stroke-width="1.8" stroke-linejoin="round"></path><circle cx="12" cy="10" r="2.5"'
            ' stroke="currentColor" stroke-width="1.8"></circle></svg><span>Ver no mapa</span></a>'
            % (q, rotulo))


def campo(rot, val):
    return ('<div class="campo-l"><div class="rot">%s</div>'
            '<div class="val">%s</div></div>' % (rot, val))


def ponto(pid, num, nome, tag, preco, nota, visiveis, fundo):
    return (
        '<article class="ponto" id="%s">'
        '<div class="ponto-topo"><div class="ponto-id"><span class="num">%02d</span>'
        '<div><h3>%s</h3><span class="tag">%s</span></div></div>'
        '<div class="preco"><span class="preco-val">%s</span>'
        '<span class="preco-nota">%s</span></div></div>'
        '<div class="campos">%s'
        '<details class="fundo"><summary>Curiosidades, história e visitação '
        '<span class="conta">%d campos</span></summary>%s</details>'
        '</div></article>'
        % (pid, num, nome, tag, preco, nota,
           "".join(campo(r, v) for r, v in visiveis),
           len(fundo), "".join(campo(r, v) for r, v in fundo)))


# ----------------------------------------------------------------- 18
BEDFORD = ponto(
    "friends-predio", 18, "90 Bedford Street, o prédio de Friends", "Fachada",
    "Grátis", "só por fora — é prédio residencial",
    [("Valor da entrada",
      "<b>Não se paga, e não se entra.</b> Consultado em 17/set/2026.<br>"
      "É um <b>prédio residencial particular</b>. A fachada é o que aparece "
      "na vinheta e nas externas da série; o térreo abriga um restaurante, "
      "que não tem relação com Friends.<br>"
      "<span class=\"flag\">O que não existe aqui</span> <b>nenhum interior "
      "de Friends foi filmado neste prédio</b>. O apartamento da Monica, o de "
      "Chandler e Joey e o Central Perk eram cenários montados no "
      "<b>Stage 24 da Warner Bros., em Burbank, Califórnia</b>."),
     ("Dias em que não funciona",
      "<b>Está lá sempre</b>, e é rua pública. Não há horário, bilheteria "
      "nem fila oficial.<br>"
      "<b>Mas moram pessoas ali.</b> Em dias movimentados a esquina junta "
      "dezenas de visitantes fotografando a porta de casa de alguém. Vale "
      "evitar de madrugada e não bloquear a entrada."),
     ("Endereço",
      "90 Bedford Street, NY 10014 — <b>esquina noroeste com a Grove "
      "Street</b>, no West Village.<br>" +
      mapa("90 Bedford Street, New York, NY 10014", "90 Bedford Street")),
     ("Metrô mais próximo",
      "<b>Christopher St–Sheridan Sq</b> (1) a 4 min · "
      "<b>West 4 St–Washington Sq</b> (A, B, C, D, E, F, M) a 7 min · "
      "<b>Houston St</b> (1) a 8 min."),
     ("Pontos de referência",
      "A esquina de Bedford com Grove, no coração do West Village. É um "
      "quarteirão de casario baixo do século XIX, muito diferente da "
      "Manhattan vertical dos cartões-postais — e é parte do porquê de a "
      "produção tê-lo escolhido."),
     ("Pontos turísticos próximos",
      "Washington Square Park 8 min a pé · Stonewall Inn 6 min · "
      "Hudson River Park 6 min · The High Line, extremidade sul, 15 min · "
      "Greenwich Village em volta, o passeio é a própria caminhada.")],
    [("Visitantes por ano",
      "<span class=\"flag\">Não existe medição.</span> Não há bilheteria, "
      "catraca nem contagem — <b>ninguém mede quantas pessoas param nesta "
      "esquina</b>, e qualquer número que circule é estimativa de terceiro."),
     ("Menor visitação e temperatura",
      "Janeiro e fevereiro <span class=\"flag\">estimativa</span>, pelo "
      "clima e pelo movimento geral da cidade. Janeiro: máx. 4 °C, "
      "mín. −2 °C. Fevereiro: máx. 6 °C, mín. −1 °C. É rua aberta, sem "
      "abrigo — no inverno a foto custa frio."),
     ("Curiosidades",
      "<ul><li><b>O prédio foi escolhido porque era a casa de alguém da "
      "produção:</b> pertencia a John Shaffner, diretor de arte da série. "
      "Não houve caça a locação — a fachada estava à mão.</li>"
      "<li><b>A fachada não mudou</b> desde o fim da série, em 2004. É o "
      "raro caso em que o cenário real envelheceu menos que o elenco.</li>"
      "<li>Na ficção o endereço é <b>Grove Street, 90</b>, apartamentos 19 e "
      "20. Na vida real é Bedford, 90 — a série trocou a rua da esquina.</li>"
      "<li><b>O apartamento da Monica seria implausível</b> na Nova York "
      "real: o tamanho mostrado, naquele bairro, estaria muito acima do que "
      "uma cozinheira e uma garçonete pagariam. A série resolveu isso com a "
      "explicação do aluguel congelado herdado da avó.</li></ul>"),
     ("Fatos históricos",
      "<ul><li>O West Village é um dos poucos trechos de Manhattan que "
      "escapou da grade de ruas de 1811 — por isso as ruas se cruzam em "
      "ângulos tortos, e por isso a Bedford faz esquina com a Grove em vez "
      "de correr paralela.</li>"
      "<li>A série foi ao ar de <b>1994 a 2004</b>, dez temporadas e 236 "
      "episódios. A fachada aparece desde o primeiro.</li></ul>")])

# ----------------------------------------------------------------- 19
PERK = ponto(
    "central-perk", 19, "Central Perk Coffeehouse", "Cafeteria licenciada",
    "Grátis", "entrar não custa; o consumo, sim",
    [("Valor da entrada",
      "<b>Entrar não se paga</b> — é uma cafeteria, não uma atração com "
      "bilheteria. Consultado em 17/set/2026 no site oficial "
      "(centralperk.com).<br>"
      "<span class=\"flag\">Preços não publicados</span> <b>o site não "
      "divulga o cardápio com valores.</b> Há um menu em PDF sem preços na "
      "página consultada. Não apuramos quanto custa o café.<br>"
      "O cardápio foi desenvolvido com participação do chef <b>Tom "
      "Colicchio</b> e traz itens exclusivos da casa de Nova York."),
     ("Dias em que não funciona",
      "<b>Abre todos os dias, das 8h às 23h</b>, segundo o site oficial.<br>"
      "Telefone: 212-204-7712.<br>"
      "<span class=\"flag\">Sala do sofá</span> a casa tem um ambiente "
      "reservado com o <b>sofá laranja</b>. <b>Não apuramos se o acesso a "
      "essa sala tem fila, reserva ou consumo mínimo.</b>"),
     ("Endereço",
      "20 Times Square, NY 10036 — <b>esquina nordeste da 7ª Avenida com a "
      "West 47th Street</b>.<br>" +
      mapa("Central Perk Coffeehouse, 20 Times Square, New York, NY 10036",
           "Central Perk Coffeehouse")),
     ("Metrô mais próximo",
      "<b>49 St</b> (N, R, W) a 2 min · <b>50 St</b> (1) a 3 min · "
      "<b>Times Sq–42 St</b> (1, 2, 3, 7, N, Q, R, W, S) a 5 min · "
      "<b>47–50 Sts–Rockefeller Ctr</b> (B, D, F, M) a 6 min."),
     ("Pontos de referência",
      "Está dentro de Times Square, a dois quarteirões da escadaria "
      "vermelha da TKTS. É a mesma esquina de painéis e multidão descrita "
      "no ponto 17 desta ficha."),
     ("Pontos turísticos próximos",
      "Times Square na porta · Top of the Rock 7 min a pé · "
      "Radio City Music Hall 6 min · Bryant Park 9 min · "
      "MoMA 10 min · Central Park, extremidade sul, 12 min.")],
    [("Visitantes por ano",
      "<span class=\"flag\">Não divulgado.</span> É estabelecimento "
      "comercial privado e não publica movimento."),
     ("Menor visitação e temperatura",
      "Janeiro e fevereiro <span class=\"flag\">estimativa</span>. "
      "Janeiro: máx. 4 °C, mín. −2 °C. Fevereiro: máx. 6 °C, mín. −1 °C. "
      "Ao contrário dos outros pontos deste grupo, aqui o inverno não "
      "atrapalha: é dentro."),
     ("Curiosidades",
      "<ul><li><b>O Central Perk da série nunca existiu como lugar.</b> Era "
      "cenário no Stage 24 da Warner Bros., em Burbank. Esta cafeteria é "
      "<b>licenciada</b> — inspirada no cenário, não a sua sobrevivência.</li>"
      "<li>Abriu em <b>Times Square</b>, não no West Village. Quem quiser "
      "fazer os dois no mesmo dia atravessa Manhattan: são cerca de "
      "6 km entre a fachada da Bedford e esta esquina.</li>"
      "<li>Antes desta, a marca só tinha operado em <b>instalações "
      "temporárias</b>. Esta é a primeira casa permanente da rede em "
      "Nova York.</li></ul>"),
     ("Fatos históricos",
      "<ul><li>A série terminou em <b>2004</b>. Esta cafeteria abriu mais de "
      "vinte anos depois — <b>não é contemporânea da série</b>, é produto do "
      "interesse que ela continuou gerando.</li>"
      "<li><span class=\"flag\">Data de abertura</span> a imprensa noticiou "
      "inauguração em <b>12 de dezembro</b>, mas <b>o site oficial não "
      "informa desde quando está aberta</b>, e não conseguimos confirmar o "
      "ano em fonte primária.</li></ul>")])

# ----------------------------------------------------------------- 20
EXPERIENCE = ponto(
    "friends-experience", 20, "The FRIENDS Experience", "Exposição",
    "US$ 39,50", "a partir de; varia por dia e horário",
    [("Valor da entrada",
      "<b>A partir de US$ 39,50</b>, em sessões com hora marcada. "
      "Consultado em 17/set/2026.<br>"
      "<span class=\"flag\">O site oficial não publica preço</span> "
      "friendstheexperience.com informa endereço, horário e política de "
      "crianças, <b>mas manda para a página de venda para saber o valor</b>. "
      "Os números abaixo vêm de revendedores e de guias, não da bilheteria:<br>"
      "• faixa corrente: <b>US$ 35 a US$ 45</b> antes de impostos, conforme "
      "o dia e o horário<br>"
      "• manhã de dia útil sai <b>US$ 5 a US$ 10 mais barato</b> que tarde "
      "de fim de semana<br>"
      "• nas <b>Summer Fridays</b>, de 1º de julho a 31 de agosto, o "
      "ingresso padrão fica a <b>US$ 41,50 mais taxas</b><br>"
      "<b>Criança de até 3 anos não paga</b>, acompanhada de responsável. "
      "Acima disso, paga ingresso."),
     ("Dias em que não funciona",
      "<b>Fecha às terças-feiras.</b> Nos outros dias abre das <b>10h às "
      "20h</b>, com <b>última entrada às 19h</b>, segundo o site oficial. "
      "Horários de feriado podem variar.<br>"
      "<span class=\"flag\">Fontes divergem</span> guias de terceiros "
      "publicam que a exposição fecharia de segunda a quarta e abriria das "
      "10h às 19h. <b>Seguimos o site oficial</b>, que diz o contrário — mas "
      "confira na véspera, porque a diferença é de dois dias inteiros."),
     ("Endereço",
      "130 East 23rd Street, NY 10010 — <b>esquina da Lexington Avenue com a "
      "23rd Street</b>, no Flatiron.<br>" +
      mapa("The FRIENDS Experience, 130 E 23rd St, New York, NY 10010",
           "The FRIENDS Experience")),
     ("Metrô mais próximo",
      "<b>23 St</b> (6) na esquina · <b>23 St</b> (R, W) a 5 min · "
      "<b>23 St</b> (F, M) a 8 min · <b>14 St–Union Sq</b> "
      "(4, 5, 6, L, N, Q, R, W) a 10 min."),
     ("Pontos de referência",
      "Fica no Flatiron, a poucos quarteirões do Madison Square Park e do "
      "próprio Flatiron Building. É bairro de escritório e restaurante, sem "
      "relação com a série — a escolha do endereço é comercial."),
     ("Pontos turísticos próximos",
      "Madison Square Park 6 min a pé · Flatiron Building 7 min · "
      "Union Square 10 min · Empire State Building 12 min · "
      "Gramercy Park 8 min.")],
    [("Visitantes por ano",
      "<span class=\"flag\">Não divulgado.</span> A operadora não publica "
      "número de visitantes da unidade de Nova York."),
     ("Menor visitação e temperatura",
      "Janeiro e fevereiro <span class=\"flag\">estimativa</span>. "
      "Janeiro: máx. 4 °C, mín. −2 °C. Fevereiro: máx. 6 °C, mín. −1 °C. "
      "A visita é interna; o inverno pesa na fila da calçada, não na "
      "exposição."),
     ("Curiosidades",
      "<ul><li>A visita é por <b>reconstituição de cenários</b> — o "
      "apartamento, o Central Perk, a fonte da abertura — com <b>figurinos e "
      "objetos originais</b> em exposição e loja no fim do percurso.</li>"
      "<li><b>Não é o cenário original.</b> Os sets do Stage 24 foram "
      "desmontados; o que existe aqui é reconstrução feita para a "
      "exposição.</li>"
      "<li><b>É o único dos três pontos deste grupo que cobra ingresso</b> — "
      "e o único em que dá para sentar no sofá sem consumir nada.</li></ul>"),
     ("Fatos históricos",
      "<ul><li>A exposição nasceu como <b>instalação temporária</b> para os "
      "25 anos da estreia e se tornou permanente diante da procura. Já "
      "circulou por várias cidades.</li>"
      "<li>A fonte que aparece na abertura da série <b>não fica em Nova "
      "York</b>: as cenas foram gravadas no <b>lote da Warner Bros.</b>, na "
      "Califórnia. Quem procurar a fonte real em Central Park não vai "
      "encontrar.</li></ul>")])


GRUPO = (
    '%s\n<section class="grupo" id="g4">'
    '<div class="grupo-head"><h2>Para quem vê Friends</h2>'
    '<p><b>Quase nada de Friends foi filmado em Nova York.</b> O apartamento, '
    'o Central Perk e a fonte da abertura eram cenários em Burbank, na '
    'Califórnia. O que a cidade tem são três endereços reais — uma fachada, '
    'uma cafeteria licenciada e uma exposição paga — e vale saber o que cada '
    'um é antes de atravessar Manhattan.</p></div>'
    '%s%s%s</section>\n%s' % (MARCA, BEDFORD, PERK, EXPERIENCE, MARCA))

IDX = ('<div><div class="idx-tit">Para quem vê Friends</div>'
       '<a class="idx-item" href="#friends-predio"><span class="idx-num">18</span>'
       '<span class="idx-nome">90 Bedford Street, o prédio</span>'
       '<span class="idx-preco">Grátis</span></a>'
       '<a class="idx-item" href="#central-perk"><span class="idx-num">19</span>'
       '<span class="idx-nome">Central Perk Coffeehouse</span>'
       '<span class="idx-preco">Grátis</span></a>'
       '<a class="idx-item" href="#friends-experience"><span class="idx-num">20</span>'
       '<span class="idx-nome">The FRIENDS Experience</span>'
       '<span class="idx-preco">US$ 39,50</span></a></div>')


def main(aplica):
    h = open(ALVO, encoding="utf-8").read()
    if MARCA in h:
        print("O grupo de Friends ja esta na ficha.")
        return

    antes = len(re.findall(r'<article class="ponto"', h))

    # 1. o grupo entra depois do ultimo </section> de grupo
    ult = h.rfind('<section class="grupo"')
    fim = h.find("</section>", ult) + len("</section>")
    h = h[:fim] + "\n" + GRUPO + h[fim:]

    # 2. a coluna do indice entra no fim do idx-cols
    i = h.find('<div class="idx-cols">')
    if i < 0:
        raise SystemExit("nao achei o indice")
    # o </div> que fecha o idx-cols: conta aninhamento
    pos, nivel = i, 0
    while pos < len(h):
        a = h.find("<div", pos)
        f = h.find("</div>", pos)
        if f < 0:
            raise SystemExit("indice sem fechamento")
        if a >= 0 and a < f:
            nivel += 1
            pos = a + 4
            continue
        nivel -= 1
        pos = f + 6
        if nivel == 0:
            break
    corte = pos - len("</div>")
    h = h[:corte] + IDX + h[corte:]

    depois = len(re.findall(r'<article class="ponto"', h))
    print("pontos na ficha: %d -> %d" % (antes, depois))
    print("grupo g4 com 3 pontos, coluna no indice, marcadores %s" % MARCA)

    if aplica:
        with open(ALVO, "w", encoding="utf-8", newline="") as f:
            f.write(h)
        print()
        print("Escrito. Depois: acertar contadores (17 -> 20) e rodar")
        print("  python _build/schema/gera.py --aplica")
        print("  python _build/confere/tudo.py")
    else:
        print()
        print("Nada alterado. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
