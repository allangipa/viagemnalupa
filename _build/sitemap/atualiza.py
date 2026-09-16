# -*- coding: utf-8 -*-
"""Poe no sitemap a data real da ultima alteracao de cada pagina.

Por que
-------
<lastmod> e o sinal que diz ao Google "esta pagina mudou, vale voltar".
Se ele fica parado numa data antiga enquanto o arquivo muda, o sinal vira
ruido - e pior: mentira, porque anuncia que nada mudou quando mudou.

Mantido na mao, esse campo envelhece sempre. Entao nao e mantido na mao:
a data vem do ultimo commit que tocou o arquivo. Enquanto o site for
publicado por git, isso e verdade por construcao.

Uso
---
    python _build/sitemap/atualiza.py            # so mostra
    python _build/sitemap/atualiza.py --aplica   # escreve
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://viagemnalupa.com.br"
MAPA = os.path.join(RAIZ, "sitemap.xml")

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def acha_git():
    """No Windows o git nem sempre esta no PATH do shell que roda isto."""
    for c in ("git",
              r"C:\Program Files\Git\cmd\git.exe",
              r"C:\Program Files (x86)\Git\cmd\git.exe",
              os.path.expandvars(r"%LOCALAPPDATA%\Programs\Git\cmd\git.exe")):
        try:
            subprocess.run([c, "--version"], capture_output=True, check=True)
            return c
        except Exception:
            continue
    return None


GIT = acha_git()


def arquivo_de(url):
    rel = url[len(SITE):].split("#")[0].split("?")[0].lstrip("/")
    if rel == "" or rel.endswith("/"):
        return os.path.join(RAIZ, rel.replace("/", os.sep), "index.html")
    return os.path.join(RAIZ, rel.replace("/", os.sep))


def data_do_commit(caminho):
    """Data do ultimo commit que tocou o arquivo, no formato AAAA-MM-DD."""
    if GIT is None:
        return None
    r = subprocess.run([GIT, "log", "-1", "--format=%cs", "--", caminho],
                       capture_output=True, text=True, cwd=RAIZ)
    d = (r.stdout or "").strip()
    return d if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) else None


def main(aplica):
    if GIT is None:
        print("git nao encontrado - sem historico, sem data confiavel.")
        return 1
    if not os.path.isfile(MAPA):
        print("sitemap.xml nao encontrado.")
        return 1

    with open(MAPA, encoding="utf-8") as f:
        xml = f.read()

    mudou, iguais, faltando = [], 0, []

    def troca(m):
        nonlocal iguais
        bloco, url, velha = m.group(0), m.group(1), m.group(2)
        arq = arquivo_de(url)
        if not os.path.isfile(arq):
            faltando.append(url)
            return bloco
        nova = data_do_commit(arq)
        if nova is None or nova == velha:
            iguais += 1
            return bloco
        mudou.append((url, velha, nova))
        return bloco.replace("<lastmod>%s</lastmod>" % velha,
                             "<lastmod>%s</lastmod>" % nova)

    saida = re.sub(
        r"<url><loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", troca, xml)

    for url, velha, nova in mudou:
        print("  %-52s %s -> %s" % (url[len(SITE):] or "/", velha, nova))
    if faltando:
        print()
        print("  !!! no sitemap mas sem arquivo em disco:")
        for u in faltando:
            print("      " + u)

    print()
    print("%s: %d data(s) atualizada(s), %d ja corretas."
          % ("Escrito" if aplica else "Faria", len(mudou), iguais))
    if aplica and mudou:
        with open(MAPA, "w", encoding="utf-8", newline="") as f:
            f.write(saida)
    elif not aplica:
        print("Nada foi alterado. Rode com --aplica para escrever.")
    return 1 if faltando else 0


if __name__ == "__main__":
    sys.exit(main("--aplica" in sys.argv))
