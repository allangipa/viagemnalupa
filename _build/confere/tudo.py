# -*- coding: utf-8 -*-
"""Confere o que uma revisao humana nao pega: numero que envelhece sozinho.

Duas familias de erro, as duas ja aconteceram de verdade neste site:

1. Contador defasado. A home ja anunciou "8 destinos" com 6 cartoes. A ficha
   de Montevideu ja anunciou "8 pontos" com 9 secoes apuradas - no titulo,
   na descricao, no og:title, no texto de abertura e nos dois indices. Cada
   ponto novo que entra deixa cinco frases erradas para tras, e nenhuma
   delas da erro em lugar nenhum.

2. Dado estruturado apontando para o vazio. JSON-LD nao quebra a pagina
   quando cita uma URL ou uma imagem que nao existe: fica so errado, em
   silencio, ate o Search Console reclamar semanas depois.

Uso:
    python _build/confere/tudo.py

Sai com codigo 1 se achar problema, para poder virar passo de workflow.
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://viagemnalupa.com.br"

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Numero por extenso, porque o site escreve "oito pontos", nao "8 pontos".
EXTENSO = {"um": 1, "dois": 2, "tres": 3, "três": 3, "quatro": 4, "cinco": 5,
           "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10, "onze": 11,
           "doze": 12, "treze": 13, "catorze": 14, "quinze": 15,
           "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19,
           "vinte": 20}

# Tipos que descendem de CreativeWork e portanto aceitam inLanguage.
# Qualquer outro que a traga esta errado - ver a anotacao no confere_schema.
SO_CRIATIVO = {"WebPage", "WebSite", "WebApplication", "Article",
               "NewsArticle", "BlogPosting", "CreativeWork", "SoftwareApplication"}

PROBLEMAS = []


def anota(x):
    PROBLEMAS.append(x)


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def paginas():
    for dirp, _, arqs in os.walk(RAIZ):
        if any(x in dirp for x in ("_build", ".git", "Claude outputs", "node_modules")):
            continue
        for a in arqs:
            if a.endswith(".html"):
                p = os.path.join(dirp, a)
                yield "/" + os.path.relpath(p, RAIZ).replace(os.sep, "/"), p


def valor(bruto):
    b = bruto.lower()
    return int(b) if b.isdigit() else EXTENSO[b]


# Como o titulo da calculadora chama cada destino, para saber quantos ele
# nomeia antes do "e mais N".
ROTULO = {
    "buenos-aires":   "Buenos Aires",
    "lisboa":         "Lisboa",
    "maceio":         "Maceió",
    "montevideu":     "Montevidéu",
    "nova-york":      "Nova York",
    "orlando":        "Orlando",
    "rio-de-janeiro": "Rio",
    "santiago":       "Santiago",
}


def rotulo_de(slug):
    return ROTULO.get(slug, slug)


# --------------------------------------------------------------- a verdade

def pontos_reais():
    """Um ponto e uma <article class="ponto" id="...">. E a unica definicao
    que o proprio HTML sustenta, entao e a que vale."""
    d = {}
    base = os.path.join(RAIZ, "destinos")
    for slug in sorted(os.listdir(base)):
        g = os.path.join(base, slug, "index.html")
        if os.path.isfile(g):
            d[slug] = len(re.findall(r'<article class="ponto" id="', le(g)))
    return d


# ------------------------------------------------------------- contadores

def confere_contadores(real):
    print("=== pontos apurados em cada ficha ===")
    for slug, n in real.items():
        print("   %-16s %2d" % (slug, n))
    print("   %-16s %2d destinos" % ("TOTAL", len(real)))
    print()

    # 1. cartao dos indices: "Uruguai - 9 pontos turisticos"
    print("=== cartoes dos indices ===")
    for idx in ("index.html", os.path.join("destinos", "index.html")):
        p = os.path.join(RAIZ, idx)
        if not os.path.isfile(p):
            continue
        h = le(p)
        for m in re.finditer(
                r'href="[^"]*?/?([a-z\-]+)/"[^>]*>([^<]+)</a></h3>'
                r'<span class="pais">([^<]*?)(\d+) pontos', h):
            slug, rotulo, n = m.group(1), m.group(2), int(m.group(4))
            if slug not in real:
                continue
            bate = real[slug] == n
            print("   %-22s %-16s diz %2d  real %2d  %s"
                  % (idx, rotulo, n, real[slug], "ok" if bate else "<<<"))
            if not bate:
                anota("%s: cartao de %s diz %d pontos, a ficha tem %d"
                      % (idx, rotulo, n, real[slug]))

    # 1b. O outro formato de cartao: "Chile - roteiro de 5 dias". O numero
    # tem de bater com a pasta que existe (roteiro-5-dias) e com quantos
    # dias o roteiro de fato descreve.
    print()
    print("=== cartoes que anunciam roteiro ===")
    for idx in ("index.html", os.path.join("destinos", "index.html")):
        p = os.path.join(RAIZ, idx)
        if not os.path.isfile(p):
            continue
        h = le(p)
        for m in re.finditer(
                r'href="[^"]*?/?([a-z\-]+)/"[^>]*>([^<]+)</a></h3>'
                r'<span class="pais">[^<]*?roteiro de (\d+) dias', h):
            slug, rotulo, n = m.group(1), m.group(2), int(m.group(3))
            if slug not in real:
                continue
            pasta = os.path.join(RAIZ, "destinos", slug, "roteiro-%d-dias" % n)
            existe = os.path.isfile(os.path.join(pasta, "index.html"))
            dias = 0
            if existe:
                dias = len(re.findall(
                    r"<h3[^>]*>", le(os.path.join(pasta, "index.html"))))
            bate = existe and dias == n
            print("   %-22s %-16s diz %d dias  pasta=%-3s h3=%-3s %s"
                  % (idx, rotulo, n, "ok" if existe else "NAO", dias,
                     "ok" if bate else "<<<"))
            if not existe:
                anota("%s: cartao de %s aponta roteiro de %d dias, mas a pasta "
                      "roteiro-%d-dias nao existe" % (idx, rotulo, n, n))
            elif dias != n:
                anota("%s: cartao de %s diz %d dias, o roteiro descreve %d"
                      % (idx, rotulo, n, dias))

    # 1c. O placar da home: "Pontos apurados". Ja esteve em 86 quando eram
    # 101 - era a conta de antes de Montevideu e Orlando entrarem. E o
    # numero mais visivel do site, o primeiro que o leitor ve.
    print()
    print("=== placar da home ===")
    soma = sum(real.values())
    ph = os.path.join(RAIZ, "index.html")
    if os.path.isfile(ph):
        h = le(ph)
        m = re.search(r'<span class="r">Pontos apurados</span>'
                      r'<span class="v">(\d+)</span>', h)
        if m:
            diz = int(m.group(1))
            print("   pontos apurados: diz %d  real %d  %s"
                  % (diz, soma, "ok" if diz == soma else "<<<"))
            if diz != soma:
                anota("index.html: o placar diz %d pontos apurados, somam %d"
                      % (diz, soma))
        else:
            print("   (placar nao encontrado - o formato mudou?)")

    # 2. numero de destinos que o site diz ter.
    #
    # So conta a frase que declara o acervo inteiro. "Rio, Lisboa, Nova York
    # e mais tres destinos", na calculadora, NAO e isso: e contagem relativa
    # ao que aquela pagina cobre, e tem conferencia propria mais abaixo.
    print()
    print("=== quantos destinos o site diz ter ===")
    alvo = len(real)
    TOTAL_DESTINOS = re.compile(
        r"(?<!mais\s)(\d+|%s)\s+destinos\b(?!\s+(?:que|onde|com\s+o))"
        % "|".join(EXTENSO), re.I)
    for rel, p in paginas():
        h = le(p)
        for m in TOTAL_DESTINOS.finditer(h):
            n = valor(m.group(1))
            bate = n == alvo
            print("   %-44s diz %-10s %s" % (rel, m.group(1), "ok" if bate else "<<<"))
            if not bate:
                anota("%s: fala em %s destinos, existem %d" % (rel, m.group(1), alvo))

    # 3. a calculadora promete no titulo N nomeados + "mais M". Nomeado mais
    # M tem de dar o tanto de destino que ela realmente cobre.
    print()
    print("=== alcance da calculadora ===")
    pc = os.path.join(RAIZ, "calculadora", "index.html")
    if os.path.isfile(pc):
        h = le(pc)
        cobre = {s for s in re.findall(r"destinos/([a-z\-]+)/", h) if s in real}
        m = re.search(r"<title>([^<]*)</title>", h)
        titulo = m.group(1) if m else ""
        mm = re.search(r"e\s+mais\s+(\d+|%s)\s+destinos" % "|".join(EXTENSO),
                       titulo, re.I)
        nomeados = sum(1 for s in real
                       if re.search(r"\b%s\b" % re.escape(rotulo_de(s)), titulo))
        print("   cobre de fato : %d  (%s)" % (len(cobre), ", ".join(sorted(cobre))))
        print("   titulo nomeia : %d" % nomeados)
        if mm:
            prometido = nomeados + valor(mm.group(1))
            print("   titulo promete: %d nomeados + %s = %d  %s"
                  % (nomeados, mm.group(1), prometido,
                     "ok" if prometido == len(cobre) else "<<<"))
            if prometido != len(cobre):
                anota("/calculadora/: o titulo promete %d destinos, a pagina "
                      "cobre %d" % (prometido, len(cobre)))
        faltam = set(real) - cobre
        if faltam:
            print("   fora da calculadora: %s" % ", ".join(sorted(faltam)))

    # 4. a ficha conferindo a si mesma.
    #
    # Prosa fala em "tres pontos que nunca cobram" e "doze pontos pagos", que
    # sao subconjuntos legitimos. Conferir todo "N pontos" faria o verificador
    # gritar a toa - e verificador que grita a toa ninguem le. Entao so as
    # formas que realmente declaram o total da ficha entram aqui.
    print()
    print("=== cada ficha contra o proprio numero ===")
    DECLARA_TOTAL = re.compile(
        r"(\d+|%s)\s+pontos\s+"
        r"(turísticos|turisticos|com\s+preço|com\s+preco|abaixo|certos|de\s+[A-ZÀ-Ý])"
        % "|".join(EXTENSO), re.I)
    achou = False
    for slug, n in real.items():
        h = le(os.path.join(RAIZ, "destinos", slug, "index.html"))
        for m in DECLARA_TOTAL.finditer(h):
            antes = h[max(0, m.start() - 24):m.start()].lower()
            if re.search(r"(dos|das|de)\s*$", antes):
                continue
            if valor(m.group(1)) != n:
                achou = True
                trecho = re.sub(r"<[^>]+>", "", h[max(0, m.start() - 70):m.end() + 30])
                print("   %-16s diz %-10s real %2d   <<<  ...%s..."
                      % (slug, m.group(1), n,
                         re.sub(r"\s+", " ", trecho).strip()[-100:]))
                anota("destinos/%s: declara %s pontos, tem %d"
                      % (slug, m.group(1), n))
    if not achou:
        print("   todas conferem")


# ---------------------------------------------------------- dado estruturado

def caminho_de(url):
    if not url.startswith(SITE):
        return None
    rel = url[len(SITE):].split("#")[0].split("?")[0].lstrip("/")
    if rel == "" or rel.endswith("/"):
        return os.path.join(RAIZ, rel.replace("/", os.sep), "index.html")
    return os.path.join(RAIZ, rel.replace("/", os.sep))


def confere_schema():
    print()
    print("=== dado estruturado ===")
    urls, imgs, tipos = set(), set(), {}
    com, sem = [], []

    def anda(o, pag):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("url", "item") and isinstance(v, str):
                    urls.add((v, pag))
                elif k == "image" and isinstance(v, str):
                    imgs.add((v, pag))
                else:
                    anda(v, pag)
        elif isinstance(o, list):
            for v in o:
                anda(v, pag)

    for rel, p in paginas():
        h = le(p)
        if h.count("<head>") != 1 or h.count("</head>") != 1:
            anota("%s: <head> desbalanceado" % rel)
        if ("tp-drive:inicio" in h) != ("tp-drive:fim" in h):
            anota("%s: marcador do Travelpayouts quebrado" % rel)
        # Tag de bloco aberta e fechada em numero diferente.
        #
        # Entrou porque aconteceu: um script de reorganizacao duplicou o
        # </article> de Montevideu (9 abriam, 18 fechavam) e de Orlando
        # (6 e 12). HTML invalido nao da erro em lugar nenhum - o
        # navegador conserta em silencio, cada um do seu jeito, e o
        # estrago so aparece num layout torto que ninguem sabe explicar.
        for tag in ("article", "section", "details", "summary", "figure",
                    "main", "header", "footer", "table"):
            abre = len(re.findall(r"<%s[\s>]" % tag, h))
            fecha = len(re.findall(r"</%s>" % tag, h))
            if abre != fecha:
                anota("%s: <%s> abre %d e fecha %d"
                      % (rel, tag, abre, fecha))

        fim = h.find("</head>")
        achou = 0
        for m in re.finditer(
                r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            achou += 1
            if m.start() > fim:
                anota("%s: bloco JSON-LD fora do <head>" % rel)
            try:
                o = json.loads(m.group(1).replace("<\\/", "</"))
            except Exception as e:
                anota("%s: JSON-LD invalido -> %s" % (rel, e))
                continue
            for x in (o if isinstance(o, list) else [o]):
                if not isinstance(x, dict):
                    continue
                t = x.get("@type", "?")
                tipos[t] = tipos.get(t, 0) + 1
                if "@context" not in x:
                    anota("%s: bloco %s sem @context" % (rel, t))
                # inLanguage e de CreativeWork. Posta num Place ou num
                # Intangible, o validador do schema.org avisa. Ja aconteceu:
                # os blocos originais de Lisboa e do Rio traziam isso e o
                # gerador copiou para mais dez antes de alguem reparar.
                if "inLanguage" in x and t not in SO_CRIATIVO:
                    anota("%s: %s nao aceita inLanguage (e de CreativeWork)"
                          % (rel, t))
            anda(o, rel)
        (com if achou else sem).append(rel)

    for u, pag in sorted(urls):
        c = caminho_de(u)
        if c is not None and not os.path.isfile(c):
            anota("%s: JSON-LD aponta para pagina inexistente -> %s" % (pag, u))
    for u, pag in sorted(imgs):
        c = caminho_de(u)
        if c is not None and not os.path.isfile(c):
            anota("%s: JSON-LD aponta para imagem inexistente -> %s" % (pag, u))

    print("   paginas com dado estruturado : %d" % len(com))
    print("   paginas SEM                  : %d" % len(sem))
    for r in sem:
        print("        %s" % r)
    # Listar nao bastava. As fichas de custo de Cancun e Fortaleza ficaram
    # no ar sem nenhum bloco - o gerador sabia monta-las, so nunca foi
    # rodado depois que as paginas nasceram - e o verificador imprimiu
    # "Nada divergente" com as duas na lista acima. Agora reclama.
    #
    # A 404 e a unica excecao legitima: nao e pagina para indexar.
    for r in sem:
        if os.path.basename(r) != "404.html":
            anota("%s: no ar sem nenhum dado estruturado "
                  "(rode _build/schema/gera.py --aplica)" % r)
    print("   URLs conferidas              : %d" % len(urls))
    print("   imagens conferidas           : %d" % len(imgs))
    print("   por tipo:")
    for t, q in sorted(tipos.items(), key=lambda x: -x[1]):
        print("      %-22s %d" % (t, q))


def main():
    real = pontos_reais()
    confere_contadores(real)
    confere_schema()
    print()
    if PROBLEMAS:
        print("!!! %d problema(s):" % len(PROBLEMAS))
        for x in PROBLEMAS:
            print("   " + x)
        return 1
    print("Nada divergente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
