# -*- coding: utf-8 -*-
"""Paginas derivadas de Lisboa: o molde do Rio, aplicado.

Plano em _build/docs/cluster-rio-2026-10-23.md ("Ordem e medicao"): se o
Rio rendesse, o mesmo molde - pagina do ponto principal, o que fecha cada
dia, descontos - passava para Lisboa. Comecou em 23/out/2026.

  /destinos/lisboa/palacio-da-pena/        o ponto principal (1,9 milhao
                                            de visitantes em 2025)
  /destinos/lisboa/o-que-fecha-cada-dia/
  /destinos/lisboa/descontos/

DE ONDE SAI TUDO: das fichas de g1.py ... g4.py, importadas, e dos avisos
publicados no guia. A mecanica (cabeca emprestada da ficha de custos, FAQ,
Continue, Booking, foto, trava de numero) e a do _build/cluster/comum.py,
a mesma do Rio.

Uso
---
    python _build/lisboa/paginas.py            # so mostra
    python _build/lisboa/paginas.py --aplica   # escreve

Depois, a cadeia de busca do LEIA-ME (sitemap, schema, adsense, drive,
confere). Regerar desfaz o que a cadeia pos.
"""
import html as H
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), "cluster"))

import comum as C  # noqa: E402
from comum import le, limpa, acha, junta, minuscula, ld, faq_ld, SITE, SOBE, RAIZ  # noqa: E402
from g1 import G1  # noqa: E402
from g2 import G2  # noqa: E402
from g3 import G3  # noqa: E402
from g4 import G4  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SLUG = "lisboa"
GUIA = os.path.join(RAIZ, "destinos", SLUG, "index.html")
MOLDE = os.path.join(RAIZ, "destinos", SLUG, "quanto-custa", "index.html")
CREDITOS = os.path.join(AQUI, "creditos.json")
GRUPOS = [G1, G2, G3, G4]
PONTOS = {p["id"]: p for g in GRUPOS for p in g["pontos"]}

IRMAS = [
    ("", "Guia dos 16 pontos turísticos"),
    ("palacio-da-pena/", "Palácio da Pena: ingresso e hora marcada"),
    ("o-que-fecha-cada-dia/", "O que abre e fecha em cada dia"),
    ("descontos/", "Descontos e dias grátis"),
    ("quanto-custa/", "Quanto custa 6 dias em Lisboa"),
    ("roteiro-6-dias/", "Roteiro de 6 dias"),
    ("quanto-custa/#calculadora", "Calculadora da viagem"),
]


def ficha(pid, campo):
    return PONTOS[pid]["campos"][campo]


def continua(atual):
    return C.continua(IRMAS, "de Lisboa", atual)


def reserva(guia, sid, frase):
    return C.reserva(guia, SLUG, "em Lisboa", sid, frase)


def capa_de(img_id):
    return C.capa_de(CREDITOS, SLUG, img_id)


def abre_pagina(migalha, eyebrow, h1, lead, capa, painel=""):
    return [
        '<main id="conteudo">\n<div class="faixa"><div class="wrap wrap-estreito">\n',
        '<p class="migalhas"><a href="%s">Início</a> › <a href="../../">Destinos</a> › '
        '<a href="../">Lisboa</a> › %s</p>\n' % (SOBE, migalha),
        '<div class="hero">\n  <span class="eyebrow">%s</span>\n  <h1>%s</h1>\n  <p>%s</p>\n%s</div>\n'
        % (eyebrow, h1, lead, C.assinatura()),
        capa, "\n", painel, '\n<div style="height:clamp(1.4rem,3vw,2.2rem)"></div>\n</div></div>\n\n',
        '<div class="wrap wrap-estreito">\n',
    ]


def pagina(pasta, titulo, descricao, img, alt, blocos_ld, partes, fim_pe=""):
    url = "%s/destinos/%s/%s/" % (SITE, SLUG, pasta)
    cabeca, pe = C.esqueleto(MOLDE, titulo, descricao, url, img, alt)
    cabeca = cabeca.replace("</head>", "".join(ld(b) for b in blocos_ld) + "</head>", 1)
    if fim_pe:
        pe = pe.replace("<!-- consentimento:inicio -->", fim_pe + "\n<!-- consentimento:inicio -->", 1)
    return os.path.join(RAIZ, "destinos", SLUG, pasta, "index.html"), cabeca + "".join(partes) + pe


def euros(t):
    """'€ 1,72' -> 1.72"""
    return float(t.replace(".", "").replace(",", "."))


# --------------------------------------------------------- Palácio da Pena
def pena(guia):
    pid = "palacio-da-pena"
    c = PONTOS[pid]["campos"]
    url = "%s/destinos/%s/%s/" % (SITE, SLUG, pid)
    valor = limpa(c["Valor da entrada"])
    m = acha(r"Visita Essencial: € (\d+) adulto de (\d+) a (\d+).*?€ (\d+) jovem de (\d+) a (\d+) e sénior a partir "
             r"de (\d+), € (\d+) a família de dois adultos e dois jovens\. Visita Total: € (\d+) adulto\. Só o "
             r"Parque: € (\d+)\. Há ainda Visita Guiada a € (\d+) e Visita Encenada a € (\d+)", valor, "os bilhetes da Pena")
    ess, a_de, a_ate, jov, j_de, j_ate, sen, fam, total, parque, guiada, encenada = m.groups()
    real = acha(r"€ %s adulto de %s a %s \(≈ (R\$ \d+)\)" % (ess, a_de, a_ate), valor, "o real da Essencial").group(1)
    circuito = acha(r"hop-on hop-off a € (\d+,\d+) por dia", valor, "o circuito interno").group(1)
    card = acha(r"(Lisboa Card: só 10% de desconto para adulto)", valor, "o Lisboa Card").group(1)
    gratis_res = acha(r"(Gratuito para residentes em Portugal aos domingos e feriados), cerca de (\d+) dias por ano",
                      valor, "a gratuidade de residente").group(2)
    dias = limpa(c["Dias em que não funciona"])
    p_abre, p_fecha, p_ult = acha(r"Parque das (\d+h) às (\d+h), com último bilhete às (\d+h)", dias, "o parque").groups()
    pl_abre, pl_fecha, pl_ult = acha(r"Palácio das (\d+h\d*) às (\d+h\d*), com último bilhete às (\d+h\d*)", dias,
                                     "o palacio").groups()
    acha(r"(“não existe tolerância de atraso”)", dias, "a regra da tolerancia")
    lotacao = acha(r"A lotação é de ([\d.]+) visitantes por dia", limpa(c["Visitantes por ano"]), "a lotacao").group(1)
    metro = limpa(c["Metrô mais próximo"])
    margem = acha(r"manda contar cerca de (\d+) minutos entre um e outro", metro, "a margem portao-palacio").group(1)
    bus, bus_preco = acha(r"autocarro (\d+), o “Circuito da Pena”.*?Bilhete diário € (\d+,\d+)", metro, "o 434").groups()
    comboio = acha(r"(comboio, na Linha de Sintra, partindo do Rossio), em (\d+) a (\d+) minutos", metro, "o comboio")
    visitantes = acha(r"([\d,]+ milhão de visitantes em 2025)", limpa(c["Visitantes por ano"]), "os visitantes").group(1)

    produtos = [
        ("Visita Essencial", "€ %s" % ess,
         "Palácio e parque. Jovem de %s a %s e sénior a partir de %s: € %s. Família de dois adultos e dois jovens: "
         "€ %s." % (j_de, j_ate, sen, jov, fam)),
        ("Visita Total", "€ %s" % total, "Adulto."),
        ("Só o Parque", "€ %s" % parque, "Sem o interior do palácio."),
        ("Visita Guiada", "€ %s" % guiada, ""),
        ("Visita Encenada", "€ %s" % encenada, ""),
    ]
    C.confere_numeros(" ".join(" ".join(p) for p in produtos), valor, "a tabela da Pena")
    tabela = "".join('<tr><td><b>%s</b></td><td class="n">%s</td><td>%s</td></tr>' % (n, v, o or "—")
                     for n, v, o in produtos)

    titulo = "Palácio da Pena: ingresso, os cinco bilhetes e a hora marcada sem tolerância"
    descricao = ("Ingresso do Palácio da Pena de € %s a € %s: Visita Essencial € %s, Total € %s, só o parque € %s. "
                 "Hora marcada sem tolerância, como chegar de Lisboa e quando fecha. Apurado em 13/set/2026."
                 % (ess, encenada, ess, total, parque))
    capa, img, alt = capa_de(PONTOS[pid]["img"])

    perguntas = [
        ("Quanto custa o ingresso do Palácio da Pena?",
         "A Visita Essencial, a mais comum, custa € %s para adulto de %s a %s anos (%s) e € %s para jovem de %s a "
         "%s e sénior a partir de %s. Só o parque custa € %s; a Visita Total, € %s." % (
             ess, a_de, a_ate, real, jov, j_de, j_ate, sen, parque, total)),
        ("O Palácio da Pena tem tolerância de atraso?",
         "Não. O texto oficial diz que “não existe tolerância de atraso”: perdeu a hora, perdeu o bilhete, sem "
         "reembolso. E a hora marca a entrada no interior do palácio, não no portão: conte cerca de %s minutos entre "
         "um e outro." % margem),
        ("Como ir de Lisboa ao Palácio da Pena?",
         "De %s, em %s a %s minutos, e da estação de Sintra o autocarro %s, o Circuito da Pena, com bilhete diário "
         "de € %s. De carro particular não se chega ao palácio." % (comboio.group(1), comboio.group(2),
                                                                    comboio.group(3), bus, bus_preco)),
        ("O Palácio da Pena é grátis algum dia?",
         "Só para quem mora em Portugal: residentes entram de graça aos domingos e feriados, cerca de %s dias por "
         "ano, na bilheteira e com documento. Para o turista não há dia grátis." % gratis_res),
        ("O Lisboa Card dá entrada no Palácio da Pena?",
         "Não dá entrada livre: dá 10%% de desconto para adulto, segundo as fontes consultadas, que divergem entre "
         "si."),
    ]
    C.confere_numeros(card, valor, "o Lisboa Card")

    atracao = {"@context": "https://schema.org", "@type": "TouristAttraction", "name": "Palácio Nacional da Pena",
               "url": url, "image": img, "description": limpa(c["Fatos históricos"])[:300],
               "isAccessibleForFree": False, "publicAccess": True,
               "address": {"@type": "PostalAddress", "streetAddress": "Estrada da Pena",
                           "postalCode": "2710-609", "addressLocality": "Sintra", "addressCountry": "PT"},
               "offers": [{"@type": "Offer", "name": n, "price": "%s.00" % v.split()[-1], "priceCurrency": "EUR",
                           "url": url + "#precos"} for n, v, _ in produtos]}
    if "Estrada da Pena, 2710-609 Sintra" not in limpa(c["Endereço"]):
        sys.exit("PARADO: o endereco da Pena mudou")
    g = C.coords("lisboa", pid)
    if g:
        atracao["geo"] = {"@type": "GeoCoordinates", "latitude": g[0], "longitude": g[1]}

    painel = (
        '<div class="painel">'
        '<div class="pcel"><span class="rotp">Visita Essencial, adulto</span><span class="big c">€ %s</span>'
        '<span class="sub">%s. Palácio e parque.</span></div>'
        '<div class="pcel"><span class="rotp">Só o parque</span><span class="big">€ %s</span>'
        '<span class="sub">Sem o interior do palácio.</span></div>'
        '<div class="pcel"><span class="rotp">Tolerância de atraso</span><span class="big c">Zero</span>'
        '<span class="sub">Conte %s minutos do portão ao palácio.</span></div>'
        '<div class="pcel"><span class="rotp">Teto diário</span><span class="big">%s</span>'
        '<span class="sub">Visitantes por dia. Quando enche, acabou.</span></div>'
        '</div>' % (ess, real, parque, margem, lotacao))

    import sv
    botao = sv.botao(pid)          # vazio quando o ponto nao tem panorama aprovado
    partes = abre_pagina(
        "Palácio da Pena", "Ingresso e hora marcada",
        "Palácio da Pena: ingresso, os cinco bilhetes e a hora marcada",
        "São cinco produtos com nomes parecidos, de € %s a € %s, e um relógio que não perdoa: a hora do bilhete "
        "vale para o interior do palácio, sem tolerância. O que cada bilhete inclui, como chegar de Lisboa e quando "
        "a serra fecha. Preços consultados em 13/set/2026." % (ess, encenada),
        capa, painel) + [
        '<section class="bloco"><div class="aviso a"><span class="t">A hora marcada é do palácio, não do portão'
        '</span><p>%s</p></div></section>\n\n' % (
            "Parque das %s às %s, com último bilhete às %s; palácio das %s às %s, com último bilhete às %s. "
            "<b>Não existe tolerância de atraso</b>, nas palavras da Parques de Sintra, e a casa manda contar cerca "
            "de <b>%s minutos</b> entre o portão e o interior. Se a sua hora é 14h, esteja no portão às 13h30."
            % (p_abre, p_fecha, p_ult, pl_abre, pl_fecha, pl_ult, margem)),
        C.campo("Os cinco bilhetes", "precos", "Preço por pessoa",
                '<div class="tabwrap"><table><thead><tr><th>Bilhete</th><th>Adulto</th><th>Outras faixas</th></tr>'
                '</thead><tbody>%s</tbody></table></div>\n  %s' % (tabela, C.paragrafos(c["Valor da entrada"]))),
        C.campo("Como chegar de Lisboa", "como-chegar", "Comboio, autocarro e a pé",
                C.paragrafos(c["Metrô mais próximo"]) + C.paragrafos(c["Endereço"]), botao),
        C.campo("Horários e quando a serra fecha", "horarios", "Antes de sair", C.paragrafos(c["Dias em que não funciona"])),
        C.campo("Quando ir", "quando-ir", "Clima e movimento", C.paragrafos(c["Menor visitação e temperatura"])),
        C.campo("O palácio", "palacio", "História e números",
                C.paragrafos(c["Fatos históricos"]) + C.paragrafos(c["Visitantes por ano"]) + c["Curiosidades"]
                + C.paragrafos(c["Pontos de referência"])),
        C.campo("Perto dali", "perto", "Para emendar", C.paragrafos(c["Pontos turísticos próximos"])),
        C.faq_html(perguntas, "o Palácio da Pena"), "\n",
        continua(pid),
        reserva(guia, "pena", "O bilhete da Pena compre no site oficial da Parques de Sintra, com a hora certa. "),
        '</div>\n',
    ]
    if visitantes not in limpa(c["Visitantes por ano"]):
        sys.exit("PARADO: visitantes")
    return pagina(pid, titulo, descricao, img, alt,
                  [atracao, faq_ld(perguntas), C.migalhas(SLUG, "Lisboa", "Palácio da Pena", url)], partes,
                  ('<script src="%sassets/js/streetview.js" defer></script>' % SOBE) if botao else "")


# ------------------------------------------------- O que fecha cada dia
# Como no Rio: a leitura de cada ficha, e as PROVAS que precisam estar no
# campo "Dias em que nao funciona". Em Lisboa os feriados de fecho sao
# datas, e cada casa tem o seu calendario; por isso nao ha coluna
# "feriado": as datas saem da ficha (regex `datas`) e vao numa lista.
DIAS = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
NOME_DIA = {"seg": "Segunda-feira", "ter": "Terça-feira", "qua": "Quarta-feira", "qui": "Quinta-feira",
            "sex": "Sexta-feira", "sab": "Sábado", "dom": "Domingo"}
CURTO = {"seg": "Seg", "ter": "Ter", "qua": "Qua", "qui": "Qui", "sex": "Sex", "sab": "Sáb", "dom": "Dom"}
TODOS = {d: ("fecha", "fechado sem data de reabertura") for d in DIAS}

CALENDARIO = {
 "mosteiro-jeronimos": ({"seg": ("fecha", "")}, ["Fecha às segundas-feiras"], r"Fecha também em (.*?)\.", ""),
 "torre-de-belem": ({"seg": ("fecha", "")}, ["Fecha às segundas-feiras"], r"Fecha às segundas-feiras, mais (.*?)\.",
                    "teto de 900 visitantes por dia"),
 "padrao-descobrimentos": ({}, ["Não há fecho semanal: abre todos os dias"], r"Encerra em (.*?)\.", ""),
 "museu-dos-coches": ({"seg": ("fecha", "")}, ["Fecha às segundas-feiras"], r"Fecha às segundas-feiras, mais (.*?)\.",
                      "o Picadeiro Real está fechado para obras"),
 "castelo-sao-jorge": ({}, ["Não há fecho semanal — abre todos os dias"], r"Encerra em (.*?);",
                       "os adarves e torres fecham antes do monumento"),
 "elevador-santa-justa": (TODOS, ["não funciona nenhum dia"], None, ""),
 "praca-do-comercio": ({}, ["A praça não fecha"], None, "a subida ao arco tem horário, e as fontes divergem"),
 "miradouros-alfama": ({}, ["Não há dia de fecho"], None, ""),
 "eletrico-28": ({}, ["Não há fecho semanal"], None, "o percurso está cortado: só circula entre Graça e Prazeres"),
 "gulbenkian": ({"ter": ("fecha", "as galerias; o jardim abre")}, ["Fecha às terças-feiras", "aberto todos os dias"],
                r"Fecha também em (.*?)\.", ""),
 "oceanario": ({}, ["Abre todos os dias do ano", "não há feriado de encerramento"], None, ""),
 "time-out-market": ({}, ["Abre todos os dias"], None, "as páginas oficiais divergem no horário da noite"),
 "palacio-da-pena": ({}, ["Não há fecho semanal"], None, "fecha com risco de incêndio ou mau tempo"),
 "quinta-da-regaleira": ({}, ["Não há fecho semanal"], r"Encerra em (.*?)\.", ""),
 "castelo-dos-mouros": ({}, ["Não há fecho semanal"], None, "fecha com risco de incêndio ou mau tempo"),
 "cabo-da-roca": ({}, ["O cabo em si não fecha"], r"(Encerra no Natal e no Ano Novo)", "o farol fecha às 17h30"),
}
ROTULO = {"abre": "Abre", "fecha": "Fecha", "parcial": "Em parte"}


def que_fecha(guia):
    pontos = [p for g in GRUPOS for p in g["pontos"]]
    if set(CALENDARIO) != set(PONTOS):
        sys.exit("PARADO: CALENDARIO e fichas divergem: %s" % sorted(set(CALENDARIO) ^ set(PONTOS)))
    feriados = []
    for p in pontos:
        regras, provas, rx, nota = CALENDARIO[p["id"]]
        texto = limpa(p["campos"]["Dias em que não funciona"])
        for pr in provas:
            if pr not in texto:
                sys.exit("PARADO: a ficha de %s nao diz mais '%s'" % (p["id"], pr))
        if nota:
            C.confere_numeros(nota, texto + " " + limpa(p["campos"]["Visitantes por ano"]), p["id"])
        if rx:
            feriados.append((p, acha(rx, texto, "os feriados de " + p["id"]).group(1)))
    aviso = acha(r"(?s)O calendário de fechos.*?</(?:details|div)>", guia, "o aviso do calendario").group(0)
    for pr in ("Jerónimos, Torre de Belém e Museu dos Coches fecham todos", "Terça-feira mata o Gulbenkian"):
        if pr not in limpa(aviso):
            sys.exit("PARADO: o aviso do guia nao diz mais '%s'" % pr)
    data_ap = acha(r"Preços verificados em (\d+ de \w+ de \d{4})", guia, "a data do guia").group(1)

    def estado(pid, d):
        return CALENDARIO[pid][0].get(d, ("abre", ""))

    def item(p, n):
        return '<a href="../#%s">%s</a>%s' % (p["id"], H.escape(p["nome"]), (" — " + n) if n else "")

    def do_dia(d):
        return ([(p, estado(p["id"], d)[1]) for p in pontos if estado(p["id"], d)[0] == "fecha"
                 and p["id"] != "elevador-santa-justa"])

    belem = [p for p in G1["pontos"]]
    dias_belem = [d for d in DIAS if all(estado(p["id"], d)[0] == "abre" for p in belem)]
    sempre_fechado = PONTOS["elevador-santa-justa"]["nome"]
    secoes = []
    for d in DIAS:
        fecha = do_dia(d)
        abre = len(pontos) - len(fecha) - 1
        li = []
        li.append(("<li><b>Fecha:</b> %s.</li>" % "; ".join(item(p, n) for p, n in fecha)) if fecha
                  else "<li>Nenhum dos pontos do guia fecha neste dia.</li>")
        li.append("<li><b>Abrem:</b> %d dos %d pontos. O %s segue fechado todos os dias.</li>"
                  % (abre, len(pontos), sempre_fechado))
        if d == "seg":
            li.append("<li>Em Belém, só o <a href=\"../#padrao-descobrimentos\">Padrão dos Descobrimentos</a> abre."
                      "</li>")
        if d == "ter":
            li.append("<li>O plano B da terça é o <a href=\"../#oceanario\">Oceanário</a>, que abre todos os dias "
                      "do ano.</li>")
        secoes.append('<section class="bloco" id="%s">\n  <div class="bloco-head"><h2>%s</h2></div>\n'
                      '  <ul class="plain">%s</ul>\n</section>\n\n' % (d, NOME_DIA[d], "".join(li)))

    def celula(pid, d):
        e, nota = estado(pid, d)
        tit = (' title="%s"' % H.escape(nota, quote=True)) if nota else ""
        if e == "abre":
            return '<td class="n" style="color:var(--nevoa)">Abre</td>'
        return '<td class="n"%s><b style="color:var(--ambar)">%s</b></td>' % (tit, ROTULO[e])
    cab = "".join("<th>%s</th>" % CURTO[d] for d in DIAS)
    linhas = "".join('<tr><td><a href="../#%s">%s</a></td>%s</tr>'
                     % (p["id"], H.escape(p["nome"]), "".join(celula(p["id"], d) for d in DIAS)) for p in pontos)
    lista_feriados = "".join("<li>%s: %s.</li>" % (item(p, ""), H.escape(f)) for p, f in feriados)
    ressalvas = "".join("<li>%s — %s.</li>" % (item(p, ""), CALENDARIO[p["id"]][3]) for p in pontos
                        if CALENDARIO[p["id"]][3])

    sem_fecho = [d for d in DIAS if not do_dia(d)]
    if [DIAS.index(d) for d in sem_fecho] != list(range(DIAS.index(sem_fecho[0]), DIAS.index(sem_fecho[-1]) + 1)):
        sys.exit("PARADO: os dias sem fecho nao sao seguidos: %s" % sem_fecho)
    faixa = "De %s a %s" % (NOME_DIA[sem_fecho[0]].split("-")[0].lower(), NOME_DIA[sem_fecho[-1]].split("-")[0].lower())
    abrem_seg = ["castelo-sao-jorge", "oceanario", "gulbenkian", "palacio-da-pena", "quinta-da-regaleira",
                 "castelo-dos-mouros"]
    if any(estado(x, "seg")[0] != "abre" for x in abrem_seg):
        sys.exit("PARADO: a lista do que abre na segunda mudou")
    seg = [p["nome"] for p, _ in do_dia("seg")]
    ter = [p["nome"] for p, _ in do_dia("ter")]
    titulo = "O que abre e o que fecha em Lisboa em cada dia da semana"
    descricao = ("Segunda fecham %s; terça, o %s. O calendário dos 16 pontos de Lisboa e Sintra, dia a dia, e os "
                 "feriados de cada um. Horários apurados em %s." % (junta(seg), junta(ter), data_ap))
    capa, img, alt = capa_de("jeronimos")
    perguntas = [
        ("O que fecha na segunda-feira em Lisboa?",
         "%s. Em Belém, só o Padrão dos Descobrimentos abre. Fora de Belém, Castelo de São Jorge, Oceanário, "
         "Gulbenkian e Sintra abrem." % junta(seg)),
        ("O que fecha na terça-feira em Lisboa?",
         "As galerias do %s; o jardim continua aberto. O Oceanário, que abre todos os dias do ano, é o plano B."
         % junta(ter)),
        ("Qual o melhor dia para visitar Belém?",
         "De terça a domingo os quatro monumentos de Belém abrem. Na segunda, %s fecham." % junta(seg)),
        ("O que abre no feriado em Lisboa?",
         "Depende da casa: cada uma tem o seu calendário. O Oceanário não tem feriado de encerramento; Jerónimos, "
         "Torre e Coches fecham em 1 de janeiro, domingo de Páscoa, 1 de maio, 13 de junho e 25 de dezembro. A "
         "lista de cada ponto está nesta página."),
    ]
    for p, f in feriados:
        if p["id"] == "mosteiro-jeronimos" and "13 de junho" not in f:
            sys.exit("PARADO: o 13 de junho saiu da ficha dos Jeronimos")

    partes = abre_pagina(
        "O que fecha cada dia", "Calendário da semana",
        "O que abre e o que fecha em Lisboa em cada dia da semana",
        "Os 16 pontos do guia, de Belém a Sintra, dia por dia, e os feriados em que cada um fecha. Em Lisboa a "
        "segunda-feira é que estraga o roteiro. Horários apurados em %s." % data_ap, capa) + [
        '<section class="bloco"><div class="aviso a"><span class="t">O resumo</span>'
        '<p><b>Segunda-feira:</b> fecham %s. <b>Terça-feira:</b> fecham as galerias do %s. %s, '
        'nenhum dos pontos do guia fecha.</p><p>O %s não funciona em dia nenhum.</p></div></section>\n\n'
        % (junta(seg), junta(ter), faixa, sempre_fechado),
        '<section class="bloco">\n  <div class="bloco-head"><span class="eyebrow">Ir para o dia</span>'
        '<h2>Dia por dia</h2></div>\n  <p class="idx-gratis">%s</p>\n</section>\n\n'
        % " · ".join('<a href="#%s">%s</a>' % (d, CURTO[d]) for d in DIAS),
    ] + secoes + [
        '<section class="bloco" id="tabela">\n  <div class="bloco-head"><span class="eyebrow">Os 16 pontos</span>'
        '<h2>A semana inteira numa tabela</h2></div>\n'
        '  <div class="tabwrap"><table><thead><tr><th>Ponto</th>%s</tr></thead><tbody>%s</tbody></table></div>\n'
        '</section>\n\n' % (cab, linhas),
        '<section class="bloco" id="feriados">\n  <div class="bloco-head"><span class="eyebrow">Datas</span>'
        '<h2>Os feriados em que cada um fecha</h2></div>\n  <ul class="plain">%s</ul>\n'
        '  <p style="color:var(--nevoa);font-size:.9rem">Os outros pontos não publicam feriado de encerramento, ou '
        'não fecham. Pena e Castelo dos Mouros: a lista de feriados não foi encontrada.</p>\n</section>\n\n'
        % lista_feriados,
        '<section class="bloco" id="em-qualquer-dia">\n  <div class="bloco-head"><span class="eyebrow">Fora do '
        'calendário</span><h2>O que pode fechar em qualquer dia</h2></div>\n  <ul class="plain">%s</ul>\n'
        '</section>\n\n' % ressalvas,
        C.faq_html(perguntas, "o que fecha em Lisboa"), "\n",
        continua("o-que-fecha-cada-dia"),
        reserva(guia, "o-que-fecha", ""),
        '</div>\n',
    ]
    url = "%s/destinos/%s/o-que-fecha-cada-dia/" % (SITE, SLUG)
    if dias_belem != DIAS[1:]:
        sys.exit("PARADO: os dias de Belem mudaram: %s" % dias_belem)
    return pagina("o-que-fecha-cada-dia", titulo, descricao, img, alt,
                  [faq_ld(perguntas), C.migalhas(SLUG, "Lisboa", "O que fecha cada dia", url)], partes)


# --------------------------------------------------------------- Descontos
# Mesma trava do Rio: todo numero do texto precisa estar no campo "Valor da
# entrada" da ficha do ponto.
DESCONTOS = {
 "morar": [
  ("mosteiro-jeronimos", "Quem mora em Portugal tem o Acesso 52: 52 entradas gratuitas por ano nos monumentos do "
                         "Estado, com Cartão de Cidadão, só na bilheteira física. Para quem não mora, não há dia "
                         "grátis."),
  ("palacio-da-pena", "Residentes em Portugal entram de graça aos domingos e feriados, cerca de 60 dias por ano, na "
                      "bilheteira, no dia, com documento."),
  ("castelo-dos-mouros", "A mesma regra da Parques de Sintra: grátis para residentes em Portugal aos domingos e "
                         "feriados, na bilheteira."),
  ("padrao-descobrimentos", "Residentes no concelho de Lisboa entram de graça aos domingos e feriados até às 14h. É "
                            "recorte municipal, mais estreito que morar em Portugal."),
  ("quinta-da-regaleira", "Munícipes de Sintra entram de graça. Mas a Regaleira não participa do domingo grátis para "
                          "residentes em Portugal: no domingo paga-se os € 20."),
  ("castelo-sao-jorge", "Acabou a gratuidade para morador de Lisboa, que valia desde 2005: desde 3 de julho de 2025 o "
                        "lisboeta paga os mesmos € 17."),
 ],
 "dia": [
  ("gulbenkian", "Grátis aos domingos a partir das 14h, para todos."),
  ("oceanario", "Não há dia grátis, mas a faixa das 16h é a mais barata: € 25 o adulto, contra € 29 entre 10h e "
                "11h30."),
  ("eletrico-28", "Pagando a bordo, € 3,30; com saldo no cartão Navegante Ocasional, que custa € 0,50 uma vez, "
                  "€ 1,72."),
  ("castelo-dos-mouros", "Comprando dois monumentos da Parques de Sintra juntos, 5% de desconto. O combinado “Viver "
                         "Sintra: Palácios Reais”, a € 42, junta Pena, Palácio Nacional de Sintra e o transporte de "
                         "24 horas, contra € 46,50 avulso."),
 ],
 "meia": [
  ("mosteiro-jeronimos", "Criança até 12 anos não paga. Jovem de 13 a 24 e sénior a partir de 65 pagam metade: € 9."),
  ("torre-de-belem", "As mesmas faixas da rede do Estado: grátis até 12 anos; € 7,50 para jovem de 13 a 24 e "
                     "sénior a partir de 65."),
  ("padrao-descobrimentos", "Inteira € 10; jovem de 13 a 25 não residente em Lisboa, € 5; sénior a partir de 65 não "
                            "residente, € 8,50."),
  ("castelo-sao-jorge", "Criança até 12 anos não paga; jovem de 13 a 25, € 8,50; sénior a partir de 65, € 14."),
  ("palacio-da-pena", "Jovem de 6 a 17 e sénior a partir de 65, € 18; família de dois adultos e dois jovens, € 65; "
                      "pessoa com deficiência, 50%."),
  ("quinta-da-regaleira", "Jovem de 6 a 17 e sénior a partir de 65, € 15; criança até 5 anos não paga; família, € 60."),
  ("gulbenkian", "Grátis para menores de 18 anos. Menores de 30 têm 25% e maiores de 65, 10%; com o Cartão "
                 "Gulbenkian, de adesão gratuita, os menores de 30 pagam metade."),
  ("oceanario", "Criança de 3 a 12, de € 15 a € 17 conforme a hora; sénior, de € 17 a € 19; até 2 anos não paga."),
 ],
}
GRUPO_DESC = {
 "morar": ("onde-voce-mora", "Morar em Portugal, ou em Lisboa, muda o preço",
           "Quase toda gratuidade de Lisboa é para residente. Para o turista brasileiro, este bloco é sobretudo "
           "o que não vale."),
 "dia": ("dia-e-jeito", "O dia, a hora e o jeito de pagar", "O mesmo ponto, mais barato por causa da hora, do "
         "cartão de transporte ou do combinado."),
 "meia": ("meia-e-gratuidade", "Criança, jovem e sénior", "Em Portugal, sénior é a partir dos 65 e as faixas "
          "de jovem mudam de casa para casa. Todos pedem documento."),
}


def descontos(guia):
    for grupo, itens in DESCONTOS.items():
        for pid, texto in itens:
            C.confere_numeros(texto, ficha(pid, "Valor da entrada"), "%s, %s" % (pid, grupo))
    data_ap = acha(r"Preços verificados em (\d+ de \w+ de \d{4})", guia, "a data do guia").group(1)
    card = acha(r'(?s)<(?:span|summary) class="t">O Lisboa Card compensa a partir de duas entradas por dia'
                r'</(?:span|summary)>(.*?)</(?:div|details)>',
                guia, "o aviso do Lisboa Card").group(1)
    card_precos = acha(r"<b>24h € (\d+), 48h € (\d+), 72h € (\d+)</b>", card, "os precos do Lisboa Card").groups()
    gratis = [p for p in PONTOS.values() if re.match(r"gr[aá]tis", limpa(p["preco"]), re.I)]

    def item(pid, texto):
        return '<li><a href="../#%s"><b>%s</b></a>: %s</li>' % (pid, H.escape(PONTOS[pid]["nome"]), texto)
    secoes = []
    for grupo in ("morar", "dia", "meia"):
        sid, h2, intro = GRUPO_DESC[grupo]
        secoes.append('<section class="bloco" id="%s">\n  <div class="bloco-head"><h2>%s</h2><p>%s</p></div>\n'
                      '  <ul class="plain">%s</ul>\n</section>\n\n'
                      % (sid, h2, intro, "".join(item(pid, t) for pid, t in DESCONTOS[grupo])))

    titulo = "Lisboa: descontos, dias grátis e o Lisboa Card, ponto por ponto"
    descricao = ("Onde o turista paga menos em Lisboa e Sintra: Gulbenkian grátis aos domingos à tarde, Oceanário "
                 "mais barato às 16h, criança grátis até 12 anos nos monumentos e quando o Lisboa Card (€ %s, € %s e "
                 "€ %s) compensa. Apurado em %s." % (card_precos + (data_ap,)))
    capa, img, alt = capa_de("castelo")
    d = dict(DESCONTOS["dia"])
    perguntas = [
        ("Tem dia grátis nos monumentos de Lisboa?",
         "Para quem não mora em Portugal, não nos monumentos do Estado: o domingo de manhã grátis acabou e virou o "
         "Acesso 52, só para residentes. O que vale para todos: o Gulbenkian, grátis aos domingos a partir das 14h."),
        ("Criança paga nos monumentos de Lisboa?",
         "Nos monumentos do Estado (Jerónimos, Torre de Belém, Coches) e no Castelo de São Jorge, criança até 12 "
         "anos não paga. No Gulbenkian, menores de 18 não pagam."),
        ("O Lisboa Card vale a pena?",
         "Custa € %s (24h), € %s (48h) e € %s (72h) e inclui o transporte. Pela conta do guia, o de 24h compensa a "
         "partir de duas entradas no dia. Mas Oceanário, Pena e Regaleira não são grátis com ele: dão só "
         "desconto." % card_precos),
        ("Qual a hora mais barata do Oceanário?",
         d["oceanario"]),
    ]
    acha(r"(Oceanário, Pena e Regaleira — não são grátis com o cartão)", limpa(card), "a ressalva do cartao")

    partes = abre_pagina(
        "Descontos", "Quem paga menos",
        "Descontos e dias grátis em Lisboa",
        "Gratuidade de residente, dia e hora mais baratos, faixas de criança, jovem e sénior, e a conta do Lisboa "
        "Card, nos pontos pagos do guia. Cada linha leva à ficha do ponto, com a fonte. Preços apurados em %s."
        % data_ap, capa) + secoes + [
        '<section class="bloco" id="lisboa-card">\n  <div class="bloco-head"><span class="eyebrow">O cartão'
        '</span><h2>Quando o Lisboa Card compensa</h2></div>\n  %s\n</section>\n\n' % card.strip(),
        '<section class="bloco" id="sem-ingresso">\n  <div class="bloco-head"><h2>Os %d pontos que não cobram '
        'entrada</h2></div>\n  <p style="color:var(--nevoa)">%s. O que cada um cobra à parte está na '
        '<a href="../../../gratis/#lisboa">lista dos pontos gratuitos</a>.</p>\n</section>\n\n'
        % (len(gratis), junta([p["nome"] for p in gratis])),
        C.faq_html(perguntas, "descontos em Lisboa"), "\n",
        continua("descontos"),
        reserva(guia, "descontos", "Leve o documento de cada desconto: sem ele, a bilheteira cobra a inteira. "),
        '</div>\n',
    ]
    url = "%s/destinos/%s/descontos/" % (SITE, SLUG)
    return pagina("descontos", titulo, descricao, img, alt,
                  [faq_ld(perguntas), C.migalhas(SLUG, "Lisboa", "Descontos", url)], partes)


# ------------------------------------------------- os links no guia
def liga_no_guia(h):
    for href, rot in (("palacio-da-pena/", "Palácio da Pena: ingresso e hora marcada"),
                      ("o-que-fecha-cada-dia/", "O que abre e fecha em cada dia"),
                      ("descontos/", "Descontos e dias grátis")):
        h = C.liga_na_lista(h, "de Lisboa", href, rot)
    if 'href="palacio-da-pena/">Página completa' not in h:
        mais = ('\n  <p class="foto-nota"><a href="palacio-da-pena/">Página completa do Palácio da Pena: os cinco '
                'bilhetes, a hora marcada e as perguntas frequentes</a></p>')
        h = re.sub(r'(<article class="ponto" id="palacio-da-pena">.*?)(\n</article>)',
                   lambda m: m.group(1) + mais + m.group(2), h, count=1, flags=re.S)
    if 'href="o-que-fecha-cada-dia/">A tabela' not in h:
        mais = '<p><a href="o-que-fecha-cada-dia/">A tabela da semana inteira, com os 16 pontos e os feriados</a>.</p>'
        h = re.sub(r"(O calendário de fechos: cada dia da semana mata um pedaço do roteiro.*?)(</(?:details|div)>)",
                   lambda m: m.group(1) + mais + m.group(2), h, count=1, flags=re.S)
    return h


def main(aplica):
    C.aplica_tudo((pena, que_fecha, descontos), ((GUIA, liga_no_guia),), GUIA, aplica)


if __name__ == "__main__":
    main("--aplica" in sys.argv)
