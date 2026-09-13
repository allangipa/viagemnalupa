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
 "mosteiro-jeronimos": dict(m="loc", v="38.697100,-9.205800", h=0, p=8, f=95, data="2024-07",
   rot="Ver a entrada na rua",
   titulo="Mosteiro dos Jerónimos visto da Praça do Império",
   nota="A fachada sul corre por toda a extensão da praça."),
 "torre-de-belem": dict(m="loc", v="38.692180,-9.215300", h=225, p=0, f=90, data="2021-01",
   rot="Ver o lugar na rua",
   titulo="Torre de Belém vista do passeio",
   nota="A fila se forma em terra, antes da passarela de madeira."),
 "padrao-descobrimentos": dict(m="pano", v="jK4d4Ql6V-rJhPpmVzx6EA", h=144, p=8, f=95, data="2024-07",
   rot="Ver o lugar na rua",
   titulo="Padrão dos Descobrimentos, com a ponte ao fundo",
   nota="A rosa dos ventos em calçada portuguesa fica no chão, em frente ao monumento."),
 "praca-do-comercio": dict(m="pano", v="KZVh1YDCaIucvPLf9-SEpg", h=130, p=6, f=95, data="2014-08",
   rot="Ver o lugar na rua",
   titulo="Praça do Comércio: a estátua de D. José I e o Tejo",
   nota="O Arco da Rua Augusta fica às costas de quem olha para o rio."),
 "miradouros-alfama": dict(m="pano", v="u7XdMx4tCUzAi2exhFxQMQ", h=134, p=6, f=95, data="2024-08",
   rot="Ver o lugar na rua",
   titulo="Largo das Portas do Sol",
   nota="Os trilhos no chão são os do elétrico 28, que passa raspando no miradouro."),
 "gulbenkian": dict(m="pano", v="ijvv5KmwG8cLZNZCEkgeCg", h=313, p=6, f=95, data="2015-03",
   rot="Ver o lugar por dentro",
   titulo="Gulbenkian: uma das galerias da coleção",
   nota="A coleção do fundador ocupa um circuito único, em ordem cronológica."),
 "oceanario": dict(m="pano", v="A3uN8ISXEd3NuiTE5sJZJA", h=182, p=6, f=95, data="2014-08",
   rot="Ver o lugar por dentro",
   titulo="Oceanário: o tanque central",
   nota="O tanque principal é visto dos dois pisos da visita."),
 "time-out-market": dict(m="pano", v="DYpR5njNtf4NMdWKmpHcSw", h=92, p=6, f=95, data="2024-08",
   rot="Ver a entrada na rua",
   titulo="Time Out Market: a fachada do Mercado da Ribeira",
   nota="O mercado tradicional de frescos funciona na metade oposta à das bancas de comida."),
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
