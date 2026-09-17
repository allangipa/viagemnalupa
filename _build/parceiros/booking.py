# -*- coding: utf-8 -*-
"""Poe o link de afiliado da Booking no espaco que ja existe nas fichas.

O que estava errado
-------------------
As dez fichas de custo traziam:

    <a class="parceiro" href="https://www.booking.com/" rel="noopener">

Dois defeitos nessa linha:

1. Sem identificador de afiliado. A pagina promete "Estes dois links dao
   comissao ao site" e o /sobre/ repete a promessa, mas o link ia para a
   home da Booking sem atribuicao nenhuma - clique que nao valia nada.

2. Sem rel="sponsored". O link da Aviasales ao lado tem. O Google pede a
   marcacao em link de afiliado, e a falta e violacao de politica, nao
   detalhe de estilo.

O que entra
-----------
O deep link da CJ Affiliate, que foi por onde a afiliacao saiu aprovada
(jdoqocy.com e ftjcfx.com sao dominios de rastreio da Commission
Junction). Verificado ponta a ponta antes de escrever: o clique atravessa
CJ -> dotomi -> emjcd e chega em

    booking.com/searchresults.pt-br.html?ss=Montevideu
      &aid=8133103
      &label=affnetcj-17323525_pub-..._clkid-vnl-montevideu_cjevent-...

ou seja: a busca da cidade preservada, a comissao atribuida, e o sid
chegando inteiro do outro lado. E o sid que responde "qual destino paga",
que sem isso nunca se saberia com dez fichas iguais.

Nao usei o widget que a Booking oferece. Medido no navegador, ele monta o
iframe com style="height:100%" dentro de uma div sem altura - 100% de
automatico da zero. A 1200px de largura a caixa fica 900 x 0 px: o leitor
nao ve nada, e o pixel de impressao conta uma impressao assim mesmo.

Sem data e sem numero de hospedes no link
-----------------------------------------
De proposito. As fichas nao sabem quando o leitor viaja, e a ocupacao
varia dentro da propria pagina - em Lisboa ha cama de dormitorio (por
pessoa) e ADR (por quarto) na mesma calculadora. Chutar 2 adultos seria
inventar premissa. A Booking aplica o padrao dela.

A lista de buscas e escrita a mao, com trava
--------------------------------------------
Nao da para deduzir o pais da pasta, e "Santiago" sozinho acha Santiago
de Compostela. Entao a lista existe - mas se aparecer ficha de custos em
disco que nao esteja nela, o script para e diz qual. Foi assim que as
listas de schema, sitemap e voos pararam de falhar caladas.

Uso
---
    python _build/parceiros/booking.py
    python _build/parceiros/booking.py --aplica
"""
import io
import os
import re
import sys
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# CJ Affiliate. Nao e segredo: o identificador viaja na URL que o
# navegador do leitor segue. O que nunca pode entrar no repositorio e
# token de API - esse continua so no secret do GitHub.
CJ = "https://www.jdoqocy.com/click-101884045-17323525"

BUSCA = {
    "buenos-aires":   "Buenos Aires, Argentina",
    "cancun":         "Cancún, México",
    "fortaleza":      "Fortaleza, Brasil",
    "lisboa":         "Lisboa, Portugal",
    "maceio":         "Maceió, Brasil",
    "montevideu":     "Montevidéu, Uruguai",
    "nova-york":      "Nova York, Estados Unidos",
    "orlando":        "Orlando, Estados Unidos",
    "rio-de-janeiro": "Rio de Janeiro, Brasil",
    "santiago":       "Santiago, Chile",
}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def fichas_de_custo():
    base = os.path.join(RAIZ, "destinos")
    saida = []
    for slug in sorted(os.listdir(base)):
        p = os.path.join(base, slug, "quanto-custa", "index.html")
        if os.path.isfile(p):
            saida.append((slug, p))
    return saida


def confere_lista(achadas):
    """A trava. Ficha nova sem busca na lista para o script."""
    faltam = [s for s, _ in achadas if s not in BUSCA]
    if faltam:
        raise SystemExit(
            "Ficha de custos em disco sem busca da Booking na lista: %s\n"
            "Acrescente em BUSCA, em _build/parceiros/booking.py, no formato\n"
            '"cidade, pais" - so o nome da cidade e ambiguo na Booking.'
            % ", ".join(faltam))
    sobra = [s for s in BUSCA if s not in {x for x, _ in achadas}]
    if sobra:
        print("   (aviso: %s esta na lista e nao tem ficha de custos)"
              % ", ".join(sobra))


def link_de(slug):
    alvo = ("https://www.booking.com/searchresults.pt-br.html?ss=%s"
            % urllib.parse.quote(BUSCA[slug], safe=""))
    return "%s?url=%s&sid=vnl-%s" % (
        CJ, urllib.parse.quote(alvo, safe=""), slug)


# A ancora da Booking, seja a home crua ou um link da CJ ja posto antes.
ANCORA = re.compile(
    r'(<a class="parceiro" href=")([^"]*(?:booking\.com|jdoqocy\.com)[^"]*)'
    r'("\s+target="_blank"\s+rel=")([^"]*)(")')


def main(aplica):
    achadas = fichas_de_custo()
    confere_lista(achadas)
    print("=== link da Booking nas fichas de custo ===")
    n = 0
    for slug, p in achadas:
        h = le(p)
        novo_href = link_de(slug)
        conta = [0]

        def troca(m):
            href_velho, rel_velho = m.group(2), m.group(4)
            rel_novo = rel_velho
            if "sponsored" not in rel_novo.split():
                rel_novo = (rel_novo + " sponsored").strip()
            if href_velho == novo_href and rel_novo == rel_velho:
                return m.group(0)
            conta[0] += 1
            return m.group(1) + novo_href + m.group(3) + rel_novo + m.group(5)

        saida = ANCORA.sub(troca, h)
        if conta[0] > 1:
            raise SystemExit("%s: achei %d ancoras da Booking, esperava 1"
                             % (slug, conta[0]))
        if not conta[0]:
            print("   %-16s ja esta como deve" % slug)
            continue
        n += 1
        print("   %-16s busca %-28s sid vnl-%s"
              % (slug, BUSCA[slug], slug))
        if aplica:
            escreve(p, saida)

    print()
    print("%s: %d ficha(s)." % ("Escrito" if aplica else "Faria", n))
    if not aplica and n:
        print("Nada foi alterado. Rode com --aplica para escrever.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
