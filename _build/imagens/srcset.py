# -*- coding: utf-8 -*-
"""Gera as versoes menores de cada foto e poe srcset nos <img>.

O NUMERO QUE JUSTIFICA ISTO
---------------------------
Medido no Porto: as 17 imagens da ficha somam 1.981 KB servidas a 1200 px.
As mesmas a 600 px dao 587 KB - 71% a menos. O site inteiro tem 128 webp
e 20 MB, e TODAS sao entregues em 1200 px, inclusive para um celular que
mostra a foto em 360 px de largura.

Nao havia srcset em lugar nenhum do site. O navegador nao tinha como
escolher: recebia a maior e encolhia na tela.

DE ONDE SAI O sizes
-------------------
Nao foi chutado. Saiu do site.css:

    .wrap        max-width:70rem                  = 1120 px
    .miolo       max-width:46.5rem (>= 1500 px)   =  744 px
    .com-lateral grid 16rem + resto (>= 1080 px)  ~  820 px
    figure.foto img { width:100% }

Ou seja: com barra lateral a foto nunca passa de ~820 px, e abaixo de
1080 px ela ocupa a largura da coluna, que no celular e a da tela.

    sizes="(min-width:1080px) 820px, 100vw"

LARGURAS GERADAS, E POR QUE ESTAS
---------------------------------
400, 640 e 820, mais a original de 1200 que ja existe.

    360 px de tela x2 de densidade = 720  ->  pega a de 820
    525 px do cartao na home       = 525  ->  pega a de 640
    744 px do miolo com lateral    = 744  ->  pega a de 820

A de 1200 continua no srcset para tela densa e para quem abre a imagem.
Nenhum arquivo e apagado: o src original fica como estava, entao pagina
que este script nao tocar continua funcionando igual.

O ARQUIVO SO E GERADO SE A ORIGINAL FOR MAIOR
---------------------------------------------
Foto de 568 px nao ganha variante de 640 nem de 820 - seria a mesma
imagem reamostrada para cima, maior em bytes e pior em nitidez. O srcset
dela sai so com as larguras que existem de fato.

Uso
---
    python _build/imagens/srcset.py            # so mostra
    python _build/imagens/srcset.py --aplica   # gera e escreve
"""
import io
import os
import re
import sys

from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMG = os.path.join(RAIZ, "assets", "img")

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

LARGURAS = (400, 640, 820)
SIZES = "(min-width:1080px) 820px, 100vw"

# A original foi salva pelo pipeline do site; 82 e o ponto em que o webp
# para de render ganho visivel neste tipo de foto. method=6 e o encoder
# lento, que e o certo para arquivo gerado uma vez e servido muitas.
QUALIDADE = dict(quality=82, method=6)

PULAR = ("favicon", "og-image", "marca-")


def paginas():
    for dirp, _, arqs in os.walk(RAIZ):
        if any(x in dirp for x in ("_build", ".git", "Claude outputs",
                                   ".claude", "node_modules")):
            continue
        for a in arqs:
            if a.endswith(".html"):
                yield os.path.join(dirp, a)


def variante(rel, w):
    raiz, ext = os.path.splitext(rel)
    return "%s-%d%s" % (raiz, w, ext)


def gera(aplica):
    """Cria as versoes menores. Devolve {rel: [larguras que existem]}."""
    feito = {}
    novos = bytes_novos = 0
    for dirp, _, arqs in os.walk(IMG):
        for a in sorted(arqs):
            if not a.endswith(".webp"):
                continue
            if any(p in a for p in PULAR):
                continue
            if re.search(r"-(\d{3,4})\.webp$", a):
                continue                      # ja e variante
            cam = os.path.join(dirp, a)
            rel = os.path.relpath(cam, RAIZ).replace(os.sep, "/")
            try:
                with Image.open(cam) as im:
                    lw, lh = im.size
            except Exception as e:
                print("  nao abri %s (%s)" % (rel, type(e).__name__))
                continue
            tem = []
            for w in LARGURAS:
                if w >= lw:
                    continue
                alvo = os.path.join(RAIZ, variante(rel, w).replace("/", os.sep))
                tem.append(w)
                if os.path.isfile(alvo):
                    continue
                novos += 1
                if aplica:
                    with Image.open(cam) as im:
                        h = max(1, round(im.height * w / im.width))
                        im.convert("RGB").resize((w, h), Image.LANCZOS).save(
                            alvo, "WEBP", **QUALIDADE)
                    bytes_novos += os.path.getsize(alvo)
            feito[rel] = (tem, lw)
    print("originais: %d    variantes a gerar: %d" % (len(feito), novos))
    if aplica and bytes_novos:
        print("bytes gravados em variantes: %.1f MB" % (bytes_novos / 1048576.0))
    return feito


def marca(aplica, feito):
    """Poe srcset e sizes nos <img> que apontam para as originais."""
    tocadas = tags = 0
    for p in sorted(paginas()):
        htm = antes = io.open(p, encoding="utf-8", errors="replace").read()
        aqui = 0

        def troca(m):
            nonlocal aqui
            tag, src = m.group(0), m.group(1)
            if "srcset=" in tag:
                return tag
            rel = re.sub(r"^(?:\.\./)+|^\./", "", src)
            if rel not in feito:
                return tag
            larguras, largura = feito[rel]
            if not larguras:
                return tag
            # o <img> aponta com caminho relativo ("../../assets/..."); a
            # variante tem de sair com o MESMO prefixo, senao a pagina de
            # dentro de destinos/x/ pediria a imagem da raiz.
            if not src.endswith(rel):
                return tag
            prefixo = src[:len(src) - len(rel)]
            partes = ["%s%s %dw" % (prefixo, variante(rel, w), w) for w in larguras]
            partes.append("%s %dw" % (src, largura))
            aqui += 1
            return tag.replace("<img ", '<img srcset="%s" sizes="%s" '
                               % (", ".join(partes), SIZES), 1)

        htm = re.sub(r'<img [^>]*src="([^"]+\.webp)"[^>]*>', troca, htm)
        if aqui:
            tags += aqui
            tocadas += 1
            if aplica and htm != antes:
                io.open(p, "w", encoding="utf-8", newline="").write(htm)
    print("paginas com <img> marcado: %d    tags marcadas: %d" % (tocadas, tags))
    return tags


def main(aplica):
    feito = gera(aplica)
    marca(aplica, feito)
    if not aplica:
        print("\nNada foi gerado nem escrito. Rode com --aplica.")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplica" in sys.argv))
