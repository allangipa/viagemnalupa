# -*- coding: utf-8 -*-
"""Ficha de custos de Cancun e Fortaleza.

Regra desta pagina, por decisao do Allan: entra o que tem dado concreto;
o que nao tem fica em branco, declarado, e FORA do total.

Fortaleza nao tem diaria de hospedagem publicada por orgao nenhum, e por
isso a ficha dela sai sem hospedagem - com o total dizendo, no proprio
rotulo, que e a viagem sem a hospedagem. O ficha.js foi ensinado a lidar
com isso; antes ele quebrava e a ficha perdia tambem os ingressos, que
estao apurados.
"""
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from dados import APURACAO  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SITE = "https://viagemnalupa.com.br"

# Todas as fichas de custo do site, para a barra "Calcular para".
CIDADES = [("nova-york", "Nova York"), ("santiago", "Santiago"),
           ("buenos-aires", "Buenos Aires"), ("maceio", "Maceió"),
           ("rio-de-janeiro", "Rio de Janeiro"), ("lisboa", "Lisboa"),
           ("montevideu", "Montevidéu"), ("orlando", "Orlando"),
           ("cancun", "Cancún"), ("fortaleza", "Fortaleza")]

FICHAS = {
    "cancun": {
        "nome": "Cancún", "dias": 5, "moeda": "MX$", "dec": 0,
        "titulo": "Quanto custa 5 dias em Cancún em 2026",
        "descricao": ("O custo de 5 dias em Cancún e na Riviera Maya, por pessoa, com as "
                      "duas bilheterias de Chichén Itzá somadas e o que não conseguimos "
                      "apurar dito na cara."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 17 de setembro de 2026."),
        "hosp": [{"k": "media", "rot": "Tarifa média da cidade (oficial)",
                  "ref": 1800, "mn": 1800, "mx": 1800}],
        "hospPadrao": "media",
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em peso "
                  "mexicano. Mude as datas e o número de pessoas, desmarque o que você "
                  "não vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
            "quarto. <b style=\"color:var(--gelo)\">A diária de MX$ 1.800 é a tarifa média "
            "de Cancún divulgada pela Secretaría de Turismo de Quintana Roo</b> — é média "
            "de cidade inteira, não de uma categoria, e a sua reserva pode ficar bem longe "
            "dela. <b>O transporte não está na conta</b>: não apuramos tarifa de ônibus nem "
            "de táxi da Zona Hoteleira. Linhas marcadas como não apuradas continuam fora "
            "do total."),
        "linhas": [
            ("hosp", None, "Hospedagem, 4 noites", "MX$ 7.200",
             "Tarifa média de Cancún, MX$ 1.800 a diária. <span class=\"flag\">Média de "
             "cidade inteira</span> divulgada pela Secretaría de Turismo de Quintana Roo e "
             "reproduzida pela imprensa local — <b>não é uma faixa por categoria</b>, e por "
             "isso não há hostel nem luxo para escolher aqui. Ocupação de 63% na medição "
             "de junho de 2026."),
            ("ingresso", 697, "Chichén Itzá", "MX$ 697",
             "<b>Duas cobranças somadas:</b> MX$ 105 do INAH federal mais MX$ 592 da taxa "
             "estadual de Yucatán, para estrangeiro. Mexicano paga MX$ 105 + MX$ 205. "
             "<span class=\"flag\">Fontes divergem</span> a imprensa mexicana publicou "
             "MX$ 571 para a taxa estadual em janeiro de 2026; a página do INAH diz "
             "MX$ 592. <b>Fica o maior.</b> Abre todos os dias, 8h às 16h."),
            ("ingresso", 580, "Isla Mujeres, ferry ida e volta", "MX$ 580",
             "Ultramar, tarifa de adulto. Criança paga MX$ 440. <b>A régua é altura, não "
             "idade:</b> acima de 1,20 m paga adulto. Sai de Puerto Juárez ou da Playa "
             "Tortugas pelo mesmo preço. <b>Entrar na ilha não se paga</b> — o que se paga "
             "é a travessia."),
            ("ingresso", 210, "Tulum", "MX$ 210",
             "De segunda a sábado, para estrangeiro; mexicano e residente pagam MX$ 105. "
             "<b>Praticamente dobrou em 2026</b> — era cerca de MX$ 104 em 2025. Abre 8h, "
             "<b>última entrada 15h30</b>. <span class=\"flag\">Não apurado</span> o Parque "
             "del Jaguar pode cobrar taxa própria por cima desta; não achamos o valor em "
             "fonte oficial."),
            ("ingresso", 210, "Museo Maya de Cancún e San Miguelito", "MX$ 210",
             "<b>Um bilhete, duas visitas:</b> o museu e a zona arqueológica no mesmo "
             "terreno. Mexicano paga MX$ 105. Fecha às segundas; de terça a domingo das 9h "
             "às 18h. Última entrada no museu às 17h e <b>em San Miguelito às 16h30</b>."),
            ("ingresso", 0, "Playa Delfines", "Grátis",
             "No México <b>toda praia é federal e de acesso público</b>. "
             "<span class=\"flag\">Sem preço apurado</span> cadeira, guarda-sol e "
             "estacionamento não foram levantados e não entram na conta."),
            ("ingresso", 0, "Xcaret", "<span class=\"flag\">Fontes divergem</span>",
             "Apuramos <b>três valores no mesmo dia</b> para adulto: MX$ 1.890, MX$ 2.180 "
             "e MX$ 2.480, conforme a fonte e o tipo de bilhete; criança aparece a "
             "MX$ 1.660. <b>Não escolhemos nenhum, e por isso ficou fora do total.</b> "
             "O preço real é o que o site oficial mostrar para a sua data. "
             "<b>Some de MX$ 1.890 a MX$ 2.480 por conta própria se for.</b>"),
            ("ingresso", 0, "Transporte urbano",
             "<span class=\"flag\">Não apurado</span>",
             "Não levantamos tarifa de ônibus da Zona Hoteleira nem de táxi, e não vamos "
             "publicar número que não conferimos. <b>Fora do total.</b>"),
        ],
        "rodape_tabela": (
            "<b>Um ponto do guia não cobra nada:</b> a Playa Delfines. "
            "<b>Não estão incluídos</b>: passagem aérea, refeições, compras, seguro "
            "viagem, traslado do aeroporto, transporte urbano e o ingresso do Xcaret, que "
            "não tem preço fechado. É o custo de fazer Cancún, não o de chegar nela."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Apuração de 17 de setembro de 2026. Fontes: páginas oficiais do INAH para "
            "Chichén Itzá, Tulum e o Museo Maya de Cancún; tabela de tarifas da Ultramar "
            "para o ferry; e a tarifa média da cidade divulgada pela Secretaría de Turismo "
            "de Quintana Roo. <b>Nenhum valor desta página foi convertido para real.</b> "
            "A conversão automática pela PTAX do Banco Central existe em outras fichas do "
            "site e entra aqui quando tivermos a série do peso mexicano — o Banco Central "
            "publica só dez moedas, e o peso mexicano não está entre elas."),
    },

    "fortaleza": {
        "nome": "Fortaleza", "dias": 5, "moeda": "R$", "dec": 2,
        "titulo": "Quanto custa 5 dias em Fortaleza em 2026",
        "descricao": ("O custo de 5 dias em Fortaleza, por pessoa, com a taxa de "
                      "Jericoacoara que a Justiça suspendeu — e sem a hospedagem, porque "
                      "não há diária publicada."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas pesquisadas "
                     "em 17 de setembro de 2026. <b>Sem a hospedagem</b> — e a página "
                     "explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa. Mude as datas e o "
                  "número de pessoas, desmarque o que você não vai fazer, e a conta se "
                  "refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> Nenhum órgão publica diária média de Fortaleza: o FOHB divulga "
            "variação percentual por categoria, não valor, e não achamos série da cidade. "
            "Como a regra desta casa é não estimar, a hospedagem ficou de fora e o total "
            "diz isso no próprio rótulo. <b>Nas outras fichas do site a hospedagem é de "
            "75% a 85% do total</b> — some a sua reserva por fora e use este número só "
            "para o resto. O transporte também não entra: não apuramos tarifa."),
        "linhas": [
            ("ingresso", 250, "Beach Park, Aqua Park", "A partir de R$ 250",
             "Site oficial de ingressos. <b>Não existe preço fechado:</b> muda conforme a "
             "data e a antecedência da compra. <span class=\"flag\">Fontes divergem</span> "
             "sites de terceiros publicam faixa de R$ 210 a R$ 325 e prometem R$ 210 com "
             "44 dias de antecedência. <b>Entrou pelo piso oficial</b>, que é o mais baixo "
             "que o próprio parque anuncia. Criança até 1 metro não paga. 11h às 17h."),
            ("ingresso", 41.5, "Jericoacoara, taxa de entrada", "R$ 41,50",
             "Taxa de Turismo Sustentável da Prefeitura de Jijoca. <b>É a única taxa "
             "obrigatória hoje.</b> A concessão do Parque Nacional previa somar R$ 50 do "
             "ICMBio, <b>mas a Justiça Federal suspendeu a cobrança</b> e o TRF-5 rejeitou "
             "o recurso duas vezes, a última em dezembro de 2025. <b>Muito roteiro "
             "publicado ainda soma R$ 91,50.</b>"),
            ("ingresso", 10, "Theatro José de Alencar, visita guiada", "R$ 10",
             "Meia a R$ 5. <b>Criança até 5 anos e pessoa acima de 60 não pagam.</b> "
             "Visita mediada em horário fixo: 9h, 10h30, 14h e 16h de terça a sábado; "
             "<b>domingo só 9h e 10h30</b>. Fecha segunda. Chegar 20 minutos antes."),
            ("ingresso", 0, "Centro Dragão do Mar", "Grátis",
             "<b>Cerca de 90% da programação é gratuita ou de preço simbólico</b>, segundo "
             "o Instituto Dragão do Mar. O cinema custa de R$ 8 a R$ 16, e <b>às terças "
             "cai para R$ 5 a R$ 10</b> — como é opcional, não entrou no total. "
             "<b>O teatro e o planetário estão em manutenção</b>, sem data de reabertura."),
            ("ingresso", 0, "Mercado Central", "Grátis",
             "Entrada franca, mais de 600 lojas em cinco andares. "
             "<span class=\"flag\">Sem preço apurado</span> não levantamos faixa de preço "
             "de rede nem de artesanato."),
            ("ingresso", 0, "Catedral Metropolitana de São José", "Grátis",
             "Visitação de segunda a sexta das 8h às 12h e das 13h às 17h; sábado só de "
             "manhã. <b>Fecha das 12h às 13h</b>, e no domingo há missa, não visita."),
            ("ingresso", 0, "Praia do Futuro", "Grátis",
             "A praia não cobra. <span class=\"flag\">Sem preço apurado</span> consumação "
             "mínima e aluguel de mesa nas barracas não foram levantados e não entram na "
             "conta."),
            ("ingresso", 0, "Hospedagem",
             "<span class=\"flag\">Não apurada</span>",
             "<b>Nenhum órgão publica diária média de Fortaleza.</b> O FOHB divulga "
             "variação percentual por categoria — economia, midscale, upscale — e não "
             "valor absoluto da cidade. <b>Sem número, sem linha:</b> preferimos a conta "
             "incompleta e honesta à conta completa e inventada."),
            ("ingresso", 0, "Transporte urbano e traslados",
             "<span class=\"flag\">Não apurado</span>",
             "Não levantamos tarifa de ônibus, táxi ou transfer para Aquiraz e "
             "Jericoacoara. <b>São 27 km até o Beach Park e cerca de 300 km até Jeri</b>, "
             "então esta lacuna pesa. <b>Fora do total.</b>"),
        ],
        "rodape_tabela": (
            "<b>Quatro dos sete pontos do guia não cobram entrada:</b> Mercado Central, "
            "Catedral, Praia do Futuro e a maior parte da programação do Dragão do Mar. "
            "<b>Não estão incluídos</b>: hospedagem, passagem aérea, refeições, compras, "
            "seguro viagem, transporte urbano e os traslados. É o custo dos ingressos de "
            "Fortaleza, não o da viagem inteira — e o rótulo do total diz isso."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e pousadas"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Apuração de 17 de setembro de 2026. Fontes: site oficial de ingressos do "
            "Beach Park; Instituto Dragão do Mar; Arquidiocese de Fortaleza; Prefeitura de "
            "Jijoca de Jericoacoara para a Taxa de Turismo Sustentável; e as decisões da "
            "Justiça Federal e do TRF-5 sobre a suspensão da taxa do ICMBio. "
            "<b>A maior lacuna desta ficha é a diária de hospedagem</b>, e ela está "
            "declarada na tabela em vez de preenchida. Quando aparecer fonte que publique "
            "valor da cidade, a linha entra — com fonte e data, como todas as outras."),
    },
}


def barra_cidades(atual):
    partes = ['<nav class="calc-cidades" aria-label="Calculadora de outro destino">'
              '<span class="cc-rot">Calcular para</span>']
    for slug, nome in CIDADES:
        if slug == atual:
            partes.append('<span class="cc atual" aria-current="page">%s</span>' % nome)
        else:
            partes.append('<a class="cc" href="../../%s/quanto-custa/#calculadora">%s</a>'
                          % (slug, nome))
    partes.append("</nav>")
    return "".join(partes)


def seletor_hosp(f):
    if not f["hosp"]:
        return ""
    ops = "".join('<option value="%s"%s>%s</option>'
                  % (h["k"], " selected" if h["k"] == f["hospPadrao"] else "", h["rot"])
                  for h in f["hosp"])
    return ('\n      <label>Hospedagem\n        <select class="c-hosp">%s</select></label>'
            % ops)


SETA = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        '<path d="M7 17 L17 7 M9 7h8v8" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"></path></svg>')


def bloco_voo(nome):
    """Espaco reservado entre os marcadores que o coletor da Aviasales
    procura. O valor real entra na proxima rodada do workflow diario —
    o token nao fica no repositorio, entao nao da para coletar daqui.
    Ate la a pagina diz que ainda nao coletou, em vez de ficar sem nada."""
    return ('<!-- voo:inicio -->\n'
            '<section class="bloco" id="voo">\n'
            '  <div class="bloco-head"><span class="eyebrow">Chegar</span>'
            '<h2>Quanto custa a passagem</h2></div>\n'
            '  <p style="color:var(--nevoa)">A passagem é o item que esta ficha '
            '<b>não inclui</b> — e costuma ser, junto com a hospedagem, o maior gasto '
            'da viagem.</p>\n'
            '  <p style="color:var(--nevoa)"><span class="flag">Ainda não coletado</span> '
            'o preço de referência vem do cache de buscas reais da Aviasales e é '
            'atualizado uma vez por dia. <b>A rota São Paulo → %s entrou no site agora</b>, '
            'e o primeiro valor aparece aqui na próxima coleta.</p>\n'
            '</section>\n<!-- voo:fim -->\n' % nome)


def bloco_reserva(nome, ondes):
    """O bloco de parceiros. E tambem a ancora que o coletor de voos usa
    para saber onde inserir o bloco de passagem quando os marcadores
    ainda nao existem."""
    links = "".join(
        '<a class="parceiro" href="%s" target="_blank" rel="noopener">'
        '<span class="p-nome">%s%s</span><span class="p-nota">%s</span></a>'
        % (url, rot, SETA, nota) for url, rot, nota in ondes)
    return (
        '<section class="bloco">\n'
        '  <div class="reserva">\n'
        '    <div class="reserva-topo">\n'
        '      <h3>Onde conferimos os preços de %s</h3>\n'
        '      <p>Foi nestes serviços que checamos os valores desta página. Use-os para '
        'ver o preço da <b>sua</b> data — preço de viagem muda, e o nosso número é o do '
        'dia da apuração.</p>\n'
        '      <p style="color:var(--nevoa);font-size:.9rem"><b>Estes links dão comissão '
        'ao site.</b> Você paga o mesmo preço que pagaria indo direto, e a comissão '
        '<b>não altera nenhum número desta ficha</b> — os valores acima saem de fonte '
        'oficial, com a data da apuração. <a href="../../../sobre/">Como isso '
        'funciona</a>.</p>\n'
        '    </div>\n'
        '    <div class="reserva-lista">%s</div>\n'
        '  </div>\n'
        '</section>\n' % (nome, links))


def linha(tipo, valor, item, mostra, obs, extra=None):
    """Uma linha da tabela.

    O sexto elemento, opcional, sao os data-* que alguns tipos precisam e
    que o ingresso nao usa. O ficha.js le:

        taxa    data-noite, data-teto (opcional), data-rot com {n}
        metro   data-dia, data-teto
        dia     data-rot com {d}, data-grupo

    Entrou com o Porto, primeira ficha destes geradores com taxa
    municipal e transporte apurado. As quatro anteriores so tinham
    ingresso, e por isso o parametro e opcional.
    """
    attrs = 'data-tipo="%s"' % tipo
    if valor is not None:
        attrs += ' data-v="%.4f"' % valor
    for k, v in sorted((extra or {}).items()):
        attrs += ' data-%s="%s"' % (k, v)
    return ('<tr %s><td>%s</td><td class="n">%s</td><td>%s</td></tr>'
            % (attrs, item, mostra, obs))


CABECA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="IpjUvTgAQF5LxYdxAXXj2g3Qi-qh1KldEl7RelcQ9bo">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<link rel="canonical" href="{site}/destinos/{slug}/quanto-custa/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Viagem na Lupa">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:url" content="{site}/destinos/{slug}/quanto-custa/">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='112 102 583 583'%3E%3Ccircle cx='352' cy='342' r='196' stroke='%23FFB703' stroke-width='58' fill='none'/%3E%3Cpath d='M491 481 L648 638' stroke='%23FFB703' stroke-width='64' stroke-linecap='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../../../assets/css/site.css?v=0">
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="bar"><div class="wrap bar-in">
<a class="marca" href="../../../"><svg width="30" height="30" viewBox="112 102 583 583" fill="none" aria-hidden="true">
  <circle cx="352" cy="342" r="196" stroke="#FFB703" stroke-width="58"></circle>
  <path d="M491 481 L648 638" stroke="#FFB703" stroke-width="64" stroke-linecap="round"></path>
  <path d="M282 396 L336 320 L392 372 L446 268" stroke="#2EC4B6" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"></path>
</svg><span>VIAGEM NA LUPA</span></a>
<nav><a href="../../../destinos/" aria-current="page">Destinos</a><a href="../../../calculadora/">Calculadora</a><a href="../../../sobre/">Sobre</a><a class="externo" href="https://www.youtube.com/@viagemnalupa" target="_blank" rel="noopener">YouTube<span class="so-leitor"> (abre em outra aba)</span><svg class="seta-ext" width="11" height="11" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 17 L17 7 M9 7h8v8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"></path></svg></a></nav>
</div></header>
<main id="conteudo">
<div class="faixa"><div class="wrap wrap-estreito">
<p class="migalhas"><a href="../../../">Início</a> › <a href="../../">Destinos</a> › <a href="../">{nome}</a> › Quanto custa</p>
<div class="hero">
  <span class="eyebrow">Ficha de custos</span>
  <h1>Quanto custa {dias} dias em {nome}</h1>
  <p>{abertura}</p>
</div>
</div></div>

<div class="wrap wrap-estreito">
<div class="ficha-calc" data-cidade="{slug}">
"""

RODAPE = """</div>
</main>
<footer class="rodape"><div class="wrap cols">
<p><b>Tarifas verificadas em {apuracao}.</b> Cada página traz a data da própria apuração. Atrações com preço dinâmico podem variar conforme a data escolhida — reconfira no checkout.</p>
<p>Quando um dado não existe em fonte confiável, a lacuna fica escrita. Não preenchemos com estimativa.</p>
<p>© 2026 Viagem na Lupa · viagemnalupa.com.br · <a href="../../../privacidade/">Privacidade</a></p>
</div></footer>
<script src="../../../assets/js/ficha.js?v=0" defer></script>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a2b63bb9c39147728b617fa302c981dc"}}'></script><!-- End Cloudflare Web Analytics -->

</body>
</html>
"""


def monta(slug):
    f = FICHAS[slug]
    hoje = "2026-09-17"
    html = CABECA.format(titulo=f["titulo"], descricao=f["descricao"], site=SITE,
                         slug=slug, nome=f["nome"], dias=f["dias"],
                         abertura=f["abertura"])

    cfg = {"moeda": f["moeda"], "dec": f["dec"], "dias": f["dias"], "pessoas": 1,
           "hosp": f["hosp"], "hospPadrao": f["hospPadrao"],
           "janela": None, "eventos": []}

    html += (
        '<section class="bloco" id="calculadora">\n'
        '  <div class="bloco-head">\n'
        '    <span class="eyebrow">Calculadora</span>\n'
        '    <h2>Faça a conta da <em style="font-style:normal;color:var(--ambar)">sua</em> viagem</h2>\n'
        '    <p>%s</p>\n'
        '  </div>\n'
        '  %s\n'
        '  <div class="calc" hidden>\n'
        '    <span class="t">Sua viagem</span>\n'
        '    <div class="calc-ctrl">\n'
        '      <label>Chegada\n'
        '        <input type="date" class="c-ida" value="2026-11-10" min="%s" max="2028-12-31"></label>\n'
        '      <label>Volta\n'
        '        <input type="date" class="c-volta" value="2026-11-14" min="%s" max="2028-12-31"></label>\n'
        '      <label>Pessoas\n'
        '        <input type="number" class="c-pes" min="1" max="8" step="1" value="1" inputmode="numeric"></label>%s\n'
        '    </div>\n'
        '    <p class="calc-dur c-dur"></p>\n'
        '    <div class="c-alertas"></div>\n'
        '    <p class="calc-nota">%s</p>\n'
        '    <div class="painel res"></div>\n'
        '  </div>\n'
        '  <script type="application/json" class="calc-cfg">%s</script>\n'
        '</section>\n'
        % (f["intro"], barra_cidades(slug), hoje, hoje, seletor_hosp(f),
           f["nota_calc"], json.dumps(cfg, ensure_ascii=False)))

    corpo = "".join(linha(*l) for l in f["linhas"])
    # O total impresso e o da viagem padrao, o que o leitor sem JavaScript
    # ve. Ate o Porto so havia linha de ingresso, e somar ingresso bastava.
    # Agora ha taxa municipal e transporte, que tambem sao custo - de fora
    # fica so "hosp", que o seletor de hospedagem trata a parte. Nas quatro
    # fichas anteriores a soma nao muda: elas nao tem linha de outro tipo
    # com valor, e isso foi conferido antes de trocar.
    total = sum(v for t, v, *_ in f["linhas"] if t != "hosp" and v)
    if f["hosp"]:
        total += f["hosp"][0]["ref"] * (f["dias"] - 1)
    rot = "Total por pessoa" + ("" if f["hosp"] else ", sem a hospedagem")
    # Casas decimais pela moeda: peso e dolar sem centavo, euro com. O
    # "{:,.0f}" fixo escreveria "EUR 125" onde a conta da 125,25. A troca
    # de separador e feita em duas partes para nao precisar de sentinela.
    inteiro, _, cent = ("{:,.%df}" % f.get("dec", 0)).format(total).partition(".")
    fmt = "%s %s" % (f["moeda"],
                     inteiro.replace(",", ".") + ("," + cent if cent else ""))
    html += (
        '<section class="bloco">\n'
        '  <div class="bloco-head"><span class="eyebrow">A apuração</span>'
        '<h2>Linha a linha, com a fonte de cada número</h2></div>\n'
        '  <div class="tabwrap"><table class="tab-ficha">'
        '<thead><tr><th>Item</th><th>Valor</th><th>Observação</th></tr></thead>'
        '<tbody>%s</tbody>'
        '<tfoot><tr><td class="tot-rot">%s</td><td class="n tot-val">%s</td>'
        '<td class="tot-dia">%s por pessoa por dia</td></tr></tfoot></table></div>\n'
        '  <p style="color:var(--nevoa);font-size:.92rem">%s</p>\n'
        '</section>\n'
        % (corpo, rot, fmt,
           "%s %s" % (f["moeda"], "{:,.0f}".format(total / f["dias"]).replace(",", ".")),
           f["rodape_tabela"]))

    html += bloco_voo(f["nome"])
    html += bloco_reserva(f["nome"], f["parceiros"])
    html += ('<section class="bloco"><div class="aviso"><span class="t">Onde conferimos '
             'estes preços</span><p>%s</p></div></section>\n' % f["fontes"])
    html += ('<section class="bloco"><div class="paginas">\n'
             '  <a class="pg" href="../">Guia dos pontos, com preço e horário</a>\n'
             '  <a class="pg" href="../roteiro-%d-dias/">Roteiro de %d dias</a>\n'
             '</div></section>\n' % (f["dias"], f["dias"]))
    html += RODAPE.format(apuracao=APURACAO)
    return html


def main(aplica):
    for slug, f in FICHAS.items():
        pasta = os.path.join(RAIZ, "destinos", slug, "quanto-custa")
        html = monta(slug)
        print("  %-12s %d linhas, hospedagem:%s, %d KB%s"
              % (slug, len(f["linhas"]), "sim" if f["hosp"] else "NAO",
                 len(html.encode("utf-8")) / 1024, "" if aplica else "   (ensaio)"))
        if aplica:
            os.makedirs(pasta, exist_ok=True)
            with open(os.path.join(pasta, "index.html"), "w",
                      encoding="utf-8", newline="") as fh:
                fh.write(html)
    if not aplica:
        print()
        print("Nada escrito. Rode com --aplica.")


if __name__ == "__main__":
    main("--aplica" in sys.argv)
