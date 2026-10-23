# -*- coding: utf-8 -*-
"""Paginas derivadas do Rio: uma pergunta por pagina, em volta do guia.

Plano em _build/docs/cluster-rio-2026-10-23.md (fase A). Esta e a 1:
/destinos/rio-de-janeiro/cristo-redentor/; a 2, o-que-fecha-cada-dia/; a 3,
pao-de-acucar/; a 4, descontos/; a 5, quando-ir/.

DE ONDE SAI TUDO: da ficha do Cristo em g1.py, importada - a mesma que o
guia publica -, e do aviso da obra, lido do guia publicado (ele mora no
AVISOS do build.py, que nao roda mais como esta). Numero nenhum e
digitado aqui: preco, horario, data da obra e data da apuracao saem por
regex do texto da ficha, e o script PARA se nao achar algum.

CABECA, CABECALHO E RODAPE SAO EMPRESTADOS da ficha de custos do Rio,
que esta na mesma profundidade (../../../), como o recortes/gratis.py faz
com o sobre/. Saem os JSON-LD dela; entram TouristAttraction com um Offer
por forma de subir, FAQPage e BreadcrumbList. O WebPage com autor e data
vem do schema/editor.py, como em qualquer pagina.

O PARCEIRO e so a Booking, copiada do guia com sid proprio. A Aviasales
fica fora de proposito: o link dela muda todo dia com o cache de
passagens, e o espalha.py nao conhece esta pagina - a copia envelheceria
sem ninguem ver.

VIVENCIA: o Allan subiu ao Cristo. O relato dele entra no bloco
VIVENCIA abaixo, nas palavras dele e marcado como experiencia propria.
Vazio, o bloco nao aparece - nada e escrito no lugar dele.

Tambem poe os links para a pagina nova no guia (bloco "As outras
paginas" e o fim da ficha do Cristo). Idempotente.

Uso
---
    python _build/rio/paginas.py            # so mostra
    python _build/rio/paginas.py --aplica   # escreve

Depois, a cadeia de busca do LEIA-ME (sitemap, schema, adsense, drive,
confere).
"""
import html as H
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
SITE = "https://viagemnalupa.com.br"
sys.path.insert(0, AQUI)

from g1 import G1  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

GUIA = os.path.join(RAIZ, "destinos", "rio-de-janeiro", "index.html")
MOLDE = os.path.join(RAIZ, "destinos", "rio-de-janeiro", "quanto-custa", "index.html")
SOBE = "../../../"

# Relato do Allan, em primeira pessoa, com as palavras dele. Lista de
# paragrafos (HTML simples). Vazio = o bloco nao sai.
VIVENCIA = []


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def limpa(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t or "")).strip()


def acha(padrao, texto, o_que):
    m = re.search(padrao, texto, re.S)
    if not m:
        sys.exit("PARADO: nao achei %s - a ficha mudou? Conferir antes de publicar." % o_que)
    return m


def reais(t):
    """'R$ 1.312' -> 1312"""
    return int(t.replace(".", ""))


def ponto(pid):
    for p in G1["pontos"]:
        if p["id"] == pid:
            return p
    sys.exit("PARADO: %s nao esta em g1.py" % pid)


def coords(pid):
    for c in json.loads(le(os.path.join(RAIZ, "_build", "coords.json"))):
        if c["c"] == "rio" and c["id"] == pid:
            return c["lat"], c["lng"]
    return None


def esqueleto(titulo, descricao, url, imagem, alt):
    s = le(MOLDE)
    cabeca = s[:s.find('<main id="conteudo">')]
    pe = s[s.find("</main>"):]
    cabeca = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", cabeca, flags=re.S)
    t, d = H.escape(titulo, quote=True), H.escape(descricao, quote=True)
    cabeca = re.sub(r"<title>.*?</title>", "<title>%s</title>" % t, cabeca, flags=re.S)
    cabeca = re.sub(r'<meta name="description" content="[^"]*">',
                    '<meta name="description" content="%s">' % d, cabeca)
    cabeca = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url, cabeca)
    cabeca = re.sub(r'<meta property="og:title" content="[^"]*">',
                    '<meta property="og:title" content="%s">' % t, cabeca)
    cabeca = re.sub(r'<meta property="og:description" content="[^"]*">',
                    '<meta property="og:description" content="%s">' % d, cabeca)
    # og:url + og:image (e largura, altura, alt e twitter:image) saem juntos
    cabeca = re.sub(r'<meta property="og:url" content="[^"]*">.*?<meta name="twitter:image" content="[^"]*">',
                    '<meta property="og:url" content="%s"><meta property="og:image" content="%s">'
                    '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="675">'
                    '<meta property="og:image:alt" content="%s"><meta name="twitter:image" content="%s">'
                    % (url, imagem, H.escape(alt, quote=True), imagem), cabeca, flags=re.S)
    return cabeca, pe


def ld(o):
    return '<script type="application/ld+json">%s</script>\n' % json.dumps(
        o, ensure_ascii=False, separators=(",", ":"))


def faq_html(perguntas, sobre="o Cristo Redentor"):
    itens = "".join(
        '\n  <details class="faq-q"><summary><h3>%s</h3></summary><p>%s</p></details>' % (H.escape(q), a)
        for q, a in perguntas)
    return ('<section class="bloco faq" id="perguntas">\n  <div class="bloco-head"><span class="eyebrow">'
            'Perguntas frequentes</span><h2>O que mais se pergunta sobre %s</h2></div>%s\n'
            '</section>\n' % (sobre, itens))


def faq_ld(perguntas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": limpa(a)}} for q, a in perguntas]}


# As paginas do cluster, na ordem em que aparecem no "Continue" de cada uma.
IRMAS = [
    ("", "Guia dos 16 pontos turísticos"),
    ("cristo-redentor/", "Cristo Redentor: ingresso e como subir"),
    ("pao-de-acucar/", "Pão de Açúcar: ingresso e desconto"),
    ("o-que-fecha-cada-dia/", "O que abre e fecha em cada dia"),
    ("descontos/", "Onde morador e brasileiro pagam menos"),
    ("quando-ir/", "Quando ir, mês a mês"),
    ("quanto-custa/", "Quanto custa 6 dias no Rio"),
    ("roteiro-6-dias/", "Roteiro de 6 dias"),
    ("quanto-custa/#calculadora", "Calculadora da viagem"),
]


def continua(atual):
    links = " ".join('<a class="pg" href="../%s">%s</a>' % (h, t) for h, t in IRMAS if h != atual + "/")
    return ('<section class="bloco">\n  <div class="bloco-head"><span class="eyebrow">Continue</span>'
            '<h2>As outras páginas do Rio de Janeiro</h2></div>\n  <div class="paginas"> %s </div>\n</section>\n\n'
            % links)


SETA = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 17 L17 7 '
        'M9 7h8v8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '</path></svg>')


def reserva(guia, sid, frase):
    """O bloco da Booking, com o link do guia e sid proprio. frase: o que dizer do ingresso."""
    booking = acha(r'<a class="parceiro" href="(https://www\.jdoqocy\.com/[^"]*)"', guia, "a Booking do guia").group(1)
    booking = re.sub(r"sid=[^&\"]*", "sid=vnl-rio-de-janeiro-" + sid, booking)
    return ('<section class="bloco">\n<div class="reserva">\n<div class="reserva-topo">\n<h3>Hospedagem</h3>\n'
            '<p>%sA hospedagem e a passagem não entram nos preços desta página; <a href="../quanto-custa/">a ficha '
            'de custos</a> traz as duas, com a data da apuração.</p>\n'
            '<p style="color:var(--nevoa);font-size:.9rem"><b>Este link dá comissão ao site.</b> Você paga o mesmo '
            'preço que pagaria indo direto, e a comissão <b>não altera nenhum número do site</b>. '
            '<a href="%ssobre/">Como isso funciona</a>.</p>\n</div>\n'
            '<div class="reserva-lista"><a class="parceiro" href="%s" target="_blank" rel="noopener sponsored">'
            '<span class="p-nome">Booking.com%s</span><span class="p-nota">hotéis no Rio de Janeiro</span></a></div>\n'
            '</div>\n</section>\n' % (frase, SOBE, H.escape(booking, quote=True), SETA))


# ------------------------------------------------------------------ Cristo
def cristo(guia):
    p = ponto("cristo-redentor")
    c = p["campos"]
    pid = p["id"]
    url = "%s/destinos/rio-de-janeiro/%s/" % (SITE, pid)

    # --- o preco, linha a linha: "<b>Forma:</b> texto com R$"
    linhas = c["Valor da entrada"].split("<br>")
    fonte = linhas[0]
    data_ap = acha(r"consultados em (\d+/\w+/\d{4})", fonte, "a data da apuracao").group(1)
    formas = []
    resto = []
    for ln in linhas[1:]:
        # "<b>Van ...:</b> adulto R$ 87" ou "<b>A pé pela trilha</b> (só o acesso): adulto R$ 60"
        m = re.match(r"\s*<b>(.*?)</b>(.*)", ln, re.S)
        v = re.search(r"R\$ ([\d.]+)", ln)
        nome = texto = None
        if m and v:
            if m.group(1).endswith(":"):
                nome, texto = m.group(1)[:-1], m.group(2)
            elif ":" in m.group(2):
                antes, texto = m.group(2).split(":", 1)
                nome = m.group(1) + antes
        if nome:
            formas.append(dict(nome=limpa(nome), adulto=reais(v.group(1)), texto=texto.strip()))
        else:
            resto.append(ln.strip())
    if len(formas) < 4:
        sys.exit("PARADO: so achei %d formas de subir na ficha" % len(formas))
    morador = " ".join(resto)
    if "morador" not in morador:
        sys.exit("PARADO: a linha da tarifa de morador sumiu da ficha")

    def forma(chave):
        for f in formas:
            if chave in f["nome"].lower():
                return f
        sys.exit("PARADO: nao achei a forma '%s'" % chave)
    paineiras, cidade, trilha = forma("paineiras"), forma("copacabana"), forma("trilha")

    # --- a obra, do aviso publicado no guia
    obra = acha(r"<p><b>Cristo Redentor:</b>\s*(as quatro escadas.*?)</p>", guia, "o aviso da obra").group(1)
    obra_ate = acha(r"até o fim de (\w+ de \d{4})", obra, "a data do fim da obra").group(1)
    degraus = acha(r"(\d+) degraus", obra, "os degraus").group(1)

    # --- horarios, carro e clima, da ficha
    dias = [x.strip() for x in c["Dias em que não funciona"].split("<br>") if x.strip()]
    horarios = next((x for x in dias if "perder o dia" in x), None)
    carro = next((x for x in dias if "Carro" in x), None)
    if not (horarios and carro):
        sys.exit("PARADO: os paragrafos de horario/carro sumiram da ficha")
    ult = acha(r"última entrada às (\d+h)", limpa(horarios), "a ultima entrada").group(1)
    vans_ate = acha(r"Largo do Machado das \d+h às (\d+h)", limpa(horarios), "o fim das vans").group(1)

    # ------------------------------------------------- textos derivados
    titulo = "Cristo Redentor: ingresso, preço e como subir em 2026"
    descricao = ("Ingresso do Cristo Redentor de R$ %d a R$ %d, conforme a forma de subir: van das Paineiras "
                 "R$ %d, de Copacabana ou do Largo do Machado R$ %d. Com a obra das escadas rolantes até %s. "
                 "Apurado em %s."
                 % (min(f["adulto"] for f in formas), max(f["adulto"] for f in formas),
                    paineiras["adulto"], cidade["adulto"], obra_ate, data_ap))
    img = SITE + "/assets/img/rio-de-janeiro/cristo.webp"
    capa = acha(r'(?s)<figure class="hero-capa">.*?</figure>', guia, "a capa do guia").group(0)
    alt = acha(r'alt="([^"]*)"', capa, "o alt da capa").group(1)
    capa = capa.replace('"../../', '"' + SOBE).replace(' ../../', ' ' + SOBE)

    perguntas = [
        ("Qual é o jeito mais barato de subir ao Cristo Redentor?",
         "%s: R$ %d o adulto, só o acesso ao monumento. Com transporte, a %s custa R$ %d; "
         "a mesma van saindo de Copacabana ou do Largo do Machado custa R$ %d."
         % (trilha["nome"], trilha["adulto"], paineiras["nome"].lower(), paineiras["adulto"], cidade["adulto"])),
        ("Tem desconto para morador do Rio no Cristo Redentor?",
         "%s O que muda o preço é o ponto de embarque: R$ %d nas Paineiras contra R$ %d em Copacabana "
         "ou no Largo do Machado, R$ %d de diferença pela mesma subida."
         % (limpa(morador), paineiras["adulto"], cidade["adulto"], cidade["adulto"] - paineiras["adulto"])),
        ("Até quando vai a obra no Cristo Redentor?",
         "Até o fim de %s. %s" % (obra_ate, limpa(obra))),
        ("Dá para subir ao Cristo Redentor de carro?", limpa(carro)),
        ("Qual é o horário do Cristo Redentor?", limpa(horarios)),
    ]

    # ------------------------------------------------- JSON-LD
    ofertas = [{"@type": "Offer", "name": f["nome"], "price": "%d.00" % f["adulto"],
                "priceCurrency": "BRL", "description": "Adulto. " + limpa(f["texto"]),
                "url": url + "#precos"} for f in formas]
    atracao = {"@context": "https://schema.org", "@type": "TouristAttraction",
               "name": p["nome"], "url": url, "image": img,
               "description": limpa(c["Fatos históricos"])[:300],
               "isAccessibleForFree": False, "publicAccess": True,
               "address": {"@type": "PostalAddress", "addressLocality": "Rio de Janeiro",
                           "addressRegion": "RJ", "addressCountry": "BR"},
               "containedInPlace": {"@type": "TouristDestination", "name": "Rio de Janeiro",
                                    "url": SITE + "/destinos/rio-de-janeiro/"},
               "offers": ofertas}
    g = coords(pid)
    if g:
        atracao["geo"] = {"@type": "GeoCoordinates", "latitude": g[0], "longitude": g[1]}
    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Destinos", "item": SITE + "/destinos/"},
        {"@type": "ListItem", "position": 3, "name": "Rio de Janeiro", "item": SITE + "/destinos/rio-de-janeiro/"},
        {"@type": "ListItem", "position": 4, "name": "Cristo Redentor", "item": url}]}

    cabeca, pe = esqueleto(titulo, descricao, url, img, alt)
    cabeca = cabeca.replace("</head>", ld(atracao) + ld(faq_ld(perguntas)) + ld(migalhas) + "</head>", 1)
    pe = pe.replace("<!-- consentimento:inicio -->",
                    '<script src="%sassets/js/streetview.js" defer></script>\n<!-- consentimento:inicio -->' % SOBE, 1)

    # ------------------------------------------------- o corpo
    import sv  # noqa: E402  (o mesmo botao do guia)

    linhas_tab = "".join(
        '<tr><td><b>%s</b></td><td class="n">R$ %d</td><td>%s</td></tr>'
        % (H.escape(f["nome"]), f["adulto"], f["texto"]) for f in formas)

    def campo(rot, sec_id, eyebrow, corpo, extra=""):
        return ('<section class="bloco" id="%s">\n  <div class="bloco-head"><span class="eyebrow">%s</span>'
                '<h2>%s</h2></div>\n  %s%s\n</section>\n\n' % (sec_id, eyebrow, rot, corpo, extra))

    def ps(t):
        return "".join('<p style="color:var(--nevoa)">%s</p>' % x.strip() for x in t.split("<br>") if x.strip())

    vivencia = ""
    if VIVENCIA:
        vivencia = campo("Quem apurou também subiu", "vivencia", "Experiência própria",
                         "".join('<p style="color:var(--nevoa)">%s</p>' % x for x in VIVENCIA)
                         + '<p style="color:var(--nevoa);font-size:.9rem">Relato de <a href="%ssobre/#quem-faz">'
                           'Allan Vitor</a>, em primeira pessoa. Os preços e horários desta página não saem do '
                           'relato: saem das fontes citadas, na data indicada.</p>' % SOBE)

    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">%s</span><span class="big c">R$ %d</span>'
        '<span class="sub">Adulto. O jeito mais barato de subir com transporte.</span></div>'
        '<div class="pcel"><span class="rotp">Van de Copacabana ou do Largo do Machado</span><span class="big">R$ %d</span>'
        '<span class="sub">A mesma subida, R$ %d a mais.</span></div>'
        '<div class="pcel"><span class="rotp">Escadas rolantes em obra até %s</span><span class="big c">%s degraus</span>'
        '<span class="sub">E metade dos ingressos à venda. Compre com antecedência.</span></div>'
        '<div class="pcel"><span class="rotp">Última entrada nas Paineiras</span><span class="big">%s</span>'
        '<span class="sub">As vans da cidade saem até as %s.</span></div>'
        '</div>' % (paineiras["nome"], paineiras["adulto"], cidade["adulto"],
                    cidade["adulto"] - paineiras["adulto"], obra_ate, degraus, ult, vans_ate))

    partes = [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="%s">Início</a> › <a href="../../">Destinos</a> › '
        '<a href="../">Rio de Janeiro</a> › Cristo Redentor</p>\n' % SOBE,
        '<div class="hero">\n  <span class="eyebrow">Ingresso e acesso</span>\n'
        '  <h1>Cristo Redentor: ingresso, preço e as %d formas de subir</h1>\n'
        '  <p>Quanto custa cada jeito de chegar ao alto do Corcovado, de onde sai cada um, o horário que '
        'faz perder o dia e a obra que reduziu os ingressos à metade. Preços consultados em %s.</p>\n'
        '<p class="assinatura">Apurado por <a href="%ssobre/#quem-faz">Allan Vitor</a> · '
        '<a href="https://www.instagram.com/viagemnalupabr/" target="_blank" rel="noopener">@viagemnalupabr'
        '<span class="so-leitor"> (abre em outra aba)</span></a></p>\n</div>\n'
        % (len(formas), data_ap, SOBE),
        capa, "\n", painel, '\n<div style="height:clamp(1.4rem,3vw,2.2rem)"></div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
        '<section class="bloco"><div class="aviso a"><span class="t">A obra das escadas rolantes, até %s</span>'
        '<p>%s</p></div></section>\n\n' % (obra_ate, obra[0].upper() + obra[1:]),
        campo("Quanto custa cada forma de subir", "precos", "Preço por pessoa",
              '<div class="tabwrap"><table><thead><tr><th>Forma de subir</th><th>Adulto</th>'
              '<th>Desconto e observação</th></tr></thead><tbody>%s</tbody></table></div>\n'
              '  <p style="color:var(--nevoa)">%s</p>\n  <p style="color:var(--nevoa)">%s</p>'
              % (linhas_tab, fonte, morador)),
        campo("De onde sai cada subida", "embarque", "Embarque e metrô",
              '<p style="color:var(--nevoa)">%s</p>\n  <p style="color:var(--nevoa)">%s</p>'
              % (c["Endereço"], c["Metrô mais próximo"]), sv.botao(pid)),
        campo("Horários e quando o acesso fecha", "horarios", "Antes de sair", ps(c["Dias em que não funciona"])),
        campo("Quando ir", "quando-ir", "Clima e movimento", ps(c["Menor visitação e temperatura"])),
        vivencia,
        campo("O monumento", "monumento", "História e números",
              '<p style="color:var(--nevoa)">%s</p>\n  <p style="color:var(--nevoa)">%s</p>\n  %s\n'
              '  <p style="color:var(--nevoa)">%s</p>'
              % (c["Fatos históricos"], c["Visitantes por ano"], c["Curiosidades"], c["Pontos de referência"])),
        campo("Perto dali", "perto", "Para emendar", '<p style="color:var(--nevoa)">%s</p>' % c["Pontos turísticos próximos"]),
        faq_html(perguntas), "\n",
        continua(pid),
        reserva(guia, "cristo", "O ingresso compre só no canal oficial: com a obra, ele esgota dias antes. "),
        '</div>\n',
    ]
    return os.path.join(RAIZ, "destinos", "rio-de-janeiro", pid, "index.html"), cabeca + "".join(partes) + pe


# ------------------------------------------------------------ Pão de Açúcar
def pao(guia):
    p = ponto("pao-de-acucar")
    c = p["campos"]
    pid = p["id"]
    url = "%s/destinos/rio-de-janeiro/%s/" % (SITE, pid)

    # --- o preco: "<b>Categoria: R$ N</b>, quem tem direito." em sequencia
    linhas = c["Valor da entrada"].split("<br>")
    fonte = linhas[0]
    data_ap = acha(r"consultado em (\d+/\w+/\d{4})", fonte, "a data da apuracao").group(1)
    cats = []
    for m in re.finditer(r"<b>(.*?)</b>([^<]*)", linhas[1]):
        b, depois = m.group(1).strip().rstrip("."), m.group(2)
        if "R$" not in b:
            continue
        if ":" in b:
            nome, preco = [x.strip() for x in b.split(":", 1)]
        else:
            nome, preco = re.match(r"(.*?)\s*(R\$.*)", b).groups()
        quem = re.sub(r"^\s*(\(≈[^)]*\))?[.,]?\s*", "", depois).split(".")[0].strip()
        if not quem and "," in nome:
            nome, quem = [x.strip() for x in nome.split(",", 1)]
        valores = [reais(v) for v in re.findall(r"R\$ ([\d.]+)", preco)]
        cats.append(dict(nome=nome, preco=preco, quem=quem, valor=valores[0]))
    if len(cats) < 5:
        sys.exit("PARADO: so achei %d categorias de preco na ficha" % len(cats))
    gratis = acha(r"(Bebês[^<]*?não pagam\.)", linhas[1], "a gratuidade de bebe").group(1)

    def cat(chave):
        for k in cats:
            if chave in k["nome"].lower():
                return k
        sys.exit("PARADO: nao achei a categoria '%s'" % chave)
    inteira, brasil, rj = cat("inteira"), cat("brasileiros"), cat("estado do rj")
    economia = round(100 * (inteira["valor"] - rj["valor"]) / inteira["valor"])
    if "%d%%" % economia not in c["Valor da entrada"]:
        sys.exit("PARADO: a economia calculada (%d%%) nao bate com a ficha" % economia)
    dinamico = next((x for x in linhas if "a partir de" in x), None)
    if not dinamico:
        sys.exit("PARADO: a ressalva do preco dinamico sumiu da ficha")

    dias = [x.strip() for x in c["Dias em que não funciona"].split("<br>") if x.strip()]
    horario = dias[0]
    doc = next((x for x in dias if "documento" in x), None)
    if not doc:
        sys.exit("PARADO: o aviso do documento sumiu da ficha")
    abre, fecha = acha(r"das (\d+h\d*) às (\d+h)", limpa(horario), "o horario").groups()
    ultimo = acha(r"último embarque às (\d+h\d*)", limpa(horario), "o ultimo embarque").group(1)
    if "feriados incluídos" not in horario:
        sys.exit("PARADO: a ficha nao diz mais que abre nos feriados")
    onibus = acha(r"ônibus de integração <b>(\d+) \(([^)]*)\)</b>", c["Metrô mais próximo"], "o onibus 513").groups()
    metro = limpa(acha(r"<b>(.*?)</b>", c["Metrô mais próximo"], "a estacao de metro").group(1)).rstrip(".")
    metro = re.sub(r"^(.*?) — (.*)$", r"\1 (\2)", metro)

    # ------------------------------------------------- textos derivados
    titulo = "Pão de Açúcar: ingresso, preço e desconto de morador em 2026"
    descricao = ("Bondinho do Pão de Açúcar: inteira R$ %d, R$ %d para brasileiro e R$ %d para quem mora no Estado "
                 "do Rio, %d%% a menos. O documento que pedem, horário e como chegar de metrô. Apurado em %s."
                 % (inteira["valor"], brasil["valor"], rj["valor"], economia, data_ap))
    img_id = p["img"]
    cred = json.loads(le(os.path.join(AQUI, "creditos.json")))[img_id]
    if cred["fonte"] == "storyblocks":
        credito = "Storyblocks · licença royalty-free · SBI-%s" % cred["sbi"]
    else:
        credito = ('Foto: %s · <a href="%s" target="_blank" rel="noopener license">%s</a> · '
                   '<a href="%s" target="_blank" rel="noopener">Wikimedia Commons</a> · recortada'
                   % (H.escape(cred["autor"]), cred["licurl"], cred["lic"], cred["pagina"]))
    base_img = SOBE + "assets/img/rio-de-janeiro/" + img_id
    capa = ('<figure class="hero-capa">\n  <img fetchpriority="high" srcset="%(b)s-400.webp 400w, %(b)s-640.webp 640w, '
            '%(b)s-820.webp 820w, %(b)s.webp 1200w" sizes="(min-width:1080px) 820px, 100vw" src="%(b)s.webp" '
            'alt="%(alt)s" width="1200" height="675" decoding="async">\n  <figcaption><p class="foto-cred">%(c)s'
            '</p></figcaption>\n</figure>' % dict(b=base_img, alt=H.escape(cred["alt"], quote=True), c=credito))
    img = "%s/assets/img/rio-de-janeiro/%s.webp" % (SITE, img_id)

    perguntas = [
        ("Quanto custa o bondinho do Pão de Açúcar?",
         "A inteira custa R$ %d. %s" % (inteira["valor"], "; ".join(
             "%s: %s" % (k["nome"], k["preco"]) for k in cats if k is not inteira) + ". " + gratis)),
        ("Morador do Rio paga menos no Pão de Açúcar?",
         "Sim. Quem mora no Estado do Rio paga %s, %s. É %d%% a menos que a inteira de R$ %d."
         % (rj["preco"], rj["quem"], economia, inteira["valor"])),
        ("Brasileiro de outro estado tem desconto?",
         "Tem: a tarifa %s custa %s, %s." % (brasil["nome"], brasil["preco"], brasil["quem"])),
        ("Que documento preciso levar ao Pão de Açúcar?", limpa(doc)),
        ("Qual é o horário do bondinho do Pão de Açúcar?",
         "Das %s às %s, todos os dias e nos feriados, com último embarque às %s. Vento forte e raio suspendem a "
         "operação dos cabos." % (abre, fecha, ultimo)),
        ("Como chegar ao Pão de Açúcar de metrô?",
         "Desça na estação %s e pegue o ônibus de integração %s (%s) até o ponto UNIRIO, a poucos metros da entrada. "
         "Não há estacionamento no parque." % (metro, onibus[0], onibus[1])),
    ]

    ofertas = [{"@type": "Offer", "name": k["nome"], "price": "%d.00" % k["valor"], "priceCurrency": "BRL",
                "description": limpa("%s %s" % (k["preco"], k["quem"])), "url": url + "#precos"} for k in cats]
    atracao = {"@context": "https://schema.org", "@type": "TouristAttraction",
               "name": "Parque Bondinho Pão de Açúcar", "alternateName": p["nome"], "url": url, "image": img,
               "description": limpa(c["Fatos históricos"])[:300],
               "isAccessibleForFree": False, "publicAccess": True,
               "address": {"@type": "PostalAddress", "streetAddress": "Av. Pasteur, 520",
                           "addressLocality": "Rio de Janeiro", "addressRegion": "RJ", "addressCountry": "BR"},
               "containedInPlace": {"@type": "TouristDestination", "name": "Rio de Janeiro",
                                    "url": SITE + "/destinos/rio-de-janeiro/"},
               "offers": ofertas}
    if "Av. Pasteur, 520" not in c["Endereço"]:
        sys.exit("PARADO: o endereco da ficha mudou")
    g = coords(pid)
    if g:
        atracao["geo"] = {"@type": "GeoCoordinates", "latitude": g[0], "longitude": g[1]}
    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Destinos", "item": SITE + "/destinos/"},
        {"@type": "ListItem", "position": 3, "name": "Rio de Janeiro", "item": SITE + "/destinos/rio-de-janeiro/"},
        {"@type": "ListItem", "position": 4, "name": "Pão de Açúcar", "item": url}]}

    cabeca, pe = esqueleto(titulo, descricao, url, img, cred["alt"])
    cabeca = cabeca.replace("</head>", ld(atracao) + ld(faq_ld(perguntas)) + ld(migalhas) + "</head>", 1)
    pe = pe.replace("<!-- consentimento:inicio -->",
                    '<script src="%sassets/js/streetview.js" defer></script>\n<!-- consentimento:inicio -->' % SOBE, 1)

    import sv  # noqa: E402  (o mesmo botao do guia)

    def campo(rot, sec_id, eyebrow, corpo, extra=""):
        return ('<section class="bloco" id="%s">\n  <div class="bloco-head"><span class="eyebrow">%s</span>'
                '<h2>%s</h2></div>\n  %s%s\n</section>\n\n' % (sec_id, eyebrow, rot, corpo, extra))

    def ps(t):
        return "".join('<p style="color:var(--nevoa)">%s</p>' % x.strip() for x in t.split("<br>") if x.strip())

    linhas_tab = "".join('<tr><td><b>%s</b></td><td class="n">%s</td><td>%s</td></tr>'
                         % (H.escape(k["nome"]), k["preco"], k["quem"][:1].upper() + k["quem"][1:] if k["quem"] else "—")
                         for k in cats)
    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">Inteira</span><span class="big">R$ %d</span>'
        '<span class="sub">O preço de quem não comprova nada.</span></div>'
        '<div class="pcel"><span class="rotp">Brasileiro de qualquer estado</span><span class="big c">R$ %d</span>'
        '<span class="sub">Nascido ou residente no Brasil.</span></div>'
        '<div class="pcel"><span class="rotp">Morador do Estado do Rio</span><span class="big c">R$ %d</span>'
        '<span class="sub">%d%% a menos que a inteira. Leve o comprovante.</span></div>'
        '<div class="pcel"><span class="rotp">Último embarque</span><span class="big">%s</span>'
        '<span class="sub">Abre às %s, todos os dias.</span></div>'
        '</div>' % (inteira["valor"], brasil["valor"], rj["valor"], economia, ultimo, abre))

    partes = [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="%s">Início</a> › <a href="../../">Destinos</a> › '
        '<a href="../">Rio de Janeiro</a> › Pão de Açúcar</p>\n' % SOBE,
        '<div class="hero">\n  <span class="eyebrow">Ingresso e desconto</span>\n'
        '  <h1>Pão de Açúcar: ingresso, preço e o desconto de quem mora no Rio</h1>\n'
        '  <p>O bondinho tem %d preços, e quem mora no Estado do Rio paga %d%% menos que a inteira. Quem paga '
        'cada um, o documento que pedem na catraca, o horário e como chegar de metrô. Preços consultados em %s.</p>\n'
        '<p class="assinatura">Apurado por <a href="%ssobre/#quem-faz">Allan Vitor</a> · '
        '<a href="https://www.instagram.com/viagemnalupabr/" target="_blank" rel="noopener">@viagemnalupabr'
        '<span class="so-leitor"> (abre em outra aba)</span></a></p>\n</div>\n' % (len(cats), economia, data_ap, SOBE),
        capa, "\n", painel, '\n<div style="height:clamp(1.4rem,3vw,2.2rem)"></div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
        '<section class="bloco"><div class="aviso b"><span class="t">Leve o documento da sua categoria</span>'
        '<p>%s</p></div></section>\n\n' % doc,
        campo("Quanto custa cada ingresso", "precos", "Preço por pessoa",
              '<div class="tabwrap"><table><thead><tr><th>Categoria</th><th>Preço</th>'
              '<th>Quem tem direito</th></tr></thead><tbody>%s</tbody></table></div>\n'
              '  <p style="color:var(--nevoa)">%s %s</p>\n  <p style="color:var(--nevoa)">%s</p>'
              % (linhas_tab, gratis, fonte, dinamico)),
        campo("Horário e quando o bondinho para", "horarios", "Antes de sair", ps(c["Dias em que não funciona"])),
        campo("Como chegar", "como-chegar", "Endereço, metrô e ônibus",
              '<p style="color:var(--nevoa)">%s</p>\n  <p style="color:var(--nevoa)">%s</p>'
              % (c["Endereço"], c["Metrô mais próximo"]), sv.botao(pid)),
        campo("Quando ir", "quando-ir", "Clima e movimento", ps(c["Menor visitação e temperatura"])),
        campo("O bondinho", "bondinho", "História e números",
              '<p style="color:var(--nevoa)">%s</p>\n  <p style="color:var(--nevoa)">%s</p>\n  %s\n'
              '  <p style="color:var(--nevoa)">%s</p>'
              % (c["Fatos históricos"], c["Visitantes por ano"], c["Curiosidades"], c["Pontos de referência"])),
        campo("Perto dali", "perto", "Para emendar", '<p style="color:var(--nevoa)">%s</p>' % c["Pontos turísticos próximos"]),
        faq_html(perguntas, "o Pão de Açúcar"), "\n",
        continua(pid),
        reserva(guia, "pao", "O ingresso compre no canal oficial e leve o documento da sua categoria. "),
        '</div>\n',
    ]
    return os.path.join(RAIZ, "destinos", "rio-de-janeiro", pid, "index.html"), cabeca + "".join(partes) + pe


def liga_pao_no_guia(h):
    if 'href="pao-de-acucar/"' in h:
        return h
    pg = '<a class="pg" href="pao-de-acucar/">Pão de Açúcar: ingresso e desconto</a>'
    h = re.sub(r'(<h2>As outras páginas do Rio de Janeiro</h2></div>\s*<div class="paginas">)',
               r"\1 " + pg, h, count=1)
    mais = ('\n  <p class="foto-nota"><a href="pao-de-acucar/">Página completa do Pão de Açúcar: '
            'os preços lado a lado, o documento que pedem e as perguntas frequentes</a></p>')
    return re.sub(r'(<article class="ponto" id="pao-de-acucar">.*?)(\n</article>)',
                  lambda m: m.group(1) + mais + m.group(2), h, count=1, flags=re.S)


# -------------------------------------------------------------- Descontos
#
# Mesma ideia do CALENDARIO: o texto de cada desconto e escrito aqui, curto,
# mas TODO numero dele (preco, idade, ano, quantidade) precisa aparecer no
# campo "Valor da entrada" da ficha daquele ponto. Numero que nao esta na
# ficha para o script - nada entra na pagina que o guia nao publique.
#
# Tres grupos: onde voce mora, o dia ou o jeito de comprar, e a meia e a
# gratuidade por idade ou condicao.
DESCONTOS = {
 "morar": [
  ("pao-de-acucar", "Morador do Estado do Rio paga R$ 89 o adulto e R$ 44 a criança de 3 a 12, contra R$ 205 da "
                    "inteira. Brasileiro de qualquer estado paga R$ 160. Pedem comprovante de residência ou "
                    "documento de naturalidade."),
  ("jardim-botanico", "Quem mora no Brasil paga R$ 40; estrangeiro, R$ 80. O desconto é por país, não por cidade: "
                      "não há tarifa de morador do município do Rio."),
  ("mar", "Nascidos e moradores da cidade do Rio pagam meia, R$ 10, contra R$ 20 da inteira. Documentação "
          "comprobatória exigida."),
  ("santa-teresa-bonde", "Moradores de Santa Teresa previamente cadastrados viajam de graça, limitados a 6 assentos "
                         "por veículo. Os outros pagam R$ 20, ida e volta."),
  ("cristo-redentor", "Não existe tarifa de morador do Rio: o programa Tarifa Carioca não cobre o monumento."),
  ("museu-do-amanha", "Não existe faixa de morador do Rio."),
 ],
 "dia": [
  ("cristo-redentor", "A van que sai das Paineiras custa R$ 87; a que sai de Copacabana ou do Largo do Machado, "
                      "R$ 132. A pé pela trilha, R$ 60, só o acesso ao monumento."),
  ("mar", "Terça-feira é gratuita para todos."),
  ("museu-do-amanha", "Todo dia 10 do mês o ingresso custa R$ 10, sem somar com a meia. Os feriados nacionais são "
                      "gratuitos. A terça deixou de ser grátis em 2025: tem preço popular, entre R$ 15 e R$ 30."),
  ("theatro-municipal", "Meia-entrada solidária: R$ 10 doando 1 kg de alimento não perecível, contra R$ 20 da "
                        "inteira."),
 ],
 "meia": [
  ("cristo-redentor", "Criança de 7 a 11 anos, estudante, 60+, PcD e acompanhante pagam R$ 60 na van das "
                      "Paineiras. No trem, o idoso 60+ brasileiro paga R$ 70. Até 6 anos não paga."),
  ("pao-de-acucar", "Criança de 3 a 12 anos e 60+ pagam R$ 102. Bebês até 2 anos e 11 meses não pagam."),
  ("jardim-botanico", "Meia de R$ 20 para estudante, PcD, jovem até 21 anos, ID Jovem e 60+, mas as fontes "
                      "oficiais divergem sobre o valor da meia. Até 5 anos não paga."),
  ("museu-do-amanha", "Meia de R$ 20. Gratuito para 60+, crianças até 5 anos e alunos e professores da rede "
                      "pública, entre outros; essa lista vem da imprensa, não do site do museu."),
  ("mar", "Meia de R$ 10 para quem tem até 21 anos, jovens de 15 a 29 anos com ID Jovem, estudantes, professores "
          "particulares e PcD. Gratuito para 60+, crianças até 5 anos e alunos da rede pública."),
  ("theatro-municipal", "Meia de R$ 10 na visita guiada."),
  ("santa-teresa-bonde", "Gratuito para idosos a partir de 65 anos, estudantes de escola pública uniformizados e "
                         "com carteirinha e portadores do Vale Social."),
  ("maracana", "Meia de R$ 57,50 para estudante, criança de 3 a 11 anos, 60+, PcD e professores da rede pública "
               "municipal do Rio. A meia não vale para grupos. Até 2 anos não paga."),
 ],
}
GRUPO_DESC = {
 "morar": ("onde-voce-mora", "Onde morar no Rio, ou no Brasil, muda o preço",
           "Em %(com)d pontos, o endereço do visitante corta o preço. Em %(sem)d, a tarifa de morador que muita "
           "gente procura não existe."),
 "dia": ("dia-e-jeito", "O dia e o jeito de comprar", "O mesmo ponto, mais barato por causa do dia, do embarque "
         "ou de uma doação."),
 "meia": ("meia-e-gratuidade", "Meia-entrada e gratuidade", "Por idade, estudo ou condição, ponto por ponto. "
          "Todos pedem documento."),
}


def minuscula(t):
    return t[:1].lower() + t[1:]


def capa_de(img_id, prioridade=True):
    cred = json.loads(le(os.path.join(AQUI, "creditos.json")))[img_id]
    if cred["fonte"] == "storyblocks":
        credito = "Storyblocks · licença royalty-free · SBI-%s" % cred["sbi"]
    else:
        credito = ('Foto: %s · <a href="%s" target="_blank" rel="noopener license">%s</a> · '
                   '<a href="%s" target="_blank" rel="noopener">Wikimedia Commons</a> · recortada'
                   % (H.escape(cred["autor"]), cred["licurl"], cred["lic"], cred["pagina"]))
    b = SOBE + "assets/img/rio-de-janeiro/" + img_id
    figura = ('<figure class="hero-capa">\n  <img%s srcset="%s-400.webp 400w, %s-640.webp 640w, %s-820.webp 820w, '
              '%s.webp 1200w" sizes="(min-width:1080px) 820px, 100vw" src="%s.webp" alt="%s" width="1200" '
              'height="675" decoding="async">\n  <figcaption><p class="foto-cred">%s</p></figcaption>\n</figure>'
              % (' fetchpriority="high"' if prioridade else "", b, b, b, b, b, H.escape(cred["alt"], quote=True),
                 credito))
    return figura, "%s/assets/img/rio-de-janeiro/%s.webp" % (SITE, img_id), cred["alt"]


def descontos(guia):
    from g2 import G2
    from g3 import G3
    from g4 import G4
    pontos = {p["id"]: p for g in (G1, G2, G3, G4) for p in g["pontos"]}
    for grupo, itens in DESCONTOS.items():
        for pid, texto in itens:
            ficha = limpa(pontos[pid]["campos"]["Valor da entrada"])
            for n in re.findall(r"\d+(?:,\d+)?", texto):
                if not re.search(r"(?<!\d)(?<!\d,)%s(?!\d|,\d)" % re.escape(n), ficha):
                    sys.exit("PARADO: '%s' (%s, %s) nao esta na ficha" % (n, pid, grupo))
    data_ap = acha(r"Preços verificados em (\d+ de \w+ de \d{4})", guia, "a data do guia").group(1)
    gratis = [p for p in pontos.values() if re.match(r"gr[aá]tis", limpa(p["preco"]), re.I)]
    url = "%s/destinos/rio-de-janeiro/descontos/" % SITE

    def numero(pid, padrao, o_que):
        return acha(padrao, limpa(pontos[pid]["campos"]["Valor da entrada"]), o_que).groups()
    pao_rj, pao_int = numero("pao-de-acucar", r"Estado do RJ: R\$ (\d+).*?", "o preco RJ")[0], \
        numero("pao-de-acucar", r"Inteira R\$ (\d+)", "a inteira")[0]
    pao_br = numero("pao-de-acucar", r"Promocional Brasileiros: R\$ (\d+)", "o preco de brasileiro")[0]
    amanha_dez = numero("museu-do-amanha", r"Todo dia 10 do mês o ingresso custa R\$ (\d+)", "o dia 10")[0]
    van_p = numero("cristo-redentor", r"Paineiras: adulto R\$ (\d+)", "a van das Paineiras")[0]
    van_c = numero("cristo-redentor", r"Largo do Machado: adulto R\$ (\d+)", "a van da cidade")[0]
    numero("mar", r"(terça-feira gratuita para todos)", "a terca gratis do MAR")

    titulo = "Rio de Janeiro: onde morador e brasileiro pagam menos, e os dias grátis"
    descricao = ("Pão de Açúcar a R$ %s para quem mora no Estado do Rio, MAR grátis na terça, Museu do Amanhã a "
                 "R$ %s todo dia 10 e onde a tarifa de morador não existe. Os descontos de %d pontos do Rio, "
                 "apurados em %s." % (pao_rj, amanha_dez, len({pid for i in DESCONTOS.values() for pid, _ in i}),
                                      data_ap))
    capa, img, alt = capa_de("mar")

    def item(pid, texto):
        return ('<li><a href="../#%s"><b>%s</b></a>: %s</li>' % (pid, H.escape(pontos[pid]["nome"]), texto))

    secoes = []
    for grupo in ("morar", "dia", "meia"):
        sid, h2, intro = GRUPO_DESC[grupo]
        sem = sum(1 for _, t in DESCONTOS[grupo] if t.startswith("Não existe"))
        if "%(" in intro:
            intro = intro % dict(com=len(DESCONTOS[grupo]) - sem, sem=sem)
        secoes.append('<section class="bloco" id="%s">\n  <div class="bloco-head"><h2>%s</h2><p>%s</p></div>\n'
                      '  <ul class="plain">%s</ul>\n</section>\n\n'
                      % (sid, h2, intro, "".join(item(pid, t) for pid, t in DESCONTOS[grupo])))

    nomes_gratis = [p["nome"] for p in gratis]
    secoes.append('<section class="bloco" id="sem-ingresso">\n  <div class="bloco-head"><h2>Os %d pontos que não '
                  'cobram nada</h2></div>\n  <p style="color:var(--nevoa)">%s. Não há meia nem tarifa de morador '
                  'porque não há ingresso. O que cada um cobra à parte está na <a href="../../../gratis/#rio-de-janeiro">'
                  'lista dos pontos gratuitos</a>.</p>\n</section>\n\n' % (len(gratis), junta(nomes_gratis)))

    perguntas = [
        ("Morador do Rio tem desconto no Pão de Açúcar?",
         dict(DESCONTOS["morar"])["pao-de-acucar"]),
        ("Morador do Rio tem desconto no Cristo Redentor?",
         dict(DESCONTOS["morar"])["cristo-redentor"] + " O que muda o preço é o embarque: "
         + minuscula(dict(DESCONTOS["dia"])["cristo-redentor"])),
        ("Que museus do Rio são de graça em algum dia?",
         "No MAR, %s No Museu do Amanhã, %s" % (minuscula(dict(DESCONTOS["dia"])["mar"]),
                                                 minuscula(dict(DESCONTOS["dia"])["museu-do-amanha"]))),
        ("Brasileiro paga menos que estrangeiro no Rio?",
         "No Pão de Açúcar, a tarifa para brasileiro é R$ %s, contra R$ %s da inteira. No Jardim Botânico, %s"
         % (pao_br, pao_int, minuscula(dict(DESCONTOS["morar"])["jardim-botanico"]))),
        ("Quais pontos do Rio não cobram entrada?",
         "%d dos 16 pontos do guia: %s." % (len(gratis), junta(nomes_gratis))),
    ]

    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Destinos", "item": SITE + "/destinos/"},
        {"@type": "ListItem", "position": 3, "name": "Rio de Janeiro", "item": SITE + "/destinos/rio-de-janeiro/"},
        {"@type": "ListItem", "position": 4, "name": "Descontos", "item": url}]}
    cabeca, pe = esqueleto(titulo, descricao, url, img, alt)
    cabeca = cabeca.replace("</head>", ld(faq_ld(perguntas)) + ld(migalhas) + "</head>", 1)

    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">Pão de Açúcar, morando no RJ</span><span class="big c">R$ %s</span>'
        '<span class="sub">Contra R$ %s da inteira.</span></div>'
        '<div class="pcel"><span class="rotp">MAR, às terças</span><span class="big c">Grátis</span>'
        '<span class="sub">Para todos, sem comprovar nada.</span></div>'
        '<div class="pcel"><span class="rotp">Museu do Amanhã, todo dia 10</span><span class="big">R$ %s</span>'
        '<span class="sub">E grátis nos feriados nacionais.</span></div>'
        '<div class="pcel"><span class="rotp">Cristo, saindo das Paineiras</span><span class="big">R$ %s</span>'
        '<span class="sub">R$ %d a menos que a van da cidade.</span></div>'
        '</div>' % (pao_rj, pao_int, amanha_dez, van_p, int(van_c) - int(van_p)))

    partes = [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="%s">Início</a> › <a href="../../">Destinos</a> › '
        '<a href="../">Rio de Janeiro</a> › Descontos</p>\n' % SOBE,
        '<div class="hero">\n  <span class="eyebrow">Quem paga menos</span>\n'
        '  <h1>Onde morador e brasileiro pagam menos no Rio</h1>\n'
        '  <p>Tarifa de morador, desconto para brasileiro, dia grátis e meia-entrada nos pontos pagos do guia, '
        'e onde o desconto que todo mundo procura não existe. Cada linha leva à ficha do ponto, com a fonte. '
        'Preços apurados em %s.</p>\n'
        '<p class="assinatura">Apurado por <a href="%ssobre/#quem-faz">Allan Vitor</a> · '
        '<a href="https://www.instagram.com/viagemnalupabr/" target="_blank" rel="noopener">@viagemnalupabr'
        '<span class="so-leitor"> (abre em outra aba)</span></a></p>\n</div>\n' % (data_ap, SOBE),
        capa, "\n", painel, '\n<div style="height:clamp(1.4rem,3vw,2.2rem)"></div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
    ] + secoes + [
        faq_html(perguntas, "descontos no Rio"), "\n",
        continua("descontos"),
        reserva(guia, "descontos", "Leve o documento de cada desconto: sem ele, a bilheteria cobra a inteira ou a "
                                   "diferença. "),
        '</div>\n',
    ]
    return os.path.join(RAIZ, "destinos", "rio-de-janeiro", "descontos", "index.html"), \
        cabeca + "".join(partes) + pe


def liga_descontos_no_guia(h):
    if 'href="descontos/"' in h:
        return h
    pg = '<a class="pg" href="descontos/">Onde morador e brasileiro pagam menos</a>'
    h = re.sub(r'(<h2>As outras páginas do Rio de Janeiro</h2></div>\s*<div class="paginas">)',
               r"\1 " + pg, h, count=1)
    mais = '<p><a href="descontos/">Todos os descontos dos pontos do Rio, numa página só</a>.</p>'
    return re.sub(r"(Onde ser brasileiro, ou morar no Rio, corta o preço pela metade.*?)(</details>)",
                  lambda m: m.group(1) + mais + m.group(2), h, count=1, flags=re.S)


# --------------------------------------------------------------- Quando ir
def confere_sazonal():
    """A serie do sazonal.py contra o texto extraido do PDF da FOHB."""
    import sazonal
    txt = le(os.path.join(AQUI, "fontes", "fohb-panorama-20-rio.txt"))
    trecho = acha(r"ACUMULADO 2025\s*(.*?)0%\s*\n10%", txt, "a serie mensal no texto da FOHB").group(1)
    nums = re.findall(r"\d+%?", trecho)
    diarias = [int(n) for n in nums if not n.endswith("%")][:12]
    ocup = [int(n[:-1]) for n in nums if n.endswith("%")][:12]
    if diarias != [m[1] for m in sazonal.MESES] or ocup != [m[2] for m in sazonal.MESES]:
        sys.exit("PARADO: sazonal.py nao bate com o texto da FOHB (%s / %s)" % (diarias, ocup))
    media = acha(r"\n(\d+) (\d+) (\d+)\d{3} \d{3} \d{3}\n", txt, "a media anual na pagina 30").group(3)
    if int(media) != sazonal.MEDIA_ANO:
        sys.exit("PARADO: a media anual (%s) nao bate com sazonal.py" % media)
    return sazonal


def faixa_de_meses(nomes, todos):
    """['maio','junho','julho'] -> 'de maio a julho' quando contiguos."""
    idx = [todos.index(n) for n in nomes]
    if len(idx) > 2 and idx == list(range(idx[0], idx[-1] + 1)):
        return "de %s a %s" % (nomes[0], nomes[-1])
    return junta(nomes)


def quando_ir(guia):
    sz = confere_sazonal()
    from g2 import G2
    from g4 import G4
    custos = le(os.path.join(RAIZ, "destinos", "rio-de-janeiro", "quanto-custa", "index.html"))
    carn_mes, carn_pico = acha(r"Carnaval de 2026 a diária média do mês foi a R\$ ([\d.]+)</b>, e a <b>noite de "
                               r"pico a R\$ ([\d.]+)", custos, "o Carnaval na ficha de custos").groups()
    rev_ocup = acha(r"ocupação hoteleira medida foi de ([\d,]+%)", custos, "o Reveillon na ficha de custos").group(1)
    cristo_f = limpa(ponto("cristo-redentor")["campos"]["Menor visitação e temperatura"])
    ferias = acha(r"(julho é mês de férias escolares brasileiras, então o movimento sobe)", cristo_f,
                  "as ferias de julho na ficha do Cristo").group(1)
    from g3 import G3
    theatro = [p for p in G3["pontos"] if p["id"] == "theatro-municipal"][0]
    acha(r"(Theatro costuma reforçar a programação)", limpa(theatro["campos"]["Menor visitação e temperatura"]),
         "a programacao de julho do Theatro")
    acha(r"(março e abril, impulsionados\s+pelo Carnaval e por grandes shows)",
         le(os.path.join(AQUI, "fontes", "fohb-panorama-20-rio.txt")), "o motivo do pico no relatorio")
    bonde = [p for p in G4["pontos"] if p["id"] == "santa-teresa-bonde"][0]
    acha(r"(julho é alta temporada para o bonde)", limpa(bonde["campos"]["Menor visitação e temperatura"]),
         "o recorde de julho do bonde")

    M = sz.MESES
    nomes = [m[0] for m in M]
    barato = min(M, key=lambda m: m[1])
    caro = max(M, key=lambda m: m[1])
    seco = min(M, key=lambda m: m[5])
    chuvoso = max(M, key=lambda m: m[5])
    frio = min(M, key=lambda m: m[3])
    LIMITE = 70
    janela = [m for m in M if m[1] < sz.MEDIA_ANO and m[5] < LIMITE]
    abaixo = [m[0] for m in M if m[1] < sz.MEDIA_ANO]
    vazio = min(M, key=lambda m: m[2])
    julho = M[nomes.index("julho")]
    junho = M[nomes.index("junho")]
    mais_cheios = sum(1 for m in M if m[2] > julho[2])
    url = "%s/destinos/rio-de-janeiro/quando-ir/" % SITE

    titulo = "Quando ir ao Rio de Janeiro: diária, chuva e temperatura mês a mês"
    descricao = ("A diária média do Rio vai de R$ %d em %s a R$ %d em %s, e a chuva de %d mm em %s a %d mm em %s. "
                 "Os 12 meses lado a lado, com Carnaval e Réveillon à parte. Dados FOHB 2025 e Climatempo."
                 % (barato[1], barato[0], caro[1], caro[0], seco[5], seco[0], chuvoso[5], chuvoso[0]))
    capa, img, alt = capa_de("copacabana")

    def linha(m):
        def neg(v, alvo):
            return "<b>%s</b>" % v if alvo else v
        return ('<tr><td>%s</td><td class="n">%s</td><td class="n">%d%%</td><td class="n">%d° / %d°</td>'
                '<td class="n">%s</td></tr>'
                % (m[0].capitalize(), neg("R$ %d" % m[1], m in (barato, caro)), m[2], m[3], m[4],
                   neg("%d mm" % m[5], m in (seco, chuvoso))))
    tabela = "".join(linha(m) for m in M)

    janela_txt = faixa_de_meses([m[0] for m in janela], nomes)
    perguntas = [
        ("Qual é o mês mais barato para ir ao Rio de Janeiro?",
         "Pela diária de hotel, %s: R$ %d em média em 2025, contra R$ %d de média do ano e R$ %d em %s, o mais "
         "caro. Ficam abaixo da média do ano %s." % (barato[0], barato[1], sz.MEDIA_ANO, caro[1], caro[0],
                                                    faixa_de_meses(abaixo, nomes) if len(abaixo) > 2 else junta(abaixo))),
        ("Qual é o mês com menos chuva no Rio?",
         "%s, com %d mm na média de 30 anos. O mais chuvoso é %s, com %d mm." % (seco[0].capitalize(), seco[5],
                                                                            chuvoso[0], chuvoso[5])),
        ("Qual é a melhor época para ir ao Rio de Janeiro?",
         "Se o critério é pagar menos e pegar menos chuva, %s: são os meses com diária abaixo da média do ano "
         "(R$ %d) e menos de %d mm de chuva. A ressalva é julho, mês de férias escolares, em que as atrações "
         "enchem mais." % (janela_txt, sz.MEDIA_ANO, LIMITE)),
        ("Vale a pena ir ao Rio em julho?",
         "Pelo preço e pelo clima, sim: diária média de R$ %d, %d mm de chuva e %d° a %d°. Mas é mês de férias "
         "escolares: a ocupação dos hotéis passa de %d%% em junho para %d%% em julho, e atrações como o bonde de "
         "Santa Teresa têm em julho a sua alta temporada." % (julho[1], julho[5], julho[3], julho[4],
                                                              junho[2], julho[2])),
        ("Quanto custa a diária no Carnaval do Rio?",
         "No Carnaval de 2026 a diária média do mês foi a R$ %s, e a noite de pico a R$ %s, contra R$ %d de média "
         "do ano. No Réveillon a ocupação medida foi de %s, e ninguém publica a diária só da noite da virada."
         % (carn_mes, carn_pico, sz.MEDIA_ANO, rev_ocup)),
    ]

    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Destinos", "item": SITE + "/destinos/"},
        {"@type": "ListItem", "position": 3, "name": "Rio de Janeiro", "item": SITE + "/destinos/rio-de-janeiro/"},
        {"@type": "ListItem", "position": 4, "name": "Quando ir", "item": url}]}
    cabeca, pe = esqueleto(titulo, descricao, url, img, alt)
    cabeca = cabeca.replace("</head>", ld(faq_ld(perguntas)) + ld(migalhas) + "</head>", 1)

    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">Diária mais baixa</span><span class="big c">R$ %d</span>'
        '<span class="sub">%s, média dos hotéis em 2025.</span></div>'
        '<div class="pcel"><span class="rotp">Diária mais alta</span><span class="big">R$ %d</span>'
        '<span class="sub">%s. A média do ano foi R$ %d.</span></div>'
        '<div class="pcel"><span class="rotp">Mês mais seco</span><span class="big c">%d mm</span>'
        '<span class="sub">%s, média de 30 anos.</span></div>'
        '<div class="pcel"><span class="rotp">Mês mais chuvoso</span><span class="big">%d mm</span>'
        '<span class="sub">%s.</span></div>'
        '</div>' % (barato[1], barato[0].capitalize(), caro[1], caro[0].capitalize(), sz.MEDIA_ANO,
                    seco[5], seco[0].capitalize(), chuvoso[5], chuvoso[0].capitalize()))

    clima_risco = "".join(
        '<li><a href="../#%s"><b>%s</b></a>: %s.</li>' % (pid, H.escape(ponto(pid)["nome"]), CALENDARIO[pid][2])
        for pid in ("cristo-redentor", "pao-de-acucar"))

    partes = [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="%s">Início</a> › <a href="../../">Destinos</a> › '
        '<a href="../">Rio de Janeiro</a> › Quando ir</p>\n' % SOBE,
        '<div class="hero">\n  <span class="eyebrow">O ano inteiro</span>\n'
        '  <h1>Quando ir ao Rio de Janeiro, mês a mês</h1>\n'
        '  <p>A diária média dos hotéis, a ocupação, a temperatura e a chuva dos 12 meses, lado a lado. No Rio a '
        'hospedagem é a maior parte da conta, então o mês pesa mais que qualquer outra escolha, e duas semanas do '
        'ano fogem de qualquer média.</p>\n'
        '<p class="assinatura">Apurado por <a href="%ssobre/#quem-faz">Allan Vitor</a> · '
        '<a href="https://www.instagram.com/viagemnalupabr/" target="_blank" rel="noopener">@viagemnalupabr'
        '<span class="so-leitor"> (abre em outra aba)</span></a></p>\n</div>\n' % SOBE,
        capa, "\n", painel, '\n<div style="height:clamp(1.4rem,3vw,2.2rem)"></div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
        '<section class="bloco"><div class="aviso a"><span class="t">Carnaval e Réveillon não cabem na média do mês'
        '</span><p><b>No Carnaval de 2026 a diária média do mês foi a R$ %s</b>, e a <b>noite de pico a R$ %s</b>, '
        'contra R$ %d de média do ano. No Réveillon a ocupação medida foi de <b>%s</b>, e ninguém publica a '
        'diária só da noite da virada. Os números estão na <a href="../quanto-custa/#quando-ir">ficha de '
        'custos</a>.</p></div></section>\n\n' % (carn_mes, carn_pico, sz.MEDIA_ANO, rev_ocup),
        '<section class="bloco" id="mes-a-mes">\n  <div class="bloco-head"><span class="eyebrow">Os 12 meses'
        '</span><h2>Diária, ocupação, temperatura e chuva</h2></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Mês</th><th>Diária média</th><th>Ocupação</th>'
        '<th>Mín. / máx.</th><th>Chuva</th></tr></thead><tbody>%s</tbody></table></div>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem"><b>Diária e ocupação:</b> %s. É a média dos hotéis '
        'filiados na cidade inteira, sem recorte por bairro, e é 2025, não previsão para o ano que vem. '
        '<b>Temperatura e chuva:</b> %s.</p>\n</section>\n\n' % (tabela, H.escape(sz.FONTE_DIARIA), H.escape(sz.FONTE_CLIMA)),
        '<section class="bloco" id="melhor-epoca">\n  <div class="bloco-head"><span class="eyebrow">A conta do '
        'calendário</span><h2>Quando o preço e a chuva caem juntos</h2></div>\n'
        '  <p style="color:var(--nevoa)"><b>%s</b> são os meses com diária abaixo da média do ano (R$ %d) e '
        'menos de %d mm de chuva. O mais barato é %s, a R$ %d; o mais seco, %s, com %d mm; o mais frio, %s, com '
        'mínima de %d°.</p>\n'
        '  <p style="color:var(--nevoa)">O mês mais vazio nos hotéis foi %s, com %d%% de ocupação. '
        'O mais caro foi %s, a R$ %d; o relatório atribui o pico de março e abril ao Carnaval e a grandes '
        'shows.</p>\n</section>\n\n'
        % (janela_txt.capitalize(), sz.MEDIA_ANO, LIMITE, barato[0], barato[1], seco[0], seco[5], frio[0], frio[3],
           vazio[0], vazio[2], caro[0], caro[1]),
        '<section class="bloco" id="julho">\n  <div class="bloco-head"><span class="eyebrow">A exceção</span>'
        '<h2>Julho: barato e seco, mas com férias escolares</h2></div>\n'
        '  <p style="color:var(--nevoa)">Diária de R$ %d, %d mm de chuva e %d° a %d°. Nos hotéis, a ocupação '
        'passa de %d%% em junho para %d%% em julho, ainda menor que a de %d dos outros meses. Quem sente mais as '
        'férias são as atrações: o bonde de Santa Teresa tem em julho a sua alta temporada, e o Theatro Municipal '
        'reforça a programação. Para o mesmo clima com menos gente, %s teve a menor ocupação do ano, %d%%.</p>\n'
        '</section>\n\n'
        % (julho[1], julho[5], julho[3], julho[4], junho[2], julho[2], mais_cheios, vazio[0], vazio[2]),
        '<section class="bloco" id="clima-fecha">\n  <div class="bloco-head"><span class="eyebrow">Chuva não é só '
        'desconforto</span><h2>Os dois pontos que o tempo fecha</h2></div>\n'
        '  <ul class="plain">%s</ul>\n  <p style="color:var(--nevoa)">Nos meses de mais chuva, deixe uma folga no '
        'roteiro para esses dois. <a href="../o-que-fecha-cada-dia/">O que fecha em cada dia da semana</a> está '
        'em outra página.</p>\n</section>\n\n' % clima_risco,
        '<section class="bloco" id="lacunas">\n  <div class="bloco-head"><span class="eyebrow">O que não '
        'sabemos</span><h2>As lacunas</h2></div>\n  <ul class="plain">'
        '<li>Nenhum dos 16 pontos do guia publica visitação mês a mês. O movimento por mês sai da ocupação dos '
        'hotéis, não das bilheterias.</li>'
        '<li>A diária não tem recorte por bairro: Copacabana, Ipanema, Botafogo e Centro não aparecem '
        'separados.</li>'
        '<li>A diária da noite do Réveillon não é publicada por ninguém.</li></ul>\n</section>\n\n',
        faq_html(perguntas, "quando ir ao Rio"), "\n",
        continua("quando-ir"),
        reserva(guia, "quando-ir", "Com a data escolhida, compare a diária da sua semana com a média do mês "
                                   "nesta tabela. "),
        '</div>\n',
    ]
    return os.path.join(RAIZ, "destinos", "rio-de-janeiro", "quando-ir", "index.html"), \
        cabeca + "".join(partes) + pe


def liga_quando_no_guia(h):
    if 'href="quando-ir/"' in h:
        return h
    pg = '<a class="pg" href="quando-ir/">Quando ir, mês a mês</a>'
    return re.sub(r'(<h2>As outras páginas do Rio de Janeiro</h2></div>\s*<div class="paginas">)',
                  r"\1 " + pg, h, count=1)


def liga_quando_na_ficha(h):
    if 'href="../quando-ir/"' in h:
        return h
    mais = ('<p style="color:var(--nevoa)"><a href="../quando-ir/">Os 12 meses lado a lado, com diária, ocupação, '
            'temperatura e chuva</a>.</p>')
    return re.sub(r'(<section class="bloco" id="quando-ir">.*?)(\n</section>)', lambda m: m.group(1) + mais + m.group(2),
                  h, count=1, flags=re.S)


# --------------------------------------------- O que fecha cada dia
#
# A ficha guarda horario em prosa, e prosa nao vira tabela sozinha. Aqui
# cada ponto tem a LEITURA da ficha (que dia fecha, que dia abre pela
# metade) e as PROVAS: trechos que precisam estar no campo "Dias em que
# nao funciona" daquela ficha. Se a ficha mudar e a prova sumir, o script
# para - a tabela nunca descola do guia em silencio.
#
# Dia nao citado = abre. Feriado so conta como aberto quando a ficha diz;
# quando nao diz, e "duvida" com a lacuna escrita.
DIAS = ["seg", "ter", "qua", "qui", "sex", "sab", "dom", "fer"]
NOME_DIA = {"seg": "Segunda-feira", "ter": "Terça-feira", "qua": "Quarta-feira", "qui": "Quinta-feira",
            "sex": "Sexta-feira", "sab": "Sábado", "dom": "Domingo", "fer": "Feriado"}
CURTO = {"seg": "Seg", "ter": "Ter", "qua": "Qua", "qui": "Qui", "sex": "Sex", "sab": "Sáb",
         "dom": "Dom", "fer": "Feriado"}
SEM_FERIADO = "a ficha não diz se abre no feriado"

CALENDARIO = {
 "cristo-redentor": ({}, ["Não há dia fixo de fechamento semanal", "inclusive feriados"],
                     "chuva, vento e neblina suspendem o acesso em qualquer dia"),
 "pao-de-acucar": ({}, ["Abre todos os dias", "feriados incluídos"],
                   "raio e vento forte param os bondinhos em qualquer dia"),
 "vista-chinesa": ({d: ("parcial", "não se sobe de carro, táxi nem aplicativo das 7h às 19h, só a pé ou de bicicleta")
                    for d in ("sab", "dom", "fer")},
                   ["sem dia fixo de fechamento semanal", "entre 7h e 19h aos finais de semana e feriados"], ""),
 "parque-lage": ({"fer": ("duvida", SEM_FERIADO)}, ["Não há dia fixo de fechamento semanal"],
                 "o palacete está fechado em obra todos os dias; só os jardins abrem"),
 "copacabana": ({}, ["todos os dias do ano"], ""),
 "ipanema-arpoador": ({}, ["acesso livre 24 horas"], "a Pedra do Arpoador fecha às 21h todos os dias"),
 "jardim-botanico": ({"qua": ("parcial", "o Arboreto só abre às 11h e o Museu fecha")},
                     ["na quarta-feira, 11h às 17h", "na quarta-feira fica fechado", "Feriados: funcionamento normal"],
                     ""),
 "floresta-da-tijuca": ({}, ["Não fecha em nenhum dia da semana", "feriados inclusive"], ""),
 "museu-do-amanha": ({"qua": ("fecha", "")}, ["Fecha às quartas-feiras", "feriados inclusive"], ""),
 "mar": ({"qua": ("fecha", ""), "seg": ("duvida", "as fontes do próprio museu divergem sobre a segunda"),
          "fer": ("duvida", SEM_FERIADO)},
         ["Fecha às quartas-feiras", "a abertura de segunda-feira fica em dúvida"], ""),
 "theatro-municipal": ({"dom": ("fecha", "sem visita guiada"), "seg": ("fecha", "sem visita guiada"),
                        "ter": ("fecha", "sem visita guiada; só instituições com agendamento"),
                        "fer": ("duvida", "não encontrado calendário de feriado")},
                       ["Não há visitas de domingo a terça-feira", "Não encontrado calendário de fechamento por feriado"],
                       "a visita guiada é o que se visita; fora dela, só com ingresso de espetáculo"),
 "real-gabinete": ({d: ("fecha", "") for d in ("sab", "dom", "fer")},
                   ["Fechado aos sábados, domingos e feriados"], ""),
 "escadaria-selaron": ({}, ["Logradouro público, sem portão e sem horário"], ""),
 "santa-teresa-bonde": ({d: ("parcial", "o ramal Silvestre não opera, e os outros dois rodam das 9h às 17h")
                         for d in ("sab", "dom", "fer")},
                        ["Não opera aos sábados, domingos e feriados", "sábados, domingos e feriados das 9h às 17h"], ""),
 "lapa-arcos": ({}, ["Praça pública, aberta 24 horas"], ""),
 "maracana": ({"fer": ("duvida", SEM_FERIADO)}, ["Não há fechamento fixo semanal"],
              "em dia de jogo o tour encurta, e pode nem abrir"),
}

# Tres endereços que nao tem ficha no guia, mas que o aviso "O calendario
# do Centro" cita. Entram como lista a parte, com a prova no aviso.
FORA = [
 ("Forte de Copacabana", {"seg": "fecha"}, "<b>Segunda-feira:</b> fecham o Forte de Copacabana"),
 ("Parque das Ruínas, em Santa Teresa", {"seg": "fecha"}, "e o Parque das Ruínas, em Santa Teresa"),
 ("Museu da Chácara do Céu", {"ter": "fecha", "dom": "fecha", "fer": "fecha"},
  "<b>Terça, domingo e feriado:</b> fecha o Museu da Chácara do Céu"),
]

ROTULO = {"abre": "Abre", "fecha": "Fecha", "parcial": "Em parte", "duvida": "?"}


def junta(itens):
    itens = list(itens)
    if len(itens) <= 1:
        return "".join(itens)
    return ", ".join(itens[:-1]) + " e " + itens[-1]


def que_fecha(guia):
    from g2 import G2
    from g3 import G3
    from g4 import G4
    grupos = [G1, G2, G3, G4]
    pontos = [p for g in grupos for p in g["pontos"]]
    if set(CALENDARIO) != {p["id"] for p in pontos}:
        sys.exit("PARADO: CALENDARIO e as fichas nao tem os mesmos pontos: %s"
                 % sorted(set(CALENDARIO) ^ {p["id"] for p in pontos}))
    for p in pontos:
        regras, provas, _ = CALENDARIO[p["id"]]
        texto = limpa(p["campos"]["Dias em que não funciona"])
        for pr in provas:
            if pr not in texto:
                sys.exit("PARADO: a ficha de %s nao diz mais '%s'" % (p["id"], pr))
    calendario = acha(r'(?s)O calendário do Centro.*?</details>', guia, "o aviso do calendario do Centro").group(0)
    for nome, _, prova in FORA:
        if prova not in calendario:
            sys.exit("PARADO: o aviso do Centro nao cita mais '%s'" % nome)
    data_ap = acha(r"Preços verificados em (\d+ de \w+ de \d{4})", guia, "a data do guia").group(1)

    def estado(pid, d):
        return CALENDARIO[pid][0].get(d, ("abre", ""))

    url = "%s/destinos/rio-de-janeiro/o-que-fecha-cada-dia/" % SITE
    centro = [p for p in G3["pontos"]]
    dias_centro = [d for d in DIAS[:7] if all(estado(p["id"], d)[0] == "abre" for p in centro)]
    nomes_centro = [p["nome"] for p in centro]

    # ------------------------------------------------- por dia
    def do_dia(d):
        fecha = [(p, estado(p["id"], d)[1]) for p in pontos if estado(p["id"], d)[0] == "fecha"]
        parte = [(p, estado(p["id"], d)[1]) for p in pontos if estado(p["id"], d)[0] == "parcial"]
        duvida = [(p, estado(p["id"], d)[1]) for p in pontos if estado(p["id"], d)[0] == "duvida"]
        fora = [n for n, regra, _ in FORA if regra.get(d) == "fecha"]
        return fecha, parte, duvida, fora

    def item(p, nota):
        return '<a href="../#%s">%s</a>%s' % (p["id"], H.escape(p["nome"]), (" — " + nota) if nota else "")

    secoes = []
    for d in DIAS:
        fecha, parte, duvida, fora = do_dia(d)
        abre = len(pontos) - len(fecha) - len(parte) - len(duvida)
        li = []
        if fecha:
            li.append("<li><b>Fecha:</b> %s.</li>" % "; ".join(item(p, n) for p, n in fecha))
        if parte:
            li.append("<li><b>Abre em parte:</b> %s.</li>" % "; ".join(item(p, n) for p, n in parte))
        if duvida:
            li.append('<li><b>Sem confirmação:</b> %s. <span class="flag">Não encontrado</span></li>'
                      % "; ".join(item(p, n) for p, n in duvida))
        if fora:
            li.append("<li><b>Fora dos 16 pontos do guia, também fecha:</b> %s.</li>" % junta(fora))
        if not li:
            li.append("<li>Nenhum dos 16 pontos fecha.</li>")
        li.append("<li><b>Abrem normalmente:</b> %d dos %d pontos.</li>" % (abre, len(pontos)))
        if d in dias_centro:
            li.append("<li>É um dos dias com <b>os quatro endereços do Centro abertos</b>.</li>")
        secoes.append('<section class="bloco" id="%s">\n  <div class="bloco-head"><h2>%s</h2></div>\n'
                      '  <ul class="plain">%s</ul>\n</section>\n\n' % (d, NOME_DIA[d], "".join(li)))

    # ------------------------------------------------- a tabela
    def celula(pid, d):
        e, nota = estado(pid, d)
        rot = ROTULO[e]
        tit = (' title="%s"' % H.escape(nota, quote=True)) if nota else ""
        if e == "abre":
            return '<td class="n" style="color:var(--nevoa)">%s</td>' % rot
        if e == "fecha":
            return '<td class="n"%s><b style="color:var(--ambar)">%s</b></td>' % (tit, rot)
        return '<td class="n"%s><b>%s</b></td>' % (tit, rot)
    cab = "".join("<th>%s</th>" % CURTO[d] for d in DIAS)
    linhas = "".join('<tr><td><a href="../#%s">%s</a></td>%s</tr>'
                     % (p["id"], H.escape(p["nome"]), "".join(celula(p["id"], d) for d in DIAS)) for p in pontos)
    ressalvas = [(p, CALENDARIO[p["id"]][2]) for p in pontos if CALENDARIO[p["id"]][2]]

    # ------------------------------------------------- textos derivados
    f_seg, f_qua, f_sab = do_dia("seg"), do_dia("qua"), do_dia("sab")
    nomes = lambda lst: [p["nome"] for p, _ in lst]
    titulo = "O que abre e o que fecha no Rio de Janeiro em cada dia da semana"
    descricao = ("Segunda, quarta e fim de semana fecham pontos diferentes no Rio. Quarta fecham %s; "
                 "sábado e domingo, o %s. %s são os únicos dias com o Centro todo aberto. "
                 "16 pontos, horários apurados em %s."
                 % (junta(nomes(f_qua[0])), junta(nomes(f_sab[0])),
                    junta(NOME_DIA[d].split("-")[0] for d in dias_centro).capitalize(), data_ap))
    img_id = "gabinete"
    cred = json.loads(le(os.path.join(AQUI, "creditos.json")))[img_id]
    credito = ('Foto: %s · <a href="%s" target="_blank" rel="noopener license">%s</a> · '
               '<a href="%s" target="_blank" rel="noopener">Wikimedia Commons</a> · recortada'
               % (H.escape(cred["autor"]), cred["licurl"], cred["lic"], cred["pagina"]))
    base_img = SOBE + "assets/img/rio-de-janeiro/" + img_id
    capa = ('<figure class="hero-capa">\n  <img fetchpriority="high" srcset="%(b)s-400.webp 400w, %(b)s-640.webp 640w, '
            '%(b)s-820.webp 820w, %(b)s.webp 1200w" sizes="(min-width:1080px) 820px, 100vw" src="%(b)s.webp" '
            'alt="%(alt)s" width="1200" height="675" decoding="async">\n  <figcaption><p class="foto-cred">%(c)s'
            '</p></figcaption>\n</figure>' % dict(b=base_img, alt=H.escape(cred["alt"], quote=True), c=credito))
    img = "%s/assets/img/rio-de-janeiro/%s.webp" % (SITE, img_id)

    quem_seg = "; ".join("%s, %s" % (p["nome"], n) if n else p["nome"] for p, n in f_seg[0]) or "nenhum fecha"
    perguntas = [
        ("O que fecha na segunda-feira no Rio de Janeiro?",
         "Dos 16 pontos do guia: %s. Fora deles, o guia avisa que fecham o %s. %s"
         % (quem_seg, junta(f_seg[3]),
            ("O MAR não está confirmado: %s." % estado("mar", "seg")[1]) if estado("mar", "seg")[0] == "duvida" else "")),
        ("Quais museus do Rio fecham na quarta-feira?",
         "%s fecham na quarta. No Jardim Botânico, %s."
         % (junta(nomes(f_qua[0])), estado("jardim-botanico", "qua")[1])),
        ("O que fecha no fim de semana no Rio?",
         "O %s fecha sábado, domingo e feriado. No domingo também não há visita guiada no Theatro Municipal. "
         "Na Vista Chinesa, %s; no bonde de Santa Teresa, %s."
         % (junta(nomes(f_sab[0])), estado("vista-chinesa", "sab")[1], estado("santa-teresa-bonde", "sab")[1])),
        ("Qual é o melhor dia para visitar o Centro do Rio?",
         "%s: são os únicos dias em que %s estão abertos ao mesmo tempo."
         % (junta(NOME_DIA[d].lower() for d in dias_centro).capitalize(), junta(nomes_centro))),
        ("O que abre no feriado no Rio?",
         "Fecham no feriado: %s. Sem confirmação na ficha: %s. Os demais pontos abrem."
         % (junta(nomes(do_dia("fer")[0]) + do_dia("fer")[3]), junta(nomes(do_dia("fer")[2])))),
    ]

    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Destinos", "item": SITE + "/destinos/"},
        {"@type": "ListItem", "position": 3, "name": "Rio de Janeiro", "item": SITE + "/destinos/rio-de-janeiro/"},
        {"@type": "ListItem", "position": 4, "name": "O que fecha cada dia", "item": url}]}
    cabeca, pe = esqueleto(titulo, descricao, url, img, cred["alt"])
    cabeca = cabeca.replace("</head>", ld(faq_ld(perguntas)) + ld(migalhas) + "</head>", 1)

    idx = " · ".join('<a href="#%s">%s</a>' % (d, CURTO[d]) for d in DIAS)
    partes = [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="%s">Início</a> › <a href="../../">Destinos</a> › '
        '<a href="../">Rio de Janeiro</a> › O que fecha cada dia</p>\n' % SOBE,
        '<div class="hero">\n  <span class="eyebrow">Calendário da semana</span>\n'
        '  <h1>O que abre e o que fecha no Rio em cada dia da semana</h1>\n'
        '  <p>Os %d pontos do guia, dia por dia: o que fecha, o que abre só em parte e o que não foi possível '
        'confirmar. Montar o roteiro no dia errado custa um dia inteiro, e no Rio cada endereço fecha num dia '
        'diferente. Horários apurados em %s.</p>\n'
        '<p class="assinatura">Apurado por <a href="%ssobre/#quem-faz">Allan Vitor</a> · '
        '<a href="https://www.instagram.com/viagemnalupabr/" target="_blank" rel="noopener">@viagemnalupabr'
        '<span class="so-leitor"> (abre em outra aba)</span></a></p>\n</div>\n' % (len(pontos), data_ap, SOBE),
        capa, '\n<div style="height:clamp(1.4rem,3vw,2.2rem)"></div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
        '<section class="bloco"><div class="aviso a"><span class="t">O resumo</span>'
        '<p><b>%s são os únicos dias com os quatro endereços do Centro abertos</b>: %s.</p>'
        '<p><b>Quarta-feira</b> fecham %s. <b>Sábado, domingo e feriado</b> fecha o %s. '
        '<b>De domingo a terça</b> não há visita guiada no Theatro Municipal.</p></div></section>\n\n'
        % (junta(NOME_DIA[d].lower() for d in dias_centro).capitalize(), junta(nomes_centro), junta(nomes(f_qua[0])),
           junta(nomes(f_sab[0]))),
        '<section class="bloco">\n  <div class="bloco-head"><span class="eyebrow">Ir para o dia</span>'
        '<h2>Dia por dia</h2></div>\n  <p class="idx-gratis">%s</p>\n</section>\n\n' % idx,
    ] + secoes + [
        '<section class="bloco" id="tabela">\n  <div class="bloco-head"><span class="eyebrow">Os 16 pontos</span>'
        '<h2>A semana inteira numa tabela</h2></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Ponto</th>%s</tr></thead><tbody>%s</tbody></table></div>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem">“Em parte”: abre com restrição de horário, de acesso ou de '
        'ramal, explicada na seção do dia. “?”: a ficha não confirma, e a lacuna fica escrita. Cada nome leva à '
        'ficha do ponto no guia, com a fonte e o horário completo.</p>\n</section>\n\n' % (cab, linhas),
        '<section class="bloco" id="em-qualquer-dia">\n  <div class="bloco-head"><span class="eyebrow">Fora do '
        'calendário</span><h2>O que fecha em qualquer dia</h2></div>\n  <ul class="plain">%s</ul>\n</section>\n\n'
        % "".join("<li>%s — %s.</li>" % (item(p, ""), n) for p, n in ressalvas),
        faq_html(perguntas, "o que fecha no Rio"), "\n",
        continua("o-que-fecha-cada-dia"),
        '</div>\n',
    ]
    return os.path.join(RAIZ, "destinos", "rio-de-janeiro", "o-que-fecha-cada-dia", "index.html"), \
        cabeca + "".join(partes) + pe


# ------------------------------------------------- os links no guia
def liga_no_roteiro(h):
    if 'href="../o-que-fecha-cada-dia/"' in h:
        return h
    mais = ('<p><a href="../o-que-fecha-cada-dia/">A semana inteira, ponto por ponto: o que abre e o que fecha '
            'em cada dia</a>.</p>')
    return re.sub(r"(As regras que sustentam esta ordem</span>.*?<p><b>O dia 4 só existe.*?</p>)",
                  lambda m: m.group(1) + mais, h, count=1, flags=re.S)


def liga_fecha_no_guia(h):
    if 'href="o-que-fecha-cada-dia/"' in h:
        return h
    pg = '<a class="pg" href="o-que-fecha-cada-dia/">O que abre e fecha em cada dia</a>'
    h = re.sub(r'(<h2>As outras páginas do Rio de Janeiro</h2></div>\s*<div class="paginas">)',
               r"\1 " + pg, h, count=1)
    mais = '<p><a href="o-que-fecha-cada-dia/">A tabela da semana inteira, com os 16 pontos</a>.</p>'
    return re.sub(r"(O calendário do Centro.*?)(</details>)", lambda m: m.group(1) + mais + m.group(2),
                  h, count=1, flags=re.S)


def liga_no_guia(h):
    pg = '<a class="pg" href="cristo-redentor/">Cristo Redentor: ingresso e como subir</a>'
    if 'href="cristo-redentor/"' not in h:
        h = re.sub(r'(<h2>As outras páginas do Rio de Janeiro</h2></div>\s*<div class="paginas">)',
                   r"\1 " + pg, h, count=1)
        mais = ('\n  <p class="foto-nota"><a href="cristo-redentor/">Página completa do Cristo Redentor: '
                'as formas de subir lado a lado, a obra e as perguntas frequentes</a></p>')
        h = re.sub(r'(<article class="ponto" id="cristo-redentor">.*?)(\n</article>)',
                   lambda m: m.group(1) + mais + m.group(2), h, count=1, flags=re.S)
    return h


def main(aplica):
    guia = le(GUIA)
    for gera in (cristo, pao, que_fecha, descontos, quando_ir):
        alvo, pagina = gera(guia)
        mudou = (not os.path.isfile(alvo)) or le(alvo) != pagina
        rel = os.path.relpath(alvo, RAIZ).replace(os.sep, "/")
        print("   %s  %d bytes  %s" % (rel, len(pagina.encode("utf-8")),
                                       "escrito" if (aplica and mudou) else ("ja igual" if not mudou else "SO MOSTRANDO")))
        if aplica and mudou:
            escreve(alvo, pagina)
    roteiro = os.path.join(RAIZ, "destinos", "rio-de-janeiro", "roteiro-6-dias", "index.html")
    for arq, liga in ((GUIA, lambda h: liga_quando_no_guia(liga_descontos_no_guia(liga_pao_no_guia(liga_fecha_no_guia(liga_no_guia(h)))))), (roteiro, liga_no_roteiro),
                      (os.path.join(RAIZ, "destinos", "rio-de-janeiro", "quanto-custa", "index.html"),
                       liga_quando_na_ficha)):
        h = le(arq)
        h2 = liga(h)
        if h2 != h:
            print("   %s: links novos  %s" % (os.path.relpath(arq, RAIZ).replace(os.sep, "/"),
                                              "escrito" if aplica else "SO MOSTRANDO"))
            if aplica:
                escreve(arq, h2)
    if not aplica:
        print("Nada foi alterado. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
