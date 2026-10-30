# -*- coding: utf-8 -*-
"""Paginas derivadas de Foz do Iguacu: o molde de Noronha e Machu Picchu.

  /destinos/foz-do-iguacu/lado-brasileiro-ou-argentino/   as duas Cataratas
                                                           lado a lado

DE ONDE SAI TUDO: dos arquivos guardados em fontes/ - a pagina de tarifas,
horarios e perguntas do Parque Nacional Iguazu (iguazu-argentina-*.txt) e as
leituras do Parque Nacional do Iguacu, do Macuco Safari e da Secretaria de
Turismo (leituras-webfetch-*.txt). Os valores sao lidos de la por regex; se
um sumir, o gerador para. O peso entra em real pelo boletim de fechamento
do BCB de 23/10/2026 (ARS venda 0,003299), o mesmo da ficha de custos.

Uso
---
    python _build/foz-do-iguacu/paginas.py            # so mostra
    python _build/foz-do-iguacu/paginas.py --aplica   # escreve
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

_s = importlib.util.spec_from_file_location("dados_foz_paginas", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)

SLUG = "foz-do-iguacu"
NOME = "Foz do Iguaçu"
GUIA = os.path.join(RAIZ, "destinos", SLUG, "index.html")
MOLDE = os.path.join(RAIZ, "destinos", SLUG, "quanto-custa", "index.html")
AR = le(os.path.join(AQUI, "fontes", "iguazu-argentina-20261029.txt"))
BR = le(os.path.join(AQUI, "fontes", "leituras-webfetch-20261029.txt"))
CREDITOS = json.loads(le(os.path.join(AQUI, "fotos-creditos.json")))
PONTOS = {p["id"]: p for p in _d.FOZ["pontos"]}
ARS_VENDA = 0.003299            # BCB, boletim de fechamento de 23/10/2026
PASTA = "lado-brasileiro-ou-argentino"

IRMAS = [
    ("", "Guia dos 9 pontos"),
    (PASTA + "/", "Cataratas: lado brasileiro ou argentino"),
    ("quanto-custa/", "Quanto custa 3 dias em Foz"),
    ("roteiro-3-dias/", "Roteiro de 3 dias"),
]


def reais(v):
    i, _, c = ("%.2f" % v).partition(".")
    return "R$ %s,%s" % ("{:,}".format(int(i)).replace(",", "."), c)


def ars(n):
    return "AR$ " + "{:,}".format(n).replace(",", ".")


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


def inteiro(t):
    return int(t.replace(".", ""))


def real(t):
    return float(t.replace(".", "").replace(",", "."))


# ------------------------------------------------------ os dois lados
def lados(guia):
    br = real(acha(r"Brasil/Mercosul: R\$ ([\d,]+)", BR, "o lado brasileiro").group(1))
    br_int = real(acha(r"Ingresso Integral: R\$ ([\d,]+)", BR, "a integral").group(1))
    fundo = real(acha(r"\+ R\$ ([\d,]+) de contribuição ao Fundo Iguaçu\)\nBrasil", BR, "o Fundo Iguacu").group(1))
    ar = inteiro(acha(r"Visitantes internacionales  AR\$ ([\d.]+)", AR, "o lado argentino").group(1))
    ar_res = inteiro(acha(r"Residentes en Argentina  AR\$ ([\d.]+)", AR, "o residente argentino").group(1))
    auto = inteiro(acha(r"Autos AR\$ ([\d.]+)", AR, "o estacionamento").group(1))
    luna = inteiro(acha(r"Paseo de Luna Llena: Adultos AR\$ ([\d.]+)", AR, "a lua cheia").group(1))
    macuco = real(acha(r'"Adulto R\$ ([\d,]+) por pessoa"', BR, "o Macuco").group(1))
    for prova, o_que in (
            (r"De segunda a sexta: das 9h às 16h\" / \"Sábado e domingos: das 8h30 às 16h", "o horario brasileiro"),
            (r"de 8:00 a 18:00", "o horario argentino"), (r"Ingreso al Área Cataratas hasta las 16:00 h", "a entrada"),
            (r"Última salida 15:30 h", "o ultimo trem"), (r"Ingreso a Circuitos hasta las 15:45 h", "15:45"),
            (r"Último ingreso 16:45 h", "16:45"), (r"el segundo día tiene 50% de descuento", "o segundo dia"),
            (r"dinero efectivo en boletería \(pesos argentinos\)", "o pagamento"),
            (r"Crianças até 6 anos isentas", "a crianca no Brasil"), (r"menores de 6 años", "a crianca na Argentina"),
            (r"não dispõe de meia-entrada", "a meia"), (r"DNI o pasaporte", "o documento"),
            (r"diariamente das 7h as 19h", "o onibus")):
        acha("(%s)" % prova, AR + BR, o_que)

    r_ar, r_auto, r_luna = round(ar * ARS_VENDA, 2), round(auto * ARS_VENDA, 2), round(luna * ARS_VENDA, 2)
    r_ar2 = round(ar * 0.5 * ARS_VENDA, 2)
    pct = round((r_ar / br - 1) * 100)
    if pct != 64:
        sys.exit("PARADO: a diferenca mudou (%d%%); reescreva o texto" % pct)
    dois = round(br + r_ar, 2)

    titulo = "Cataratas do Iguaçu: lado brasileiro ou argentino? Preço e horário em 2026"
    descricao = ("Lado brasileiro: %s para brasileiro. Lado argentino: %s, cerca de %s, sem tarifa Mercosul. "
                 "Horários, o último trem da Garganta, quem tem desconto e como fazer os dois."
                 % (reais(br), ars(ar), reais(r_ar)))
    figura, img, alt = capa("parque-nacional-do-iguacu")

    def linha(rot, a, b):
        return '<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (rot, a, b)
    tabela = "".join([
        linha("Entrada para brasileiro", "<b>%s</b> (Brasil/Mercosul)" % reais(br),
              "<b>%s</b>, cerca de %s — sem faixa Mercosul" % (ars(ar), reais(r_ar))),
        linha("Entrada para quem é de fora do Mercosul", reais(br_int), "%s, a mesma" % ars(ar)),
        linha("Quem é da casa", "argentino e paraguaio pagam como brasileiro: %s" % reais(br),
              "residente na Argentina: %s" % ars(ar_res)),
        linha("Criança", "até 6 anos não paga", "menor de 6 anos não paga"),
        linha("Idoso e estudante", "<b>sem meia-entrada</b>: pagam %s" % reais(br),
              "a meia de estudante é só para estudante argentino"),
        linha("Segundo dia", "sem desconto na tabela", "<b>metade do preço</b>, com o ingresso do primeiro dia"),
        linha("Como pagar", "—", "cartão, ou dinheiro <b>só em peso argentino</b>"),
        linha("Horário", "seg a sex 9h às 16h; sáb e dom 8h30 às 16h",
              "todos os dias 8h às 18h; <b>entrada até 16h</b>"),
        linha("Trem até a Garganta do Diabo", "—",
              "<b>último às 15h30</b>, incluído na entrada"),
        linha("Estacionamento", "só link de reserva, sem valor publicado", "%s o carro (%s)" % (ars(auto),
                                                                                         reais(r_auto))),
        linha("Passeio extra", "Macuco Safari, %s, entrada do parque à parte" % reais(macuco),
              "Passeio de Lua Cheia, %s (%s)" % (ars(luna), reais(r_luna))),
    ])

    perguntas = [
        ("Qual lado das Cataratas é mais barato, o brasileiro ou o argentino?",
         "O brasileiro, para quem é do Mercosul: %s, contra %s do lado argentino, cerca de %s pela taxa de venda do "
         "Banco Central de 23 de outubro de 2026 — %d%% a mais." % (reais(br), ars(ar), reais(r_ar), pct)),
        ("Brasileiro tem desconto no lado argentino das Cataratas?",
         "Não. O Parque Nacional Iguazú não tem faixa Mercosul: o brasileiro paga %s, como qualquer estrangeiro. O "
         "único desconto aberto a ele é o do segundo dia, que sai pela metade com o ingresso do primeiro." % ars(ar)),
        ("Posso pagar o lado argentino com real?",
         "Em dinheiro, não: a bilheteria aceita cartão de crédito, débito ou dinheiro em peso argentino. No cartão "
         "brasileiro entra o IOF de compra internacional."),
        ("Até que horas dá para entrar em cada lado?",
         "No lado brasileiro, a página dá 9h às 16h nos dias úteis e 8h30 às 16h no fim de semana. No argentino, o "
         "parque abre das 8h às 18h, mas a entrada vai até 16h e o último trem para a Garganta do Diabo sai às "
         "15h30."),
        ("Dá para fazer os dois lados no mesmo dia?",
         "Os dois fecham a entrada às 16h, e o trem da Garganta sai até 15h30. O roteiro deste site faz um lado por "
         "dia. Os dois juntos custam %s para o brasileiro." % reais(dois)),
    ]

    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">Lado brasileiro</span><span class="big">%s</span>'
        '<span class="sub">Brasil e Mercosul. Integral: %s.</span></div>'
        '<div class="pcel"><span class="rotp">Lado argentino</span><span class="big c">%s</span>'
        '<span class="sub">Cerca de %s, para qualquer estrangeiro.</span></div>'
        '<div class="pcel"><span class="rotp">Diferença</span><span class="big c">%d%%</span>'
        '<span class="sub">A mais do lado argentino, para o brasileiro.</span></div>'
        '<div class="pcel"><span class="rotp">Segundo dia argentino</span><span class="big">%s</span>'
        '<span class="sub">Metade, com o ingresso do primeiro.</span></div>'
        '</div>' % (reais(br), reais(br_int), ars(ar), reais(r_ar), pct, reais(r_ar2)))

    partes = abre_pagina(
        "Lado brasileiro ou argentino", "As duas Cataratas",
        "Cataratas do Iguaçu: lado brasileiro ou argentino?",
        "O mesmo rio, duas bilheterias e duas regras. O brasileiro paga %s de um lado e %s do outro — e o argentino "
        "paga como brasileiro do lado de cá. Preço, horário, desconto e o que muda em cada um."
        % (reais(br), ars(ar)),
        figura, painel) + [
        '<section class="bloco"><div class="aviso a"><span class="t">O lado argentino não tem tarifa Mercosul — o '
        'brasileiro tem</span><p>No Parque Nacional do Iguaçu, a faixa <b>Brasil/Mercosul</b> (%s) vale para '
        'brasileiro, argentino e paraguaio. No Parque Nacional Iguazú, a tabela tem <b>“Visitantes internacionales '
        '%s”</b> e nenhuma faixa Mercosul: o brasileiro paga como qualquer estrangeiro, %d%% a mais. E a '
        'bilheteria não aceita real em dinheiro.</p></div></section>\n\n' % (reais(br), ars(ar), pct),
        '<section class="bloco" id="lado-a-lado">\n  <div class="bloco-head"><span class="eyebrow">Lado a lado</span>'
        '<h2>O que muda de um parque para o outro</h2><p>Fontes: site oficial do Parque Nacional do Iguaçu '
        '(tabela de 2026, publicada em 19/12/2025) e do Parque Nacional Iguazú (tarifas vigentes desde 1º/6/2026, '
        'horários e perguntas frequentes), consultados em %s. O peso em real pela taxa de venda do Banco Central '
        'de 23/out/2026 (AR$ 1 = R$ 0,003299).</p></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th></th><th>Lado brasileiro</th><th>Lado argentino</th></tr>'
        '</thead><tbody>%s</tbody></table></div>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem">Os %s do lado brasileiro incluem %s do Fundo Iguaçu, '
        '<b>que é voluntário</b>. <span class="flag">Fontes divergem</span> a página argentina diz que a entrada '
        'nos circuitos vai até 15h45 e, mais abaixo, até 16h45; conte com o horário mais cedo.</p>\n'
        '</section>\n\n' % (_d.APURACAO, tabela, reais(br), reais(fundo)),
        '<section class="bloco" id="os-dois">\n  <div class="bloco-head"><span class="eyebrow">Para fazer os dois'
        '</span><h2>Um lado por dia, e a Garganta primeiro</h2></div>\n'
        '  <ul class="plain"><li><b>Do lado argentino, vá direto à Garganta do Diabo</b>: o primeiro trem sai às '
        '8h20 e o último às 15h30.</li><li><b>Leve peso ou cartão</b>, e documento: a bilheteria pede DNI ou '
        'passaporte para definir a categoria.</li><li><b>O ônibus</b> para o lado argentino sai do Terminal de '
        'Transporte Urbano todos os dias das 7h às 19h, por duas empresas — <span class="flag">Lacuna declarada'
        '</span> a Secretaria de Turismo não publica o preço.</li><li><b>Voltando ao lado argentino no dia '
        'seguinte</b>, o ingresso sai por %s.</li></ul>\n'
        '  <p style="color:var(--nevoa)">O <a href="../roteiro-3-dias/">roteiro de 3 dias</a> faz o lado brasileiro '
        'na sexta e o argentino no sábado.</p>\n</section>\n\n' % reais(r_ar2),
        C.faq_html(perguntas, "os dois lados das Cataratas"), "\n",
        C.continua(IRMAS, "de Foz do Iguaçu", PASTA),
        C.reserva(guia, SLUG, "em Foz do Iguaçu", "lados",
                  "Quem faz os dois lados dorme em Foz: o ônibus para a Argentina sai do terminal urbano da "
                  "cidade. "),
        '</div>\n',
    ]
    contas = " ".join([reais(v) for v in (br, br_int, r_ar, r_auto, r_luna, r_ar2, dois, macuco, fundo)]
                      + [ars(v) for v in (ar, ar_res, auto, luna)] + ["%d%%" % pct, "23", "2026", "15h30", "16h",
                                                                        "9h", "8h30", "8h", "18h"])
    for q, a in perguntas:
        C.confere_numeros(a, AR + " " + BR + " " + contas, q)
    url = "%s/destinos/%s/%s/" % (SITE, SLUG, PASTA)
    return pagina(PASTA, titulo, descricao, img, alt,
                  [C.faq_ld(perguntas), C.migalhas(SLUG, NOME, "Lado brasileiro ou argentino", url)], partes)


# ------------------------------------------------- os links no guia
def liga_no_guia(h):
    for pid in ("parque-nacional-do-iguacu", "parque-nacional-iguazu"):
        h = C.liga_no_ponto(h, pid, PASTA + "/", "Os dois lados comparados: preço, horário, desconto e como fazer "
                            "os dois")
    return h


def main(aplica):
    C.aplica_tudo((lados,), ((GUIA, liga_no_guia),), GUIA, aplica)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
