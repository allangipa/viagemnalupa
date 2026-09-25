# -*- coding: utf-8 -*-
"""Poe Sevilha nos dois indices, e acerta os contadores.

Mesmo molde do porto/cartao.py, que fez isso pelo Porto, e do
novos2/cartoes.py antes dele.

O MOTIVO DESTE DESTINO EXISTIR E DE GRADE, E ESTA DITO

Com treze destinos a grade fechava em seis linhas cheias mais UM cartao
sozinho, porque ela e de duas colunas: o container tem 1120 px, o cartao
minimo 25rem e o vao 18 px. Com catorze, fecham sete linhas.

    13 cartoes -> 6 linhas + 1 sozinho
    14 cartoes -> 7 linhas cheias

Nao e capricho: cartao orfao ao lado de um vazio e a primeira coisa que
se ve ao rolar ate o fim da home.

A CAPA
------
"Plaza de España, Sevilla", de Wzwz, DOMINIO PUBLICO, 6016x4034.
Licenca conferida no LicenseShortName da API do Commons, no proprio
arquivo - nao na etiqueta da pagina.

Escolhida em folha de contato com seis candidatas, todas ja recortadas em
16:9, com cap de uma por autor. As outras cinco eram do Alcazar, e quatro
delas nao liam como Sevilha em miniatura: palmeiras, um muro com banco,
um portal de colunas. A Plaza de España diz o nome da cidade na hora.

Ha uma coincidencia util: e justamente o ponto do achado da pagina - a
cobranca de entrada anunciada em 2024 e nunca aprovada.

Uso
---
    python _build/sevilha/cartao.py
    python _build/sevilha/cartao.py --aplica
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

_spec = importlib.util.spec_from_file_location(
    "sevilha_dados", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d)
DESTINOS = _d.DESTINOS

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Os numeros que estao nos indices ANTES desta rodada. Explicitos para a
# substituicao ser verificavel: se nao encontrar, o script avisa em vez de
# seguir calado.
ANTES_DESTINOS = 13
ANTES_PONTOS = 149

CAPAS = {
    "sevilha": dict(
        arq="plaza-de-espana.webp",
        alt=("A Plaza de España em Sevilha, com a galeria curva de tijolo e cerâmica, "
             "a ponte sobre o canal e as torres nas pontas"),
        cred="Wzwz · domínio público · via Wikimedia Commons"),
}

RESUMO = {
    "sevilha": dict(
        numeros=[("Alcázar, tudo somado", "€ 21,00", False),
                 ("Plaza de España", "grátis", True)],
        # O achado e o da praca, e nao o do Alcazar, porque e o unico que
        # desmente algo que o leitor provavelmente ja leu em outro lugar.
        achado=("<b>A entrada paga na Plaza de España nunca existiu.</b> Foi anunciada "
                "pelo prefeito em 2024 e não aparece em nenhuma ordenança fiscal de "
                "Sevilha, nem nas de 2026. A praça segue de acesso livre.")),
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

    # a simetria da grade, que e o motivo deste destino existir agora
    colunas = 2
    print("grade de %d colunas: %d cartoes -> %d linhas%s" %
          (colunas, len(todos), len(todos) // colunas,
           " cheias" if len(todos) % colunas == 0
           else " + %d sozinho(s)" % (len(todos) % colunas)))
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
