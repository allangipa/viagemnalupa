# -*- coding: utf-8 -*-
"""Escreve a ficha de um destino novo no padrao da casa.

Le _build/novos/dados.py, que traz a apuracao com fonte em cada numero, e
produz destinos/<slug>/index.html no mesmo molde de Montevideu e Orlando.

Nao inventa nada: o que a apuracao nao tem, nao aparece. As lacunas ja
vem escritas nos proprios dados, com <span class="flag">.

Depois de rodar este script, rode na ordem:
    python _build/layout/reorganiza.py --todos --aplica
    python _build/layout/atalhos.py --aplica
    python _build/schema/gera.py --aplica
    python _build/sitemap/atualiza.py --aplica
    python _build/cachebust/atualiza.py --aplica
    python _build/confere/tudo.py
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

# De qual pasta vem a apuracao.
#
# Este gerador nasceu para Cancun e Fortaleza, lendo _build/novos/dados.py.
# Bariloche e Punta Cana vieram depois, em _build/novos2/dados.py. Copiar
# o gerador inteiro para a pasta nova seria duplicar mil e quinhentas
# linhas que teriam de ser corrigidas em dois lugares para sempre.
#
#     VNL_DADOS=novos2 python _build/novos/gera.py --aplica
#
# Sem a variavel, le a pasta de sempre e nada muda para quem ja usava.
_PASTA = os.environ.get("VNL_DADOS", "").strip()
_ORIGEM = os.path.join(os.path.dirname(AQUI), _PASTA) if _PASTA else AQUI
if not os.path.isfile(os.path.join(_ORIGEM, "dados.py")):
    raise SystemExit("nao achei dados.py em %s" % _ORIGEM)
sys.path.insert(0, _ORIGEM)

from dados import DESTINOS, APURACAO  # noqa: E402

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
<link rel="canonical" href="{site}/destinos/{slug}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Viagem na Lupa">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:url" content="{site}/destinos/{slug}/">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='112 102 583 583'%3E%3Ccircle cx='352' cy='342' r='196' stroke='%23FFB703' stroke-width='58' fill='none'/%3E%3Cpath d='M491 481 L648 638' stroke='%23FFB703' stroke-width='64' stroke-linecap='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../../assets/css/site.css?v=0">
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="bar"><div class="wrap bar-in">
<a class="marca" href="../../"><svg width="30" height="30" viewBox="112 102 583 583" fill="none" aria-hidden="true">
  <circle cx="352" cy="342" r="196" stroke="#FFB703" stroke-width="58"></circle>
  <path d="M491 481 L648 638" stroke="#FFB703" stroke-width="64" stroke-linecap="round"></path>
  <path d="M282 396 L336 320 L392 372 L446 268" stroke="#2EC4B6" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"></path>
</svg><span>VIAGEM NA LUPA</span></a>
<nav><a href="../../destinos/" aria-current="page">Destinos</a><a href="../../calculadora/">Calculadora</a><a href="../../sobre/">Sobre</a><a class="externo" href="https://www.youtube.com/@viagemnalupa" target="_blank" rel="noopener">YouTube<span class="so-leitor"> (abre em outra aba)</span><svg class="seta-ext" width="11" height="11" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 17 L17 7 M9 7h8v8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"></path></svg></a></nav>
</div></header>
<main id="conteudo">
<div class="faixa"><div class="wrap">
<p class="migalhas"><a href="../../">Início</a> › <a href="../">Destinos</a> › {nome}</p>
<div class="hero">
  <span class="eyebrow">Guia</span>
  <h1>{nome}</h1>
  <p>{abertura}</p>
</div>
</div></div>

<div class="wrap">
"""

RODAPE = """</div>
</main>
<footer class="rodape"><div class="wrap cols">
<p><b>Tarifas verificadas em {apuracao}.</b> Cada página traz a data da própria apuração. Atrações com preço dinâmico podem variar conforme a data escolhida — reconfira no checkout.</p>
<p>Quando um dado não existe em fonte confiável, a lacuna fica escrita. Não preenchemos com estimativa.</p>
<p>© 2026 Viagem na Lupa · viagemnalupa.com.br · <a href="../../privacidade/">Privacidade</a></p>
</div></footer>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a2b63bb9c39147728b617fa302c981dc"}}'></script><!-- End Cloudflare Web Analytics -->

</body>
</html>
"""


def aviso_apurado(d, n_pontos, n_lacunas):
    """O bloco que diz o que esta apurado e o que falta. Vem primeiro, e o
    numero de lacunas e contado do proprio HTML, nao digitado."""
    return (
        '<section class="bloco"><div class="aviso a"><span class="t">O que já está '
        'apurado e o que ainda falta</span>'
        '<p>Os %s pontos abaixo têm <b>preço, horário e endereço verificados</b> em '
        'fonte oficial ou na página do próprio ponto, com a data da consulta ao lado '
        'de cada número.</p>'
        '<p><b>O que ainda não está aqui:</b> <b>visitação anual</b>, <b>distâncias a '
        'pé</b> e <b>fotografia de cada ponto</b>. Esta página nasce sem foto e as '
        'imagens entram à medida que encontrarmos material com licença que permita uso '
        'comercial — é o mesmo caminho que Montevidéu percorreu.</p>'
        '<p><b>E há %d ressalvas escritas ponto a ponto</b>, marcadas em vermelho ao '
        'longo da página: onde a fonte não existe, onde duas fontes divergem e onde o '
        'preço muda conforme a data. <b>Preferimos %s pontos certos a doze meio '
        'certos</b>, e é por isso que esta página cresce por camada em vez de nascer '
        'inteira.</p></div></section>\n'
        % (extenso(n_pontos), n_lacunas, extenso(n_pontos)))


def extenso(n):
    return {1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis",
            7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze",
            12: "doze"}.get(n, str(n))


def indice(d):
    """O indice, no formato que o resto do site usa."""
    n = 0
    colunas = []
    for g in d["grupos"]:
        itens = []
        for p in d["pontos"]:
            if p["grupo"] != g["id"]:
                continue
            n += 1
            itens.append(
                '<a class="idx-item" href="#%s"><span class="idx-num">%02d</span>'
                '<span class="idx-nome">%s</span><span class="idx-preco">%s</span></a>'
                % (p["id"], n, p["nome"], p["preco_val"]))
        if itens:
            colunas.append('<div><div class="idx-tit">%s</div>%s</div>'
                           % (g["titulo"], "".join(itens)))
    return ('<section class="bloco">\n'
            '  <div class="bloco-head"><span class="eyebrow">Os %d pontos</span>'
            '<h2>Índice</h2></div>\n'
            '  <div class="idx-cols">%s</div>\n</section>\n'
            % (n, "".join(colunas)))


def um_ponto(p, numero):
    campos = "".join(
        '<div class="campo-l"><div class="rot">%s</div><div class="val">%s</div></div>'
        % (rot, val) for rot, val in p["campos"])
    return (
        '<article class="ponto" id="%s">\n'
        '  <div class="ponto-topo">\n'
        '    <div class="ponto-id"><span class="num">%02d</span>\n'
        '      <div><h3>%s</h3><span class="tag">%s</span></div></div>\n'
        '    <div class="preco"><span class="preco-val">%s</span>\n'
        '      <span class="preco-nota">%s</span></div>\n'
        '  </div>\n'
        '  <div class="campos">%s</div>\n'
        '</article>\n'
        % (p["id"], numero, p["nome"], p["tag"], p["preco_val"], p["preco_nota"], campos))


def grupos(d):
    saida = []
    n = 0
    for g in d["grupos"]:
        pts = [p for p in d["pontos"] if p["grupo"] == g["id"]]
        if not pts:
            continue
        saida.append('<section class="grupo"><div class="grupo-head"><h2>%s</h2>'
                     '<p>%s</p></div>\n' % (g["titulo"], g["intro"]))
        for p in pts:
            n += 1
            saida.append(um_ponto(p, n))
        saida.append('</section>\n')
    return "".join(saida)


def fontes(d):
    return (
        '<section class="bloco"><div class="aviso"><span class="t">Onde conferimos os '
        'preços de %s</span>'
        '<p>Cada valor desta página traz, no próprio campo, a fonte e a data em que foi '
        'consultado. <b>Nenhum número aqui vem de agregador de viagem ou de guia de '
        'terceiro sem que isso esteja dito.</b></p>'
        '<p><b>Onde duas fontes divergiram, as duas ficaram na página.</b> Não '
        'escolhemos a mais conveniente nem tiramos média — quando o número não fecha, '
        'quem decide com a informação completa é você.</p>'
        '<p><b>Preço em moeda estrangeira não foi convertido para real nesta camada.</b> '
        'A conversão automática pela PTAX do Banco Central já existe em outras fichas do '
        'site e entra aqui quando a ficha de custos for publicada.</p>'
        '</div></section>\n' % d["nome"])


def paginas_irmas(d):
    return ('<section class="bloco"><div class="paginas">\n'
            '</div></section>\n')


def monta(d):
    html = CABECA.format(titulo=d["titulo"], descricao=d["descricao"], site=SITE,
                         slug=d["slug"], nome=d["nome"], abertura=d["abertura"])
    corpo = indice(d) + grupos(d)
    n_lacunas = len(re.findall(r'<span class="flag">', corpo))
    html += aviso_apurado(d, len([p for p in d["pontos"]]), n_lacunas)
    html += corpo
    html += fontes(d)
    html += RODAPE.format(apuracao=APURACAO)
    return html


def main(aplica):
    for d in DESTINOS:
        pasta = os.path.join(RAIZ, "destinos", d["slug"])
        alvo = os.path.join(pasta, "index.html")
        html = monta(d)
        lacunas = len(re.findall(r'<span class="flag">', html))
        print("  %-12s %d pontos, %d grupos, %d ressalvas, %d KB%s"
              % (d["slug"], len(d["pontos"]), len(d["grupos"]), lacunas,
                 len(html.encode("utf-8")) / 1024,
                 "" if aplica else "   (ensaio)"))
        if aplica:
            os.makedirs(pasta, exist_ok=True)
            with open(alvo, "w", encoding="utf-8", newline="") as f:
                f.write(html)
    if not aplica:
        print()
        print("Nada escrito. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
