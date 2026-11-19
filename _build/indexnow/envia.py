# -*- coding: utf-8 -*-
"""Avisa o IndexNow (Bing, Yandex, Seznam, Naver) das paginas que mudaram.

O Google nao le o IndexNow; para ele continua valendo o sitemap e o pedido
manual no Search Console. O Bing le, e alimenta o Copilot e o DuckDuckGo.

A chave e publica por desenho: fica em /<chave>.txt na raiz do site, e e
por esse arquivo que o buscador confere que o aviso veio do dono.

Uso
---
    python _build/indexnow/envia.py --tudo               # todo o sitemap (so mostra)
    python _build/indexnow/envia.py --tudo --aplica      # envia
    python _build/indexnow/envia.py --desde <sha> --aplica   # so o que mudou desde o commit

Roda sozinho no push, pela Action .github/workflows/indexnow.yml.
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://viagemnalupa.com.br"
HOST = "viagemnalupa.com.br"
CHAVE = "7d02cf38774f33514c5275ec84629c59"


def do_sitemap():
    with open(os.path.join(RAIZ, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def mudadas(desde):
    """As URLs do sitemap cujo index.html mudou entre <desde> e HEAD."""
    r = subprocess.run(["git", "diff", "--name-only", desde, "HEAD"], cwd=RAIZ, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("PARADO: git diff falhou: " + r.stderr.strip())
    urls = set()
    for arq in r.stdout.splitlines():
        if arq == "index.html":
            urls.add(SITE + "/")
        elif arq.endswith("/index.html"):
            urls.add("%s/%s/" % (SITE, arq[:-len("/index.html")]))
    no_mapa = set(do_sitemap())
    return sorted(urls & no_mapa)


def main():
    if "--tudo" in sys.argv:
        urls = do_sitemap()
    elif "--desde" in sys.argv:
        urls = mudadas(sys.argv[sys.argv.index("--desde") + 1])
    else:
        sys.exit(__doc__)
    print("%d URL(s)" % len(urls))
    for u in urls[:12]:
        print("  ", u)
    if len(urls) > 12:
        print("   ... e mais %d" % (len(urls) - 12))
    if not urls:
        return
    if "--aplica" not in sys.argv:
        print("Nada foi enviado. Rode com --aplica.")
        return
    # a chave tem de estar no ar antes: sem ela o IndexNow devolve 403
    with urllib.request.urlopen("%s/%s.txt" % (SITE, CHAVE), timeout=30) as r:
        if r.read().decode("utf-8").strip() != CHAVE:
            sys.exit("PARADO: o arquivo da chave no ar nao bate com a chave")
    corpo = json.dumps({"host": HOST, "key": CHAVE, "keyLocation": "%s/%s.txt" % (SITE, CHAVE),
                        "urlList": urls}).encode("utf-8")
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=corpo,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow respondeu", r.status)      # 200 ou 202 = aceito


if __name__ == "__main__":
    main()
