# -*- coding: utf-8 -*-
import html, re, urllib.parse

def mapa(nome, q=None):
    q = q or (nome + ", Rio de Janeiro, Brasil")
    u = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(q)
    return ('<br><a class="mapa" href="%s" target="_blank" rel="noopener" '
            'aria-label="Abrir %s no Google Maps"><svg width="15" height="15" viewBox="0 0 24 24" '
            'fill="none" aria-hidden="true"><path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z" '
            'stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path>'
            '<circle cx="12" cy="10" r="2.5" stroke="currentColor" stroke-width="1.8"></circle>'
            '</svg><span>Ver no mapa</span></a>') % (u, html.escape(nome, quote=True))

def flag(t):
    return '<span class="flag">%s</span>' % t

def ul(items):
    return "<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>"

ROTULOS = ["Endereço","Valor da entrada","Pontos de referência","Metrô mais próximo",
           "Visitantes por ano","Menor visitação e temperatura","Curiosidades",
           "Fatos históricos","Dias em que não funciona","Pontos turísticos próximos"]

def ficha(num, p, cred):
    c = cred[p["img"]]
    if c.get("fonte") == "pendente":
        campos = "".join(
            '\n    <div class="campo-l"><div class="rot">%s</div><div class="val">%s</div></div>'
            % (r, p["campos"][r]) for r in ROTULOS)
        return """<article class="ponto" id="%(id)s">
  <div class="ponto-topo">
    <div class="ponto-id"><span class="num">%(num)02d</span>
      <div><h3>%(nome)s</h3><span class="tag">%(tag)s</span></div></div>
    <div class="preco"><span class="preco-val">%(preco)s</span>
      <span class="preco-nota">%(preconota)s</span></div>
  </div>
  <div class="campos">%(campos)s
  </div>
</article>""" % dict(id=p["id"], num=num, nome=p["nome"], tag=p["tag"], preco=p["preco"],
                     preconota=p["preconota"], campos=campos)
    if c["fonte"] == "storyblocks":
        credito = "Storyblocks · licença royalty-free · SBI-%s" % c["sbi"]
    else:
        credito = ('Foto: %s · <a href="%s" target="_blank" rel="noopener license">%s</a> · '
                   '<a href="%s" target="_blank" rel="noopener">Wikimedia Commons</a> · recortada'
                   % (html.escape(c["autor"]), c["licurl"], c["lic"], c["pagina"]))
    campos = "".join(
        '\n    <div class="campo-l"><div class="rot">%s</div><div class="val">%s</div></div>'
        % (r, p["campos"][r]) for r in ROTULOS)
    nota = ('\n  <p class="foto-nota">%s</p>' % p["fotonota"]) if p.get("fotonota") else ""
    return """<article class="ponto" id="%(id)s">
  <div class="ponto-topo">
    <div class="ponto-id"><span class="num">%(num)02d</span>
      <div><h3>%(nome)s</h3><span class="tag">%(tag)s</span></div></div>
    <div class="preco"><span class="preco-val">%(preco)s</span>
      <span class="preco-nota">%(preconota)s</span></div>
  </div>
  <figure class="foto"><img src="../../assets/img/lisboa/%(img)s.webp" alt="%(alt)s" width="1200" height="675" loading="lazy" decoding="async"><figcaption><p class="foto-cred">%(cred)s</p></figcaption></figure>%(nota)s
  <div class="campos">%(campos)s
  </div>
</article>""" % dict(id=p["id"], num=num, nome=p["nome"], tag=p["tag"], preco=p["preco"],
                     preconota=p["preconota"], img=p["img"], alt=html.escape(c["alt"], quote=True),
                     cred=credito, nota=nota, campos=campos)
