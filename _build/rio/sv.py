# -*- coding: utf-8 -*-
"""Registro dos panoramas de Street View usados nos botoes "Ver na rua".

Cada entrada tem:
  m       "pano" (panorama do carro do Google) ou "loc" (coordenada; obrigatorio
          para foto 360 de colaborador, cujo ID o Embed nao aceita)
  v       o ID do panorama ou a coordenada "lat,lng"
  h/p/f   heading, pitch e field of view ja conferidos visualmente
  rot     rotulo do botao
  titulo  titulo do modal
  nota    uma linha de contexto pratico
  data    captura, para controle (nao vai para o HTML; aparece na propria imagem)

Ponto sem entrada aqui simplesmente nao ganha botao. Onde a cobertura e ruim,
a ausencia e deliberada.
"""
import html

SV = {
 "cristo-redentor": dict(m="pano", v="MRvCod8a41uiJFRdP8MM8g", h=87, p=25, f=95, data="2016-05",
   rot="Ver o lugar na rua",
   titulo="Cristo Redentor visto da plataforma",
   nota="A estátua é vista de baixo, do patamar onde terminam as escadas."),
 "pao-de-acucar": dict(m="loc", v="-22.948977,-43.157063", h=0, p=10, f=95, data="2019-10",
   rot="Ver o lugar na rua",
   titulo="Do Morro da Urca, a vista sobre a enseada de Botafogo",
   nota="A primeira parada do bondinho é aqui; a segunda sobe para o Pão de Açúcar."),
 "vista-chinesa": dict(m="pano", v="-Cz-TRDjJMSYsIciUUS9NA", h=94, p=4, f=45, data="2026-02",
   rot="Ver o lugar na rua",
   titulo="A chegada ao mirante da Vista Chinesa",
   nota="O pagode fica no fim da estrada, sem estacionamento próprio."),
 "museu-do-amanha": dict(m="pano", v="NpxVsntmwU2yHP4Lso9q4Q", h=143, p=6, f=95, data="2016-03",
   rot="Ver a entrada na rua",
   titulo="Museu do Amanhã visto da Praça Mauá",
   nota="O prédio de Santiago Calatrava avança sobre o píer."),
 "copacabana": dict(m="loc", v="-22.9758906,-43.1864163", h=338, p=0, f=95, data="2021-06",
   rot="Ver o lugar na rua",
   titulo="Copacabana: a areia e o calçadão",
   nota="O calçadão em ondas de pedra portuguesa corre do Leme ao Posto 6."),
 "ipanema-arpoador": dict(m="pano", v="2kD8iZUFQ8j6wo4C0RCOIg", h=185, p=6, f=95, data="2026-02",
   rot="Ver o lugar na rua",
   titulo="Ipanema vista da Avenida Vieira Souto",
   nota="Ao fundo, o Morro Dois Irmãos fecha a praia."),
 "real-gabinete": dict(m="loc", v="-22.9053704,-43.182216", h=298, p=0, f=95, data="2019-09",
   rot="Ver o lugar por dentro",
   titulo="Real Gabinete: o salão de leitura",
   nota="Três andares de estantes em volta de um vão central iluminado pela claraboia."),
 "theatro-municipal": dict(m="pano", v="mGQzmv1NOWXmYbyI_d8E5g", h=0, p=8, f=90, data="2024-06",
   rot="Ver a entrada na rua",
   titulo="Theatro Municipal: onde fica a entrada da visita guiada",
   nota="A bilheteria é na entrada lateral, pelo Boulevard, na Av. 13 de Maio."),
 "lapa-arcos": dict(m="pano", v="gUHipNX4cmByb_YhRbmgAg", h=57, p=6, f=95, data="2024-07",
   rot="Ver o lugar na rua",
   titulo="Arcos da Lapa vistos da Avenida Mem de Sá",
   nota="O bonde de Santa Teresa cruza por cima dos arcos."),
 "maracana": dict(m="pano", v="mZCH4Em1yZQsYaSez5-rKw", h=290, p=6, f=95, data="2014-04",
   rot="Ver o lugar por dentro",
   titulo="Maracanã: a boca do túnel dos jogadores",
   nota="Vista de dentro do estádio, no nível do gramado."),
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
