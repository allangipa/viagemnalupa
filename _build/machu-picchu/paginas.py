# -*- coding: utf-8 -*-
"""Paginas derivadas de Machu Picchu: o molde de Noronha, aplicado.

  /destinos/machu-picchu/entrada/   quanto custa a entrada para brasileiro

DE ONDE SAI TUDO: do arquivo fontes/leituras-20261029.txt - a resolucao do
SERNANP no El Peruano, as notas da Andina e as materias de El Comercio e
Infobae, com o cambio do BCB. Os valores sao lidos de la por regex; se o
arquivo nao trouxer um deles, o gerador para.

COMO OS NUMEROS ENTRAM: a mesma decisao do Allan de 29/10/2026 para a ficha.
A tabela oficial do Ministerio fica atras de um "no soy un robot"; bilhete
de estrangeiro e taxa do SERNANP vem da imprensa, marcados como "tarifa
oficial noticiada pela imprensa". A montanha do estrangeiro so tem valor de
guia, marcado como fonte secundaria.

Uso
---
    python _build/machu-picchu/paginas.py            # so mostra
    python _build/machu-picchu/paginas.py --aplica   # escreve
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
from comum import le, acha, ld, SITE, SOBE, RAIZ  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

_s = importlib.util.spec_from_file_location("dados_machu_paginas", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)

SLUG = "machu-picchu"
NOME = "Machu Picchu"
GUIA = os.path.join(RAIZ, "destinos", SLUG, "index.html")
MOLDE = os.path.join(RAIZ, "destinos", SLUG, "quanto-custa", "index.html")
FONTE = le(os.path.join(AQUI, "fontes", "leituras-20261029.txt"))
CREDITOS = json.loads(le(os.path.join(AQUI, "fotos-creditos.json")))
PONTOS = {p["id"]: p for p in _d.MACHU["pontos"]}
IMP = '<span class="flag">Tarifa oficial noticiada pela imprensa</span> '
SEC = '<span class="flag">Só em fonte secundária</span> '

IRMAS = [
    ("", "Guia dos 8 pontos"),
    ("entrada/", "A entrada para brasileiro"),
    ("quanto-custa/", "Quanto custa 4 dias em Cusco e Machu Picchu"),
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


def lido(padrao, o_que, tipo=int):
    return tipo(acha(padrao, FONTE, o_que).group(1).replace(",", "."))


# --------------------------------------------------------------- a entrada
def entrada(guia):
    est = lido(r"El Comercio, 07/02/2026: estrangeiro adulto S/ (\d+);", "o bilhete de estrangeiro")
    est_estud = lido(r"estudante estrangeiro S/ (\d+);", "o estudante estrangeiro")
    menor_a, menor_b = (int(x) for x in acha(r'"Entre (\d+) y (\d+) soles, según circuito elegido"', FONTE,
                                              "o menor estrangeiro").groups())
    can, can_red = (int(x) for x in acha(r"geral S/ (\d+), reduzida S/ (\d+)\.\nRotas 1-A", FONTE,
                                          "a tarifa promocional").groups())
    mont, mont_red = (int(x) for x in acha(r"\(Gran Caverna\): geral S/ (\d+), reduzida S/ (\d+)\.", FONTE,
                                            "a montanha promocional").groups())
    sern_est, sern_nac = (int(x) for x in acha(r"estrangeiros S/ (\d+), nacionais\nS/ (\d+)", FONTE,
                                                "o SERNANP").groups())
    pen = lido(r"PEN venda (1,\d+)", "o cambio", float)
    acha(r"(01/01/2024 \(R\.D\. 112-2023\), 01/01/2025 \(R\.D\. 297-2023\), 01/01/2026 \(R\.D\. 22-2025\),\n"
         r"01/02/2026 \(R\.D\. 16-2025\))", FONTE, "os adiamentos")
    acha(r"(estrangeiro adulto US\$ 60)", FONTE, "a divergencia")
    acha(r"(Aforo: 5\.600/dia na alta \(01/01; 02 a 05/04; 19/06 a 02/11; 30 e 31/12/2026\); 4\.500)", FONTE,
         "o aforo")

    r_est, r_sern, r_can = round(est * pen, 2), round(sern_est * pen, 2), round(can * pen, 2)
    r_can_sern = round(sern_nac * pen, 2)
    total_br, total_pe = est + sern_est, can + sern_nac
    razao = est / can
    if round(razao, 1) != 2.4:
        sys.exit("PARADO: a razao mudou (%.2f); reescreva o '2,4 vezes'" % razao)

    url = "%s/destinos/%s/entrada/" % (SITE, SLUG)
    titulo = "Machu Picchu para brasileiro: quanto custa a entrada em 2026"
    descricao = ("Brasileiro paga S/ %d pela entrada de Machu Picchu, 2,4 vezes os S/ %d do peruano e do andino, e "
                 "mais S/ %d de taxa do SERNANP desde maio: %s em real. Circuitos, montanha e hora marcada."
                 % (est, can, sern_est, reais(r_est + r_sern)))
    figura, img, alt = capa("circuitos")

    tabela = (
        '<tr><td><b>Brasileiro e demais estrangeiros</b>, adulto</td><td class="n"><b>S/ %d</b></td>'
        '<td class="n">%s</td><td>%s</td></tr>'
        '<tr><td>Estudante estrangeiro</td><td class="n">S/ %d</td><td class="n">%s</td><td>%s</td></tr>'
        '<tr><td>Menor estrangeiro, 3 a 17 anos</td><td class="n">S/ %d a S/ %d</td><td class="n">—</td>'
        '<td>conforme o circuito; %s</td></tr>'
        '<tr><td><b>Peruano, residente e cidadão da Comunidade Andina</b>, adulto</td><td class="n"><b>S/ %d</b>'
        '</td><td class="n">%s</td><td>tarifa promocional de 2026 (R.M. 000284-2025-MC, pela Andina)</td></tr>'
        '<tr><td>Peruano e andino, estudante ou menor de 3 a 17</td><td class="n">S/ %d</td><td class="n">%s</td>'
        '<td>idem</td></tr>'
        '<tr><td>Menor de 3 anos</td><td class="n">grátis</td><td class="n">—</td><td>Andina</td></tr>'
        % (est, reais(r_est), IMP + "El Comercio e Infobae, fev/2026", est_estud, reais(round(est_estud * pen, 2)),
           IMP + "El Comercio, fev/2026", menor_a, menor_b, IMP + "El Comercio", can, reais(r_can), can_red,
           reais(round(can_red * pen, 2))))

    perguntas = [
        ("Quanto custa a entrada de Machu Picchu para brasileiro em 2026?",
         "S/ %d o adulto, segundo a imprensa peruana, que reproduz a tarifa do Ministério da Cultura — mais S/ %d da "
         "taxa do SERNANP desde 1º de maio de 2026. São S/ %d, ou %s pela taxa de venda do Banco Central de 23 de "
         "outubro de 2026." % (est, sern_est, total_br, reais(r_est + r_sern))),
        ("Por que o peruano paga menos que o brasileiro?",
         "A tarifa promocional de 2026, S/ %d, vale para peruanos, residentes e cidadãos da Comunidade Andina — "
         "Bolívia, Colômbia, Equador e Peru. O Brasil não é membro, e o brasileiro paga a tarifa de estrangeiro, "
         "S/ %d: 2,4 vezes." % (can, est)),
        ("O que é a taxa do SERNANP de Machu Picchu?",
         "É a tarifa de ingresso do órgão peruano de áreas protegidas, somada ao bilhete: S/ %d para estrangeiro e "
         "S/ %d para peruano, desde 1º de maio de 2026. A resolução no El Peruano registra quatro datas de início "
         "anteriores, de janeiro de 2024 a fevereiro de 2026. Quem chega pelo Caminho Inca não paga."
         % (sern_est, sern_nac)),
        ("Quanto custa subir a Huayna Picchu ou a Montanha Machu Picchu?",
         "Para peruano e andino, S/ %d, contra S/ %d dos circuitos. Para estrangeiro, guias de viagem citam S/ 200, "
         "valor que não achamos na imprensa nem em fonte oficial legível." % (mont, can)),
        ("Onde comprar a entrada de Machu Picchu?",
         "A venda online oficial é só pelo tuboleto.cultura.pe, do Ministério da Cultura. Há venda presencial em "
         "Aguas Calientes, no Centro Cultural de Machu Picchu Pueblo, das 15h às 22h, para o dia seguinte."),
    ]

    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">Brasileiro</span><span class="big c">S/ %d</span>'
        '<span class="sub">%s. Estudante: S/ %d.</span></div>'
        '<div class="pcel"><span class="rotp">Peruano e andino</span><span class="big">S/ %d</span>'
        '<span class="sub">%s. O brasileiro paga 2,4 vezes.</span></div>'
        '<div class="pcel"><span class="rotp">Taxa do SERNANP</span><span class="big">S/ %d</span>'
        '<span class="sub">Estrangeiro, desde 1º/5/2026. Peruano: S/ %d.</span></div>'
        '<div class="pcel"><span class="rotp">O brasileiro paga, ao todo</span><span class="big c">%s</span>'
        '<span class="sub">S/ %d, pela taxa de venda do BCB de 23/out.</span></div>'
        '</div>' % (est, reais(r_est), est_estud, can, reais(r_can), sern_est, sern_nac, reais(r_est + r_sern),
                    total_br))

    partes = abre_pagina(
        "A entrada para brasileiro", "O bilhete",
        "Machu Picchu para brasileiro: quanto custa a entrada",
        "O mesmo bilhete custa S/ %d ao peruano e ao andino e S/ %d ao brasileiro — e, desde maio, mais S/ %d de "
        "taxa ambiental. A tabela por passaporte, a montanha, a hora marcada e onde comprar." % (can, est, sern_est),
        figura, painel) + [
        '<section class="bloco"><div class="aviso a"><span class="t">O Brasil não é da Comunidade Andina</span>'
        '<p>A tarifa promocional de 2026 vale para peruanos, residentes e cidadãos dos países-membros da '
        'Comunidade Andina: <b>Bolívia, Colômbia, Equador e Peru</b>. O argentino, o chileno e o brasileiro pagam '
        'como qualquer estrangeiro. É o contrário do lado brasileiro das Cataratas do Iguaçu, onde o Mercosul paga '
        'como brasileiro.</p></div></section>\n\n',
        '<section class="bloco" id="tabela">\n  <div class="bloco-head"><span class="eyebrow">Por passaporte</span>'
        '<h2>Quem paga quanto pelo bilhete</h2><p>Circuitos 1, 2 e 3, sem montanha. Em real, pela taxa de venda do '
        'boletim de fechamento do Banco Central de 23/out/2026 (S/ 1 = R$ %s). A taxa do SERNANP vem à parte.</p>'
        '</div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Quem</th><th>Em sol</th><th>Em real</th><th>Fonte</th></tr>'
        '</thead><tbody>%s</tbody></table></div>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem"><span class="flag">Fontes divergem</span> a Infobae de '
        'novembro de 2025 dava US$ 60 ao adulto estrangeiro; os S/ %d são de fevereiro de 2026, e é o que usamos. '
        '<b>Por que não lemos a tabela oficial:</b> no tuboleto.cultura.pe ela aparece depois de uma verificação '
        '“não sou um robô”, que não fazemos.</p>\n</section>\n\n'
        % (("%.4f" % pen).replace(".", ","), tabela, est),
        '<section class="bloco" id="sernanp">\n  <div class="bloco-head"><span class="eyebrow">A taxa que entrou em '
        'maio</span><h2>SERNANP: S/ %d, adiada quatro vezes</h2></div>\n'
        '  <p style="color:var(--nevoa)">A <b>Resolução Diretoral 000006-2026-SERNANP/DUSRN</b>, publicada no El '
        'Peruano em 4/fev/2026, autoriza a tarifa de ingresso ao Santuário Histórico <i>“a partir del 01 de mayo '
        'de 2026”</i>. A mesma resolução lista as datas anteriores: <b>1º/1/2024, 1º/1/2025, 1º/1/2026 e '
        '1º/2/2026</b>.</p>\n'
        '  <p style="color:var(--nevoa)">%s<b>S/ %d para estrangeiro, S/ %d para peruano</b>, somados ao bilhete '
        '(El Comercio e Infobae, fev/2026). O valor não está no texto da resolução. Quem chega pelo Caminho Inca '
        'não paga.</p>\n'
        '  <ul class="plain"><li><b>Brasileiro</b>: S/ %d + S/ %d = <b>S/ %d</b> (%s).</li>'
        '<li><b>Peruano</b>: S/ %d + S/ %d = <b>S/ %d</b> (%s).</li></ul>\n</section>\n\n'
        % (sern_est, IMP, sern_est, sern_nac, est, sern_est, total_br, reais(r_est + r_sern), can, sern_nac,
           total_pe, reais(r_can + r_can_sern)),
        '<section class="bloco" id="montanha">\n  <div class="bloco-head"><span class="eyebrow">Circuitos e '
        'montanhas</span><h2>O que muda o preço dentro do sítio</h2></div>\n'
        '  <p style="color:var(--nevoa)">Desde 1º de junho de 2024 o sítio tem <b>três circuitos e 10 rotas</b> — '
        'Panorâmico, Clássico e Realeza (Ministério da Cultura). As rotas com montanha são a 1-A (Montanha Machu '
        'Picchu), a 3-A (Huayna Picchu) e a 3-C (Grande Caverna); <b>as rotas 1-C, 1-D, 3-C e 3-D só abrem na '
        'temporada alta</b> (Andina).</p>\n'
        '  <p style="color:var(--nevoa)">Para peruano e andino, a montanha custa <b>S/ %d</b> (reduzida S/ %d), '
        'contra S/ %d dos circuitos. %s<b>para estrangeiro, guias de viagem citam S/ 200</b>; não achamos o valor '
        'na imprensa nem em fonte oficial legível.</p>\n</section>\n\n' % (mont, mont_red, can, SEC),
        '<section class="bloco" id="comprar">\n  <div class="bloco-head"><span class="eyebrow">Na prática</span>'
        '<h2>Hora marcada, permanência e onde comprar</h2></div>\n'
        '  <ul class="plain"><li><b>Venda online só pelo tuboleto.cultura.pe</b>, do Ministério da Cultura.</li>'
        '<li><b>Hora exata de entrada</b>, e de 4 a 6 horas no sítio, conforme o percurso (Infobae, nov/2025).</li>'
        '<li><b>Venda presencial</b> no Centro Cultural de Machu Picchu Pueblo, em Aguas Calientes, das 15h às '
        '22h, <b>para o dia seguinte</b> — mil bilhetes por dia (Andina).</li>'
        '<li><b>Quantos entram</b>: 5.600 por dia na temporada alta e 4.500 no resto do ano. A alta de 2026: '
        '1º/1, 2 a 5/4, <b>19/6 a 2/11</b> e 30–31/12 (Andina).</li>'
        '<li><b>Horário de atenção</b>: todos os dias, 8h às 16h15 (página oficial).</li></ul>\n'
        '</section>\n\n',
        C.faq_html(perguntas, "a entrada de Machu Picchu"), "\n",
        C.continua(IRMAS, "de Machu Picchu", "entrada"),
        C.reserva(guia, SLUG, "em Cusco e Aguas Calientes", "entrada",
                  "O bilhete tem hora marcada: quem dorme em Aguas Calientes entra cedo e pode tentar a venda "
                  "presencial da véspera. "),
        '</div>\n',
    ]
    contas = " ".join([reais(v) for v in (r_est, r_sern, r_can, r_can_sern, r_est + r_sern, r_can + r_can_sern,
                                          round(est_estud * pen, 2), round(can_red * pen, 2))]
                      + [str(total_br), str(total_pe), "2,4", "200", _d.APURACAO])
    for q, a in perguntas:
        C.confere_numeros(a, FONTE + " " + contas, q)
    return pagina("entrada", titulo, descricao, img, alt,
                  [C.faq_ld(perguntas), C.migalhas(SLUG, NOME, "A entrada para brasileiro", url)], partes)


# ------------------------------------------------- os links no guia
def liga_no_guia(h):
    return C.liga_no_ponto(h, "boleto", "entrada/", "Página completa da entrada: a tabela por passaporte, a taxa "
                           "do SERNANP, a montanha e as perguntas frequentes")


def main(aplica):
    C.aplica_tudo((entrada,), ((GUIA, liga_no_guia),), GUIA, aplica)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
