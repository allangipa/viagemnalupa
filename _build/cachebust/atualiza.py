# -*- coding: utf-8 -*-
"""Poe o hash do arquivo real em cada ?v= do site.

Por que
-------
O .htaccess manda o navegador guardar css e js por um ano, com
"immutable". Isso so e seguro porque o endereco carrega o hash do
conteudo: mudou o arquivo, muda o ?v=, o navegador busca de novo.

Quando alguem edita o css e esquece de mexer no ?v=, o leitor que ja
visitou continua vendo o site com o css velho - por um ano. E nao ha
erro em lugar nenhum: a pagina carrega, so que errada, e so para quem ja
tinha estado la. Isso ja aconteceu neste site, em tres paginas.

Manter 30 referencias iguais na mao nao e trabalho de gente. O hash
passa a vir do arquivo.

Uso
---
    python _build/cachebust/atualiza.py            # so mostra
    python _build/cachebust/atualiza.py --aplica   # escreve
"""
import hashlib
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def hash_de(caminho):
    with open(caminho, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def paginas():
    for dirp, _, arqs in os.walk(RAIZ):
        if any(x in dirp for x in ("_build", ".git", "Claude outputs", "node_modules")):
            continue
        for a in arqs:
            if a.endswith(".html"):
                yield os.path.join(dirp, a)


def main(aplica):
    # descobre o hash de cada arquivo versionado que existe em disco
    reais = {}
    for sub, ext in (("css", ".css"), ("js", ".js")):
        pasta = os.path.join(RAIZ, "assets", sub)
        if not os.path.isdir(pasta):
            continue
        for a in sorted(os.listdir(pasta)):
            if a.endswith(ext):
                reais[a] = hash_de(os.path.join(pasta, a))

    print("=== hash do arquivo em disco ===")
    for a, h in reais.items():
        print("   %-16s %s" % (a, h))

    alvo = re.compile(r'(assets/(?:css|js)/([\w.\-]+))\?v=([0-9a-f]+)')
    mudou, ok, orfaos = [], 0, set()

    for p in paginas():
        rel = "/" + os.path.relpath(p, RAIZ).replace(os.sep, "/")
        with open(p, encoding="utf-8") as f:
            h = f.read()
        novo = h
        for m in alvo.finditer(h):
            arq, atual = m.group(2), m.group(3)
            certo = reais.get(arq)
            if certo is None:
                orfaos.add((rel, arq))
                continue
            if atual != certo:
                novo = novo.replace("%s?v=%s" % (m.group(1), atual),
                                    "%s?v=%s" % (m.group(1), certo))
                mudou.append((rel, arq, atual, certo))
            else:
                ok += 1
        if aplica and novo != h:
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(novo)

    print()
    print("=== referencias ===")
    for rel, arq, a, b in mudou:
        print("   %-46s %s  %s -> %s" % (rel, arq, a, b))
    if not mudou:
        print("   nenhuma defasada")
    print()
    print("ja corretas: %d   corrigidas: %d" % (ok, len(mudou)))
    if orfaos:
        print()
        print("!!! apontam para arquivo que nao existe:")
        for rel, arq in sorted(orfaos):
            print("   %s -> %s" % (rel, arq))
        return 1
    if not aplica and mudou:
        print("Nada foi alterado. Rode com --aplica para escrever.")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplica" in sys.argv))
