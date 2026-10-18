# -*- coding: utf-8 -*-
"""Poe a linha de assinatura logo abaixo da abertura, nas paginas de destino.

    Apurado por Allan Vitor · @viagemnalupabr

Nasceu do _build/docs/concorrentes-2026-10-17.md: as seis materias que
ranqueiam nas nossas buscas tem autor com nome e bio; nos tinhamos ZERO em
67 paginas, e a pagina Sobre nao citava pessoa. A proposicao do site e "nos
conferimos" - e ninguem estava nomeado.

O segundo link vai ao Instagram, nao ao WhatsApp. O Allan decidiu em
17/10/2026: a conta @viagemnalupabr acabou de nascer, e o site e o unico
ativo que manda gente para la. Os concorrentes poem "compartilhar no
WhatsApp" no mesmo lugar; o nosso lugar e este.

E POS-PROCESSADOR, COMO O atalhos.py, DE PROPOSITO
--------------------------------------------------
Os guias sao gerados pelo novos/gera.py; a ficha e o roteiro, pelos
gera_custos.py e gera_roteiro.py de cada cidade; Nova York, Porto, Rio e
Lisboa sao mantidos a mao ou por lib.py. Ensinar a assinatura a cada um
desses e cinco mudancas. Um pos-processador na cadeia e uma - e, como o
LEIA-ME avisa, "regerar uma pagina desfaz o que veio depois dela": este
script repoe.

Idempotente: se a linha ja existe, e TROCADA (para o texto poder mudar);
se nao existe, e posta. Rodar duas vezes nao duplica.

Onde ancora: no primeiro </p> depois do </h1>, que nos tres tipos de
pagina e a abertura. O <h1> esta dentro do hero; a assinatura entra no
mesmo bloco, antes do </div> que o fecha.

Uso
---
    python _build/layout/assinatura.py            # so mostra
    python _build/layout/assinatura.py --aplica   # escreve
"""
import glob
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

NOME = "Allan Vitor"
INSTAGRAM = "https://www.instagram.com/viagemnalupabr/"
ARROBA = "@viagemnalupabr"

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def paginas():
    """Guia, ficha de custos e roteiro de cada destino, com a profundidade."""
    for p in sorted(glob.glob(os.path.join(RAIZ, "destinos", "*", "index.html"))):
        yield p, 2
    for p in sorted(glob.glob(os.path.join(RAIZ, "destinos", "*", "quanto-custa", "index.html"))):
        yield p, 3
    for p in sorted(glob.glob(os.path.join(RAIZ, "destinos", "*", "roteiro-*", "index.html"))):
        yield p, 3


def linha(prof):
    pre = "../" * prof
    return ('<p class="assinatura">Apurado por <a href="%ssobre/#quem-faz">%s</a>'
            ' · <a href="%s" target="_blank" rel="noopener">%s'
            '<span class="so-leitor"> (abre em outra aba)</span></a></p>'
            % (pre, NOME, INSTAGRAM, ARROBA))


JA = re.compile(r'\n?<p class="assinatura">.*?</p>', re.S)


def main(aplica):
    posta = trocada = pulada = 0
    for p, prof in paginas():
        h = le(p)
        rel = os.path.relpath(p, RAIZ).replace(os.sep, "/")
        nova = linha(prof)
        if JA.search(h):
            h2 = JA.sub("\n" + nova, h, count=1)
            if h2 != h:
                trocada += 1
                if aplica:
                    escreve(p, h2)
            continue
        i = h.find("</h1>")
        if i < 0:
            print("   SEM <h1>: %s" % rel); pulada += 1; continue
        j = h.find("</p>", i)
        if j < 0 or j - i > 2000:
            print("   SEM abertura depois do <h1>: %s" % rel); pulada += 1; continue
        j += len("</p>")
        h = h[:j] + "\n" + nova + h[j:]
        posta += 1
        if aplica:
            escreve(p, h)
    print("   %d posta(s), %d trocada(s), %d pulada(s)   %s"
          % (posta, trocada, pulada, "escrito" if aplica else "SO MOSTRANDO"))
    if not aplica:
        print("   Rode com --aplica para escrever.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
