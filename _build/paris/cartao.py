# -*- coding: utf-8 -*-
"""Poe Paris nos dois indices, e acerta os contadores.

Mesmo molde do roma/cartao.py.

A CAPA: A TORRE EIFFEL, E NAO O LOUVRE
--------------------------------------
O achado da ficha mora no Louvre - e a pirâmide seria a escolha
editorial coerente, como a cupula de Sao Pedro foi em Roma.

Nao foi. A foto do Louvre que temos e de ceu encoberto, e a 525 px na
home ela le como "uma praca cinza". A Torre Eiffel le como Paris na
primeira fracao de segundo, que e o que um cartao precisa fazer.

O achado continua na ficha e no texto do proprio cartao, em palavras.

A CAPA E DIURNA, E ISSO NAO E ESTETICA
--------------------------------------
A torre e dominio publico - Eiffel morreu em 1923. A ILUMINACAO
NOTURNA nao e: e instalacao de Pierre Bideau, de 1985, reconhecida
como criacao original pela Justica francesa. Capa noturna seria uso de
obra protegida.

SOBRE A GRADE
-------------
19 cartoes deixam um orfao na grade de duas colunas - nove linhas
cheias e um sozinho. Roma tinha fechado a grade em 18; Paris a desfaz
de novo, e o proximo destino a refecha.
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

_spec = importlib.util.spec_from_file_location(
    "dados_paris_cartao", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d)
DESTINOS = _d.DESTINOS

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ANTES_DESTINOS = 18
ANTES_PONTOS = 199

CAPAS = {
    "paris": dict(
        arq="torre-eiffel.webp",
        alt=("A Torre Eiffel inteira vista do Champ de Mars, em dia de céu azul, com "
             "a cidade baixa ao redor"),
        cred="Nik Las · CC BY 3.0 · via Wikimedia Commons"),
}

RESUMO = {
    "paris": dict(
        numeros=[("Os seis pontos pagos", "€ 159,50", False),
                 ("Se o passaporte fosse europeu", "€ 146,50", True)],
        # O achado e que a diferenca existe, nao que ela seja enorme: sao
        # 13 euros num adulto, mas a REGRA muda de lugar para lugar, e e
        # isso que nenhum guia separa.
        achado=("<b>Paris passou a cobrar mais de quem não é europeu — e cada lugar "
                "faz isso de um jeito diferente.</b> O Louvre cobra € 32 em vez de "
                "€ 22 desde janeiro de 2026; Versalhes separa por € 3; a Torre Eiffel "
                "não separa nada. E a gratuidade de 18 a 25 anos dos monumentos "
                "nacionais vale só para quem mora na União Europeia.")),
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
