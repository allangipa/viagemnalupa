# -*- coding: utf-8 -*-
"""Poe o bloco de parceiros tambem na ficha de destino e no roteiro.

O pedido
--------
"Nao sao em todas as paginas que aparecem as opcoes de booking e do
afiliado em passagem aerea."

Medido: os parceiros estavam so nas 10 fichas de custo. As 10 fichas de
destino e os 10 roteiros - as paginas onde a pessoa esta justamente
planejando a viagem - nao tinham nenhum.

De onde vem cada link
---------------------
Booking: montado aqui, com a busca da propria cidade. Nao precisa de
data, entao e so trocar o sid.

Aviasales: COPIADO da ficha de custos do mesmo destino. Nao inventei
link.

Por que copiar em vez de montar: testei as formas de URL da Aviasales e a
de rota sem data NAO funciona - /search/SAOLIS1 abre a pagina, reconhece
"Sao Paulo - Lisbon", e mostra "Oops, the search failed to launch". Sem
data ela nao busca. A forma com data (/search/SAO2602LIS15031) funciona e
abre a busca com a faixa de datas para o leitor mexer.

As datas que existem no site sao as da apuracao, ja publicadas na ficha
de custos ("a passagem mais barata do cache partia em 26 de fevereiro de
2027"). Usar outra data seria inventar premissa; usar essa e reaproveitar
dado apurado.

O sub-id muda por pagina
------------------------
    vnl-lisboa          ficha de custos  (ja existia)
    vnl-lisboa-guia     ficha de destino
    vnl-lisboa-roteiro  roteiro

Assim o painel diz nao so qual destino, mas qual PAGINA converte - que e
o que decide onde vale investir texto.

A trava
-------
Se um destino tiver ficha de custos sem link de voo coletado, o script
avisa e poe so a Booking naquela pagina, em vez de gerar link quebrado.

Uso
---
    python _build/parceiros/espalha.py
    python _build/parceiros/espalha.py --aplica
"""
import io
import os
import re
import sys
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

MARCA = "<!-- parceiros:espalhados -->"
VIZINHOS = "<!-- vizinhos -->"

SETA = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" '
        'aria-hidden="true"><path d="M7 17 L17 7 M9 7h8v8" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        'stroke-linejoin="round"></path></svg>')


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def destinos():
    base = os.path.join(RAIZ, "destinos")
    for slug in sorted(os.listdir(base)):
        d = os.path.join(base, slug)
        if not os.path.isfile(os.path.join(d, "index.html")):
            continue
        rot = None
        for sub in sorted(os.listdir(d)):
            if re.fullmatch(r"roteiro-\d+-dias", sub) and \
                    os.path.isfile(os.path.join(d, sub, "index.html")):
                rot = sub
        yield slug, rot


def links_da_ficha_de_custos(slug):
    """Pega da ficha de custos os hrefs ja verificados e no ar."""
    p = os.path.join(RAIZ, "destinos", slug, "quanto-custa", "index.html")
    if not os.path.isfile(p):
        return None, None
    h = le(p)
    voo = re.search(r'<a class="parceiro" href="([^"]*aviasales[^"]*)"', h)
    book = re.search(r'<a class="parceiro" href="([^"]*jdoqocy[^"]*)"', h)
    return (voo.group(1) if voo else None), (book.group(1) if book else None)


def troca_subid(url, de, para):
    """marker=775563.vnl-lisboa -> marker=775563.vnl-lisboa-guia"""
    return re.sub(r"(marker=\d+\.)%s(?=&|$)" % re.escape(de),
                  r"\g<1>" + para, url)


def troca_sid(url, para):
    return re.sub(r"(&sid=)[^&]*", r"\g<1>" + urllib.parse.quote(para), url)


def bloco(voo, book, para_custos, para_sobre):
    itens = []
    if voo:
        itens.append(
            '<a class="parceiro" href="%s" target="_blank" '
            'rel="noopener sponsored"><span class="p-nome">Aviasales%s</span>'
            '<span class="p-nota">passagens aéreas</span></a>' % (voo, SETA))
    if book:
        itens.append(
            '<a class="parceiro" href="%s" target="_blank" '
            'rel="noopener sponsored"><span class="p-nome">Booking.com%s</span>'
            '<span class="p-nota">hotéis e alojamento local</span></a>'
            % (book, SETA))
    return (
        '%s\n<section class="bloco">\n'
        '<div class="reserva">\n'
        '<div class="reserva-topo">\n'
        '<h3>Passagem e hospedagem</h3>\n'
        '<p>São os dois maiores gastos da viagem e nenhum dos dois entra '
        'nos preços desta página — cada um depende das suas datas. '
        '<a href="%s">A ficha de custos</a> traz a passagem '
        'mais barata que encontramos, com a data da apuração.</p>\n'
        '<p style="color:var(--nevoa);font-size:.9rem"><b>Estes links dão '
        'comissão ao site.</b> Você paga o mesmo preço que pagaria indo '
        'direto, e a comissão <b>não altera nenhum número do site</b>. '
        '<a href="%s">Como isso funciona</a>.</p>\n'
        '</div>\n'
        '<div class="reserva-lista">%s</div>\n'
        '</div>\n'
        '</section>\n%s' % (MARCA, para_custos, para_sobre,
                            "".join(itens), MARCA))


# De cada tipo de pagina: caminho ate a ficha de custos do mesmo destino,
# e caminho ate /sobre/. A ficha mora em destinos/<slug>/ e o roteiro um
# nivel abaixo, em destinos/<slug>/<roteiro>/.
CAMINHOS = {
    "guia":    ("quanto-custa/", "../../sobre/"),
    "roteiro": ("../quanto-custa/", "../../../sobre/"),
}


def poe(caminho, voo, book, tipo):
    h = le(caminho)
    if not (voo or book):
        return h, False, "sem link"
    para_custos, para_sobre = CAMINHOS[tipo]

    # Conferir os caminhos relativos ANTES de gravar.
    #
    # Entrou porque errei: troquei o significado do parametro e nao o
    # texto do template, e sairam "quanto-custa/quanto-custa/" e
    # "../../sobre/sobre/" em vinte paginas. Link quebrado nao levanta
    # excecao nenhuma - so o leitor descobre, clicando.
    base = os.path.dirname(caminho)
    for rel in (para_custos, para_sobre):
        alvo = os.path.normpath(os.path.join(base, rel.replace("/", os.sep),
                                             "index.html"))
        if not os.path.isfile(alvo):
            raise SystemExit(
                "%s: o link %r nao leva a lugar nenhum (esperava %s)"
                % (os.path.relpath(caminho, RAIZ), rel,
                   os.path.relpath(alvo, RAIZ)))

    b = bloco(voo, book, para_custos, para_sobre)

    # Se ja existe, SUBSTITUIR - nao pular.
    #
    # O coletor de voos reescreve a ficha de custos todo dia as 18h30
    # UTC. Se aqui fosse "ja tem, pula", a copia da ficha de destino e do
    # roteiro apontaria para uma busca velha para sempre. E exatamente o
    # erro do atalhos.py, que conferia existencia em vez de conteudo e
    # deixou Cancun meses sem o link de quanto custa.
    ini = h.find(MARCA)
    if ini >= 0:
        fim = h.find(MARCA, ini + len(MARCA))
        if fim < 0:
            raise SystemExit("%s: marcador de abertura sem o de fechamento"
                             % os.path.relpath(caminho, RAIZ))
        fim += len(MARCA)
        if h[ini:fim] == b:
            return h, False, "ja atual"
        return h[:ini] + b + h[fim:], True, "atualizado"

    i = h.find(VIZINHOS)
    if i < 0:
        m = re.search(r"\n</div>\n</main>", h)
        if not m:
            return h, False, "sem onde por"
        i = m.start()
    return h[:i] + b + "\n" + h[i:], True, "novo"


def main(aplica):
    print("%-16s %-10s %-22s %s" % ("destino", "pagina", "voo", "booking"))
    n = falhas = 0
    for slug, rot in destinos():
        voo0, book0 = links_da_ficha_de_custos(slug)
        if not book0:
            print("   %-16s SEM ficha de custos com Booking - pulado" % slug)
            falhas += 1
            continue
        if not voo0:
            print("   %-16s ficha de custos sem link de voo coletado - "
                  "vai so com Booking" % slug)
            falhas += 1

        alvos = [("index.html", "guia")]
        if rot:
            alvos.append((os.path.join(rot, "index.html"), "roteiro"))

        for rel, tipo in alvos:
            p = os.path.join(RAIZ, "destinos", slug, rel)
            voo = troca_subid(voo0, "vnl-" + slug, "vnl-%s-%s" % (slug, tipo)) \
                if voo0 else None
            # Aviasales e Booking sao URLs absolutas: nao mudam entre a
            # ficha e o roteiro. So o sub-id muda, para o painel separar
            # de qual pagina veio o clique.
            book = troca_sid(book0, "vnl-%s-%s" % (slug, tipo))
            h, fez, porque = poe(p, voo, book, tipo)
            if not fez:
                if porque != "ja atual":
                    print("%-16s %-10s %s" % (slug, tipo, porque))
                continue
            n += 1
            print("%-16s %-10s %-11s %-24s %s"
                  % (slug, tipo, porque,
                     ("marker .%s" % voo.split("marker=")[-1][:22])
                     if voo else "(sem voo)",
                     "sid .%s" % book.split("sid=")[-1][:22]))
            if aplica:
                escreve(p, h)

    print()
    print("%s: %d pagina(s). %d aviso(s)."
          % ("Escrito" if aplica else "Faria", n, falhas))
    if not aplica and n:
        print("Nada foi alterado. Rode com --aplica para escrever.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
