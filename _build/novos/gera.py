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
<meta property="og:url" content="{site}/destinos/{slug}/"><meta property="og:image" content="https://viagemnalupa.com.br/assets/img/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Viagem na Lupa — todo preço tem fonte e data."><meta name="twitter:image" content="https://viagemnalupa.com.br/assets/img/og-image.png">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../../assets/img/favicon-32.png" sizes="32x32"><link rel="icon" href="../../assets/img/favicon-512.png" sizes="512x512"><link rel="apple-touch-icon" href="../../assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../../assets/css/site.css?v=0">
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="bar"><div class="wrap bar-in">
<a class="marca" href="../../"><svg width="30" height="30" viewBox="0 0 100 100" fill="none" aria-hidden="true"><circle cx="46" cy="46" r="33" fill="var(--card, #18304A)"></circle><circle cx="46" cy="46" r="33" stroke="var(--ciano, #43D3C2)" stroke-width="3.5"></circle><ellipse cx="46" cy="46" rx="33" ry="12.5" stroke="var(--ciano, #43D3C2)" stroke-width="2.5"></ellipse><ellipse cx="46" cy="46" rx="13" ry="33" stroke="var(--ciano, #43D3C2)" stroke-width="2.5"></ellipse><path d="M60.5 58.5 L78 76" stroke="var(--ambar, #FFB703)" stroke-width="8" stroke-linecap="round"></path><circle cx="46" cy="44" r="20" fill="var(--noite, #122334)"></circle><circle cx="46" cy="44" r="20" stroke="var(--ambar, #FFB703)" stroke-width="7"></circle></svg><span>VIAGEM NA LUPA</span></a>
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


def aviso_apurado(d, n_pontos, n_lacunas, n_fotos=0):
    """O bloco que diz o que esta apurado e o que falta. Vem primeiro, e o
    numero de lacunas e contado do proprio HTML, nao digitado."""
    return (
        '<section class="bloco"><div class="aviso a"><span class="t">O que já está '
        'apurado e o que ainda falta</span>'
        '<p>Os %s pontos abaixo têm <b>preço, horário e endereço verificados</b> em '
        'fonte oficial ou na página do próprio ponto, com a data da consulta ao lado '
        'de cada número.</p>'
        '<p><b>O que ainda não está aqui:</b> %s</p>'
        '<p><b>E há %d ressalvas escritas ponto a ponto</b>, marcadas em vermelho ao '
        'longo da página: onde a fonte não existe, onde duas fontes divergem e onde o '
        'preço muda conforme a data. <b>%s</b>, e é por isso que esta página cresce por camada em vez de nascer '
        'inteira.</p></div></section>\n'
        % (extenso(n_pontos), falta_fotos(n_pontos, n_fotos), n_lacunas,
           comparacao(n_pontos)))


def falta_fotos(n_pontos, n_fotos):
    """O paragrafo do que ainda falta, contando as fotos em vez de afirmar.

    O texto era fixo e dizia "esta pagina nasce sem foto". Com o tempo tres
    fichas passaram a ter foto e continuaram dizendo que nao tinham -
    Bariloche com duas de nove, Punta Cana com duas de sete, e o Porto com
    DEZESSEIS de dezesseis, o que e o caso em que a frase fica absurda.

    Afirmacao que o proprio arquivo pode conferir nao se escreve a mao.
    """
    if n_fotos >= n_pontos > 0:
        return ("<b>visitação anual</b> e <b>distâncias a pé</b>. "
                "<b>A fotografia de cada ponto já está</b>, toda com licença que "
                "permite uso comercial e com o crédito ao lado da imagem.")
    if n_fotos:
        return ("<b>visitação anual</b>, <b>distâncias a pé</b> e a "
                "<b>fotografia de %s dos %s pontos</b>. As imagens entram à medida "
                "que encontrarmos material com licença que permita uso comercial."
                % (extenso(n_pontos - n_fotos), extenso(n_pontos)))
    return ("<b>visitação anual</b>, <b>distâncias a pé</b> e <b>fotografia de cada "
            "ponto</b>. Esta página nasce sem foto e as imagens entram à medida que "
            "encontrarmos material com licença que permita uso comercial — é o mesmo "
            "caminho que Montevidéu percorreu.")


def extenso(n):
    return {1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis",
            7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze",
            12: "doze", 13: "treze", 14: "quatorze", 15: "quinze",
            16: "dezesseis", 17: "dezessete", 18: "dezoito",
            19: "dezenove", 20: "vinte"}.get(n, str(n))


def comparacao(n):
    """A frase de "melhor pouco e certo do que muito e meio certo".

    Ate doze pontos ela compara com doze, que e o numero que estava
    escrito aqui desde Cancun. Acima de doze, comparar com doze inverte o
    sentido: "preferimos dezesseis certos a doze meio certos" nao quer
    dizer nada. Ai a frase perde o numero e ganha em clareza.

    A condicao existe para que as fichas ja publicadas saiam iguais
    quando forem regeradas.
    """
    if n <= 12:
        return "Preferimos %s pontos certos a doze meio certos" % extenso(n)
    return "Preferimos ponto certo a ponto meio certo"


def preco(p):
    """O valor que aparece no cartao do ponto e no indice.

    preco_val = None quer dizer "a fonte oficial nao publica preco", e a
    preco_nota ao lado diz qual e a fonte que nao publica. Sem este
    travessao o %s do template escreveria a palavra None na pagina - foi
    o que o Porto trouxe, com quatro pontos nessa situacao: Sao Francisco,
    as caves de Gaia, a Capela das Almas e o Mercado do Bolhao.
    """
    return p["preco_val"] or "—"


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
                % (p["id"], n, p["nome"], preco(p)))
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

    # A foto, quando o ponto tem uma.
    #
    # Fica aqui, no gerador, e nao inserida no HTML depois: a ficha e
    # regerada a cada mudanca na apuracao, e foto colada direto no
    # arquivo sumiria na proxima geracao sem aviso.
    #
    # Ponto sem foto sai sem <figure> - "melhor ficar sem imagem do que
    # quadro sem imagem", que foi o pedido do Allan e virou regra.
    foto = ""
    if p.get("foto"):
        f = p["foto"]
        foto = ('  <figure class="foto">'
                '<img src="../../assets/img/%s" alt="%s" width="1200" '
                'height="675" loading="lazy" decoding="async">'
                '<figcaption><p class="foto-cred">%s</p></figcaption>'
                '</figure>\n' % (f["arq"], f["alt"], f["cred"]))

    return (
        '<article class="ponto" id="%s">\n'
        '  <div class="ponto-topo">\n'
        '    <div class="ponto-id"><span class="num">%02d</span>\n'
        '      <div><h3>%s</h3><span class="tag">%s</span></div></div>\n'
        '    <div class="preco"><span class="preco-val">%s</span>\n'
        '      <span class="preco-nota">%s</span></div>\n'
        '  </div>\n'
        '%s'
        '  <div class="campos">%s</div>\n'
        '</article>\n'
        % (p["id"], numero, p["nome"], p["tag"], preco(p),
           p["preco_nota"], foto, campos))


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
    html += aviso_apurado(d, len(d["pontos"]), n_lacunas,
                          sum(1 for p in d["pontos"] if p.get("foto")))
    # Aviso de moeda, quando o destino tem um.
    #
    # Nasceu porque eu escrevi a explicacao do peso argentino DENTRO do
    # paragrafo de abertura. Deu 944 caracteres, contra 110 a 222 dos
    # outros onze destinos, e o hero foi a 685px de altura - o Allan
    # reparou que a barra estava grande demais na vertical.
    #
    # A abertura e o gancho, em uma frase. Nota de metodo tem bloco
    # proprio, que e o padrao que o resto do site ja usa.
    if d.get("aviso_moeda"):
        html += ('<section class="bloco"><div class="aviso b">'
                 '<span class="t">%s</span>%s</div></section>\n'
                 % (d["aviso_moeda"]["titulo"], d["aviso_moeda"]["corpo"]))
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
