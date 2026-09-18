# -*- coding: utf-8 -*-
"""Cartao de destino sem o link que cobre o retangulo inteiro.

O Allan: "Nao esta abrindo bariloche e punta cana clicando no retangulo.
So quando clica em guias."

Os dez cartoes antigos terminam com

    <a class="dest-link" href="..." tabindex="-1" aria-hidden="true"></a>

e o CSS faz esse link cobrir o cartao:

    .dest{position:relative}
    .dest-link{position:absolute; inset:0; z-index:1}
    .dest .paginas{position:relative; z-index:2}

Os dois cartoes que eu gerei nao tinham. Copiei o molde e parei antes do
ultimo elemento - o unico que nao aparece na tela, e por isso o unico que
nao se nota faltando ao olhar a pagina.

tabindex=-1 e aria-hidden porque o link do titulo ja da o nome acessivel
ao cartao; este aqui e so para o mouse. Repetir o mesmo destino no
teclado seria ruido para quem navega por tabulacao.

Uso
---
    python _build/conserto/dest_link.py
    python _build/conserto/dest_link.py --aplica
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

CARTAO = re.compile(r"(?s)<article class=\"dest\".*?</article>")


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def main(aplica):
    total = 0
    for rel in ("index.html", os.path.join("destinos", "index.html")):
        p = os.path.join(RAIZ, rel)
        if not os.path.isfile(p):
            continue
        h = le(p)
        faltam = []

        def um(m):
            b = m.group(0)
            if 'class="dest-link"' in b:
                return b
            # o destino sai do link do titulo, que todo cartao tem
            alvo = re.search(r'<h3><a href="([^"]+)"', b)
            if not alvo:
                faltam.append(("?", "sem link no titulo"))
                return b
            href = alvo.group(1)
            nome = re.search(r'<h3><a[^>]*>([^<]+)</a>', b)
            faltam.append((nome.group(1) if nome else href, href))
            return b.replace(
                "</article>",
                '<a class="dest-link" href="%s" tabindex="-1" '
                'aria-hidden="true"></a></article>' % href)

        novo = CARTAO.sub(um, h)
        n = len(re.findall(r'<article class="dest"', h))
        print("%-22s %d cartao(oes), %d sem o link do retangulo"
              % (rel, n, len(faltam)))
        for nome, href in faltam:
            print("     %-16s -> %s" % (nome, href))
        total += len(faltam)
        if aplica and novo != h:
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(novo)

    print()
    if not total:
        print("Todos os cartoes ja abrem pelo retangulo.")
    elif aplica:
        print("Escrito: %d cartao(oes) consertado(s)." % total)
    else:
        print("Faria: %d. Nada alterado. Rode com --aplica." % total)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
