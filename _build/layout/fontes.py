# -*- coding: utf-8 -*-
"""Tira o CSS do Google Fonts do caminho da primeira pintura.

PageSpeed de 18/10/2026, celular (4G lento, CPU 4x): FCP 4,9 s, LCP 8,1 s,
com HTML de 13 KB e CSS de 14 KB comprimidos - o peso nao era o problema,
a espera era. A tag <link rel="stylesheet"> do fonts.googleapis.com e
bloqueante: o navegador nao pinta nada ate esse CSS (16 KB, outra origem)
chegar. E ele ja vem com display=swap, ou seja, o texto JA aparecia na
fonte de reserva e trocava depois. Bloquear a pintura so para esperar um
CSS que, chegando, manda pintar com a reserva nao faz sentido.

O QUE MUDA: a tag passa a media="print", que o navegador baixa sem
bloquear e com prioridade baixa (deixa a foto do hero na frente), e no
onload vira media="all". Um <noscript> repete a tag bloqueante para quem
esta sem JavaScript. A troca de fonte (FOUT) e a mesma de antes - swap ja
era swap; o que sai e a espera pelo CSS.

E POS-PROCESSADOR, como assinatura.py: a tag e identica nas 68 paginas e
nos cinco geradores, e o script aceita os .py tambem para a pagina nova ja
nascer certa. Idempotente.

Uso
---
    python _build/layout/fontes.py            # so mostra
    python _build/layout/fontes.py --aplica   # escreve, paginas e geradores
"""
import glob
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
PULA = ("_build", "Claude outputs", ".git", "node_modules")

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# a copia dentro do <noscript> e bloqueante de proposito e fica fora do padrao
BLOQUEANTE = re.compile(r'(?<!<noscript>)<link rel="stylesheet" href="(https://fonts\.googleapis\.com/css2\?[^"]*)">')
JA = re.compile(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]*" media="print"')
GERADORES = ("lisboa/build.py", "rio/build.py", "novos/gera.py", "novos/gera_custos.py", "novos/gera_roteiro.py")


def troca(m):
    u = m.group(1)
    return ('<link rel="stylesheet" href="%s" media="print" onload="this.media=\'all\'">'
            '<noscript><link rel="stylesheet" href="%s"></noscript>' % (u, u))


def paginas():
    for base, pastas, arquivos in os.walk(RAIZ):
        pastas[:] = [d for d in pastas if d not in PULA]
        for a in arquivos:
            if a.endswith(".html"):
                yield os.path.join(base, a)


def main(aplica):
    alvos = sorted(paginas()) + [os.path.join(RAIZ, "_build", g) for g in GERADORES]
    feitos = iguais = 0
    for p in alvos:
        h = io.open(p, encoding="utf-8").read()
        if JA.search(h) and not BLOQUEANTE.search(h):
            iguais += 1
            continue
        h2 = BLOQUEANTE.sub(troca, h, count=1)
        if h2 == h:
            continue
        feitos += 1
        if aplica:
            io.open(p, "w", encoding="utf-8", newline="").write(h2)
        print("   %s %s" % ("feito " if aplica else "faria ", os.path.relpath(p, RAIZ)))
    print("   %d trocado(s), %d ja certo(s)   %s" % (feitos, iguais, "escrito" if aplica else "SO MOSTRANDO"))


if __name__ == "__main__":
    main("--aplica" in sys.argv)
