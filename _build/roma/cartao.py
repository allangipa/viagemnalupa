# -*- coding: utf-8 -*-
"""Poe Roma nos dois indices, e acerta os contadores.

Mesmo molde do madri/cartao.py.

A CAPA
------
"St Peter's Square, Vatican City - April 2007", de Diliff, CC BY-SA 3.0,
4200x2359 - ja nasceu em 16:9, sem recorte.

Licenca conferida no LicenseShortName da API do Commons, no proprio
arquivo, e nao na etiqueta da pagina.

Escolhida em folha de contato com seis candidatas. As descartadas dizem
mais que a escolhida:

  - a gravura do Piranesi do Coliseu e DOMINIO PUBLICO e e linda, mas e
    agua-forte do seculo XVIII. Destoaria de dezessete fotos.
  - o Coliseu fotografado de perto mostrava a arcada superior sem o
    oval. Em miniatura le como "uns arcos romanos", nao como o Coliseu.
  - as duas da Fontana di Trevi vinham cortadas, com cabeca e braco de
    gente na borda.

A ESCOLHIDA TEM UM ENCAIXE EDITORIAL QUE AS OUTRAS NAO TINHAM
-------------------------------------------------------------
E a vista do alto da cupula - ou seja, e exatamente o que os 320 degraus
do ponto "Basilica de Sao Pedro e a cupula" compram. A capa ilustra o
que a ficha cobra, e nao so o lugar.

E resolve a atribuicao: CC BY-SA 3.0 EXIGE credito, e o credito da capa
neste site so acontece porque a mesma imagem e a foto de um ponto no
guia. Ela e.

A foto e de abril de 2007. A praca nao mudou - colunata, obelisco e
tracado sao os mesmos -, mas fica registrado que a imagem nao e recente.

SOBRE A GRADE
-------------
18 cartoes fecham 9 linhas cheias na grade de duas colunas. Roma desfaz
o orfao que Madri deixou, como o cartao dela previa.
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

_spec = importlib.util.spec_from_file_location(
    "dados_roma_cartao", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d)
DESTINOS = _d.DESTINOS

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ANTES_DESTINOS = 17
ANTES_PONTOS = 190

CAPAS = {
    "roma": dict(
        arq="sao-pedro.webp",
        alt=("A Praça de São Pedro vista do alto da cúpula da basílica, com a colunata "
             "de Bernini em elipse, o obelisco ao centro e a Via della Conciliazione "
             "indo até o horizonte de Roma"),
        cred="Diliff · CC BY-SA 3.0 · via Wikimedia Commons"),
}

RESUMO = {
    "roma": dict(
        numeros=[("Os cinco pontos pagos", "€ 78", False),
                 ("Num primeiro domingo", "€ 37", True)],
        # O achado e a distincao entre os dois domingos, porque quase
        # todo guia trata "domingo gratuito de Roma" como uma coisa so.
        achado=("<b>Roma tem dois domingos gratuitos por mês, e eles não são o mesmo "
                "domingo.</b> O primeiro libera Coliseu, Panteão e Borghese e corta "
                "€ 41; o último libera os Museus Vaticanos e corta € 25 — e é o único "
                "domingo em que eles abrem. Uma viagem de cinco dias pega no máximo "
                "um.")),
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
