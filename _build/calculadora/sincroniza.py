# -*- coding: utf-8 -*-
"""Poe na calculadora os destinos que estavam de fora.

O que estava errado
-------------------
O Allan: "Quando clica direto no quanto custa da pagina principal aparece
a calculadora e nao aparece todos os destinos."

Medido: dez destinos no site, seis na calculadora. De fora ficavam
Cancun, Fortaleza, Montevideu e Orlando - e o titulo ainda prometia
"Rio, Lisboa, Nova York e mais tres destinos".

E o mesmo defeito que ja apareceu no schema, no sitemap, nos voos e nos
atalhos: destino novo nao entra sozinho numa estrutura montada antes.

De onde vem o dado
------------------
Dos NUMEROS da ficha de custos do proprio destino - hospedagem,
ingressos, transporte, dias, moeda. Nao reapurei nada: a ficha ja traz
tudo com fonte e data, e derivar de la garante que a calculadora nunca
discorde da pagina que ela resume.

A PROSA (o que nao entra na conta, as fontes, a ressalva de cada cidade)
continua escrita a mao aqui embaixo, porque e texto autoral, nao dado. Mas
com trava: destino com ficha de custos e sem prosa aqui para o script.

Fortaleza fica de fora, e esta escrito por que
----------------------------------------------
A ficha de custos de Fortaleza nao tem NENHUMA faixa de hospedagem - nao
achamos diaria publicada que servisse, e isso ja esta declarado na
pagina. Sem diaria a calculadora nao fecha conta de estadia nenhuma.
Entao ela nao entra, e a pagina diz o motivo em vez de omitir a cidade
caladamente.

Uso
---
    python _build/calculadora/sincroniza.py
    python _build/calculadora/sincroniza.py --aplica
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

from montar import bloco, fmt                                   # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


# ---------------------------------------------------------------- a prosa
# Um verbete por destino que ENTRA na calculadora. O resto e derivado.
PROSA = {
    "montevideu": dict(
        gratis=("Três dos nove pontos não cobram entrada: o Mercado del Puerto, "
                "o Museo Nacional de Artes Visuales e a Feria de Tristán Narvaja."),
        fonte=("Intendencia de Montevideo (tarifa do STM) e as fichas dos 9 pontos, "
               "apuradas em 13 de setembro de 2026. Hospedagem: amostra de mercado — "
               "Montevidéu não publica diária média oficial."),
        nota=("As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
              "quarto; dormitório de hostel é por pessoa. <b>Nenhuma faixa de "
              "hospedagem aqui é estatística oficial</b> — procuramos no Ministerio "
              "de Turismo e no Observatorio Turístico da própria Intendência e não "
              "existe série publicada. São amostras de mercado, rotuladas como tal: "
              "servem para dimensionar, não para reservar."),
    ),
    "orlando": dict(
        gratis=("Nenhum dos pontos apurados é gratuito. Não entram na conta: "
                "aluguel de carro, estacionamento, traslado do aeroporto, "
                "Park Hopper, Express Pass e Lightning Lane."),
        fonte=("I-RIDE Trolley (passe diário) e as fichas dos 6 pontos, apuradas em "
               "13 de setembro de 2026. Hospedagem: Visit Orlando (ADR de 2022) e "
               "amostra de mercado de 2026."),
        nota=("As noites saem das suas datas. <b>Os ingressos de parque são piso, não "
              "preço</b>: são o menor valor publicado para um dia, e a data escolhida "
              "muda muito esse número. <b>Nenhuma das faixas de hospedagem é "
              "estatística oficial atual</b> — o dado da Visit Orlando é de 2022 e o "
              "de 2026 é de aluguel por temporada, outra categoria."),
    ),
    "cancun": dict(
        gratis=("Um dos seis pontos não cobra nada: a Playa Delfines. No México toda "
                "praia é federal e de acesso público."),
        fonte=("INAH (Chichén Itzá, Tulum e Museo Maya), Ultramar (ferry) e as fichas "
               "dos 6 pontos, apuradas em 17 de setembro de 2026. Hospedagem: tarifa "
               "média da cidade divulgada pela Secretaría de Turismo de Quintana Roo."),
        nota=("As noites saem das suas datas. <b>Não há linha de transporte urbano</b>: "
              "não levantamos tarifa de ônibus da Zona Hoteleira nem de táxi, e "
              "preferimos a lacuna à estimativa. <b>O Xcaret também está fora da "
              "conta</b> — apuramos três valores diferentes no mesmo dia e nenhum se "
              "confirmou como o oficial. Os valores em peso não são convertidos: o "
              "Banco Central publica dez moedas e o peso mexicano não está entre elas."),
    ),
}

# Destino com ficha de custos que NAO entra, e o motivo, escrito.
FORA = {
    "fortaleza": "a ficha de custos não tem nenhuma faixa de hospedagem apurada",
}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def limpa(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def texto_td(t):
    """Mantem <b> e <a>, tira o resto. A observacao usa negrito."""
    t = re.sub(r"</?(?!/?(b|a|em|i)\b)[a-zA-Z][^>]*>", "", t)
    return re.sub(r"\s+", " ", t).strip()


# ------------------------------------------------- numeros, da ficha de custos
def do_destino(slug):
    p = os.path.join(RAIZ, "destinos", slug, "quanto-custa", "index.html")
    if not os.path.isfile(p):
        return None
    h = le(p)
    m = re.search(r'(?s)class="calc-cfg"[^>]*>(.*?)</script>', h)
    if not m:
        return None
    cfg = json.loads(m.group(1))

    ingressos, transporte, fixos, taxa = [], None, [], None
    for mm in re.finditer(r'(?s)<tr data-tipo="([^"]+)"([^>]*)>(.*?)</tr>', h):
        tipo, attrs, corpo = mm.group(1), mm.group(2), mm.group(3)
        tds = re.findall(r"(?s)<td[^>]*>(.*?)</td>", corpo)
        if len(tds) < 3:
            continue
        nome, obs = limpa(tds[0]), texto_td(tds[2])
        v = re.search(r'data-v="([^"]+)"', attrs)
        if tipo == "ingresso":
            val = float(v.group(1)) if v else 0.0
            # data-v="0" e linha visivel FORA do total: fica de fora aqui
            # tambem, senao a calculadora somaria zero e diria que apurou.
            if val > 0:
                ingressos.append((nome, val, obs))
        elif tipo == "dia" and v:
            rot = re.search(r'data-rot="([^"]*)"', attrs)
            transporte = dict(v=float(v.group(1)),
                              rot=rot.group(1) if rot else "Transporte, {d} dias",
                              obs=obs)
        elif tipo == "fixo" and v:
            fixos.append((nome, float(v.group(1)), obs))
        elif tipo == "taxa":
            noite = re.search(r'data-noite="([^"]+)"', attrs)
            teto = re.search(r'data-teto="([^"]+)"', attrs)
            rot = re.search(r'data-rot="([^"]*)"', attrs)
            if noite and teto:
                taxa = dict(noite=float(noite.group(1)), teto=int(teto.group(1)),
                            rot=rot.group(1) if rot else "Taxa, {n}", obs=obs)

    # quantos pontos a ficha do destino tem
    hg = le(os.path.join(RAIZ, "destinos", slug, "index.html"))
    pontos = len(re.findall(r'<article class="ponto"', hg))
    nome = re.sub(r"<[^>]+>", "", re.search(r"(?s)<h1[^>]*>(.*?)</h1>", hg).group(1))
    nome = re.split(r"\s+em\s+", nome.split(":")[0])[0].strip()

    return dict(
        slug=slug, nome=nome, pontos=pontos,
        moeda=cfg["moeda"], dec=cfg["dec"], dias=cfg["dias"],
        pessoas=cfg.get("pessoas", 1),
        destino="../destinos/%s/" % slug,
        hosp=cfg.get("hosp") or [],
        hospPadrao=cfg.get("hospPadrao"),
        ingressos=ingressos, transporte=transporte, fixos=fixos, taxa=taxa,
        eventos=cfg.get("eventos") or [], janela=cfg.get("janela"),
        **PROSA[slug])


def total_de(c):
    """Mesma conta do montar.py, para o rotulo do botao."""
    noites = c["dias"] - 1
    hp = {h["k"]: h for h in c["hosp"]}[c["hospPadrao"]]
    t = c["transporte"]
    v = sum(x for _, x, _ in c["ingressos"])
    v += (t["v"] * c["dias"] if t else 0)
    v += sum(x for _, x, _ in c["fixos"])
    if c["taxa"]:
        v += c["taxa"]["noite"] * min(noites, c["taxa"]["teto"])
    return v + hp["ref"] * noites


def main(aplica):
    base = os.path.join(RAIZ, "destinos")
    com_ficha = [s for s in sorted(os.listdir(base))
                 if os.path.isfile(os.path.join(base, s, "quanto-custa",
                                                "index.html"))]
    p = os.path.join(RAIZ, "calculadora", "index.html")
    h = le(p)
    ja = set(re.findall(r'data-cidade="([^"]+)"', h))

    # A trava: destino com ficha de custos tem de estar decidido - ja na
    # calculadora, ou com prosa escrita para entrar, ou explicitamente
    # fora com motivo. E o que impede a proxima cidade de sumir daqui em
    # silencio, como Cancun, Fortaleza, Montevideu e Orlando sumiram.
    indecisos = [s for s in com_ficha
                 if s not in ja and s not in PROSA and s not in FORA]
    if indecisos:
        raise SystemExit(
            "Destino com ficha de custos e sem decisao: %s\n"
            "Ou escreva o verbete em PROSA (entra na calculadora), ou\n"
            "declare em FORA com o motivo. Nao deixo passar em silencio."
            % ", ".join(indecisos))
    print("na calculadora hoje: %d  (%s)" % (len(ja), ", ".join(sorted(ja))))
    for s, porque in sorted(FORA.items()):
        print("fora de proposito   : %-14s %s" % (s, porque))
    print()

    novos = [s for s in com_ficha if s in PROSA and s not in ja]
    if not novos:
        print("Nenhum destino novo para acrescentar.")
        return

    blocos, botoes = [], []
    for slug in novos:
        c = do_destino(slug)
        tot = total_de(c)
        print("  %-16s %d dias, %d ingressos, hosp %d, transporte %s -> %s"
              % (slug, c["dias"], len(c["ingressos"]), len(c["hosp"]),
                 "sim" if c["transporte"] else "NAO", fmt(c, tot)))
        blocos.append(bloco(c, False))
        botoes.append('<button type="button" class="cc-big" data-troca="%s">'
                      '<b>%s</b><span>%s por pessoa &middot; %d dias</span>'
                      '</button>' % (slug, c["nome"], fmt(c, tot), c["dias"]))

    # os botoes entram no fim da nav de abas
    m = re.search(r"(?s)(<nav class=\"calc-abas\".*?)(</nav>)", h)
    if not m:
        raise SystemExit("nao achei a nav das abas da calculadora")
    h = h[:m.end(1)] + "".join(botoes) + h[m.end(1):]

    # os blocos entram depois do ultimo .ficha-calc
    fim = h.rfind("</div>", 0, h.find("</main>"))
    ult = h.rfind('<div class="ficha-calc"')
    corte = h.find("\n</div>", ult)
    if ult < 0 or corte < 0:
        raise SystemExit("nao achei onde terminam as fichas da calculadora")
    corte += len("\n</div>")
    h = h[:corte] + "\n" + "\n".join(blocos) + h[corte:]

    print()
    print("%s: %d destino(s) na calculadora." % ("Escrito" if aplica else "Faria",
                                                 len(novos)))
    if aplica:
        escreve(p, h)
    else:
        print("Nada foi alterado. Rode com --aplica para escrever.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
