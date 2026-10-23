# -*- coding: utf-8 -*-
"""Do aeroporto ao hotel no Rio: apuracao de 23/out/2026.

TAXI: nao ha numero digitado aqui. As tabelas oficiais de cobranca
antecipada (SMTR, Resolucoes 3898 e 3899 de 07/01/2026, em vigor desde
11/01/2026) estao em _build/rio/fontes/smtr-taxi-2026.txt, e a pagina le
os valores de la, bairro por bairro. O taximetro (Resolucao SMTR 3893, de
29/12/2025) tambem esta no mesmo arquivo.

TRANSPORTE PUBLICO: cada opcao traz o texto da pagina e o TRECHO da fonte.
Todo numero do texto precisa aparecer no trecho - o gerador confere.
Trecho e citacao curta da fonte, consultada na data indicada.

O que ficou de fora de proposito:
- Aplicativo (Uber, 99): preco dinamico, sem tabela publica.
- As linhas do BRT Transcarioca que saem do Galeao: nenhuma fonte oficial
  de 2026 confirmou numero e itinerario (as wikis divergem). Entra so a
  tarifa, que e do decreto, com a lacuna escrita.
- A tarifa de 2026 da linha executiva LECD71 (Leblon x Aeroporto): a ultima
  publicacao oficial e de 30/11/2023. Entra como nao confirmada.
"""

TAXI_FONTE = ("Secretaria Municipal de Transportes do Rio (SMTR), tabelas de cobrança antecipada das Resoluções "
              "nº 3.898 e nº 3.899, de 7/jan/2026, em vigor desde 11/jan/2026, consultadas em 23/out/2026")
TAXIMETRO_FONTE = "Resolução SMTR nº 3.893, de 29/dez/2025, consultada em 23/out/2026"

# Os bairros da pagina, na ordem da tabela, com o nome EXATO que a SMTR usa.
BAIRROS = [
    ("Centro (até a Av. Rio Branco)", "CENTRO (até Rio Branco)"),
    ("Lapa", "LAPA"),
    ("Santa Teresa", "SANTA TERESA"),
    ("Flamengo", "FLAMENGO"),
    ("Botafogo", "BOTAFOGO"),
    ("Urca", "URCA"),
    ("Leme", "LEME"),
    ("Copacabana, até a Rua República do Peru", "COPACABANA ( até a Rua Rep. do Peru)"),
    ("Copacabana, depois da Rua República do Peru", "COPACABANA ( Após a Rua Rep. do Peru)"),
    ("Ipanema", "IPANEMA"),
    ("Leblon", "LEBLON"),
    ("Barra da Tijuca, até a Av. Ayrton Senna", "BARRA DA TIJUCA ( até A . Sena)"),
    ("Rodoviária Novo Rio", "RODOVIÁRIA"),
]

TRANSPORTE = {
 "galeao": [
  dict(nome="Ônibus Expresso Galeão–Gentileza",
       texto="Ônibus executivo sem paradas entre o aeroporto e o Terminal Intermodal Gentileza, no Centro. "
             "Tarifa de R$ 15, paga com o cartão Jaé. Funciona das 6h à meia-noite, com saídas a cada 20 "
             "minutos, e a viagem leva cerca de 25 minutos.",
       trecho="“O preço da tarifa é de R$15.” “opera das 6h à meia-noite, com intervalos previstos de 20 "
              "minutos.” “O tempo de deslocamento da linha é de cerca de 25 minutos.” — e, em 2026: “a tarifa "
              "é de R$ 15,00”, paga com o cartão Jaé",
       fonte="Prefeitura do Rio (prefeitura.rio), 24/fev/2025; tarifa reconfirmada por Ônibus & Transporte, "
             "8/fev/2026; consultadas em 23/out/2026"),
  dict(nome="Do Terminal Gentileza à Zona Sul",
       texto="No Gentileza passa a Linha 1 do VLT, que vai ao Centro e termina no Santos Dumont. A tarifa do VLT "
             "é R$ 5,00. Para seguir à Zona Sul, troque para o metrô na Cinelândia ou na Carioca: R$ 7,90.",
       trecho="Decreto Rio nº 57.473, de 29/dez/2025: tarifa de R$ 5,00 para ônibus municipais, BRT e VLT. "
              "Governo do RJ mantém o metrô em R$ 7,90 até dezembro de 2026. O terminal se conecta à Linha 1 do "
              "VLT, que vem do Aeroporto Santos Dumont; Cinelândia e Carioca (metrô) são pontos de integração "
              "da Linha 1",
       fonte="Prefeitura do Rio, 24/fev/2025 (conexões do Gentileza); Decreto Rio nº 57.473 via Ônibus & "
             "Transporte, 31/dez/2025; Diário do Transporte, 26/fev/2026 (metrô); ANPTrilhos (paradas do "
             "VLT); consultados em 23/out/2026"),
  dict(nome="BRT Transcarioca",
       texto="O BRT também serve o Galeão. A tarifa é R$ 5,00, a mesma do ônibus municipal.",
       trecho="Decreto Rio nº 57.473, de 29/dez/2025: tarifa de R$ 5,00 para ônibus municipais, BRT e VLT",
       fonte="Decreto Rio nº 57.473 via Ônibus & Transporte, 31/dez/2025 (tarifa); Wikipédia, lista de "
             "estações do BRT (estação Galeão–Tom Jobim); consultados em 23/out/2026",
       lacuna="Não confirmamos em fonte oficial de 2026 quais linhas do BRT saem do Galeão nem o itinerário de "
              "cada uma: as listas públicas divergem. Confira no aplicativo da Mobi-Rio antes de sair."),
  dict(nome="Ônibus executivo Leblon x Aeroporto (LECD71)",
       texto="Linha executiva pela orla: Leblon, Ipanema, Copacabana, Botafogo, Flamengo e Centro.",
       trecho="Leblon, Ipanema, Copacabana, Botafogo, Flamengo, Centro e Avenida Brasil",
       fonte="Prefeitura do Rio (prefeitura.rio), 30/nov/2023, consultada em 23/out/2026",
       lacuna="A última tarifa publicada pela Prefeitura é de novembro de 2023. Não encontramos confirmação "
              "oficial do preço nem dos horários de 2026."),
 ],
 "santos-dumont": [
  dict(nome="VLT e metrô",
       texto="O VLT sai da porta do aeroporto. A Linha 1 passa pela Cinelândia, onde se troca para o metrô "
             "rumo à Zona Sul. VLT R$ 5,00 e metrô R$ 7,90, pagos separadamente.",
       trecho="Decreto Rio nº 57.473, de 29/dez/2025: tarifa de R$ 5,00 para ônibus municipais, BRT e VLT. "
              "Governo do RJ mantém o metrô em R$ 7,90 até dezembro de 2026. Na Linha 1 do VLT, Cinelândia e "
              "Carioca são as paradas de integração com o metrô; a Cinelândia é a segunda a partir do aeroporto",
       fonte="Decreto Rio nº 57.473 via Ônibus & Transporte, 31/dez/2025; Diário do Transporte, 26/fev/2026; "
             "ANPTrilhos e Viaje na Viagem (paradas do VLT); consultados em 23/out/2026"),
 ],
}

TAXI_REGRAS = dict(
    texto="A tabela é paga antes, no balcão de táxi do aeroporto, que emite um voucher com o valor do bairro. "
          "É opcional: o passageiro pode preferir o taxímetro.",
    trecho="Art. 1º autoriza o serviço “mediante cobrança antecipada de tarifas, através de tabela pré-fixada”. "
           "Art. 3º: “A utilização da tabela pré-fixada somente será permitida mediante a prévia emissão de "
           "‘voucher’ no balcão.” Art. 4º: a escolha do taxímetro “cabe ao usuário do serviço”",
    fonte="Resolução SMTR nº 3.898, de 7/jan/2026 (DOM de 8/jan/2026), via LegisWeb, consultada em 23/out/2026",
)

LACUNAS = [
    "Aplicativo (Uber, 99 e outros): o preço muda com a hora e a demanda, e não há tabela pública. Não "
    "publicamos número.",
    "Tarifa 1 e Tarifa 2 da tabela de táxi: a resolução traz as duas colunas, mas não diz quando vale cada "
    "uma. Pergunte no balcão antes de pagar.",
    "Integração com desconto entre o ônibus, o VLT e o metrô: não apuramos. As somas desta página são de "
    "tarifas cheias.",
]
