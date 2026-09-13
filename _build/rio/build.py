# -*- coding: utf-8 -*-
import json, sys, io, re
sys.path.insert(0, '/home/claude/rio/build')
from lib import ficha
from g1 import G1
from g2 import G2
from g3 import G3
from g4 import G4

CRED = json.load(open('/home/claude/rio/creditos.json', encoding='utf-8'))
GRUPOS = [G1, G2, G3, G4]
CSSV = "68fde8e7"
TITULO = "Rio de Janeiro: 16 pontos turísticos com preço e horário"
DESC = ("Preço, horário e endereço de 16 pontos do Rio, com as três obras e restrições em vigor "
        "agora — Cristo a 50% da capacidade, palacete do Parque Lage fechado e Vista Chinesa sem "
        "carro no fim de semana. Apurado em 13/set/2026.")

# ---------- índice ----------
def indice():
    cols = []
    n = 0
    for g in GRUPOS:
        itens = []
        for p in g["pontos"]:
            n += 1
            itens.append('<a class="idx-item" href="#%s"><span class="idx-num">%02d</span>'
                         '<span class="idx-nome">%s</span><span class="idx-preco">%s</span></a>'
                         % (p["id"], n, p["nome"], p["preco"]))
        cols.append('<div><div class="idx-tit">%s</div>%s</div>' % (g["titulo"], "".join(itens)))
    return '<div class="idx-cols">%s</div>' % "".join(cols)

# ---------- corpo ----------
def corpo():
    out = []
    n = 0
    for g in GRUPOS:
        fichas = []
        for p in g["pontos"]:
            n += 1
            fichas.append(ficha(n, p, CRED))
        out.append('<section class="grupo"><div class="grupo-head"><h2>%s</h2><p>%s</p></div>\n%s</section>'
                   % (g["titulo"], g["intro"], "\n".join(fichas)))
    return "\n".join(out)

# ---------- JSON-LD ----------
def jsonld():
    base = "https://viagemnalupa.com.br/destinos/rio-de-janeiro/"
    dest = {"@context":"https://schema.org","@type":"TouristDestination","name":"Rio de Janeiro",
            "description":DESC,"url":base,"inLanguage":"pt-BR",
            "geo":{"@type":"GeoCoordinates","latitude":-22.9068,"longitude":-43.1729},
            "containedInPlace":{"@type":"City","name":"Rio de Janeiro","address":{
                "@type":"PostalAddress","addressLocality":"Rio de Janeiro",
                "addressRegion":"RJ","addressCountry":"BR"}}}
    itens = []
    n = 0
    for g in GRUPOS:
        for p in g["pontos"]:
            n += 1
            itens.append({"@type":"ListItem","position":n,"item":{
                "@type":"TouristAttraction","name":p["nome"],
                "url":base+"#"+p["id"],
                "address":{"@type":"PostalAddress","addressLocality":"Rio de Janeiro",
                           "addressRegion":"RJ","addressCountry":"BR"},
                "image":"https://viagemnalupa.com.br/assets/img/rio-de-janeiro/%s.webp" % p["img"]}})
    lista = {"@context":"https://schema.org","@type":"ItemList",
             "name":"16 pontos turísticos do Rio de Janeiro","numberOfItems":n,
             "itemListElement":itens}
    migalhas = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Início","item":"https://viagemnalupa.com.br/"},
        {"@type":"ListItem","position":2,"name":"Destinos","item":"https://viagemnalupa.com.br/destinos/"},
        {"@type":"ListItem","position":3,"name":"Rio de Janeiro","item":base}]}
    return "\n".join('<script type="application/ld+json">%s</script>'
                     % json.dumps(o, ensure_ascii=False, separators=(",",":"))
                     for o in (dest, lista, migalhas))

AVISOS = """<div class="aviso a"><span class="t">Três pontos estão com obra ou restrição em vigor agora</span><p><b>Cristo Redentor:</b> as quatro escadas rolantes que levam ao mirante estão desligadas desde 3 de agosto de 2026, para serem trocadas. Sem elas, <b>cabe metade das pessoas lá em cima ao mesmo tempo</b> — e por isso o parque passou a vender metade dos ingressos. A obra vai <b>até o fim de maio de 2027</b>. Na prática: <b>o ingresso esgota dias antes</b>, então compre com antecedência e só por canal oficial. E, enquanto as escadas não voltam, <b>quem sobe encara 80 degraus de pedra</b> do 2º piso até o platô do Cristo; o ICMBio disponibiliza 5 carros e 5 cadeiras escaladoras para mobilidade reduzida. Fonte: Parque Nacional da Tijuca / ICMBio.</p><p><b>Parque Lage:</b> o palacete está fechado para restauro e deve reabrir só em <b>abril de 2027</b>. Os jardins seguem abertos, mas <b>o pátio interno com a piscina e o Cristo ao fundo — a foto que leva todo mundo ao Parque Lage — não está acessível</b>. Ainda não há definição sobre horários de visitação depois da entrega. Fonte: O Globo / Rio Show, reportando o Governo do Rio.</p><p><b>Vista Chinesa:</b> a estrada que sobe até o mirante, a Dona Castorina, <b>fecha para carros das 7h às 19h aos sábados, domingos e feriados</b>. Nesse intervalo você não chega lá de carro, de táxi nem de aplicativo — só a pé ou de bicicleta, numa subida longa e íngreme. A regra vale desde março de 2026 e é o erro número um de quem vai à Vista Chinesa no fim de semana.</p></div><div class="aviso b"><span class="t">Onde ser brasileiro, ou morar no Rio, corta o preço pela metade</span><p><b>Bondinho do Pão de Açúcar:</b> a inteira é R$ 205, mas nascido ou residente no <b>Estado do Rio paga R$ 89</b> — 57% de desconto — e <b>brasileiro de qualquer estado paga R$ 160</b>. Leve documento ou comprovante de residência; sem comprovação, a entrada é barrada ou é cobrada a diferença.</p><p><b>Cristo Redentor:</b> não há tarifa de morador, mas o <b>ponto de embarque muda o preço</b>. Saindo do Centro de Visitantes Paineiras, a van custa <b>R$ 87</b>; saindo de Copacabana ou do Largo do Machado, <b>R$ 132</b>. Mesmo destino, R$ 45 de diferença.</p><p><b>MAR:</b> é o único museu desta lista com faixa explícita de morador — <b>nascidos e moradores da cidade do Rio pagam meia, R$ 10</b>. E a <b>terça-feira é gratuita para todos</b>.</p><p><b>Jardim Botânico:</b> o desconto é por <b>residência no Brasil</b>, não por município: R$ 40 contra R$ 80 do estrangeiro. Não existe tarifa de carioca aqui.</p></div><div class="aviso"><span class="t">O calendário do Centro: cada endereço fecha num dia diferente</span><p>Esta é a armadilha que estraga um dia inteiro de roteiro no Centro. <b>Quarta-feira:</b> Museu do Amanhã e MAR fecham, e o Jardim Botânico só abre às 11h, com o Museu fechado. <b>Sábado, domingo e feriado:</b> o Real Gabinete Português de Leitura fecha — ele só abre de segunda a sexta, das 10h às 17h. <b>Domingo, segunda e terça:</b> não há visita guiada no Theatro Municipal, cuja grade vai de quarta a sábado. <b>Segunda-feira:</b> fecham o Forte de Copacabana e o Parque das Ruínas, em Santa Teresa. <b>Terça, domingo e feriado:</b> fecha o Museu da Chácara do Céu.</p><p>Traduzindo: <b>quinta e sexta-feira são os dois dias em que tudo do Centro está aberto ao mesmo tempo.</b> Quarta perde os dois museus do Porto; fim de semana perde o Real Gabinete.</p></div><div class="aviso a"><span class="t">As cotações e o que não medimos</span><p><b>1 USD ≈ R$ 5,12</b> — taxa de mercado de 11 a 13 de setembro de 2026 (Wise, com conferência no Investing.com). Todos os valores em dólar nesta página são <b>conversão nossa</b>, não preços cotados em dólar pelos estabelecimentos. Confira a cotação no dia.</p><p><b>Sobre o campo “menor visitação”:</b> <b>nenhum dos 16 pontos publica estatística de visitação mês a mês.</b> Nem o ICMBio, nem os museus, nem o Parque Bondinho, nem a Prefeitura. O que existe é total anual, acumulado histórico ou recorte parcial — e nós dizemos qual é em cada ficha. Por isso, onde falamos de período mais vazio, estamos combinando <b>clima verificado</b> (climatologia de 30 anos do Climatempo) com <b>sazonalidade do turismo carioca</b>, e dizemos isso na cara. Não é dado de bilheteria, e não vamos apresentá-lo como se fosse.</p><p>E há dois casos em que a intuição da baixa temporada <b>não vale</b>: o bonde de Santa Teresa bateu recorde diário justamente em julho, e o Theatro Municipal reforça a programação nas férias escolares. Nesses dois, inverno não significa menos gente.</p></div>"""

PAINEL = """<div class="painel"><div class="pcel"><span class="rotp">Pontos gratuitos da lista</span><span class="big">8 de 16</span><span class="sub">Praias, mirantes, floresta, arcos, escadaria e biblioteca.</span></div><div class="pcel"><span class="rotp">Cristo Redentor, até maio de 2027</span><span class="big c">50%</span><span class="sub">Com as escadas rolantes em obra, entra metade do público de sempre. Compre o ingresso com antecedência.</span></div><div class="pcel"><span class="rotp">Bondinho para quem mora no RJ</span><span class="big c">R$ 89</span><span class="sub">Contra R$ 205 da inteira. Leve comprovante.</span></div><div class="pcel"><span class="rotp">Temperatura em julho</span><span class="big">25° / 15°</span><span class="sub">Máxima e mínima médias; 37 mm de chuva.</span></div></div>"""

HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="IpjUvTgAQF5LxYdxAXXj2g3Qi-qh1KldEl7RelcQ9bo">
<title>%(t)s</title>
<meta name="description" content="%(d)s">
<link rel="canonical" href="https://viagemnalupa.com.br/destinos/rio-de-janeiro/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Viagem na Lupa">
<meta property="og:title" content="%(t)s">
<meta property="og:description" content="%(d)s">
<meta property="og:url" content="https://viagemnalupa.com.br/destinos/rio-de-janeiro/">
<meta property="og:image" content="https://viagemnalupa.com.br/assets/img/rio-de-janeiro/cristo.webp">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='112 102 583 583'%%3E%%3Ccircle cx='352' cy='342' r='196' stroke='%%23FFB703' stroke-width='58' fill='none'/%%3E%%3Cpath d='M491 481 L648 638' stroke='%%23FFB703' stroke-width='64' stroke-linecap='round'/%%3E%%3C/svg%%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../../assets/css/site.css?v=%(v)s">

%(ld)s</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="bar"><div class="wrap bar-in">
<a class="marca" href="../../"><svg width="30" height="30" viewBox="112 102 583 583" fill="none" aria-hidden="true">
  <circle cx="352" cy="342" r="196" stroke="#FFB703" stroke-width="58"></circle>
  <path d="M491 481 L648 638" stroke="#FFB703" stroke-width="64" stroke-linecap="round"></path>
  <path d="M282 396 L336 320 L392 372 L446 268" stroke="#2EC4B6" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"></path>
</svg><span>VIAGEM NA LUPA</span></a>
<nav><a href="../../destinos/" aria-current="page">Destinos</a><a href="../../calculadora/">Calculadora</a><a href="../../sobre/">Sobre</a><a class="externo" href="https://www.youtube.com/@viagemnalupa" target="_blank" rel="noopener">YouTube<span class="so-leitor"> (abre em outra aba)</span><svg class="seta-ext" width="11" height="11" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 17 L17 7 M9 7h8v8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"></path></svg></a></nav>
</div></header>
<main id="conteudo">
<div class="faixa"><div class="wrap">
<p class="migalhas"><a href="../../">Início</a> › <a href="../">Destinos</a> › Rio de Janeiro</p>
<div class="hero">
  <span class="eyebrow">Guia dos pontos turísticos</span>
  <h1>Rio de Janeiro: 16 pontos turísticos</h1>
  <p>Dezesseis pontos com preço em real e conversão, horário de funcionamento, estação de metrô e o que não foi possível confirmar. Incluindo as três obras e restrições em vigor agora, que mudam o roteiro de quem vai este ano.</p>
</div>
%(painel)s
<div style="height:clamp(1.4rem,3vw,2.2rem)"></div>
</div></div>

<div class="wrap">
<section class="bloco">%(avisos)s</section>
<section class="bloco">
  <div class="bloco-head"><span class="eyebrow">Os 16 pontos</span><h2>Índice</h2></div>
  %(idx)s
</section>
"""

FOOT = """<section class="bloco">
  <div class="bloco-head"><span class="eyebrow">Continue</span><h2>As outras páginas do Rio de Janeiro</h2></div>
  <div class="breve"><span class="bv">Quanto custa 5 dias no Rio — em apuração</span><span class="bv">Roteiro dia a dia — em apuração</span></div>
</section>
</div>
</main>
<footer class="rodape"><div class="wrap cols">
<p><b>Preços verificados em 13 de setembro de 2026.</b> Cada página traz a data da própria apuração. Atrações com preço dinâmico podem variar conforme a data escolhida — reconfira no checkout.</p>
<p>Quando um dado não existe em fonte confiável, a lacuna fica escrita. Não preenchemos com estimativa.</p>
<p>© 2026 Viagem na Lupa · viagemnalupa.com.br</p>
</div></footer>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "a2b63bb9c39147728b617fa302c981dc"}'></script><!-- End Cloudflare Web Analytics -->

</body>
</html>
"""

html = (HEAD % dict(t=TITULO, d=DESC, v=CSSV, ld=jsonld(), painel=PAINEL, avisos=AVISOS, idx=indice())
        + corpo() + "\n" + FOOT)

import os
os.makedirs('/home/claude/out/rio-page', exist_ok=True)
open('/home/claude/out/rio-page/index.html','w',encoding='utf-8').write(html)
print("bytes:", len(html.encode('utf-8')))
print("fichas:", html.count('<article class="ponto"'))
print("div abre/fecha:", html.count('<div'), html.count('</div>'))
print("section:", html.count('<section'), html.count('</section>'))
print("article:", html.count('<article'), html.count('</article>'))
