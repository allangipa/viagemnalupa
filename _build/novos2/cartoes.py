# -*- coding: utf-8 -*-
"""Poe Bariloche e Punta Cana nos dois indices, e acerta os contadores.

O verificador pegou o estado intermediario, que era exatamente o que ele
existe para pegar:

    index.html: o placar diz 114 pontos apurados, somam 130
    /index.html: fala em 10 destinos, existem 12
    /destinos/index.html: fala em 10 destinos, existem 12

As fichas estavam em disco e nenhum indice as listava. Este script fecha
isso: monta o cartao no mesmo molde dos outros dez e recalcula os
numeros a partir do que existe, nao de constante escrita a mao.

As capas
--------
Escolhidas olhando, nao pelo filtro de licenca - que ja me deixou passar
quadro no lugar de museu tres vezes neste projeto.

  Bariloche  Llao Llao Peninsula Panorama, CC BY-SA 4.0, User:Fernando.
             E a vista do Punto Panoramico, que esta na propria ficha.
             Descartei uma com fios eletricos cruzando o quadro e outra
             em neblina fechada.
  Punta Cana Punta Cana, Dominican Republic (31), CC BY 2.0, via Flickr.
             Descartei a mais bonita porque tinha gente reconhecivel em
             primeiro plano - direito de imagem em pagina comercial.

Uso
---
    python _build/novos2/cartoes.py
    python _build/novos2/cartoes.py --aplica
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

from dados import DESTINOS                                     # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Os numeros que estavam nos indices antes desta rodada. Ficam explicitos
# para a substituicao ser verificavel: se nao encontrar, o script avisa em
# vez de seguir calado.
ANTES_DESTINOS = 10
ANTES_PONTOS = 114

CAPAS = {
    "bariloche": dict(
        arq="llao-llao.webp",
        alt=("Vista da Península Llao Llao sobre o lago Nahuel Huapi, com o "
             "hotel na ponta e a cordilheira ao fundo, em dia de céu limpo"),
        cred="Fernando · CC BY-SA 4.0 · via Wikimedia Commons"),
    "punta-cana": dict(
        arq="praia.webp",
        alt=("Faixa de coqueiros na areia de uma praia de Punta Cana, com "
             "sargaço trazido pela maré e banhistas ao longe"),
        cred="Flickr · CC BY 2.0 · via Wikimedia Commons"),
}

# Os dois numeros em destaque e o achado de cada cartao. Sao os mesmos
# fatos que a ficha apura - aqui so em forma curta.
RESUMO = {
    "bariloche": dict(
        # ARS, nao "$". O Allan leu "$ 182.600" e perguntou se era mais de
        # mil dolares - sao pesos argentinos, cerca de R$ 621. Buenos
        # Aires ja escrevia ARS e Santiago escreve CLP: e a convencao da
        # casa para moeda que se confunde, e eu nao tinha seguido.
        numeros=[("Isla Victoria, tudo somado", "ARS 182.600", False),
                 ("Circuito Chico inteiro", "grátis", True)],
        achado=("<b>A excursão mais vendida da cidade tem três cobranças, e "
                "o anúncio mostra uma.</b> A taxa do Parque Nacional e a de "
                "embarque se pagam em dinheiro, no porto.")),
    "punta-cana": dict(
        numeros=[("Hoyo Azul, admissão geral", "US$ 129", False),
                 ("As praias, por lei", "grátis", True)],
        achado=("<b>Quase nada em Punta Cana tem tarifa oficial publicada.</b> "
                "O ministério do ambiente não divulga preço de Los Haitises, e "
                "a mesma reserva aparece a US$ 15 e a US$ 50.")),
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
        '</article>'
        % (d["regiao"], d["busca"], sobe, slug, capa["arq"], capa["alt"],
           "./" if sobe == "../" else "./destinos/", slug, d["nome"],
           d["pais"], n, nums, r["achado"],
           "./" if sobe == "../" else "./destinos/", slug))


def main(aplica):
    todos = sorted(s for s in os.listdir(os.path.join(RAIZ, "destinos"))
                   if os.path.isfile(os.path.join(RAIZ, "destinos", s,
                                                  "index.html")))
    soma = sum(pontos_de(s) for s in todos)
    print("destinos em disco: %d      pontos somados: %d" % (len(todos), soma))
    print()

    for idx, sobe in (("index.html", "./"),
                      (os.path.join("destinos", "index.html"), "../")):
        p = os.path.join(RAIZ, idx)
        h = le(p)
        antes = h
        for d in DESTINOS:
            if 'href="%s%s/"' % ("./" if sobe == "../" else "./destinos/",
                                 d["slug"]) in h:
                print("  %-22s %-12s ja esta" % (idx, d["slug"]))
                continue
            # entra depois do ultimo cartao da grade
            m = None
            for mm in re.finditer(r"</article>", h):
                m = mm
            if not m:
                print("  %-22s sem grade de cartoes" % idx)
                continue
            h = h[:m.end()] + "\n" + cartao(d, sobe) + h[m.end():]
            print("  %-22s %-12s + cartao (%d pontos)"
                  % (idx, d["slug"], pontos_de(d["slug"])))

        # Contadores. Os indices escrevem o total como ALGARISMO ("10
        # destinos"), nao por extenso - conferi antes de trocar, porque a
        # primeira versao procurou "dez" e nao casou com nada, em
        # silencio. Substituicao que nao encontra nada e pior que erro:
        # ela passa.
        h, n1 = re.subn(r"\b%d(?=\s+destinos\b)" % ANTES_DESTINOS,
                        str(len(todos)), h)
        h, n2 = re.subn(r"(>)\s*%d\s*(<)" % ANTES_PONTOS,
                        r"\g<1>%d\g<2>" % soma, h)
        print("  %-22s contadores: %d de destinos, %d de pontos"
              % (idx, n1, n2))
        if not n1 and str(ANTES_DESTINOS) in antes:
            print("  %-22s  !! nao troquei o total de destinos - confira"
                  % idx)
        if aplica and h != antes:
            escreve(p, h)

    print()
    print("%s." % ("Escrito" if aplica else "Faria isso"))
    if not aplica:
        print("Nada foi alterado. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
