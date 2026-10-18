# -*- coding: utf-8 -*-
"""Gera /gratis/: os pontos que nao cobram entrada, em todas as cidades.

Item 2 do _build/docs/concorrentes-2026-10-17.md ("varias paginas por
destino, nao tres"), com a decisao de 17/10/2026: UMA pagina cruzando o
acervo, e nao vinte por cidade. Sete das vinte cidades tem so 1 ou 2
pontos gratis; vinte paginas dariam sete finas, num site que ja tem 42
URLs "detectadas, mas nao indexadas". Uma pagina forte, que linka os 20
guias, e entrada nova para todas elas.

O QUE FAZ ESTA PAGINA SER SO NOSSA e a coluna preco-nota: gratis COM A
PEGADINHA ESCRITA - "a praca; subir ao arco e pago", "so aos domingos",
"sentar na escada custa € 250", "a cobranca anunciada nunca foi
aprovada". Nenhum dos sete concorrentes lidos tem isso.

DE ONDE SAI TUDO: dos guias publicados, pelo mesmo caminho do faq.py e do
ofertas.py - o <article class="ponto"> com preco-val gratis/gratuito/
livre, o nome no <h3>, a ressalva no preco-nota, a ancora no id. Nada e
escrito a mao. Hospedagem fica fora: e conta, nao lugar.

O NOME DA CIDADE sai do DESTINOS do schema/gera.py, nao do <h1>: o de
Nova York e "Nova York em novembro: ...".

CABECA, CABECALHO E RODAPE SAO EMPRESTADOS do sobre/index.html, que e a
pagina de topo mantida a mao: troca-se titulo, descricao, canonical, og e
breadcrumb; os JSON-LD dele saem e entram os desta pagina (Breadcrumb e
ItemList). O WebPage, com author e data, vem do schema/editor.py como em
qualquer pagina. Assim a pagina nova nunca descola do template da casa.

O CARTAO DA HOME e atualizado aqui tambem: os numeros "N pontos" e "M
cidades" do cartao de /gratis/ sao trocados pelos atuais, para o cartao
nao envelhecer quando um destino entrar.

Idempotente. Entra na cadeia do LEIA-ME depois do faq.py.

Uso
---
    python _build/recortes/gratis.py            # so mostra
    python _build/recortes/gratis.py --aplica   # escreve
"""
import glob
import html as H
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
SITE = "https://viagemnalupa.com.br"

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

GRATIS = re.compile(r"gr[aá]tis|gratuit|livre", re.I)


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def limpa(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t or "")).strip()


def nomes_dos_destinos():
    """slug -> nome, lido do dicionario DESTINOS do schema/gera.py."""
    s = le(os.path.join(RAIZ, "_build", "schema", "gera.py"))
    m = re.search(r"(?s)^DESTINOS = \{(.*?)^\}", s, re.M)
    return dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', m.group(1)))


def pontos_gratis(slug):
    h = le(os.path.join(RAIZ, "destinos", slug, "index.html"))
    total, itens = 0, []
    for m in re.finditer(r'(?s)<article class="ponto" id="([^"]+)"(.*?)</article>', h):
        pid, corpo = m.group(1), m.group(2)
        val = re.search(r'class="preco-val"[^>]*>(.*?)</span>', corpo, re.S)
        nome = re.search(r"<h3[^>]*>(.*?)</h3>", corpo, re.S)
        if not (val and nome):
            continue
        total += 1
        if "hospedagem" in pid or not GRATIS.search(limpa(val.group(1))):
            continue
        nota = re.search(r'class="preco-nota"[^>]*>(.*?)</span>', corpo, re.S)
        itens.append(dict(id=pid, nome=limpa(nome.group(1)),
                          nota=limpa(nota.group(1)) if nota else ""))
    return total, itens


def esqueleto():
    """Cabeca, cabecalho e rodape do sobre/, com o que e dele trocado."""
    s = le(os.path.join(RAIZ, "sobre", "index.html"))
    cabeca = s[:s.find("<main id=\"conteudo\">")]
    pe = s[s.find("</main>"):]
    # os JSON-LD do sobre saem; os desta pagina entram no lugar
    cabeca = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", cabeca, flags=re.S)
    cabeca = cabeca.replace(' aria-current="page"', "")
    return cabeca, pe


def main(aplica):
    nomes = nomes_dos_destinos()
    cidades = []
    for slug in sorted(nomes, key=lambda k: nomes[k]):
        if not os.path.isfile(os.path.join(RAIZ, "destinos", slug, "index.html")):
            continue
        total, itens = pontos_gratis(slug)
        cidades.append((slug, nomes[slug], total, itens))
    n_pts = sum(len(c[3]) for c in cidades)
    n_tot = sum(c[2] for c in cidades)
    n_cid = len(cidades)

    titulo = "%d pontos turísticos que não cobram entrada, em %d cidades" % (n_pts, n_cid)
    descricao = ("Os %d pontos gratuitos dos %d guias do Viagem na Lupa, cidade por cidade — "
                 "e o que cada um cobra à parte, com a fonte e a data no guia de cada ponto."
                 % (n_pts, n_cid))
    url = SITE + "/gratis/"

    cabeca, pe = esqueleto()
    cabeca = re.sub(r"<title>.*?</title>", "<title>%s — Viagem na Lupa</title>" % H.escape(titulo), cabeca, flags=re.S)
    cabeca = re.sub(r'<meta name="description" content="[^"]*">',
                    '<meta name="description" content="%s">' % H.escape(descricao, quote=True), cabeca)
    cabeca = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url, cabeca)
    cabeca = re.sub(r'<meta property="og:title" content="[^"]*">',
                    '<meta property="og:title" content="%s — Viagem na Lupa">' % H.escape(titulo, quote=True), cabeca)
    cabeca = re.sub(r'<meta property="og:description" content="[^"]*">',
                    '<meta property="og:description" content="%s">' % H.escape(descricao, quote=True), cabeca)
    cabeca = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % url, cabeca)

    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Grátis", "item": url}]}
    lista = {"@context": "https://schema.org", "@type": "ItemList",
             "name": titulo, "numberOfItems": n_pts, "itemListElement": []}
    pos = 0
    for slug, nome, total, itens in cidades:
        for it in itens:
            pos += 1
            lista["itemListElement"].append({
                "@type": "ListItem", "position": pos,
                "name": "%s (%s)" % (it["nome"], nome),
                "url": "%s/destinos/%s/#%s" % (SITE, slug, it["id"])})
    jsonld = "".join('<script type="application/ld+json">%s</script>\n'
                     % json.dumps(o, ensure_ascii=False, separators=(",", ":")) for o in (migalhas, lista))
    cabeca = cabeca.replace("</head>", jsonld + "</head>", 1)

    # ------------------------------------------------------------- o corpo
    idx = " · ".join('<a href="#%s">%s</a>' % (slug, H.escape(nome)) for slug, nome, _, _ in cidades)
    partes = [
        '<main id="conteudo">\n',
        '<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="../">Início</a> › Grátis</p>\n',
        '<div class="hero">\n  <h1>%s</h1>\n' % H.escape(titulo),
        '  <p>E o que cada um cobra à parte — porque “grátis” quase sempre tem uma vírgula depois: '
        'a praça é livre, subir ao arco é pago; a feira é de graça, só no domingo.</p>\n'
        '</div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
        '<section class="bloco">\n  <div class="bloco-head"><span class="eyebrow">Como esta lista foi feita</span>'
        '<h2>Nada aqui foi escrito à mão</h2>\n'
        '  <p>São os %d pontos marcados como gratuitos nos %d guias deste site, entre %d pontos apurados. '
        'Cada linha leva ao ponto no guia da cidade, onde estão a fonte, a data da consulta e o que não foi '
        'possível confirmar. A ressalva ao lado do nome é a mesma que o guia publica. Hospedagem não entra: '
        'é conta, não lugar.</p>\n</div>\n</section>\n\n' % (n_pts, n_cid, n_tot),
        '<section class="bloco">\n  <div class="bloco-head"><span class="eyebrow">Índice</span>'
        '<h2>Por cidade</h2></div>\n  <p class="idx-gratis">%s</p>\n</section>\n\n' % idx,
    ]
    for slug, nome, total, itens in cidades:
        li = "".join(
            '\n    <li><a href="../destinos/%s/#%s">%s</a>%s</li>'
            % (slug, it["id"], H.escape(it["nome"]),
               (" — " + H.escape(it["nota"])) if it["nota"] else "")
            for it in itens)
        partes.append(
            '<section class="bloco" id="%s">\n  <div class="bloco-head"><span class="eyebrow">%d de %d pontos</span>'
            '<h2><a href="../destinos/%s/">%s</a></h2></div>\n  <ul class="plain">%s\n  </ul>\n</section>\n\n'
            % (slug, len(itens), total, slug, H.escape(nome), li))
    partes.append("</div>\n")
    corpo = "".join(partes)

    pagina = cabeca + corpo + pe
    alvo = os.path.join(RAIZ, "gratis", "index.html")
    mudou = (not os.path.isfile(alvo)) or le(alvo) != pagina
    print("   /gratis/  %d pontos gratis em %d cidades (de %d apurados)   %s"
          % (n_pts, n_cid, n_tot, "escrito" if (aplica and mudou) else ("ja igual" if not mudou else "SO MOSTRANDO")))
    if aplica and mudou:
        escreve(alvo, pagina)

    # ------------------------------------------------- o cartao da home
    home = os.path.join(RAIZ, "index.html")
    h = le(home)
    h2 = re.sub(r"(\d+) pontos que não cobram entrada, em (\d+) cidades",
                "%d pontos que não cobram entrada, em %d cidades" % (n_pts, n_cid), h)
    h2 = re.sub(r"Ver os (\d+) pontos", "Ver os %d pontos" % n_pts, h2)
    if h2 != h:
        print("   home: numeros do cartao de /gratis/ atualizados")
        if aplica:
            escreve(home, h2)
    elif "/gratis/" not in h:
        print("   home: AINDA SEM o cartao de /gratis/ (ver o Edit de 17/10/2026)")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
