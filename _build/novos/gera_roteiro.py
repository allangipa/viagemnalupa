# -*- coding: utf-8 -*-
"""Escreve a pagina de roteiro de um destino novo, no molde da casa."""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

from roteiros import ROTEIROS          # noqa: E402
from dados import DESTINOS, APURACAO   # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SITE = "https://viagemnalupa.com.br"

CABECA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="IpjUvTgAQF5LxYdxAXXj2g3Qi-qh1KldEl7RelcQ9bo">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<link rel="canonical" href="{site}/destinos/{slug}/roteiro-{dias}-dias/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Viagem na Lupa">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:url" content="{site}/destinos/{slug}/roteiro-{dias}-dias/"><meta property="og:image" content="https://viagemnalupa.com.br/assets/img/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Viagem na Lupa — todo preço tem fonte e data."><meta name="twitter:image" content="https://viagemnalupa.com.br/assets/img/og-image.png">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../../../assets/img/favicon-32.png" sizes="32x32"><link rel="icon" href="../../../assets/img/favicon-512.png" sizes="512x512"><link rel="apple-touch-icon" href="../../../assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../../../assets/css/site.css?v=0">
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="bar"><div class="wrap bar-in">
<a class="marca" href="../../../"><svg width="30" height="30" viewBox="0 0 100 100" fill="none" aria-hidden="true"><circle cx="46" cy="46" r="33" fill="var(--card, #18304A)"></circle><circle cx="46" cy="46" r="33" stroke="var(--ciano, #43D3C2)" stroke-width="3.5"></circle><ellipse cx="46" cy="46" rx="33" ry="12.5" stroke="var(--ciano, #43D3C2)" stroke-width="2.5"></ellipse><ellipse cx="46" cy="46" rx="13" ry="33" stroke="var(--ciano, #43D3C2)" stroke-width="2.5"></ellipse><path d="M60.5 58.5 L78 76" stroke="var(--ambar, #FFB703)" stroke-width="8" stroke-linecap="round"></path><circle cx="46" cy="44" r="20" fill="var(--noite, #122334)"></circle><circle cx="46" cy="44" r="20" stroke="var(--ambar, #FFB703)" stroke-width="7"></circle></svg><span>VIAGEM NA LUPA</span></a>
<nav><a href="../../../destinos/" aria-current="page">Destinos</a><a href="../../../calculadora/">Calculadora</a><a href="../../../sobre/">Sobre</a><a class="externo" href="https://www.youtube.com/@viagemnalupa" target="_blank" rel="noopener">YouTube<span class="so-leitor"> (abre em outra aba)</span><svg class="seta-ext" width="11" height="11" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 17 L17 7 M9 7h8v8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"></path></svg></a></nav>
</div></header>
<main id="conteudo">
<div class="faixa"><div class="wrap wrap-estreito">
<p class="migalhas"><a href="../../../">Início</a> › <a href="../../">Destinos</a> › <a href="../">{nome}</a> › Roteiro de {dias} dias</p>
<div class="hero">
  <span class="eyebrow">Roteiro dia a dia</span>
  <h1>{titulo}</h1>
  <p>{abertura}</p>
</div>
</div></div>

<div class="wrap wrap-estreito">
"""

RODAPE = """</div>
</main>
<footer class="rodape"><div class="wrap cols">
<p><b>Tarifas verificadas em {apuracao}.</b> Cada página traz a data da própria apuração. Atrações com preço dinâmico podem variar conforme a data escolhida — reconfira no checkout.</p>
<p>Quando um dado não existe em fonte confiável, a lacuna fica escrita. Não preenchemos com estimativa.</p>
<p>© 2026 Viagem na Lupa · viagemnalupa.com.br · <a href="../../../privacidade/">Privacidade</a></p>
</div></footer>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a2b63bb9c39147728b617fa302c981dc"}}'></script><!-- End Cloudflare Web Analytics -->

</body>
</html>
"""


def monta(slug):
    r = ROTEIROS[slug]
    d = next(x for x in DESTINOS if x["slug"] == slug)
    html = CABECA.format(titulo=r["titulo"], descricao=r["descricao"], site=SITE,
                         slug=slug, dias=r["dias"], nome=d["nome"],
                         abertura=r["abertura"])

    avisos = "".join('<div class="aviso%s"><span class="t">%s</span>%s</div>'
                     % ((" " + cls) if cls else "", t, corpo)
                     for cls, t, corpo in r["avisos"])
    html += '<section class="bloco">%s</section>\n' % avisos

    dias = []
    for i, (tit, texto, paradas) in enumerate(r["dias_lista"], 1):
        p = "".join('<span class="parada">%s</span>' % x for x in paradas)
        dias.append('<div class="dia"><span class="dia-n">Dia %d</span>'
                    '<div class="dia-b"><h3>%s</h3><p>%s</p>'
                    '<div class="paradas">%s</div></div></div>' % (i, tit, texto, p))
    html += ('<section class="bloco"><div class="dias">%s</div>\n'
             '<div class="paginas">\n'
             '  <a class="pg" href="../">Guia dos pontos, com preço e horário</a>\n'
             '</div></section>\n' % "".join(dias))

    html += ('<section class="bloco"><p style="color:var(--nevoa);font-size:.86rem">%s</p>'
             '</section>\n' % r["fontes"])
    html += RODAPE.format(apuracao=APURACAO)
    return html


def main(aplica):
    for slug, r in ROTEIROS.items():
        pasta = os.path.join(RAIZ, "destinos", slug, "roteiro-%d-dias" % r["dias"])
        html = monta(slug)
        lac = len(re.findall(r'<span class="flag">', html))
        print("  %-12s roteiro de %d dias, %d ressalvas, %d KB%s"
              % (slug, r["dias"], lac, len(html.encode("utf-8")) / 1024,
                 "" if aplica else "   (ensaio)"))
        if aplica:
            os.makedirs(pasta, exist_ok=True)
            with open(os.path.join(pasta, "index.html"), "w",
                      encoding="utf-8", newline="") as f:
                f.write(html)
    if not aplica:
        print()
        print("Nada escrito. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
