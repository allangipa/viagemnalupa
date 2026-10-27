# -*- coding: utf-8 -*-
"""Gera /comparar/: os destinos lado a lado, so no que e comparavel.

Pedido de 26/10/2026 (pagina de "inspiracao"). O ranking por dia ficou de
fora ate as fichas terem hotel (10 de 22 nao tinham). Em 27/10/2026, com 17
fichas com diaria, entrou o "dia tipico": UMA pessoa, quarto inteiro, uma
noite da diaria da ficha mais o resto da ficha (ingressos, transporte, taxa)
dividido pelos dias, SEM a alimentacao que so Maceio soma. Normaliza as tres
diferencas entre as fichas: duracao (3 a 7 dias), quarto (Buenos Aires
divide o apartamento por dois) e o que entra no total. As 5 sem hotel ficam
fora, nomeadas; a base de cada diaria (media oficial, amostra, categoria)
aparece ao lado do valor.

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
    q = le(p)
    cfg = json.loads(m.group(1))
    hp = {x["k"]: x for x in cfg.get("hosp") or []}.get(cfg.get("hospPadrao"))
    if cfg["moeda"] not in SIMBOLO:
        sys.exit("PARADO: moeda %s da ficha de %s sem codigo no boletim" % (cfg["moeda"], slug))
    resto = None
    if hp:
        # o resto por dia: total publicado menos a linha de hospedagem e a de
        # alimentacao, dividido pelos dias do roteiro
        def num(t):
            t = re.sub(r"[^\d,.]", "", t)
            return float(t.replace(".", "").replace(",", ".")) if t else 0.0

        def valor_da_linha(corpo):
            return num(re.findall(r"(?s)<td[^>]*>(.*?)</td>", corpo)[1])
        tot = num(re.search(r'class="n tot-val">([^<]*)', q).group(1))
        hrow = re.search(r'(?s)<tr data-tipo="hosp"[^>]*>(.*?)</tr>', q)
        if not hrow:
            sys.exit("PARADO: %s tem diaria no seletor e nao tem linha de hospedagem" % slug)
        alim = sum(valor_da_linha(c) for c in re.findall(r'(?s)<tr data-tipo="[^"]*"[^>]*>(<td>Alimenta.*?)</tr>', q))
        resto = (tot - valor_da_linha(hrow.group(1)) - alim) / cfg["dias"]
    return dict(moeda=SIMBOLO[cfg["moeda"]], hosp=hp, resto=resto, dias=cfg["dias"])


def base_da_diaria(rot):
    r = rot.lower()
    if "amostra" in r:
        return "amostra"
    if "painel" in r:
        return "painel do setor, via imprensa"
    if "gmcvb" in r:
        return "média do órgão de turismo"
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
        diaria = dia = None
        if ficha and ficha["hosp"]:
            diaria = (ficha["hosp"]["ref"] * taxas[ficha["moeda"]], base_da_diaria(ficha["hosp"]["rot"]),
                      ficha["hosp"]["rot"])
            dia = (diaria[0] + ficha["resto"] * taxas[ficha["moeda"]], ficha["resto"] * taxas[ficha["moeda"]],
                   ficha["dias"])
        linhas.append(dict(slug=slug, nome=nomes[slug], total=total, gratis=len(gratis), npagos=len(pagos),
                           mediana=med, maior=maior, diaria=diaria, dia=dia, tem_ficha=bool(ficha)))

    n_cid = len(linhas)
    sem_hosp = [l["nome"] for l in linhas if l["tem_ficha"] and not l["diaria"]]
    por_dia = sorted([l for l in linhas if l["dia"]], key=lambda l: l["dia"][0])
    sem_ficha = [l["nome"] for l in linhas if not l["tem_ficha"]]
    metade = sorted([l for l in linhas if l["total"] and l["gratis"] * 2 >= l["total"]],
                    key=lambda l: -l["gratis"] / l["total"])
    # Mediana de 1 ou 2 precos nao diz nada sobre a cidade: fica na tabela,
    # avisada, e fora do destaque e do FAQ.
    MIN_PAGOS = 3
    com_med = sorted([l for l in linhas if l["mediana"] is not None and l["npagos"] >= MIN_PAGOS],
                     key=lambda l: l["mediana"])
    poucos = [l for l in linhas if l["mediana"] is not None and l["npagos"] < MIN_PAGOS]

    def minus(t):
        return t[:1].lower() + t[1:]

    def j(itens):
        itens = list(itens)
        return itens[0] if len(itens) == 1 else ", ".join(itens[:-1]) + " e " + itens[-1]

    def nome_link(l):
        return '<a href="../destinos/%s/">%s</a>' % (l["slug"], H.escape(l["nome"]))

    titulo = "Quanto custa um dia em %d cidades, do mais barato ao mais caro, em reais" % len(por_dia)
    descricao = ("Um dia de viagem, com hotel, ingressos e transporte, em %d cidades: de %s (%s) a %s (%s). E os "
                 "%d destinos do site lado a lado em pontos grátis, ingresso típico e diária, pelo câmbio do Banco "
                 "Central." % (len(por_dia), por_dia[0]["nome"], reais(por_dia[0]["dia"][0]), por_dia[-1]["nome"],
                               reais(por_dia[-1]["dia"][0]), n_cid))
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
         "Entre as %d cidades com hotel na ficha, %s: um dia típico custa %s, com hotel, ingressos e transporte, "
         "para uma pessoa. Depois vêm %s (%s) e %s (%s). O mais caro é %s, a %s. %s ficam fora, porque a ficha não "
         "tem diária de hotel." % (len(por_dia), por_dia[0]["nome"], reais(por_dia[0]["dia"][0]), por_dia[1]["nome"],
                                   reais(por_dia[1]["dia"][0]), por_dia[2]["nome"], reais(por_dia[2]["dia"][0]),
                                   por_dia[-1]["nome"], reais(por_dia[-1]["dia"][0]), j(sem_hosp))
         + ((" Ressalva: a diária de %s é %s, não a média da cidade inteira." % (
             por_dia[0]["nome"], minus(por_dia[0]["diaria"][2])))
            if por_dia[0]["diaria"][1] in ("amostra", "a ficha não diz a base") else "")),
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
        '  <h1>Quanto custa um dia em cada destino</h1>\n',
        '  <p>Um dia de viagem para uma pessoa, com hotel, ingressos e transporte, em %d cidades, do mais barato '
        'ao mais caro. Depois, os %d destinos do site lado a lado em pontos grátis e ingresso típico. Tudo em reais '
        'pelo mesmo câmbio.</p>\n</div>\n</div></div>\n\n' % (len(por_dia), n_cid),
        '<div class="wrap wrap-estreito">\n',
        '<section class="bloco" id="por-dia">\n  <div class="bloco-head"><span class="eyebrow">Um dia típico, por '
        'pessoa</span><h2>Do mais barato ao mais caro</h2><p>Uma noite de hotel, no quarto inteiro, mais o resto '
        'da ficha de custos (ingressos, transporte e taxa) dividido pelos dias do roteiro. Sem passagem aérea e sem '
        'alimentação.</p></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th></th><th>Destino</th><th>Um dia</th><th>Hotel, 1 noite</th>'
        '<th>O resto, por dia</th></tr></thead><tbody>%s</tbody></table></div>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem"><b>Leia a coluna do hotel antes de comparar.</b> Em umas '
        'cidades a diária é a média oficial da cidade inteira; em outras é amostra ou uma categoria (intermediário, '
        'econômico, apartamento), e a tabela diz qual é qual.%s</p>\n'
        '</section>\n\n' % (" O hotel é o maior item do dia em todos eles." if all(
            l["diaria"][0] > l["dia"][1] for l in por_dia) else "", "".join(
            '<tr><td class="n">%d</td><td>%s</td><td class="n"><b>%s</b></td><td class="n">%s <span style="color:'
            'var(--nevoa)">· %s</span></td><td class="n">%s</td></tr>'
            % (i, nome_link(l), reais(l["dia"][0]), reais(l["diaria"][0]), H.escape(l["diaria"][2]),
               reais(l["dia"][1])) for i, l in enumerate(por_dia, 1))),
        '<section class="bloco"><div class="aviso a"><span class="t">As %d cidades que ficam fora do ranking'
        '</span><p>%s: a ficha de custos de cada um não tem diária de hotel, porque a apuração não achou diária '
        'média publicada que servisse, e a ficha diz isso. Sem o hotel, essas cidades pareceriam mais baratas do '
        'que são, só por falta de uma linha. Elas continuam na comparação de pontos grátis e ingressos, abaixo.</p>%s'
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
