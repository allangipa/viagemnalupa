# -*- coding: utf-8 -*-
"""Dados apurados das duas cidades novas da calculadora.

Nada aqui é estimativa minha. Cada cifra tem fonte e data, registradas na
coluna de observação da tabela e nas apurações do Projeto.
"""

RIO = dict(
 slug="rio-de-janeiro", nome="Rio de Janeiro", moeda="R$", dec=0, dias=6, pessoas=1, pontos=16,
 destino="../destinos/rio-de-janeiro/",
 # FOHB/HotelInvest, Panorama da Hotelaria Brasileira 20a ed., 597 hoteis, ano 2025.
 # A media da cidade traz min e max da propria serie mensal publicada (jun e mar).
 hosp=[
  dict(k="hostel",   rot="Cama em dormitório (amostra)",        ref=106, mn=87,  mx=126, pessoa=True),
  dict(k="economico",rot="Econômico (FOHB)",                    ref=373, mn=373, mx=373),
  dict(k="midscale", rot="Intermediário (FOHB)",                ref=533, mn=533, mx=533),
  dict(k="media",    rot="Média da cidade (ADR)",        ref=610, mn=534, mx=750),
  dict(k="upscale",  rot="Upscale (FOHB)",                      ref=1117,mn=1117,mx=1117),
 ],
 hospPadrao="media",
 ingressos=[
  ("Cristo Redentor",            87,  "Van oficial saindo das Paineiras; R$ 132 de Copacabana"),
  ("Pão de Açúcar",              205, "Inteira; R$ 89 morando no Rio de Janeiro"),
  ("Maracanã",                   115, "Tour; horário muda em dia de jogo"),
  ("Jardim Botânico",            40,  "Residente no Brasil; R$ 80 estrangeiro"),
  ("Museu do Amanhã",            40,  "R$ 10 todo dia 10; grátis em feriado nacional"),
  ("MAR — Museu de Arte do Rio", 20,  "Terça é grátis para todos"),
  ("Theatro Municipal",          20,  "Visita guiada; só na bilheteria, no dia"),
  ("Bonde de Santa Teresa",      20,  "Ida e volta no mesmo dia; passa sobre os Arcos"),
 ],
 transporte=dict(
   v=15.80, rot="Metrô, {d} dias",
   obs="R$ 7,90 a viagem, duas por dia. Não existe passe diário nem turístico no Rio"),
 fixos=[("Cartão Giro do metrô", 4.00, "Depósito do cartão, cobrado uma vez")],
 taxa=None,
 gratis=("Oito dos dezesseis pontos não cobram entrada: Vista Chinesa, Parque Lage, "
         "Copacabana, Ipanema e o Arpoador, Floresta da Tijuca, Real Gabinete Português "
         "de Leitura, Escadaria Selarón e os Arcos da Lapa."),
 fonte="MetrôRio (tarifa) e as fichas dos 16 pontos, apuradas em 13 de setembro de 2026. "
       "Hospedagem: FOHB/HotelInvest, Panorama da Hotelaria Brasileira, 20ª edição, ano de 2025.",
 eventos=[
  ["2026-12-28","2027-01-02","",
   "Sua viagem pega o Réveillon de Copacabana",
   "A ocupação hoteleira da virada foi de <b>90,58%</b> na última medição. "
   "<b>Não existe diária publicada só da noite do Réveillon</b> — a média de dezembro "
   "(R$ 732) dilui a virada em 31 dias e a subestima. A conta abaixo usa a diária normal."],
  ["2027-02-05","2027-02-10","",
   "Sua viagem pega o Carnaval",
   "No Carnaval de 2026 a diária média do mês foi a <b>R$ 1.312</b> e a noite de pico a "
   "<b>R$ 2.657</b>, contra R$ 610 de média anual. <b>A conta abaixo não embute essa alta.</b> "
   "Se a data for flexível, sair desta semana é a maior economia possível na viagem."],
 ],
 janela=None,
 nota=("As noites saem das suas datas. Hospedagem por quarto, duas pessoas por quarto; "
       "dormitório de hostel é por pessoa. O metrô é contado a duas viagens por dia, por pessoa. "
       "A diária vem da média do ano de 2025 — <b>o Carnaval e o Réveillon custam muito mais, "
       "e a conta avisa mas não multiplica</b>, porque ninguém publica o fator."),
)

LISBOA = dict(
 slug="lisboa", nome="Lisboa", moeda="€", dec=2, dias=6, pessoas=1, pontos=16,
 destino="../destinos/lisboa/",
 # INE, serie mensal jan-jul/2026, recorte Grande Lisboa (9 municipios).
 # As demais faixas sao amostra de mercado, rotuladas como tal.
 hosp=[
  dict(k="hostel",     rot="Cama em dormitório (amostra)",            ref=25,    mn=15,    mx=35, pessoa=True),
  dict(k="economico",  rot="Hotel económico (amostra)",               ref=75,    mn=50,    mx=100),
  dict(k="alojamento", rot="Alojamento local (amostra)",ref=118,   mn=118,   mx=118),
  dict(k="media",      rot="Média oficial (ADR)",    ref=144.40,mn=109.60,mx=154.60),
 ],
 hospPadrao="media",
 ingressos=[
  ("Mosteiro dos Jerónimos",      18, "O mais caro da rede de monumentos nacionais"),
  ("Castelo de São Jorge",        17, "Acabou a gratuidade para morador de Lisboa"),
  ("Museu Calouste Gulbenkian",   16, "Reabriu em julho de 2026"),
  ("Torre de Belém",              15, "Teto de 900 visitantes por dia"),
  ("Museu Nacional dos Coches",   15, "Picadeiro Real fechado desde setembro de 2025"),
  ("Oceanário de Lisboa",         25, "A partir de; vai a € 29 conforme a hora"),
  ("Palácio Nacional da Pena",    20, "Hora marcada, sem tolerância de atraso"),
  ("Quinta da Regaleira",         20, "Uma hora de tolerância no bilhete"),
  ("Castelo dos Mouros",          12, "Sem hora marcada — o plano B da Pena"),
  ("Padrão dos Descobrimentos",   10, "Completo; € 5 só a exposição"),
  ("Farol do Cabo da Roca",       5,  "Abriu em julho de 2026; o cabo em si é grátis"),
 ],
 transporte=dict(
   v=3.44, rot="Transporte, {d} dias",
   obs="Zapping a € 1,72 a viagem, duas por dia. <b>O elétrico 28 entra aqui</b> — "
       "pago a bordo custaria € 3,30"),
 fixos=[("Cartão Navegante Ocasional", 0.50, "Suporte físico, válido um ano, pago uma vez")],
 taxa=dict(noite=4.00, teto=7, rot="Taxa municipal turística, {n}",
           obs="€ 4 por pessoa por noite, no máximo 7 noites. "
               "<b>Não vem no preço da reserva</b> — paga-se no alojamento"),
 gratis=("Quatro dos dezesseis pontos não cobram entrada: Praça do Comércio, os miradouros "
         "de Alfama, o Time Out Market e o Cabo da Roca. O Elevador de Santa Justa está "
         "fechado, sem data de reabertura, e por isso ficou fora da conta."),
 fonte="Carris e Metropolitano de Lisboa (tarifário de 1 de janeiro de 2026) e as fichas dos "
       "16 pontos, apuradas em 13 de setembro de 2026. Hospedagem: INE, série mensal de "
       "janeiro a julho de 2026.",
 eventos=[],
 janela=None,
 nota=("As noites saem das suas datas. Hospedagem por quarto, duas pessoas por quarto; "
       "dormitório de hostel é por pessoa. A média oficial é da <b>Grande Lisboa</b>, que "
       "inclui Sintra e Cascais — <b>não existe ADR publicado só do município de Lisboa</b>. "
       "Janeiro custou € 109,60 e julho € 154,60: a época pesa mais que a categoria. "
       "<b>A viagem de comboio até Sintra não está na conta</b>, porque não apuramos a tarifa."),
)
