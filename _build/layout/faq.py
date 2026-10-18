# -*- coding: utf-8 -*-
"""Perguntas frequentes no fim de cada guia, derivadas do que a pagina ja diz.

Item 3 do _build/docs/concorrentes-2026-10-17.md: o Dica de Portugal fecha
guia, ficha e roteiro com quatro perguntas em H3, e e isso que entra no
"As pessoas tambem perguntam". Nos tinhamos zero perguntas como titulo.

NENHUMA RESPOSTA E ESCRITA A MAO. As quatro saem de dados que TODOS os 20
guias ja tem, lidos do HTML publicado - o mesmo caminho do ofertas.py, que
le o preco do <span class="preco-val"> e nao de uma lista paralela:

  1. Quais pontos nao cobram entrada?   preco-val com "gratis"/"gratuito"/"livre"
  2. Qual e o ponto mais caro?          o maior preco-val com moeda, CITADO
                                        COMO ESTA - faixa fica faixa, "a
                                        partir de" fica "a partir de"; nunca
                                        vira numero. Hospedagem fica de fora:
                                        e conta, nao lugar.
  3. Quanto custa N dias, por pessoa?   "Total por pessoa" e "dias" da ficha
                                        de custos irma, com link para ela
  4. De quando sao os precos?           dateModified do WebPage (JSON-LD),
                                        que o schema/editor.py tira do commit

Onde foi testado antes de escrever (17/10/2026): os cartoes do topo e o
rodape "Precos verificados em" so existem em 3 dos 20 guias - os de lib.py
(Lisboa, Rio) e Santiago. Um FAQ ancorado neles cobriria 3 cidades. Por
isso a fonte e o que e igual nos 20: o <article class="ponto"> e a ficha.

Entra logo ANTES do bloco "Os guias das outras cidades", que os 20 tem.
Idempotente: troca o bloco se ja existe, poe se nao existe.

O FAQPage do JSON-LD e emitido pelo schema/gera.py, lendo ESTA secao -
pergunta no <h3>, resposta no <p> -, para a marcacao nunca discordar do
que esta na tela.

Uso
---
    python _build/layout/faq.py            # so mostra
    python _build/layout/faq.py --aplica   # escreve
"""
import glob
import html as H
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

MOEDA = r"(?:US\$|R\$|€|MX\$|CLP|ARS|UYU|\$U|\$)"
GRATIS = re.compile(r"gr[aá]tis|gratuit|livre", re.I)
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def limpa(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t or "")).strip()


def numero(t):
    """So para ORDENAR. O texto publicado e sempre o preco-val como esta."""
    m = re.search(r"[\d][\d.,]*", t)
    if not m:
        return None
    v = m.group(0)
    if "," in v:
        v = v.replace(".", "").replace(",", ".")
    elif re.search(r"\.\d{3}(?!\d)", v):
        v = v.replace(".", "")
    try:
        return float(v)
    except ValueError:
        return None


def pontos(h):
    out = []
    for m in re.finditer(r'(?s)<article class="ponto" id="([^"]+)"(.*?)</article>', h):
        pid, corpo = m.group(1), m.group(2)
        nome = re.search(r"<h3[^>]*>(.*?)</h3>", corpo, re.S)
        val = re.search(r'class="preco-val"[^>]*>(.*?)</span>', corpo, re.S)
        nota = re.search(r'class="preco-nota"[^>]*>(.*?)</span>', corpo, re.S)
        tag = re.search(r'class="tag"[^>]*>(.*?)</span>', corpo, re.S)
        if not (nome and val):
            continue
        out.append(dict(id=pid, nome=limpa(nome.group(1)), val=limpa(val.group(1)),
                        nota=limpa(nota.group(1)) if nota else "",
                        tag=limpa(tag.group(1)) if tag else ""))
    return out


def lista_pt(nomes):
    if len(nomes) <= 1:
        return "".join(nomes)
    return ", ".join(nomes[:-1]) + " e " + nomes[-1]


def data_extenso(iso):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", iso or "")
    if not m:
        return None
    return "%d de %s de %s" % (int(m.group(3)), MESES[int(m.group(2)) - 1], m.group(1))


def ficha(slug):
    p = os.path.join(RAIZ, "destinos", slug, "quanto-custa", "index.html")
    if not os.path.isfile(p):
        return None
    q = le(p)
    dias = re.search(r'"dias"\s*:\s*(\d+)', q)
    i = q.find("Total por pessoa")
    if i < 0 or not dias:
        return None
    t = limpa(q[i:i + 400])
    v = re.search(r"((?:%s)\s?[\d][\d.,]*)" % MOEDA, t)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", q, re.S)
    h1 = limpa(h1.group(1)) if h1 else ""
    if not v:
        return None
    return dict(dias=int(dias.group(1)), total=v.group(1), h1=h1)


def monta(slug, h):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    cidade = limpa(h1.group(1)).split(":")[0].strip() if h1 else slug
    pts = pontos(h)
    if not pts:
        return None, "sem pontos"
    qs = []

    # 1. gratis
    gr = [p for p in pts if GRATIS.search(p["val"]) and "hospedagem" not in p["id"]]
    if gr:
        qs.append(("Quais pontos de %s não cobram entrada?" % cidade,
                   "%d dos %d pontos deste guia: %s. O que cada um tem de "
                   "gratuito — e o que cobra à parte — está na ficha de cada ponto."
                   % (len(gr), len(pts), lista_pt([p["nome"] for p in gr]))))
    else:
        qs.append(("Algum ponto de %s não cobra entrada?" % cidade,
                   "Nenhum dos %d pontos deste guia tem entrada gratuita. Os preços de cada "
                   "um estão na ficha de cada ponto, com a fonte e a data." % len(pts)))

    # 2. mais caro - citado como esta; hospedagem (conta, nao lugar) fora
    pagos = [(numero(p["val"]), p) for p in pts
             if re.search(MOEDA, p["val"]) and "hospedagem" not in p["id"]
             and "conta" not in p["tag"].lower()]
    pagos = [(n, p) for n, p in pagos if n is not None]
    if pagos:
        n, p = max(pagos, key=lambda x: x[0])
        faixa = bool(re.search(r"\ba\b|partir|–|-", p["val"]))
        r = "%s, com entrada %s %s" % (p["nome"], "na faixa de" if faixa else "a", p["val"])
        if p["nota"]:
            r += " — %s" % p["nota"]
        r += ". É o maior valor publicado entre os pontos deste guia."
        qs.append(("Qual é o ponto mais caro de %s?" % cidade, r))

    # 3. quanto custa N dias
    f = ficha(slug)
    if f:
        perg = f["h1"] if re.match(r"Quanto custa \d+ dias", f["h1"]) \
            else "Quanto custa %d dias em %s" % (f["dias"], cidade)
        qs.append((perg + ", por pessoa?",
                   "%s, pela <a href=\"quanto-custa/\">ficha de custos de %d dias</a> — "
                   "com hospedagem, ingressos e transporte, sem passagem aérea. A "
                   "calculadora da ficha refaz a conta com as suas datas."
                   % (f["total"], f["dias"])))

    # 4. de quando sao os precos
    dm = re.search(r'"dateModified"\s*:\s*"([^"]+)"', h)
    ext = data_extenso(dm.group(1)) if dm else None
    if ext:
        qs.append(("De quando são os preços deste guia?",
                   "Cada número traz, ao lado, a data em que foi consultado na fonte. "
                   "Esta página foi atualizada pela última vez em %s. Quando um dado "
                   "não existe em fonte confiável, a lacuna fica escrita." % ext))

    itens = "".join(
        '\n  <details class="faq-q"><summary><h3>%s</h3></summary><p>%s</p></details>'
        % (H.escape(q, quote=False), r) for q, r in qs)
    sec = ('<section class="bloco faq" id="perguntas">\n'
           '  <div class="bloco-head"><span class="eyebrow">Perguntas frequentes</span>'
           '<h2>O que mais se pergunta sobre %s</h2></div>%s\n</section>\n'
           % (H.escape(cidade, quote=False), itens))
    return sec, "%d pergunta(s)" % len(qs)


JA = re.compile(r'(?s)<section class="bloco faq" id="perguntas">.*?</section>\n?')


def main(aplica):
    posto = trocado = pulado = 0
    for p in sorted(glob.glob(os.path.join(RAIZ, "destinos", "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(p))
        h = le(p)
        sec, nota = monta(slug, h)
        if not sec:
            print("   PULADO %-16s %s" % (slug, nota)); pulado += 1; continue
        if JA.search(h):
            h2 = JA.sub(sec, h, count=1)
            if h2 != h:
                trocado += 1
                if aplica:
                    escreve(p, h2)
            print("   %-16s %s  (trocado)" % (slug, nota))
            continue
        # ancora: o bloco "Os guias das outras cidades", que os 20 tem
        i = h.find("Os guias das outras cidades")
        j = h.rfind('<section class="bloco"', 0, i) if i > 0 else -1
        if j < 0:
            print("   PULADO %-16s sem o bloco das outras cidades" % slug); pulado += 1; continue
        h = h[:j] + sec + h[j:]
        posto += 1
        if aplica:
            escreve(p, h)
        print("   %-16s %s" % (slug, nota))
    print("   %d posto(s), %d trocado(s), %d pulado(s)   %s"
          % (posto, trocado, pulado, "escrito" if aplica else "SO MOSTRANDO"))


if __name__ == "__main__":
    main("--aplica" in sys.argv)
