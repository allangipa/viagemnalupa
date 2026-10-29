# -*- coding: utf-8 -*-
"""Poe na calculadora os destinos que estavam de fora.

O que estava errado
-------------------
O Allan: "Quando clica direto no quanto custa da pagina principal aparece
a calculadora e nao aparece todos os destinos."

Medido: dez destinos no site, seis na calculadora. De fora ficavam
Cancun, Fortaleza, Montevideu e Orlando - e o titulo ainda prometia
"Rio, Lisboa, Nova York e mais tres destinos".

E o mesmo defeito que ja apareceu no schema, no sitemap, nos voos e nos
atalhos: destino novo nao entra sozinho numa estrutura montada antes.

De onde vem o dado
------------------
Dos NUMEROS da ficha de custos do proprio destino - hospedagem,
ingressos, transporte, dias, moeda. Nao reapurei nada: a ficha ja traz
tudo com fonte e data, e derivar de la garante que a calculadora nunca
discorde da pagina que ela resume.

A PROSA (o que nao entra na conta, as fontes, a ressalva de cada cidade)
continua escrita a mao aqui embaixo, porque e texto autoral, nao dado. Mas
com trava: destino com ficha de custos e sem prosa aqui para o script.

Fortaleza fica de fora, e esta escrito por que
----------------------------------------------
A ficha de custos de Fortaleza nao tem NENHUMA faixa de hospedagem - nao
achamos diaria publicada que servisse, e isso ja esta declarado na
pagina. Sem diaria a calculadora nao fecha conta de estadia nenhuma.
Entao ela nao entra, e a pagina diz o motivo em vez de omitir a cidade
caladamente.

Uso
---
    python _build/calculadora/sincroniza.py
    python _build/calculadora/sincroniza.py --aplica
    python _build/calculadora/sincroniza.py --refaz porto [--aplica]

--refaz remonta o bloco e o botao de uma cidade que JA esta na calculadora,
a partir da ficha de custos de hoje. Sem ele, so cidade nova entra: um
bloco montado errado ficava errado para sempre.
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

from montar import bloco, fmt, noites_cobradas                  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


# ---------------------------------------------------------------- a prosa
# Um verbete por destino que ENTRA na calculadora. O resto e derivado.
# O verbete de quem nao tem faixa de hospedagem. Repetido em sete
# destinos, entao mora numa constante: se a redacao mudar, muda nos
# sete de uma vez.
# Texto que vai para a tela: com acento (estava sem ate 26/10/2026).
SEM = ("<b>Esta ficha não tem hospedagem, e isso é deliberado.</b> Não há diária "
       "média publicada por órgão oficial que sirva a este destino, e usar média de "
       "agregador seria furar a regra da casa <b>justamente na linha mais cara da "
       "viagem</b>. O total abaixo é o que dá para somar com fonte, não o que a "
       "viagem custa — por isso o botão desta cidade diz <b>sem hospedagem</b>. ")

PROSA = {
    "montevideu": dict(
        gratis=("Três dos nove pontos não cobram entrada: o Mercado del Puerto, "
                "o Museo Nacional de Artes Visuales e a Feria de Tristán Narvaja."),
        fonte=("Intendencia de Montevideo (tarifa do STM) e as fichas dos 9 pontos, "
               "apuradas em 13 de setembro de 2026. Hospedagem: amostra de mercado — "
               "Montevidéu não publica diária média oficial."),
        nota=("As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
              "quarto; dormitório de hostel é por pessoa. <b>Nenhuma faixa de "
              "hospedagem aqui é estatística oficial</b> — procuramos no Ministerio "
              "de Turismo e no Observatorio Turístico da própria Intendência e não "
              "existe série publicada. São amostras de mercado, rotuladas como tal: "
              "servem para dimensionar, não para reservar."),
    ),
    "orlando": dict(
        gratis=("Nenhum dos pontos apurados é gratuito. Não entram na conta: "
                "aluguel de carro, estacionamento, traslado do aeroporto, "
                "Park Hopper, Express Pass e Lightning Lane."),
        fonte=("I-RIDE Trolley (passe diário) e as fichas dos 6 pontos, apuradas em "
               "13 de setembro de 2026. Hospedagem: Visit Orlando (ADR de 2022) e "
               "amostra de mercado de 2026."),
        nota=("As noites saem das suas datas. <b>Os ingressos de parque são piso, não "
              "preço</b>: são o menor valor publicado para um dia, e a data escolhida "
              "muda muito esse número. <b>Nenhuma das faixas de hospedagem é "
              "estatística oficial atual</b> — o dado da Visit Orlando é de 2022 e o "
              "de 2026 é de aluguel por temporada, outra categoria."),
    ),
    "cancun": dict(
        gratis=("Um dos seis pontos não cobra nada: a Playa Delfines. No México toda "
                "praia é federal e de acesso público."),
        fonte=("INAH (Chichén Itzá, Tulum e Museo Maya), Ultramar (ferry) e as fichas "
               "dos 6 pontos, apuradas em 17 de setembro de 2026. Hospedagem: tarifa "
               "média da cidade divulgada pela Secretaría de Turismo de Quintana Roo."),
        nota=("As noites saem das suas datas. <b>Não há linha de transporte urbano</b>: "
              "não levantamos tarifa de ônibus da Zona Hoteleira nem de táxi, e "
              "preferimos a lacuna à estimativa. <b>O Xcaret também está fora da "
              "conta</b> — apuramos três valores diferentes no mesmo dia e nenhum se "
              "confirmou como o oficial. Os valores em peso não são convertidos: a "
              "conversão automática do site usa a PTAX, que cobre dez moedas, e o peso "
              "mexicano não está entre elas. Para ordem de grandeza, o boletim de "
              "fechamento do Banco Central dava MX$ 100 = R$ 26,99 em 23/out/2026, na "
              "taxa de venda."),
    ),

    # --- os oito que travavam o script desde 17/set/2026 --------------
    #
    # Sete nao tem faixa de hospedagem, pelo mesmo motivo de Fortaleza.
    # A diferenca e que Fortaleza foi para FORA e estes entram: as
    # paginas deles ja exibem total sem hospedagem, o ficha.js ja sabe
    # rotular assim, e a calculadora nao poe cidades lado a lado - so a
    # tira de abas poe, e o botao agora avisa.
    #
    # Sevilha e a unica omissao de verdade: tem hospedagem, tem ADR
    # oficial do INE por ponto turistico, e devia estar aqui desde 25 de
    # setembro.

    "sevilha": dict(
        gratis=("A Plaza de España não cobra entrada — e a cobrança anunciada para ela "
                "em 2024 nunca existiu, não aparece em ordenança fiscal nenhuma."),
        fonte=("Páginas oficiais do Real Alcázar, da Catedral de Sevilha e das Setas de "
               "Sevilla; o transporte, da tabela do Consorcio de Transportes de "
               "Andalucía; a hospedagem, da Encuesta de Ocupación Hotelera do INE "
               "espanhol. Apuradas em 25 de setembro de 2026. "
               "<b>Nenhum valor veio de agregador de viagem.</b>"),
        nota=("As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
              "quarto. <b>Sevilha tem três faixas de hospedagem</b> porque o dado "
              "permite: o INE espanhol publica ADR "
              "por ponto turístico. E a série revela o que importa — <b>agosto a "
              "€ 87,39 contra abril a € 204,57</b>, 2,3 vezes mais, por causa da "
              "Semana Santa e da Feria. <b>A média de 12 meses é cálculo nosso</b> "
              "sobre os doze valores publicados, e está rotulada como tal."),
    ),
    "porto": dict(
        gratis=("Quatro dos dezesseis pontos não cobram entrada: a Ponte Dom Luís I, o "
                "Centro Histórico e a Ribeira, a Estação de São Bento e os Jardins do "
                "Palácio de Cristal."),
        fonte=("Páginas oficiais da Livraria Lello, da Irmandade dos Clérigos, do "
               "Palácio da Bolsa, da Fundação de Serralves, da Casa da Música, do "
               "Teleférico de Gaia, da Direção Regional de Cultura do Norte, do Metro "
               "do Porto e da Câmara Municipal do Porto. Apuradas em 24 e 25 de "
               "setembro de 2026. <b>Nenhum valor veio de agregador de viagem.</b>"),
        nota=(SEM + "No caso do Porto o motivo é específico: <b>o INE português só "
              "publica ADR para Portugal inteiro</b>, e uma média nacional não "
              "descreve a diária do Porto."),
    ),
    "bariloche": dict(
        gratis=("Dois dos nove pontos não cobram entrada: o Circuito Chico com o Punto "
                "Panorámico, e Colonia Suiza."),
        fonte=("Páginas oficiais do Parque Nacional Nahuel Huapi, da Catedral Alta "
               "Patagonia, do Teleférico Cerro Otto e dos operadores da Isla Victoria "
               "e de Puerto Blest. Apuradas em 17 de setembro de 2026. <b>Nenhum valor "
               "veio de agregador de viagem.</b>"),
        nota=(SEM + "No caso de Bariloche, o INDEC coleta a tarifa média na Encuesta "
              "de Ocupación Hotelera mas não a publica, e a série está suspensa desde "
              "novembro de 2025. <b>Os valores estão em peso "
              "argentino e não são convertidos</b>: a conversão automática do site usa "
              "a PTAX, que cobre dez moedas, e o peso argentino não está entre elas. "
              "Para ordem de grandeza, o boletim de fechamento do Banco Central dava "
              "ARS 1.000 = R$ 3,30 em 23/out/2026, na taxa de venda."),
    ),
    "punta-cana": dict(
        gratis=("Duas das sete linhas não cobram entrada: a Playa Bávaro e a Playa "
                "Macao."),
        fonte=("<b>Punta Cana é o destino com menos tarifa oficial do site.</b> Onde só "
               "existe preço de operador, isso está dito, e onde duas fontes divergem, "
               "as duas ficam. Apurado em 17 de setembro de 2026. Nenhum número foi "
               "escolhido por conveniência nem tirado por média."),
        nota=(SEM + "E aqui a lacuna é maior que a hospedagem: <b>três dos sete pontos "
              "também não têm tarifa única publicada</b> e ficam fora da conta. O "
              "Banco Central dominicano e a ASONAHORES publicam a ocupação por zona, "
              "não a diária."),
    ),
    "miami": dict(
        gratis=("Duas das linhas não cobram entrada: Little Havana com a Calle Ocho, e "
                "South Beach com o Art Deco District."),
        fonte=("Páginas oficiais do National Park Service, do Pérez Art Museum Miami, "
               "do Frost Science, do Zoo Miami, do Vizcaya e do Wynwood Walls, mais a "
               "página de impostos turísticos do condado de Miami-Dade. Apuradas em 29 "
               "de setembro de 2026. Hospedagem: Greater Miami Convention and Visitors "
               "Bureau, dados STR de 2025, consultado em 26 de outubro de 2026."),
        nota=("As noites saem das suas datas. <b>A hospedagem é a diária média de 2025 "
              "do órgão de turismo de Miami</b>; troque para Miami Beach ou Downtown no "
              "seletor. <b>Mas a diária não é o que se paga</b>: somam-se "
              "de 13% a 14% de impostos, com composição que muda conforme o bairro, "
              "mais uma <b>resort fee diária de US$ 25 a US$ 60</b> que desde maio de "
              "2025 tem de aparecer no preço total por regra federal. <b>A entrada do "
              "veículo no Everglades também fica fora do total</b>: é por carro, não "
              "por pessoa, e esta calculadora soma por pessoa."),
    ),
    "fortaleza": dict(
        gratis=("Quatro dos sete pontos não cobram entrada: o Centro Dragão do Mar, o "
                "Mercado Central, a Catedral Metropolitana e a Praia do Futuro."),
        fonte=("Site oficial do Beach Park, Instituto Dragão do Mar, Arquidiocese de "
               "Fortaleza e Prefeitura de Jijoca, apurados em 17 de setembro de 2026. "
               "Hospedagem: FOHB e HotelInvest, Panorama da Hotelaria Brasileira, 20ª "
               "edição, consultado em 26 de outubro de 2026."),
        nota=("As noites saem das suas datas. <b>A hospedagem é a média dos hotéis de "
              "Fortaleza em 2025, da FOHB</b>; troque para maio, o mês mais barato, ou "
              "janeiro, o mais caro. <b>O Beach Park entra pelo piso oficial</b>, porque "
              "o preço muda com a data. <b>Não há linha de transporte</b>: não "
              "levantamos tarifa de ônibus, táxi nem dos traslados para o Beach Park e "
              "Jericoacoara."),
    ),
    "salvador": dict(
        gratis=("Cinco das linhas não cobram entrada: o Elevador Lacerda, o Pelourinho "
                "e o Centro Histórico, a Basílica do Senhor do Bonfim, o Mercado "
                "Modelo e a Praia do Porto da Barra."),
        fonte=("Prefeitura de Salvador, portal Pelourinho Dia e Noite, secretaria de "
               "Mobilidade e Museu Náutico da Bahia. Apuradas em 29 de setembro de "
               "2026."),
        nota=("As noites saem das suas datas. <b>A hospedagem é a média dos hotéis de "
              "Salvador em 2025, da FOHB</b>, a mesma fonte do Rio; troque para junho ou "
              "março no seletor. <b>E há um desconto que a calculadora não aplica "
              "sozinha:</b> três dos quatro pontos pagos são equipamentos municipais, e "
              "municipais <b>não cobram nada às quartas-feiras</b>. Desmarque Casa do "
              "Carnaval, Casa do Rio Vermelho e os Espaços do Forte e você vê os "
              "ingressos de uma quarta — sobra só o Farol da Barra, que não é da "
              "prefeitura."),
    ),
    "madri": dict(
        gratis=("Quatro das linhas não cobram entrada: a nave da Catedral de la "
                "Almudena, o Templo de Debod, o Parque del Retiro com o Palacio de "
                "Cristal, e a Plaza Mayor com a Puerta del Sol e o Mercado de San "
                "Miguel."),
        fonte=("Patrimonio Nacional, Museo Reina Sofía, Museo Thyssen-Bornemisza, "
               "Ayuntamiento de Madrid e Real Madrid C.F. Apuradas em 29 de setembro "
               "de 2026. <b>A página do Museo del Prado está atrás de proteção "
               "anti-bot e não abriu</b>: os valores dele vêm da indexação do próprio "
               "domínio somada à ficha do esMadrid, portal oficial de turismo da "
               "cidade, que coincidem. Hospedagem: INE, tabela 46298, lida em 26 de "
              "outubro de 2026."),
        nota=("As noites saem das suas datas. <b>A hospedagem é a média de 12 meses do "
              "INE espanhol</b> (cálculo nosso sobre a série oficial); troque para agosto "
              "ou setembro no seletor. <b>E quatro das seis linhas pagas têm horário em "
              "que não custam nada.</b> Desmarque Prado, Reina Sofía, Thyssen e Palácio "
              "Real e os ingressos caem de € 101 para € 42. <b>€ 18 desse desconto é seu por "
              "nacionalidade</b>: a tarifa gratuita do Palácio Real vale para cidadão "
              "latino-americano com documento, e não só para europeu."),
    ),
    "paris": dict(
        gratis=("Três linhas não cobram entrada: a Catedral de Notre-Dame, o "
                "Sacré-Cœur — aberto todos os dias do ano, das 6h30 às 22h30 — e o "
                "Centre Pompidou, que não cobra porque <b>está fechado até 2030</b>."),
        fonte=("louvre.fr, chateauversailles.fr, toureiffel.paris, "
               "catacombes.paris.fr, sainte-chapelle.fr, paris-arc-de-triomphe.fr, "
               "sacre-coeur-montmartre.com, centrepompidou.fr e culture.gouv.fr. "
               "Apuradas em 30 de setembro de 2026. <b>Três sites oficiais recusaram "
               "leitura</b> — notredamedeparis.fr, toureiffel.paris (que abriu no "
               "navegador) e musee-orsay.fr —, e isso está dito ponto a ponto na ficha "
               "do destino. Hospedagem: painel do setor In Extenso, via imprensa, "
               "consultado em 26 de outubro de 2026."),
        nota=("As noites saem das suas datas. <b>A hospedagem é a média de 2025 de um "
              "painel do setor</b> (In Extenso), noticiada pela imprensa: nenhum órgão "
              "público francês publica a diária de Paris. A taxe de séjour fica fora. "
              "<b>E Paris passou a cobrar por passaporte, com regra diferente em "
              "cada lugar.</b> O Louvre cobra <b>€ 32</b> de quem não é do Espaço "
              "Econômico Europeu e € 22 de quem é, desde 14 de janeiro de 2026; "
              "Versalhes separa por € 3; a Torre Eiffel não separa nada. <b>Um europeu "
              "paga € 146,50 pelos mesmos seis pontos que custam € 159,50 a um "
              "brasileiro.</b> <b>O Musée d’Orsay está fora da conta</b>: a página de "
              "tarifas dele recusa acesso e a bilheteria só mostra preço depois de "
              "escolher data, então quem for ao Orsay vai gastar mais do que esta "
              "calculadora soma. <b>A taxe de séjour também fica fora</b>: é por pessoa "
              "por noite, vai de € 3,25 a € 15,93 conforme a categoria, e a calculadora "
              "não modela isso."),
    ),
    "granada": dict(
        gratis=("Duas linhas não cobram, e uma delas está em lei: o <b>Museo de la "
                "Alhambra</b> e o <b>Corral del Carbón</b> têm entrada livre para todos "
                "pelo artigo 9.1 da ordem de preços da Junta de Andalucía — e o museu "
                "fica <b>dentro do recinto da Alhambra</b>. O Mirador de San Nicolás, a "
                "Silla del Moro e as Torres Bermejas também não cobram."),
        fonte=("A Orden de 17 de julio de 2025 publicada no BOJA e a página de horários "
               "e tarifas do Patronato da Alhambra; os canais oficiais de venda da "
               "Catedral, da Capilla Real e do Museo Cuevas del Sacromonte; o Consorcio "
               "de Transporte Metropolitano e o Ayuntamiento de Granada, para o "
               "transporte; e os Indicadores de Rentabilidad del Sector Hotelero do INE "
               "espanhol, para a hospedagem. Apuradas em 30 de setembro de 2026. "
               "<b>O caixa da Alhambra está atrás de verificação anti-bot e não "
               "abriu</b>, e isso está dito ponto a ponto na ficha do destino."),
        nota=("As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
              "quarto. <b>A Alhambra entra nesta conta por € 22,27, que é um piso e não "
              "um total:</b> a lei fixa € 21, o site do monumento publica € 22,27 e a "
              "mesma página avisa que a comissão ainda se soma. <b>Nenhuma fonte "
              "publica o valor final.</b><br>"
              "<b>E o seletor de hospedagem é o que mais muda a conta aqui:</b> "
              "<b>€ 73,07 em agosto contra € 122,46 em outubro</b>, 68% mais caro pelo "
              "mesmo quarto. <b>Agosto é o mês mais barato do ano em Granada</b> — o "
              "contrário do que se espera na Europa, e é o calor que explica. "
              "<b>A média de 12 meses é cálculo nosso</b> sobre os doze valores do INE, "
              "e está rotulada como tal."),
    ),
    "barcelona": dict(
        gratis=("Nenhuma das doze linhas é gratuita o dia inteiro para todos — mas "
                "<b>três delas não cobram em tardes fixas da semana</b>: o Museu Picasso "
                "na quinta das 16h às 19h (com reserva que abre quatro dias antes), o "
                "MNAC no sábado a partir das 15h e o Castell de Montjuïc no domingo a "
                "partir das 15h. No primeiro domingo do mês os três são gratuitos o dia "
                "inteiro. São € 36 que o calendário tira da conta."),
        fonte=("As páginas de preços dos próprios monumentos e museus — Sagrada "
               "Família, Park Güell, Casa Batlló, La Pedrera, Museu Picasso, MNAC, "
               "Castell de Montjuïc, Sant Pau, Catedral, Palau de la Música e FC "
               "Barcelona; a TMB, para o transporte; a tabela oficial da Agència "
               "Tributària de Catalunya, para a taxa turística; e os Indicadores de "
               "Rentabilidad del Sector Hotelero do INE espanhol, para a hospedagem. "
               "Apuradas em 18 de outubro de 2026. <b>Quatro linhas são piso</b> — "
               "Casa Batlló, La Pedrera, o museu do Barça e a Sagrada Família sem as "
               "torres — e isso está dito ponto a ponto na ficha do destino."),
        nota=("As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
              "quarto. <b>A taxa turística é linha própria e escala pelas noites</b>: "
              "€ 7 por pessoa por noite num hotel de até três estrelas (€ 2 de imposto "
              "catalão mais € 5 de recargo de Barcelona), com teto de 7 noites — e o "
              "recargo sobe para € 6 em abril de 2027. Num quatro estrelas são € 8,40; "
              "num cinco, € 12.<br>"
              "<b>O seletor de hospedagem vai de € 131,41 em dezembro a € 223,37 em "
              "maio</b>, 70% de diferença pelo mesmo quarto, pelo INE. <b>A média de 12 "
              "meses é cálculo nosso</b> sobre os doze valores do INE, e está rotulada "
              "como tal."),
    ),
    "gramado": dict(
        gratis=("Uma linha não cobra: o <b>Lago Negro e a Rua Coberta</b>, da lista oficial "
                "de atrativos gratuitos da Secretaria de Turismo — o pedalinho cobra, e o "
                "valor não está publicado. E <b>cinco atrações do Natal Luz são de "
                "graça</b>, de 22 de outubro a janeiro: Vila de Natal, Show de Acendimento, "
                "Parada de Natal, o palco da Rua Coberta e o Caminho de Luzes."),
        fonte=("As lojas e páginas oficiais de cada parque — Parque do Caracol, Snowland, "
               "Mini Mundo, GramadoZoo, Dreamland, Mundo a Vapor —, o site oficial do Natal "
               "Luz, a Secretaria de Turismo de Gramado, a venda oficial da Citral e a loja "
               "do Bustour. Apuradas em 18 de outubro de 2026. <b>Cinco linhas são "
               "piso</b>, e isso está dito ponto a ponto na ficha do destino."),
        nota=(SEM + "<b>O Parque do Caracol cobra R$ 134,90 de quem é de fora do RS e "
              "R$ 67,00 de gaúcho</b>; a conta usa o primeiro. <b>A taxa de turismo de "
              "Gramado foi revogada pela Câmara em abril de 2026</b>, e a Room Tax que "
              "ficou no lugar é voluntária — por isso nenhuma das duas está no total."),
    ),
    "foz-do-iguacu": dict(
        gratis=("Uma linha não cobra: o <b>Templo Budista Chen Tien</b>, que só aparece em "
                "guias de viagem, sem página oficial — e fecha na segunda."),
        fonte=("As páginas oficiais do Parque Nacional do Iguaçu, do Parque Nacional Iguazú e "
               "da Administración de Parques Nacionales, do Macuco Safari, do Parque das Aves, "
               "do Turismo Itaipu e do Marco das Três Fronteiras, e a Secretaria Municipal de "
               "Turismo. Apuradas em 29 de outubro de 2026. <b>Nenhum valor veio de agregador "
               "de viagem.</b>"),
        nota=(SEM + "<b>O lado argentino das Cataratas está em peso</b>: AR$ 60.000, "
              "convertidos pela taxa de venda do boletim de fechamento do Banco Central de "
              "23/out/2026, R$ 197,94 — <b>sem tarifa Mercosul</b>, o brasileiro paga como "
              "estrangeiro. O ônibus até a Argentina não tem preço publicado e está fora."),
    ),
    "roma": dict(
        gratis=("Três das linhas não cobram entrada: a Basílica de São Pedro, a "
                "Fontana di Trevi com a Piazza Navona, e a Piazza di Spagna — onde, no "
                "entanto, <b>sentar na escadaria custa € 250 de multa</b>."),
        fonte=("Ministero della Cultura, bilheteria oficial da Galleria Borghese e "
               "basilicasanpietro.va, mais a indexação dos domínios oficiais do Parco "
               "archeologico del Colosseo e dos Museus Vaticanos. Apuradas em 29 de "
               "setembro de 2026. <b>Vários sites oficiais italianos recusaram conexão "
               "direta</b>, e isso está dito ponto a ponto na ficha do destino."),
        nota=(SEM + "<b>E Roma tem dois domingos gratuitos por mês, que não são o mesmo "
              "domingo.</b> O primeiro é do Estado italiano e libera Coliseu, Panteão "
              "e Galleria Borghese; o último é do Vaticano, e é o único domingo em que "
              "os Museus Vaticanos abrem. Uma viagem de cinco dias pega no máximo um. "
              "<b>O contributo di soggiorno também fica fora do total</b>: vai de € 3 "
              "a € 10 por pessoa por noite conforme a estrutura, e a calculadora não "
              "modela isso."),
    ),
}

# Destino com ficha de custos que NAO entra, e o motivo, escrito.
# Fortaleza saiu daqui em 26/10/2026: a ficha ganhou a diaria da FOHB.
FORA = {
}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def limpa(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def texto_td(t):
    """Mantem <b> e <a>, tira o resto. A observacao usa negrito."""
    t = re.sub(r"</?(?!/?(b|a|em|i)\b)[a-zA-Z][^>]*>", "", t)
    return re.sub(r"\s+", " ", t).strip()


# ------------------------------------------------- numeros, da ficha de custos
def do_destino(slug):
    p = os.path.join(RAIZ, "destinos", slug, "quanto-custa", "index.html")
    if not os.path.isfile(p):
        return None
    h = le(p)
    m = re.search(r'(?s)class="calc-cfg"[^>]*>(.*?)</script>', h)
    if not m:
        return None
    cfg = json.loads(m.group(1))

    ingressos, transporte, fixos, taxa = [], None, [], None
    for mm in re.finditer(r'(?s)<tr data-tipo="([^"]+)"([^>]*)>(.*?)</tr>', h):
        tipo, attrs, corpo = mm.group(1), mm.group(2), mm.group(3)
        tds = re.findall(r"(?s)<td[^>]*>(.*?)</td>", corpo)
        if len(tds) < 3:
            continue
        nome, obs = limpa(tds[0]), texto_td(tds[2])
        v = re.search(r'data-v="([^"]+)"', attrs)
        if tipo == "ingresso":
            val = float(v.group(1)) if v else 0.0
            # data-v="0" e linha visivel FORA do total: fica de fora aqui
            # tambem, senao a calculadora somaria zero e diria que apurou.
            if val > 0:
                ingressos.append((nome, val, obs))
        elif tipo == "dia" and v:
            rot = re.search(r'data-rot="([^"]*)"', attrs)
            transporte = dict(v=float(v.group(1)),
                              rot=rot.group(1) if rot else "Transporte, {d} dias",
                              obs=obs)
        elif tipo == "fixo" and v:
            fixos.append((nome, float(v.group(1)), obs))
        elif tipo == "taxa":
            noite = re.search(r'data-noite="([^"]+)"', attrs)
            teto = re.search(r'data-teto="([^"]+)"', attrs)
            rot = re.search(r'data-rot="([^"]*)"', attrs)
            # O teto e opcional, como no ficha.js: sem ele, cobra todas as
            # noites. Ate 26/10/2026 exigia os dois, e o Porto (que nao
            # tem teto) entrou na calculadora SEM a taxa: o botao dizia
            # € 113,25 e a ficha, € 125,25.
            if noite:
                taxa = dict(noite=float(noite.group(1)),
                            teto=int(teto.group(1)) if teto else None,
                            rot=rot.group(1) if rot else "Taxa, {n}", obs=obs)

    # quantos pontos a ficha do destino tem
    hg = le(os.path.join(RAIZ, "destinos", slug, "index.html"))
    pontos = len(re.findall(r'<article class="ponto"', hg))
    nome = re.sub(r"<[^>]+>", "", re.search(r"(?s)<h1[^>]*>(.*?)</h1>", hg).group(1))
    nome = re.split(r"\s+em\s+", nome.split(":")[0])[0].strip()

    return dict(
        slug=slug, nome=nome, pontos=pontos,
        moeda=cfg["moeda"], dec=cfg["dec"], dias=cfg["dias"],
        pessoas=cfg.get("pessoas", 1),
        destino="../destinos/%s/" % slug,
        hosp=cfg.get("hosp") or [],
        hospPadrao=cfg.get("hospPadrao"),
        ingressos=ingressos, transporte=transporte, fixos=fixos, taxa=taxa,
        eventos=cfg.get("eventos") or [], janela=cfg.get("janela"),
        **PROSA[slug])


def total_de(c):
    """Mesma conta do montar.py, para o rotulo do botao."""
    noites = c["dias"] - 1
    # Ficha sem hospedagem nao e erro - ver o comentario no montar.py.
    hp = {h["k"]: h for h in c["hosp"]}.get(c["hospPadrao"])
    t = c["transporte"]
    v = sum(x for _, x, _ in c["ingressos"])
    v += (t["v"] * c["dias"] if t else 0)
    v += sum(x for _, x, _ in c["fixos"])
    if c["taxa"]:
        v += c["taxa"]["noite"] * noites_cobradas(noites, c["taxa"])
    return v + (hp["ref"] * noites if hp else 0)


def main(aplica):
    base = os.path.join(RAIZ, "destinos")
    com_ficha = [s for s in sorted(os.listdir(base))
                 if os.path.isfile(os.path.join(base, s, "quanto-custa",
                                                "index.html"))]
    p = os.path.join(RAIZ, "calculadora", "index.html")
    h = le(p)
    ja = set(re.findall(r'data-cidade="([^"]+)"', h))

    # A trava: destino com ficha de custos tem de estar decidido - ja na
    # calculadora, ou com prosa escrita para entrar, ou explicitamente
    # fora com motivo. E o que impede a proxima cidade de sumir daqui em
    # silencio, como Cancun, Fortaleza, Montevideu e Orlando sumiram.
    indecisos = [s for s in com_ficha
                 if s not in ja and s not in PROSA and s not in FORA]
    if indecisos:
        raise SystemExit(
            "Destino com ficha de custos e sem decisao: %s\n"
            "Ou escreva o verbete em PROSA (entra na calculadora), ou\n"
            "declare em FORA com o motivo. Nao deixo passar em silencio."
            % ", ".join(indecisos))
    print("na calculadora hoje: %d  (%s)" % (len(ja), ", ".join(sorted(ja))))
    for s, porque in sorted(FORA.items()):
        print("fora de proposito   : %-14s %s" % (s, porque))
    print()

    novos = [s for s in com_ficha if s in PROSA and s not in ja]
    if not novos:
        print("Nenhum destino novo para acrescentar.")
        return

    blocos, botoes = [], []
    for slug in novos:
        c = do_destino(slug)
        tot = total_de(c)
        print("  %-16s %d dias, %d ingressos, hosp %d, transporte %s -> %s"
              % (slug, c["dias"], len(c["ingressos"]), len(c["hosp"]),
                 "sim" if c["transporte"] else "NAO", fmt(c, tot)))
        blocos.append(bloco(c, False))
        rot = "por pessoa" if c["hosp"] else "<b>sem hospedagem</b>"
        botoes.append('<button type="button" class="cc-big" data-troca="%s">'
                      '<b>%s</b><span>%s %s &middot; %d dias</span>'
                      '</button>' % (slug, c["nome"], fmt(c, tot), rot, c["dias"]))

    # os botoes entram no fim da nav de abas
    m = re.search(r"(?s)(<nav class=\"calc-abas\".*?)(</nav>)", h)
    if not m:
        raise SystemExit("nao achei a nav das abas da calculadora")
    h = h[:m.end(1)] + "".join(botoes) + h[m.end(1):]

    # os blocos entram depois do ultimo .ficha-calc
    fim = h.rfind("</div>", 0, h.find("</main>"))
    ult = h.rfind('<div class="ficha-calc"')
    corte = h.find("\n</div>", ult)
    if ult < 0 or corte < 0:
        raise SystemExit("nao achei onde terminam as fichas da calculadora")
    corte += len("\n</div>")
    h = h[:corte] + "\n" + "\n".join(blocos) + h[corte:]

    print()
    print("%s: %d destino(s) na calculadora." % ("Escrito" if aplica else "Faria",
                                                 len(novos)))
    if aplica:
        escreve(p, h)
    else:
        print("Nada foi alterado. Rode com --aplica para escrever.")


def refaz(slug, aplica):
    """Troca o bloco e o rotulo do botao de `slug` pelos da ficha de hoje."""
    c = do_destino(slug)
    if not c:
        raise SystemExit("%s nao tem ficha de custos com calc-cfg" % slug)
    p = os.path.join(RAIZ, "calculadora", "index.html")
    h = le(p)
    ini = re.search(r'<div class="ficha-calc" data-cidade="%s"( hidden)?>' % re.escape(slug), h)
    if not ini:
        raise SystemExit("%s nao esta na calculadora; rode sem --refaz para acrescentar" % slug)
    fim = h.find("\n</div>\n", ini.start()) + len("\n</div>")
    novo = bloco(c, False)
    if not ini.group(1):
        novo = novo.replace(' hidden>', '>', 1)
    tot = total_de(c)
    rot = "por pessoa" if c["hosp"] else "<b>sem hospedagem</b>"
    h2 = h[:ini.start()] + novo + h[fim:]
    # O botao inteiro, no mesmo formato que main() usa ao acrescentar cidade.
    # A primeira versao trocava so o texto ate a primeira tag: perdia "por
    # pessoa · N dias" e deixava um "sem hospedagem" velho atras do valor.
    botao = ('<button type="button" class="cc-big" data-troca="%s"><b>%s</b><span>%s %s &middot; %d dias'
             '</span></button>' % (slug, c["nome"], fmt(c, tot), rot, c["dias"]))
    h2, n = re.subn(r'<button type="button" class="cc-big" data-troca="%s">.*?</button>' % re.escape(slug),
                    lambda m: botao, h2, count=1, flags=re.S)
    antigo = re.search(r'data-troca="%s"><b>[^<]*</b><span>([^<]*)' % re.escape(slug), h)
    print("   %s: botao %s-> %s %s  (%d linhas no bloco)"
          % (slug, antigo.group(1) if antigo else "?", fmt(c, tot), rot,
             novo.count("<tr data-tipo=")))
    if h2 == h:
        print("   ja igual")
    elif aplica:
        escreve(p, h2)
        print("   escrito")
    else:
        print("   Nada foi alterado. Rode com --aplica.")


if __name__ == "__main__":
    if "--refaz" in sys.argv:
        refaz(sys.argv[sys.argv.index("--refaz") + 1], "--aplica" in sys.argv)
    else:
        main("--aplica" in sys.argv)
