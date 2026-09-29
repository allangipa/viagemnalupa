# -*- coding: utf-8 -*-
"""Poe Madri nos dois indices, e acerta os contadores.

Mesmo molde do salvador/cartao.py, que fez isso por Miami e Salvador.

SOBRE A GRADE, E POR QUE ELA NAO MANDA AQUI
-------------------------------------------
A grade da home e de duas colunas, e com 17 cartoes fecha 8 linhas mais
um sozinho. Sevilha e Salvador entraram, cada uma no seu momento, para
resolver exatamente esse orfao.

Aqui nao. A home promete "um destino novo por semana" no bloco Roteiro de
publicacao, e o Allan confirmou que uma por semana e o MINIMO. Com esse
ritmo o cartao orfao e estado de meio de semana, nao defeito a corrigir -
o proximo destino da fila (Roma) o desfaz.

Este script imprime a conta da grade assim mesmo, para o estado ficar
visivel em vez de suposto.

A CAPA
------
"Rainy day at Plaza Mayor, Madrid, Spain - DSC07879", de Daderot, CC0,
5472x3648. Recortada 285 px em cima e embaixo para 16:9.

Licenca conferida no LicenseShortName da API do Commons, no proprio
arquivo, e nao na etiqueta da pagina.

Escolhida em folha de contato. A primeira folha foi descartada inteira: a
busca automatica, que pontuava licenca e resolucao, trouxe um cartao
postal litografado do seculo XIX como Gran Via, o Palacio Real visto de
dentro de um arco quase todo preto, e a Puerta de Alcala com onibus na
frente. Nenhum criterio automatico substitui olhar - a folha existe para
isso.

A segunda folha teve cinco candidatas. A mais bonita era a Gran Via do
alto, com a cupula do Metropolis - mas ela e CC BY 2.0, que EXIGE
atribuicao, e a atribuicao da capa neste site so acontece porque a mesma
imagem e a foto de um ponto no guia. Gran Via nao e um dos dez pontos
apurados, entao ela ficaria sem credito. A Plaza Mayor encaixa no ponto
que ja existe, e ainda e CC0.
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

_spec = importlib.util.spec_from_file_location(
    "dados_madri_cartao", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d)
DESTINOS = _d.DESTINOS

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Os numeros que estao nos indices ANTES desta rodada.
ANTES_DESTINOS = 16
ANTES_PONTOS = 180

CAPAS = {
    "madri": dict(
        arq="plaza-mayor.webp",
        alt=("A Plaza Mayor de Madri em dia de chuva, com a fachada vermelha de arcadas "
             "refletida no piso molhado, a estátua equestre de Filipe III ao centro e "
             "pessoas atravessando"),
        cred="Daderot · CC0 · via Wikimedia Commons"),
}

RESUMO = {
    "madri": dict(
        numeros=[("Os seis pontos pagos", "€ 101", False),
                 ("Pelas janelas gratuitas", "€ 42", True)],
        # O achado e o direito por nacionalidade, porque e o unico numero
        # desta pagina que o leitor daqui tem e nao sabe que tem.
        achado=("<b>A entrada gratuita do Palácio Real não é só para europeu:</b> o texto "
                "oficial da Patrimonio Nacional inclui <b>cidadão latino-americano</b> com "
                "prova de nacionalidade. São € 18 por pessoa que quase todo guia faz o "
                "brasileiro pagar — e três janelas gratuitas encadeiam na mesma "
                "segunda-feira.")),
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

    colunas = 2
    resto = len(todos) % colunas
    print("grade de %d colunas: %d cartoes -> %d linhas%s" %
          (colunas, len(todos), len(todos) // colunas,
           " cheias" if not resto else " + %d sozinho(s), que o proximo da fila desfaz" % resto))
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
