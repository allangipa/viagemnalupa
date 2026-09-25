# -*- coding: utf-8 -*-
"""Acerta todo numero que CONTA alguma coisa, derivando do disco.

Por que existe
--------------
Este site tem tres contadores e os tres ja mentiram:

  - o "N pontos turisticos" de cada cartao, nos dois indices;
  - o placar "Pontos apurados" da home;
  - o "N destinos" do texto.

Sempre pelo mesmo motivo: a ficha cresce e o numero fica para tras, sem
erro em lugar nenhum. Nova York passou de 17 para 20 pontos e o ItemList
continuou anunciando 17. Sevilha passou de 5 para 12 e os dois cartoes
continuaram dizendo 5.

Ate agora isso era corrigido a mao, com o numero ANTERIOR escrito dentro
de cada cartao.py - porto/cartao.py guarda ANTES_PONTOS = 149, e
sevilha/cartao.py guarda 149 tambem. Esse desenho funciona uma vez, na
rodada em que o destino entra, e envelhece no dia seguinte.

Aqui nao ha numero guardado. Tudo e contado no disco, agora:

    pontos de um destino = <article class="ponto"> na ficha dele
    total de pontos      = soma de todos
    total de destinos    = pastas em destinos/ com index.html

O QUE ELE NAO FAZ
-----------------
Nao inventa cartao nem cria destino. So corrige numero que ja esta
escrito. Cartao que nao existe continua nao existindo - quem poe cartao
novo e o cartao.py de cada destino.

E so troca quando o numero DIFERE. Se bater, nao toca no arquivo.

Uso
---
    python _build/layout/contadores.py            # so mostra
    python _build/layout/contadores.py --aplica
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

INDICES = ["index.html", os.path.join("destinos", "index.html")]


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def pontos_por_destino():
    base = os.path.join(RAIZ, "destinos")
    fora = {}
    for slug in sorted(os.listdir(base)):
        arq = os.path.join(base, slug, "index.html")
        if os.path.isfile(arq):
            fora[slug] = len(re.findall(r'<article class="ponto"', le(arq)))
    return fora


def main(aplica):
    por_slug = pontos_por_destino()
    soma = sum(por_slug.values())
    print("destinos em disco: %d      pontos somados: %d\n"
          % (len(por_slug), soma))

    mudou = 0
    for rel in INDICES:
        p = os.path.join(RAIZ, rel)
        if not os.path.isfile(p):
            continue
        h = antes = le(p)

        # 1. o "N pontos turisticos" de cada cartao, casado pelo href do
        #    proprio cartao - assim o numero corrigido e sempre o do
        #    destino certo, e nao o do vizinho.
        for slug, n in por_slug.items():
            def troca(m, n=n):
                if int(m.group(2)) == n:
                    return m.group(0)
                troca.achou = (int(m.group(2)), n)
                return "%s%d%s" % (m.group(1), n, m.group(3))
            troca.achou = None
            h, _ = re.subn(
                r'(href="\.?\.?/?(?:\./)?(?:destinos/)?%s/">[^<]*</a></h3>'
                r'<span class="pais">[^<·]*·\s*)(\d+)(\s*pontos turísticos)'
                % re.escape(slug), troca, h)
            if troca.achou:
                print("  %-22s %-16s %d -> %d"
                      % (rel, slug, troca.achou[0], troca.achou[1]))

        # 2. o placar "Pontos apurados" da home
        def placar(m):
            if int(m.group(2)) == soma:
                return m.group(0)
            placar.achou = (int(m.group(2)), soma)
            return "%s%d%s" % (m.group(1), soma, m.group(3))
        placar.achou = None
        h, _ = re.subn(r'(<span class="r">Pontos apurados</span>'
                       r'<span class="v">)(\d+)(</span>)', placar, h)
        if placar.achou:
            print("  %-22s %-16s %d -> %d"
                  % (rel, "placar", placar.achou[0], placar.achou[1]))

        # 3. o "N destinos" do texto corrido
        def dest(m):
            if int(m.group(1)) == len(por_slug):
                return m.group(0)
            dest.achou = (int(m.group(1)), len(por_slug))
            return "%d%s" % (len(por_slug), m.group(2))
        dest.achou = None
        h, _ = re.subn(r"\b(\d+)( destinos\b)", dest, h)
        if dest.achou:
            print("  %-22s %-16s %d -> %d"
                  % (rel, "n de destinos", dest.achou[0], dest.achou[1]))

        if h != antes:
            mudou += 1
            if aplica:
                escreve(p, h)

    print()
    print("%d indice(s) %s" % (mudou, "escrito(s)" if aplica else "a escrever"))
    if not mudou:
        print("Nada defasado.")
    elif not aplica:
        print("Nada foi alterado. Rode com --aplica.")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplica" in sys.argv))
