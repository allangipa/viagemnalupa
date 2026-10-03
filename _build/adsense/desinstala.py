# -*- coding: utf-8 -*-
"""Remove o Google AdSense de todas as paginas: os blocos entre
<!-- adsense:inicio --> e <!-- adsense:fim --> (meta de verificacao) e entre
<!-- consentimento:inicio --> e <!-- consentimento:fim --> (faixa e
carregador). Os links Sobre/Contato do rodape ficam.

Depois de rodar, atualize /privacidade/ - ela declara o AdSense.

    python _build/adsense/desinstala.py            (mostra o que faria)
    python _build/adsense/desinstala.py --aplica   (grava)
"""
import io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IGNORAR = ("/.git/", "Claude outputs", "_build", "node_modules")

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

M_CABECA = re.compile(r"<!-- adsense:inicio.*?<!-- adsense:fim -->\s*", re.S)
M_PE = re.compile(r"<!-- consentimento:inicio -->.*?<!-- consentimento:fim -->\s*", re.S)


def main():
    aplica = "--aplica" in sys.argv
    n = 0
    for base, _, arquivos in os.walk(RAIZ):
        b = base.replace("\\", "/") + "/"
        if any(x in b for x in IGNORAR):
            continue
        for a in arquivos:
            if not a.endswith(".html"):
                continue
            p = os.path.join(base, a)
            html = io.open(p, encoding="utf-8").read()
            novo = M_PE.sub("", M_CABECA.sub("", html))
            if novo != html:
                n += 1
                print("  %s %s" % ("removido:" if aplica else "removeria:", os.path.relpath(p, RAIZ)))
                if aplica:
                    io.open(p, "w", encoding="utf-8", newline="").write(novo)
    print("\n%d paginas" % n)
    if not aplica:
        print("(seco - nada gravado; use --aplica)")


if __name__ == "__main__":
    main()
