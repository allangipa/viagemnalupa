# -*- coding: utf-8 -*-
"""Instala o Travelpayouts Drive no <head> de todas as páginas do site.

O bloco entra entre marcadores <!-- tp-drive:inicio --> e <!-- tp-drive:fim -->,
para que desinstala.py consiga removê-lo com exatidão, sem depender de casar
o conteúdo do script.

Rode em seco por padrão. Passe --aplica para gravar.

    python _build/drive/instala.py            (mostra o que faria)
    python _build/drive/instala.py --aplica   (grava)
"""
import io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IGNORAR = ("\\.git\\", "Claude outputs", "_build")

BLOCO = """<!-- tp-drive:inicio
     Travelpayouts Drive, marcador 775563. Instalado em 16/set/2026.
     Identifica o navegador, detecta bloqueador de anuncio, registra cliques
     de saida e pode injetar unidades com marca de parceiro.
     Declarado ao leitor em /privacidade/.
     Desde 18/10/2026 entra no primeiro gesto do leitor ou 4 s depois do
     load, como o AdSense: sao 59 KB que disputavam a primeira pintura, e
     clique de parceiro acontece depois de um gesto de qualquer jeito.
     Para remover: python _build/drive/desinstala.py --aplica -->
<script nowprocket data-noptimize="1" data-cfasync="false" data-wpfc-render="false" seraph-accel-crit="1" data-no-defer="1" data-cmp-ab="2">
  (function () {
      var feito = false, gestos = ["scroll", "touchstart", "keydown", "pointerdown", "mousemove"], timer = 0;
      function entra() {
          if (feito) return; feito = true;
          clearTimeout(timer);
          gestos.forEach(function (g) { window.removeEventListener(g, entra); });
          var script = document.createElement("script");
          script.async = 1;
          script.setAttribute("data-cmp-ab","2");
          script.src = 'https://tpembars.com/NTcyMDMw.js?t=572030';
          document.head.appendChild(script);
      }
      function armar() {
          gestos.forEach(function (g) { window.addEventListener(g, entra, { once: true, passive: true }); });
          timer = setTimeout(entra, 4000);
      }
      if (document.readyState === "complete") armar();
      else window.addEventListener("load", armar, { once: true });
  })();
</script>
<!-- tp-drive:fim -->
"""

# qualquer instalacao anterior, inclusive a do teste de uma pagina so
ANTIGO = re.compile(
    r"(?:<!-- TESTE: Travelpayouts Drive.*?-->\s*)?"
    r"<script nowprocket[^>]*>.*?tpembars\.com.*?</script>\s*",
    re.S)
MARCADO = re.compile(r"<!-- tp-drive:inicio.*?<!-- tp-drive:fim -->\s*", re.S)


def paginas():
    for base, _, arquivos in os.walk(RAIZ):
        if any(x in base + "\\" for x in IGNORAR):
            continue
        for a in arquivos:
            if a.endswith(".html"):
                yield os.path.join(base, a)


def main():
    aplica = "--aplica" in sys.argv
    tocadas = puladas = 0
    for p in sorted(paginas()):
        rel = os.path.relpath(p, RAIZ)
        html = io.open(p, encoding="utf-8").read()
        limpo = MARCADO.sub("", ANTIGO.sub("", html))
        if "</head>" not in limpo:
            print("  SEM <head>, pulada: %s" % rel)
            puladas += 1
            continue
        novo = limpo.replace("</head>", BLOCO + "</head>", 1)
        if novo == html:
            puladas += 1
            continue
        tocadas += 1
        print("  %s %s" % ("instalada:" if aplica else "instalaria:", rel))
        if aplica:
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
    print("\n%d páginas, %d já estavam certas" % (tocadas, puladas))
    if not aplica:
        print("(seco — nada gravado; use --aplica)")


if __name__ == "__main__":
    main()
