# -*- coding: utf-8 -*-
"""Poe o Porto nos dois indices, e acerta os contadores.

Mesmo molde do novos2/cartoes.py, que fez isso por Bariloche e Punta
Cana. O verificador pegou o estado intermediario de novo, que e
exatamente o que ele existe para pegar:

    index.html: o placar diz 133 pontos apurados, somam 149
    /index.html: fala em 12 destinos, existem 13
    /destinos/index.html: fala em 12 destinos, existem 13

A ficha estava em disco, ja no sitemap, e nenhum indice a listava - o
Google achava, o visitante nao.

A CAPA
------
View of Porto old town from Cais de Gaia with Porto Cathedral, de Jakub
Halun, CC BY 4.0, obra propria, 5968x4032, feita em 05/06/2025. Licenca
conferida na API do Commons, no campo LicenseShortName do proprio
arquivo - nao na etiqueta da pagina, que e o erro que o CLAUDE.md do
Vestigio Oculto registra ter quase passado com material do Vesuvius
Challenge.

Escolhida olhando, em folha de contato 3x3 com todos os nove candidatos
ja recortados em 16:9 - porque no cartao o que importa e como a imagem
le em miniatura, nao em tamanho cheio. Descartei:

  - uma noturna, bonita e escura demais para cartao
  - duas lavadas, de ceu estourado
  - uma de rua vazia, que nao diz "Porto" a quem nunca foi
  - o panorama mais largo, cujo terco esquerdo e estacionamento

O corte central deixa a agua no terco de baixo, que e onde a legenda do
cartao pousa. Foi sorte, mas fica registrado para a proxima: capa boa
tem area calma embaixo.

Cap de dois por autor na busca, que e a licao do episodio 05 do canal -
doze de dezesseis imagens tinham vindo da mesma sessao de um fotografo
so, e a folha de contato denunciou o que a contagem de arquivos nao viu.

Uso
---
    python _build/porto/cartao.py
    python _build/porto/cartao.py --aplica
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

# Por caminho, nao por nome: existem varios dados.py em _build e o
# sys.modules devolve o primeiro que ja tiver sido carregado.
_spec = importlib.util.spec_from_file_location(
    "porto_dados", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d)
DESTINOS = _d.DESTINOS

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Os numeros que estao nos indices ANTES desta rodada. Explicitos para a
# substituicao ser verificavel: se nao encontrar, o script avisa em vez
# de seguir calado - substituicao que nao casa com nada e pior que erro,
# porque passa.
ANTES_DESTINOS = 12
ANTES_PONTOS = 133

CAPAS = {
    "porto": dict(
        arq="ribeira.webp",
        alt=("A frente da Ribeira do Porto vista da outra margem do Douro, com "
             "as casas coloridas encostadas na encosta, a Sé e o Paço Episcopal "
             "no alto e um barco rabelo passando em primeiro plano"),
        cred="Jakub Hałun · CC BY 4.0 · via Wikimedia Commons"),
}

# Os dois numeros em destaque e o achado. Sao os mesmos fatos que a ficha
# apura, aqui em forma curta.
RESUMO = {
    "porto": dict(
        numeros=[("Livraria Lello, dedutível em livro", "15,95 €", False),
                 ("Ponte, Ribeira e São Bento", "grátis", True)],
        # O achado e o da Ponte, e nao o do preco, porque e o unico dos
        # tres que o visitante consegue conferir sozinho depois - basta
        # abrir a ficha do DGPC. Achado que o leitor pode checar vale
        # mais que achado que ele tem de acreditar.
        achado=("<b>A Ponte Dom Luís I não é de Gustave Eiffel.</b> É de "
                "Théophile Seyrig, que foi sócio dele na Ponte D. Maria — "
                "outra ponte, oito anos antes. Quem assina está escrito na "
                "ficha do Património Cultural.")),
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
                   if os.path.isfile(os.path.join(RAIZ, "destinos", s,
                                                  "index.html")))
    soma = sum(pontos_de(s) for s in todos)
    print("destinos em disco: %d      pontos somados: %d" % (len(todos), soma))

    # A capa tem de existir antes de o cartao apontar para ela. Cartao com
    # <img> quebrado e pior que cartao ausente: o leitor ve moldura vazia.
    for slug, capa in CAPAS.items():
        cam = os.path.join(RAIZ, "assets", "img", slug, capa["arq"])
        if not os.path.isfile(cam):
            raise SystemExit("PARADO: capa nao existe em disco: %s" % cam)
    print("capas conferidas em disco: %d" % len(CAPAS))
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

        h, n1 = re.subn(r"\b%d(?=\s+destinos\b)" % ANTES_DESTINOS,
                        str(len(todos)), h)
        h, n2 = re.subn(r"(>)\s*%d\s*(<)" % ANTES_PONTOS,
                        r"\g<1>%d\g<2>" % soma, h)
        print("  %-22s contadores: %d de destinos, %d de pontos"
              % (idx, n1, n2))
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
