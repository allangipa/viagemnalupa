# -*- coding: utf-8 -*-
"""Instala o Google AdSense em todas as paginas do site.

Poe dois blocos, cada um entre marcadores, para que desinstala.py consiga
remove-los com exatidao:

  no <head>   <!-- adsense:inicio --> meta de verificacao + preconnect <!-- adsense:fim -->
  no </body>  <!-- consentimento:inicio --> tag do assets/js/consentimento.js <!-- consentimento:fim -->

O script do AdSense em si NAO vai escrito no HTML: quem o injeta e o
consentimento.js, conforme a escolha do leitor na faixa.

De quebra, garante no rodape os links Sobre e Contato ao lado de
Privacidade (a pagina /contato/ nasceu junto com o AdSense).

Idempotente: rodado duas vezes, a segunda nao muda nada. Rode de novo
depois de regerar qualquer pagina com os geradores de _build/ - eles nao
sabem do AdSense, e _build/confere/tudo.py reclama da pagina sem os blocos.

    python _build/adsense/instala.py            (mostra o que faria)
    python _build/adsense/instala.py --aplica   (grava)
"""
import hashlib, io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IGNORAR = ("\\.git\\", "/.git/", "Claude outputs", "_build", "node_modules")
PUB = "pub-4401770243539507"

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

CABECA = """<!-- adsense:inicio
     Google AdSense, ca-%s. Instalado em 2/out/2026.
     O script de anuncio entra por assets/js/consentimento.js, nao por aqui.
     Para remover: python _build/adsense/desinstala.py --aplica -->
<meta name="google-adsense-account" content="ca-%s">
<link rel="preconnect" href="https://pagead2.googlesyndication.com" crossorigin>
<!-- adsense:fim -->
""" % (PUB, PUB)

PE = ('<!-- consentimento:inicio --><script src="/assets/js/consentimento.js?v=%s" defer>'
      '</script><!-- consentimento:fim -->\n')

M_CABECA = re.compile(r"<!-- adsense:inicio.*?<!-- adsense:fim -->\s*", re.S)
M_PE = re.compile(r"<!-- consentimento:inicio -->.*?<!-- consentimento:fim -->\s*", re.S)

# rodape: "... · <a href="P/privacidade/">Privacidade</a>"  ->  com Sobre e Contato antes
ROD_PRIV = re.compile(r'(viagemnalupa\.com\.br) · <a href="([^"]*?)privacidade/">Privacidade</a></p>')
# a propria pagina de privacidade nao linka para si
ROD_SEM = re.compile(r'(<p>© 2026 Viagem na Lupa · viagemnalupa\.com\.br)</p>')


def paginas():
    for base, _, arquivos in os.walk(RAIZ):
        b = base.replace("\\", "/") + "/"
        if any(x.replace("\\", "/") in b for x in IGNORAR):
            continue
        for a in arquivos:
            if a.endswith(".html"):
                yield os.path.join(base, a)


def hash_js():
    with open(os.path.join(RAIZ, "assets", "js", "consentimento.js"), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def rodape(html, rel):
    if 'contato/">Contato</a>' in html:
        return html
    if rel == "404.html":
        # a 404 e servida em qualquer profundidade: so caminho absoluto funciona
        return ROD_PRIV.sub(r'\1 · <a href="/sobre/">Sobre</a> · <a href="/contato/">Contato</a>'
                            r' · <a href="/privacidade/">Privacidade</a></p>', html, 1)
    novo = ROD_PRIV.sub(r'\1 · <a href="\2sobre/">Sobre</a> · <a href="\2contato/">Contato</a>'
                        r' · <a href="\2privacidade/">Privacidade</a></p>', html, 1)
    if novo == html and rel.replace("\\", "/") == "privacidade/index.html":
        novo = ROD_SEM.sub(r'\1 · <a href="../sobre/">Sobre</a> · <a href="../contato/">Contato</a></p>',
                           html, 1)
    return novo


def main():
    aplica = "--aplica" in sys.argv
    pe = PE % hash_js()
    tocadas = certas = 0
    erros = []
    for p in sorted(paginas()):
        rel = os.path.relpath(p, RAIZ)
        html = io.open(p, encoding="utf-8").read()
        limpo = M_PE.sub("", M_CABECA.sub("", html))
        if limpo.count("</head>") != 1 or limpo.count("</body>") != 1:
            erros.append(rel)
            continue
        novo = limpo.replace("</head>", CABECA + "</head>", 1)
        novo = novo.replace("</body>", pe + "</body>", 1)
        novo = rodape(novo, rel)
        if 'contato/">Contato</a>' not in novo:
            erros.append(rel + " (rodape sem link de Contato)")
        if novo == html:
            certas += 1
            continue
        tocadas += 1
        print("  %s %s" % ("instalada:" if aplica else "instalaria:", rel))
        if aplica:
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
    print("\n%d paginas alteradas, %d ja estavam certas" % (tocadas, certas))
    if erros:
        print("!!! sem <head>/<body> unico ou sem rodape reconhecivel:")
        for e in erros:
            print("   " + e)
        return 1
    if not aplica:
        print("(seco - nada gravado; use --aplica)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
