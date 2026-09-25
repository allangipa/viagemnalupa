# -*- coding: utf-8 -*-
"""Poe os atalhos de afiliado no indice lateral, abaixo da lista de pontos.

O pedido
--------
"Gostaria de colocar os atalhos dos sites afiliados como botoes embaixo do
menu dos pontos turisticos. Facilitando o acesso do visitante caso resolva
pesquisar voos e hospedagens enquanto navega no site."

Os parceiros ja existiam na pagina, mas num bloco solto la embaixo, depois
das fichas. Quem esta lendo o ponto 03 de 16 nao passa por ele. O indice
lateral e pegajoso e acompanha a leitura - e o lugar certo.

De onde vem cada link
---------------------
COPIADO do bloco que o espalha.py ja pos na propria pagina. Nao se inventa
link de afiliado: o da Aviasales so funciona com data, e as datas que
existem sao as da apuracao publicada na ficha de custos.

O sub-id muda
-------------
    vnl-cancun-guia    o bloco de baixo, que ja existia
    vnl-cancun-aside   estes botoes

E o motivo e o mesmo que criou os outros sub-ids: sem separar, o painel diz
que "o guia de Cancun converte" e nao diz se foi o bloco do rodape ou o
atalho da lateral - que e justamente a pergunta que este trabalho levanta.

A trava
-------
Bariloche e Punta Cana nao tem ficha de custos e, por isso, nao tem link de
voo coletado. Nessas duas entra so a Booking, e o script diz quais foram.
Gerar link de voo sem data daria "Oops, the search failed to launch" - medido
pelo espalha.py.

Uso
---
    python _build/parceiros/aside.py
    python _build/parceiros/aside.py --aplica
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEST = os.path.join(RAIZ, "destinos")
APLICA = "--aplica" in sys.argv

MARCA_INI = "<!-- parceiros:aside -->"
MARCA_FIM = "<!-- /parceiros:aside -->"

SETA = ('<svg width="12" height="12" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        '<path d="M7 17 L17 7 M9 7h8v8" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"></path></svg>')


# O nome da cidade e escrito a mao, com trava - mesma solucao do booking.py.
#
# Nao da para deduzir: o <title> e o <h1> variam de pagina para pagina.
# Deduzindo deles sairiam botoes dizendo "Voos para Buenos Aires em 5 dias",
# "Voos para Nova York em novembro" e "Voos para Lisboa: 16 pontos
# turisticos". Se aparecer destino em disco que nao esteja aqui, o script
# para e diz qual.
CIDADES = {
    "bariloche":      "Bariloche",
    "buenos-aires":   "Buenos Aires",
    "cancun":         "Cancún",
    "fortaleza":      "Fortaleza",
    "lisboa":         "Lisboa",
    "maceio":         "Maceió",
    "montevideu":     "Montevidéu",
    "nova-york":      "Nova York",
    "orlando":        "Orlando",
    "porto":          "Porto",
    "sevilha":        "Sevilha",
    "punta-cana":     "Punta Cana",
    "rio-de-janeiro": "Rio de Janeiro",
    "santiago":       "Santiago",
}


def extrai(h):
    """Devolve (href_voo, href_hotel) do bloco que o espalha.py escreveu."""
    bloco = re.search(r'<div class="reserva-lista">(.*?)</div>\s*</div>', h, re.S)
    if not bloco:
        return None, None
    voo = hotel = None
    for href in re.findall(r'<a class="parceiro"[^>]*href="([^"]+)"', bloco.group(1)):
        if "aviasales" in href:
            voo = href
        elif "click-" in href or "booking.com" in href:
            hotel = href
    return voo, hotel


def troca_subid(href, de, para):
    return href.replace(de, para)


def botao(href, rotulo, nota):
    return ('<a class="parceiro" href="%s" target="_blank" rel="noopener sponsored">'
            '<span class="p-nome">%s%s</span>'
            '<span class="p-nota">%s</span></a>' % (href, rotulo, SETA, nota))


def monta(cidade, voo, hotel):
    bs = []
    if voo:
        bs.append(botao(voo, "Voos para %s" % cidade, "Aviasales"))
    bs.append(botao(hotel, "Hospedagem em %s" % cidade, "Booking.com"))
    return (MARCA_INI +
            '<div class="idx-parceiros">'
            '<div class="idx-tit">Pesquisar agora</div>' +
            "".join(bs) +
            '<p class="idx-nota-afiliado">Links de afiliado. Você paga o mesmo preço, '
            'e a comissão <b>não altera nenhum número do site</b>. '
            '<a href="../../sobre/">Como funciona</a>.</p>'
            '</div>' + MARCA_FIM)


mudados, so_hotel, pulados = [], [], []
for slug in sorted(os.listdir(DEST)):
    pag = os.path.join(DEST, slug, "index.html")
    if not os.path.isdir(os.path.join(DEST, slug)) or not os.path.exists(pag):
        continue
    h = io.open(pag, encoding="utf-8").read()

    voo, hotel = extrai(h)
    if not hotel:
        pulados.append((slug, "sem link de hospedagem no bloco de baixo"))
        continue
    if slug not in CIDADES:
        sys.exit("PARADO: destino em disco que nao esta na lista CIDADES: %s.\n"
                 "Acrescente o nome como ele deve aparecer no botao." % slug)
    cidade = CIDADES[slug]

    de, para = "vnl-%s-guia" % slug, "vnl-%s-aside" % slug
    voo = troca_subid(voo, de, para) if voo else None
    hotel = troca_subid(hotel, de, para)
    if para not in hotel:
        pulados.append((slug, "o sub-id nao trocou: esperava %s no link" % de))
        continue
    if not voo:
        so_hotel.append(slug)

    novo = monta(cidade, voo, hotel)

    # remove uma versao anterior, para o script poder rodar duas vezes
    h = re.sub(re.escape(MARCA_INI) + ".*?" + re.escape(MARCA_FIM), "", h, flags=re.S)

    # entra depois da lista de pontos, antes dos atalhos de grupo
    if '<div class="idx-atalho">' in h:
        h2 = h.replace('<div class="idx-atalho">', novo + '<div class="idx-atalho">', 1)
    elif "</section></aside>" in h:
        h2 = h.replace("</section></aside>", novo + "</section></aside>", 1)
    else:
        pulados.append((slug, "nao achei onde encaixar no aside"))
        continue

    if h2 == h:
        pulados.append((slug, "nada mudou"))
        continue
    mudados.append((slug, cidade, 2 if voo else 1))
    if APLICA:
        # Sem newline="" o Python do Windows troca o fim de linha na
        # escrita, e as 13 fichas aparecem modificadas no git com zero
        # mudanca de conteudo. Os outros geradores da casa ja passam
        # este argumento; este nao passava, e foi defeito meu.
        io.open(pag, "w", encoding="utf-8", newline="").write(h2)

print("%-16s %-22s %s" % ("destino", "cidade no botao", "botoes"))
for slug, cidade, n in mudados:
    print("%-16s %-22s %d" % (slug, cidade, n))
print("\n%d paginas%s" % (len(mudados), "" if APLICA else " (nada escrito; use --aplica)"))
if so_hotel:
    print("\nSO HOSPEDAGEM, por nao terem ficha de custos com voo apurado:")
    for s in so_hotel:
        print("   ", s)
if pulados:
    print("\nPULADOS:")
    for s, m in pulados:
        print("   %-16s %s" % (s, m))
