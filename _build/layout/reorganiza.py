# -*- coding: utf-8 -*-
"""Reorganiza a ficha de um destino para caber em menos rolagem.

A medida que motivou
--------------------
Lisboa, no celular (375x812), media 111,9 telas. O leitor batia no
primeiro ponto turistico so na tela 10,7 e o indice - o atalho para
pular - estava na tela 9,3, depois do trecho que se quer pular.

Onde estava o peso, medido e nao suposto:
  bloco dos 8 avisos ......  8,1 telas
  64 campos de fundo .....  36,5 telas  <- um terco da pagina
  o resto ................  67,3 telas

Tres mudancas, nenhuma apaga uma linha de conteudo:

1. O indice sobe para antes dos avisos e ganha atalho para os grupos.
   No desktop alto, acompanha a rolagem.

2. Os avisos viram <details>. O titulo de cada um ja afirma a conclusao
   ("A taxa turistica nao esta no preco da sua reserva"), entao vira
   resumo sem reescrita. O PRIMEIRO fica aberto: e o que diz o que
   mudou na cidade, e quem chega sem saber planeja errado.

3. Os campos de cada ponto se separam em dois grupos e mudam de ordem.
   "Dias em que nao funciona" era o nono campo, abaixo de Curiosidades
   e Fatos historicos - o dado que estraga a viagem enterrado sob
   trivia. Passa a ser o segundo, logo depois do preco.

Sobre esconder atras de clique: <details> e HTML nativo. Nao depende de
JavaScript, o conteudo continua no DOM e indexado, e o Ctrl+F do
navegador abre o bloco fechado sozinho.

Uso
---
    python _build/layout/reorganiza.py lisboa
    python _build/layout/reorganiza.py lisboa --aplica
    python _build/layout/reorganiza.py --todos --aplica
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Campos que respondem "posso ir, quando, quanto custa". Ficam abertos,
# nesta ordem: preco e fecho primeiro, porque sao os que decidem a visita.
ABERTOS = [
    "Valor da entrada",
    "Dias em que não funciona",
    "Endereço",
    "Onde fica",
    "Dias e horários",
    "Metrô mais próximo",
    "Pontos de referência",
    "Pontos turísticos próximos",
    "Estacionamento",
    "Quando é barato e quando é caro",
]
# Leitura de fundo. Continua na pagina, atras de um clique.
FUNDO = [
    "Visitantes por ano",
    "Menor visitação e temperatura",
    "Curiosidades",
    "Fatos históricos",
]
RESUMO_FUNDO = "Curiosidades, história e visitação"


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def so_texto(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def fatia(txt, marca):
    pos = [m.start() for m in re.finditer(re.escape(marca), txt)]
    return [txt[a:b] for a, b in zip(pos, pos[1:] + [len(txt)])]


# --------------------------------------------------------------- avisos
def avisos_em_details(html):
    """Cada <div class="aviso"> vira <details>; o primeiro nasce aberto."""
    if '<details class="aviso' in html:
        return html, 0                      # ja passou por aqui
    n = [0]

    def um(m):
        classe, corpo = m.group(1), m.group(2)
        t = re.search(r'<span class="t">(.*?)</span>', corpo, re.S)
        if not t:
            return m.group(0)
        n[0] += 1
        resto = corpo.replace(t.group(0), "", 1)
        aberto = " open" if n[0] == 1 else ""
        return ('<details class="%s"%s><summary class="t">%s</summary>%s</details>'
                % (classe, aberto, t.group(1), resto))

    saida = re.sub(
        r'<div class="(aviso(?:\s+[ab])?)">(.*?)</div>(?=<div class="aviso|</section>)',
        um, html, flags=re.S)
    return saida, n[0]


# ------------------------------------------------------- campos do ponto
def reorganiza_campos(html):
    if '<details class="fundo">' in html:
        return html, 0                      # ja passou por aqui
    n = [0]

    def um_bloco(m):
        campos = fatia(m.group(1), '<div class="campo-l">')
        if len(campos) < 3:
            return m.group(0)
        ordem, por_rotulo = [], {}
        for c in campos:
            r = re.search(r'<div class="rot">(.*?)</div>', c, re.S)
            if not r:
                return m.group(0)           # formato inesperado: nao mexe
            rot = so_texto(r.group(1))
            por_rotulo[rot] = c
            ordem.append(rot)

        fundo = [por_rotulo[k] for k in FUNDO if k in por_rotulo]
        if not fundo:
            return m.group(0)               # nada a colapsar aqui

        abertos = [por_rotulo[k] for k in ABERTOS if k in por_rotulo]
        conhecidos = set(ABERTOS) | set(FUNDO)
        # campo que este destino tem e os outros nao: mantem onde estava,
        # depois dos conhecidos, em vez de sumir
        sobra = [por_rotulo[k] for k in ordem if k not in conhecidos]

        n[0] += 1
        resumo = ('<details class="fundo"><summary>%s '
                  '<span class="conta">%d campos</span></summary>%s</details>'
                  % (RESUMO_FUNDO, len(fundo), "".join(fundo)))
        return ('<div class="campos">%s%s%s</div>'
                % ("".join(abertos), "".join(sobra), resumo))

    saida = re.sub(r'<div class="campos">(.*?)</div>\s*</article>',
                   lambda m: um_bloco(m) + "</article>", html, flags=re.S)
    return saida, n[0]


# ---------------------------------------------------------- indice sobe
def sobe_indice(html):
    m_idx = re.search(
        r'<section class="bloco">\s*<div class="bloco-head">'
        r'<span class="eyebrow">[^<]*</span><h2>Índice</h2>.*?</section>',
        html, re.S)
    m_av = re.search(r'<section class="bloco"><div class="aviso', html)
    if not m_idx or not m_av:
        return html, False
    if m_idx.start() < m_av.start():
        return html, False                  # ja esta em cima

    indice = m_idx.group(0)
    grupos = re.findall(r'<div class="idx-tit">([^<]+)</div>', indice)
    if grupos:
        atalhos = "".join('<a href="#g%d">%s</a>' % (i, g)
                          for i, g in enumerate(grupos, 1))
        indice = indice.replace("</section>",
                                '<div class="idx-atalho">%s</div></section>' % atalhos, 1)
    indice = indice.replace('<section class="bloco">',
                            '<section class="bloco idx-fixo">', 1)

    sem = html[:m_idx.start()] + html[m_idx.end():]
    corte = re.search(r'<section class="bloco"><div class="aviso', sem).start()
    return sem[:corte] + indice + sem[corte:], True


def ancora_grupos(html):
    if re.search(r'<section class="grupo" id="g\d+">', html):
        return html, 0
    i = [0]

    def marca(m):
        i[0] += 1
        return '<section class="grupo" id="g%d">' % i[0]

    return re.sub(r'<section class="grupo">', marca, html), i[0]


# ------------------------------------------------------------------ roda
def uma_ficha(slug, aplica):
    p = os.path.join(RAIZ, "destinos", slug, "index.html")
    if not os.path.isfile(p):
        print("  %-16s sem index.html" % slug)
        return False
    h0 = le(p)
    h, subiu = sobe_indice(h0)
    h, n_av = avisos_em_details(h)
    h, n_pt = reorganiza_campos(h)
    h, n_gr = ancora_grupos(h)

    if h == h0:
        print("  %-16s nada a fazer (ja reorganizada)" % slug)
        return False
    print("  %-16s indice%s  avisos:%d  pontos:%d  grupos:%d"
          % (slug, " sobe" if subiu else " ja", n_av, n_pt, n_gr))
    if aplica:
        escreve(p, h)
    return True


def main(argv):
    aplica = "--aplica" in argv
    alvos = [a for a in argv[1:] if not a.startswith("--")]
    if "--todos" in argv:
        base = os.path.join(RAIZ, "destinos")
        alvos = sorted(d for d in os.listdir(base)
                       if os.path.isdir(os.path.join(base, d)))
    if not alvos:
        print(__doc__)
        return 2

    print("=== %s ===" % ("aplicando" if aplica else "ensaio"))
    n = sum(1 for s in alvos if uma_ficha(s, aplica))
    print()
    print("%s: %d ficha(s)." % ("Escrito" if aplica else "Faria", n))
    if not aplica and n:
        print("Nada foi alterado. Rode com --aplica para escrever.")
        print("Depois: python _build/cachebust/atualiza.py --aplica")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
