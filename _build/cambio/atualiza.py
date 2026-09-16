# -*- coding: utf-8 -*-
"""Atualiza as conversões euro→real da página de Lisboa pela PTAX do Banco Central.

Fonte: API pública Olinda/PTAX do BCB. Não exige chave, não exige conta e é
fonte oficial — o que respeita a regra da casa: preço não vem de parceiro
interessado, e todo número tem fonte e data.

O que ele toca, e só isso:
  <span class="brl" data-eur="18">R$ 107</span>   ← recalcula o conteúdo
  <span class="fx" data-fx="eur-brl">5,9430</span>
  <span class="fx" data-fx="eur-usd">1,1542</span>
  <span class="fx" data-fx="data">15 de setembro de 2026</span>

Só grava se algum número mudou. Sem dependência externa: roda com a stdlib.

ATENÇÃO: os geradores em _build/lisboa/ têm caminhos /home/claude cravados e
não rodam nesta máquina. Por isso este script edita o HTML publicado direto —
não existe rebuild capaz de reverter. Se um dia os geradores forem consertados,
a marcação precisa ser espelhada neles antes do primeiro rebuild.
"""
import json, re, io, os, sys, urllib.request
from datetime import date, timedelta

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "destinos", "lisboa", "index.html")
API = ("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
       "CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,"
       "dataFinalCotacao=@dataFinalCotacao)?@moeda='{m}'&@dataInicial='{a}'"
       "&@dataFinalCotacao='{b}'&$format=json")
MESES = ("janeiro fevereiro março abril maio junho julho agosto setembro "
         "outubro novembro dezembro").split()


def ptax(simbolo):
    """Última cotação de venda com boletim de Fechamento nos últimos 12 dias.

    A janela é larga de propósito: feriado prolongado pode deixar vários dias
    sem boletim, e é melhor repetir a cotação de anteontem do que falhar.
    """
    hoje = date.today()
    ini = hoje - timedelta(days=12)
    url = API.format(m=simbolo, a=ini.strftime("%m-%d-%Y"), b=hoje.strftime("%m-%d-%Y"))
    with urllib.request.urlopen(url, timeout=45) as r:
        dados = json.load(r)["value"]
    fech = [d for d in dados if d.get("tipoBoletim") == "Fechamento"]
    if not fech:
        raise SystemExit("PTAX sem boletim de fechamento para %s em 12 dias" % simbolo)
    ult = fech[-1]
    return float(ult["cotacaoVenda"]), ult["dataHoraCotacao"][:10]


def br(valor, casas):
    return ("%.*f" % (casas, valor)).replace(".", ",")


def main():
    eur, dia = ptax("EUR")
    usd, _ = ptax("USD")
    ano, mes, d = (int(x) for x in dia.split("-"))
    extenso = "%d de %s de %d" % (d, MESES[mes - 1], ano)

    html = io.open(PAGINA, encoding="utf-8").read()
    antes = html

    # as conversões espalhadas pelo texto, arredondadas ao real inteiro
    def conv(m):
        inteiro = "{:,}".format(int(round(float(m.group(2)) * eur))).replace(",", ".")
        return "%sR$ %s%s" % (m.group(1), inteiro, m.group(3))

    html = re.sub(r'(<span class="brl" data-eur="([\d.]+)">)R\$\s*[\d.,]+(</span>)',
                  conv, html)

    trocas = {"eur-brl": br(eur, 4), "eur-usd": br(eur / usd, 4), "data": extenso}
    for chave, valor in trocas.items():
        html = re.sub(r'(<span class="fx" data-fx="%s">)[^<]*(</span>)' % chave,
                      lambda m, v=valor: m.group(1) + v + m.group(2), html)

    n = len(re.findall(r'class="brl"', html))
    print("PTAX %s — EUR %s / USD %s / EUR-USD %s — %d conversões"
          % (extenso, br(eur, 4), br(usd, 4), br(eur / usd, 4), n))

    if html == antes:
        print("nada mudou")
        return 0
    io.open(PAGINA, "w", encoding="utf-8", newline="").write(html)
    print("página atualizada")
    return 0


if __name__ == "__main__":
    sys.exit(main())
