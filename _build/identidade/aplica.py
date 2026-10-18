# -*- coding: utf-8 -*-
"""Poe a marca nova, o favicon e o og:image em todas as paginas.

A MARCA
-------
O simbolo antigo era um circulo ambar com um zigue-zague ciano - chapado
demais ao lado do resto do site. O novo e uma lupa sobre um globo, gerado
no Higgsfield (Nano Banana Pro) e depois simplificado a mao para o
cabecalho, porque marca detalhada e quadro de 30 px sao objetivos que
brigam entre si.

Em 18/10/2026 o render deu lugar ao emblema de kit.py (GPT Image 2.5,
candidata 2 de quatro): mesmos elementos, tratamento de distintivo sobre
fundo carvao, que segura a 110 px no avatar do Instagram. Os arquivos
trocaram de conteudo, nao de nome - este script nao precisou rodar de
novo. Em seguida o cabecalho tambem passou ao emblema, em PNG com alfa.

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

# A marca do cabecalho e um PNG com alfa (identidade/kit.py, 18/10/2026):
# o emblema renderizado, recortado pelo disco do aro. Nao segue o tema -
# o distintivo escuro e o proprio fundo dele, e le nos dois. O arquivo de
# 64 px serve o 2x das telas retina; o SVG com variaveis que estava aqui
# saiu porque o Allan quis o emblema novo como padrao.
def marca(prefixo):
    return ('<img src="%sassets/img/marca-cabecalho-64.png" width="30" height="30" '
            'alt="" decoding="async">' % prefixo)


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
    m = re.search(r'(<a class="marca" href="([^"]*)">)(<svg.*?</svg>|<img[^>]*>)(<span>)', h, re.S)
    if not m:
        avisos.append((p, "nao achei <a class=\"marca\"> com svg ou img"))
        continue
    prefixo = m.group(2)
    if m.group(3) != marca(prefixo):
        h = h[:m.start(3)] + marca(prefixo) + h[m.end(3):]
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
