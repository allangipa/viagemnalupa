# -*- coding: utf-8 -*-
"""Resolve marcadores de conflito de merge deixados em arquivo publicado.

O que aconteceu
---------------
Um git pull juntou duas historias que tinham mexido na mesma area das
fichas de Buenos Aires e Maceio, e o merge foi gravado com os marcadores
dentro do HTML. Trinta e nove marcadores, treze conflitos, os dois lados
colados no arquivo - e o arquivo foi para o ar assim.

Foi assim que apareceu: contei 12 pontos, 6 fotos e 12 molduras vazias em
Buenos Aires. O numero nao fechava porque o arquivo tinha as duas
versoes do mesmo trecho.

A resolucao
-----------
Em todos os treze o padrao e o mesmo:

    HEAD  -> <figure class="foto"><img src="...webp" alt="..."> - a foto
    OUTRO -> <div class="foto-slot"> com icone e botao de buscar - a
             moldura vazia que existia antes da foto entrar

Fica o HEAD. As treze imagens foram conferidas em disco antes: existem
todas. Resolver para um <figure> cuja imagem nao existisse trocaria um
problema por outro.

Este script e generico de proposito: se acontecer de novo, ele lista os
conflitos e so resolve sozinho os que seguem esse padrao - foto de um
lado, moldura vazia do outro. Qualquer outro conflito ele mostra e para,
porque conflito de texto quem resolve e gente.

Uso
---
    python _build/conserto/conflitos.py
    python _build/conserto/conflitos.py --aplica
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

CONFLITO = re.compile(
    r"(?s)^<{7}[^\n]*\n(?P<a>.*?)^={7}\n(?P<b>.*?)^>{7}[^\n]*\n", re.M)


def arquivos():
    for dp, dirs, fs in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules")]
        for f in sorted(fs):
            if f.endswith((".html", ".css", ".js", ".py", ".xml", ".txt")):
                yield os.path.join(dp, f)


def foto_contra_moldura(a, b):
    """True quando o lado A traz a foto e o lado B a moldura vazia."""
    return ("<img" in a and "foto-slot" not in a
            and "<img" not in b and "foto-slot" in b)


def imagens_existem(trecho, base):
    for src in re.findall(r'<img[^>]+src="([^"]+)"', trecho):
        cam = os.path.normpath(os.path.join(base, src.replace("/", os.sep)))
        if not os.path.isfile(cam):
            return False, src
    return True, None


def main(aplica):
    total = resolvidos = parados = 0
    for p in arquivos():
        t = open(p, encoding="utf-8").read()
        if not CONFLITO.search(t):
            continue
        rel = os.path.relpath(p, RAIZ).replace(os.sep, "/")
        base = os.path.dirname(p)
        print("=== %s ===" % rel)
        duvida = [0]

        def um(m):
            a, b = m.group("a"), m.group("b")
            if not foto_contra_moldura(a, b):
                duvida[0] += 1
                print("   !! conflito fora do padrao - NAO resolvo sozinho")
                print("      HEAD : %s" % re.sub(r"\s+", " ", a)[:90])
                print("      OUTRO: %s" % re.sub(r"\s+", " ", b)[:90])
                return m.group(0)
            ok, falta = imagens_existem(a, base)
            if not ok:
                duvida[0] += 1
                print("   !! a foto do lado HEAD nao existe: %s" % falta)
                return m.group(0)
            src = re.search(r'<img[^>]+src="([^"]+)"', a).group(1)
            print("   fica a foto  %s" % src)
            return a

        novo, n = CONFLITO.subn(um, t)
        total += n
        resolvidos += n - duvida[0]
        parados += duvida[0]
        if aplica and duvida[0] == 0 and novo != t:
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(novo)
        elif duvida[0]:
            print("   arquivo NAO gravado: ha conflito que preciso que "
                  "alguem olhe")
        print()

    print("%d conflito(s): %d no padrao foto-contra-moldura, %d para olhar."
          % (total, resolvidos, parados))
    if not total:
        print("Nenhum marcador de conflito no repositorio.")
    elif not aplica:
        print("Nada foi alterado. Rode com --aplica para escrever.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
