# -*- coding: utf-8 -*-
"""Roteiros de Cancun e Fortaleza, montados sobre a apuracao das fichas.

O que torna um roteiro util nao e a ordem bonita: e o dia da semana que
fecha alguma coisa. Tudo aqui sai dos mesmos horarios apurados em
17/set/2026 e registrados em dados.py — nenhum horario novo foi inventado
para fazer o roteiro fechar.
"""

ROTEIROS = {
    "cancun": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Cancún",
        "descricao": ("Cinco dias entre Cancún e a Riviera Maya na ordem que respeita as "
                      "últimas entradas — e o único dia da semana que fecha o museu da "
                      "Zona Hoteleira."),
        "abertura": ("Cinco dias por distância, do que está na Zona Hoteleira ao que exige "
                     "200 km de estrada — e na ordem que não perde nenhuma última entrada."),
        "avisos": [
            ("b", "O que decide este roteiro não é o horário de abrir: é o de parar de entrar",
             "<p><b>Três dos seis pontos têm hora de corte antes do fechamento</b>, e é aí "
             "que o dia dá errado para quem se guia pelo horário de encerramento.</p>"
             "<p><b>Tulum fecha às 17h, mas a última entrada é às 15h30.</b> Chegar às 16h "
             "é encontrar o sítio aberto e o portão fechado para você.</p>"
             "<p><b>No Museo Maya há dois relógios diferentes dentro do mesmo bilhete:</b> "
             "a última entrada no museu é às 17h, mas <b>em San Miguelito é às 16h30</b>. "
             "Quem chega às 16h45 paga o bilhete inteiro e vê metade.</p>"
             "<p><b>Chichén Itzá fecha às 16h</b>, e fica a cerca de 200 km de Cancún. É o "
             "único ponto deste guia que exige sair antes do amanhecer.</p>"),
            ("a", "A segunda-feira tira o único ponto que não exige estrada",
             "<p><b>O Museo Maya de Cancún e San Miguelito fecham às segundas</b> — e são "
             "o único ponto do guia dentro da Zona Hoteleira, a única visita que não "
             "custa meio dia de carro ou barco.</p>"
             "<p>Se a sua semana tem uma segunda, ela é dia de praia ou de Isla Mujeres. "
             "<b>Não tente resolver o museu numa segunda:</b> ele não abre.</p>"),
            ("", "O domingo gratuito não é para você",
             "<p>O INAH libera a entrada aos domingos, e isso aparece em guia de viagem sem "
             "a letra miúda. <b>A gratuidade é para mexicanos e estrangeiros residentes no "
             "México</b>, com documento.</p><p><b>O turista brasileiro paga integral todos "
             "os dias da semana</b>, inclusive domingo — e em Chichén Itzá paga as duas "
             "taxas, a federal e a estadual.</p>"),
        ],
        "dias_lista": [
            ("Zona Hoteleira, sem sair de Cancún — em qualquer dia menos segunda",
             "O dia mais barato e o único que não exige estrada. Comece no <b>Museo Maya de "
             "Cancún</b>, no km 16,5 do Boulevard Kukulcán: <b>MX$ 210 para estrangeiro</b>, "
             "e o mesmo bilhete vale para a <b>zona arqueológica de San Miguelito</b>, que "
             "fica no mesmo terreno. <b>Faça San Miguelito primeiro</b>, porque a última "
             "entrada nele é às 16h30, meia hora antes da do museu. Feche na "
             "<b>Playa Delfines</b>, ainda no Kukulcán: no México toda praia é federal e de "
             "acesso público, nenhum hotel pode fechar a faixa de areia, e esta é a maior "
             "praia pública da Zona Hoteleira. Não se paga nada por ela.",
             [("Museo Maya e San Miguelito · MX$ 210 · fecha segunda"),
              ("San Miguelito · última entrada 16h30"),
              ("Playa Delfines · grátis, sempre aberta")]),
            ("Chichén Itzá — e este é o dia de acordar cedo",
             "São cerca de <b>200 km</b> de Cancún, e o sítio <b>fecha às 16h</b>: a conta "
             "de ida e volta não perdoa saída tardia. O preço são <b>duas cobranças "
             "somadas</b>, e é a parte que os guias costumam omitir: <b>MX$ 105 do INAH "
             "federal mais MX$ 592 da taxa estadual de Yucatán</b>, o que dá "
             "<b>MX$ 697</b>. <span class=\"flag\">Fontes divergem</span> a imprensa "
             "mexicana publicou MX$ 571 para a taxa estadual em janeiro de 2026 e a página "
             "do INAH diz MX$ 592 — <b>leve o valor maior</b>. A vila de Piste fica a 2 km "
             "do sítio e tem transporte público.",
             [("Chichén Itzá · MX$ 697 no total"),
              ("MX$ 105 INAH + MX$ 592 taxa de Yucatán"),
              ("Abre todos os dias · 8h às 16h")]),
            ("Tulum, com o relógio na mão",
             "Cerca de <b>130 km</b> de Cancún, dentro do Parque del Jaguar. "
             "<b>MX$ 210 de segunda a sábado</b> para estrangeiro. <b>O reajuste de 2026 "
             "praticamente dobrou este valor</b> — em 2025 era cerca de MX$ 104, e qualquer "
             "roteiro escrito antes deste ano está errado pela metade. O sítio abre às 8h e "
             "fecha às 17h, <b>mas a última entrada é às 15h30</b>: este é o dia em que "
             "chegar depois do almoço custa a visita inteira. "
             "<span class=\"flag\">Não apurado</span> o Parque del Jaguar pode cobrar taxa "
             "própria, somada à do INAH, como Yucatán faz em Chichén Itzá. Não achamos o "
             "valor em fonte oficial e não vamos publicar número que não confirmamos — "
             "<b>leve folga no orçamento do dia</b>.",
             [("Tulum · MX$ 210 · dobrou em 2026"),
              ("Última entrada 15h30, não 17h"),
              ("Taxa do Parque del Jaguar não apurada")]),
            ("Isla Mujeres, de ferry — bom para uma segunda-feira",
             "<b>Entrar na ilha é de graça; o que se paga é a travessia.</b> A Ultramar "
             "cobra <b>MX$ 290 a ida e MX$ 580 ida e volta</b> por adulto, e "
             "<b>MX$ 220 e MX$ 440</b> por criança. <b>Atenção à régua, que é altura e não "
             "idade:</b> criança acima de 1,20 m paga tarifa de adulto. Sai de "
             "<b>Puerto Juárez</b> ou da <b>Playa Tortugas</b>, na própria Zona Hoteleira, "
             "<b>pelo mesmo preço</b> — de Puerto Juárez a travessia leva cerca de 20 "
             "minutos. <span class=\"flag\">Horário não apurado</span> a Ultramar avisa que "
             "tarifas e horários mudam sem aviso e não publica a grade completa na página "
             "de tarifas. Reconfira no dia.",
             [("Ferry Ultramar · MX$ 580 ida e volta"),
              ("Criança acima de 1,20 m paga adulto"),
              ("Entrar na ilha não se paga")]),
            ("Xcaret, o dia inteiro — e o dia mais caro",
             "Cerca de <b>70 km</b>, na Riviera Maya. <b>Xcaret não tem um preço; tem uma "
             "faixa que muda com a data e com o tipo de bilhete</b>, como os parques de "
             "Orlando. <span class=\"flag\">Fontes divergem</span> apuramos <b>três valores "
             "diferentes no mesmo dia</b> para adulto: MX$ 1.890, MX$ 2.180 e MX$ 2.480. "
             "<b>Não escolhemos nenhum</b> — o preço real é o que o site oficial mostrar "
             "para a sua data. O parque abre às 8h30 e vai até as <b>22h</b>, e o show "
             "noturno é o fecho: <b>quem sai às 18h paga o dia inteiro e perde a parte que "
             "justifica o horário estendido</b>.",
             [("Xcaret · MX$ 1.890 a 2.480, conforme a data"),
              ("8h30 às 22h · o show é no fim"),
              ("Reserve o dia inteiro")]),
        ],
        "fontes": (
            "Apuração de 17 de setembro de 2026. Fontes: páginas oficiais do INAH para "
            "Chichén Itzá, Tulum e o Museo Maya de Cancún; tabela de tarifas da Ultramar "
            "para o ferry de Isla Mujeres. Os horários citados são os publicados por cada "
            "ponto na data da apuração — <b>confirme antes de sair</b>, com atenção "
            "especial às horas de última entrada, que são o que estraga o dia aqui. "
            "Onde a fonte não publica o dado, esta página diz que não publica em vez de "
            "estimar: é o caso da <b>taxa do Parque del Jaguar</b> em Tulum, do "
            "<b>preço de Xcaret</b>, em que três fontes divergem, e da grade de horários "
            "do ferry. A <b>taxa estadual de Chichén Itzá</b> aparece como MX$ 592 no INAH "
            "e MX$ 571 na imprensa mexicana, e as duas ficam declaradas."),
    },

    "fortaleza": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Fortaleza",
        "descricao": ("Cinco dias em Fortaleza na ordem que resolve o calendário: a janela "
                      "de quarta a sexta que abre o Centro inteiro, e a taxa de "
                      "Jericoacoara que a Justiça suspendeu."),
        "abertura": ("Cinco dias na ordem que resolve o calendário do Centro — porque em "
                     "Fortaleza há uma janela de três dias em que tudo abre junto, e fora "
                     "dela sempre falta alguma coisa."),
        "avisos": [
            ("b", "Existe uma janela de três dias, e o roteiro inteiro gira em torno dela",
             "<p><b>O Centro de Fortaleza tem quatro pontos a distância de caminhada, e "
             "cada um fecha num dia diferente.</b> Cruzando os quatro horários, sobra uma "
             "janela só.</p>"
             "<p><b>Segunda fecha dois:</b> o Theatro José de Alencar e o Centro Dragão do "
             "Mar não abrem.</p>"
             "<p><b>Terça abre o Dragão do Mar, mas não os museus dele:</b> o centro "
             "funciona de terça a domingo, e <b>os museus só de quarta a sábado</b>. Quem "
             "vai numa terça encontra o prédio aberto e as duas exposições fechadas.</p>"
             "<p><b>Domingo fecha a Catedral para visita:</b> a visitação é de segunda a "
             "sexta, das 8h às 12h e das 13h às 17h, e sábado só de manhã. No domingo há "
             "missa, não visita.</p>"
             "<p><b>E o Mercado Central encurta no fim de semana:</b> até as 18h de segunda "
             "a sexta, <b>17h no sábado e 13h no domingo</b>.</p>"
             "<p><b>Sobra quarta, quinta ou sexta.</b> É o único intervalo em que o "
             "Theatro, a Catedral, o Mercado e os museus do Dragão do Mar estão abertos ao "
             "mesmo tempo — e é por isso que o Dia 1 abaixo tem dia da semana marcado.</p>"),
            ("a", "A visita guiada do Theatro tem hora marcada, não é livre",
             "<p><b>Não se entra no Theatro José de Alencar a qualquer hora.</b> A visita é "
             "mediada por guia e sai em <b>horários fixos: 9h, 10h30, 14h e 16h</b>, de "
             "terça a sábado. <b>Aos domingos, só 9h e 10h30</b>, porque o teatro fecha ao "
             "meio-dia.</p><p>Recomenda-se chegar <b>20 minutos antes</b>. "
             "<b>R$ 10 a inteira e R$ 5 a meia</b>; criança até 5 anos e pessoa acima de 60 "
             "não pagam. É o ingresso mais barato deste guia.</p>"),
            ("", "Jericoacoara custa R$ 41,50, e não R$ 91,50",
             "<p><b>A taxa de R$ 50 do ICMBio está suspensa por decisão judicial.</b> A "
             "concessão do Parque Nacional previa somá-la aos R$ 41,50 da Taxa de Turismo "
             "Sustentável da Prefeitura de Jijoca, <b>mas a Justiça Federal suspendeu a "
             "cobrança</b> até que ICMBio e concessionária apresentem plano detalhado. Em "
             "dezembro de 2025 o <b>TRF-5 rejeitou o recurso pela segunda vez</b>.</p>"
             "<p><b>Muito roteiro publicado ainda soma os dois.</b> Hoje a única taxa "
             "obrigatória é a municipal, de <b>R$ 41,50 por pessoa</b>.</p>"),
        ],
        "dias_lista": [
            ("Centro histórico a pé — e que seja quarta, quinta ou sexta",
             "O dia mais denso do roteiro, e o único que depende do dia da semana. Comece no "
             "<b>Theatro José de Alencar</b> na visita das <b>9h</b>, chegando às 8h40: "
             "<b>R$ 10 a inteira</b>, e o percurso cobre o prédio de 1910, os seis espaços "
             "cênicos e os jardins. <b>A estrutura metálica veio de Glasgow</b>, fundida "
             "pela Walter MacFarlane &amp; Company e importada pela Casa Boris — está à "
             "vista, sem revestimento. <b>Os jardins de Burle Marx não são originais:</b> o "
             "projeto de 1908 já imaginava um teatro-jardim, mas a parte verde só veio na "
             "reforma de <b>1975</b>. Siga para a <b>Catedral Metropolitana de São José</b>, "
             "na Praça Pedro II, que não cobra nada e comporta cinco mil pessoas — "
             "<b>mas fecha das 12h às 13h</b>, então não a deixe para o meio-dia. Almoce e "
             "vá ao <b>Mercado Central</b>, na Av. Alberto Nepomuceno, 199: entrada franca, "
             "<b>mais de 600 lojas em cinco andares</b>. Feche no <b>Centro Dragão do Mar</b>, "
             "na virada para a Praia de Iracema, que fica aberto até as <b>21h</b> e tem "
             "cerca de <b>90% da programação gratuita</b>.",
             [("Theatro José de Alencar · R$ 10 · visita 9h, 10h30, 14h, 16h"),
              ("Catedral · grátis · fecha das 12h às 13h"),
              ("Mercado Central · grátis · até 18h em dia útil"),
              ("Dragão do Mar · ~90% grátis · museus só de quarta a sábado")]),
            ("Praia do Futuro — o dia que funciona até numa segunda",
             "<b>Sete quilômetros de praia urbana</b>, faixa larga, areia clara e mar "
             "aberto. <b>A praia não cobra nada</b>; o que cobra é a barraca, e as "
             "estruturas da orla oferecem mesa, chuveiro, banheiro e refeição. "
             "<span class=\"flag\">Sem preço apurado</span> não levantamos consumação "
             "mínima nem aluguel de mesa, e por isso nada disso entra na ficha de custos. "
             "<span class=\"flag\">Não apurado</span> horário de guarda-vidas e sinalização "
             "de banho — <b>o mar da Praia do Futuro é aberto e tem correnteza</b>, e isso é "
             "relevante demais para publicarmos sem fonte oficial. <b>Guarde este dia para "
             "a segunda-feira</b>, que é quando o Centro fecha.",
             [("Praia do Futuro · grátis · aberta sempre"),
              ("Barracas cobram consumo · valor não apurado"),
              ("Mar aberto, com correnteza")]),
            ("Beach Park, em Aquiraz",
             "<b>27 km</b> de Fortaleza, na praia de Porto das Dunas. O <b>Aqua Park</b> "
             "abre a bilheteria às 10h30 e opera das <b>11h às 17h</b>; o <b>Parque "
             "Arvorar</b>, que reúne mais de 250 animais, das <b>9h às 17h</b>. "
             "<b>Não existe preço fechado:</b> o site oficial anuncia o Aqua Park "
             "<b>a partir de R$ 250</b> e o Arvorar <b>a partir de R$ 129</b>, e o valor "
             "muda conforme a data e a antecedência da compra. "
             "<span class=\"flag\">Fontes divergem</span> sites de terceiros publicam faixa "
             "de R$ 210 a R$ 325 e prometem R$ 210 com 44 dias de antecedência — "
             "<b>o oficial é o que vale no checkout</b>. <b>A régua da criança é altura, "
             "não idade:</b> até 1 metro, acompanhada de adulto pagante, não paga.",
             [("Aqua Park · a partir de R$ 250 · 11h às 17h"),
              ("Arvorar · a partir de R$ 129 · 9h às 17h"),
              ("Criança até 1 metro não paga")]),
            ("Estrada para Jericoacoara",
             "São cerca de <b>300 km</b> de Fortaleza, e o acesso final é por areia — "
             "<b>é bate-volta longo demais para caber num dia</b>, e a maior parte de quem "
             "vai dorme lá. Por isso ele ocupa dois dias deste roteiro. <b>A única taxa "
             "obrigatória é a Taxa de Turismo Sustentável, de R$ 41,50 por pessoa</b>, "
             "cobrada pela Prefeitura de Jijoca de Jericoacoara. <b>A taxa de R$ 50 do "
             "ICMBio continua suspensa</b> por decisão da Justiça Federal, mantida pelo "
             "TRF-5 em dezembro de 2025. <span class=\"flag\">Não apurado</span> horário de "
             "entrada de veículo na vila e restrição de tráfego nas dunas: não achamos a "
             "regra oficial publicada.",
             [("Taxa de Turismo Sustentável · R$ 41,50"),
              ("Taxa ICMBio de R$ 50 · suspensa pela Justiça"),
              ("300 km · acesso final por areia")]),
            ("Jericoacoara e a volta",
             "O dia da vila e das dunas, e a estrada de volta. <b>Nada aqui foi apurado por "
             "nós além da taxa de entrada</b> — passeio de buggy, lagoas, Pedra Furada e "
             "pôr do sol na duna não têm preço levantado nesta camada, e por isso não "
             "aparecem com valor. <span class=\"flag\">Camada seguinte</span> esta página "
             "cresce como as outras do site: o que entra, entra com fonte e data. "
             "<b>Preferimos dizer que não apuramos a dizer um número que não conferimos.</b>",
             [("Vila e dunas · sem preço apurado nesta camada"),
              ("Volta a Fortaleza · cerca de 300 km")]),
        ],
        "fontes": (
            "Apuração de 17 de setembro de 2026. Fontes: Instituto Dragão do Mar para os "
            "horários e a gratuidade do centro cultural; site oficial de ingressos do Beach "
            "Park; Arquidiocese de Fortaleza para os horários da Catedral; e as decisões da "
            "Justiça Federal e do TRF-5 sobre a suspensão da taxa do ICMBio em Jericoacoara. "
            "Os horários citados são os publicados por cada ponto na data da apuração — "
            "<b>confirme antes de sair</b>, com atenção ao Centro, onde cada endereço fecha "
            "num dia diferente. Onde a fonte não publica o dado, esta página diz que não "
            "publica em vez de estimar: é o caso da <b>consumação nas barracas da Praia do "
            "Futuro</b>, do <b>calendário anual do Beach Park</b> e das <b>regras de "
            "tráfego nas dunas de Jericoacoara</b>. O <b>preço do Beach Park</b> aparece "
            "como a partir de R$ 250 no site oficial e como R$ 210 a R$ 325 em sites de "
            "terceiros, e os dois ficam declarados. <b>Também não há aqui diária de "
            "hospedagem</b>: não encontramos número publicado para Fortaleza que sirva de "
            "referência, e a ficha de custos só existirá quando ele existir."),
    },
}
