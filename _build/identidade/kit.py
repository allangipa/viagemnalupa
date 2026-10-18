# -*- coding: utf-8 -*-
"""Gera o kit da marca a partir do emblema escolhido (candidatas/c2.png).

O EMBLEMA
---------
Candidata 2 de quatro, GPT Image 2.5 no Higgsfield, 18/10/2026, com o
marca-1024 antigo como referencia de composicao (globo, lupa de aro
dourado, meridianos ciano, arco de rota na lente). O registro do trabalho
esta em candidatas/job2.json. Custou 1,5 credito; as quatro, 6. O Allan
escolheu a 2 pela leitura a 110 px: o aro largo de latao faz o distintivo
e a 40 px ainda se reconhece. E o mesmo registro das marcas do Guia
Produto na Lupa, do Vestigio Oculto e do Xadrez Belico - emblema
renderizado sobre fundo carvao.

O QUE SAI, E PARA ONDE
----------------------
    avatar-1080.png           o perfil do Instagram (encolhido 8%: a ponta
                              do cabo chega a 1017 px de raio num circulo
                              de 1024, e o recorte circular roeria o latao)
    avatar-previa-circulo.png so para olhar, como o Instagram mostra
    favicon-32/512, apple-touch-icon.png
                              recorte justo no distintivo, fundo solido
    marca-1024.png            o emblema inteiro (logo da Organization)
    marca-cabecalho-64/128    o icone de 30 px do cabecalho, PNG com alfa
                              (o SVG com variaveis saiu em 18/10, a pedido)
    og-image.png              NAO sai daqui: e o og.html renderizado pelo
                              Chrome headless, porque tem texto nas fontes
                              do site (ver o comentario do og.html)

Os arquivos vao para assets/img com os mesmos nomes. A troca do SVG pelo
<img> nas paginas e do identidade/aplica.py, que le o prefixo do href.

Uso
---
    python _build/identidade/kit.py            # escreve em _build/identidade/
    python _build/identidade/kit.py --aplica   # e copia os cinco para assets/img
"""
import os
import shutil
import sys

import numpy as np
from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
FONTE = os.path.join(AQUI, "candidatas", "c2.png")
PARA_O_SITE = ("favicon-32.png", "favicon-512.png", "apple-touch-icon.png", "marca-1024.png",
               "marca-cabecalho-64.png", "marca-cabecalho-128.png")


def main(aplica):
    src = Image.open(FONTE).convert("RGB")
    W = src.width
    a = np.asarray(src).astype(int)
    fundo = tuple(int(v) for v in a[:40, :40].reshape(-1, 3).mean(0))

    # avatar: encolhe para caber no circulo inscrito
    k = 0.92
    av = Image.new("RGB", (W, W), fundo)
    s = src.resize((int(W * k), int(W * k)), Image.LANCZOS)
    av.paste(s, ((W - s.width) // 2, (W - s.height) // 2))
    av = av.resize((1080, 1080), Image.LANCZOS)
    av.save(os.path.join(AQUI, "avatar-1080.png"))
    m = Image.new("L", (1080, 1080), 0)
    ImageDraw.Draw(m).ellipse((0, 0, 1079, 1079), fill=255)
    pv = Image.new("RGB", (1080, 1080), (255, 255, 255))
    pv.paste(av, (0, 0), m)
    pv.save(os.path.join(AQUI, "avatar-previa-circulo.png"))

    # favicon e apple-touch: a caixa do conteudo, com 4% de folga
    mk = np.abs(a - np.array(fundo)).sum(2) > 60
    ys, xs = np.nonzero(mk)
    x0, y0, x1, y1 = xs.min(), ys.min(), xs.max(), ys.max()
    lado = max(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    half = lado // 2 + int(lado * 0.04)
    caixa = Image.new("RGB", (2 * half, 2 * half), fundo)
    caixa.paste(src.crop((cx - half, cy - half, cx + half, cy + half)), (0, 0))
    for nome, n in (("favicon-512.png", 512), ("favicon-32.png", 32), ("apple-touch-icon.png", 180)):
        caixa.resize((n, n), Image.LANCZOS).save(os.path.join(AQUI, nome))
    src.resize((1024, 1024), Image.LANCZOS).save(os.path.join(AQUI, "marca-1024.png"))

    # cabecalho (30 px, 2x = 64): PNG com alfa. Recortar por cor deixava um
    # halo da vinheta no tema claro; o disco do aro e um circulo, achado pelo
    # latao (R alto, B baixo), e so o cabo, fora do disco, sai por cor.
    latao = (a[..., 0] > 150) & (a[..., 2] < 110) & (a[..., 0] - a[..., 2] > 70)
    ly, lx = np.nonzero(latao)
    xL, yT = lx.min(), ly.min()
    ccx = int(np.median(lx[ly == yT])); ccy = int(np.median(ly[lx == xL])); r = ccx - xL
    yy, xx = np.mgrid[0:W, 0:W]
    dist = np.sqrt((xx - ccx) ** 2 + (yy - ccy) ** 2)
    d = np.abs(a - np.array(fundo)).sum(2)
    disco = np.clip((r + 6 - dist) / 6, 0, 1)
    cabo = np.clip((d - 60) / 50, 0, 1) * (dist > r)
    alfa = np.maximum(disco, cabo)
    im = Image.fromarray(np.dstack([a, alfa * 255]).astype("uint8"), "RGBA")
    ay, ax = np.nonzero(alfa > 0.05)
    im = im.crop((ax.min(), ay.min(), ax.max() + 1, ay.max() + 1))
    q = Image.new("RGBA", (max(im.size),) * 2, (0, 0, 0, 0))
    q.paste(im, ((q.width - im.width) // 2, (q.height - im.height) // 2))
    for n in (128, 64):
        q.resize((n, n), Image.LANCZOS).save(os.path.join(AQUI, "marca-cabecalho-%d.png" % n))
    print("   kit escrito em _build/identidade/  (fundo %s, distintivo %d px, disco r=%d)" % (fundo, lado, r))

    if aplica:
        for nome in PARA_O_SITE + ("og-image.png",):
            de = os.path.join(AQUI, nome)
            if not os.path.exists(de):
                print("   FALTA %s (o og-image vem do og.html pelo Chrome)" % nome)
                continue
            shutil.copyfile(de, os.path.join(RAIZ, "assets", "img", nome))
            print("   assets/img/%s" % nome)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
