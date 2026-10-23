# -*- coding: utf-8 -*-
"""Paginas derivadas do Rio: uma pergunta por pagina, em volta do guia.

Plano em _build/docs/cluster-rio-2026-10-23.md (fase A). Esta e a 1:
/destinos/rio-de-janeiro/cristo-redentor/.

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


def faq_html(perguntas):
    itens = "".join(
        '\n  <details class="faq-q"><summary><h3>%s</h3></summary><p>%s</p></details>' % (H.escape(q), a)
        for q, a in perguntas)
    return ('<section class="bloco faq" id="perguntas">\n  <div class="bloco-head"><span class="eyebrow">'
            'Perguntas frequentes</span><h2>O que mais se pergunta sobre o Cristo Redentor</h2></div>%s\n'
            '</section>\n' % itens)


def faq_ld(perguntas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": limpa(a)}} for q, a in perguntas]}


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
    booking = acha(r'<a class="parceiro" href="(https://www\.jdoqocy\.com/[^"]*)"', guia, "a Booking do guia").group(1)
    booking = re.sub(r"sid=[^&\"]*", "sid=vnl-rio-de-janeiro-cristo", booking)
    seta = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 17 L17 7 '
            'M9 7h8v8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            '</path></svg>')
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
        '<section class="bloco">\n  <div class="bloco-head"><span class="eyebrow">Continue</span>'
        '<h2>As outras páginas do Rio de Janeiro</h2></div>\n'
        '  <div class="paginas"> <a class="pg" href="../">Guia dos 16 pontos turísticos</a> '
        '<a class="pg" href="../quanto-custa/">Quanto custa 6 dias no Rio</a> '
        '<a class="pg" href="../roteiro-6-dias/">Roteiro de 6 dias</a> '
        '<a class="pg" href="../quanto-custa/#calculadora">Calculadora da viagem</a> </div>\n</section>\n\n',
        '<section class="bloco">\n<div class="reserva">\n<div class="reserva-topo">\n<h3>Hospedagem</h3>\n'
        '<p>O ingresso compre só no canal oficial: com a obra, ele esgota dias antes. A hospedagem e a passagem '
        'não entram nos preços desta página; <a href="../quanto-custa/">a ficha de custos</a> traz as duas, '
        'com a data da apuração.</p>\n'
        '<p style="color:var(--nevoa);font-size:.9rem"><b>Este link dá comissão ao site.</b> Você paga o mesmo '
        'preço que pagaria indo direto, e a comissão <b>não altera nenhum número do site</b>. '
        '<a href="%ssobre/">Como isso funciona</a>.</p>\n</div>\n'
        '<div class="reserva-lista"><a class="parceiro" href="%s" target="_blank" rel="noopener sponsored">'
        '<span class="p-nome">Booking.com%s</span><span class="p-nota">hotéis no Rio de Janeiro</span></a></div>\n'
        '</div>\n</section>\n' % (SOBE, H.escape(booking, quote=True), seta),
        '</div>\n',
    ]
    return os.path.join(RAIZ, "destinos", "rio-de-janeiro", pid, "index.html"), cabeca + "".join(partes) + pe


# ------------------------------------------------- os links no guia
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
    alvo, pagina = cristo(guia)
    mudou = (not os.path.isfile(alvo)) or le(alvo) != pagina
    rel = os.path.relpath(alvo, RAIZ).replace(os.sep, "/")
    print("   %s  %d bytes  %s" % (rel, len(pagina.encode("utf-8")),
                                   "escrito" if (aplica and mudou) else ("ja igual" if not mudou else "SO MOSTRANDO")))
    if aplica and mudou:
        escreve(alvo, pagina)
    g2 = liga_no_guia(guia)
    if g2 != guia:
        print("   guia: +2 links para cristo-redentor/  %s" % ("escrito" if aplica else "SO MOSTRANDO"))
        if aplica:
            escreve(GUIA, g2)
    if not aplica:
        print("Nada foi alterado. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
