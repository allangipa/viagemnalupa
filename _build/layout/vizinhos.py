# -*- coding: utf-8 -*-
"""Liga cada ficha e cada roteiro aos seus equivalentes nos outros destinos.

Por que
-------
Contando os links internos que cada pagina RECEBE - fora da barra e do
rodape, que sao iguais em toda pagina e nao distinguem uma da outra aos
olhos do rastreador - apareceu isto:

    media nas 5 paginas que o Google ja indexou ... 12,2
    media nas outras 31 .......................... 6,3

E o detalhe que explica a diferenca: as fichas de custo recebem de 11 a
14 links, porque a barra "Calcular para" liga as dez entre si. As fichas
de destino recebem 4 ou 5. Os roteiros, 4. Nenhuma dessas esta indexada.

As paginas maiores e mais trabalhosas do site sao as que menos recebem
link. Nao e prova de causa - mas link interno e como o rastreador
distribui atencao, e a unica familia de paginas com navegacao cruzada e
justamente a que tem paginas indexadas.

Nao e truque: e a mesma navegacao que ja existe nas fichas de custo.
Quem le o guia de Lisboa e quer comparar com o de Montevideu hoje precisa
voltar a /destinos/ e entrar de novo.

O que faz
---------
1. Completa o bloco de paginas irmas onde ele esta incompleto. Quatro
   paginas estavam assim: os roteiros de Cancun e Fortaleza nao levavam
   a ficha de custos, a de custos de Montevideu nao levava ao guia, e a
   de Orlando nao levava ao roteiro.
2. Poe a barra dos outros destinos no pe de cada ficha e de cada roteiro.

Tudo descoberto em disco. Sem lista escrita a mao - ja foram tres neste
repositorio (schema, sitemap, voos) e as tres falharam em silencio quando
chegou destino novo.

Uso
---
    python _build/layout/vizinhos.py
    python _build/layout/vizinhos.py --aplica
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

MARCA = "<!-- vizinhos -->"
FIM_DO_MAIN = re.compile(r"\n</div>\n</main>")


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def nome_de(slug):
    """O nome de exibicao sai do <h1> da propria ficha.

    "Buenos Aires: 12 pontos turisticos" -> Buenos Aires
    "Nova York em novembro"              -> Nova York
    """
    p = os.path.join(RAIZ, "destinos", slug, "index.html")
    m = re.search(r"(?s)<h1[^>]*>(.*?)</h1>", le(p))
    if not m:
        raise SystemExit("ficha sem <h1>: %s" % slug)
    t = re.sub(r"<[^>]+>", "", m.group(1))
    t = t.split(":")[0]
    t = re.split(r"\s+em\s+", t)[0].strip()
    if not t or len(t) > 30:
        raise SystemExit("nao consegui o nome de %s a partir do <h1>: %r"
                         % (slug, t))
    return t


def destinos():
    """slug -> {nome, roteiro, custos}, tudo lido do disco."""
    saida = {}
    base = os.path.join(RAIZ, "destinos")
    for slug in sorted(os.listdir(base)):
        d = os.path.join(base, slug)
        if not os.path.isfile(os.path.join(d, "index.html")):
            continue
        rot = None
        for sub in sorted(os.listdir(d)):
            if re.fullmatch(r"roteiro-\d+-dias", sub) and \
                    os.path.isfile(os.path.join(d, sub, "index.html")):
                rot = sub
        saida[slug] = {
            "nome": nome_de(slug),
            "roteiro": rot,
            "custos": os.path.isfile(
                os.path.join(d, "quanto-custa", "index.html")),
        }
    return saida


D = destinos()
ORDEM = sorted(D, key=lambda s: D[s]["nome"])


# ------------------------------------------- 1. o bloco das paginas irmas
def irmas(aplica):
    """Cada pagina de um destino leva as outras duas do mesmo destino."""
    print("=== bloco das paginas irmas ===")
    n = 0
    for slug in ORDEM:
        d = D[slug]
        pontos = re.search(r"(\d+)\s+pontos", le(
            os.path.join(RAIZ, "destinos", slug, "index.html")))
        rot_guia = ("Guia dos %s pontos" % pontos.group(1)) if pontos \
            else "Guia dos pontos"
        dias = re.search(r"(\d+)", d["roteiro"]).group(1) if d["roteiro"] else None

        alvos = []                      # (arquivo, subida, o que deve haver)
        if d["custos"]:
            alvos.append((os.path.join("quanto-custa", "index.html"), "../"))
        if d["roteiro"]:
            alvos.append((os.path.join(d["roteiro"], "index.html"), "../"))

        for rel, sobe in alvos:
            p = os.path.join(RAIZ, "destinos", slug, rel)
            h = le(p)
            eu = rel.split(os.sep)[0]
            querido = [(sobe, rot_guia)]
            if d["custos"] and eu != "quanto-custa":
                querido.append((sobe + "quanto-custa/", "Ficha de custos completa"))
            if d["roteiro"] and eu != d["roteiro"]:
                querido.append((sobe + d["roteiro"] + "/",
                                "Roteiro de %s dias" % dias))

            m = re.search(r'(?s)<div class="paginas">(.*?)</div>', h)
            if not m:
                print("   %-16s %-16s sem bloco de paginas" % (slug, eu))
                continue
            falta = [(href, rot) for href, rot in querido
                     if 'href="%s"' % href not in m.group(1)]
            if not falta:
                continue
            add = "".join(' <a class="pg" href="%s">%s</a>' % (href, rot)
                          for href, rot in falta)
            h = h[:m.end(1)] + add + h[m.end(1):]
            print("   %-16s %-16s +%d  (%s)"
                  % (slug, eu, len(falta), ", ".join(r for _, r in falta)))
            n += 1
            if aplica:
                escreve(p, h)
    if not n:
        print("   nenhum incompleto")
    return n


# ------------------------------------------ 2. a barra dos outros destinos
def barra(atual, tipo, sobe):
    rotulo = "Ver o guia de" if tipo == "guia" else "Ver o roteiro de"
    titulo = ("Os guias das outras cidades" if tipo == "guia"
              else "Os roteiros das outras cidades")
    itens = []
    for slug in ORDEM:
        nome = D[slug]["nome"]
        if slug == atual:
            itens.append('<span class="cc atual" aria-current="page">%s</span>'
                         % nome)
            continue
        if tipo == "guia":
            alvo = "%s%s/" % (sobe, slug)
        else:
            if not D[slug]["roteiro"]:
                continue
            alvo = "%s%s/%s/" % (sobe, slug, D[slug]["roteiro"])
        itens.append('<a class="cc" href="%s">%s</a>' % (alvo, nome))
    return ('%s\n<section class="bloco">\n'
            '<div class="bloco-head"><span class="eyebrow">Outros destinos'
            '</span><h2>%s</h2></div>\n'
            '<nav class="calc-cidades" aria-label="Outros destinos">'
            '<span class="cc-rot">%s</span>%s</nav>\n'
            '</section>\n%s' % (MARCA, titulo, rotulo, "".join(itens), MARCA))


def barras(aplica):
    print()
    print("=== barra dos outros destinos ===")
    n = 0
    for slug in ORDEM:
        alvos = [("index.html", "guia", "../")]
        if D[slug]["roteiro"]:
            alvos.append((os.path.join(D[slug]["roteiro"], "index.html"),
                          "roteiro", "../../"))
        for rel, tipo, sobe in alvos:
            p = os.path.join(RAIZ, "destinos", slug, rel)
            h = le(p)
            if MARCA in h:
                continue
            m = FIM_DO_MAIN.search(h)
            if not m:
                print("   %-16s %-10s nao achei o fim do main" % (slug, tipo))
                continue
            b = barra(slug, tipo, sobe)
            h = h[:m.start()] + "\n" + b + h[m.start():]
            quantos = len(re.findall(r'<a class="cc"', b))
            print("   %-16s %-10s +%d links" % (slug, tipo, quantos))
            n += 1
            if aplica:
                escreve(p, h)
    if not n:
        print("   todas ja tem")
    return n


def main(aplica):
    print("%d destinos em disco: %s"
          % (len(D), ", ".join(D[s]["nome"] for s in ORDEM)))
    print()
    a = irmas(aplica)
    b = barras(aplica)
    print()
    print("%s: %d bloco(s) de irmas, %d barra(s)."
          % ("Escrito" if aplica else "Faria", a, b))
    if not aplica:
        print("Nada foi alterado. Rode com --aplica para escrever.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
