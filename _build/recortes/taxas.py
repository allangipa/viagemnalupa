# -*- coding: utf-8 -*-
"""Gera /taxas/: as taxas de turismo de todos os destinos, numa pagina so.

Pedido de 19/11/2026. O Search Console mostrou que o site aparece mas nao e
clicado, e que nenhum site aponta para ele. Esta pagina e o ativo "citavel"
que faltava: junta num lugar o que so nos apuramos com fonte e data - quem
cobra taxa de turista, quanto, quem nao cobra e quem acabou com ela.

NADA E APURACAO NOVA. Cada linha resume o que a ficha, o guia ou a pagina de
pergunta so do destino ja publica, e leva a ela. Duas travas, as mesmas do
_build/cluster/comum.py:

  provas    frases que tem de existir na pagina de origem; se a ficha mudar,
            o gerador para em vez de publicar um resumo velho
  numeros   todo numero do resumo tem de aparecer na pagina de origem

Cabeca, cabecalho e rodape emprestados do sobre/, como o gratis.py.

Uso
---
    python _build/recortes/taxas.py            # so mostra
    python _build/recortes/taxas.py --aplica   # escreve
"""
import html as H
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
SITE = "https://viagemnalupa.com.br"
sys.path.insert(0, os.path.join(RAIZ, "_build", "cluster"))
import comum as C  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def texto(rel):
    """O texto visivel de uma pagina publicada, sem script, com a pontuacao colada."""
    h = le(os.path.join(RAIZ, "destinos", rel.replace("/", os.sep), "index.html"))
    h = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", h)
    t = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", h)))
    return re.sub(r"\s+([.,;:])", r"\1", t)


# (destino, pagina de origem, taxa, valor, resumo, provas)
COBRAM = [
    ("Fernando de Noronha", "fernando-de-noronha/tpa", "Taxa de Preservação Ambiental (TPA)", "R$ 105,79 por dia",
     "Por pessoa, por dia na ilha. 5 dias: R$ 520,50. O 11º dia custa sozinho R$ 126,95, mais que o primeiro.",
     ["R$ 105,79", "R$ 520,50", "R$ 126,95"]),
    ("Bonito", "bonito/tca", "Taxa de Conservação Ambiental (TCA)", "R$ 15,00 por dia de passeio",
     "Por pessoa, só nos dias com visita a atrativo. Menor de 7 anos não paga.",
     ["R$ 15,00 por dia", "Menor de 7 anos", "dias em que há visitação em atrativos"]),
    ("Jericoacoara", "fortaleza/quanto-custa", "Taxa de Turismo Sustentável", "R$ 41,50",
     "Da Prefeitura de Jijoca. A concessão do parque previa somar R$ 50 do ICMBio, cobrança que a Justiça Federal "
     "suspendeu.",
     ["Taxa de Turismo Sustentável da Prefeitura de Jijoca", "R$ 41,50", "previa somar R$ 50 do ICMBio"]),
    ("Maragogi", "maceio/quanto-custa", "Taxa ambiental municipal", "R$ 7",
     "Normalmente já vem embutida no preço do passeio de catamarã.",
     ["Taxa ambiental municipal de R$ 7 normalmente já embutida"]),
    ("Machu Picchu", "machu-picchu/entrada", "Taxa do SERNANP", "S/ 11",
     "Para estrangeiro, somada ao bilhete desde 1º/5/2026, depois de quatro adiamentos. Peruano paga S/ 5.",
     ["S/ 11", "a partir del 01 de mayo de 2026", "S/ 5"]),
    ("Lisboa", "lisboa/quanto-custa", "Taxa municipal turística", "€ 4 por noite",
     "Por pessoa, no máximo 7 noites. Não vem no preço da reserva: paga-se no alojamento.",
     ["€ 4 por pessoa por noite, no máximo 7 noites", "Não vem no preço da reserva"]),
    ("Porto", "porto/quanto-custa", "Taxa municipal turística", "€ 3 por noite",
     "Por pessoa, cobrada pelo alojamento. Até 12 anos não paga.",
     ["€ 3 por pessoa por noite", "até 12 anos"]),
    ("Barcelona", "barcelona/quanto-custa", "Taxa turística (imposto catalão + recargo municipal)", "€ 7,00 por noite",
     "Por pessoa, em hotel de até três estrelas; cinco estrelas, € 12,00. Teto de 7 noites; menor de 17 não paga. "
     "O recargo sobe em 1º de abril de 2027.",
     ["€ 7,00 por pessoa por noite num hotel de até três estrelas", "Cinco estrelas: € 12,00",
      "Teto de 7 noites; menor de 17 não paga", "1º de abril de 2027"]),
    ("Paris", "paris/quanto-custa", "Taxe de séjour", "€ 3,25 a € 15,93 por noite",
     "Por pessoa, conforme a categoria do hotel. Aparece no check-in ou no check-out, fora do preço da reserva.",
     ["€ 3,25 a € 15,93 por noite", "não vem no preço da reserva"]),
    ("Roma", "roma/quanto-custa", "Contributo di soggiorno", "€ 3 a € 10 por noite",
     "Por pessoa, conforme a classificação da hospedagem.",
     ["€ 3 a € 10 por noite", "por pessoa por noite"]),
    ("Aruba", "aruba/quanto-custa", "Imposto de hospedagem e taxa ambiental", "12,5% + US$ 3 por noite",
     "12,5% do valor do quarto, mais US$ 3 por quarto por noite.",
     ["12,5% do valor do quarto", "(US$ 3) por noite por quarto"]),
    ("Miami", "miami/quanto-custa", "Impostos sobre a diária e resort fee", "13% a 14%",
     "A diária publicada não inclui os impostos nem a resort fee diária.",
     ["some de 13% a 14% de impostos e a resort fee diária"]),
]

NAO_COBRAM = [
    ("Gramado", "gramado/quanto-custa", "revogada",
     "A taxa de R$ 3,43 por dia teve a revogação aprovada pela Câmara em 13/abr/2026. A Room Tax anunciada no "
     "lugar é voluntária: dá para recusar no check-out.",
     ["R$ 3,43 por dia e por apartamento", "13/abr/2026", "voluntária"]),
    ("Sevilha", "sevilha/quanto-custa", "não existe",
     "Não há taxa turística na Andaluzia em 2026. As prefeituras pedem, mas a criação depende do governo "
     "regional.",
     ["Não há taxa turística na Andaluzia em 2026"]),
    ("Granada", "granada/quanto-custa", "não existe",
     "A mesma regra da Andaluzia: sem o governo regional, o município não pode criar a taxa.",
     ["Não há taxa turística na Andaluzia em 2026"]),
    ("Florianópolis", "florianopolis/quanto-custa", "não existe para hóspede",
     "O Selo Turismo Legal é cobrado de ônibus, micro-ônibus e vans de turismo, não de quem chega de carro ou de "
     "avião.",
     ["Florianópolis não cobra taxa de quem se hospeda", "ônibus, micro-ônibus e vans de turismo"]),
    ("Londres", "londres/quanto-custa", "ainda não existe",
     "O governo britânico deu aos prefeitos o poder de criar a taxa; a imprensa não a espera antes de 2028. Só "
     "em fonte secundária.",
     ["o governo britânico deu aos prefeitos o poder de criar uma taxa por noite", "antes de 2028"]),
    ("São Paulo", "sao-paulo/quanto-custa", "não achada",
     "Não achamos taxa turística na capital, nem por hóspede nem por visitante. Lacuna declarada.",
     ["Não achamos taxa turística na capital"]),
    ("Foz do Iguaçu", "foz-do-iguacu/quanto-custa", "sem lei nem valor achados",
     "Hotéis associados ao Visit Iguassu cobram uma taxa na recepção, mas não achamos lei municipal nem valor "
     "publicado. Pergunte se é obrigatória.",
     ["não achamos lei municipal que a crie nem o valor publicado"]),
]

VOLTA = [
    ("Buenos Aires", "buenos-aires/quanto-custa", "21% de IVA devolvidos",
     "Na hospedagem, para quem paga com cartão emitido no exterior. Em dinheiro, o desconto se perde.",
     ["os 21% de IVA devolvidos por pagar com cartão emitido no exterior"]),
    ("Santiago", "santiago/quanto-custa", "19% de IVA isentos",
     "Na hospedagem, para estrangeiro sem residência no Chile que paga em moeda estrangeira.",
     ["Isenção de 19% de IVA na hospedagem",
      "para estrangeiro sem residência no Chile que paga em moeda estrangeira"]),
]


def confere(linhas, com_valor):
    for l in linhas:
        nome, rel, provas = l[0], l[1], l[-1]
        t = texto(rel)
        for p in provas:
            if p not in t:
                sys.exit("PARADO: a pagina de %s (%s) nao diz mais '%s'" % (nome, rel, p))
        escrito = " ".join(l[2:-1])
        C.confere_numeros(escrito, t + " 1º 11º", nome)


def esqueleto():
    s = le(os.path.join(RAIZ, "sobre", "index.html"))
    cabeca = s[:s.find('<main id="conteudo">')]
    pe = s[s.find("</main>"):]
    cabeca = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", cabeca, flags=re.S)
    return cabeca.replace(' aria-current="page"', ""), pe


def main(aplica):
    confere(COBRAM, True)
    confere(NAO_COBRAM, False)
    confere(VOLTA, False)
    n = len(COBRAM) + len(NAO_COBRAM) + len(VOLTA)

    titulo = "Taxas de turismo em 2026: quem cobra, quanto, e quem não cobra"
    descricao = ("Taxa de turista em %d lugares, com fonte e data: Noronha R$ 105,79 por dia, Lisboa € 4 por noite, "
                 "Barcelona € 7,00, Bonito R$ 15,00. E onde ela não existe, foi revogada ou o imposto volta." % n)
    url = SITE + "/taxas/"

    cabeca, pe = esqueleto()
    for pad, novo in (
            (r"<title>.*?</title>", "<title>%s — Viagem na Lupa</title>" % H.escape(titulo)),
            (r'<meta name="description" content="[^"]*">',
             '<meta name="description" content="%s">' % H.escape(descricao, quote=True)),
            (r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url),
            (r'<meta property="og:title" content="[^"]*">',
             '<meta property="og:title" content="%s — Viagem na Lupa">' % H.escape(titulo, quote=True)),
            (r'<meta property="og:description" content="[^"]*">',
             '<meta property="og:description" content="%s">' % H.escape(descricao, quote=True)),
            (r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % url)):
        cabeca, k = re.subn(pad, lambda m: novo, cabeca, count=1, flags=re.S)
        if k != 1:
            sys.exit("PARADO: a cabeca do sobre/ mudou (%s)" % pad[:30])

    perguntas = [
        ("Quais destinos cobram taxa de turista?",
         "Entre os destinos deste site: Fernando de Noronha, Bonito, Jericoacoara e Maragogi no Brasil; Machu "
         "Picchu, Lisboa, Porto, Barcelona, Paris, Roma, Aruba e Miami no exterior. O valor e a regra de cada um "
         "estão na tabela desta página."),
        ("A taxa turística vem no preço da reserva do hotel?",
         "Em geral, não. Em Lisboa, no Porto e em Paris ela é paga no alojamento, na chegada ou na saída, por "
         "pessoa e por noite. É a surpresa mais comum de quem chega com a estadia já paga."),
        ("Qual é a taxa de turismo mais cara do Brasil?",
         "Entre as que apuramos, a de Fernando de Noronha: R$ 105,79 por pessoa por dia, R$ 520,50 em cinco dias. "
         "A de Bonito custa R$ 15,00 por dia de passeio; a de Jericoacoara, R$ 41,50."),
        ("Gramado ainda cobra taxa de turismo?",
         "A Câmara aprovou a revogação em 13/abr/2026. O que pode aparecer no check-out é uma Room Tax anunciada "
         "pelo Convention Bureau, que é voluntária."),
    ]
    base = " ".join(" ".join(l[2:-1]) for l in COBRAM + NAO_COBRAM + VOLTA)
    for q, a in perguntas:
        C.confere_numeros(a, base, q)

    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Taxas de turismo", "item": url}]}
    jsonld = "".join('<script type="application/ld+json">%s</script>\n'
                     % json.dumps(o, ensure_ascii=False, separators=(",", ":"))
                     for o in (migalhas, C.faq_ld(perguntas)))
    cabeca = cabeca.replace("</head>", jsonld + "</head>", 1)

    def lk(rel, nome):
        return '<a href="../destinos/%s/">%s</a>' % (rel, H.escape(nome))

    cobram = "".join('<tr><td>%s</td><td>%s</td><td class="n"><b>%s</b></td><td>%s</td></tr>'
                     % (lk(rel, nome), H.escape(taxa), H.escape(valor), H.escape(resumo))
                     for nome, rel, taxa, valor, resumo, _ in COBRAM)
    nao = "".join('<tr><td>%s</td><td><b>%s</b></td><td>%s</td></tr>' % (lk(rel, nome), H.escape(est), H.escape(r))
                  for nome, rel, est, r, _ in NAO_COBRAM)
    volta = "".join('<li>%s: <b>%s</b>. %s</li>' % (lk(rel, nome), H.escape(est), H.escape(r))
                    for nome, rel, est, r, _ in VOLTA)

    partes = [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="../">Início</a> › Taxas de turismo</p>\n',
        '<div class="hero">\n  <h1>%s</h1>\n' % H.escape(titulo),
        '  <p>%d lugares, uma linha cada: a taxa que o turista paga além da diária e do ingresso, quanto custa e '
        'como é cobrada — e os lugares onde ela não existe, foi revogada ou o imposto volta.</p>\n%s</div>\n'
        '</div></div>\n\n' % (n, C.assinatura().replace(C.SOBE, "../")),
        '<div class="wrap wrap-estreito">\n',
        '<section class="bloco">\n  <div class="bloco-head"><span class="eyebrow">Como esta lista foi feita</span>'
        '<h2>Cada linha resume uma página do site</h2>\n'
        '  <p>Nenhum valor foi apurado só para esta lista: cada um está na ficha de custos ou no guia do destino, '
        'com a fonte e a data da consulta. O nome do destino leva a essa página. Onde a fonte é a imprensa ou não '
        'existe, a linha diz.</p>\n</div>\n</section>\n\n',
        '<section class="bloco" id="cobram">\n  <div class="bloco-head"><span class="eyebrow">%d lugares</span>'
        '<h2>Quem cobra, e quanto</h2></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Destino</th><th>Taxa</th><th>Valor</th><th>Como é cobrada'
        '</th></tr></thead><tbody>%s</tbody></table></div>\n</section>\n\n' % (len(COBRAM), cobram),
        '<section class="bloco" id="nao-cobram">\n  <div class="bloco-head"><span class="eyebrow">%d lugares</span>'
        '<h2>Onde não existe, acabou ou não achamos</h2></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Destino</th><th>Situação</th><th>O que apuramos</th></tr>'
        '</thead><tbody>%s</tbody></table></div>\n</section>\n\n' % (len(NAO_COBRAM), nao),
        '<section class="bloco" id="volta">\n  <div class="bloco-head"><span class="eyebrow">O contrário da taxa'
        '</span><h2>Onde o imposto volta para o turista</h2></div>\n  <ul class="plain">%s</ul>\n</section>\n\n'
        % volta,
        C.faq_html(perguntas, "taxa de turismo"),
        '</div>\n',
    ]
    pagina = cabeca + "".join(partes) + pe
    alvo = os.path.join(RAIZ, "taxas", "index.html")
    mudou = (not os.path.isfile(alvo)) or le(alvo) != pagina
    print("   /taxas/  %d cobram, %d nao cobram, %d devolvem   %s"
          % (len(COBRAM), len(NAO_COBRAM), len(VOLTA),
             "escrito" if (aplica and mudou) else ("ja igual" if not mudou else "SO MOSTRANDO")))
    if aplica and mudou:
        C.escreve(alvo, pagina)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
