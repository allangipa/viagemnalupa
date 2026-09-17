# -*- coding: utf-8 -*-
"""Tira a moldura de foto vazia, o botao de buscar e a nota de licenca.

O pedido
--------
"OS que nao tiver foto deixar so o nome. Retirar esse quadrado."

E antes, sobre o bloco de Nova York que explicava onde buscar imagem e o
que a lei americana permite fotografar: "Essa informacao na pagina de
nova york e irrelevante para o visitante. Pode retirar."

O Allan ja tinha dito a mesma coisa quando montei Cancun e Fortaleza:
"Melhor ficar sem imagem do que quadro sem imagem." As fichas novas
nasceram assim; as antigas ficaram para tras.

O que sai
---------
1. <div class="foto"> que so contem a moldura vazia - o quadro tracejado
   com icone de imagem, o rotulo "FOTO DE <ponto>" e o botao "Buscar no
   acervo livre". Sai inteiro. O ponto fica so com o nome, como pedido.

2. <p class="foto-nota"> - o paragrafo que explica liberdade de panorama
   e regime de licenca. Sai de todos os pontos, inclusive os que JA tem
   foto: quem le quer saber quanto custa entrar, nao sob que lei a
   fotografia pode ser publicada. Em Nova York havia 17 desses para 17
   pontos.

3. A secao "Onde buscar foto de cada ponto" da ficha de Nova York.

O que NAO sai
-------------
<figcaption class="foto-cred"> - o credito das fotos que existem. CC BY-SA
obriga nomear autor e licenca; tirar isso seria descumprir a licenca.
Conferido depois: 92 fotos, 92 creditos.

Uso
---
    python _build/layout/sem_moldura.py
    python _build/layout/sem_moldura.py --aplica
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def fim_do_elemento(h, ini, tag):
    """Onde termina o elemento aberto em `ini`, contando aninhamento.

    Regex com .*? erra aqui: a moldura tem <div> dentro de <div>, e o
    primeiro </div> nao e o do elemento certo. Ja duplicou </article>
    neste repositorio por causa disso.
    """
    abre = re.compile(r"<%s[\s>]" % tag)
    fecha = re.compile(r"</%s>" % tag)
    pos, nivel = ini, 0
    while pos < len(h):
        a = abre.search(h, pos)
        f = fecha.search(h, pos)
        if not f:
            return -1
        if a and a.start() < f.start():
            nivel += 1
            pos = a.end()
            continue
        nivel -= 1
        pos = f.end()
        if nivel == 0:
            return pos
    return -1


def tira_molduras(h):
    """Remove <div class="foto"> que nao tem <img> dentro."""
    n = 0
    while True:
        m = re.search(r'<div class="foto">', h)
        achou = False
        for m in re.finditer(r'<div class="foto">', h):
            fim = fim_do_elemento(h, m.start(), "div")
            if fim < 0:
                continue
            bloco = h[m.start():fim]
            if "<img" in bloco:
                continue            # tem foto de verdade: fica
            # come o espaco em branco que sobra
            j = fim
            while j < len(h) and h[j] in " \t\r\n":
                j += 1
            h = h[:m.start()] + h[j:]
            n += 1
            achou = True
            break
        if not achou:
            return h, n


def tira_notas(h):
    h, n = re.subn(r'(?s)<p class="foto-nota">.*?</p>\s*', "", h)
    return h, n


def tira_secao_imagens(h):
    for m in re.finditer(r'<section class="bloco">', h):
        fim = fim_do_elemento(h, m.start(), "section")
        if fim < 0:
            continue
        bloco = h[m.start():fim]
        if "Onde buscar foto" not in bloco:
            continue
        j = fim
        while j < len(h) and h[j] in " \t\r\n":
            j += 1
        return h[:m.start()] + h[j:], 1
    return h, 0


def main(aplica):
    print("%-16s %8s %8s %10s" % ("destino", "molduras", "notas", "secao"))
    tot = [0, 0, 0]
    base = os.path.join(RAIZ, "destinos")
    for slug in sorted(os.listdir(base)):
        p = os.path.join(base, slug, "index.html")
        if not os.path.isfile(p):
            continue
        h = le(p)
        antes = h
        h, a = tira_molduras(h)
        h, b = tira_notas(h)
        h, c = tira_secao_imagens(h)
        if not (a or b or c):
            continue
        print("%-16s %8d %8d %10s" % (slug, a, b, "sim" if c else "-"))
        tot[0] += a
        tot[1] += b
        tot[2] += c
        if aplica and h != antes:
            escreve(p, h)
    print("%-16s %8d %8d %10d" % ("TOTAL", tot[0], tot[1], tot[2]))
    print()
    print("%s." % ("Escrito" if aplica else "Faria isso"))
    if not aplica:
        print("Nada foi alterado. Rode com --aplica para escrever.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
