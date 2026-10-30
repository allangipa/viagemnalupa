# -*- coding: utf-8 -*-
"""Paginas derivadas de Fernando de Noronha: o molde de Lisboa, aplicado.

  /destinos/fernando-de-noronha/tpa/   a Taxa de Preservacao Ambiental dia a
                                        dia - a busca mais forte da ilha

DE ONDE SAI TUDO: a tabela inteira (1 a 30 dias) e lida do arquivo guardado
em fontes/tpa-tabela-2026-20261029.txt, copiado do portal da Administracao
do Distrito; o ingresso do Parque, de fontes/parnamar-visitante-20261029.txt.
Nenhum valor da tabela e digitado aqui. Os numeros escritos a mao no texto
passam pela trava de numero do _build/cluster/comum.py contra essas fontes,
mais as contas que a propria pagina faz (custo por dia, dia a mais).

A mecanica (cabeca emprestada da ficha de custos, FAQ, Continue, Booking,
trava) e a do _build/cluster/comum.py, a mesma do Rio e de Lisboa.

Uso
---
    python _build/fernando-de-noronha/paginas.py            # so mostra
    python _build/fernando-de-noronha/paginas.py --aplica   # escreve

Depois, a cadeia de busca do LEIA-ME (regera_ficha.py <slug> /dev/null roda
toda). Regerar desfaz o que a cadeia pos.
"""
import html as H
import importlib.util
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), "cluster"))

import comum as C  # noqa: E402
from comum import le, limpa, acha, ld, SITE, SOBE, RAIZ  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

_s = importlib.util.spec_from_file_location("dados_noronha_paginas", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)

SLUG = "fernando-de-noronha"
NOME = "Fernando de Noronha"
GUIA = os.path.join(RAIZ, "destinos", SLUG, "index.html")
MOLDE = os.path.join(RAIZ, "destinos", SLUG, "quanto-custa", "index.html")
FONTE_TPA = le(os.path.join(AQUI, "fontes", "tpa-tabela-2026-20261029.txt"))
FONTE_PARQUE = le(os.path.join(AQUI, "fontes", "parnamar-visitante-20261029.txt"))
CREDITOS = json.loads(le(os.path.join(AQUI, "fotos-creditos.json")))
PONTOS = {p["id"]: p for p in _d.NORONHA["pontos"]}

IRMAS = [
    ("", "Guia dos 9 pontos"),
    ("tpa/", "TPA: quanto custa por dia"),
    ("quanto-custa/", "Quanto custa 5 dias em Noronha"),
    ("roteiro-5-dias/", "Roteiro de 5 dias"),
]


def reais(v):
    """1028.31 -> 'R$ 1.028,31'"""
    i, _, c = ("%.2f" % v).partition(".")
    return "R$ %s,%s" % ("{:,}".format(int(i)).replace(",", "."), c)


def num(t):
    """'1.028,31' -> 1028.31"""
    return float(t.replace(".", "").replace(",", "."))


def tabela_tpa():
    """{dias: total}, lida do arquivo da fonte; para se faltar um dia."""
    t = {int(d): num(v) for d, v in re.findall(r"^(\d{1,2}) R\$ ([\d.]+,\d\d)$", FONTE_TPA, re.M)}
    if sorted(t) != list(range(1, 31)):
        sys.exit("PARADO: a tabela da TPA na fonte nao tem os 30 dias")
    return t


def capa(img_id):
    cred = CREDITOS[img_id]
    alt = PONTOS[img_id]["foto"]["alt"]
    b = SOBE + "assets/img/%s/%s" % (SLUG, img_id)
    autor, lic = cred["cred"].split(" · ")[:2]
    figura = ('<figure class="hero-capa">\n  <img fetchpriority="high" srcset="%s-400.webp 400w, %s-640.webp 640w, '
              '%s-820.webp 820w, %s.webp 1200w" sizes="(min-width:1080px) 820px, 100vw" src="%s.webp" alt="%s" '
              'width="1200" height="675" decoding="async">\n  <figcaption><p class="foto-cred">Foto: %s · %s · '
              '<a href="%s" target="_blank" rel="noopener">Wikimedia Commons</a> · recortada</p></figcaption>\n'
              '</figure>' % (b, b, b, b, b, H.escape(alt, quote=True), H.escape(autor), lic, cred["pagina"]))
    return figura, "%s/assets/img/%s/%s.webp" % (SITE, SLUG, img_id), alt


def abre_pagina(migalha, eyebrow, h1, lead, figura, painel=""):
    return [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="%s">Início</a> › <a href="../../">Destinos</a> › '
        '<a href="../">%s</a> › %s</p>\n' % (SOBE, NOME, migalha),
        '<div class="hero">\n  <span class="eyebrow">%s</span>\n  <h1>%s</h1>\n  <p>%s</p>\n%s</div>\n'
        % (eyebrow, h1, lead, C.assinatura()),
        figura, "\n", painel, '\n<div style="height:clamp(1.4rem,3vw,2.2rem)"></div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
    ]


def pagina(pasta, titulo, descricao, img, alt, blocos_ld, partes):
    url = "%s/destinos/%s/%s/" % (SITE, SLUG, pasta)
    cabeca, pe = C.esqueleto(MOLDE, titulo, descricao, url, img, alt)
    cabeca = cabeca.replace("</head>", "".join(ld(b) for b in blocos_ld) + "</head>", 1)
    return os.path.join(RAIZ, "destinos", SLUG, pasta, "index.html"), cabeca + "".join(partes) + pe


# ------------------------------------------------------------------- TPA
def tpa(guia):
    t = tabela_tpa()
    marg = {d: round(t[d] - t.get(d - 1, 0), 2) for d in t}
    por_dia = {d: round(t[d] / d, 2) for d in t}
    # a forma da tabela de 2026: tres faixas e a virada. O texto depende dela;
    # se a tabela do ano que vem mudar de forma, para aqui. (Diferenca de um
    # centavo entre dias vizinhos e arredondamento da propria tabela.)
    def faixa(a, b):
        vs = [marg[d] for d in range(a, b + 1)]
        return max(vs) - min(vs) <= 0.02
    vira = next(d for d in range(2, 31) if marg[d] > marg[d - 1] + 1)
    if not (faixa(1, 4) and faixa(6, 10) and vira == 11 and marg[11] > t[1]
            and all(marg[d] > marg[d - 1] + 1 for d in range(12, 31))):
        sys.exit("PARADO: a tabela mudou de forma (vira no %do dia); reescreva o texto" % vira)
    parque = num(acha(r"Brasileiros têm desconto de 50%, custando R\$ ([\d,]+)\.", FONTE_PARQUE,
                      "o ingresso do brasileiro").group(1))
    parque_geral = num(acha(r"o ingresso tem o valor de R\$ ([\d,]+)\.", FONTE_PARQUE, "o ingresso geral").group(1))
    novo = num(acha(r"brasileiros de R\$ 192 para R\$ ([\d,]+);", FONTE_PARQUE, "o reajuste").group(1))
    acha(r"(Menores de 12 anos de idade e brasileiros \(as\) maiores de 60 anos)", FONTE_PARQUE, "a isencao")
    acha(r"(cartão de crédito emitido em país diferente do Brasil, o pagamento da TPA só poderá ocorrer no "
         r"balcão do aeroporto)", FONTE_TPA, "o cartao estrangeiro")
    acha(r"(será cobrado em dobro)", FONTE_TPA, "o dobro")

    url = "%s/destinos/%s/tpa/" % (SITE, SLUG)
    titulo = "TPA de Fernando de Noronha 2026: quanto custa por dia, de 1 a 30 dias"
    descricao = ("A tabela oficial da Taxa de Preservação Ambiental de Noronha dia a dia: %s por um dia, %s por "
                 "cinco, %s por dez — e o 11º dia, que custa sozinho mais que o primeiro."
                 % (reais(t[1]), reais(t[5]), reais(t[10])))
    figura, img, alt = capa("ingresso-do-parque")

    def linha(d):
        cls = ' style="background:var(--papel-2,rgba(0,0,0,.04))"' if d in (10, 11) else ""
        return ('<tr%s><td class="n">%d</td><td class="n"><b>%s</b></td><td class="n">%s</td><td class="n">%s</td>'
                '</tr>' % (cls, d, reais(t[d]), reais(por_dia[d]), reais(marg[d])))
    tabela = "".join(linha(d) for d in range(1, 31))

    def combo(d):
        return ('<li><b>%d dias</b>: TPA %s + ingresso %s = <b>%s</b> por pessoa.</li>'
                % (d, reais(t[d]), reais(parque), reais(t[d] + parque)))

    perguntas = [
        ("Quanto custa a TPA de Fernando de Noronha em 2026?",
         "%s por um dia, %s por três, %s por cinco, %s por sete e %s por dez, pela tabela oficial da Administração "
         "do Distrito. A tabela vai até 30 dias, que custam %s."
         % (reais(t[1]), reais(t[3]), reais(t[5]), reais(t[7]), reais(t[10]), reais(t[30]))),
        ("A TPA fica mais barata quanto mais dias eu fico?",
         "Até o 10º dia, sim: do 1º ao 4º cada dia custa %s, o 5º custa %s e do 6º ao 10º cada um custa %s — dez "
         "dias saem a %s por dia. No 11º a conta vira: só ele custa %s, mais que o primeiro, e cada dia seguinte "
         "custa mais que o anterior. Quinze dias saem a %s por dia; trinta, a %s."
         % (reais(marg[1]), reais(marg[5]), reais(marg[7]), reais(por_dia[10]), reais(marg[11]),
            reais(por_dia[15]), reais(por_dia[30]))),
        ("A TPA inclui o ingresso do Parque Nacional Marinho?",
         "Não. São duas cobranças diferentes: a TPA é do Distrito, por dia na ilha; o ingresso é do ICMBio, %s para "
         "brasileiro, válido por 10 dias. Em cinco dias, as duas somam %s."
         % (reais(parque), reais(t[5] + parque))),
        ("O que acontece se eu ficar mais dias do que paguei?",
         "Os dias excedentes são cobrados em dobro, quando a permanência não foi agendada e autorizada pela "
         "Administração (Lei 11.704, art. 86). Ajuste antes de ficar."),
        ("Como pagar a TPA?",
         "Pela internet antes do embarque, com cartão de crédito ou boleto, ou no desembarque. Cartão emitido fora "
         "do Brasil só paga no balcão do aeroporto da ilha."),
    ]

    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">1 dia</span><span class="big">%s</span>'
        '<span class="sub">Por pessoa, tabela de 2026.</span></div>'
        '<div class="pcel"><span class="rotp">5 dias</span><span class="big c">%s</span>'
        '<span class="sub">%s por dia.</span></div>'
        '<div class="pcel"><span class="rotp">10 dias</span><span class="big">%s</span>'
        '<span class="sub">%s por dia, o mais barato.</span></div>'
        '<div class="pcel"><span class="rotp">Só o 11º dia</span><span class="big c">%s</span>'
        '<span class="sub">Mais que o primeiro.</span></div>'
        '</div>' % (reais(t[1]), reais(t[5]), reais(por_dia[5]), reais(t[10]), reais(por_dia[10]),
                    reais(marg[11])))

    partes = abre_pagina(
        "Taxa ambiental (TPA)", "A taxa de quem chega",
        "TPA de Fernando de Noronha: quanto custa por dia",
        "A tabela oficial de 2026, de 1 a 30 dias, com o custo médio por dia e quanto custa cada dia a mais. Do "
        "6º ao 10º dia, o dia a mais é o mais barato da tabela; no 11º a conta vira.",
        figura, painel) + [
        '<section class="bloco"><div class="aviso a"><span class="t">O 11º dia custa sozinho %s — mais que o '
        'primeiro</span><p>A tabela tem três faixas: do 1º ao 4º dia, cada dia custa %s; o 5º, %s; do 6º ao 10º, '
        '%s cada. No 11º, o total salta para %s, e daí em diante cada dia custa mais que o de antes. <b>Quem pensa '
        'em ficar 11 dias paga %s a mais que quem fica 10</b>, e o 30º dia sozinho custa %s.</p></div>'
        '</section>\n\n'
        % (reais(marg[11]), reais(marg[1]), reais(marg[5]), reais(marg[7]), reais(t[11]), reais(marg[11]),
           reais(marg[30])),
        '<section class="bloco" id="tabela">\n  <div class="bloco-head"><span class="eyebrow">A tabela oficial'
        '</span><h2>De 1 a 30 dias</h2><p>Fonte: <b>Administração do Distrito Estadual de Fernando de Noronha</b>, '
        'portal oficial (noronha.pe.gov.br), tabela de permanência da TPA 2026, consultada em %s. A coluna do '
        'total é a da tabela; as outras duas são contas nossas sobre ela.</p></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Dias</th><th>Total</th><th>Média por dia</th>'
        '<th>Só este dia</th></tr></thead><tbody>%s</tbody></table></div>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem">Do 6º ao 10º dia, acrescentar um dia custa %s — o mais '
        'barato da tabela. As linhas marcadas são o 10º e o 11º, onde a conta vira. Diferenças de um centavo '
        'entre dias vizinhos vêm do arredondamento da própria tabela.</p>\n</section>\n\n'
        % (_d.APURACAO, tabela, reais(marg[7])),
        '<section class="bloco" id="contagem">\n  <div class="bloco-head"><span class="eyebrow">O que a página não '
        'diz</span><h2>Chegada e partida contam?</h2></div>\n'
        '  <p style="color:var(--nevoa)"><span class="flag">Lacuna declarada</span> A tabela fala em <i>“dias de '
        'permanência”</i> e não diz se o dia da chegada e o da partida contam. Uma viagem de 4 noites pode ser '
        'cobrada como 4 dias (%s) ou como 5 (%s). O site de pagamento pede as datas e calcula.</p>\n'
        '  <p style="color:var(--nevoa)">A <a href="../quanto-custa/">ficha de custos</a> usa 5 dias para 4 noites, '
        'o maior dos dois.</p>\n</section>\n\n' % (reais(t[4]), reais(t[5])),
        '<section class="bloco" id="com-o-parque">\n  <div class="bloco-head"><span class="eyebrow">A outra '
        'cobrança</span><h2>TPA e ingresso do Parque, somados</h2><p>O ingresso do Parque Nacional Marinho é do '
        'ICMBio, não do Distrito: %s para brasileiro e %s para o público geral, <b>válido por 10 dias</b> '
        '(Portaria ICMBio 4.423/2025, página consultada em %s). Menor de 12 anos e brasileiro acima de 60 não '
        'pagam o ingresso — mas pagam a TPA.</p></div>\n'
        '  <ul class="plain">%s</ul>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem"><span class="flag">Muda em 1º de novembro</span> a '
        'imprensa, citando o ICMBio, dá %s para brasileiro a partir de 1º/11/2026. As somas acima usam o valor '
        'da página oficial.</p>\n</section>\n\n'
        % (reais(parque), reais(parque_geral), _d.APURACAO, "".join(combo(d) for d in (3, 5, 7, 10)), reais(novo)),
        '<section class="bloco" id="pagar">\n  <div class="bloco-head"><span class="eyebrow">Na prática</span>'
        '<h2>Como pagar, e o dia a mais que sai em dobro</h2></div>\n'
        '  <ul class="plain"><li><b>Antes do embarque</b>, pela internet, com cartão de crédito ou boleto — ou no '
        'desembarque.</li><li><b>Cartão emitido fora do Brasil</b> só paga no balcão do aeroporto da ilha.</li>'
        '<li><b>A cobrança é individual</b>, para todo visitante não residente.</li><li><b>Dia excedente em '
        'dobro</b>: <i>“O valor da Taxa de Preservação Ambiental que se referir aos dias excedentes ao período '
        'inicialmente previsto, será cobrado em dobro”</i>, quando a permanência não foi agendada e autorizada '
        '(Lei 11.704, art. 86).</li></ul>\n</section>\n\n',
        C.faq_html(perguntas, "a TPA de Noronha"), "\n",
        C.continua(IRMAS, "de Fernando de Noronha", "tpa"),
        C.reserva(guia, SLUG, "em Fernando de Noronha", "tpa",
                  "A TPA conta por dia na ilha — reserve a pousada com as datas certas, porque o dia a mais "
                  "sem agendar sai em dobro. "),
        '</div>\n',
    ]
    # trava: todo numero escrito a mao sai das fontes ou das contas da propria tabela
    contas = " ".join(reais(v) for v in list(t.values()) + list(marg.values()) + list(por_dia.values())
                      + [t[d] + parque for d in (3, 5, 7, 10)])
    base = FONTE_TPA + " " + FONTE_PARQUE + " " + contas + " " + _d.APURACAO + " 1 2 3 4 5 7 10 11 12 15 30"
    for q, a in perguntas:
        C.confere_numeros(a, base, q)
    return pagina("tpa", titulo, descricao, img, alt,
                  [C.faq_ld(perguntas), C.migalhas(SLUG, NOME, "Taxa ambiental (TPA)", url)], partes)


# ------------------------------------------------- os links no guia
def liga_no_guia(h):
    return C.liga_no_ponto(h, "tpa", "tpa/", "Página completa da TPA: a tabela de 1 a 30 dias, o custo de cada dia "
                           "a mais e as perguntas frequentes")


def main(aplica):
    C.aplica_tudo((tpa,), ((GUIA, liga_no_guia),), GUIA, aplica)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
