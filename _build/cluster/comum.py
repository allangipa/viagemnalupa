# -*- coding: utf-8 -*-
"""O que as paginas de cluster de qualquer cidade usam igual.

Nasceu do _build/rio/paginas.py (23/out/2026), quando o molde do Rio passou
para Lisboa. Cada cidade tem o seu paginas.py, com os dados e o texto
dela; aqui fica so a mecanica: ler e escrever, a trava de numero, a cabeca
emprestada da ficha de custos, o FAQ, o "Continue", o bloco da Booking e a
foto de capa.

Nada aqui sabe de cidade: tudo o que muda de uma para outra entra como
argumento.
"""
import html as H
import json
import os
import re
import sys

SITE = "https://viagemnalupa.com.br"
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOBE = "../../../"          # toda pagina de cluster mora em destinos/<cidade>/<pagina>/


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


def junta(itens):
    itens = list(itens)
    if len(itens) <= 1:
        return "".join(itens)
    return ", ".join(itens[:-1]) + " e " + itens[-1]


def minuscula(t):
    return t[:1].lower() + t[1:]


def confere_numeros(texto, fonte, rotulo):
    """Todo numero de `texto` (preco, idade, ano, quantidade) precisa estar em `fonte`."""
    fonte = limpa(fonte)
    for n in re.findall(r"\d+(?:,\d+)?", limpa(texto)):
        if not re.search(r"(?<!\d)(?<!\d,)%s(?!\d|,\d)" % re.escape(n), fonte):
            sys.exit("PARADO: '%s' (%s) nao esta na fonte" % (n, rotulo))


def ld(o):
    return '<script type="application/ld+json">%s</script>\n' % json.dumps(
        o, ensure_ascii=False, separators=(",", ":"))


def faq_html(perguntas, sobre):
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


def migalhas(slug, cidade, folha, url):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Destinos", "item": SITE + "/destinos/"},
        {"@type": "ListItem", "position": 3, "name": cidade, "item": "%s/destinos/%s/" % (SITE, slug)},
        {"@type": "ListItem", "position": 4, "name": folha, "item": url}]}


def esqueleto(molde, titulo, descricao, url, imagem, alt):
    """Cabeca, cabecalho e rodape da ficha de custos da cidade (mesma profundidade)."""
    s = le(molde)
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


def continua(irmas, cidade, atual):
    """irmas: [(href relativo a destinos/<cidade>/, rotulo)]."""
    links = " ".join('<a class="pg" href="../%s">%s</a>' % (h, t) for h, t in irmas if h != atual + "/")
    return ('<section class="bloco">\n  <div class="bloco-head"><span class="eyebrow">Continue</span>'
            '<h2>As outras páginas %s</h2></div>\n  <div class="paginas"> %s </div>\n</section>\n\n'
            % (cidade, links))


SETA = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 17 L17 7 '
        'M9 7h8v8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '</path></svg>')


def reserva(guia, slug, onde, sid, frase):
    """O bloco da Booking, com o link do guia e sid proprio. onde: 'no Rio de Janeiro', 'em Lisboa'."""
    booking = acha(r'<a class="parceiro" href="(https://www\.jdoqocy\.com/[^"]*)"', guia, "a Booking do guia").group(1)
    booking = re.sub(r"sid=[^&\"]*", "sid=vnl-%s-%s" % (slug, sid), booking)
    return ('<section class="bloco">\n<div class="reserva">\n<div class="reserva-topo">\n<h3>Hospedagem</h3>\n'
            '<p>%sA hospedagem e a passagem não entram nos preços desta página; <a href="../quanto-custa/">a ficha '
            'de custos</a> traz as duas, com a data da apuração.</p>\n'
            '<p style="color:var(--nevoa);font-size:.9rem"><b>Este link dá comissão ao site.</b> Você paga o mesmo '
            'preço que pagaria indo direto, e a comissão <b>não altera nenhum número do site</b>. '
            '<a href="%ssobre/">Como isso funciona</a>.</p>\n</div>\n'
            '<div class="reserva-lista"><a class="parceiro" href="%s" target="_blank" rel="noopener sponsored">'
            '<span class="p-nome">Booking.com%s</span><span class="p-nota">hotéis %s</span></a></div>\n'
            '</div>\n</section>\n' % (frase, SOBE, H.escape(booking, quote=True), SETA, onde))


def capa_de(creditos, slug, img_id, prioridade=True):
    """(figura, url absoluta da imagem, alt), com o credito do creditos.json da cidade."""
    cred = json.loads(le(creditos))[img_id]
    if cred["fonte"] == "storyblocks":
        credito = "Storyblocks · licença royalty-free · SBI-%s" % cred["sbi"]
    else:
        credito = ('Foto: %s · <a href="%s" target="_blank" rel="noopener license">%s</a> · '
                   '<a href="%s" target="_blank" rel="noopener">Wikimedia Commons</a> · recortada'
                   % (H.escape(cred["autor"]), cred["licurl"], cred["lic"], cred["pagina"]))
    b = SOBE + "assets/img/%s/%s" % (slug, img_id)
    figura = ('<figure class="hero-capa">\n  <img%s srcset="%s-400.webp 400w, %s-640.webp 640w, %s-820.webp 820w, '
              '%s.webp 1200w" sizes="(min-width:1080px) 820px, 100vw" src="%s.webp" alt="%s" width="1200" '
              'height="675" decoding="async">\n  <figcaption><p class="foto-cred">%s</p></figcaption>\n</figure>'
              % (' fetchpriority="high"' if prioridade else "", b, b, b, b, b, H.escape(cred["alt"], quote=True),
                 credito))
    return figura, "%s/assets/img/%s/%s.webp" % (SITE, slug, img_id), cred["alt"]


def coords(cidade, pid):
    """cidade: a chave 'c' do _build/coords.json ('rio', 'lisboa')."""
    for c in json.loads(le(os.path.join(RAIZ, "_build", "coords.json"))):
        if c["c"] == cidade and c["id"] == pid:
            return c["lat"], c["lng"]
    return None


def campo(rot, sec_id, eyebrow, corpo, extra=""):
    return ('<section class="bloco" id="%s">\n  <div class="bloco-head"><span class="eyebrow">%s</span>'
            '<h2>%s</h2></div>\n  %s%s\n</section>\n\n' % (sec_id, eyebrow, rot, corpo, extra))


def paragrafos(t):
    """Um campo da ficha, com <br>, vira paragrafos."""
    return "".join('<p style="color:var(--nevoa)">%s</p>' % x.strip() for x in t.split("<br>") if x.strip())


def assinatura():
    return ('<p class="assinatura">Apurado por <a href="%ssobre/#quem-faz">Allan Vitor</a> · '
            '<a href="https://www.instagram.com/viagemnalupabr/" target="_blank" rel="noopener">@viagemnalupabr'
            '<span class="so-leitor"> (abre em outra aba)</span></a></p>\n' % SOBE)


def liga_na_lista(h, cidade_frase, href, rotulo):
    """Poe um link no bloco 'As outras paginas <cidade>' do guia, se ainda nao estiver."""
    if 'href="%s"' % href in h:
        return h
    return re.sub(r'(<h2>As outras páginas %s</h2></div>\s*<div class="paginas">)' % re.escape(cidade_frase),
                  lambda m: m.group(1) + ' <a class="pg" href="%s">%s</a>' % (href, rotulo), h, count=1)


def aplica_tudo(geradores, ligacoes, guia_path, aplica):
    """Roda os geradores de pagina e as ligacoes nos arquivos ja publicados."""
    guia = le(guia_path)
    for gera in geradores:
        alvo, pagina = gera(guia)
        mudou = (not os.path.isfile(alvo)) or le(alvo) != pagina
        rel = os.path.relpath(alvo, RAIZ).replace(os.sep, "/")
        print("   %s  %d bytes  %s" % (rel, len(pagina.encode("utf-8")),
                                       "escrito" if (aplica and mudou) else ("ja igual" if not mudou else "SO MOSTRANDO")))
        if aplica and mudou:
            escreve(alvo, pagina)
    for arq, liga in ligacoes:
        h = le(arq)
        h2 = liga(h)
        if h2 != h:
            print("   %s: links novos  %s" % (os.path.relpath(arq, RAIZ).replace(os.sep, "/"),
                                              "escrito" if aplica else "SO MOSTRANDO"))
            if aplica:
                escreve(arq, h2)
    if not aplica:
        print("Nada foi alterado. Rode com --aplica.")
