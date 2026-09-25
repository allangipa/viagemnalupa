# -*- coding: utf-8 -*-
"""Poe a marca nova, o favicon e o og:image em todas as paginas.

A MARCA
-------
O simbolo antigo era um circulo ambar com um zigue-zague ciano - chapado
demais ao lado do resto do site. O novo e uma lupa sobre um globo, gerado
no Higgsfield (Nano Banana Pro) e depois simplificado a mao para o
cabecalho, porque marca detalhada e quadro de 30 px sao objetivos que
brigam entre si.

E ELA USA AS VARIAVEIS DO SITE, NAO COR FIXA
--------------------------------------------
    var(--card)   o corpo do globo
    var(--ciano)  meridianos e equador
    var(--noite)  o vidro da lente
    var(--ambar)  o aro e o cabo

O site nao tem tema fixo: segue o `prefers-color-scheme` de quem le. Cor
fixa obrigaria a dois arquivos e a um truque de CSS para trocar entre
eles; com variavel, a marca vira junto com a pagina de graca.

O FAVICON
---------
Era um data-URI com o simbolo antigo, embutido em toda pagina. Vira
arquivo PNG, que e o que iOS e Android sabem usar como icone de atalho -
o apple-touch-icon leva fundo solido de proposito, porque o iOS troca
alfa por preto.

O OG:IMAGE, QUE E O QUE MAIS FALTAVA
------------------------------------
Estava em 2 paginas de 45. Nas outras 43, colar o link num grupo de
WhatsApp mandava um retangulo cinza. A URL e ABSOLUTA de proposito: robo
de rede social nao resolve caminho relativo.

Uso
---
    python _build/identidade/aplica.py
    python _build/identidade/aplica.py --aplica
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
APLICA = "--aplica" in sys.argv

# tres niveis: aplica.py -> identidade -> _build -> raiz do site.
# Com dois, o os.walk varria o proprio _build e nao achava pagina
# nenhuma - e o script fechava com "0 paginas" sem erro nenhum.
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://viagemnalupa.com.br"
PULA = (".git", "_build", "Claude outputs", "node_modules")

# Cada var() leva um valor de reserva, que e o do tema escuro. Sem ele,
# uma pagina que carregue sem a folha de estilo - CDN fora do ar, rede
# ruim no meio do caminho - renderiza a marca INTEIRA sem cor, porque
# toda cor dela vem de variavel. A marca antiga tinha cor fixa e nunca
# sumia; esta so nao some por causa da reserva.
SVG = (
    '<svg width="30" height="30" viewBox="0 0 100 100" fill="none" aria-hidden="true">'
    '<circle cx="46" cy="46" r="33" fill="var(--card, #18304A)"></circle>'
    '<circle cx="46" cy="46" r="33" stroke="var(--ciano, #43D3C2)" stroke-width="3.5"></circle>'
    '<ellipse cx="46" cy="46" rx="33" ry="12.5" stroke="var(--ciano, #43D3C2)" stroke-width="2.5"></ellipse>'
    '<ellipse cx="46" cy="46" rx="13" ry="33" stroke="var(--ciano, #43D3C2)" stroke-width="2.5"></ellipse>'
    '<path d="M60.5 58.5 L78 76" stroke="var(--ambar, #FFB703)" stroke-width="8" stroke-linecap="round"></path>'
    '<circle cx="46" cy="44" r="20" fill="var(--noite, #122334)"></circle>'
    '<circle cx="46" cy="44" r="20" stroke="var(--ambar, #FFB703)" stroke-width="7"></circle>'
    '</svg>')


def icones(prefixo):
    return ('<link rel="icon" href="%sassets/img/favicon-32.png" sizes="32x32">'
            '<link rel="icon" href="%sassets/img/favicon-512.png" sizes="512x512">'
            '<link rel="apple-touch-icon" href="%sassets/img/apple-touch-icon.png">'
            % (prefixo, prefixo, prefixo))


OG = ('<meta property="og:image" content="%s/assets/img/og-image.png">'
      '<meta property="og:image:width" content="1200">'
      '<meta property="og:image:height" content="630">'
      '<meta property="og:image:alt" content="Viagem na Lupa — todo preço tem fonte e data.">'
      '<meta name="twitter:image" content="%s/assets/img/og-image.png">' % (SITE, SITE))


def paginas():
    for r, ds, fs in os.walk(RAIZ):
        ds[:] = [d for d in ds if d not in PULA and not d.startswith(".")]
        for f in sorted(fs):
            if f.endswith(".html"):
                yield os.path.join(r, f)


mudadas, avisos = [], []
for p in paginas():
    h = io.open(p, encoding="utf-8").read()
    antes = h
    feito = []

    # 1. a marca. O prefixo relativo sai do href que ja esta la, em vez de
    #    ser deduzido da profundidade da pasta - assim uma pagina em lugar
    #    incomum nao quebra em silencio.
    m = re.search(r'(<a class="marca" href="([^"]*)">)(<svg.*?</svg>)(<span>)', h, re.S)
    if not m:
        avisos.append((p, "nao achei <a class=\"marca\"> com svg"))
        continue
    prefixo = m.group(2)
    if m.group(3) != SVG:
        h = h[:m.start(3)] + SVG + h[m.end(3):]
        feito.append("marca")

    # 2. favicon
    if 'assets/img/favicon-32.png' not in h:
        novo = icones(prefixo)
        h2 = re.sub(r'<link rel="icon"[^>]*>', novo, h, count=1)
        if h2 != h:
            h = h2
            feito.append("icones")
        else:
            avisos.append((p, "nao achei <link rel=\"icon\">"))

    # 3. og:image, depois do og:url, que toda pagina tem
    if "og:image" not in h:
        m2 = re.search(r'<meta property="og:url"[^>]*>', h)
        if m2:
            h = h[:m2.end()] + OG + h[m2.end():]
            feito.append("og:image")
        else:
            avisos.append((p, "sem og:url para ancorar o og:image"))

    if h != antes:
        mudadas.append((os.path.relpath(p, RAIZ), feito))
        if APLICA:
            io.open(p, "w", encoding="utf-8", newline="").write(h)

print("%-52s %s" % ("pagina", "o que mudou"))
for rel, feito in mudadas[:6]:
    print("%-52s %s" % (rel, ", ".join(feito)))
if len(mudadas) > 6:
    print("... e mais %d" % (len(mudadas) - 6))
print()
from collections import Counter
c = Counter(x for _, f in mudadas for x in f)
print("%d pagina(s):  %s" % (len(mudadas), dict(c)))
if avisos:
    print("\nAVISOS:")
    for p, a in avisos:
        print("   %-46s %s" % (os.path.relpath(p, RAIZ), a))
if not APLICA:
    print("\nNada escrito. Rode com --aplica.")
