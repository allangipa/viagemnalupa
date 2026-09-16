# -*- coding: utf-8 -*-
"""Escreve o dado estruturado (JSON-LD) que falta nas paginas.

Por que existe
--------------
O Search Console reportou "Detectada, mas nao indexada" e "Nenhuma pagina
foi detectada" como referencia. Nao ha conserto tecnico para falta de link
de fora, mas havia um buraco real: 22 paginas sem dado estruturado nenhum,
incluindo as duas fichas novas (Montevideu, Orlando) e TODAS as paginas de
"quanto custa" e "roteiro" - justamente as que respondem a busca que vale.

O que ele NAO faz, de proposito
-------------------------------
1. Nao escreve preco (estimatedCost). O total das paginas de custo e
   calculado pelo ficha.js conforme a hospedagem que o leitor escolhe.
   Cravar um numero aqui criaria um preco que envelhece em silencio,
   que e exatamente o que a regra editorial do site existe para evitar.

2. Nao escreve "address" nos pontos turisticos. O bloco que ja existe em
   Lisboa diz que o Cabo da Roca, Cascais e a Quinta da Regaleira ficam
   em addressLocality "Lisboa" - nao ficam, sao Sintra e Cascais. Repetir
   isso em 101 pontos espalharia o erro para Maragogi, Xingo, Valparaiso,
   Tigre e o Kennedy Space Center. Nome, URL e imagem bastam e sao verdade.

3. Nao reescreve bloco que ja existe. So preenche o que falta.

Uso
---
    python _build/schema/gera.py            # so mostra o que faria
    python _build/schema/gera.py --aplica   # escreve
"""
import html as _html
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://viagemnalupa.com.br"

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Nome de exibicao de cada destino, para a trilha. Vem do h1 da ficha, mas
# fixar aqui evita que uma mudanca de titulo quebre a trilha em silencio.
DESTINOS = {
    "buenos-aires":   "Buenos Aires",
    "lisboa":         "Lisboa",
    "maceio":         "Maceió",
    "montevideu":     "Montevidéu",
    "nova-york":      "Nova York",
    "orlando":        "Orlando",
    "rio-de-janeiro": "Rio de Janeiro",
    "santiago":       "Santiago",
}

# Cidade e pais de cada ficha. Usado so no containedInPlace do destino -
# que e a cidade da ficha e portanto sempre verdade - e nunca nos pontos.
LUGAR = {
    "montevideu": ("Montevidéu", "UY"),
    "orlando":    ("Orlando", "US"),
}

PAGINAS_SOLTAS = {
    "calculadora": "Calculadora de custos",
    "sobre":       "Como este site apura",
    "privacidade": "Privacidade",
}


# ---------------------------------------------------------------- utilidades

def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def texto(s):
    """Tira tag e devolve o texto como o leitor le."""
    s = re.sub(r"<[^>]+>", "", s)
    s = _html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def campo(htm, padrao, g=1):
    m = re.search(padrao, htm, re.S)
    return texto(m.group(g)) if m else None


def tipos_ja_presentes(htm):
    achados = set()
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',
                         htm, re.S):
        try:
            o = json.loads(m.group(1))
        except Exception:
            continue
        for x in (o if isinstance(o, list) else [o]):
            if isinstance(x, dict) and x.get("@type"):
                achados.add(x["@type"])
    return achados


def bloco(obj):
    """Serializa um objeto como o site ja faz: uma linha, sem escapar acento."""
    corpo = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    # Um "</script>" dentro de string encerraria a tag mais cedo. Nao ocorre
    # hoje, mas custa uma linha garantir que nunca ocorra.
    corpo = corpo.replace("</", "<\\/")
    return '<script type="application/ld+json">%s</script>' % corpo


def injeta(htm, blocos):
    """Poe os blocos no fim do <head>, antes do script do Travelpayouts se
    houver - assim o dado estruturado fica junto do resto do cabecalho e o
    instalador do Drive continua achando os marcadores dele intactos."""
    novo = "\n".join(blocos)
    marca = "<!-- tp-drive:inicio"
    if marca in htm:
        return htm.replace(marca, novo + "\n" + marca, 1)
    return htm.replace("</head>", novo + "\n</head>", 1)


# ------------------------------------------------------------------- pedacos

def trilha(degraus):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": n, "item": SITE + u}
            for i, (n, u) in enumerate(degraus, 1)
        ],
    }


def pontos_da_ficha(htm, slug):
    """Cada secao com id= que tem titulo vira um TouristAttraction.

    A imagem so entra quando a secao realmente tem uma; ponto sem foto sai
    sem o campo, em vez de apontar para um arquivo que nao existe.
    """
    cortes = [(m.group(1), m.start()) for m in re.finditer(
        r'<(?:section|article|div)[^>]*\bid="([^"]+)"', htm)]
    saida = []
    for i, (aid, ini) in enumerate(cortes):
        fim = cortes[i + 1][1] if i + 1 < len(cortes) else len(htm)
        pedaco = htm[ini:fim]
        tit = re.search(r"<h[234][^>]*>(.*?)</h[234]>", pedaco, re.S)
        if not tit:
            continue
        item = {
            "@type": "TouristAttraction",
            "name": texto(tit.group(1)),
            "url": "%s/destinos/%s/#%s" % (SITE, slug, aid),
        }
        img = re.search(r'<img[^>]+src="([^"]+)"', pedaco)
        if img:
            src = re.sub(r"^(\.\./)+", "", img.group(1))
            if not src.startswith("http"):
                src = SITE + "/" + src.lstrip("/")
            item["image"] = src
        saida.append(item)
    return saida


# --------------------------------------------------------------------- roda

def main(aplica):
    mudadas = 0
    total_blocos = 0

    for slug, nome in sorted(DESTINOS.items()):
        base = os.path.join(RAIZ, "destinos", slug)
        guia = os.path.join(base, "index.html")
        if not os.path.isfile(guia):
            continue

        # ---------------------------------------------------- ficha do destino
        htm = le(guia)
        tem = tipos_ja_presentes(htm)
        novos = []
        url_d = "%s/destinos/%s/" % (SITE, slug)

        if "TouristDestination" not in tem:
            d = {
                "@context": "https://schema.org",
                "@type": "TouristDestination",
                "name": nome,
                "url": url_d,
                "inLanguage": "pt-BR",
            }
            desc = campo(htm, r'<meta name="description" content="([^"]*)"')
            if desc:
                d["description"] = desc
            if slug in LUGAR:
                cidade, pais = LUGAR[slug]
                d["containedInPlace"] = {
                    "@type": "City", "name": cidade,
                    "address": {"@type": "PostalAddress",
                                "addressLocality": cidade,
                                "addressCountry": pais},
                }
            # reordena para o mesmo desenho dos blocos que ja existem
            d = {k: d[k] for k in
                 ["@context", "@type", "name", "description", "url",
                  "inLanguage", "containedInPlace"] if k in d}
            novos.append(d)

        if "ItemList" not in tem:
            pts = pontos_da_ficha(htm, slug)
            if pts:
                novos.append({
                    "@context": "https://schema.org",
                    "@type": "ItemList",
                    "name": "%d pontos turísticos de %s" % (len(pts), nome),
                    "numberOfItems": len(pts),
                    "itemListElement": [
                        {"@type": "ListItem", "position": i, "item": p}
                        for i, p in enumerate(pts, 1)
                    ],
                })

        if "BreadcrumbList" not in tem:
            novos.append(trilha([("Início", "/"), ("Destinos", "/destinos/"),
                                 (nome, "/destinos/%s/" % slug)]))

        if novos:
            print("  %-34s +%d  (%s)" % (
                "/destinos/%s/" % slug, len(novos),
                ", ".join(b["@type"] for b in novos)))
            total_blocos += len(novos)
            if aplica:
                escreve(guia, injeta(htm, [bloco(b) for b in novos]))
            mudadas += 1

        # ------------------------------------------------ quanto custa/roteiro
        for sub in sorted(os.listdir(base)):
            alvo = os.path.join(base, sub, "index.html")
            if not os.path.isfile(alvo):
                continue
            h2 = le(alvo)
            tem2 = tipos_ja_presentes(h2)
            n2 = []
            h1 = campo(h2, r"<h1[^>]*>(.*?)</h1>") or sub
            url_p = "%s/destinos/%s/%s/" % (SITE, slug, sub)
            desc = campo(h2, r'<meta name="description" content="([^"]*)"')

            if sub.startswith("roteiro") and "TouristTrip" not in tem2:
                dias = [texto(m.group(1))
                        for m in re.finditer(r"<h3[^>]*>(.*?)</h3>", h2, re.S)]
                t = {
                    "@context": "https://schema.org",
                    "@type": "TouristTrip",
                    "name": h1,
                    "url": url_p,
                    "inLanguage": "pt-BR",
                }
                if desc:
                    t["description"] = desc
                if dias:
                    t["itinerary"] = {
                        "@type": "ItemList",
                        "numberOfItems": len(dias),
                        "itemListElement": [
                            {"@type": "ListItem", "position": i, "name": d}
                            for i, d in enumerate(dias, 1)
                        ],
                    }
                t = {k: t[k] for k in
                     ["@context", "@type", "name", "description", "url",
                      "inLanguage", "itinerary"] if k in t}
                n2.append(t)

            if sub.startswith("quanto-custa") and "WebPage" not in tem2:
                w = {
                    "@context": "https://schema.org",
                    "@type": "WebPage",
                    "name": h1,
                    "url": url_p,
                    "inLanguage": "pt-BR",
                    "isPartOf": {"@type": "WebSite", "name": "Viagem na Lupa",
                                 "url": SITE + "/"},
                    "about": {"@type": "TouristDestination", "name": nome,
                              "url": url_d},
                }
                if desc:
                    w["description"] = desc
                w = {k: w[k] for k in
                     ["@context", "@type", "name", "description", "url",
                      "inLanguage", "isPartOf", "about"] if k in w}
                n2.append(w)

            if "BreadcrumbList" not in tem2:
                folha = "Quanto custa" if sub.startswith("quanto-custa") else h1
                n2.append(trilha([
                    ("Início", "/"), ("Destinos", "/destinos/"),
                    (nome, "/destinos/%s/" % slug),
                    (folha, "/destinos/%s/%s/" % (slug, sub)),
                ]))

            if n2:
                print("  %-34s +%d  (%s)" % (
                    "/destinos/%s/%s/" % (slug, sub), len(n2),
                    ", ".join(b["@type"] for b in n2)))
                total_blocos += len(n2)
                if aplica:
                    escreve(alvo, injeta(h2, [bloco(b) for b in n2]))
                mudadas += 1

    # ------------------------------------------------------- paginas soltas
    for rel, rotulo in PAGINAS_SOLTAS.items():
        p = os.path.join(RAIZ, rel, "index.html")
        if not os.path.isfile(p):
            continue
        h = le(p)
        tem = tipos_ja_presentes(h)
        n = []
        if rel == "calculadora" and "WebApplication" not in tem:
            a = {
                "@context": "https://schema.org",
                "@type": "WebApplication",
                "name": campo(h, r"<h1[^>]*>(.*?)</h1>") or rotulo,
                "url": SITE + "/calculadora/",
                "inLanguage": "pt-BR",
                "applicationCategory": "TravelApplication",
                "browserRequirements": "Requer JavaScript.",
                "isAccessibleForFree": True,
                "offers": {"@type": "Offer", "price": "0",
                           "priceCurrency": "BRL"},
            }
            desc = campo(h, r'<meta name="description" content="([^"]*)"')
            if desc:
                a["description"] = desc
            n.append(a)
        if "BreadcrumbList" not in tem:
            n.append(trilha([("Início", "/"), (rotulo, "/%s/" % rel)]))
        if n:
            print("  %-34s +%d  (%s)" % (
                "/%s/" % rel, len(n), ", ".join(b["@type"] for b in n)))
            total_blocos += len(n)
            if aplica:
                escreve(p, injeta(h, [bloco(b) for b in n]))
            mudadas += 1

    print()
    print("%s: %d blocos em %d paginas."
          % ("Escrito" if aplica else "Faria", total_blocos, mudadas))
    if not aplica:
        print("Nada foi alterado. Rode com --aplica para escrever.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
