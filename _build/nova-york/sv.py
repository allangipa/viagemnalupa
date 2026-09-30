# -*- coding: utf-8 -*-
"""Registro dos panoramas de Street View usados nos botoes "Ver na rua".

Mesmo formato de _build/rio/sv.py e _build/lisboa/sv.py:

  m       "pano" (ID de panorama) ou "loc" (coordenada "lat,lng";
          obrigatorio quando o Embed nao aceita o ID da esfera)
  v       o ID ou a coordenada
  h/p/f   heading, pitch e field of view ja conferidos visualmente
  rot     rotulo do botao
  titulo  titulo do modal
  nota    uma linha de contexto pratico
  data    captura, para controle (nao vai para o HTML; aparece na imagem)

Ponto sem entrada aqui simplesmente nao ganha botao. Onde a cobertura e
ruim, a ausencia e deliberada.

DIFERENCA PARA O RIO E LISBOA: ESTE ARQUIVO E TAMBEM SCRIPT
-----------------------------------------------------------
Rio e Lisboa tem gerador de pagina (lib.py), que chama botao(pid) na hora
de montar o HTML. Nova York nao tem: a pagina e mantida a mao. Entao aqui
vai junto um main() que escreve os botoes direto no index.html publicado,
no mesmo lugar em que um gerador os colocaria - depois da <figure> e
antes de <div class="campos">.

E IDEMPOTENTE: rodar de novo troca o botao pelo do registro, nao empilha.

    python _build/nova-york/sv.py            # so mostra
    python _build/nova-york/sv.py --aplica   # escreve

COMO ESTES DOZE FORAM ESCOLHIDOS, em 30/set/2026
------------------------------------------------
Os vinte pontos foram consultados no endpoint de metadados (gratuito), e
os candidatos renderizados em quatro angulos para achar onde o assunto
estava. Oito foram reprovados a olho, e o motivo e quase sempre o mesmo:
o metadado devolve o panorama MAIS PROXIMO do endereco, e o mais proximo
de um arranha-ceu e a calcada do pe dele, de onde nao se ve o predio.

O que ficou de fora, e por que:

  empire        so ha calcada ao pe da torre; tentativa pela Quinta
                Avenida caiu num corredor de interior.
  oneworld      idem; tentativa da praca do memorial deu arvore e ceu.
  edge          o panorama mais proximo esta DENTRO do shopping de
                Hudson Yards, com o Shake Shack na tela.
  nove11        quadra generica; nada identifica o memorial.
  liberdade     o mais proximo fica no Liberty State Park, em NEW
                JERSEY. Tentativa na propria ilha deu ceu e agua.
  vessel        a unica esfera e de 2019, ANTES das telas de aco de
                2024. Mesma identidade obsoleta que ja tinha descartado
                a fotografia de 2020 deste ponto.
  central-perk  quadra generica da Times Square; a loja nao aparece.
  friends-exp.  esquina generica; a fachada da exposicao nao aparece.

CENTRAL PARK: A ESFERA DE COLABORADOR RESOLVEU
----------------------------------------------
A primeira busca devolveu o panorama do carro de 2012 - catorze anos, e
um caminho arborizado que poderia ser qualquer parque. Como o parque e
grande demais para "o ponto mais proximo do nome" acertar, foram
consultadas coordenadas de lugares iconicos dentro dele. Ficou a esfera
do Sheep Meadow: o gramado com o skyline de Midtown atras, de 2017 -
nove anos mais nova, e que nao poderia ser outro parque.
"""
import html
import io
import os
import re
import sys

SV = {
 "summit": dict(m="pano", v="m8xyW-y2bimjZgucWZCY8w", h=8, p=10, f=90, data="2026-04",
   rot="Ver a entrada na rua",
   titulo="SUMMIT One Vanderbilt: a entrada na Vanderbilt Avenue",
   nota="A entrada do mirante fica ao lado do Grand Central, no pé da torre."),
 "met": dict(m="pano", v="xcKEPIfDMGhcG3Tf7seZLA", h=270, p=8, f=90, data="2026-04",
   rot="Ver a entrada na rua",
   titulo="The Met: a escadaria da Quinta Avenida",
   nota="A fachada e a escadaria dão para a Quinta Avenida, na borda do Central Park."),
 "moma": dict(m="pano", v="JvTGi1onZ1gM0PoqdtaOwA", h=0, p=6, f=85, data="2024-08",
   rot="Ver a entrada na rua",
   titulo="MoMA: a entrada na rua 53",
   nota="A entrada principal fica na West 53rd Street, entre a Quinta e a Sexta."),
 "amnh": dict(m="pano", v="Ek1Tg_QEZB5cwnpqpcoXBg", h=272, p=10, f=90, data="2026-08",
   rot="Ver a entrada na rua",
   titulo="Museu Americano de História Natural, pelo Central Park West",
   nota="Esta é a entrada histórica; há outra, mais nova, pela Columbus Avenue."),
 "guggenheim": dict(m="loc", v="40.783193,-73.959198", h=95, p=10, f=90,
   data="2022-12",
   rot="Ver o lugar por dentro",
   titulo="Guggenheim: a rampa em espiral vista de dentro",
   nota="A galeria é uma rampa contínua; a visita desce do alto até o térreo."),
 "timessquare": dict(m="pano", v="Mo9wk0nKMhEFuKkDo8BLgQ", h=95, p=14, f=95, data="2026-04",
   rot="Ver o lugar na rua",
   titulo="Times Square, do cruzamento com a Sétima Avenida",
   nota="A praça é via pública e não fecha; os letreiros ficam acesos a noite toda."),
 "topofrock": dict(m="loc", v="40.759417,-73.979304", h=178, p=4, f=95,
   data="2022-02",
   rot="Ver a vista do mirante",
   titulo="Top of the Rock: a vista para o sul, com o Empire State",
   nota="É deste mirante que se vê o Empire State — do próprio Empire não se vê ele."),
 "grandcentral": dict(m="pano", v="zlFALrkqgRcIv3MPQoHLCw", h=5, p=14, f=90, data="2026-04",
   rot="Ver a entrada na rua",
   titulo="Grand Central: a fachada da rua 42, sob o viaduto",
   nota="O viaduto da Park Avenue passa por cima da entrada principal."),
 # A PRIMEIRA ESCOLHA MOSTRAVA A CALCADA DE BAIXO, e o Allan reparou: o
 # parque e elevado, e o panorama do carro so alcanca a estrutura de ferro
 # vista do chao. A coordenada do passeio e a MESMA da rua embaixo, entao
 # "o panorama mais proximo" sempre devolve a rua.
 #
 # A saida foi procurar em trechos no meio do quarteirao, onde nao ha via
 # publica por baixo. Seis esferas apareceram; cinco eram interior de
 # predio vizinho - o Chelsea Market, um saguao, um apartamento. Esta e a
 # High Line mesmo: o gramado, o deck de madeira e o corredor de
 # vegetacao entre os prédios. Julho de 2026, a mais nova do destino.
 #
 # Conferido que a coordenada cai nela COM e SEM o parametro radius, que
 # o Embed nao aceita.
 "highline": dict(m="loc", v="40.747807,-74.004783", h=0, p=2, f=95, data="2026-07",
   rot="Ver o lugar por cima",
   titulo="The High Line: o gramado, na altura da rua 23",
   nota="O parque corre sobre a antiga linha de carga elevada, entre os prédios."),
 "friends-predio": dict(m="pano", v="atRw7naucB5nFUESHuol9g", h=355, p=8, f=100,
   data="2024-09",
   rot="Ver o lugar na rua",
   titulo="A esquina de Bedford com Grove, em Greenwich Village",
   nota="O prédio da vinheta é o de tijolo, à direita; é residencial e não se entra."),
 "brooklyn": dict(m="loc", v="40.706100,-73.996900", h=130, p=6, f=95, data="2025-05",
   rot="Ver o lugar na travessia",
   titulo="Ponte do Brooklyn: a passarela de pedestres",
   nota="A passarela corre acima do trânsito, no meio do tabuleiro."),
 "centralpark": dict(m="loc", v="40.772200,-73.974500", h=180, p=2, f=95, data="2017-04",
   rot="Ver o lugar por dentro",
   titulo="Central Park: o gramado do Sheep Meadow, com o skyline atrás",
   nota="O gramado abre de meados de abril a meados de outubro, conforme o tempo."),
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
    pag = os.path.join(raiz, "destinos", "nova-york", "index.html")
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
    # O BOTAO SEM O SCRIPT NAO FAZ NADA. Na primeira aplicacao os doze
    # botoes entraram e a pagina nao tinha o streetview.js - clicar nao
    # abria coisa nenhuma. Rio e Lisboa carregam a tag porque o gerador
    # deles a escreve; aqui ela entra junto, na mesma posicao.
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
