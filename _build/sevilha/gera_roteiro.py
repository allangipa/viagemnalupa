# -*- coding: utf-8 -*-
"""Roteiro de 3 dias em Sevilha.

Reusa o renderizador de novos/gera_roteiro.py, como a ficha de custos faz.

POR QUE TRES DIAS
-----------------
O guia tem 5 pontos apurados e um deles e a linha de transporte. Sao
quatro visitas, todas no centro historico, que se faz a pe. Esticar isso
para cinco dias seria inventar programa - e roteiro inventado e o que
este site existe para nao fazer.

O QUE ORGANIZA ESTE ROTEIRO
---------------------------
Tres fatos apurados, nenhum deles distancia. Sevilha e compacta: o
Alcazar e a Catedral sao vizinhos, as Setas ficam a quinze minutos e a
Plaza de Espana a vinte, tudo a pe.

1. O DOMINGO DA CATEDRAL. De segunda a sabado ela abre as 10h45. NO
   DOMINGO so abre as 14h30 - e a propria apuracao registra que "o
   domingo abrir so a tarde e o que mais desorganiza roteiro de fim de
   semana". Por isso a Catedral e o dia 3, que e o dia mais facil de
   mover, e nao o dia 1.

2. AS SETAS SAO O UNICO PONTO NOTURNO. Abrem das 9h30 a 1h da manha,
   com ultima entrada as 0h15. Todos os outros fecham entre 17h e 19h.
   Poe-las a noite nao e capricho de composicao: e o que libera a manha
   e a tarde inteiras para o que so funciona de dia.

   E ha uma consequencia de calendario que muda o que o visitante ve: o
   espetaculo Aurora acontece das 21h30 a 1h, DE ABRIL A OUTUBRO. Fora
   desses meses quem sobe a noite ve a cidade, e nao o espetaculo.

3. A HORA DE PARAR DE ENTRAR NAO E A DE FECHAR. No Alcazar a evacuacao
   do recinto comeca 45 minutos APOS o horario de fechamento, o que
   encurta a ultima hora util. Na Catedral a bilheteira fecha as 18h e a
   porta as 19h. Nas Setas a ultima entrada e as 0h15, e a visita leva
   entre 60 e 90 minutos.

DE ONDE SAEM OS HORARIOS
------------------------
Todos da apuracao de 25 de setembro de 2026, registrada em
sevilha/dados.py, com fonte nomeada em cada campo.

Onde o horario nao existe em fonte oficial - Barrio de Santa Cruz,
Triana, Parque de Maria Luisa, Archivo de Indias - o roteiro promete
SEQUENCIA, nao hora, e nao atribui preco nenhum. Sao lugares de rua ou
pontos que esta apuracao ainda nao cobriu.

A GRATUIDADE DE DOMINGO TEM DUAS VERSOES OFICIAIS
--------------------------------------------------
E as duas estao no aviso, sem escolha. A pagina de horarios e tarifas da
Catedral diz domingos das 16h30 as 18h; a de planejamento de alta
temporada, do mesmo dominio, diz das 14h30 as 18h. Um roteiro que
cravasse uma das duas mandaria o leitor chegar as 14h40 para encontrar a
porta fechada.

Uso
---
    python _build/sevilha/gera_roteiro.py
    python _build/sevilha/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))
import gera_roteiro as base   # noqa: E402

# O renderizador procura o destino na lista DESTINOS do novos/dados.py, e
# Sevilha mora em sevilha/dados.py. Carregado por CAMINHO pelo mesmo motivo
# anotado no porto/gera_roteiro.py: o import normal devolveria o `dados`
# que o renderizador ja deixou em sys.modules, calado.
#
# E o rodape imprime a data da apuracao, que no renderizador e a do novos
# (17/set) e aqui e 25/set. Sem a troca, a pagina sairia datada errado -
# foi a armadilha que o Porto encontrou e anotou.
_s = importlib.util.spec_from_file_location(
    "dados_sevilha", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "sevilha": {
        "dias": 3,
        "titulo": "Roteiro de 3 dias em Sevilha",
        "descricao": ("Três dias em Sevilha na ordem que respeita o domingo em que a "
                      "Catedral só abre às 14h30, a hora de parar de entrar no Alcázar "
                      "e o único ponto da cidade que funciona à noite — com preço e "
                      "horário conferidos em fonte oficial."),
        "abertura": ("Três dias organizados por três fatos que folheto nenhum junta: "
                     "<b>o domingo que atrasa a Catedral, a evacuação que começa 45 "
                     "minutos depois do fechamento e as Setas, que ficam abertas até "
                     "1h da manhã</b>."),
        "avisos": [
            ("b", "O domingo é o que desorganiza o fim de semana em Sevilha",
             "<p><b>A Catedral abre às 10h45 de segunda a sábado — e só às 14h30 aos "
             "domingos.</b> Quem monta um fim de semana começando pela Catedral na "
             "manhã de domingo perde a manhã inteira.</p>"
             "<p><b>E há entrada gratuita aos domingos, mas duas páginas oficiais "
             "discordam sobre o horário dela.</b> A página de horários e tarifas diz "
             "<b>16h30 às 18h</b>, com reserva online prévia e lotação limitada. A de "
             "planejamento de alta temporada, <b>do mesmo domínio</b>, diz <b>14h30 às "
             "18h</b>. As duas foram consultadas em 25/set/2026 e nós não escolhemos "
             "uma.</p>"
             "<p>Se for contar com a gratuidade, <b>reserve pelo portal oficial e "
             "confirme o horário na hora da reserva</b> — e não chegue às 14h40 "
             "esperando entrar.</p>"),
            ("a", "A hora de parar de entrar não é a hora de fechar",
             "<p><b>No Real Alcázar a evacuação do recinto começa 45 minutos após o "
             "horário de fechamento</b> — ou seja, a última hora útil de visita "
             "termina antes do que a tabela sugere. O Alcázar fecha às <b>17h de 1º de "
             "outubro a 31 de março</b> e às <b>19h de 1º de abril a 30 de setembro</b>, "
             "abrindo sempre às 9h30.</p>"
             "<p><b>Na Catedral a bilheteira fecha às 18h e a porta às 19h.</b> Uma "
             "hora de diferença entre parar de vender e parar de deixar sair.</p>"
             "<p><b>Nas Setas a última entrada é às 0h15</b> e a visita leva entre 60 e "
             "90 minutos.</p>"
             "<p>O Alcázar ainda <b>fecha em quatro datas do ano</b>: 1º e 6 de "
             "janeiro, Sexta-feira Santa e 25 de dezembro.</p>"),
            ("", "Duas coisas práticas que mudam o dia",
             "<p><b>A bilheteira física do Real Alcázar aceita apenas cartão.</b> Não "
             "há pagamento em dinheiro. Quem chega com espécie compra online ou não "
             "entra.</p>"
             "<p><b>O Cuarto Real Alto é cobrado à parte</b>, € 5,50 além da entrada "
             "geral de € 15,50. É o andar onde a família real se hospeda quando está "
             "em Sevilha, e é a linha que quase nenhum roteiro soma: <b>ver tudo custa "
             "€ 21,00, não € 15,50</b>.</p>"
             "<p><b>O espetáculo Aurora, nas Setas, só acontece de abril a outubro</b>, "
             "das 21h30 à 1h. Fora desses meses quem sobe à noite vê a cidade "
             "iluminada, que já vale — mas não vê o espetáculo.</p>"),
        ],
        "dias_lista": [
            ("Chegada, o que não cobra nada — e a noite nas Setas",
             "Comece pela <b>Plaza de España</b>, que é de <b>acesso livre</b> e não "
             "tem hora de fechar. E comece sabendo de uma coisa: <b>a entrada paga "
             "anunciada ali nunca existiu</b>. O prefeito disse em 2024 que cobraria "
             "três euros de turista, a notícia correu o mundo, e não há taxa aprovada "
             "em nenhuma ordenança fiscal do município — nem nas de 2026. Do lado da "
             "praça fica o <b>Parque de María Luisa</b>, também aberto, que é onde a "
             "cidade descansa do calor. Volte ao centro a pé pelo <b>Barrio de Santa "
             "Cruz</b>, o antigo bairro judeu, de ruas estreitas feitas justamente para "
             "dar sombra.<br>"
             "Deixe a noite para as <b>Setas de Sevilla</b>: são <b>€ 16,00</b> e o "
             "<b>único ponto desta apuração que funciona à noite</b> — abertas das 9h30 "
             "à 1h da manhã, com última entrada às 0h15. Reserve de 60 a 90 minutos. "
             "<b>De abril a outubro</b>, o espetáculo Aurora acontece das 21h30 à 1h.",
             ["Plaza de España · grátis · a cobrança anunciada nunca foi aprovada",
              "Parque de María Luisa · grátis · ao lado da praça",
              "Barrio de Santa Cruz · grátis · a pé, sem hora marcada",
              "Setas de Sevilla · € 16,00 · até 1h, última entrada 0h15"]),
            ("O Alcázar inteiro, incluindo o andar que quase ninguém conta",
             "É o dia que pede a manhã inteira, e pede cedo. O <b>Real Alcázar</b> abre "
             "às <b>9h30</b> e fecha às <b>17h no inverno</b> (1º de outubro a 31 de "
             "março) ou às <b>19h no verão</b> (1º de abril a 30 de setembro) — mas "
             "<b>a evacuação do recinto começa 45 minutos depois do fechamento</b>, "
             "então a última hora não é hora de começar a visita.<br>"
             "São <b>€ 15,50</b> de entrada geral. Some o <b>Cuarto Real Alto</b>, "
             "<b>€ 5,50 à parte</b>, e o total vira <b>€ 21,00</b> — a linha que a "
             "maioria dos roteiros omite. Leve cartão: <b>a bilheteira física não "
             "aceita dinheiro</b>.<br>"
             "A tarde fica para o que está em volta e não tem cobrança apurada aqui: o "
             "<b>Archivo de Indias</b>, do outro lado da praça, e a travessia do "
             "<b>Guadalquivir pela Puente de Isabel II</b> até <b>Triana</b>, no fim do "
             "dia. Não prometemos horário para esses três porque não os apuramos — "
             "prometemos a sequência, que é curta e toda a pé.",
             ["Real Alcázar · € 15,50 · abre 9h30, chegue cedo",
              "Cuarto Real Alto · € 5,50 · cobrado à parte da entrada geral",
              "Archivo de Indias · não apurado · do outro lado da praça",
              "Triana, pela Puente de Isabel II · grátis · fim de tarde"]),
            ("A Catedral e a Giralda — e o dia que você move se cair num domingo",
             "<b>Este é o dia que se mexe.</b> De segunda a sábado a <b>Catedral de "
             "Sevilha</b> abre às <b>10h45</b> e fecha às <b>19h</b>, com a bilheteira "
             "fechando às <b>18h</b>. <b>Aos domingos ela só abre às 14h30</b> — se o "
             "seu dia 3 cair num domingo, troque com o dia 1, que não tem hora "
             "nenhuma.<br>"
             "São <b>€ 13,00</b>, com a subida à <b>Giralda</b> incluída — e a subida é "
             "por rampas, não por escada, porque a torre foi feita para se subir a "
             "cavalo. A audioguia custa <b>€ 5,00</b> à parte, ou <b>€ 4,00</b> pelo "
             "aplicativo.<br>"
             "<b>Se for num domingo e quiser a entrada gratuita, leia o primeiro aviso "
             "desta página</b>: há duas versões oficiais do horário, e a diferença "
             "entre elas é de duas horas. Reserve pelo portal oficial e confirme na "
             "hora.",
             ["Catedral de Sevilha · € 13,00 · seg a sáb 10h45, domingo só 14h30",
              "Giralda · incluída · sobe por rampas, não por escadas",
              "Bilheteira fecha às 18h · uma hora antes da porta",
              "Gratuidade de domingo · duas versões oficiais · confira ao reservar"]),
        ],
        "fontes": (
            "Os horários e os preços vêm das páginas oficiais do Real Alcázar "
            "(alcazarsevilla.org), da Catedral de Sevilha (catedraldesevilla.es) e das "
            "Setas de Sevilla (setasdesevilla.com), todas consultadas em 25 de setembro "
            "de 2026 e registradas uma a uma no guia dos pontos. "
            "<b>Nenhum horário foi inventado para o roteiro fechar.</b> Barrio de Santa "
            "Cruz, Parque de María Luisa, Archivo de Indias e Triana entram sem preço e "
            "sem hora, porque esta apuração ainda não os cobriu — o roteiro promete a "
            "sequência, que é toda a pé, e não a hora. "
            "<b>E onde as fontes oficiais se contradizem, as duas versões estão "
            "escritas</b>: o horário da entrada gratuita de domingo na Catedral aparece "
            "como 16h30 numa página do site e como 14h30 em outra, do mesmo domínio."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
