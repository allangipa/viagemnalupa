# -*- coding: utf-8 -*-
"""Poe "quanto custa" e "roteiro" onde o leitor os encontre.

O problema, medido
------------------
O Allan, que constroi o site, disse nao achar o botao de quanto custa.
Fui medir e ele tinha razao duas vezes:

1. Na ficha de Lisboa, no celular, o link esta na TELA 69,9 de 70,4 -
   a ultima coisa da pagina, e o unico lugar da ficha inteira onde ele
   aparece. Achar "quanto custa" custava rolar a pagina toda.

2. Quatro dos oito cartoes dos indices - Orlando, Montevideu, Lisboa e
   Rio - so ofereciam "Guia dos pontos", embora as tres paginas existam
   nos oito destinos. E sao os quatro primeiros da grade, os que aparecem
   antes de rolar. Mesmo padrao dos contadores defasados: a pagina foi
   criada e a navegacao nao acompanhou.

O conserto
----------
Os links das paginas irmas entram no topo da ficha, dentro do bloco do
indice. Isso resolve os dois lados de uma vez: no celular o indice esta
na tela 1,2, e no desktop ele viaja na coluna lateral fixa - entao os
dois links ficam a alcance o tempo todo, em vez de no fim de 70 telas.

O bloco do rodape continua onde estava. Quem chega ao fim da pagina
tambem merece o caminho.

Uso
---
    python _build/layout/atalhos.py
    python _build/layout/atalhos.py --aplica
"""
import io
import json
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


def dias_da_ficha(slug):
    """Quantos dias a ficha de custos usa. Vem da propria configuracao da
    calculadora, nao do titulo - titulo se reescreve, configuracao nao."""
    p = os.path.join(RAIZ, "destinos", slug, "quanto-custa", "index.html")
    if not os.path.isfile(p):
        return None
    m = re.search(r'class="calc-cfg"[^>]*>(.*?)</script>', le(p), re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1)).get("dias")
    except Exception:
        return None


def irmas_de(slug):
    """Descobre as paginas irmas pelas pastas que existem em disco."""
    base = os.path.join(RAIZ, "destinos", slug)
    saida = []
    if os.path.isfile(os.path.join(base, "quanto-custa", "index.html")):
        d = dias_da_ficha(slug)
        saida.append(("quanto-custa/", "Quanto custa",
                      "%d dias, por pessoa" % d if d else "por pessoa"))
    for sub in sorted(os.listdir(base)):
        m = re.fullmatch(r"roteiro-(\d+)-dias", sub)
        if m and os.path.isfile(os.path.join(base, sub, "index.html")):
            saida.append((sub + "/", "Roteiro",
                          "%s dias, dia a dia" % m.group(1)))
    return saida


# --------------------------------------------------- 1. topo de cada ficha
def topo_da_ficha(aplica):
    print("=== links no topo da ficha ===")
    n = 0
    base = os.path.join(RAIZ, "destinos")
    for slug in sorted(os.listdir(base)):
        p = os.path.join(base, slug, "index.html")
        if not os.path.isfile(p):
            continue
        h = le(p)
        if 'class="idx-irmas"' in h:
            print("   %-16s ja tem" % slug)
            continue
        irmas = irmas_de(slug)
        if not irmas:
            print("   %-16s sem paginas irmas" % slug)
            continue
        # entra logo depois do cabecalho do indice
        m = re.search(r'(<div class="bloco-head"><span class="eyebrow">[^<]*'
                      r'</span><h2>Índice</h2></div>)', h)
        if not m:
            print("   %-16s sem indice - nao ha onde por" % slug)
            continue
        bloco = ('<div class="idx-irmas">%s</div>' % "".join(
            '<a href="%s"><b>%s</b><span>%s</span></a>' % (href, tit, sub)
            for href, tit, sub in irmas))
        h = h[:m.end()] + "\n  " + bloco + h[m.end():]
        print("   %-16s +%d  (%s)"
              % (slug, len(irmas), ", ".join(t for _, t, _ in irmas)))
        n += 1
        if aplica:
            escreve(p, h)
    return n


# ------------------------------------------------- 2. cartoes dos indices
def cartoes(aplica):
    """Completa os cartoes que so oferecem "Guia dos pontos".

    Uma substituicao so, com funcao: assim nao ha indice de posicao para
    envelhecer enquanto o texto cresce a cada insercao.
    """
    print()
    print("=== cartoes dos indices ===")
    total = 0
    for idx in ("index.html", os.path.join("destinos", "index.html")):
        p = os.path.join(RAIZ, idx)
        if not os.path.isfile(p):
            continue
        conta = [0]

        def um(m):
            bloco = m.group(0)
            guia = re.search(
                r'<a class="pg" href="([^"]*)">Guia dos pontos</a>', bloco)
            if not guia:
                return bloco
            caminho = guia.group(1)          # ./lisboa/ ou ../destinos/lisboa/
            slug = caminho.rstrip("/").split("/")[-1]
            if not os.path.isdir(os.path.join(RAIZ, "destinos", slug)):
                return bloco
            faltando = []
            for href, tit, _sub in irmas_de(slug):
                destino = caminho + href
                if 'href="%s"' % destino in bloco:
                    continue
                if tit == "Quanto custa":
                    rot = "Quanto custa"
                else:
                    rot = "Roteiro %s dias" % re.search(
                        r"roteiro-(\d+)-dias", href).group(1)
                faltando.append('<a class="pg" href="%s">%s</a>'
                                % (destino, rot))
            if not faltando:
                return bloco
            conta[0] += 1
            print("   %-22s %-16s +%d  (%s)"
                  % (idx, slug, len(faltando),
                     ", ".join(re.search(r">([^<]*)</a>", f).group(1)
                               for f in faltando)))
            return bloco.replace("</div>", "".join(faltando) + "</div>", 1)

        h = le(p)
        novo = re.sub(r'<div class="paginas">.*?</div>', um, h, flags=re.S)
        total += conta[0]
        if aplica and novo != h:
            escreve(p, novo)
    if not total:
        print("   nenhum incompleto")
    return total


def main(aplica):
    a = topo_da_ficha(aplica)
    b = cartoes(aplica)
    print()
    print("%s: %d ficha(s), %d cartao(oes)."
          % ("Escrito" if aplica else "Faria", a, b))
    if not aplica:
        print("Nada foi alterado. Rode com --aplica para escrever.")
        print("Depois: python _build/cachebust/atualiza.py --aplica")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
