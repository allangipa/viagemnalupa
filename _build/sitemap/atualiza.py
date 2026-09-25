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


def paginas():
    """Todo .html publicavel do site, em disco."""
    for dirp, _, arqs in os.walk(RAIZ):
        if any(x in dirp for x in ("_build", ".git", "Claude outputs",
                                   ".claude", "node_modules")):
            continue
        for a in arqs:
            if a.endswith(".html"):
                yield os.path.join(dirp, a)


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
        r"<url><loc>([^<]+)</loc><lastmod>([^<]*)</lastmod>", troca, xml)

    # Pagina que existe em disco e nao esta no mapa.
    #
    # Este script so sabia corrigir data. Quando Cancun e Fortaleza foram
    # publicadas, as fichas entraram no ar e o sitemap continuou com 29
    # URLs, sem erro em lugar nenhum - a pagina simplesmente nao existia
    # para quem le o mapa. Agora ele acrescenta.
    no_mapa = set(re.findall(r"<loc>([^<]+)</loc>", saida))
    novas = []
    for p in sorted(paginas()):
        rel = os.path.relpath(p, RAIZ).replace(os.sep, "/")
        if rel == "404.html":
            continue                      # pagina de erro nao se indexa
        url = SITE + "/" + (rel[:-len("index.html")] if rel.endswith("index.html")
                            else rel)
        if url in no_mapa:
            continue
        # <lastmod> VAZIO E INVALIDO, e era o que saia aqui.
        #
        # data_do_commit devolve None para arquivo ainda nao commitado, e
        # a pagina entra no mapa no mesmo lote em que e criada - ou seja,
        # sempre antes do commit. O "or \"\"" virava <lastmod></lastmod>,
        # que o protocolo nao aceita, em 14 das 45 URLs: Cancun, Fortaleza,
        # Bariloche, Punta Cana, Porto e Sevilha, os seis destinos mais
        # novos. Treze delas estao hoje como "Detectada, mas nao indexada".
        #
        # E nao se curava na rodada seguinte: o regex de conserto pedia
        # [^<]+ e tag vazia nao casa com "um ou mais".
        #
        # Sem data confiavel, a tag nao entra. Ausente e valido; vazia nao.
        d = data_do_commit(p)
        prof = url[len(SITE):].strip("/").count("/")
        prio = "0.9" if prof <= 1 else ("0.8" if prof == 2 else "0.7")
        lm = "<lastmod>%s</lastmod>" % d if d else ""
        novas.append('<url><loc>%s</loc>%s'
                     '<changefreq>weekly</changefreq><priority>%s</priority></url>'
                     % (url, lm, prio))
    if novas:
        print()
        print("=== entraram no mapa agora ===")
        for n in novas:
            print("   " + re.search(r"<loc>([^<]+)</loc>", n).group(1))
        saida = saida.replace("</urlset>", "\n".join(novas) + "\n</urlset>", 1)

    for url, velha, nova in mudou:
        print("  %-52s %s -> %s" % (url[len(SITE):] or "/", velha, nova))
    if faltando:
        print()
        print("  !!! no sitemap mas sem arquivo em disco:")
        for u in faltando:
            print("      " + u)

    print()
    print("%s: %d data(s) atualizada(s), %d ja corretas, %d URL(s) nova(s)."
          % ("Escrito" if aplica else "Faria", len(mudou), iguais, len(novas)))
    if aplica and (mudou or novas):
        with open(MAPA, "w", encoding="utf-8", newline="") as f:
            f.write(saida)
    elif not aplica:
        print("Nada foi alterado. Rode com --aplica para escrever.")
    return 1 if faltando else 0


if __name__ == "__main__":
    sys.exit(main("--aplica" in sys.argv))
