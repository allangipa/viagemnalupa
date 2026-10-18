# -*- coding: utf-8 -*-
"""Poe Barcelona nos dois indices, e acerta os contadores.

Mesmo molde do granada/cartao.py.

A CAPA
------
A Sagrada Familia e o assunto de Barcelona na primeira fracao de segundo,
e e tambem a linha mais cara e mais rigida da ficha (nominativa, sem
devolucao). A capa e ela. A foto e a mesma do ponto, lida do dados.py.

SOBRE A GRADE
-------------
Granada fechou a grade em vinte, dez linhas cheias. Barcelona e o
vigesimo primeiro e abre um orfao na ultima linha, como Paris fez com o
decimo nono. O proximo destino fecha de novo.

OS DOIS NUMEROS DO CARTAO
--------------------------
Os onze pontos pagos somam 219,00 EUR, usando o piso onde o preco e
"a partir de":

    Sagrada Familia     26,00
    Park Guell          18,00
    Casa Batllo         29,00  (desde)
    La Pedrera          29,00  (desde)
    Museu Picasso       12,00
    MNAC                12,00
    Castell Montjuic    12,00
    Sant Pau            17,00  (depois das 14h)
    Catedral            16,00
    Palau               20,00
    Museu do Barca      28,00  (desde)
                       ------
                       219,00

E 183,00 EUR nas tres tardes certas - Picasso na quinta, MNAC no sabado,
Montjuic no domingo tiram 36. O segundo numero e o destacado.
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

_spec = importlib.util.spec_from_file_location(
    "dados_barcelona_cartao", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d)
DESTINOS = _d.DESTINOS

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ANTES_DESTINOS = 20
ANTES_PONTOS = 220

CAPAS = {
    "barcelona": dict(
        arq="sagrada-familia.webp",
        alt=("A fachada da Sagrada Família vista de baixo, com as torres e os "
             "guindastes da obra, em dezembro de 2025"),
        cred="Enric · CC BY-SA 4.0 · via Wikimedia Commons · recortada"),
}

RESUMO = {
    "barcelona": dict(
        numeros=[("Os onze pontos pagos", "€ 219,00", False),
                 ("Nas três tardes grátis", "€ 183,00", True)],
        achado=("<b>A taxa turística de Barcelona dobrou em 1º de abril de 2026 e já "
                "tem aumento marcado para 2027 e 2028:</b> quatro noites num três "
                "estrelas são € 28 por pessoa, fora do quarto. <b>E a semana tem três "
                "tardes grátis em três dias</b> — Picasso na quinta, MNAC no sábado, "
                "Montjuïc no domingo —, que uma viagem de quinta a segunda pega todas.")),
}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def pontos_de(slug):
    h = le(os.path.join(RAIZ, "destinos", slug, "index.html"))
    return len(re.findall(r'<article class="ponto"', h))


def cartao(d, sobe):
    slug = d["slug"]
    capa = CAPAS[slug]
    r = RESUMO[slug]
    n = pontos_de(slug)
    dentro = "./" if sobe == "../" else "./destinos/"
    nums = "".join(
        '<div class="num-b"><span class="r">%s</span>'
        '<span class="v%s">%s</span></div>' % (rot, " c" if c else "", val)
        for rot, val, c in r["numeros"])
    return (
        '<article class="dest" data-regiao="%s" data-status="publicado"\n'
        ' data-busca="%s">'
        '<figure class="dest-capa">'
        '<img src="%sassets/img/%s/%s" alt="%s" width="1200" height="675" '
        'loading="lazy" decoding="async">'
        '<figcaption><div><h3><a href="%s%s/">%s</a></h3>'
        '<span class="pais">%s · %d pontos turísticos</span></div>'
        '<span class="tag-pub">Publicado</span></figcaption></figure>'
        '<div class="numeros">%s</div>'
        '<p class="achado">%s</p>'
        '<div class="paginas"> <a class="pg" href="%s%s/">Guia dos pontos</a> </div>'
        '<a class="dest-link" href="%s%s/" tabindex="-1" aria-hidden="true"></a>'
        '</article>'
        % (d["regiao"], d["busca"], sobe, slug, capa["arq"], capa["alt"],
           dentro, slug, d["nome"], d["pais"], n, nums, r["achado"],
           dentro, slug, dentro, slug))


def main(aplica):
    todos = sorted(s for s in os.listdir(os.path.join(RAIZ, "destinos"))
                   if os.path.isfile(os.path.join(RAIZ, "destinos", s, "index.html")))
    soma = sum(pontos_de(s) for s in todos)
    print("destinos em disco: %d      pontos somados: %d" % (len(todos), soma))

    for slug, capa in CAPAS.items():
        cam = os.path.join(RAIZ, "assets", "img", slug, capa["arq"])
        if not os.path.isfile(cam):
            raise SystemExit("PARADO: capa nao existe em disco: %s" % cam)
        if capa["cred"] == "PENDENTE":
            raise SystemExit("PARADO: a capa ainda nao tem credito; preencha CAPAS")
    print("capas conferidas em disco: %d" % len(CAPAS))

    colunas = 2
    resto = len(todos) % colunas
    print("grade de %d colunas: %d cartoes -> %d linhas%s" %
          (colunas, len(todos), len(todos) // colunas,
           " cheias" if not resto else " + %d sozinho(s)" % resto))
    print()

    for idx, sobe in (("index.html", "./"),
                      (os.path.join("destinos", "index.html"), "../")):
        p = os.path.join(RAIZ, idx)
        h = le(p)
        antes = h
        dentro = "./" if sobe == "../" else "./destinos/"
        for d in DESTINOS:
            if 'href="%s%s/"' % (dentro, d["slug"]) in h:
                print("  %-22s %-12s ja esta" % (idx, d["slug"]))
                continue
            m = None
            for mm in re.finditer(r"</article>", h):
                m = mm
            if not m:
                print("  %-22s sem grade de cartoes" % idx)
                continue
            h = h[:m.end()] + "\n" + cartao(d, sobe) + h[m.end():]
            print("  %-22s %-12s + cartao (%d pontos)"
                  % (idx, d["slug"], pontos_de(d["slug"])))

        h, n1 = re.subn(r"\b%d(?=\s+destinos\b)" % ANTES_DESTINOS, str(len(todos)), h)
        h, n2 = re.subn(r"(>)\s*%d\s*(<)" % ANTES_PONTOS, r"\g<1>%d\g<2>" % soma, h)
        print("  %-22s contadores: %d de destinos, %d de pontos" % (idx, n1, n2))
        if not n1 and str(ANTES_DESTINOS) in antes:
            print("  %-22s  !! nao troquei o total de destinos - confira" % idx)
        if aplica and h != antes:
            escreve(p, h)

    print()
    print("%s." % ("Escrito" if aplica else "Faria isso"))
    if not aplica:
        print("Nada foi alterado. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
