# -*- coding: utf-8 -*-
"""Poe o preco apurado de cada ponto no dado estruturado, como Offer.

O QUE ESTE SCRIPT CORRIGE NA MINHA PROPRIA LEITURA
--------------------------------------------------
A auditoria anterior disse "TouristAttraction AUSENTE". Estava errada: ela
so olhava o @type do topo de cada bloco, e os pontos moram ANINHADOS,
dentro do itemListElement do ItemList. Os 14 destinos ja marcam cada ponto
como TouristAttraction, com nome, url e imagem, desde o gera.py.

O que falta nao e o tipo. E o PRECO - que e justamente o trabalho do site.
Sao 154 pontos apurados com valor, fonte e data, e o buscador nao le
nenhum deles.

POR QUE ISTO NAO CONTRARIA A RECUSA DO gera.py
-----------------------------------------------
O gera.py se recusa a escrever estimatedCost, e a razao esta escrita la:
o total da pagina de custo e somado pelo ficha.js conforme a hospedagem
que o leitor escolhe, entao cravar um numero criaria um preco que
envelhece em silencio.

Isto aqui e outra coisa. Nao e o total da viagem, e a entrada de UM ponto,
que tem valor unico, fonte nomeada e data de consulta. E, sobretudo:

    O PRECO E LIDO DO HTML PUBLICADO, NAO DE UMA TABELA A PARTE.

Sai do mesmo <span class="preco-val"> que o leitor ve na tela. Os dois nao
podem divergir, porque sao o mesmo texto. Se a apuracao mudar e a pagina
for regerada, rodar isto de novo realinha - e enquanto nao rodar, o que
esta no JSON-LD continua sendo exatamente o que esta escrito na pagina.

O QUE FICA DE FORA, DE PROPOSITO
--------------------------------
So entra valor UNICO e sem ambiguidade. Fica sem offers, e sem nenhum
palpite no lugar:

    "US$ 25 a US$ 40"        faixa - nao ha um numero verdadeiro
    "A partir de R$ 30"      piso, nao preco
    "US$ 12 ou US$ 18"       depende de condicao nao modelada aqui
    "Fontes divergem"        o site diz que nao sabe; o dado tambem diz
    "Sem tarifa publicada"   idem
    "Contribuicao"           valor livre
    "Fechado"                nao ha o que comprar
    "—"                      lacuna declarada

"Gratis" ENTRA, com price 0. Gratuidade e informacao, nao lacuna - e e a
resposta de 58 dos 154 pontos.

HORARIO NAO ENTRA, E NAO E ESQUECIMENTO
----------------------------------------
openingHoursSpecification pede dia da semana e hora de abrir e fechar. O
que o site guarda e prosa, em rotulos que variam - "Dias e horarios",
"Horario", "Dias em que nao funciona" - e muitas vezes so o dia de folga,
sem hora nenhuma. Converter isso em horario estruturado seria inventar a
parte que falta. Quando a apuracao passar a guardar hora de abrir e
fechar por dia, este script ganha um bloco; hoje, nao.

Uso
---
    python _build/schema/ofertas.py            # so mostra
    python _build/schema/ofertas.py --aplica   # escreve
"""
import collections
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://viagemnalupa.com.br"

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Simbolo como o site escreve -> codigo ISO 4217. Os mais longos primeiro,
# senao "US$" casaria como "$" e "MX$" viraria dolar.
MOEDAS = [
    ("US$", "USD"),
    ("MX$", "MXN"),
    ("R$", "BRL"),
    ("$U", "UYU"),
    ("ARS", "ARS"),
    ("CLP", "CLP"),
    ("€", "EUR"),
]

# Texto que, sozinho, quer dizer "de graca".
GRATIS = {"grátis", "gratis", "gratuito", "entrada gratuita"}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def serializa(obj):
    return json.dumps(obj, ensure_ascii=False,
                      separators=(",", ":")).replace("</", "<\\/")


def numero(s):
    """'15,50' -> '15.50'   '1.200' -> '1200'   devolve None se nao der."""
    s = s.strip()
    if not re.fullmatch(r"\d{1,3}(\.\d{3})*(,\d{1,2})?|\d+(,\d{1,2})?|\d+\.\d{1,2}", s):
        return None
    if "," in s:                      # formato daqui: ponto e milhar
        s = s.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(\.\d{3})+", s):
        s = s.replace(".", "")
    v = float(s)
    return ("%.2f" % v).rstrip("0").rstrip(".") if "." in ("%.2f" % v) else str(int(v))


def oferta(bruto, moeda_local="BRL"):
    """Devolve (Offer, motivo) - Offer None quando nao da para afirmar.

    A moeda do ponto GRATIS nao pode ser chutada. "Gratis" nao traz
    simbolo nenhum, e a primeira versao disto marcava BRL em tudo - o que
    poria um preco em real no Mosteiro dos Jeronimos. A moeda vem da
    propria ficha, apurada dos pontos dela que TEM simbolo.
    """
    t = re.sub(r"\s+", " ", bruto).strip()
    if not t:
        return None, "vazio"
    if t.lower() in GRATIS:
        return {"@type": "Offer", "price": "0", "priceCurrency": moeda_local,
                "availability": "https://schema.org/InStock"}, "gratis " + moeda_local
    # qualquer marca de faixa, piso ou duvida derruba o valor
    baixo = t.lower()
    for marca, motivo in ((" a ", "faixa"), ("–", "faixa"), (" ou ", "alternativa"),
                          ("a partir de", "piso"), ("divergem", "divergencia"),
                          ("sem tarifa", "sem tarifa"), ("fechado", "fechado"),
                          ("contribui", "contribuicao"), ("—", "lacuna")):
        if marca in baixo:
            return None, motivo
    for simbolo, iso in MOEDAS:
        if t.startswith(simbolo):
            n = numero(t[len(simbolo):])
            if n is None:
                return None, "numero ilegivel"
            return {"@type": "Offer", "price": n, "priceCurrency": iso,
                    "availability": "https://schema.org/InStock"}, iso
    return None, "sem moeda reconhecida"


def precos_da_ficha(htm, slug):
    """{url do ponto: texto cru do preco} lendo os mesmos article.ponto."""
    cortes = [(m.group(1), m.start()) for m in re.finditer(
        r'<article class="ponto"[^>]*\bid="([^"]+)"', htm)]
    fora = {}
    for i, (aid, ini) in enumerate(cortes):
        fim = cortes[i + 1][1] if i + 1 < len(cortes) else len(htm)
        m = re.search(r'<span class="preco-val">(.*?)</span>', htm[ini:fim], re.S)
        if m:
            txt = re.sub(r"<[^>]+>", "", m.group(1))
            fora["%s/destinos/%s/#%s" % (SITE, slug, aid)] = txt
    return fora


def main(aplica):
    destinos = sorted(d for d in os.listdir(os.path.join(RAIZ, "destinos"))
                      if os.path.isdir(os.path.join(RAIZ, "destinos", d)))
    postas = 0
    recusadas = {}
    sem_preco = 0
    tocadas = 0

    for slug in destinos:
        arq = os.path.join(RAIZ, "destinos", slug, "index.html")
        if not os.path.isfile(arq):
            continue
        htm = antes = le(arq)
        precos = precos_da_ficha(htm, slug)

        m = re.search(r'<script type="application/ld\+json">\s*(\{[^<]*?'
                      r'"@type"\s*:\s*"ItemList".*?\})\s*</script>', htm, re.S)
        if not m:
            print("  %-16s sem ItemList - pulei" % slug)
            continue
        try:
            lista = json.loads(m.group(1))
        except Exception:
            print("  %-16s ItemList ilegivel - pulei" % slug)
            continue

        # a moeda da ficha, apurada dos pontos que trazem simbolo
        vistas = collections.Counter()
        for bruto in precos.values():
            limpo = re.sub(r"\s+", " ", bruto).strip()
            for simbolo, iso in MOEDAS:
                if limpo.startswith(simbolo):
                    vistas[iso] += 1
                    break
        moeda = vistas.most_common(1)[0][0] if vistas else None
        if moeda is None:
            print("  %-16s nenhum ponto com simbolo de moeda - pulei" % slug)
            continue

        aqui = 0
        for li in lista.get("itemListElement", []):
            item = li.get("item")
            if not isinstance(item, dict):
                continue
            if "offers" in item:            # nunca reescreve o que ja esta la
                continue
            bruto = precos.get(item.get("url"))
            if bruto is None:
                sem_preco += 1
                continue
            of, motivo = oferta(bruto, moeda)
            if of is None:
                recusadas.setdefault(motivo, []).append(
                    "%s: %s" % (slug, re.sub(r"\s+", " ", bruto).strip()[:46]))
                continue
            item["offers"] = of
            aqui += 1

        if aqui:
            htm = htm[:m.start(1)] + serializa(lista) + htm[m.end(1):]
            postas += aqui
            tocadas += 1
            print("  %-16s %2d oferta(s) em %d ponto(s)"
                  % (slug, aqui, len(lista.get("itemListElement", []))))
            if aplica and htm != antes:
                escreve(arq, htm)

    print()
    print("ofertas escritas: %d   fichas tocadas: %d" % (postas, tocadas))
    print("pontos sem <span class=preco-val>: %d" % sem_preco)
    if recusadas:
        print("\n=== deixados SEM preco, de proposito ===")
        for motivo in sorted(recusadas):
            print("  %-14s %d" % (motivo, len(recusadas[motivo])))
            for x in recusadas[motivo]:
                print("      " + x)
    if not aplica:
        print("\nNada foi alterado. Rode com --aplica.")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplica" in sys.argv))
