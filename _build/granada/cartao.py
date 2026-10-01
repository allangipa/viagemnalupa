# -*- coding: utf-8 -*-
"""Poe Granada nos dois indices, e acerta os contadores.

Mesmo molde do paris/cartao.py.

A CAPA: O PATIO DOS LEOES, E DESSA VEZ SEM CONFLITO
----------------------------------------------------
Em Paris houve escolha a fazer: o achado morava no Louvre, mas a foto
do Louvre lia como "uma praca cinza" a 525 px, e a capa foi a Torre
Eiffel.

Aqui nao ha esse conflito. O achado mora na Alhambra E a melhor foto do
conjunto e a Alhambra - o Patio dos Leoes visto por entre a arcada, com
as colunas finas e a fonte ao centro. Ela le como Granada na primeira
fracao de segundo e e o assunto da linha mais importante da ficha.

A capa e DIURNA por coincidencia, nao por regra. Diferente da Torre
Eiffel, a iluminacao noturna da Alhambra nao e obra protegida de que se
tenha noticia: a noturna do guia esta publicada normalmente, com licenca
livre lida do arquivo. Aqui a diurna venceu so por ser melhor foto.

SOBRE A GRADE
-------------
Paris desfez a grade em 19 cartoes - nove linhas cheias e um orfao.
Granada e o vigesimo e REFECHA a grade: dez linhas cheias de duas
colunas, sem sobra. Era o que o proprio cartao de Paris previa.

OS DOIS NUMEROS DO CARTAO
--------------------------
Os seis pontos pagos somam 60,00 EUR exatos:

    Alhambra diurna     22,27
    Alhambra noturna    12,73
    Catedral            10,00
    Capilla Real         7,00
    Sacromonte           6,00
    Monumento andalusi   2,00
                        ------
                         60,00

E 43,00 EUR na quarta-feira certa, porque Catedral e Capilla Real saem
de graca por reserva - 17 EUR a menos. O segundo numero e o destacado,
como em Paris.
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

_spec = importlib.util.spec_from_file_location(
    "dados_granada_cartao", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d)
DESTINOS = _d.DESTINOS

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ANTES_DESTINOS = 19
ANTES_PONTOS = 210

CAPAS = {
    "granada": dict(
        arq="alhambra-diurna.webp",
        alt=("O Pátio dos Leões da Alhambra visto por entre a arcada, com as colunas "
             "finas e a fonte ao centro"),
        cred="Tuxyso · CC BY-SA 3.0 · via Wikimedia Commons"),
}

RESUMO = {
    "granada": dict(
        numeros=[("Os seis pontos pagos", "€ 60,00", False),
                 ("Na quarta-feira certa", "€ 43,00", True)],
        achado=("<b>A Alhambra tem dois preços oficiais para o mesmo ingresso:</b> a "
                "lei da Junta de Andalucía diz € 21, o site do próprio monumento diz "
                "€ 22,27 — e ainda avisa que a comissão se soma a isso. <b>E a Catedral "
                "e a Capilla Real são gratuitas em quartas-feiras à tarde</b>, por "
                "reserva num site da diocese que nenhum guia cita.")),
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
