# -*- coding: utf-8 -*-
"""Gera o bloco .ficha-calc de uma cidade, no mesmo contrato que ficha.js espera."""
import json, html
from dados import RIO, LISBOA

def fmt(c, v):
    s = ("%.2f" % v) if c["dec"] == 2 else ("%.0f" % v)
    inteiro, _, frac = s.partition(".")
    inteiro = "{:,}".format(int(inteiro)).replace(",", ".")
    return c["moeda"] + " " + (inteiro + "," + frac if frac else inteiro)

def plural(n, um, muitos):
    return "%d %s" % (n, um if n == 1 else muitos)

def bloco(c, primeira):
    d, noites = c["dias"], c["dias"] - 1
    hosp = {h["k"]: h for h in c["hosp"]}
    hp = hosp[c["hospPadrao"]]

    cfg = {"moeda": c["moeda"], "dec": c["dec"], "dias": d, "pessoas": c["pessoas"],
           "hosp": [{k: v for k, v in h.items()} for h in c["hosp"]],
           "hospPadrao": c["hospPadrao"], "janela": c["janela"], "eventos": c["eventos"]}

    opts = "".join('<option value="%s"%s>%s</option>'
                   % (h["k"], " selected" if h["k"] == c["hospPadrao"] else "", h["rot"])
                   for h in c["hosp"])

    linhas = []
    for nome, v, obs in c["ingressos"]:
        linhas.append('<tr data-tipo="ingresso" data-v="%.4f"><td>%s</td><td class="n">%s</td>'
                      '<td>%s</td></tr>' % (v, nome, fmt(c, v), obs))
    t = c["transporte"]
    linhas.append('<tr data-tipo="dia" data-v="%.4f" data-rot="%s"><td>%s</td>'
                  '<td class="n">%s</td><td>%s</td></tr>'
                  % (t["v"], t["rot"], t["rot"].replace("{d}", str(d)),
                     fmt(c, t["v"] * d), t["obs"]))
    if c["taxa"]:
        tx = c["taxa"]
        nc = min(noites, tx["teto"])
        linhas.append('<tr data-tipo="taxa" data-noite="%.4f" data-teto="%d" data-rot="%s">'
                      '<td>%s</td><td class="n">%s</td><td>%s</td></tr>'
                      % (tx["noite"], tx["teto"], tx["rot"],
                         tx["rot"].replace("{n}", plural(nc, "noite", "noites")),
                         fmt(c, tx["noite"] * nc), tx["obs"]))
    for nome, v, obs in c["fixos"]:
        linhas.append('<tr data-tipo="fixo" data-v="%.4f"><td>%s</td><td class="n">%s</td>'
                      '<td>%s</td></tr>' % (v, nome, fmt(c, v), obs))
    linhas.append('<tr data-tipo="hosp"><td>Hospedagem, %s</td><td class="n">%s</td>'
                  '<td>%s, %s a diária</td></tr>'
                  % (plural(noites, "noite", "noites"), fmt(c, hp["ref"] * noites),
                     hp["rot"], fmt(c, hp["ref"])))

    ing = sum(v for _, v, _ in c["ingressos"])
    outros = t["v"] * d + sum(v for _, v, _ in c["fixos"])
    if c["taxa"]:
        outros += c["taxa"]["noite"] * min(noites, c["taxa"]["teto"])
    total = ing + outros + hp["ref"] * noites

    return """<div class="ficha-calc" data-cidade="%(slug)s"%(hid)s>

<section class="bloco" id="calculadora">
  <div class="bloco-head">
    <span class="eyebrow">Calculadora</span>
    <h2>Faça a conta da <em style="font-style:normal;color:var(--ambar)">sua</em> viagem</h2>
    <p>A tabela abaixo é a nossa apuração: %(d)d dias, 1 pessoa.
       Mude as datas, o número de pessoas e a categoria de hospedagem, desmarque o que
       você não vai fazer, e a conta se refaz na hora.</p>
  </div>

  <div class="calc" hidden>
    <span class="t">Sua viagem</span>
    <div class="calc-ctrl">
      <label>Chegada
        <input type="date" class="c-ida" value="2026-11-10" min="2026-09-14" max="2028-12-31"></label>
      <label>Volta
        <input type="date" class="c-volta" value="2026-11-%(volta)02d" min="2026-09-14" max="2028-12-31"></label>
      <label>Pessoas
        <input type="number" class="c-pes" min="1" max="8" step="1" value="1" inputmode="numeric"></label>
      <label>Hospedagem
        <select class="c-hosp">%(opts)s</select></label>
    </div>
    <p class="calc-dur c-dur"></p>
    <div class="c-alertas"></div>
    <p class="calc-nota">%(nota)s Os valores unitários são os apurados e estão na tabela
       abaixo — <b style="color:var(--gelo)">o que muda aqui é só a aritmética, não a
       fonte</b>. Linhas marcadas como não encontradas continuam fora da conta.</p>
    <div class="painel res"></div>
  </div>
  <script type="application/json" class="calc-cfg">%(cfg)s</script>
</section>
<section class="bloco"><div class="tabwrap"><table class="tab-ficha"><thead><tr><th>Item</th><th>Valor</th><th>Observação</th></tr></thead><tbody>%(linhas)s</tbody><tfoot><tr><td class="tot-rot">Total por pessoa</td><td class="n tot-val">%(total)s</td><td class="tot-dia">%(dia)s por pessoa por dia</td></tr></tfoot></table></div>
<p style="color:var(--nevoa);font-size:.92rem">%(gratis)s <b>Não inclui passagem aérea, alimentação nem seguro</b> — é o custo de fazer %(nome)s, não o de chegar nela.</p>
<p style="color:var(--nevoa);font-size:.92rem">Fontes: %(fonte)s</p>
<div class="paginas"><a class="pg" href="%(destino)s">Os 16 pontos de %(nome)s, com preço, horário e fonte</a></div></section>
</div>""" % dict(
        slug=c["slug"], hid="" if primeira else " hidden", d=d,
        volta=10 + d - 1, opts=opts, nota=c["nota"],
        cfg=json.dumps(cfg, ensure_ascii=False),
        linhas="".join(linhas), total=fmt(c, total),
        dia=c["moeda"] + " " + "{:,}".format(int(round(total / d))).replace(",", "."),
        gratis=c["gratis"], nome=c["nome"], fonte=c["fonte"], destino=c["destino"])

if __name__ == "__main__":
    import io
    for c in (RIO, LISBOA):
        io.open("/home/claude/calc/%s.html" % c["slug"], "w", encoding="utf-8").write(bloco(c, False))
        print(c["nome"], "ok")
