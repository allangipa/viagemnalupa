# -*- coding: utf-8 -*-
"""Registro dos panoramas de Street View usados nos botoes "Ver na rua".

Mesmo formato de _build/rio/sv.py, _build/lisboa/sv.py,
_build/nova-york/sv.py e _build/porto/sv.py:

  m       "pano" (ID de panorama do carro ou de colecao interna do Google)
          ou "loc" (coordenada "lat,lng"; obrigatorio para esfera de
          colaborador, cujo ID o Embed nao aceita)
  v       o ID ou a coordenada
  h/p/f   heading, pitch e field of view ja conferidos visualmente
  rot     rotulo do botao
  titulo  titulo do modal
  nota    uma linha de contexto pratico
  data    captura, para controle (nao vai para o HTML; aparece na imagem)

Ponto sem entrada aqui simplesmente nao ganha botao. Onde a cobertura e
ruim, a ausencia e deliberada.

ESTE ARQUIVO E MODULO E SCRIPT, como os de Nova York e do Porto.
Granada tem gerador de pagina - o novos/gera.py -, MAS ele nao sabe de
Street View, e nao ha lib.py de cidade para chamar botao(pid) como no Rio
e em Lisboa. Entao o sv.py entra na cadeia DEPOIS do gera.py: regerar o
guia apaga os botoes, e rodar este script os repoe.

    python _build/granada/sv.py            # so mostra
    python _build/granada/sv.py --aplica   # escreve

SETE DOS DEZ, escolhidos em 1 de outubro de 2026
-------------------------------------------------
E a melhor proporcao do site ate agora: Rio 10/16, Lisboa 8/16, Nova York
12/20, Porto 9/16, Granada 7/10.

Metodo: 40 consultas de metadado (gratuitas) em coordenadas escolhidas a
mao DENTRO de cada lugar, nunca por nome - armadilha 4. Depois 65 quadros
renderizados em quatro angulos, aprovados pelo Allan em tres lotes, e
olhados um por um.

TRES PONTOS FICAM SEM BOTAO, CADA UM POR UM MOTIVO
---------------------------------------------------
  hospedagem             e conta, nao lugar - nem foto tem

  alhambra-noturna       O STREET VIEW NAO TEM PANORAMA NOTURNO. A
                         consulta devolveu exatamente o mesmo panorama
                         do alhambra-diurna (ckccP-L-bb3lzPR2ApxPYg) -
                         armadilha 5 - e, no fundo, imagem diurna sob
                         botao de visita noturna e o defeito que o
                         LEIA-ME chama de pior que a ausencia, porque
                         parece que funciona.

  monumentos-andalusies  tres tentativas, tres fracassos. O patio do
                         Corral del Carbon nao tem cobertura: os dois
                         panoramas de carro por perto estao na Calle
                         Reyes Catolicos e mostram vitrine de loja. El
                         Banuelo, de 2025, devolveu parede caiada cega.
                         Sao monumentos atras de porta, em viela - o
                         carro passa e nao os ve.

O QUE AS ARMADILHAS DO LEIA-ME CUSTARAM AQUI
---------------------------------------------
Armadilha 2 (o metadado devolve o pano MAIS PROXIMO) derrubou tres:

  Patio de los Leones    duas esferas diferentes, a 5 e a 6 metros, e as
                         duas caem FORA do patio - uma numa esplanada de
                         terra batida, outra num jardim de sebes
  Mirador San Nicolas    o panorama de carro mais proximo esta na viela
                         ao lado, entre muros caiados, sem vista nenhuma
  Corral del Carbon      descrito acima

As duas primeiras so foram resolvidas trocando o alvo: a Alhambra entrou
pela COLECAO INTERNA do Google dentro dos Palacios Nazaries, e o mirante
entrou por ESFERA DE COLABORADOR no proprio muro - que e o corolario do
LEIA-ME, de que em vista e interior a esfera e a unica coisa que existe.

QUATRO DOS SETE SAO ESFERA DE COLABORADOR. O carro do Google nao sobe em
mirante, nao entra em catedral e nao sobe ao Generalife.

PITCH ZERO EM TODOS, E ISSO E DE PROPOSITO
-------------------------------------------
Os 65 quadros foram renderizados com pitch 0. Publicar um pitch diferente
seria publicar angulo NAO conferido - e a regra desta pasta e que h/p/f
sao "ja conferidos visualmente". Onde um pitch para cima melhoraria o
enquadramento, ele fica para uma proxima rodada com quadro a mais.
"""
import html
import io
import os
import re
import sys

SV = {
 "alhambra-diurna": dict(m="pano", v="ckccP-L-bb3lzPR2ApxPYg", h=90, p=0, f=90, data="2013-06",
   rot="Ver por dentro dos palácios",
   titulo="Palácios Nazaríes: o estuque entalhado da sala de Comares",
   nota="É aqui que o ingresso tem hora marcada: 300 pessoas a cada meia hora, e perder o turno é perder o espaço."),
 "generalife": dict(m="loc", v="37.178230,-3.585260", h=330, p=0, f=90, data="2018-08",
   rot="Ver o pátio do alto",
   titulo="Generalife: o Pátio da Acequia, com o canal e a galeria",
   nota="O bilhete barato da Alhambra dá este pátio — e não dá os Palacios Nazaríes."),
 "catedral": dict(m="loc", v="37.176520,-3.598960", h=345, p=0, f=90, data="2017-05",
   rot="Ver o lugar por dentro",
   titulo="Catedral de Granada: a Capilla Mayor vista da nave",
   nota="Na quarta-feira à tarde a visita é gratuita, com reserva feita até 24 horas antes."),
 "capilla-real": dict(m="loc", v="37.176400,-3.598600", h=90, p=0, f=90, data="2019-07",
   rot="Ver a entrada na rua",
   titulo="Capilla Real: o portal plateresco, na Lonja",
   nota="É bilhete separado do da catedral, embora as duas sejam paredes-meias."),
 "sacromonte": dict(m="pano", v="COGU9Iojymd0A-ob3zDMPw", h=0, p=0, f=90, data="2025-07",
   rot="Ver o lugar na rua",
   titulo="Sacromonte: a subida entre as casas-caverna",
   nota="As fachadas brancas são a frente de cavernas escavadas no morro; o museu cobra € 6."),
 "museo-alhambra": dict(m="pano", v="XZXc-rhIASEcoLCJubF2FA", h=270, p=0, f=90, data="2016-07",
   rot="Ver o lugar por dentro",
   titulo="Palacio de Carlos V: a galeria do pátio circular",
   nota="A entrada aqui é livre para todos, mesmo sem bilhete da Alhambra — e isso está em norma legal."),
 "miradouros": dict(m="loc", v="37.180960,-3.592220", h=170, p=0, f=90, data="2018-08",
   rot="Ver a vista do mirante",
   titulo="Mirador de San Nicolás: a Alhambra do outro lado do vale",
   nota="A praça é pública e não cobra nada; a torre da igreja ao lado custa € 3."),
}

# Armadilha 5 do LEIA-ME: dois pontos no mesmo panorama mostram a MESMA
# imagem sob nomes diferentes. A trava roda na importacao, nao so no main.
_vals = [e["v"] for e in SV.values()]
if len(set(_vals)) != len(_vals):
    from collections import Counter
    raise SystemExit("PARADO: panorama repetido entre pontos: %s"
                     % [v for v, n in Counter(_vals).items() if n > 1])

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
    pag = os.path.join(raiz, "destinos", "granada", "index.html")
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
