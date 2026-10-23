# -*- coding: utf-8 -*-
"""O bloco "As respostas mais procuradas" na home: as paginas de cluster.

As paginas de uma pergunta so (Cristo, Pena, o que fecha cada dia,
descontos, aeroporto...) so eram alcancadas a partir do guia de cada
cidade, a dois cliques da raiz. Este bloco as poe a um clique.

NADA E ESCRITO A MAO: a lista sai do disco. Pagina de cluster e toda
destinos/<cidade>/<pasta>/index.html que nao seja quanto-custa nem
roteiro-N-dias. O rotulo e o ultimo item das migalhas da propria pagina
("Cristo Redentor", "O que fecha cada dia"); a ordem e a do sitemap.xml;
o nome da cidade vem do DESTINOS do schema/gera.py, como no /gratis/.
Cidade nova com cluster entra sozinha na proxima rodada.

O bloco fica entre <!-- cluster:inicio --> e <!-- cluster:fim -->, logo
depois do cartao de /gratis/. Idempotente.

Uso
---
    python _build/cluster/home.py            # so mostra
    python _build/cluster/home.py --aplica   # escreve
"""
import html as H
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from comum import le, escreve, limpa, junta, RAIZ, SITE  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

INI, FIM = "<!-- cluster:inicio -->", "<!-- cluster:fim -->"
FORA = re.compile(r"^(quanto-custa|roteiro-\d+-dias)$")


def nomes_dos_destinos():
    s = le(os.path.join(RAIZ, "_build", "schema", "gera.py"))
    m = re.search(r"(?s)^DESTINOS = \{(.*?)^\}", s, re.M)
    return dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', m.group(1)))


def paginas_de_cluster():
    """{slug: [(pasta, rotulo)]}, na ordem do sitemap."""
    mapa = le(os.path.join(RAIZ, "sitemap.xml"))
    ordem = re.findall(r"<loc>%s/destinos/([^/<]+)/([^/<]+)/</loc>" % re.escape(SITE), mapa)
    saida = {}
    for slug, pasta in ordem:
        if FORA.match(pasta):
            continue
        arq = os.path.join(RAIZ, "destinos", slug, pasta, "index.html")
        if not os.path.isfile(arq):
            continue
        mig = re.search(r'<p class="migalhas">(.*?)</p>', le(arq), re.S)
        rotulo = limpa(mig.group(1).split("›")[-1]) if mig else ""
        if not rotulo:
            sys.exit("PARADO: %s sem migalhas para dar o rotulo" % arq)
        saida.setdefault(slug, []).append((pasta, rotulo))
    # pagina de cluster que existe em disco mas nao esta no sitemap: avisa
    for slug in os.listdir(os.path.join(RAIZ, "destinos")):
        d = os.path.join(RAIZ, "destinos", slug)
        if not os.path.isdir(d):
            continue
        for pasta in os.listdir(d):
            if os.path.isfile(os.path.join(d, pasta, "index.html")) and not FORA.match(pasta) \
                    and pasta not in [p for p, _ in saida.get(slug, [])]:
                print("   AVISO: destinos/%s/%s/ fora do sitemap - nao entra no bloco" % (slug, pasta))
    return saida


def bloco(cluster, nomes):
    linhas = []
    for slug in cluster:
        links = "".join('<a class="cc" href="./destinos/%s/%s/">%s</a>' % (slug, pasta, H.escape(rot))
                        for pasta, rot in cluster[slug])
        linhas.append('  <nav class="calc-cidades" aria-label="Páginas de %s"><span class="cc-rot">%s</span>%s</nav>'
                      % (H.escape(nomes[slug]), H.escape(nomes[slug]), links))
    n = sum(len(v) for v in cluster.values())
    cidades = junta([nomes[s] for s in cluster])
    return ('%s\n<section class="bloco" id="respostas">\n  <div class="bloco-head">\n'
            '    <span class="eyebrow">Uma pergunta, uma página</span>\n'
            '    <h2>As respostas mais procuradas</h2>\n'
            '    <p>Ingresso, o que fecha em cada dia, descontos, quando ir, como sair do aeroporto: %d páginas que '
            'respondem uma pergunta só, com o número, a fonte e a data. Cidades com páginas assim, por enquanto: %s.</p>\n  </div>\n%s\n'
            '</section>\n%s' % (INI, n, cidades, "\n".join(linhas), FIM))


def main(aplica):
    nomes = nomes_dos_destinos()
    cluster = paginas_de_cluster()
    if not cluster:
        print("   nenhuma pagina de cluster no sitemap")
        return
    novo = bloco(cluster, nomes)
    home = os.path.join(RAIZ, "index.html")
    h = le(home)
    if INI in h:
        h2 = re.sub(r"(?s)%s.*?%s" % (re.escape(INI), re.escape(FIM)), lambda m: novo, h, count=1)
    else:
        m = re.search(r'(?s)<section class="bloco">\s*<div class="destaque">.*?href="\./gratis/".*?</section>\n', h)
        if not m:
            sys.exit("PARADO: nao achei o cartao de /gratis/ na home para encaixar o bloco")
        h2 = h[:m.end()] + "\n" + novo + "\n" + h[m.end():]
    for slug, itens in cluster.items():
        print("   %-16s %d paginas: %s" % (slug, len(itens), ", ".join(r for _, r in itens)))
    if h2 == h:
        print("   home: ja igual")
    else:
        print("   home: %s" % ("escrito" if aplica else "SO MOSTRANDO"))
        if aplica:
            escreve(home, h2)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
