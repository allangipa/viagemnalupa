# -*- coding: utf-8 -*-
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import ficha
from g1 import G1
from g2 import G2
from g3 import G3
from g4 import G4

CRED = json.load(open('/home/claude/lisboa/creditos.json', encoding='utf-8'))
GRUPOS = [G1, G2, G3, G4]
CSSV = "68fde8e7"
TITULO = "Lisboa: 16 pontos turísticos com preço e horário"
DESC = ("Preço, horário e endereço de 16 pontos de Lisboa e Sintra, com o que mudou em 2026 — "
        "ascensores fechados, elétrico 28 desviado, Torre de Belém com teto diário e o controlo "
        "biométrico na fronteira. Apurado em 13/set/2026.")

def indice():
    cols, n = [], 0
    for g in GRUPOS:
        itens = []
        for p in g["pontos"]:
            n += 1
            itens.append('<a class="idx-item" href="#%s"><span class="idx-num">%02d</span>'
                         '<span class="idx-nome">%s</span><span class="idx-preco">%s</span></a>'
                         % (p["id"], n, p["nome"], p["preco"]))
        cols.append('<div><div class="idx-tit">%s</div>%s</div>' % (g["titulo"], "".join(itens)))
    return '<div class="idx-cols">%s</div>' % "".join(cols)

def corpo():
    out, n = [], 0
    for g in GRUPOS:
        fichas = []
        for p in g["pontos"]:
            n += 1
            fichas.append(ficha(n, p, CRED))
        out.append('<section class="grupo"><div class="grupo-head"><h2>%s</h2><p>%s</p></div>\n%s</section>'
                   % (g["titulo"], g["intro"], "\n".join(fichas)))
    return "\n".join(out)

def jsonld():
    base = "https://viagemnalupa.com.br/destinos/lisboa/"
    dest = {"@context":"https://schema.org","@type":"TouristDestination","name":"Lisboa",
            "description":DESC,"url":base,"inLanguage":"pt-BR",
            "geo":{"@type":"GeoCoordinates","latitude":38.7223,"longitude":-9.1393},
            "containedInPlace":{"@type":"City","name":"Lisboa","address":{
                "@type":"PostalAddress","addressLocality":"Lisboa","addressCountry":"PT"}}}
    itens, n = [], 0
    for g in GRUPOS:
        for p in g["pontos"]:
            n += 1
            itens.append({"@type":"ListItem","position":n,"item":{
                "@type":"TouristAttraction","name":p["nome"],"url":base+"#"+p["id"],
                "address":{"@type":"PostalAddress","addressLocality":"Lisboa","addressCountry":"PT"},
                "image":"https://viagemnalupa.com.br/assets/img/lisboa/%s.webp" % p["img"]}})
    lista = {"@context":"https://schema.org","@type":"ItemList",
             "name":"16 pontos turísticos de Lisboa","numberOfItems":n,"itemListElement":itens}
    mig = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Início","item":"https://viagemnalupa.com.br/"},
        {"@type":"ListItem","position":2,"name":"Destinos","item":"https://viagemnalupa.com.br/destinos/"},
        {"@type":"ListItem","position":3,"name":"Lisboa","item":base}]}
    return "\n".join('<script type="application/ld+json">%s</script>'
                     % json.dumps(o, ensure_ascii=False, separators=(",",":"))
                     for o in (dest, lista, mig))

AVISOS = """<div class="aviso a"><span class="t">Os ascensores históricos de Lisboa estão parados — e isso reescreve o roteiro do centro</span><p>Em <b>3 de setembro de 2025 o Ascensor da Glória descarrilou e matou 16 pessoas</b>, deixando 24 feridas. A Carris suspendeu preventivamente todos os ascensores históricos. Um ano depois, este é o quadro: a <b>Glória não será reparada e sim substituída</b> por equipamento novo, com concurso internacional até ao primeiro trimestre de 2027 e operação estimada só para <b>2029</b>; a <b>Bica</b> e o <b>Lavra</b> seguem fechados sem data; e o <b>Elevador de Santa Justa está fechado</b>, cabine e miradouro.</p><p><b>O único que voltou é o Funicular da Graça</b>, desde 30 de abril de 2026 — e ele serve justamente a subida para os miradouros de Alfama.</p><p><b>Repare no que isso significa para quem planeja:</b> a página oficial do metrô de Lisboa <b>ainda lista o Santa Justa e a Bica como ligações à superfície</b>, sem qualquer aviso de que estão encerrados, e o tarifário da Carris continua a publicar o preço deles. Se você montou o roteiro por uma tabela de preços oficial, montou com informação incompleta.</p></div><div class="aviso b"><span class="t">E mais três coisas mudaram de lugar em 2026</span><p><b>O elétrico 28 não parte mais de Martim Moniz.</b> Desde 24 de agosto de 2026, o troço até a Graça é feito por autocarro e o elétrico só circula entre <b>Graça e Campo de Ourique</b>. Há integração tarifária no transbordo — você não paga duas vezes — mas <b>a Carris não publicou data de término</b>. Se o seu plano era pegar o 28 em Martim Moniz, comece na Graça.</p><p><b>A Torre de Belém reabriu com teto diário.</b> Esteve fechada cerca de um ano e voltou em maio de 2026 com <b>lotação máxima de 900 visitantes por dia</b>, em sessões de 30 minutos com 60 pessoas cada. Qualquer guia anterior a maio está errado. O bilhete também se compra na bilheteira do Mosteiro dos Jerónimos — dá para resolver a torre enquanto você está no mosteiro.</p><p><b>O Gulbenkian reabriu.</b> A Coleção do Fundador esteve fechada quinze meses e voltou em <b>18 de julho de 2026</b>. Sites revendedores de bilhete ainda a listam como encerrada.</p></div><div class="aviso"><span class="t">Acabou o dia grátis para quem não mora em Portugal</span><p>Os monumentos do Estado — Jerónimos, Torre de Belém, Museu dos Coches — <b>não têm mais o “domingo de manhã gratuito”</b>. O que existe hoje é o <b>Acesso 52</b>: 52 entradas gratuitas por ano <b>exclusivas para quem reside em Portugal</b>, com Cartão de Cidadão, e o bilhete só sai na bilheteira física. <b>Para o turista brasileiro, não há dia grátis nesses monumentos.</b></p><p>No <b>Castelo de São Jorge</b> a mudança foi ainda mais dura, e atingiu o próprio lisboeta: por decisão judicial com efeito em <b>3 de julho de 2025</b>, acabou a gratuidade para morador de Lisboa, que vigorava desde 2005. Hoje o carioca e o alfacinha pagam os mesmos € 17.</p><p><b>Onde ainda há gratuidade que serve a você:</b> o <b>Gulbenkian</b> é grátis aos domingos a partir das 14h — e por isso mesmo é o horário mais cheio da semana. O <b>Padrão dos Descobrimentos</b> tem gratuidade dominical, mas só para residente no concelho de Lisboa. E há três pontos que nunca cobram: os <b>miradouros de Alfama</b>, a <b>Praça do Comércio</b> e o <b>acesso ao Cabo da Roca</b>.</p></div><div class="aviso a"><span class="t">O calendário de fechos: cada dia da semana mata um pedaço do roteiro</span><p><b>Segunda-feira é o pior dia de Belém:</b> Jerónimos, Torre de Belém e Museu dos Coches fecham todos. <b>Só o Padrão dos Descobrimentos abre</b> — ele é quem resolve a segunda.</p><p><b>Terça-feira mata o Gulbenkian.</b> O jardim continua aberto, de graça, do nascer ao pôr do sol; as galerias, não. O plano B da terça é o <b>Oceanário</b>, que abre todos os dias do ano, sem exceção nem feriado.</p><p><b>Sábado, domingo e feriado:</b> nada disso afeta Belém nem Sintra, mas note que o <b>Castelo de São Jorge</b> fecha às 12h30 do dia 31 de dezembro e encerra em 1 de janeiro, 1 de maio, 24 e 25 de dezembro.</p><p><b>E há uma armadilha de horário dentro do horário:</b> no Castelo de São Jorge, <b>os adarves e as torres fecham antes do monumento</b> — no verão, entre as 18h e as 21h, conforme a luz. Entrar às 19h30 em agosto com bilhete válido pode significar encontrar a muralha, que é a parte fotogénica, já fechada.</p></div><div class="aviso b"><span class="t">O Lisboa Card compensa a partir de duas entradas por dia</span><p>Preços em vigor de abril de 2026 a março de 2027: <b>24h € 31, 48h € 51, 72h € 62</b> para adulto; € 21, € 28 e € 35 para criança de 4 a 15 anos. Inclui transporte público ilimitado — metro, Carris, elétricos, e os comboios urbanos para Sintra e Cascais.</p><p><b>A conta, com os preços que apuramos:</b> o passe de transporte de 24h com comboio custa € 11,40 sozinho. Some uma entrada nos Jerónimos, a € 18, e já dá € 29,40 — <b>falta € 1,60 para compensar</b>. Some duas entradas grandes, Jerónimos e Torre, e dá € 44,40 contra os € 31 do cartão: <b>folga de € 13,40</b>. Ou seja, <b>o de 24h compensa a partir de duas entradas no dia</b>; o de 48h, a partir de duas entradas grandes no total; o de 72h, com apenas duas. Quanto mais dias, mais fácil compensar, porque o transporte incluído vira a parte pesada do valor.</p><p><b>Onde o cartão dá entrada livre:</b> Jerónimos, Torre de Belém, Castelo de São Jorge, Museu dos Coches, Padrão dos Descobrimentos e o Arco da Rua Augusta. <b>Onde dá só desconto:</b> Gulbenkian 20%, Regaleira 20%, Oceanário 15% e Palácio da Pena 10%. <b>Repare que os três lugares que quase todo brasileiro quer ver — Oceanário, Pena e Regaleira — não são grátis com o cartão.</b></p><p><b>E há uma armadilha no cartão infantil:</b> crianças <b>até 12 anos já entram de graça</b> em Jerónimos, Torre, Castelo e Padrão. O cartão de criança, a € 21, compra basicamente transporte. <b>Só passa a fazer sentido dos 13 aos 15 anos</b>, quando o menor já paga meia nos monumentos nacionais.</p><p>O que se compra online é um <b>voucher</b>, trocado presencialmente por cartão físico. <b>A ativação é manual</b> e o relógio começa a correr quando você escreve a data e valida num transporte — não quando retira.</p></div><div class="aviso"><span class="t">A taxa turística não está no preço da sua reserva</span><p><b>Lisboa cobra € 4 por pessoa por noite</b>, no máximo 7 noites, a partir dos 13 anos. Dobrou de € 2 para € 4 em <b>1 de setembro de 2024</b>. <b>Sintra cobra € 2</b>, no máximo 3 noites consecutivas; <b>Cascais cobra € 2</b>, até 7 noites.</p><p><b>Paga-se no alojamento, no check-in ou no check-out — não vem no valor do Booking nem do Airbnb.</b> Um casal, cinco noites em Lisboa: <b>€ 40 fora do preço da reserva</b>, cerca de R$ 237. É pouco por noite e muito quando aparece de uma vez, no balcão.</p></div><div class="aviso a"><span class="t">Fronteira: o controlo biométrico está a 100% desde 6 de setembro</span><p>O <b>EES</b>, o sistema de entradas e saídas da União Europeia, opera desde outubro de 2025 e está plenamente em vigor desde abril de 2026. Acabou o carimbo no passaporte: recolhe-se <b>rosto e impressões digitais</b>.</p><p><b>E Portugal foi o caso mais problemático da Europa.</b> Entre dezembro de 2025 e março de 2026 o país chegou a <b>suspender o EES</b> por causa de filas de <b>até oito horas</b> em Lisboa; em abril voltaram as esperas de horas e passageiros perderam conexões. Depois de reforço de agentes e mais portas automáticas, a média de espera caiu para cerca de 13 minutos em junho. <b>Em 27 de agosto de 2026 o primeiro-ministro anunciou controlo biométrico a 100% a partir de 6 de setembro</b> — ou seja, o regime mais rigoroso entrou em vigor há uma semana, e a janela de suspensão em picos expirou.</p><p><b>Tradução prática: se você tem conexão em Lisboa, deixe muito mais folga.</b> O histórico de 2026 vai de oito horas a treze minutos, e não há garantia de qual cenário você pega. A primeira entrada, com o cadastro completo, é a mais lenta.</p><p><b>O ETIAS ainda não vale, e não há data.</b> O portal oficial da UE diz que começa “no último trimestre de 2026” e que a data específica será anunciada “vários meses antes”. Estamos em setembro de 2026, faltam menos de quatro meses, e <b>essa data não foi anunciada</b> — há motivo concreto para duvidar que comece este ano. Quando começar, custará € 7 e valerá até 3 anos. <b>Hoje você não precisa de ETIAS para ir a Portugal.</b></p><p><b>O que a fronteira pode exigir:</b> passaporte com 3 meses de validade além da saída, comprovativo de alojamento, passagem de regresso, seguro com cobertura mínima de € 30.000 e meios de subsistência. <span class="flag">Não confirmado</span> os valores de subsistência que circulam — € 75 por entrada mais € 40 por dia — vêm de uma portaria de 2007 e <b>não conseguimos verificar se foram atualizados</b> em quase 19 anos: os sites oficiais bloquearam a consulta.</p></div><div class="aviso"><span class="t">As cotações e o que não medimos</span><p><b>1 EUR = R$ 5,92</b> e <b>1 EUR = US$ 1,16</b> — taxas de referência do <b>Banco Central Europeu de 11 de setembro de 2026</b>. Usamos a de sexta-feira porque o BCE só publica em dias úteis e a apuração é de domingo. O próprio BCE diz que essas taxas são apenas informativas e não devem ser usadas como taxa de transação: <b>o câmbio do seu cartão será pior, e ainda leva IOF</b>. Use os valores em real como ordem de grandeza, não como preço final.</p><p><b>Sobre o campo “menor visitação”:</b> <b>nenhum dos 16 pontos publica visitação mês a mês.</b> Nem os monumentos do Estado, nem a EGEAC, nem a Fundação Gulbenkian, nem o Oceanário, nem a Parques de Sintra. O que existe é total anual ou acumulado — e nós dizemos, em cada ficha, exatamente o que existe. Por isso, onde falamos de período mais vazio, estamos combinando <b>clima verificado</b> com <b>sazonalidade do turismo</b>, e dizemos isso na cara. Não é dado de bilheteira.</p><p>Para o clima usamos as <b>normais do IPMA, série 1991–2020</b>, de 30 anos: a estação Lisboa / Instituto Geofísico para a cidade, e a estação <b>Cabo da Roca</b> para Sintra e a serra — porque o IPMA não publica ficha para a vila de Sintra, e a do Cabo da Roca é muito melhor que usar a de Lisboa. <b>Ressalva honesta:</b> essa estação fica a 141 metros de altitude, e o Palácio da Pena está acima dos 400. <b>A Pena é mais fria e mais húmida do que a nossa tabela mostra</b> — mas não aplicamos gradiente térmico, porque isso seria estimativa.</p></div>"""

PAINEL = """<div class="painel"><div class="pcel"><span class="rotp">Pontos gratuitos da lista</span><span class="big">4 de 16</span><span class="sub">Miradouros, Praça do Comércio, Time Out e o Cabo da Roca.</span></div><div class="pcel"><span class="rotp">Torre de Belém, desde maio de 2026</span><span class="big c">900</span><span class="sub">Visitantes por dia, em sessões de 30 minutos. É teto, não fila.</span></div><div class="pcel"><span class="rotp">Taxa turística, por pessoa e por noite</span><span class="big c">€ 4</span><span class="sub">Até 7 noites, paga no hotel. Não vem no preço da reserva.</span></div><div class="pcel"><span class="rotp">Temperatura em agosto</span><span class="big">29° / 19°</span><span class="sub">Máxima e mínima médias; 5 mm de chuva no mês.</span></div></div>"""

HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="IpjUvTgAQF5LxYdxAXXj2g3Qi-qh1KldEl7RelcQ9bo">
<title>%(t)s</title>
<meta name="description" content="%(d)s">
<link rel="canonical" href="https://viagemnalupa.com.br/destinos/lisboa/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Viagem na Lupa">
<meta property="og:title" content="%(t)s">
<meta property="og:description" content="%(d)s">
<meta property="og:url" content="https://viagemnalupa.com.br/destinos/lisboa/">
<meta property="og:image" content="https://viagemnalupa.com.br/assets/img/lisboa/jeronimos.webp">
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
<p class="migalhas"><a href="../../">Início</a> › <a href="../">Destinos</a> › Lisboa</p>
<div class="hero">
  <span class="eyebrow">Guia dos pontos turísticos</span>
  <h1>Lisboa: 16 pontos turísticos</h1>
  <p>Dezesseis pontos com preço em euro e conversão, horário de funcionamento, estação de metrô e o que não foi possível confirmar. Incluindo Sintra e o Cabo da Roca — e tudo o que mudou de lugar em 2026, que é muita coisa.</p>
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
  <div class="bloco-head"><span class="eyebrow">Continue</span><h2>As outras páginas de Lisboa</h2></div>
  <div class="paginas"> <a class="pg" href="quanto-custa/">Quanto custa 6 dias em Lisboa</a> <a class="pg" href="roteiro-6-dias/">Roteiro de 6 dias, dia a dia</a> </div>
</section>
</div>
</main>
<footer class="rodape"><div class="wrap cols">
<p><b>Preços verificados em 13 de setembro de 2026.</b> Cada página traz a data da própria apuração. Atrações com preço dinâmico podem variar conforme a data escolhida — reconfira no checkout.</p>
<p>Quando um dado não existe em fonte confiável, a lacuna fica escrita. Não preenchemos com estimativa.</p>
<p>© 2026 Viagem na Lupa · viagemnalupa.com.br</p>
</div></footer>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "a2b63bb9c39147728b617fa302c981dc"}'></script><!-- End Cloudflare Web Analytics -->

<script src="../../assets/js/streetview.js" defer></script>
</body>
</html>
"""

html = (HEAD % dict(t=TITULO, d=DESC, v=CSSV, ld=jsonld(), painel=PAINEL, avisos=AVISOS, idx=indice())
        + corpo() + "\n" + FOOT)

os.makedirs('/home/claude/out/lisboa-page', exist_ok=True)
open('/home/claude/out/lisboa-page/index.html','w',encoding='utf-8').write(html)
print("bytes:", len(html.encode('utf-8')))
print("fichas:", html.count('<article class="ponto"'))
print("div:", html.count('<div'), html.count('</div>'))
print("article:", html.count('<article'), html.count('</article>'))
