# -*- coding: utf-8 -*-
"""Faz cada roteiro responder tambem a "roteiro CIDADE 3 dias", "4 dias"...

Item 5 do _build/docs/concorrentes-2026-10-17.md. O Viagens e Caminhos
responde "roteiro Lisboa 2, 3, 4, 5 dias" numa URL so; o nosso roteiro
tem um tamanho travado na URL (roteiro-6-dias/), e a busca "roteiro
Lisboa 3 dias" nao nos encontra.

O CAMINHO BARATO, escolhido pelo Allan em 17/10/2026: nao mexer na URL,
que ja esta indexada e linkada. Mexer em dois lugares:

  1. <title> e og:title ganham os cortes:
       Roteiro de 6 dias em Lisboa, dia a dia (2026)
       Roteiro de 6 dias em Lisboa (ou 3, 4 e 5), dia a dia — 2026
     O <h1> fica como esta: o TouristTrip do JSON-LD foi gerado dele.

  2. Um bloco "Com menos dias" abre o conteudo, logo depois do hero, com
     um H2 que carrega os numeros - "Roteiro de Lisboa em 3, 4 ou 5 dias"
     - e a lista dos dias do proprio roteiro, na ordem.

NADA E INVENTADO POR CIDADE. Qual dia cortar e decisao editorial que o
dados.py nao tem, e este site nao escreve o que nao apurou. O bloco diz a
unica coisa que e verdade nos 20: cada dia fecha um bairro, uma regiao ou
um bate-volta, entao corta-se dia inteiro - e confira o dia da semana
antes de pular um, porque varios pontos fecham num dia fixo.

Os cortes: roteiro de 3 dias oferece "2"; de 5, "3 e 4"; de 6, "3, 4 e
5"; de 7, "3, 4, 5 e 6". Nunca 1 dia: nao e roteiro, e lista.

E POS-PROCESSADOR, como assinatura.py e faq.py: os roteiros vem de tres
familias (novos/gera_roteiro.py, os lib.py do Rio e de Lisboa, Nova York
a mao). Idempotente: o titulo e reconhecido nas duas formas e refeito; o
bloco e trocado se existe, posto se nao.

Uso
---
    python _build/layout/tamanhos.py            # so mostra
    python _build/layout/tamanhos.py --aplica   # escreve
"""
import glob
import html as H
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# As duas formas do <title>: a original e a ja aplicada.
TITULO = re.compile(
    r"(Roteiro de (\d+) dias (?:em|no|na) [^(,<]+?)(?: \(ou [^)]*\))?, dia a dia (?:\((\d{4})\)|— (\d{4}))")
JA = re.compile(r'(?s)\n?<section class="bloco cortes" id="menos-dias">.*?</section>\n?')
PREP = {"em": "de", "no": "do", "na": "da"}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def limpa(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t or "")).strip()


def cortes_de(n):
    if n <= 2:
        return []
    return [2] if n == 3 else list(range(3, n))


def lista(nums, conj):
    s = [str(x) for x in nums]
    return s[0] if len(s) == 1 else ", ".join(s[:-1]) + " %s " % conj + s[-1]


def monta(h, n):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    m = re.match(r"Roteiro de \d+ dias (em|no|na) (.+)", limpa(h1.group(1)) if h1 else "")
    if not m:
        return None, "H1 fora do padrao"
    prep, cidade = PREP[m.group(1)], m.group(2)
    dias = [limpa(x) for x in re.findall(r'<div class="dia-b"[^>]*>.*?<h2[^>]*>(.*?)</h2>', h, re.S)]
    if len(dias) != n:
        return None, "a URL diz %d dias e a pagina tem %d" % (n, len(dias))
    c = cortes_de(n)
    if not c:
        return None, "sem corte possivel"
    li = "".join("\n    <li>%s</li>" % H.escape(d, quote=False) for d in dias)
    sec = ('<section class="bloco cortes" id="menos-dias">\n'
           '  <div class="bloco-head"><span class="eyebrow">Com menos dias</span>'
           '<h2>Roteiro %s %s em %s dias</h2>\n'
           '  <p>Este roteiro tem %d dias, e cada um fecha um bairro, uma região ou um bate-volta. '
           'Com menos tempo, <b>corte dias inteiros, não pedaços</b> — e confira o dia da semana '
           'antes de pular um: vários pontos fecham num dia fixo, e a ficha de cada um diz qual. '
           'Os %d dias, na ordem:</p></div>\n'
           '  <ol class="plain">%s\n  </ol>\n</section>\n'
           % (prep, H.escape(cidade, quote=False), lista(c, "ou"), n, n, li))
    return sec, "cortes %s" % lista(c, "e")


def titulo_novo(h, n):
    c = cortes_de(n)
    def troca(m):
        ano = m.group(3) or m.group(4)
        return "%s (ou %s), dia a dia — %s" % (m.group(1), lista(c, "e"), ano)
    h2, k = TITULO.subn(troca, h)
    return h2, k


def main(aplica):
    posto = trocado = pulado = 0
    for p in sorted(glob.glob(os.path.join(RAIZ, "destinos", "*", "roteiro-*", "index.html"))):
        slug = p.replace(os.sep, "/").split("/")[-3]
        n = int(re.search(r"roteiro-(\d+)-dias", p).group(1))
        h = le(p)
        sec, nota = monta(h, n)
        if not sec:
            print("   PULADO %-16s %s" % (slug, nota)); pulado += 1; continue
        h2, k = titulo_novo(h, n)          # <title> e og:title: k deve ser 2
        if JA.search(h2):
            h2 = JA.sub("\n" + sec, h2, count=1); modo = "trocado"
        else:
            i = h2.find("</h1>")
            j = h2.find('<div class="wrap wrap-estreito">', i)
            if j < 0 or j - i > 4000:
                print("   PULADO %-16s sem o wrap depois do hero" % slug); pulado += 1; continue
            j = h2.find("\n", j) + 1
            h2 = h2[:j] + sec + h2[j:]; modo = "posto"
        if h2 != h:
            if modo == "posto": posto += 1
            else: trocado += 1
            if aplica:
                escreve(p, h2)
        print("   %-16s %d dias  %-16s titulos trocados: %d  %s" % (slug, n, nota, k, modo if h2 != h else "igual"))
    print("   %d posto(s), %d trocado(s), %d pulado(s)   %s"
          % (posto, trocado, pulado, "escrito" if aplica else "SO MOSTRANDO"))


if __name__ == "__main__":
    main("--aplica" in sys.argv)
