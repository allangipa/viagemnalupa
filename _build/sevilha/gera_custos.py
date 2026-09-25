# -*- coding: utf-8 -*-
"""Ficha de custos de Sevilha.

Reusa o renderizador de novos/gera_custos.py, como Porto, Cancun,
Fortaleza, Bariloche e Punta Cana.

ESTA FICHA E DA FATIA 1, E A FATIA 2 JA ENTROU NO GUIA
-------------------------------------------------------
Quando ela foi escrita o guia tinha 5 pontos, dos quais quatro eram
visitas - por isso tres dias, e por isso a tabela conta quatro ingressos.

O GUIA TEM 12 PONTOS DESDE 25/set/2026. Entraram Casa de Pilatos,
Palacio de las Duenas, Torre del Oro, Archivo General de Indias, Iglesia
del Salvador, Museo de Bellas Artes e a Plaza de Toros - e quatro deles
cobram: 12,00, 15,00, 1,50 e 12,00 euros.

A tabela abaixo NAO os inclui. Ela continua correta sobre o que declara -
uma viagem de tres dias pelos quatro pontos centrais - mas ja nao esgota
o que o guia oferece. Atualizar a ficha e o roteiro para os 12 pontos e
um trabalho a parte, e esta anotado aqui para nao se perder.

O QUE ESTA FICHA TEM QUE A DO PORTO NAO TEVE: HOSPEDAGEM
---------------------------------------------------------
O Porto saiu sem diaria porque o INE portugues so publica ADR para
Portugal inteiro. O INE espanhol publica por PONTO TURISTICO, e Sevilha
e um deles - tabela 46298, serie "Sevilla. Tarifa media diaria (ADR).
Total categorias".

E a serie revelou o achado desta pagina:

    ago/2026   €  87,39     o mes mais barato
    abr/2026   € 204,57     Semana Santa e Feria de Abril
                            2,3 vezes o de agosto

Nenhuma outra ficha do site tem tres faixas de hospedagem. Esta tem
porque o dado permite, e porque uma media anual aqui esconderia o unico
numero que muda de verdade a conta de quem viaja.

A MEDIA DE 12 MESES E CALCULO NOSSO, E ESTA ROTULADA
-----------------------------------------------------
€ 135,28 e a media aritmetica dos doze meses de set/2025 a ago/2026 da
serie do INE. O INE publica os doze valores; a media e nossa. A regra da
casa manda rotular, e a linha rotula.

O TRANSPORTE ENTROU, MAS POR OUTRA PORTA
-----------------------------------------
A apuracao do guia deixou o transporte em branco: o TUSSAM esta atras da
Cloudflare e o Metro de Sevilha devolve 401. Os dois continuam fechados.

Mas quem FIXA a tarifa nao e a operadora: e o Consorcio de Transportes de
Andalucia, orgao da Junta, e ele publica a tabela em pagina aberta -
"Tarifas urbanas: Sevilla (TUSSAM), billete sencillo 1,40 €".

O que NAO conseguimos foi a tarjeta turistica de 1 e 3 dias, que e
produto do TUSSAM e so existe no site bloqueado. Fica escrito.

NAO HA TAXA TURISTICA NA ANDALUZIA
-----------------------------------
E a segunda cobranca anunciada e inexistente desta cidade, depois da
entrada da Plaza de Espana. Sevilha e Malaga pedem a taxa desde 2024; a
Junta nao aprovou, e sem a Junta o municipio nao pode criar. A linha
entra na tabela com valor nenhum, porque a ausencia tambem e resposta -
e porque o leitor que viu a noticia vai procurar por ela.

Uso
---
    python _build/sevilha/gera_custos.py
    python _build/sevilha/gera_custos.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402

# Carrega a ficha do Porto so pelo efeito colateral: e ela que acrescenta
# o Porto a barra "Calcular para", e ela por sua vez carrega o novos2,
# que acrescenta Bariloche e Punta Cana. Sem esta linha, publicar Sevilha
# sozinha sairia com uma barra de dez cidades em vez de catorze.
_s = importlib.util.spec_from_file_location(
    "vnl_custos_porto", os.path.join(RAIZ, "_build", "porto", "gera_custos.py"))
_m = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_m)

APURADO = "25 de setembro de 2026"

# Serie do INE, tabela 46298, "Sevilla. Tarifa media diaria (ADR)".
# Guardada aqui inteira para a media ser conferivel sem sair do arquivo.
ADR = {
    "set/2025": 141.60, "out/2025": 161.00, "nov/2025": 125.88,
    "dez/2025": 117.05, "jan/2026": 103.91, "fev/2026": 119.31,
    "mar/2026": 143.70, "abr/2026": 204.57, "mai/2026": 177.19,
    "jun/2026": 140.05, "jul/2026": 101.71, "ago/2026": 87.39,
}
MEDIA = round(sum(ADR.values()) / len(ADR), 2)      # 135.28
assert len(ADR) == 12, "a media diz 12 meses; confira a serie"

FICHAS = {
    "sevilha": {
        "nome": "Sevilha", "dias": 3, "moeda": "€", "dec": 2,
        "titulo": "Quanto custa 3 dias em Sevilha em 2026",
        "descricao": ("O custo de 3 dias em Sevilha, por pessoa, com a diária oficial "
                      "que varia 2,3 vezes ao longo do ano, o ingresso do Alcázar que "
                      "quase ninguém soma e a taxa turística que não existe."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas conferidas "
                     "em fonte oficial em 25 de setembro de 2026. <b>Com hospedagem</b> "
                     "— e com a diária aberta em três épocas, porque em Sevilha isso "
                     "muda tudo."),
        "hosp": [
            {"k": "media", "rot": "Média dos 12 meses (cálculo nosso, INE)",
             "ref": MEDIA, "mn": MEDIA, "mx": MEDIA},
            {"k": "baixa", "rot": "Agosto — o mês mais barato do ano (INE)",
             "ref": ADR["ago/2026"], "mn": ADR["ago/2026"], "mx": ADR["ago/2026"]},
            {"k": "alta", "rot": "Abril — Semana Santa e Feria (INE)",
             "ref": ADR["abr/2026"], "mn": ADR["abr/2026"], "mx": ADR["abr/2026"]},
        ],
        "hospPadrao": "media",
        "intro": ("A tabela abaixo é a nossa apuração: 3 dias, 1 pessoa, valores em "
                  "euro. Mude as datas e o número de pessoas, troque a época da "
                  "hospedagem, desmarque o que você não vai fazer, e a conta se refaz "
                  "na hora."),
        "nota_calc": (
            "As noites saem das suas datas. Hospedagem por quarto, duas pessoas por "
            "quarto. <b style=\"color:var(--gelo)\">A diária vem do INE espanhol, aberta "
            "por ponto turístico</b> — Sevilha é um deles — e por isso esta ficha tem "
            "hospedagem, ao contrário da do Porto, onde só existe média de país "
            "inteiro.<br>"
            "<b>O seletor de hospedagem tem três épocas e não é enfeite:</b> a diária "
            "oficial de abril é <b>2,3 vezes</b> a de agosto. Nenhuma média anual "
            "sobrevive a essa diferença, e é por isso que ela está aberta em vez de "
            "escondida num número só. "
            "Linhas marcadas como não apuradas continuam fora do total."),
        "linhas": [
            # ---------------------------------------------------- ingressos
            ("ingresso", 15.50, "Real Alcázar, entrada geral", "€ 15,50",
             "Fonte: página <i>Prepara la visita</i> do site oficial do Real Alcázar "
             "(alcazarsevilla.org), consultada em 25/set/2026.<br>"
             "<b>Entrada geral: € 15,50.</b> A reduzida sai por <b>€ 8,00</b> para "
             "maiores de 65 anos, estudantes de 14 a 30 anos e portadores do Carné "
             "Jovem Europeu.<br>"
             "<b>A bilheteira física aceita apenas cartão</b> — não há pagamento em "
             "dinheiro. Quem chega com espécie compra online ou não entra."),
            ("ingresso", 5.50, "Cuarto Real Alto, cobrado à parte", "€ 5,50",
             "Mesma fonte, mesma data. <b>É a linha que quase nenhum roteiro soma.</b><br>"
             "O Cuarto Real Alto <b>não está incluído na entrada geral</b>: são € 5,50 "
             "adicionais. É o andar onde a família real se hospeda quando está em "
             "Sevilha.<br>"
             "<b>Quem quiser ver tudo gasta € 21,00, e não € 15,50</b> — uma diferença "
             "de 35% sobre o número que circula por aí."),
            ("ingresso", 13.00, "Catedral de Sevilha e Giralda", "€ 13,00",
             "Fonte: página de <i>Horarios y tarifas</i> do site oficial da Catedral de "
             "Sevilla (catedraldesevilla.es), consultada em 25/set/2026.<br>"
             "<b>Entrada geral: € 13,00</b>, com a subida à Giralda incluída. A "
             "audioguia custa <b>€ 5,00</b> à parte, ou <b>€ 4,00</b> pelo aplicativo.<br>"
             "<b>Há entrada gratuita aos domingos</b> — e "
             "<span class=\"flag\">duas páginas oficiais discordam sobre o horário "
             "dela</span> a de horários e tarifas diz 16h30 às 18h; a de alta "
             "temporada diz 14h30 às 18h. Não escolhemos uma: as duas estão no guia."),
            ("ingresso", 16.00, "Setas de Sevilla, mirador", "€ 16,00",
             "Fonte: site oficial das Setas de Sevilla (setasdesevilla.com), consultado "
             "em 25/set/2026.<br>"
             "<b>€ 16,00</b> pelo acesso ao mirador.<br>"
             "<b>Tem o horário mais longo da cidade:</b> todos os dias das 9h30 à 1h da "
             "manhã, com última entrada às 0h15. É o único ponto desta ficha que se "
             "visita depois do jantar — e isso é o que o roteiro usa para não empilhar "
             "tudo de manhã."),
            ("ingresso", 0.00, "Plaza de España", "grátis",
             "<b>A entrada paga na Plaza de España nunca existiu.</b><br>"
             "Em fevereiro e em setembro de 2024 o prefeito de Sevilha anunciou que "
             "passaria a cobrar três euros de turista. Procuramos nas ordenanças "
             "fiscais do município, <b>inclusive nas de 2026</b>: não há taxa aprovada. "
             "A praça segue de acesso livre.<br>"
             "A linha fica na tabela valendo zero de propósito — <b>muito texto de "
             "viagem já fala da cobrança como se ela valesse</b>, e quem leu isso vai "
             "procurar o valor aqui."),
            # ---------------------------------------------------- transporte
            ("fixo", 8.40, "Ônibus urbano, 6 viagens", "€ 8,40",
             "Fonte: tabela de tarifas do <b>Consorcio de Transportes de Andalucía</b> "
             "(siu.ctas.ctan.es), órgão da Junta de Andalucía, consultada em "
             "25/set/2026: <b>Tarifas urbanas — Sevilla (TUSSAM), billete sencillo "
             "€ 1,40</b>.<br>"
             "<b>Seis viagens é a suposição desta ficha, não um dado.</b> O centro "
             "histórico se faz inteiro a pé — Alcázar e Catedral são vizinhos, as Setas "
             "ficam a quinze minutos e a Plaza de España a vinte. Esta linha cobre "
             "chegada, saída e algum deslocamento solto. <b>Quem andar só a pé "
             "desmarca.</b><br>"
             "<span class=\"flag\">Não conseguimos a tarjeta turística de 1 e 3 dias</span> "
             "ela é produto do TUSSAM, e o site do TUSSAM está atrás de verificação "
             "anti-bot da Cloudflare. O Metro de Sevilha devolve 401. A tarifa acima "
             "veio do órgão que a fixa, não da operadora."),
            # ---------------------------------------------------- a taxa que nao ha
            ("taxa", None, "Taxa turística municipal", "não existe",
             "<b>Não há taxa turística na Andaluzia em 2026.</b><br>"
             "É a segunda cobrança anunciada e inexistente desta cidade, depois da "
             "entrada da Plaza de España. As prefeituras de Sevilha e de Málaga pedem a "
             "taxa desde 2024, mas <b>a criação depende da Junta de Andalucía</b>, que "
             "não aprovou — e sem a Junta o município não pode instituí-la.<br>"
             "Se você reservou um hotel em Sevilha e viu nota sobre taxa turística, "
             "<b>ela não é municipal</b>. Confira o que está sendo cobrado. "
             "<b>Fora do total, porque não há valor.</b>"),
            # ---------------------------------------------------- hospedagem
            ("hosp", None, "Hospedagem, 2 noites", "€ 270,56",
             "Fonte: <b>INE</b> (Instituto Nacional de Estadística de Espanha), "
             "<i>Encuesta de Ocupación Hotelera</i>, tabela 46298 — tarifa média diária "
             "(ADR) por <b>ponto turístico</b>, série <i>Sevilla, total de categorias</i>, "
             "consultada em 25/set/2026.<br>"
             "<b>O valor mostrado usa a média dos 12 meses de set/2025 a ago/2026: "
             "€ 135,28 por quarto por noite.</b> Os doze valores são do INE; "
             "<b>a média é cálculo nosso</b>, e está rotulada como tal no seletor.<br>"
             "<b>A variação ao longo do ano é o achado desta página:</b> € 87,39 em "
             "agosto contra <b>€ 204,57 em abril</b>, que é quando caem a Semana Santa "
             "e a Feria de Abril. <b>Duas vírgula três vezes mais caro</b> pelo mesmo "
             "quarto. Troque a época no seletor acima e veja a conta mudar.<br>"
             "ADR é por <b>quarto ocupado</b>, não por pessoa. A conta divide por duas "
             "pessoas por quarto, como nas outras fichas."),
        ],
        "rodape_tabela": (
            "Valores em euro, por pessoa, apurados em fonte oficial em 25 de setembro "
            "de 2026. <b>Uma linha está fora do total</b> — a taxa turística, porque "
            "ela não existe — e está marcada na tabela.<br>"
            "<b>A armadilha desta cidade não é o ingresso, é o calendário.</b> "
            "Os quatro ingressos somam <b>€ 50,00</b> e não mudam no ano. A hospedagem "
            "de duas noites vai de <b>€ 174,78</b> em agosto a <b>€ 409,14</b> em "
            "abril, pelo mesmo quarto. <b>Escolher a semana pesa mais que cortar "
            "qualquer visita.</b>"),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. As tarifas vêm das "
            "páginas oficiais do Real Alcázar, da Catedral de Sevilha e das Setas de "
            "Sevilla; o transporte, da tabela do Consorcio de Transportes de Andalucía; "
            "a hospedagem, da Encuesta de Ocupación Hotelera do INE espanhol. "
            "<b>Nenhum valor veio de agregador de viagem.</b> "
            "<b>E dois deles desmentem cobranças que circulam como certas:</b> a "
            "entrada de € 3 na Plaza de España, anunciada em 2024 e nunca aprovada, e "
            "a taxa turística municipal, que a Andaluzia não tem."),
    },
}

# A barra "Calcular para" lista todas as fichas do site. Sevilha entra no
# fim, na ordem em que foi publicada. O dedupe protege contra o caso de a
# cadeia de imports ja ter passado por aqui neste mesmo processo.
base.CIDADES = base.CIDADES + [("sevilha", "Sevilha")]
_vistos, _limpo = set(), []
for _slug, _nome in base.CIDADES:
    if _slug not in _vistos:
        _vistos.add(_slug)
        _limpo.append((_slug, _nome))
base.CIDADES = _limpo

base.FICHAS = FICHAS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
