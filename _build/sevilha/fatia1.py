# -*- coding: utf-8 -*-
"""Apuracao de Sevilha, com fonte e data em cada numero.

POR QUE SEVILHA, E NAO MADRI

Madri foi tentada primeiro e abandonada no meio. Os sites oficiais
espanhois de la sao fechados: o Museo del Prado esta atras de verificacao
anti-bot da Cloudflare, o Metro de Madrid so mostra tarifa depois de abrir
acordeao, e a bilheteira do Palacio Real so revela preco depois de
escolher data num calendario. Cada ponto custava cinco ou seis vezes mais
que no Porto, e dois dos mais buscados iam ficar sem preco.

Sevilha e o oposto: o Real Alcazar e a Catedral publicam tabela completa
em pagina simples, e sairam de primeira.

O metodo nao mudou - mudou o destino, porque a regra da casa e que pagina
sem numero apurado nao vale a pena. Fica registrado para ninguem tentar
Madri de novo pelo mesmo caminho.

O QUE ESTA APURACAO ACHOU
-------------------------

1. DUAS PAGINAS OFICIAIS DA CATEDRAL DISCORDAM entre si sobre o horario
   da entrada gratuita de domingo. A de horarios e tarifas diz 16h30 as
   18h; a de planejamento de alta temporada diz 14h30 as 18h. As duas sao
   do mesmo dominio. Entram as duas, sem escolher.

2. A ENTRADA PAGA NA PLAZA DE ESPANA NAO EXISTE. O prefeito anunciou em
   2024 que cobraria tres euros de turista. Procurei nas ordenancas
   fiscais de Sevilha, inclusive nas de 2026: nao ha taxa aprovada. A
   praca continua de acesso livre, e muito texto de viagem ja fala da
   cobranca como se ela valesse.

3. O ALCAZAR TEM DOIS INGRESSOS, E O SEGUNDO QUASE NINGUEM CONTA. O
   Cuarto Real Alto custa 5,50 EUR a parte da entrada geral.

4. NAO CONSEGUIMOS O TRANSPORTE. O TUSSAM esta atras da Cloudflare e o
   Metro de Sevilha devolve 401. Fica escrito - e com a observacao que
   importa: os quatro pontos desta fatia se fazem a pe.

Apuracao de 25 de setembro de 2026.
"""

APURACAO = "25 de setembro de 2026"
APURACAO_CURTA = "25/set/2026"


def mapa(consulta):
    """Link para o Google Maps no padrao da casa."""
    import urllib.parse
    q = urllib.parse.quote(consulta)
    return ('<a class="mapa" href="https://www.google.com/maps/search/?api=1&query=%s"'
            ' target="_blank" rel="noopener" aria-label="Abrir %s no Google Maps">'
            '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
            '<path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z" stroke="currentColor"'
            ' stroke-width="1.8" stroke-linejoin="round"></path><circle cx="12" cy="10" r="2.5"'
            ' stroke="currentColor" stroke-width="1.8"></circle></svg><span>Ver no mapa</span></a>'
            % (q, consulta.split(",")[0]))


SEVILHA = {
    "slug": "sevilha",
    "nome": "Sevilha",
    "pais": "Espanha",
    "regiao": "europa",
    "titulo": "Sevilha: preço e horário verificados na fonte oficial",
    "descricao": ("Preço, horário e fonte de cinco pontos centrais de Sevilha — com o "
                  "segundo ingresso do Alcázar que quase ninguém soma e a cobrança da "
                  "Plaza de España que foi anunciada e nunca aprovada."),
    "abertura": ("Cinco pontos centrais com preço, horário e fonte conferidos em 25 de "
                 "setembro de 2026 — e o detalhe que muda a conta: <b>a entrada paga na "
                 "Plaza de España foi anunciada em 2024 e nunca existiu</b>."),
    "busca": ("sevilha sevilla espanha andaluzia real alcazar catedral giralda plaza de espana "
              "setas de sevilla metropol parasol antiquarium cuarto real alto patio de las "
              "doncellas salon de embajadores triana santa cruz guadalquivir torre del oro "
              "archivo de indias tussam metro de sevilla"),
    "grupos": [
        {"id": "g1", "titulo": "Os dois que cobram, e valem",
         "intro": ("O palácio e a catedral ficam a duzentos metros um do outro, e os dois "
                   "têm tarifa publicada em tabela — o que em Espanha é menos comum do "
                   "que parece.")},
        {"id": "g2", "titulo": "O que não cobra, e o que quase cobrou",
         "intro": ("A praça mais fotografada da cidade continua de acesso livre, apesar do "
                   "que muito texto de viagem afirma.")},
        {"id": "g3", "titulo": "Como circular",
         "intro": ("O centro histórico se faz inteiro a pé — o que é bom, porque as duas "
                   "operadoras de transporte fecharam a porta para a apuração.")},
    ],
    "pontos": [
        # -------------------------------------------------------------
        {
            "id": "real-alcazar", "grupo": "g1",
            "foto": {"arq": "sevilha/real-alcazar.webp",
                     "alt": "Patio de las Doncellas no Real Alcázar, com as arcadas rendilhadas em volta do espelho d'água e os canteiros rebaixados dos lados",
                     "cred": "Benjamin Smith · CC BY-SA 4.0 · via Wikimedia Commons"},
            "nome": "Real Alcázar", "tag": "Palácio",
            "preco_val": "€ 15,50",
            "preco_nota": "o Cuarto Real Alto custa € 5,50 à parte",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página <i>Prepara la visita</i> do site oficial do Real Alcázar "
                 "(alcazarsevilla.org), consultada em 25/set/2026.<br>"
                 "<b>Entrada geral: € 15,50.</b><br>"
                 "<b>Entrada reduzida: € 8,00</b> — maiores de 65 anos, estudantes de 14 a "
                 "30 anos e portadores do Carné Jovem Europeu.<br>"
                 "<b>Cuarto Real Alto: € 5,50</b>, cobrado <b>à parte</b> da entrada geral. "
                 "É o andar onde a família real se hospeda quando está em Sevilha, e é a "
                 "linha que quase nenhum roteiro soma — quem quiser ver tudo gasta "
                 "<b>€ 21,00</b>, não € 15,50."),
                ("Quem não paga",
                 "Mesma fonte, mesma data. A lista é generosa e vale conferir antes de "
                 "comprar:<br>"
                 "<b>Nascidos ou residentes no município de Sevilha.</b><br>"
                 "<b>Menores de 14 anos</b> acompanhados de um adulto responsável.<br>"
                 "<b>Pessoas com deficiência a partir de 33%</b> e um acompanhante.<br>"
                 "<b>Desempregados residentes na província</b>, com documentação válida.<br>"
                 "<b>Pesquisadores acreditados e membros do ICOMOS.</b>"),
                ("Horário e fechamentos",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Inverno, de 1º de outubro a 31 de março: 9h30 às 17h.</b><br>"
                 "<b>Verão, de 1º de abril a 30 de setembro: 9h30 às 19h.</b><br>"
                 "<b>A evacuação do recinto começa 45 minutos após o horário de "
                 "fechamento</b> — ou seja, a última hora útil de visita é antes disso.<br>"
                 "<b>Fechado:</b> 1º e 6 de janeiro, Sexta-feira Santa e 25 de dezembro."),
                ("Como se compra",
                 "Mesma fonte, mesma data. Há venda online e na bilheteira física — e uma "
                 "restrição que pega quem chega com dinheiro em espécie: <b>a bilheteira "
                 "aceita apenas cartão</b>.<br>"
                 "O audioguia é acessado por código QR ou pelo aplicativo, e há um mapa em "
                 "PDF para baixar."),
                ("Onde fica", mapa("Real Alcázar de Sevilla, Patio de Banderas, Sevilha, Espanha")),
            ],
        },
        # -------------------------------------------------------------
        {
            "id": "catedral-giralda", "grupo": "g1",
            "foto": {"arq": "sevilha/catedral-giralda.webp",
                     "alt": "A Giralda vista de baixo, com o campanário renascentista sobre a torre almóada e os pináculos góticos da catedral na base",
                     "cred": "Harvey Barrison from Massapequa, NY, USA · CC BY-SA 2.0 · via Wikimedia Commons"},
            "nome": "Catedral e Giralda", "tag": "Catedral",
            "preco_val": "€ 13",
            "preco_nota": "online; € 14 na bilheteira",
            "campos": [
                ("Valor da entrada",
                 "Fonte: página de <i>Horarios y tarifas</i> do site oficial da Catedral de "
                 "Sevilla (catedraldesevilla.es), consultada em 25/set/2026. A própria "
                 "página informa que as tarifas valem <b>a partir de 1º de janeiro de "
                 "2026</b>.<br>"
                 "<b>Geral: € 13,00 online e € 14,00 na bilheteira.</b><br>"
                 "<b>Reduzida: € 7,00 online e € 8,00 na bilheteira</b> — maiores de 65, "
                 "estudantes até 25 anos, pessoas com deficiência entre 33% e 65% e "
                 "famílias numerosas.<br>"
                 "<b>Comprar online sai € 1,00 mais barato</b> em qualquer faixa, ao "
                 "contrário do que costuma acontecer."),
                ("Audioguia e visita guiada",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Audioguia: € 5,00</b>; pelo aplicativo, <b>€ 4,00</b>.<br>"
                 "<b>Visita guiada: € 20,00 online e € 21,00 na bilheteira</b>, mais "
                 "<b>€ 1,00 de taxa de gestão por bilhete</b> na compra online. Duração "
                 "estimada de 90 minutos.<br>"
                 "A visita comum leva cerca de <b>75 minutos</b>."),
                ("Quem não paga",
                 "Mesma fonte, mesma data. <b>Naturais ou residentes na Arquidiocese de "
                 "Sevilha</b>; <b>menores de 13 anos</b> acompanhados de adulto; "
                 "<b>pessoas com deficiência acima de 65%</b>; e <b>desempregados de "
                 "nacionalidade espanhola</b>. Todos precisam apresentar documentação na "
                 "entrada."),
                ("O horário gratuito, e as duas versões dele",
                 "<span class=\"flag\">Duas páginas oficiais discordam</span> e não vamos "
                 "escolher uma:<br>"
                 "A página de <b>horários e tarifas</b> diz que o acesso gratuito ao "
                 "público geral é aos <b>domingos, das 16h30 às 18h</b>, com reserva online "
                 "prévia e lotação limitada.<br>"
                 "A página de <b>planejamento de visita em alta temporada</b>, do mesmo "
                 "domínio, diz <b>domingos das 14h30 às 18h</b>.<br>"
                 "As duas foram consultadas em 25/set/2026. <b>Se for contar com a "
                 "gratuidade, reserve pelo portal oficial e confirme o horário na hora da "
                 "reserva</b> — e não chegue às 14h40 esperando entrar."),
                ("Horário de visita",
                 "Fonte: página de horários e tarifas, 25/set/2026.<br>"
                 "<b>Segunda a sábado: 10h45 às 19h</b>, com a bilheteira fechando às 18h.<br>"
                 "<b>Domingos: 14h30 às 19h</b>, bilheteira até as 18h.<br>"
                 "O domingo abrir só à tarde é o que mais desorganiza roteiro de fim de "
                 "semana."),
                ("Onde fica", mapa("Catedral de Sevilla, Avenida de la Constitución, Sevilha, Espanha")),
            ],
        },
        # -------------------------------------------------------------
        {
            "id": "setas-de-sevilla", "grupo": "g1",
            "foto": {"arq": "sevilha/setas-de-sevilla.webp",
                     "alt": "A cobertura ondulada das Setas de Sevilla vista do mirador, com os telhados do centro histórico e a Giralda ao fundo",
                     "cred": "Abel Maestro Garcia from Asunción, España · Public domain · via Wikimedia Commons"},
            "nome": "Setas de Sevilla", "tag": "Mirador",
            "preco_val": "€ 16",
            "preco_nota": "a partir de; experiência geral",
            "campos": [
                ("Valor da entrada",
                 "Fonte: site oficial das Setas de Sevilla (setasdesevilla.com), consultado "
                 "em 25/set/2026.<br>"
                 "<b>Experiência geral: a partir de € 16.</b> Inclui o mirador de 360 "
                 "graus, o filme multissensorial <i>Feeling Sevilla</i> e o espetáculo de "
                 "luzes <i>Aurora</i>.<br>"
                 "<b>Pacote com espetáculo de flamenco: a partir de € 48.</b><br>"
                 "<span class=\"flag\">O site diz \"a partir de\" e não publica tabela</span> "
                 "não há preço fechado nem tarifa reduzida publicada, e <b>o Antiquarium — "
                 "as ruínas romanas no subsolo — não aparece com preço próprio</b>. "
                 "Confirme no site antes de contar com um valor."),
                ("Horário, que é o mais longo da cidade",
                 "Mesma fonte, mesma data.<br>"
                 "<b>Todos os dias, das 9h30 à 1h da manhã</b>, com <b>última entrada às "
                 "0h15</b>. É o único ponto desta apuração que funciona à noite.<br>"
                 "<b>O <i>Aurora</i> acontece das 21h30 à 1h, de abril a outubro</b> — "
                 "fora desses meses, quem sobe à noite não vê o espetáculo de luzes.<br>"
                 "A visita leva <b>entre 60 e 90 minutos</b>."),
                ("Onde fica", mapa("Setas de Sevilla, Plaza de la Encarnación, Sevilha, Espanha")),
            ],
        },
        # -------------------------------------------------------------
        {
            "id": "plaza-de-espana", "grupo": "g2",
            "foto": {"arq": "sevilha/plaza-de-espana-ponte.webp",
                     "alt": "Uma das pontes de azulejo da Plaza de España sobre o canal, com a balaustrada branca refletida na água",
                     "cred": "Proa 500 · CC BY-SA 4.0 · via Wikimedia Commons"},
            "nome": "Plaza de España", "tag": "Praça",
            "preco_val": "Grátis",
            "preco_nota": "a cobrança anunciada nunca foi aprovada",
            "campos": [
                ("A entrada paga que não existe",
                 "<b>Em fevereiro e em setembro de 2024, o prefeito de Sevilha anunciou "
                 "que passaria a cobrar de turistas</b> — falou-se em três euros, e depois "
                 "em \"três ou quatro\" — para entrar na parte da praça administrada pela "
                 "prefeitura, com os moradores da província isentos.<br>"
                 "<b>Procuramos a taxa nas ordenanças fiscais de Sevilha, inclusive nas de "
                 "2026, e ela não existe.</b> Não há tarifa aprovada, e a praça continua de "
                 "acesso livre. Conferido em 25/set/2026 no portal da Agencia Tributaria de "
                 "Sevilla (sevilla.org).<br>"
                 "<b>Muito texto de viagem já fala da cobrança como se ela valesse.</b> Se "
                 "um dia valer, será por ordenança publicada — e é lá que dá para conferir."),
                ("Por que a praça tem dois donos",
                 "É o que explica a confusão. <b>O edifício principal é administrado pelo "
                 "governo central</b>, que abriga ali a Delegação do Governo na Andaluzia; "
                 "<b>a parte a céu aberto é da prefeitura</b>. O anúncio de cobrança "
                 "alcançava só a segunda.<br>"
                 "<span class=\"flag\">Sem fonte oficial sobre horário</span> a praça é "
                 "espaço público aberto e não localizamos horário publicado de abertura e "
                 "fechamento."),
                ("Onde fica", mapa("Plaza de España, Sevilha, Espanha")),
            ],
        },
        # -------------------------------------------------------------
        {
            "id": "transporte", "grupo": "g3",
            "foto": {"arq": "sevilha/metro-sevilha.webp",
                     "alt": "Entrada da estação Blas Infante do Metro de Sevilha, com a fachada em concreto e o letreiro verde",
                     "cred": "Andreuvv · CC BY-SA 4.0 · via Wikimedia Commons"},
            "nome": "Transporte urbano", "tag": "Transporte",
            "preco_val": None,
            "preco_nota": "as duas operadoras bloquearam a apuração",
            "campos": [
                ("Por que não há número nesta linha",
                 "<span class=\"flag\">As duas fontes oficiais fecharam a porta</span> em "
                 "25/set/2026, o site da <b>TUSSAM</b>, que opera os ônibus urbanos, "
                 "respondeu com verificação anti-bot da Cloudflare, e o do <b>Metro de "
                 "Sevilla</b> devolveu erro 401 em todas as páginas de tarifa.<br>"
                 "<b>Não copiamos preço de agregador</b>, que é a mesma regra que fez a "
                 "Torre dos Clérigos aparecer a € 10 e não aos € 6 que os resumos de busca "
                 "davam, na apuração do Porto."),
                ("O que ameniza a lacuna",
                 "<b>Os quatro pontos acima se fazem a pé.</b> O Real Alcázar e a Catedral "
                 "são vizinhos, as Setas ficam a cerca de quinze minutos de caminhada, e a "
                 "Plaza de España fica a vinte do Alcázar, atravessando o Parque de María "
                 "Luisa.<br>"
                 "<b>Transporte em Sevilha é assunto de chegada e saída</b> — aeroporto e "
                 "estação — e não de circulação no centro. Enquanto a tarifa não entra "
                 "aqui, é isso que a página promete: nada."),
                ("Onde fica", mapa("Plaza Nueva, Sevilha, Espanha")),
            ],
        },
    ],
}

DESTINOS = [SEVILHA]
