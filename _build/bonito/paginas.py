# -*- coding: utf-8 -*-
"""Paginas derivadas de Bonito: o molde de Noronha, Machu Picchu e Foz.

  /destinos/bonito/tca/   a Taxa de Conservacao Ambiental: quanto, quando
                           conta e como pagar

DE ONDE SAI TUDO: da nota informativa da prefeitura guardada em
fontes/tca-nota-prefeitura-20261029.txt. O valor por dia, as isencoes, o
portal e o seguro sao lidos de la; se um sumir, o gerador para. A
comparacao com Noronha le a tabela guardada em
_build/fernando-de-noronha/fontes/.

Uso
---
    python _build/bonito/paginas.py            # so mostra
    python _build/bonito/paginas.py --aplica   # escreve
"""
import html as H
import importlib.util
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), "cluster"))

import comum as C  # noqa: E402
from comum import le, acha, ld, SITE, SOBE, RAIZ  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

_s = importlib.util.spec_from_file_location("dados_bonito_paginas", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)

SLUG = "bonito"
NOME = "Bonito"
GUIA = os.path.join(RAIZ, "destinos", SLUG, "index.html")
MOLDE = os.path.join(RAIZ, "destinos", SLUG, "quanto-custa", "index.html")
FONTE = le(os.path.join(AQUI, "fontes", "tca-nota-prefeitura-20261029.txt"))
NORONHA = le(os.path.join(RAIZ, "_build", "fernando-de-noronha", "fontes", "tpa-tabela-2026-20261029.txt"))
CREDITOS = json.loads(le(os.path.join(AQUI, "fotos-creditos.json")))
PONTOS = {p["id"]: p for p in _d.BONITO["pontos"]}

IRMAS = [
    ("", "Guia dos 8 pontos"),
    ("tca/", "TCA: a taxa ambiental"),
    ("quanto-custa/", "Quanto custa 4 dias em Bonito"),
    ("roteiro-4-dias/", "Roteiro de 4 dias"),
]


def reais(v):
    i, _, c = ("%.2f" % v).partition(".")
    return "R$ %s,%s" % ("{:,}".format(int(i)).replace(",", "."), c)


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


def real(t):
    return float(t.replace(".", "").replace(",", "."))


# --------------------------------------------------------------------- TCA
def tca(guia):
    dia = real(acha(r"• R\$ ([\d,]+) por dia para visitantes brasileiros;", FONTE, "o valor do brasileiro").group(1))
    dia_est = real(acha(r"• R\$ ([\d,]+) por dia para visitantes estrangeiros\.", FONTE, "o estrangeiro").group(1))
    idade = int(acha(r"Crianças menores de (\d+) anos", FONTE, "a idade da isencao").group(1))
    morte = real(acha(r"Morte Acidental \(MA\): até R\$ ([\d.,]+)", FONTE, "a morte acidental").group(1))
    funeral = real(acha(r"Auxílio Funeral: até R\$ ([\d.,]+)", FONTE, "o funeral").group(1))
    hosp = real(acha(r"\[\.\.\.\] até R\$ ([\d.,]+)\nAssistência", FONTE, "o reembolso").group(1))
    for prova, o_que in ((r"O sistema gera o valor total da taxa referente aos dias em que há visitação em atrativos",
                          "os dias de passeio"), (r"www\.turistapornatureza\.com\.br", "o portal"),
                         (r"Obter os vouchers \(após a agência realizar a emissão\)", "a ordem"),
                         (r"Lei Municipal nº 162/2021", "a lei"), (r"a partir do dia 20 de dezembro", "o inicio"),
                         (r"Funcionamento diário das 7h às 19h", "o APH"), (r"Moradores de Bonito/MS", "o morador"),
                         (r"Trabalhadores e prestadores de serviço que atuam no município", "o trabalhador")):
        acha("(%s)" % prova, FONTE, o_que)
    if dia != dia_est:
        sys.exit("PARADO: brasileiro e estrangeiro passaram a pagar diferente; reescreva o texto")
    tpa5 = real(acha(r"(?m)^5 R\$ ([\d.,]+)\s*$", NORONHA, "a TPA de 5 dias").group(1))

    url = "%s/destinos/%s/tca/" % (SITE, SLUG)
    titulo = "TCA de Bonito 2026: quanto custa a taxa ambiental e como pagar"
    descricao = ("A Taxa de Conservação Ambiental de Bonito custa %s por pessoa, por dia de passeio — não por dia "
                 "na cidade. Quem não paga, onde pagar antes dos vouchers e o seguro que vem junto." % reais(dia))
    figura, img, alt = capa("tca")

    tabela = "".join(
        '<tr><td class="n">%d</td><td class="n"><b>%s</b></td><td class="n">%s</td><td class="n">%s</td></tr>'
        % (n, reais(dia * n), reais(dia * n * 2), reais(dia * n * 4)) for n in range(1, 8))

    perguntas = [
        ("Quanto custa a taxa de Bonito?",
         "%s por pessoa, por dia, para brasileiro ou estrangeiro. É a Taxa de Conservação Ambiental, a TCA, "
         "cobrada pela prefeitura desde 20 de dezembro de 2025." % reais(dia)),
        ("A TCA conta todos os dias que eu fico em Bonito?",
         "Não. A prefeitura diz que o sistema gera o valor da taxa referente aos dias em que há visitação em "
         "atrativos. Quatro dias na cidade com três de passeio pagam %s por pessoa." % reais(dia * 3)),
        ("Quem não paga a TCA?",
         "Criança menor de %d anos, morador de Bonito e quem trabalha no município. Morador e trabalhador não "
         "precisam de cadastro, mas devem mostrar documento se o fiscal pedir." % idade),
        ("Onde pagar a TCA de Bonito?",
         "Só pelo portal turistapornatureza.com.br: informa-se o grupo e os dias, paga-se online, e depois a "
         "agência emite os vouchers dos passeios."),
        ("A TCA de Bonito inclui seguro?",
         "Sim, um seguro ao visitante durante a permanência: morte acidental e invalidez até %s, auxílio funeral "
         "até %s e reembolso de hospedagem do acompanhante até %s, além de atendimento pré-hospitalar das 7h às "
         "19h." % (reais(morte), reais(funeral), reais(hosp))),
    ]

    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">Por dia de passeio</span><span class="big c">%s</span>'
        '<span class="sub">Por pessoa, brasileiro ou estrangeiro.</span></div>'
        '<div class="pcel"><span class="rotp">4 dias de passeio</span><span class="big">%s</span>'
        '<span class="sub">O roteiro deste site.</span></div>'
        '<div class="pcel"><span class="rotp">Menor de %d anos</span><span class="big">grátis</span>'
        '<span class="sub">E morador e trabalhador de Bonito.</span></div>'
        '<div class="pcel"><span class="rotp">Seguro incluído</span><span class="big">%s</span>'
        '<span class="sub">Morte acidental ou invalidez.</span></div>'
        '</div>' % (reais(dia), reais(dia * 4), idade, reais(morte)))

    partes = abre_pagina(
        "Taxa ambiental (TCA)", "A taxa de quem passeia",
        "TCA de Bonito: quanto custa a taxa ambiental e como pagar",
        "%s por pessoa, por dia de passeio — e só por dia de passeio. Quem não paga, onde pagar antes dos "
        "vouchers, o seguro que vem junto e a contestação na Justiça." % reais(dia),
        figura, painel) + [
        '<section class="bloco"><div class="aviso a"><span class="t">Conta só o dia com passeio, não o dia na '
        'cidade</span><p>A nota da prefeitura: <i>“O sistema gera o valor total da taxa referente aos dias em que '
        'há visitação em atrativos.”</i> Chegar à noite e só jantar não gera taxa; um dia de descanso entre dois '
        'passeios também não. É o contrário da TPA de Fernando de Noronha, que conta cada dia na ilha.</p></div>'
        '</section>\n\n',
        '<section class="bloco" id="tabela">\n  <div class="bloco-head"><span class="eyebrow">A conta</span>'
        '<h2>Quanto dá, por dias de passeio</h2><p>Fonte: <b>Prefeitura Municipal de Bonito</b>, nota informativa '
        'de 19/11/2025 (atualizada em 27/11/2025), consultada em %s: <b>%s por dia, por pessoa</b>, desde 20 de '
        'dezembro de 2025 (Lei Municipal 162/2021). A tabela é conta nossa sobre esse valor.</p></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Dias de passeio</th><th>1 pessoa</th><th>2 pessoas</th>'
        '<th>4 pessoas</th></tr></thead><tbody>%s</tbody></table></div>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem">Criança menor de %d anos não entra na conta. Para '
        'comparar: cinco dias em Fernando de Noronha pagam %s de TPA por pessoa, pela tabela oficial da ilha.</p>\n'
        '</section>\n\n' % (_d.APURACAO, reais(dia), tabela, idade, reais(tpa5)),
        '<section class="bloco" id="pagar">\n  <div class="bloco-head"><span class="eyebrow">Na prática</span>'
        '<h2>Quem paga, onde e em que ordem</h2></div>\n'
        '  <ul class="plain"><li><b>Isentos</b>: criança menor de %d anos, morador de Bonito e trabalhador ou '
        'prestador de serviço no município — sem cadastro, mas com documento se o fiscal pedir.</li>'
        '<li><b>Só pelo portal turistapornatureza.com.br</b>: informa-se o grupo e o período, o sistema calcula os '
        'dias de passeio, paga-se online.</li><li><b>Depois a agência emite os vouchers</b> — em Bonito nenhum '
        'passeio se compra na porta, e o voucher sai depois da taxa.</li></ul>\n</section>\n\n' % idade,
        '<section class="bloco" id="seguro">\n  <div class="bloco-head"><span class="eyebrow">O que vem junto</span>'
        '<h2>O seguro ao visitante</h2></div>\n'
        '  <p style="color:var(--nevoa)">Em contrapartida à TCA, a prefeitura dá um seguro válido durante a '
        'permanência: <b>morte acidental e invalidez até %s</b>, <b>auxílio funeral até %s</b> e, em caso de '
        'acidente em atrativo licenciado, <b>reembolso de hospedagem do acompanhante até %s</b>, com nota fiscal e '
        'comprovação da internação. Há ainda atendimento pré-hospitalar com ambulância, <b>todos os dias das 7h às '
        '19h</b>.</p>\n</section>\n\n' % (reais(morte), reais(funeral), reais(hosp)),
        '<section class="bloco" id="justica">\n  <div class="bloco-head"><span class="eyebrow">O que pode mudar'
        '</span><h2>A taxa na Justiça</h2></div>\n'
        '  <p style="color:var(--nevoa)"><span class="flag">Só em fonte secundária</span> <b>associações do '
        'turismo contestam a TCA num mandado de segurança coletivo</b>, que o Tribunal de Justiça de Mato Grosso do '
        'Sul reabriu depois de uma decisão que o extinguia (Campo Grande News). Até a consulta desta página, a '
        'cobrança seguia valendo.</p>\n</section>\n\n',
        C.faq_html(perguntas, "a TCA de Bonito"), "\n",
        C.continua(IRMAS, "de Bonito", "tca"),
        C.reserva(guia, SLUG, "em Bonito", "tca",
                  "A TCA conta os dias de passeio, não as noites: a pousada pode ter um dia livre sem taxa. "),
        '</div>\n',
    ]
    contas = " ".join([reais(dia * n * k) for n in range(1, 8) for k in (1, 2, 4)]
                      + [reais(v) for v in (morte, funeral, hosp, tpa5)] + [str(idade), "2025", "2026"])
    for q, a in perguntas:
        C.confere_numeros(a, FONTE + " " + contas, q)
    return pagina("tca", titulo, descricao, img, alt,
                  [C.faq_ld(perguntas), C.migalhas(SLUG, NOME, "Taxa ambiental (TCA)", url)], partes)


# ------------------------------------------------- os links no guia
def liga_no_guia(h):
    return C.liga_no_ponto(h, "tca", "tca/", "Página completa da TCA: a conta por dias de passeio, quem não paga, "
                           "como pagar e o seguro")


def main(aplica):
    C.aplica_tudo((tca,), ((GUIA, liga_no_guia),), GUIA, aplica)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
