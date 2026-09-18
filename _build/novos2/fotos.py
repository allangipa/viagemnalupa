# -*- coding: utf-8 -*-
"""Converte as fotos baixadas do Storyblocks para o formato das fichas.

Quatro imagens, escolhidas olhando uma por uma antes de gastar download -
e quatro descartadas no caminho por estarem mal rotuladas (uma dizia
"Our Lady of Nahuel Huapi Cathedral" e mostrava a cidade inteira; outra
dizia "San Eduardo Church" e era um telhado a prumo; a do "Cerro Otto"
era so ceu e nuvem).

Le de ~/Downloads pelo SBI do nome do arquivo, corta 16:9 no centro,
redimensiona para 1200x675 e grava em assets/img/<destino>/.

Uso
---
    python _build/novos2/fotos.py
    python _build/novos2/fotos.py --aplica
"""
import io
import os
import sys

from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BAIXADOS = os.path.join(os.path.expanduser("~"), "Downloads")

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# sbi -> (destino, nome do arquivo de saida)
FOTOS = {
    "357309567": ("bariloche", "circuito-chico"),
    "357934593": ("bariloche", "parque-nahuel-huapi"),
    "358012617": ("punta-cana", "playa-bavaro"),
    "357989562": ("punta-cana", "isla-saona"),
}


def acha(sbi):
    for f in os.listdir(BAIXADOS):
        if ("SBI-" + sbi) in f and f.lower().endswith((".jpg", ".jpeg", ".png")):
            return os.path.join(BAIXADOS, f)
    return None


def converte(origem, destino, aplica):
    im = Image.open(origem).convert("RGB")
    lo, ao = im.size
    alvo = 16 / 9
    if lo / ao > alvo:
        nl = int(ao * alvo)
        im = im.crop(((lo - nl) // 2, 0, (lo - nl) // 2 + nl, ao))
    else:
        na = int(lo / alvo)
        im = im.crop((0, (ao - na) // 2, lo, (ao - na) // 2 + na))
    im = im.resize((1200, 675), Image.LANCZOS)
    if aplica:
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        im.save(destino, "WEBP", quality=82, method=6)
    return lo, ao


def main(aplica):
    print("lendo de %s" % BAIXADOS)
    print()
    faltam = 0
    for sbi, (slug, nome) in sorted(FOTOS.items(), key=lambda x: x[1]):
        src = acha(sbi)
        if not src:
            print("  SBI-%s  NAO ACHEI o arquivo baixado" % sbi)
            faltam += 1
            continue
        dst = os.path.join(RAIZ, "assets", "img", slug, nome + ".webp")
        lo, ao = converte(src, dst, aplica)
        tam = (os.path.getsize(dst) / 1024) if (aplica and os.path.isfile(dst)) else 0
        print("  %-12s %-22s %dx%d -> 1200x675   %s"
              % (slug, nome + ".webp", lo, ao,
                 ("%.0f KB" % tam) if tam else "(ensaio)"))

    print()
    if faltam:
        print("%d arquivo(s) nao encontrado(s) em Downloads." % faltam)
    print("%s." % ("Escrito" if aplica else "Faria isso"))
    if not aplica:
        print("Nada gravado. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
