# -*- coding: utf-8 -*-
"""Tira o link do YouTube da nav - das paginas publicadas E dos geradores.

O Allan, em 17/10/2026: "pode apagar as citacoes ao YouTube pois ainda nao
movimentei o canal". O link estava na nav das 67 paginas e em cinco
geradores (lisboa/build.py, rio/build.py, novos/gera.py, gera_custos.py,
gera_roteiro.py). Tirar so do HTML nao basta: a proxima regeracao traria
de volta. Por isso este script passa nos dois lugares.

Sem o link a nav fica Destinos · Calculadora · Sobre - que tambem alivia o
cabecalho no celular (visual 3 do _build/docs/concorrentes-2026-10-17.md).

Quando o canal existir, o lugar dele e aqui de novo, ao contrario; ou o
Instagram, que hoje so esta na assinatura.

Idempotente: se nao ha o link, nao escreve.

Uso
---
    python _build/layout/sem_youtube.py            # so mostra
    python _build/layout/sem_youtube.py --aplica   # escreve
"""
import glob
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# O <a> inteiro, com o <span> de leitor de tela e o <svg> da seta dentro.
LINK = re.compile(r'\s*<a class="externo" href="https://www\.youtube\.com/@viagemnalupa"'
                  r'[^>]*>.*?</a>', re.S)


def arquivos():
    for p in glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True):
        if any(x in p for x in ("_build", "Claude outputs", "node_modules")):
            continue
        yield p
    for p in ("lisboa/build.py", "rio/build.py", "novos/gera.py",
              "novos/gera_custos.py", "novos/gera_roteiro.py"):
        yield os.path.join(RAIZ, "_build", p)


def main(aplica):
    tocados = sobras = 0
    for p in arquivos():
        with open(p, encoding="utf-8") as f:
            h = f.read()
        h2, n = LINK.subn("", h)
        if n:
            tocados += 1
            if aplica:
                with open(p, "w", encoding="utf-8", newline="") as f:
                    f.write(h2)
        if "youtube" in h2.lower():
            sobras += 1
            rel = os.path.relpath(p, RAIZ).replace(os.sep, "/")
            for m in re.finditer(r"[^\n]{0,70}youtube[^\n]{0,70}", h2, re.I):
                print("   ainda cita: %-40s %s" % (rel, m.group(0).strip()[:110]))
    print("   %d arquivo(s) com o link tirado; %d ainda citam YouTube fora da nav   %s"
          % (tocados, sobras, "escrito" if aplica else "SO MOSTRANDO"))


if __name__ == "__main__":
    main("--aplica" in sys.argv)
