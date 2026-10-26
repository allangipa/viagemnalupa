# -*- coding: utf-8 -*-
"""Gera /comparar/: os destinos lado a lado, so no que e comparavel.

Pedido de 26/10/2026 (pagina de "inspiracao"). A ideia original era um
ranking de custo por dia, e os dados nao deixam: 10 das 21 fichas de custos
nao tem hospedagem, e as outras 11 tem roteiros de 3 a 7 dias, conjuntos de
ingressos diferentes e diarias de bases diferentes. Ordenar por custo por
dia poria Roma e Salvador como "os mais baratos" so porque a ficha deles
nao tem hotel. Fica para quando as 10 fichas tiverem diaria.

O QUE ENTRA, e tem a mesma base nos 22 guias:
  - pontos que nao cobram entrada, contados como o /gratis/ conta
    (recortes/gratis.py, importado: o numero e o mesmo nas duas paginas);
  - a mediana e o maximo dos ingressos pagos, lidos do Offer do JSON-LD
    de cada guia - o schema/ofertas.py ja recusa faixa, piso e divergencia,
    entao so entra preco unico. A "hospedagem" que alguns guias listam
    como ponto fica fora;
  - a diaria que a ficha de custos usa, com a base que a propria ficha
    declara (media oficial, calculo sobre o INE, amostra).

CONVERSAO: boletim de fechamento do Banco Central de 23/out/2026, taxa de
venda, guardado em _build/recortes/fontes/bcb-fechamento-20261023.csv. A
PTAX do site so cobre euro e dolar; este boletim tem as sete moedas.

CABECA, CABECALHO E RODAPE emprestados do sobre/, como o gratis.py.

Uso
---
    python _build/recortes/comparar.py            # so mostra
    python _build/recortes/comparar.py --aplica   # escreve
"""
import html as H

import json
import os
import re
import statistics
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
SITE = "https://viagemnalupa.com.br"
sys.path.insert(0, AQUI)
# o gratis.py ja poe o stdout em utf-8 ao ser importado
from gratis import le, escreve, limpa, nomes_dos_destinos, pontos_gratis, esqueleto  # noqa: E402

BOLETIM = os.path.join(AQUI, "fontes", "bcb-fechamento-20261023.csv")
DATA_BOLETIM = "23 de outubro de 2026"
# simbolo da ficha de custos -> codigo do boletim
SIMBOLO = {"€": "EUR", "US$": "USD", "R$": "BRL", "ARS": "ARS", "MX$": "MXN", "$U": "UYU", "CLP": "CLP"}


def cotacoes():
    taxas = {"BRL": 1.0}
    for linha in le(BOLETIM).splitlines():
        c = linha.split(";")
        if len(c) >= 6:
            taxas[c[3]] = float(c[5].replace(",", "."))
    for m in set(SIMBOLO.values()):
        if m not in taxas:
            sys.exit("PARADO: o boletim do BCB nao tem %s" % m)
    return taxas


def reais(v):
    return "R$ " + "{:,.0f}".format(v).replace(",", ".")


def do_guia(slug):
    h = le(os.path.join(RAIZ, "destinos", slug, "index.html"))
    lista = None
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        o = json.loads(m.group(1))
        if o.get("@type") == "ItemList":
            lista = o
    if not lista:
        sys.exit("PARADO: %s sem ItemList" % slug)
    pagos, moedas = [], set()
    for it in lista["itemListElement"]:
        a = it["item"]
        if "hospedagem" in a.get("url", "") or "hospedagem" in a["name"].lower():
            continue
        of = a.get("offers")
        if of and float(of["price"]) > 0:
            pagos.append((float(of["price"]), a["name"], a["url"].split("#")[-1]))
            moedas.add(of["priceCurrency"])
    if len(moedas) > 1:
        sys.exit("PARADO: %s com mais de uma moeda nos Offer: %s" % (slug, moedas))
    return pagos, (moedas.pop() if moedas else None)


def da_ficha(slug):
    p = os.path.join(RAIZ, "destinos", slug, "quanto-custa", "index.html")
    if not os.path.isfile(p):
        return None
    m = re.search(r'(?s)class="calc-cfg"[^>]*>(.*?)</script>', le(p))
    if not m:
        return None
    cfg = json.loads(m.group(1))
    hp = {x["k"]: x for x in cfg.get("hosp") or []}.get(cfg.get("hospPadrao"))
    if cfg["moeda"] not in SIMBOLO:
        sys.exit("PARADO: moeda %s da ficha de %s sem codigo no boletim" % (cfg["moeda"], slug))
    return dict(moeda=SIMBOLO[cfg["moeda"]], hosp=hp)


def base_da_diaria(rot):
    r = rot.lower()
    if "amostra" in r:
        return "amostra"
    if "oficial" in r or "adr" in r or "ine" in r or "fohb" in r:
        return "média oficial" if "cálculo" not in r else "cálculo sobre dado oficial"
    return "a ficha não diz a base"


def main(aplica):
    taxas = cotacoes()
    nomes = nomes_dos_destinos()
    linhas = []
    for slug in sorted(nomes, key=lambda k: nomes[k]):
        if not os.path.isfile(os.path.join(RAIZ, "destinos", slug, "index.html")):
            continue
        total, gratis = pontos_gratis(slug)
        pagos, moeda = do_guia(slug)
        ficha = da_ficha(slug)
        if pagos:
            tx = taxas[moeda]
            vals = [v * tx for v, _, _ in pagos]
            caro = max(pagos)
            med, maior = statistics.median(vals), (caro[0] * tx, caro[1], caro[2])
        else:
            med = maior = None
        diaria = None
        if ficha and ficha["hosp"]:
            diaria = (ficha["hosp"]["ref"] * taxas[ficha["moeda"]], base_da_diaria(ficha["hosp"]["rot"]),
                      ficha["hosp"]["rot"])
        linhas.append(dict(slug=slug, nome=nomes[slug], total=total, gratis=len(gratis), npagos=len(pagos),
                           mediana=med, maior=maior, diaria=diaria, tem_ficha=bool(ficha)))

    n_cid = len(linhas)
    sem_hosp = [l["nome"] for l in linhas if l["tem_ficha"] and not l["diaria"]]
    sem_ficha = [l["nome"] for l in linhas if not l["tem_ficha"]]
    metade = sorted([l for l in linhas if l["total"] and l["gratis"] * 2 >= l["total"]],
                    key=lambda l: -l["gratis"] / l["total"])
    # Mediana de 1 ou 2 precos nao diz nada sobre a cidade: fica na tabela,
    # avisada, e fora do destaque e do FAQ.
    MIN_PAGOS = 3
    com_med = sorted([l for l in linhas if l["mediana"] is not None and l["npagos"] >= MIN_PAGOS],
                     key=lambda l: l["mediana"])
    poucos = [l for l in linhas if l["mediana"] is not None and l["npagos"] < MIN_PAGOS]

    def j(itens):
        itens = list(itens)
        return itens[0] if len(itens) == 1 else ", ".join(itens[:-1]) + " e " + itens[-1]

    def nome_link(l):
        return '<a href="../destinos/%s/">%s</a>' % (l["slug"], H.escape(l["nome"]))

    titulo = "%d destinos lado a lado: ingressos, pontos grátis e diária, em reais" % n_cid
    descricao = ("Os %d destinos do Viagem na Lupa comparados no que tem a mesma base: quantos pontos não cobram "
                 "entrada, quanto custa o ingresso típico e o mais caro, e a diária que cada ficha usa, tudo em "
                 "reais pelo câmbio do Banco Central de %s." % (n_cid, DATA_BOLETIM))
    url = SITE + "/comparar/"

    perguntas = [
        ("Qual destino tem mais pontos turísticos de graça?",
         "Em proporção, %s: %d de %d pontos do guia não cobram entrada. Metade ou mais dos pontos também é grátis "
         "em %s." % (metade[0]["nome"], metade[0]["gratis"], metade[0]["total"],
                     j(l["nome"] for l in metade[1:]))),
        ("Em qual destino os ingressos são mais baratos?",
         "Pela mediana dos ingressos pagos de cada guia, em reais: %s (%s), %s (%s) e %s (%s). Os mais caros: %s "
         "(%s) e %s (%s)." % (com_med[0]["nome"], reais(com_med[0]["mediana"]), com_med[1]["nome"],
                               reais(com_med[1]["mediana"]), com_med[2]["nome"], reais(com_med[2]["mediana"]),
                               com_med[-1]["nome"], reais(com_med[-1]["mediana"]), com_med[-2]["nome"],
                               reais(com_med[-2]["mediana"]))),
        ("Qual é o destino mais barato do site por dia?",
         "Ainda não dá para responder com honestidade: %d das fichas de custos não têm hospedagem (%s), e sem ela "
         "o custo por dia de uma cidade não se compara com o de outra. A comparação entra quando essas fichas "
         "tiverem diária apurada." % (len(sem_hosp), j(sem_hosp))),
    ]

    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Comparar destinos", "item": url}]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": limpa(a)}}
        for q, a in perguntas]}

    cabeca, pe = esqueleto()
    cabeca = re.sub(r"<title>.*?</title>", "<title>%s — Viagem na Lupa</title>" % H.escape(titulo), cabeca, flags=re.S)
    for prop, val in (("description", descricao),):
        cabeca = re.sub(r'<meta name="%s" content="[^"]*">' % prop,
                        '<meta name="%s" content="%s">' % (prop, H.escape(val, quote=True)), cabeca)
    cabeca = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url, cabeca)
    cabeca = re.sub(r'<meta property="og:title" content="[^"]*">',
                    '<meta property="og:title" content="%s — Viagem na Lupa">' % H.escape(titulo, quote=True), cabeca)
    cabeca = re.sub(r'<meta property="og:description" content="[^"]*">',
                    '<meta property="og:description" content="%s">' % H.escape(descricao, quote=True), cabeca)
    cabeca = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % url, cabeca)
    cabeca = cabeca.replace("</head>", "".join(
        '<script type="application/ld+json">%s</script>\n' % json.dumps(o, ensure_ascii=False, separators=(",", ":"))
        for o in (migalhas, faq)) + "</head>", 1)

    tabela = "".join(
        '<tr><td>%s</td><td class="n">%d de %d</td><td class="n">%s</td><td>%s</td><td>%s</td></tr>'
        % (nome_link(l), l["gratis"], l["total"],
           ("%s <span style=\"color:var(--nevoa)\">(%s)</span>" % (
               reais(l["mediana"]), ("%d pagos" % l["npagos"]) if l["npagos"] >= MIN_PAGOS
               else "só %d com preço único" % l["npagos"]))
           if l["mediana"] is not None else "—",
           ('%s · <a href="../destinos/%s/#%s">%s</a>' % (reais(l["maior"][0]), l["slug"], l["maior"][2],
                                                          H.escape(l["maior"][1]))) if l["maior"] else "—",
           ("%s <span style=\"color:var(--nevoa)\">· %s</span>" % (reais(l["diaria"][0]), l["diaria"][1]))
           if l["diaria"] else ('<span class="flag">Não apurada</span>' if l["tem_ficha"]
                                else '<span class="flag">Sem ficha</span>'))
        for l in linhas)

    def li(l, txt):
        return "<li>%s: %s</li>" % (nome_link(l), txt)

    partes = [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="../">Início</a> › Comparar destinos</p>\n',
        '<div class="hero">\n  <span class="eyebrow">Para escolher o destino</span>\n'
        '  <h1>%d destinos lado a lado</h1>\n' % n_cid,
        '  <p>Quantos pontos não cobram entrada, quanto custa o ingresso típico e o mais caro, e a diária que cada '
        'ficha usa, tudo convertido em reais pelo mesmo câmbio. Só entra o que tem a mesma base em todos os '
        'guias.</p>\n</div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
        '<section class="bloco"><div class="aviso a"><span class="t">Por que esta página não diz qual destino é o '
        'mais barato</span><p>O custo por dia de cada destino está na ficha de custos de cada um, mas a comparação '
        'ainda não é justa: <b>%d fichas não têm hospedagem</b> (%s): a apuração de cada uma não achou diária '
        'média publicada que servisse, e a ficha diz isso. Sem o hotel, Roma ou Salvador pareceriam mais baratos '
        'que o Rio só por falta de uma linha. O ranking por dia entra quando essas fichas tiverem diária.</p>%s'
        '</div></section>\n\n' % (len(sem_hosp), j(sem_hosp),
                                  ("<p>%s ainda não tem ficha de custos.</p>" % j(sem_ficha)) if sem_ficha else ""),
        '<section class="bloco" id="gratis">\n  <div class="bloco-head"><span class="eyebrow">Para gastar menos com '
        'entrada</span><h2>Onde metade ou mais dos pontos é grátis</h2></div>\n  <ul class="plain">%s</ul>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem">A mesma conta da <a href="../gratis/">lista dos pontos que '
        'não cobram entrada</a>, onde está o que cada um cobra à parte.</p>\n</section>\n\n'
        % "".join(li(l, "%d de %d pontos" % (l["gratis"], l["total"])) for l in metade),
        '<section class="bloco" id="ingressos">\n  <div class="bloco-head"><span class="eyebrow">O ingresso típico'
        '</span><h2>Onde entrar custa menos, e onde custa mais</h2><p>A mediana dos ingressos pagos de cada guia: '
        'metade custa menos que isso, metade custa mais. Um passeio caro sozinho não puxa o número.</p></div>\n'
        '  <ul class="plain">%s</ul>\n</section>\n\n'
        % ("".join(li(l, "%s, entre %d pontos pagos" % (reais(l["mediana"]), l["npagos"])) for l in com_med)
           + ("<li style=\"color:var(--nevoa)\">Fora desta lista, porque têm menos de %d pontos pagos com preço "
              "único: %s.</li>" % (MIN_PAGOS, j(l["nome"] for l in poucos)) if poucos else "")),
        '<section class="bloco" id="tabela">\n  <div class="bloco-head"><span class="eyebrow">Os %d destinos'
        '</span><h2>A tabela completa</h2></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Destino</th><th>Pontos grátis</th><th>Ingresso típico</th>'
        '<th>O mais caro</th><th>Diária na ficha</th></tr></thead><tbody>%s</tbody></table></div>\n</section>\n\n'
        % (n_cid, tabela),
        '<section class="bloco" id="metodo">\n  <div class="bloco-head"><span class="eyebrow">Como esta página foi '
        'feita</span><h2>As fontes e o que não entra</h2></div>\n  <ul class="plain">'
        '<li><b>Câmbio:</b> boletim de fechamento do Banco Central do Brasil de %s, taxa de venda, para as sete '
        'moedas dos guias. O valor em reais é conversão nossa: a do seu cartão será pior.</li>'
        '<li><b>Ingressos:</b> o preço de cada ponto que o guia publica como valor único. Faixa de preço, “a partir '
        'de” e fontes divergentes ficam fora, e por isso alguns pontos pagos não entram na conta.</li>'
        '<li><b>Diária:</b> a que a ficha de custos de cada destino usa, com a base que ela declara. Média oficial, '
        'cálculo sobre dado oficial e amostra não são a mesma coisa, e a tabela diz qual é qual.</li>'
        '<li><b>O que não entra:</b> passagem aérea, alimentação e transporte, que cada ficha apura de um jeito.</li>'
        '</ul>\n</section>\n\n' % DATA_BOLETIM,
        '<section class="bloco faq" id="perguntas">\n  <div class="bloco-head"><span class="eyebrow">Perguntas '
        'frequentes</span><h2>O que mais se pergunta ao comparar destinos</h2></div>%s\n</section>\n\n'
        % "".join('\n  <details class="faq-q"><summary><h3>%s</h3></summary><p>%s</p></details>' % (H.escape(q), a)
                  for q, a in perguntas),
        '</div>\n',
    ]
    pagina = cabeca + "".join(partes) + pe
    alvo = os.path.join(RAIZ, "comparar", "index.html")
    mudou = (not os.path.isfile(alvo)) or le(alvo) != pagina
    print("   /comparar/  %d destinos, %d com mediana, %d com diaria, %d sem hospedagem   %s"
          % (n_cid, len(com_med), sum(1 for l in linhas if l["diaria"]), len(sem_hosp),
             "escrito" if (aplica and mudou) else ("ja igual" if not mudou else "SO MOSTRANDO")))
    for l in linhas:
        print("      %-16s %2d/%2d  med %-9s  max %-9s  diaria %s" % (
            l["slug"], l["gratis"], l["total"], reais(l["mediana"]) if l["mediana"] is not None else "-",
            reais(l["maior"][0]) if l["maior"] else "-", ("%s (%s)" % (reais(l["diaria"][0]), l["diaria"][1]))
            if l["diaria"] else "-"))
    if aplica and mudou:
        escreve(alvo, pagina)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
