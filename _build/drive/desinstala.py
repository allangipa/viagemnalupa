# -*- coding: utf-8 -*-
"""Remove o Travelpayouts Drive de todas as páginas do site.

O contrário exato de instala.py. Não depende de reconhecer o conteúdo do
script: apaga tudo que estiver entre <!-- tp-drive:inicio --> e
<!-- tp-drive:fim -->, e também pega instalações antigas, sem marcador.

Rode em seco por padrão. Passe --aplica para gravar.

    python _build/drive/desinstala.py            (mostra o que faria)
    python _build/drive/desinstala.py --aplica   (grava)

Depois de rodar, lembre de ajustar /privacidade/ — a seção que declara o
Drive ao leitor precisa sair junto, senão a página passa a descrever uma
coleta que não acontece mais.
"""
import io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IGNORAR = ("\\.git\\", "Claude outputs", "_build")

MARCADO = re.compile(r"<!-- tp-drive:inicio.*?<!-- tp-drive:fim -->\s*", re.S)
SEM_MARCA = re.compile(
    r"(?:<!-- TESTE: Travelpayouts Drive.*?-->\s*)?"
    r"<script nowprocket[^>]*>.*?tpembars\.com.*?</script>\s*",
    re.S)


def paginas():
    for base, _, arquivos in os.walk(RAIZ):
        if any(x in base + "\\" for x in IGNORAR):
            continue
        for a in arquivos:
            if a.endswith(".html"):
                yield os.path.join(base, a)


def main():
    aplica = "--aplica" in sys.argv
    tocadas = 0
    for p in sorted(paginas()):
        rel = os.path.relpath(p, RAIZ)
        html = io.open(p, encoding="utf-8").read()
        novo = SEM_MARCA.sub("", MARCADO.sub("", html))
        if novo == html:
            continue
        tocadas += 1
        print("  %s %s" % ("removido de:" if aplica else "removeria de:", rel))
        if aplica:
            io.open(p, "w", encoding="utf-8", newline="").write(novo)

    restantes = sum(1 for p in paginas()
                    if "tpembars" in io.open(p, encoding="utf-8").read())
    print("\n%d páginas alteradas. Ainda mencionam tpembars: %d" % (tocadas, restantes))
    if restantes and aplica:
        print("  (a página de privacidade cita o nome no texto — isso é esperado)")
    if not aplica:
        print("(seco — nada gravado; use --aplica)")


if __name__ == "__main__":
    main()
