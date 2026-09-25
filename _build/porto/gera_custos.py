# -*- coding: utf-8 -*-
"""Ficha de custos do Porto.

Reusa o renderizador de novos/gera_custos.py, o mesmo que fez Cancun,
Fortaleza, Bariloche e Punta Cana. So os dados sao daqui.

O QUE ESTA FICHA TEM DE DIFERENTE DAS QUATRO ANTERIORES
-------------------------------------------------------
E a primeira com TRANSPORTE apurado e com TAXA MUNICIPAL. Bariloche e
Punta Cana sairam sem os dois, e a lacuna estava escrita nas duas. Aqui
o Metro do Porto publica tarifario e a Camara Municipal publica a taxa,
entao os dois entram no total.

Isso obrigou a mexer no renderizador: o linha() so emitia data-tipo e
data-v, que e o que "ingresso" precisa. Os tipos "taxa" e "metro" do
ficha.js precisam de data-noite, data-teto e data-rot. O sexto elemento
da tupla, opcional, carrega esses atributos.

E TAMBEM NAO TEM HOSPEDAGEM, pelo mesmo motivo das outras duas
-------------------------------------------------------------
O INE publica ADR - proveito medio por quarto ocupado - mas so para
Portugal inteiro: 130,90 EUR em maio de 2026. Nao achamos a serie aberta
por municipio, e os destaques mensais do INE dao o Porto em dormidas,
nao em ADR. Media de pais numa pagina de cidade seria justamente o tipo
de numero que este site recusa nas outras fichas.

O valor nacional fica escrito na nota, como ordem de grandeza, e FORA
do total.

O TETO DE NOITES DA TAXA NAO FOI APURADO
----------------------------------------
Lisboa cobra no maximo 7 noites, e o ficha.js ja sabe lidar com teto. A
pagina municipal do Porto nao informa limite, e o Regulamento e o
folheto sao PDF sem texto extraivel. Sem data-teto o calculador cobra
todas as noites, que e o comportamento conservador - erra para mais,
nunca para menos, e a nota diz isso.

Para a viagem padrao desta ficha, 4 noites, um eventual teto de 7 nao
mudaria nada.

Uso
---
    python _build/porto/gera_custos.py
    python _build/porto/gera_custos.py --aplica
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_custos as base      # noqa: E402
import importlib.util           # noqa: E402

# Carrega o novos2 so pelo efeito colateral: e ele que acrescenta
# Bariloche e Punta Cana a barra "Calcular para". Sem isto, rodar esta
# ficha sozinha publicaria uma barra com dez cidades em vez de treze.
_s = importlib.util.spec_from_file_location(
    "vnl_custos_novos2", os.path.join(RAIZ, "_build", "novos2", "gera_custos.py"))
_m = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_m)

APURADO = "24 e 25 de setembro de 2026"

FICHAS = {
    "porto": {
        "nome": "Porto", "dias": 5, "moeda": "€", "dec": 2,
        "titulo": "Quanto custa 5 dias no Porto em 2026",
        "descricao": ("O custo de 5 dias no Porto, por pessoa, com a taxa municipal "
                      "turística que não vem no preço da reserva e o transporte "
                      "apurado — e sem a hospedagem, porque não há diária publicada "
                      "para a cidade."),
        "abertura": ("A conta do que foi apurado, por pessoa, com as tarifas "
                     "conferidas em fonte oficial em 24 e 25 de setembro de 2026. "
                     "<b>Sem a hospedagem</b> — e a página explica por quê."),
        "hosp": [],
        "hospPadrao": None,
        "intro": ("A tabela abaixo é a nossa apuração: 5 dias, 1 pessoa, valores em "
                  "euro. Mude as datas e o número de pessoas, desmarque o que você "
                  "não vai fazer, e a conta se refaz na hora."),
        "nota_calc": (
            "<b style=\"color:var(--gelo)\">Esta ficha não tem hospedagem, e isso é "
            "deliberado.</b> O INE publica o proveito médio por quarto ocupado, mas "
            "<b>só para Portugal inteiro</b> — 130,90 € em maio de 2026 — e não "
            "encontramos a série aberta por município. Média de país numa página de "
            "cidade é o tipo de número que recusamos nas outras fichas, e não vamos "
            "abrir exceção aqui. O valor nacional fica como ordem de grandeza, fora "
            "do total. "
            "<b>O transporte e a taxa municipal, ao contrário, estão dentro</b>: o "
            "Metro do Porto publica tarifário e a Câmara Municipal publica a taxa. "
            "Linhas marcadas como não apuradas continuam fora do total."),
        "linhas": [
            # ---------------------------------------------------- transporte
            ("fixo", 16.55, "Andante Tour 3, 72 horas na rede toda", "€ 16,55",
             "Fonte: página de preços do Metro do Porto (metrodoporto.pt), consultada "
             "em 24–25/set/2026, com <b>tarifário em vigor desde 1º de janeiro de "
             "2026</b> e IVA incluído.<br>"
             "<b>Circula sem limite por toda a rede Andante</b> — metrô, ônibus e trem "
             "urbano — durante 72 horas consecutivas após a primeira validação, "
             "<b>aeroporto incluído</b>. Cartão de papel, não recarregável.<br>"
             "<b>Escolhemos o Tour porque ele não usa zonas.</b> A alternativa por "
             "viagem sairia mais barata para quem anda a pé no centro, mas "
             "<span class=\"flag\">não conseguimos apurar a zona do aeroporto</span> "
             "o próprio Metro publica um link para calcular zonas que <b>devolve erro "
             "404 no site deles</b>, e o mapa de zonamento é PDF sem texto."),
            ("fixo", 7.75, "Andante Tour 1, para o quinto dia", "€ 7,75",
             "Mesma fonte, mesma data. O Tour 3 cobre 72 horas; uma viagem de 5 dias "
             "passa disso. <b>O Tour 1 vale 24 horas consecutivas</b>, também pela rede "
             "toda.<br>"
             "<b>Some os dois e dá € 24,30 pelos cinco dias.</b> Quem ficar só três "
             "dias desmarca esta linha."),
            # ---------------------------------------------------- taxa
            ("taxa", 12.00, "Taxa municipal turística, 4 noites", "€ 12,00",
             "Fonte: página oficial da Taxa Municipal Turística do Porto, no portal de "
             "Atividades Económicas da Câmara Municipal (cm-porto.pt), consultada em "
             "24–25/set/2026.<br>"
             "<b>€ 3 por pessoa por noite</b>, cobrados pelo alojamento. O valor "
             "<b>passou a ser por dormida em 1º de dezembro de 2024</b>, quando entrou "
             "em vigor o novo regulamento — antes era por reserva.<br>"
             "<b>Não vem no preço da reserva</b>, e é a surpresa mais comum de quem "
             "chega ao Porto com a estadia já paga.<br>"
             "<b>Não pagam:</b> crianças e jovens até 12 anos, estadia por ato médico "
             "e acompanhantes, pessoa com incapacidade igual ou superior a 60% e "
             "acompanhantes, peregrinos em albergue na primeira noite, e pessoas em "
             "situação de deslocação forçada.<br>"
             "<span class=\"flag\">Não apuramos se há teto de noites</span> Lisboa "
             "limita a 7 noites; a página do Porto <b>não informa limite</b>, e o "
             "regulamento e o folheto oficiais são PDF sem texto extraível. "
             "<b>O calculador cobra todas as noites</b>, que erra para mais e nunca "
             "para menos. Nas 4 noites desta ficha, um teto de 7 não mudaria nada.",
             {"noite": "3.0000", "rot": "Taxa municipal turística, {n}"}),
            # ---------------------------------------------------- ingressos
            ("ingresso", 15.95, "Livraria Lello", "€ 15,95",
             "Loja oficial de bilhetes da própria livraria (tickets.livrarialello.pt), "
             "consultada em 24–25/set/2026.<br>"
             "<b>O valor é dedutível num livro Edições Livraria Lello</b> — quem "
             "comprar uma edição da casa usa os € 15,95 como crédito e a entrada sai "
             "de graça. <b>Se você já ia comprar um livro, esta linha é zero.</b><br>"
             "Cuidado com o Ticket-Voucher Ai Weiwei, de € 8,00: é mais barato e "
             "<b>não dá acesso ao edifício histórico</b>."),
            ("ingresso", 10.00, "Torre dos Clérigos, Torre + Museu", "€ 10,00",
             "Bilheteira oficial da Irmandade dos Clérigos (torredosclerigos.pt), "
             "consultada em 24–25/set/2026. É o único bilhete diurno que existe. "
             "Estudante com identificação paga € 7,00 e <b>criança até 10 anos não "
             "paga</b>.<br>"
             "<span class=\"flag\">O valor que circula está errado</span> agregadores "
             "dão a entrada como € 6. A bilheteira oficial não tem nenhum bilhete "
             "diurno nesse valor."),
            ("ingresso", 14.00, "Palácio da Bolsa", "€ 14,00",
             "Página de turismo do site oficial (palaciodabolsa.com), consultada em "
             "24–25/set/2026. Estudante, escola e sénior pagam € 9,50; menores de 12 "
             "acompanhados não pagam, <b>exceto em grupos de crianças</b>.<br>"
             "<b>A visita é obrigatoriamente guiada e dura cerca de 30 minutos</b>, com "
             "o idioma definido por ordem de chegada. Reserve tempo de espera: não "
             "existe visita livre."),
            ("ingresso", 24.00, "Serralves, bilhete geral", "€ 24,00",
             "Bilheteira oficial da Fundação de Serralves (serralves.byblueticket.pt), "
             "consultada em 24–25/set/2026. Residente paga € 20,00.<br>"
             "Inclui <b>museu, parque de 18 hectares, Treetop Walk, Casa de Serralves e "
             "Casa do Cinema</b>. <b>Só o parque custa € 15,00.</b><br>"
             "<b>Não pagam</b> crianças até 11 anos, Amigos de Serralves e portadores "
             "de Cartão BPI. <span class=\"flag\">Os valores com desconto não são "
             "publicados</span> jovem, estudante e sénior têm desconto que só aparece "
             "na finalização da compra online."),
            ("ingresso", 12.00, "Casa da Música, visita guiada", "€ 12",
             "Página de visitas guiadas do site oficial (casadamusica.com), consultada "
             "em 24–25/set/2026. Jovem de 13 a 18 anos paga € 5; menor de 12 não paga, "
             "com adulto pagante; <b>com Porto Card sai por € 9</b>.<br>"
             "<b>Visitas às 11h e às 15h</b>, em português, espanhol, francês e "
             "italiano, cerca de uma hora, <b>lotação de 35 pessoas</b>.<br>"
             "<b>Os espaços abertos dependem da programação do dia</b> — é sala de "
             "concertos em funcionamento."),
            ("ingresso", 10.00, "Teleférico de Gaia, ida e volta", "€ 10,00",
             "Página de preços e horários do site oficial (gaiacablecar.com), "
             "consultada em 24–25/set/2026. <b>Só ida custa € 7,00.</b> Criança de 5 a "
             "12 anos paga € 5,00 ida e volta.<br>"
             "<b>Família de 2 adultos e 2 crianças, ida e volta: € 22,50</b> — contra "
             "€ 30,00 comprando à parte, poupa € 7,50.<br>"
             "O bilhete <b>vale 30 dias</b> a contar da compra. Fecha só no dia de "
             "Natal."),
            ("ingresso", 3.00, "Sé do Porto", "€ 3",
             "Ficha oficial da Direção Regional de Cultura do Norte, no portal do "
             "Governo (culturaportugal.gov.pt), consultada em 24–25/set/2026.<br>"
             "<b>A torre fecha meia hora antes da catedral</b>: 17h contra 17h30 de "
             "novembro a março, 18h contra 18h30 de abril a outubro.<br>"
             "<span class=\"flag\">A fonte oficial não diz do que é o bilhete</span> "
             "publica esse valor único e não discrimina nave, claustro, torre nem "
             "museu, nem informa descontos."),
            # ---------------------------------------------------- gratuitos
            ("ingresso", 0, "Ponte Dom Luís I", "Grátis",
             "<b>Não há bilheteira.</b> Os dois tabuleiros têm passeio para pedestre — "
             "o superior, por onde passa o metrô, e o inferior, que liga o Cais da "
             "Ribeira a Gaia.<br>"
             "A travessia a pé pelo tabuleiro superior é a melhor vista gratuita da "
             "cidade, e sai no mesmo lugar em que começa a descida para as caves."),
            ("ingresso", 0, "Centro Histórico e Ribeira", "Grátis",
             "<b>É a cidade: não há bilheteira.</b> O conjunto está inscrito na Lista "
             "do Património Mundial da UNESCO desde 5 de dezembro de 1996, pelo "
             "critério IV — ficha do Património Cultural / DGPC, consultada em "
             "24–25/set/2026."),
            ("ingresso", 0, "Estação de São Bento", "Grátis",
             "<b>É estação ferroviária em funcionamento</b>, não há bilhete para "
             "entrar no átrio. Os <b>cerca de vinte mil azulejos</b> do pintor Jorge "
             "Colaço estão a poucos passos da porta.<br>"
             "Classificada como Imóvel de Interesse Público pelo Decreto n.º 67/97 — "
             "ficha da DGPC, consultada em 24–25/set/2026."),
            ("ingresso", 0, "Jardins do Palácio de Cristal", "Grátis",
             "Página oficial do município, no portal do Ambiente da Câmara Municipal "
             "(ambiente.cm-porto.pt), consultada em 24–25/set/2026.<br>"
             "<b>O acesso é livre por condição de venda</b>: a propriedade foi vendida "
             "à Câmara com a obrigação de se tornar espaço verde público.<br>"
             "<b>O Palácio de Cristal não existe</b> — foi demolido em 1951. Quem "
             "procura o edifício de ferro e vidro encontra o Pavilhão Rosa Mota."),
            # ---------------------------------------------------- fora do total
            ("ingresso", None, "Igreja e Museu de São Francisco",
             "<span class=\"flag\">Não publicado</span>",
             "<b>A bilheteira existe e o preço não é publicado.</b> O site oficial da "
             "Venerável Ordem Terceira de São Francisco do Porto divulga o horário com "
             "precisão — 9h às 20h no verão, 9h às 19h no inverno, fechado só em 25 de "
             "dezembro — e <b>não tem preçário nem bilheteira online</b>. Conferimos "
             "todos os links da página em 24–25/set/2026.<br>"
             "Valores de agregador não entram: foi um deles que deu a Torre dos "
             "Clérigos 40% mais barata do que ela é. <b>Fora do total.</b>"),
            ("ingresso", None, "Caves do Vinho do Porto",
             "<span class=\"flag\">Sem tarifa única</span>",
             "<b>São dezenas de operadores privados, cada um com o seu preço</b>, e as "
             "três mais procuradas quase não publicam tarifa. A Taylor's divulga "
             "horário, os 13 idiomas do audioguia e até quais os três vinhos da prova "
             "— e não o preço. A Graham's também não. A Cálem vende por um botão que "
             "não abre tabela. Conferido em 24–25/set/2026.<br>"
             "<b>Fora do total</b>, porque não há número a somar. Confirme direto com "
             "a cave antes de ir."),
            ("ingresso", None, "Capela das Almas",
             "<span class=\"flag\">Não apurado</span>",
             "<b>É templo em funcionamento, não museu</b>, e não encontramos site "
             "oficial da paróquia com horário ou tarifa em 24–25/set/2026. Os horários "
             "que circulam vêm de agregadores e divergem entre si.<br>"
             "Vale a parada mesmo assim: os azulejos da fachada <b>são de 1929 e imitam "
             "os do século XVIII de propósito</b>. <b>Fora do total.</b>"),
            ("ingresso", None, "Mercado do Bolhão",
             "<span class=\"flag\">Não apurado</span>",
             "O site oficial divulga horários, bancas e serviços e <b>não menciona "
             "bilhete nem preço de acesso</b>. Como a fonte não escreve “entrada "
             "gratuita”, não afirmamos que é — a regra vale igual para número alto e "
             "para número zero.<br>"
             "<b>Fecha aos domingos</b>, e muito roteiro de fim de semana o marca para "
             "domingo de manhã. <b>Fora do total.</b>"),
            ("ingresso", 0, "Hospedagem",
             "<span class=\"flag\">Não apurada</span>",
             "<b>O INE publica ADR só para Portugal inteiro</b> — 130,90 € em maio de "
             "2026 — e não encontramos a série aberta por município. Os destaques "
             "mensais dão o Porto em <b>dormidas</b>, não em preço médio.<br>"
             "<b>Sem número da cidade, sem linha.</b> Preferimos a conta incompleta e "
             "honesta à conta completa e inventada. <b>Fora do total.</b>"),
        ],
        "rodape_tabela": (
            "Valores em euro, por pessoa, apurados em fonte oficial em 24 e 25 de "
            "setembro de 2026. <b>Quatro linhas estão fora do total</b> e estão "
            "marcadas na tabela.<br>"
            "<b>O combinado que vale a pena:</b> Clérigos, Casa da Música e Serralves "
            "à parte somam <b>€ 46,00</b>. Comprando <b>Casa da Música + Serralves por "
            "€ 28,80</b> e os Clérigos à parte, dá <b>€ 38,80</b> — poupa <b>€ 7,20</b> "
            "sem cortar nada. Há também Clérigos + Serralves por € 27,20, contra "
            "€ 34,00 separados."),
        "parceiros": [
            ("https://www.booking.com/", "Booking.com", "hotéis e apartamentos"),
            ("https://www.getyourguide.com/", "GetYourGuide", "ingressos e passeios"),
        ],
        "fontes": (
            "Cada linha traz a fonte e a data no próprio campo. As tarifas vêm das "
            "páginas oficiais da Livraria Lello, da Irmandade dos Clérigos, do Palácio "
            "da Bolsa, da Fundação de Serralves, da Casa da Música, do Teleférico de "
            "Gaia, da Direção Regional de Cultura do Norte, do Metro do Porto e da "
            "Câmara Municipal do Porto. <b>Nenhum valor veio de agregador de viagem.</b> "
            "<b>E um deles foi desmentido por isso:</b> a Torre dos Clérigos aparece a "
            "€ 6 em resumo de busca e custa € 10 na bilheteira oficial."),
    },
}

# A barra "Calcular para" lista todas as fichas do site. O Porto entra no
# fim, na ordem em que foi publicado. O dedupe protege contra o caso de o
# novos2 ja ter sido carregado antes neste mesmo processo.
base.CIDADES = base.CIDADES + [("porto", "Porto")]
_vistos, _limpo = set(), []
for _slug, _nome in base.CIDADES:
    if _slug not in _vistos:
        _vistos.add(_slug)
        _limpo.append((_slug, _nome))
base.CIDADES = _limpo

base.FICHAS = FICHAS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
