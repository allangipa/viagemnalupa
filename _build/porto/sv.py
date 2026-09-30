# -*- coding: utf-8 -*-
"""Registro dos panoramas de Street View usados nos botoes "Ver na rua".

Mesmo formato de _build/rio/sv.py, _build/lisboa/sv.py e
_build/nova-york/sv.py:

  m       "pano" (ID de panorama do carro) ou "loc" (coordenada "lat,lng";
          obrigatorio para esfera de colaborador, cujo ID o Embed nao aceita)
  v       o ID ou a coordenada
  h/p/f   heading, pitch e field of view ja conferidos visualmente
  rot     rotulo do botao
  titulo  titulo do modal
  nota    uma linha de contexto pratico
  data    captura, para controle (nao vai para o HTML; aparece na imagem)

Ponto sem entrada aqui simplesmente nao ganha botao. Onde a cobertura e
ruim, a ausencia e deliberada.

ESTE ARQUIVO E MODULO E SCRIPT, como o de Nova York e ao contrario dos do
Rio e de Lisboa: o Porto nao tem gerador de pagina, o index.html e
mantido a mao, entao nao ha lib.py para chamar botao(pid).

    python _build/porto/sv.py            # so mostra
    python _build/porto/sv.py --aplica   # escreve

NOVE DOS DEZESSEIS, escolhidos em 30/set/2026
---------------------------------------------
Os dezesseis foram consultados nos metadados (gratuitos) e renderizados
em quatro angulos para achar onde o assunto estava. Sete foram reprovados
a olho; o motivo de cada um esta em _build/streetview/aprovados.json.

DOIS PARES CAIRAM NO MESMO PANORAMA, e este destino foi o primeiro em que
isso apareceu:

  se-do-porto              = metro-do-porto   (a estacao de metro)
  centro-historico-ribeira = ponte-dom-luis   (o mesmo mirante com palmeiras)

Publicar assim mostraria a MESMA IMAGEM sob nomes diferentes - defeito
pior que a falta do botao, porque parece que funciona. Os dois pares
foram desfeitos com coordenada escolhida a mao: a Se pelo Terreiro, a
ponte pelo Cais da Ribeira.

QUATRO DOS NOVE SAO ESFERA DE COLABORADOR - a Livraria Lello por dentro,
a Se, a ponte e a plataforma da Trindade. O carro do Google nao entra em
livraria nem em estacao.
"""
import html
import io
import os
import re
import sys

SV = {
 "livraria-lello": dict(m="loc", v="41.146749,-8.614948", h=180, p=10, f=95, data="2017-08",
   rot="Ver o lugar por dentro",
   titulo="Livraria Lello: a escadaria e o vitral do teto",
   nota="A entrada é paga e o valor vira crédito em livro; a fila costuma dobrar a esquina."),
 "se-do-porto": dict(m="loc", v="41.142870,-8.611425", h=90, p=14, f=90, data="2018-09",
   rot="Ver a entrada na rua",
   titulo="Sé do Porto: a fachada e a rosácea, vistas do Terreiro",
   nota="O terreiro em frente é também miradouro sobre os telhados e o rio."),
 "ponte-dom-luis": dict(m="loc", v="41.140510,-8.611589", h=105, p=10, f=95, data="2016-07",
   rot="Ver o lugar na rua",
   titulo="Ponte Dom Luís I, vista do Cais da Ribeira",
   nota="São dois tabuleiros: o de cima leva o metrô e pedestres; o de baixo, os carros."),
 "centro-historico-ribeira": dict(m="loc", v="41.140700,-8.612900", h=250, p=6, f=95, data="2022-05",
   rot="Ver o lugar na rua",
   titulo="A Ribeira: os arcos e o casario junto ao rio",
   nota="O cais é via pública; o que se paga é o consumo nos cafés sob os arcos."),
 "caves-vinho-do-porto": dict(m="pano", v="IaXD40bbi-VqF1Osskg28g", h=0, p=4, f=95, data="2025-06",
   rot="Ver o lugar na rua",
   titulo="As caves de Gaia, do cais, com a ponte ao fundo",
   nota="As caves ficam na margem de Gaia; a visita e a prova são pagas em cada casa."),
 "capela-das-almas": dict(m="pano", v="Kg8cRT4gSTqdMfbgMRFucQ", h=95, p=8, f=90, data="2024-08",
   rot="Ver o lugar na rua",
   titulo="Capela das Almas: a parede de azulejos, na Rua de Santa Catarina",
   nota="Os azulejos cobrem a lateral inteira e se veem da rua, sem entrar."),
 "mercado-do-bolhao": dict(m="pano", v="7aEyWy3WG1RGvrTkBzmtVg", h=92, p=6, f=90, data="2026-05",
   rot="Ver a entrada na rua",
   titulo="Mercado do Bolhão: a entrada pela Rua Formosa",
   nota="Entrar não se paga; o que se paga é o que se compra nas bancas."),
 "casa-da-musica": dict(m="pano", v="GmjM8u4chXIs3mbX2aElSA", h=180, p=10, f=90, data="2024-08",
   rot="Ver o lugar na rua",
   titulo="Casa da Música: o volume de concreto, na Boavista",
   nota="O prédio de Rem Koolhaas fica isolado no meio da praça, sem vizinhos colados."),
 "metro-do-porto": dict(m="loc", v="41.152277,-8.609299", h=180, p=2, f=95, data="2022-10",
   rot="Ver o lugar por dentro",
   titulo="Metrô do Porto: a plataforma da Trindade",
   nota="A Trindade é a estação onde as linhas se cruzam, e onde quase toda baldeação acontece."),
}

_SVG = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        '<circle cx="12" cy="12" r="8.2" stroke="currentColor" stroke-width="1.8"></circle>'
        '<path d="M3.8 12h16.4M12 3.8c2.2 2.4 2.2 13.9 0 16.4-2.2-2.5-2.2-14 0-16.4Z" '
        'stroke="currentColor" stroke-width="1.6"></path></svg>')


def botao(pid):
    """Devolve o botao do ponto, ou string vazia se ele nao tem panorama aprovado."""
    e = SV.get(pid)
    if not e:
        return ""
    alvo = ('data-sv-pano="%s"' % e["v"]) if e["m"] == "pano" else ('data-sv-loc="%s"' % e["v"])
    return ('\n  <button type="button" class="sv-btn" data-sv %s '
            'data-sv-head="%d" data-sv-pitch="%d" data-sv-fov="%d" '
            'data-sv-titulo="%s" data-sv-nota="%s">%s%s '
            '<span class="sv-sub">&middot; Street View</span></button>'
            % (alvo, e["h"], e["p"], e["f"],
               html.escape(e["titulo"], quote=True), html.escape(e["nota"], quote=True),
               _SVG, e["rot"]))


def main(aplica):
    raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    pag = os.path.join(raiz, "destinos", "porto", "index.html")
    s = io.open(pag, encoding="utf-8").read()
    posto = trocado = 0
    for pid in sorted(SV):
        marca = '<article class="ponto" id="%s"' % pid
        i = s.find(marca)
        if i < 0:
            print("   PONTO NAO ENCONTRADO NA PAGINA: %s" % pid)
            continue
        j = s.index('<div class="campos">', i)
        trecho = s[i:j]
        b = botao(pid)
        antigo = re.search(r'\n?  <button[^>]*\bdata-sv\b.*?</button>', trecho, re.S)
        if antigo:
            s = s[:i] + trecho.replace(antigo.group(0), b) + s[j:]
            trocado += 1
        else:
            s = s[:j] + b + "\n  " + s[j:]
            posto += 1

    # O botao sem o script nao faz nada - licao de Nova York.
    TAG = '<script src="../../assets/js/streetview.js" defer></script>'
    script = "ja tinha"
    if TAG not in s:
        s = s.replace("\n</body>", "\n\n" + TAG + "\n</body>", 1)
        script = "acrescentado"

    if aplica:
        io.open(pag, "w", encoding="utf-8", newline="").write(s)
    print("   %d registrado(s), %d posto(s), %d trocado(s)  script: %s  %s"
          % (len(SV), posto, trocado, script,
             "escrito" if aplica else "SO MOSTRANDO"))


if __name__ == "__main__":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main("--aplica" in sys.argv)
