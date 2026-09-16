# -*- coding: utf-8 -*-
"""Preenche a lacuna que as oito fichas declaram: o preço da passagem aérea.

Fonte: Aviasales Data API, endpoint /aviasales/v3/prices_for_dates. Os
preços vêm do CACHE de buscas reais feitas por usuários nas últimas 48
horas — não são cotação. A própria documentação da Travelpayouts
recomenda usá-los para gerar página estática, que é exatamente o que
este script faz.

O TOKEN NUNCA ENTRA NO REPOSITÓRIO. Ele é lido de:
  1. a variável de ambiente AVIASALES_TOKEN  (é assim que a Action usa,
     vindo de secrets.AVIASALES_TOKEN), ou
  2. um arquivo apontado por AVIASALES_TOKEN_FILE, para teste local.

Uso:
    python _build/voos/atualiza.py            mostra o que faria
    python _build/voos/atualiza.py --aplica   grava nas fichas
"""
import io, json, os, re, sys, urllib.parse, urllib.request
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
API = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

ORIGEM = "SAO"          # São Paulo: GRU + CGH + VCP. O maior emissor do país.
MERCADO = "br"
MOEDA = "brl"

# slug da ficha -> (codigo IATA, nome como aparece no texto)
DESTINOS = {
    "lisboa":         ("LIS", "Lisboa"),
    "rio-de-janeiro": ("RIO", "o Rio de Janeiro"),
    "nova-york":      ("NYC", "Nova York"),
    "santiago":       ("SCL", "Santiago"),
    "buenos-aires":   ("BUE", "Buenos Aires"),
    "maceio":         ("MCZ", "Maceió"),
    "montevideu":     ("MVD", "Montevidéu"),
    "orlando":        ("MCO", "Orlando"),
}

MESES = ("janeiro fevereiro março abril maio junho julho agosto setembro "
         "outubro novembro dezembro").split()

# A API devolve o codigo IATA de duas letras da companhia. "pela AT" nao
# diz nada a ninguem, entao traduzimos o que aparece com frequencia nas
# rotas deste site e caimos no proprio codigo quando nao conhecemos.
CIAS = {
    "AD": "Azul", "G3": "Gol", "JJ": "LATAM", "LA": "LATAM", "O6": "Avianca",
    "AV": "Avianca", "CM": "Copa", "AR": "Aerolíneas Argentinas", "H2": "Sky Airline",
    "JA": "JetSmart", "WJ": "JetSmart", "AA": "American", "UA": "United", "DL": "Delta",
    "TP": "TAP", "IB": "Iberia", "UX": "Air Europa", "AF": "Air France", "KL": "KLM",
    "LH": "Lufthansa", "AZ": "ITA Airways", "TK": "Turkish", "EK": "Emirates",
    "QR": "Qatar", "AT": "Royal Air Maroc", "DM": "Arajet", "B6": "JetBlue",
    "F9": "Frontier", "NK": "Spirit", "WN": "Southwest", "AC": "Air Canada",
    "SQ": "Singapore", "ET": "Ethiopian", "MS": "EgyptAir", "SU": "Aeroflot",
}

MARCADOR = "775563"   # marcador de afiliado; e publico por natureza


def companhia(cod):
    if not cod:
        return None, None
    return CIAS.get(cod), cod


def token():
    t = os.environ.get("AVIASALES_TOKEN", "").strip()
    if t:
        return t
    caminho = os.environ.get("AVIASALES_TOKEN_FILE", "").strip()
    if caminho and os.path.exists(caminho):
        return io.open(caminho, encoding="utf-8").read().strip()
    raise SystemExit(
        "Token ausente. Defina AVIASALES_TOKEN (a Action faz isso pelo secret)\n"
        "ou AVIASALES_TOKEN_FILE apontando para um arquivo FORA do repositorio.")


def busca(destino, tk):
    q = urllib.parse.urlencode({
        "origin": ORIGEM, "destination": destino,
        "one_way": "false",          # o padrao da API e true; queremos ida e volta
        "sorting": "price",
        "direct": "false",
        "currency": MOEDA,
        "market": MERCADO,
        "limit": 5,
    })
    req = urllib.request.Request(API + "?" + q, headers={
        "X-Access-Token": tk,
        "Accept-Encoding": "identity",
        "User-Agent": "ViagemNaLupa/1.0 (https://viagemnalupa.com.br)",
    })
    with urllib.request.urlopen(req, timeout=45) as r:
        corpo = json.load(r)
    if not corpo.get("success"):
        return None, corpo.get("error") or "resposta sem success"
    dados = corpo.get("data") or []
    if not dados:
        return None, "cache vazio para esta rota"
    return sorted(dados, key=lambda x: x.get("price") or 10**9)[0], None


def brl(n):
    return "R$ " + "{:,}".format(int(round(n))).replace(",", ".")


def por_extenso(iso):
    try:
        a, m, d = iso[:10].split("-")
        return "%d de %s de %s" % (int(d), MESES[int(m) - 1], a)
    except Exception:
        return iso[:10]


def bloco(nome, v, hoje):
    if v is None:
        return ('<!-- voo:inicio -->\n'
                '<section class="bloco" id="voo">\n'
                '  <div class="bloco-head"><span class="eyebrow">Chegar</span><h2>Quanto custa a passagem</h2></div>\n'
                '  <p style="color:var(--nevoa)"><span class="flag">Sem preço no momento</span> '
                'consultamos o cache de buscas reais da Aviasales para <b>São Paulo → %s</b> e '
                '<b>não havia nenhuma busca recente</b> nessa rota. Isso acontece em trecho pouco '
                'procurado. Voltamos a consultar todo dia, e o valor aparece aqui quando existir.</p>\n'
                '</section>\n<!-- voo:fim -->' % nome)

    # A API separa ida e volta: "transfers" e SO da ida, e "return_transfers"
    # da volta. Ler so o primeiro faz anunciar "sem escala" um voo cuja volta
    # para noutro pais - foi o que quase aconteceu com Montevideu.
    def conta(n):
        if n == 0:
            return "sem escala"
        if n == 1:
            return "1 escala"
        return "%s escalas" % n

    ida, volta = v.get("transfers"), v.get("return_transfers")
    if ida == volta:
        txt_escalas = "%s nos dois trechos" % conta(ida) if ida == 0 else \
                      "%s em cada trecho" % conta(ida)
    else:
        txt_escalas = "ida %s, volta com %s" % (conta(ida), conta(volta))

    nome_cia, cod_cia = companhia(v.get("airline"))
    if nome_cia:
        txt_cia = "pela <b>%s</b>" % nome_cia
    elif cod_cia:
        txt_cia = "pela companhia de código <b>%s</b>" % cod_cia
    else:
        txt_cia = "companhia não informada"

    # Usamos duration_to e duration_back, que a documentacao define como o
    # tempo de cada voo. O campo "duration" devolve um numero que nao e a
    # soma dos dois e que nao conseguimos explicar - entao nao exibimos.
    def hm(m):
        return "%dh%02d" % (m // 60, m % 60)

    dt, db = v.get("duration_to"), v.get("duration_back")
    txt_dur = ""
    if dt and db:
        txt_dur = " <b>%s</b> na ida e <b>%s</b> na volta." % (hm(dt), hm(db))
    elif dt:
        txt_dur = " <b>%s</b> na ida." % hm(dt)

    # o campo link vem como caminho relativo; o marcador faz a atribuicao
    caminho = v.get("link") or ""
    if caminho:
        sep = "&" if "?" in caminho else "?"
        url = "https://www.aviasales.com" + caminho + sep + "marker=" + MARCADOR
        txt_link = ('  <div class="reserva"><div class="reserva-topo">'
                    '<h3>Ver esta rota com as suas datas</h3>'
                    '<p>O preço acima é do cache. Para ver o valor das <b>suas</b> datas, a busca '
                    'é aqui. <b>Este link dá comissão ao site</b>, e você paga o mesmo preço. '
                    '<a href="../../../sobre/">Como isso funciona</a>.</p></div>'
                    '<div class="reserva-lista"><a class="parceiro" href="%s" target="_blank" '
                    'rel="noopener sponsored"><span class="p-nome">Aviasales'
                    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
                    '<path d="M7 17 L17 7 M9 7h8v8" stroke="currentColor" stroke-width="2" '
                    'stroke-linecap="round" stroke-linejoin="round"></path></svg></span>'
                    '<span class="p-nota">passagens aéreas</span></a></div></div>\n') % url
    else:
        txt_link = ""

    return ('<!-- voo:inicio -->\n'
            '<section class="bloco" id="voo">\n'
            '  <div class="bloco-head"><span class="eyebrow">Chegar</span><h2>Quanto custa a passagem</h2></div>\n'
            '  <p style="color:var(--nevoa)">A passagem é o item que esta ficha <b>não inclui</b> — '
            'e costuma ser, junto com a hospedagem, o maior gasto da viagem. Então aqui está a '
            'referência que conseguimos, separada do total:</p>\n'
            '  <div class="painel"><div class="pcel"><span class="rotp">São Paulo → %s</span>'
            '<span class="big c">%s</span><span class="sub">Ida e volta %s — %s.%s</span></div></div>\n'
            '  <div class="aviso a"><span class="t">Leia o que este número é, e o que ele não é</span>'
            '<p><b>Não é uma cotação.</b> É o menor preço que <b>usuários reais encontraram nas '
            'últimas 48 horas</b> buscando essa rota, guardado em cache. Quando você buscar, o valor '
            'pode estar diferente — para mais ou para menos.</p>'
            '<p><b>A data de partida abaixo não é recomendação nossa</b> — é simplesmente o dia em que '
            'a passagem mais barata foi encontrada. Preço de voo depende tanto da data que ele diz '
            'mais sobre o calendário do que sobre a rota.</p>'
            '<p><b>A origem é São Paulo</b>, que é o maior aeroporto emissor do país. Saindo de outra '
            'cidade, a conta muda, e às vezes muito.</p>'
            '<p><b>Por isso ele não entra no total da ficha.</b> O total soma tarifa publicada e '
            'estimativa de hospedagem; preço de passagem não é nem uma coisa nem outra.</p></div>\n'
            '%s'
            '  <p style="color:var(--nevoa);font-size:.92rem">Consultado em <b>%s</b>. '
            'A passagem mais barata do cache partia em <b>%s</b>.</p>\n'
            '</section>\n<!-- voo:fim -->'
            % (nome, brl(v["price"]), txt_cia, txt_escalas, txt_dur, txt_link,
               por_extenso(hoje), por_extenso(v.get("departure_at", ""))))


def main():
    aplica = "--aplica" in sys.argv
    tk = token()
    hoje = date.today().isoformat()
    marcado = re.compile(r"<!-- voo:inicio -->.*?<!-- voo:fim -->", re.S)
    ancora = re.compile(r'<section class="bloco">\s*<div class="reserva">')

    for slug, (iata, nome) in DESTINOS.items():
        caminho = os.path.join(RAIZ, "destinos", slug, "quanto-custa", "index.html")
        if not os.path.exists(caminho):
            print("  %-16s ficha nao existe" % slug); continue

        v, erro = busca(iata, tk)
        if erro:
            print("  %-16s %s" % (slug, erro))
        else:
            print("  %-16s %-10s ida %s / volta %s escala(s)  %-4s  partida %s"
                  % (slug, brl(v["price"]), v.get("transfers"), v.get("return_transfers"),
                     v.get("airline"), (v.get("departure_at") or "")[:10]))

        html = io.open(caminho, encoding="utf-8").read()
        novo_bloco = bloco(nome, v, hoje)

        if marcado.search(html):
            html = marcado.sub(lambda _: novo_bloco, html)
        else:
            m = ancora.search(html)
            if not m:
                print("  %-16s  (nao achei onde inserir)" % ""); continue
            html = html[:m.start()] + novo_bloco + "\n\n" + html[m.start():]

        if aplica:
            io.open(caminho, "w", encoding="utf-8", newline="").write(html)

    print("gravado" if aplica else "(seco - use --aplica)")


if __name__ == "__main__":
    main()
