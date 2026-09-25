# -*- coding: utf-8 -*-
"""Poe quem publica (Organization) e quando mudou (dateModified) nas paginas.

Por que
-------
A auditoria de dado estruturado achou tres ausencias totais no site:
Organization, publisher e dateModified. Nenhuma das 46 paginas dizia quem
assina o que publica, nem quando a pagina foi alterada pela ultima vez.

O dateModified importa mais aqui do que importaria em outro site. A tese
do Viagem na Lupa e que todo numero tem data. Essa data esta na prosa de
cada ponto - "consultada em 25/set/2026" - e em lugar nenhum que uma
maquina leia. Um site que se vende por dado datado deve expor a data.

DE ONDE VEM A DATA
------------------
Do <lastmod> do sitemap.xml, que por sua vez vem do ultimo commit que
tocou o arquivo. Ou seja: nao ha data escrita a mao em lugar nenhum, e
nao ha uma segunda fonte para divergir da primeira.

Rode DEPOIS de _build/sitemap/atualiza.py, sempre. Se o sitemap estiver
velho, este script propaga o atraso em vez de corrigi-lo.

ONDE O dateModified PODE ENTRAR, E ONDE NAO PODE
------------------------------------------------
dateModified e propriedade de CreativeWork. TouristDestination herda de
Place, e nao de CreativeWork - po-la la e o mesmo erro que o gera.py ja
documenta para o inLanguage, e o validador do schema.org reclama.

Por isso a data nunca entra no TouristDestination das 14 fichas. Entra
num bloco WebPage proprio, que e CreativeWork e aceita tanto dateModified
quanto publisher. Onde ja existe WebPage - as 13 paginas de custo - os
dois campos sao acrescentados ao bloco que esta la.

A EXCECAO A REGRA DA CASA, DECLARADA
------------------------------------
O gera.py nao reescreve bloco que ja existe, com uma unica excecao (a
contagem do ItemList). Este script abre a segunda: acrescenta campo em
WebSite e em WebPage que ja existem.

A diferenca que torna isso seguro e a mesma da primeira excecao: so
ACRESCENTA chave ausente. Nunca altera valor escrito, nunca remove nada.
Se a chave ja estiver la, passa direto. Nao ha redacao humana em risco.

Uso
---
    python _build/schema/editor.py            # so mostra
    python _build/schema/editor.py --aplica   # escreve
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://viagemnalupa.com.br"
MAPA = os.path.join(RAIZ, "sitemap.xml")

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ID_ORG = SITE + "/#organizacao"
ID_SITE = SITE + "/#site"

# A organizacao, inteira, uma vez so - na home. As outras paginas apontam
# para o @id. Repetir o objeto em 45 paginas seria peso morto e, pior, 45
# lugares para uma correcao futura esquecer um.
#
# So campo que e verdade e conferivel. Sem fundacao, sem endereco, sem
# telefone, sem perfil de rede: o site nao publica nada disso, e inventar
# aqui seria exatamente o que a regra editorial proibe.
ORGANIZACAO = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": ID_ORG,
    "name": "Viagem na Lupa",
    "url": SITE + "/",
    "description": "Guias de viagem com custo verificado e datado.",
    "logo": {
        "@type": "ImageObject",
        "url": SITE + "/assets/img/marca-1024.png",
        "width": 1024,
        "height": 1024,
    },
}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def serializa(obj):
    corpo = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return corpo.replace("</", "<\\/")


def bloco(obj):
    return '<script type="application/ld+json">%s</script>' % serializa(obj)


def datas_do_sitemap():
    """{url: 'AAAA-MM-DD'} a partir do <lastmod>, que vem do git."""
    if not os.path.isfile(MAPA):
        raise SystemExit("PARADO: sitemap.xml nao encontrado.")
    fora = {}
    for u in re.findall(r"<url>(.*?)</url>", le(MAPA), re.S):
        loc = re.search(r"<loc>([^<]*)</loc>", u)
        lm = re.search(r"<lastmod>([^<]*)</lastmod>", u)
        if loc and lm and re.fullmatch(r"\d{4}-\d{2}-\d{2}", lm.group(1)):
            fora[loc.group(1)] = lm.group(1)
    return fora


def arquivo_de(url):
    rel = url[len(SITE):].lstrip("/")
    if rel == "" or rel.endswith("/"):
        return os.path.join(RAIZ, rel.replace("/", os.sep), "index.html")
    return os.path.join(RAIZ, rel.replace("/", os.sep))


def blocos_de(htm):
    """[(inicio, fim, objeto)] de cada JSON-LD que da para ler."""
    fora = []
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',
                         htm, re.S):
        try:
            o = json.loads(m.group(1))
        except Exception:
            continue
        if isinstance(o, dict):
            fora.append((m.start(1), m.end(1), o))
    return fora


def injeta(htm, novos):
    texto = "\n".join(bloco(o) for o in novos)
    marca = "<!-- tp-drive:inicio"
    if marca in htm:
        return htm.replace(marca, texto + "\n" + marca, 1)
    return htm.replace("</head>", texto + "\n</head>", 1)


def acrescenta(htm, ini, fim, obj, campos):
    """So chave AUSENTE. Devolve (htm, [nomes acrescentados])."""
    postos = [k for k, v in campos.items() if k not in obj]
    if not postos:
        return htm, []
    for k in postos:
        obj[k] = campos[k]
    return htm[:ini] + serializa(obj) + htm[fim:], postos


def main(aplica):
    datas = datas_do_sitemap()
    print("datas validas lidas do sitemap: %d\n" % len(datas))

    mudadas = org_posta = pag_novas = pag_ricas = site_rico = 0
    sem_arquivo = []

    for url in sorted(datas):
        arq = arquivo_de(url)
        if not os.path.isfile(arq):
            sem_arquivo.append(url)
            continue
        htm = antes = le(arq)
        data = datas[url]
        conta = []

        # ---------------------------------------------------- a organizacao
        tipos = {o.get("@type") for _, _, o in blocos_de(htm)}
        if url == SITE + "/" and "Organization" not in tipos:
            htm = injeta(htm, [ORGANIZACAO])
            org_posta = 1
            conta.append("Organization")

        # --------------------------------- publisher e @id no WebSite da home
        for ini, fim, o in reversed(blocos_de(htm)):
            if o.get("@type") == "WebSite":
                htm, pos = acrescenta(htm, ini, fim, o,
                                      {"@id": ID_SITE,
                                       "publisher": {"@id": ID_ORG}})
                if pos:
                    site_rico = 1
                    conta.append("WebSite +" + "+".join(pos))

        # ------------------------------------- a data, num WebPage que aceite
        alvo = [(i, f, o) for i, f, o in blocos_de(htm)
                if o.get("@type") == "WebPage"]
        if alvo:
            ini, fim, o = alvo[-1]
            htm, pos = acrescenta(htm, ini, fim, o,
                                  {"dateModified": data,
                                   "publisher": {"@id": ID_ORG},
                                   "isPartOf": {"@id": ID_SITE}})
            if pos:
                pag_ricas += 1
                conta.append("WebPage +" + "+".join(x.lstrip("@") for x in pos))
        else:
            nome = re.search(r"<title>(.*?)</title>", htm, re.S)
            novo = {
                "@context": "https://schema.org",
                "@type": "WebPage",
                "@id": url + "#pagina",
                "url": url,
                "name": re.sub(r"\s+", " ", nome.group(1)).strip() if nome else None,
                "inLanguage": "pt-BR",
                "dateModified": data,
                "isPartOf": {"@id": ID_SITE},
                "publisher": {"@id": ID_ORG},
            }
            novo = {k: v for k, v in novo.items() if v is not None}
            htm = injeta(htm, [novo])
            pag_novas += 1
            conta.append("WebPage novo (%s)" % data)

        if htm != antes:
            mudadas += 1
            print("  %-46s %s" % (url[len(SITE):] or "/", ", ".join(conta)))
            if aplica:
                escreve(arq, htm)

    print()
    print("Organization: %d   WebSite enriquecido: %d" % (org_posta, site_rico))
    print("WebPage novos: %d   WebPage enriquecidos: %d" % (pag_novas, pag_ricas))
    print("paginas tocadas: %d" % mudadas)
    if sem_arquivo:
        print("\nURL no sitemap sem arquivo em disco: %d" % len(sem_arquivo))
        for u in sem_arquivo:
            print("   " + u)
    if not aplica:
        print("\nNada foi alterado. Rode com --aplica.")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplica" in sys.argv))
