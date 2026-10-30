# -*- coding: utf-8 -*-
"""Roteiro de 4 dias em Cusco e Machu Picchu, montado pelo bilhete.

Mesmo molde do bonito/gera_roteiro.py.

O QUE DECIDE A ORDEM
--------------------
    bilhete   hora exata de entrada, 4 a 6 horas no sitio; a venda
              presencial em Aguas Calientes (15h-22h) vale para o dia
              seguinte - por isso o roteiro dorme em Aguas Calientes
    fevereiro o Caminho Inca nao tem percursos (manutencao)
    alta      19/6 a 2/11: 5.600 por dia e as rotas 1-C, 1-D, 3-C, 3-D

POR QUE ESTA ORDEM
------------------
    dia 1  Cusco: chegada e o Boleto Turistico
    dia 2  trem para Aguas Calientes; quem nao comprou online tenta o
           bilhete presencial das 15h as 22h, para o dia seguinte
    dia 3  Machu Picchu na hora marcada, onibus, trem de volta
    dia 4  Cusco e a volta

Uso
---
    python _build/machu-picchu/gera_roteiro.py
    python _build/machu-picchu/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_machu_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

SEC = '<span class="flag">Só em fonte secundária</span> '

ROTEIROS = {
    "machu-picchu": {
        "dias": 4,
        "titulo": "Roteiro de 4 dias em Cusco e Machu Picchu",
        "descricao": ("Quatro dias em Cusco e Machu Picchu na ordem que o bilhete permite: "
                      "hora de entrada marcada, a noite em Aguas Calientes e a venda "
                      "presencial que vale só para o dia seguinte."),
        "abertura": ("Quatro dias, com uma noite em Aguas Calientes, porque <b>o bilhete de "
                     "Machu Picchu tem hora exata de entrada</b> e a venda presencial na "
                     "cidade, das 15h às 22h, vale só para o dia seguinte. <b>E uma conta que "
                     "depende do passaporte:</b> o brasileiro paga S/ 152 pelo mesmo bilhete "
                     "que custa S/ 64 ao peruano — e, desde maio, mais S/ 11 de taxa "
                     "ambiental."),
        "avisos": [
            ("a", "O brasileiro paga a tarifa de estrangeiro — 2,4 vezes a do peruano",
             "<p>A tarifa promocional de 2026, <b>S/ 64</b>, vale para peruanos, "
             "residentes e cidadãos da <b>Comunidade Andina</b> — Bolívia, Colômbia, "
             "Equador e Peru. O Brasil não é membro.</p>"
             "<p>O brasileiro paga <b>S/ 152</b>, segundo a imprensa peruana, e desde 1º de "
             "maio mais <b>S/ 11</b> da taxa do SERNANP. Em real, pela taxa do Banco "
             "Central de 23 de outubro: R$ 222,12 e R$ 16,07.</p>"),
            ("b", "O bilhete tem hora marcada — compre antes de comprar o trem",
             "<p>A venda oficial é só pelo <b>tuboleto.cultura.pe</b>. Cada bilhete tem "
             "<b>hora exata de entrada</b> e dá de 4 a 6 horas no sítio.</p>"
             "<p>Na temporada alta de 2026 — <b>19 de junho a 2 de novembro</b> — entram até "
             "5.600 pessoas por dia; no resto do ano, 4.500.</p>"
             "<p><b>Sem bilhete online?</b> O Centro Cultural de Machu Picchu Pueblo vende "
             "mil por dia, das 15h às 22h, <b>para o dia seguinte</b>. Por isso o roteiro "
             "dorme em Aguas Calientes.</p>"),
            ("a", "A taxa do SERNANP foi adiada quatro vezes antes de valer",
             "<p>A resolução publicada no El Peruano em fevereiro de 2026 lista as datas de "
             "início anteriores: <b>janeiro de 2024, janeiro de 2025, janeiro e fevereiro "
             "de 2026</b>. A cobrança começou em <b>1º de maio de 2026</b>.</p>"
             "<p>Quem chega pelo Caminho Inca não paga — e o Caminho fica <b>fechado em "
             "fevereiro</b>, para manutenção.</p>"),
            ("b", "O que este roteiro não alcança, e está dito",
             "<p><b>A hospedagem</b>, sem diária oficial.</p>"
             "<p><b>O trem</b>, de empresas privadas, com preço por data.</p>"
             "<p><b>O ônibus até as ruínas e o Boleto Turístico de Cusco</b>, cujos sites "
             "não abriram — os valores dos guias estão marcados.</p>"
             "<p><b>A tabela oficial do Ministério da Cultura</b>, que fica atrás de uma "
             "verificação “não sou um robô”.</p>"),
        ],
        "dias_lista": [
            ("Dia 1 — Cusco e o Boleto Turístico",
             "Chegada a Cusco. Os sítios arqueológicos da cidade e do Vale Sagrado entram "
             "no <b>Boleto Turístico</b>, que <b>não inclui Machu Picchu</b>. " + SEC +
             "o site do comitê que o vende estava fora do ar; guias citam S/ 130 o "
             "integral, de 10 dias.",
             ["Boleto Turístico · guias S/ 130",
              "Não inclui Machu Picchu",
              "Bilhete de Machu Picchu · já comprado?"]),

            ("Dia 2 — o trem para Aguas Calientes",
             "<b>Trem até Aguas Calientes</b> (Machu Picchu Pueblo): Machu Picchu fica a "
             "210 km de Cusco, diz a página oficial. O trem é de empresa privada, com "
             "preço por data. <b>Quem não comprou o bilhete online</b> tenta a venda "
             "presencial no Centro Cultural, das 15h às 22h — vale para amanhã.",
             ["Trem · preço por data",
              "Venda presencial · 15h–22h",
              "Vale para o dia seguinte"]),

            ("Dia 3 — Machu Picchu na hora marcada",
             "<b>Na hora exata do bilhete</b>: S/ 152 para o brasileiro, mais S/ 11 do "
             "SERNANP. O sítio fica a 2.430 m, e o horário de atenção é das 8h às 16h15. "
             "São de 4 a 6 horas lá dentro, conforme o circuito. A montanha (Huayna Picchu "
             "ou Montanha Machu Picchu) é outra rota, mais cara. " + SEC + "o ônibus "
             "até a entrada sai por US$ 24 ida e volta, segundo os guias — o site da "
             "Consettur não abriu. À tarde, trem de volta.",
             ["Bilhete · S/ 152 · hora marcada",
              "SERNANP · S/ 11",
              "4 a 6 horas no sítio",
              "Ônibus · guias US$ 24"]),

            ("Dia 4 — Cusco e a volta",
             "Último dia em Cusco, com o que sobrou do Boleto Turístico, que vale 10 dias, "
             "e a volta.",
             ["Boleto Turístico · 10 dias",
              "Volta"]),
        ],
        "fontes": ("Os preços deste roteiro são os mesmos da ficha de custos, conferidos em "
                   "29 de outubro de 2026. <b>O bilhete e a taxa do SERNANP</b> vêm da "
                   "imprensa peruana, que reproduz a tarifa oficial; a data da taxa, da "
                   "resolução no El Peruano; a tarifa de peruanos e andinos, da Andina. "
                   "<b>Ficaram sem fonte oficial</b> o trem, o ônibus, o Boleto Turístico e "
                   "a hospedagem."),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
