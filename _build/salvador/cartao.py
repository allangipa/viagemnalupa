# -*- coding: utf-8 -*-
"""Poe Miami E Salvador nos dois indices, e acerta os contadores.

Mesmo molde do sevilha/cartao.py, que fez isso por Sevilha, e do
novos2/cartoes.py antes dele.

POR QUE OS DOIS NO MESMO SCRIPT
-------------------------------
Porque a grade so fecha com os dois. Ela e de duas colunas: o container
tem 1120 px, o cartao minimo 25rem e o vao 18 px.

    14 cartoes -> 7 linhas cheias      (o estado antes desta rodada)
    15 cartoes -> 7 linhas + 1 sozinho (Miami entrando sozinha)
    16 cartoes -> 8 linhas cheias      (Miami + Salvador)

Entrar so com Miami devolveria o cartao orfao que Sevilha entrou para
resolver quando havia treze. Por isso os dois sao inseridos na mesma
passada, e por isso este script mora na pasta de Salvador - que e o
destino cuja razao de existir agora E a grade.

AS DUAS CAPAS
-------------
"MARCIO FILHO PELOURINHO SALVADOR BAHIA", de MTur Destinos, DOMINIO
PUBLICO, 5224x3277. Recortada 169 px em cima e embaixo para 16:9.

"Mia beach", de Cristo Vlahos, CC BY-SA 4.0, 5312x2988 - ja nasceu em
16:9, sem recorte.

Licencas conferidas no LicenseShortName da API do Commons, no proprio
arquivo, e nao na etiqueta da pagina.

Escolhidas em folha de contato com quatro candidatas cada, todas ja
recortadas em 16:9, com cap de uma por autor. O criterio foi o mesmo de
Sevilha: a foto tem de ler como a cidade EM MINIATURA. As rejeitadas de
Salvador eram uma loja de souvenir, uma fachada azul isolada e um
telhado - nenhuma diz "Salvador" num cartao pequeno. O Largo do
Pelourinho de cima diz na hora.

A ATRIBUICAO, QUE QUASE FICOU FALTANDO
--------------------------------------
O cartao NAO exibe credito de foto - conferido no HTML dos indices. Quem
credita a capa e a pagina do guia, onde a mesma imagem e a foto de um
ponto e carrega o <span class="foto-cred">. E assim que Sevilha, Porto e
Punta Cana estao em conformidade.

Miami e Salvador nasceram com os pontos SEM foto, entao a capa ficaria
sem credito em lugar nenhum. Para o dominio publico de Salvador isso
seria so descuido; para o CC BY-SA 4.0 de Miami seria descumprimento de
licenca, porque essa licenca EXIGE atribuicao.

Resolvido antes deste script rodar: cada capa foi anexada ao ponto
correspondente no dados.py - Pelourinho em Salvador, South Beach em
Miami - e o guia agora imprime os dois creditos.
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))


def _carrega(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Carregados por CAMINHO, os dois: import normal devolveria o `dados` que
# o outro gerador ja deixou em sys.modules, calado.
_sal = _carrega("dados_salvador_cartao", os.path.join(AQUI, "dados.py"))
_mia = _carrega("dados_miami_cartao",
                os.path.join(RAIZ, "_build", "miami", "dados.py"))

# Miami primeiro, Salvador depois - a ordem em que foram publicados.
DESTINOS = _mia.DESTINOS + _sal.DESTINOS

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Os numeros que estao nos indices ANTES desta rodada. Explicitos para a
# substituicao ser verificavel: se nao encontrar, o script avisa em vez
# de seguir calado.
ANTES_DESTINOS = 14
ANTES_PONTOS = 161

CAPAS = {
    "miami": dict(
        arq="south-beach.webp",
        alt=("Guarita de salva-vidas pintada em rosa e laranja na areia de South Beach, "
             "em Miami, com a praia vazia, rastros de pneu na areia e o skyline de "
             "hotéis ao fundo"),
        cred="Cristo Vlahos · CC BY-SA 4.0 · via Wikimedia Commons"),
    "salvador": dict(
        arq="pelourinho.webp",
        alt=("Vista do alto do Largo do Pelourinho, em Salvador, com as fachadas "
             "coloridas dos dois lados da ladeira de pedra, as torres da igreja ao "
             "fundo e o mar no horizonte"),
        cred="MTur Destinos · domínio público · via Wikimedia Commons"),
}

RESUMO = {
    "miami": dict(
        numeros=[("Everglades, brasileiro de carro", "US$ 135", False),
                 ("PAMM na quinta à noite", "grátis", True)],
        # O achado e o adicional de nao-residente, porque e a mudanca que
        # desmente o preco que o leitor vai encontrar em qualquer guia.
        achado=("<b>Desde 1º de janeiro de 2026 o Everglades cobra US$ 100 por pessoa "
                "de quem não mora nos Estados Unidos</b>, e os oito dias de entrada "
                "gratuita do parque deixaram de valer para estrangeiro. Um casal de "
                "carro paga US$ 235, não os US$ 35 da tabela.")),
    "salvador": dict(
        numeros=[("Os quatro pontos pagos", "R$ 80", False),
                 ("Numa quarta-feira", "R$ 20", True)],
        # O achado e a quarta, porque e regra permanente publicada e
        # quase nenhum guia usa.
        achado=("<b>Sete museus municipais não cobram entrada às quartas-feiras</b>, e "
                "é regra permanente da prefeitura, não promoção. O total de R$ 80 cai "
                "para R$ 20 — só o Farol da Barra continua cobrando, porque é o único "
                "que não é municipal.")),
}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def pontos_de(slug):
    h = le(os.path.join(RAIZ, "destinos", slug, "index.html"))
    return len(re.findall(r'<article class="ponto"', h))


def cartao(d, sobe):
    slug = d["slug"]
    capa = CAPAS[slug]
    r = RESUMO[slug]
    n = pontos_de(slug)
    dentro = "./" if sobe == "../" else "./destinos/"
    nums = "".join(
        '<div class="num-b"><span class="r">%s</span>'
        '<span class="v%s">%s</span></div>' % (rot, " c" if c else "", val)
        for rot, val, c in r["numeros"])
    return (
        '<article class="dest" data-regiao="%s" data-status="publicado"\n'
        ' data-busca="%s">'
        '<figure class="dest-capa">'
        '<img src="%sassets/img/%s/%s" alt="%s" width="1200" height="675" '
        'loading="lazy" decoding="async">'
        '<figcaption><div><h3><a href="%s%s/">%s</a></h3>'
        '<span class="pais">%s · %d pontos turísticos</span></div>'
        '<span class="tag-pub">Publicado</span></figcaption></figure>'
        '<div class="numeros">%s</div>'
        '<p class="achado">%s</p>'
        '<div class="paginas"> <a class="pg" href="%s%s/">Guia dos pontos</a> </div>'
        '<a class="dest-link" href="%s%s/" tabindex="-1" aria-hidden="true"></a>'
        '</article>'
        % (d["regiao"], d["busca"], sobe, slug, capa["arq"], capa["alt"],
           dentro, slug, d["nome"], d["pais"], n, nums, r["achado"],
           dentro, slug, dentro, slug))


def main(aplica):
    todos = sorted(s for s in os.listdir(os.path.join(RAIZ, "destinos"))
                   if os.path.isfile(os.path.join(RAIZ, "destinos", s, "index.html")))
    soma = sum(pontos_de(s) for s in todos)
    print("destinos em disco: %d      pontos somados: %d" % (len(todos), soma))

    for slug, capa in CAPAS.items():
        cam = os.path.join(RAIZ, "assets", "img", slug, capa["arq"])
        if not os.path.isfile(cam):
            raise SystemExit("PARADO: capa nao existe em disco: %s" % cam)
    print("capas conferidas em disco: %d" % len(CAPAS))

    # a simetria da grade, que e o motivo de Salvador existir agora
    colunas = 2
    print("grade de %d colunas: %d cartoes -> %d linhas%s" %
          (colunas, len(todos), len(todos) // colunas,
           " cheias" if len(todos) % colunas == 0
           else " + %d sozinho(s)" % (len(todos) % colunas)))
    print()

    for idx, sobe in (("index.html", "./"),
                      (os.path.join("destinos", "index.html"), "../")):
        p = os.path.join(RAIZ, idx)
        h = le(p)
        antes = h
        dentro = "./" if sobe == "../" else "./destinos/"
        for d in DESTINOS:
            if 'href="%s%s/"' % (dentro, d["slug"]) in h:
                print("  %-22s %-12s ja esta" % (idx, d["slug"]))
                continue
            m = None
            for mm in re.finditer(r"</article>", h):
                m = mm
            if not m:
                print("  %-22s sem grade de cartoes" % idx)
                continue
            h = h[:m.end()] + "\n" + cartao(d, sobe) + h[m.end():]
            print("  %-22s %-12s + cartao (%d pontos)"
                  % (idx, d["slug"], pontos_de(d["slug"])))

        h, n1 = re.subn(r"\b%d(?=\s+destinos\b)" % ANTES_DESTINOS, str(len(todos)), h)
        h, n2 = re.subn(r"(>)\s*%d\s*(<)" % ANTES_PONTOS, r"\g<1>%d\g<2>" % soma, h)
        print("  %-22s contadores: %d de destinos, %d de pontos" % (idx, n1, n2))
        if not n1 and str(ANTES_DESTINOS) in antes:
            print("  %-22s  !! nao troquei o total de destinos - confira" % idx)
        if aplica and h != antes:
            escreve(p, h)

    print()
    print("%s." % ("Escrito" if aplica else "Faria isso"))
    if not aplica:
        print("Nada foi alterado. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
