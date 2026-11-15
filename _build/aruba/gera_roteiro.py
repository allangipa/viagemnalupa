# -*- coding: utf-8 -*-
"""Roteiro de 5 dias em Aruba, montado pela geografia e pelo que se paga antes.

Mesmo molde do florianopolis/gera_roteiro.py.

O QUE DECIDE ESTE ROTEIRO
-------------------------
    antes do voo  o ED card e a taxa de US$ 20, so no cartao, antes do
                  check-in
    o Arikok      a Natural Pool so de 4x4: o dia do parque e de tour ou de
                  carro 4x4, nao de carro comum
    a distancia   a Baby Beach fica a ~45 min de Palm Beach, no lado oposto
    o noroeste    a Butterfly Farm deixa voltar; o farol abre ate as 19h

Uso
---
    python _build/aruba/gera_roteiro.py
    python _build/aruba/gera_roteiro.py --aplica
"""
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "_build", "novos"))

import gera_roteiro as base  # noqa: E402

_s = importlib.util.spec_from_file_location(
    "dados_aruba_roteiro", os.path.join(AQUI, "dados.py"))
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
base.DESTINOS = _d.DESTINOS
base.APURACAO = _d.APURACAO

ROTEIROS = {
    "aruba": {
        "dias": 5,
        "titulo": "Roteiro de 5 dias em Aruba",
        "descricao": ("Cinco dias em Aruba na ordem que a ilha pede: a taxa paga antes do voo, "
                      "o Arikok de 4x4, a costa norte, o noroeste do farol e a Baby Beach no "
                      "extremo sul."),
        "abertura": ("Cinco dias montados por três coisas que os guias não juntam: <b>a taxa "
                     "de US$ 20 se paga antes do voo</b>, no próprio formulário de entrada; "
                     "<b>a piscina natural do Arikok só se alcança de 4x4</b>; e <b>a Baby "
                     "Beach fica a cerca de 45 minutos dos hotéis</b>, no lado oposto da "
                     "ilha."),
        "avisos": [
            ("a", "Antes do voo: o ED card e a taxa de US$ 20",
             "<p>O formulário de entrada é <b>obrigatório até para bebê</b> e se preenche "
             "entre 7 dias e 4 horas antes do voo, no portal oficial (edcardaruba.aw).</p>"
             "<p>Dentro dele vem a <b>Sustainability Fee de US$ 20 por pessoa</b>, desde "
             "1º/jul/2024: <b>só no cartão de crédito, antes do check-in</b>. Menor de 8 anos "
             "não paga.</p>"
             "<p>A autoridade de turismo avisa: <i>“No pagues más de $20 dólares de tasa de "
             "sostenibilidad.”</i> Site que cobra para “ajudar” com o formulário não é "
             "oficial.</p>"),
            ("b", "A diária não é o que você paga",
             "<p>Por cima da diária vêm <b>12,5% de imposto de hospedagem</b> e <b>US$ 3 por "
             "noite por quarto</b> de taxa ambiental. A diária média dos hotéis em 2025 foi "
             "<b>US$ 408,99</b> (Banco Central de Aruba), 12,3% acima de 2024.</p>"
             "<p>No all-inclusive, o imposto incide sobre metade do pacote.</p>"),
            ("a", "A praia é pública; a cadeira do hotel, não",
             "<p>O governo: <i>“All beaches remain public and accessible.”</i> Mas a diretriz "
             "de 2026 diz que palapa e espreguiçadeira montadas pelo hotel <i>“are considered "
             "in use, even if the guest steps away”</i>. Leve a sua toalha.</p>"
             "<p><b>A praia dos flamingos, na Renaissance Island, é só para hóspedes</b> do "
             "resort, pela autoridade de turismo.</p>"),
            ("b", "Carro comum não chega à piscina natural",
             "<p><i>“Accessible only by 4x4 vehicle.”</i> É regra do Parque Nacional Arikok, "
             "não conselho. ATV, UTV e moto são proibidos nas áreas protegidas.</p>"),
            ("a", "O que este roteiro não alcança, e está dito",
             "<p><b>O preço e o horário do museu do Forte Zoutman</b>, que a página atual não "
             "publica.</p>"
             "<p><b>O day pass da Renaissance Island</b>, sem preço em fonte oficial.</p>"
             "<p><b>A cobrança na costa norte</b> — Bushiribana e a Baby Bridge —, que as "
             "páginas oficiais não citam.</p>"
             "<p><b>O número de dias de permanência</b>, que a imigração define na "
             "chegada.</p>"),
        ],
        "dias_lista": [
            ("A chegada e a Eagle Beach",
             "Do aeroporto, o <b>ônibus da Linha 2</b> custa US$ 2,60 e aceita dinheiro; o "
             "<b>táxi</b>, pela tabela do governo, sai a <b>US$ 37 até Eagle Beach</b> e "
             "US$ 40 a 41 até os hotéis altos de Palm Beach, por carro. À tarde, a <b>Eagle "
             "Beach</b>, pública, com as árvores fofoti — e com os ninhos de tartaruga da "
             "ilha.",
             ["ED card e taxa · pagos antes do voo",
              "Ônibus Linha 2 · US$ 2,60",
              "Táxi até Eagle Beach · US$ 37",
              "Eagle Beach · pública",
              "Cadeira do hotel · do hotel"]),

            ("O Arikok e a piscina natural",
             "O dia do <b>Parque Nacional Arikok</b>: <b>US$ 22 por adulto</b>, e <b>menor de "
             "17 não paga</b>. O centro de visitantes de San Fuego abre às 8h. A <b>Natural "
             "Pool</b> está no mesmo passe, mas <b>só de 4x4</b> — tour, carro 4x4 ou a "
             "trilha de três a quatro horas, ida e volta. Nade só com o mar calmo, e siga os "
             "guardas.",
             ["Arikok · US$ 22 · menor de 17 grátis",
              "Natural Pool · só de 4x4",
              "Trilha a pé · 3 a 4 horas",
              "Mar calmo para nadar",
              "ATV e moto · proibidos"]),

            ("A costa norte e o Donkey Sanctuary",
             "O lado selvagem da ilha, oposto aos hotéis: as ruínas de <b>Bushiribana</b>, da "
             "corrida do ouro de 1824, e a <b>Baby Bridge</b> — <b>a Natural Bridge das fotos "
             "caiu em 2005</b>. As páginas oficiais não citam cobrança nem horário. À tarde, o "
             "<b>Donkey Sanctuary</b>, que não cobra entrada, aceita doação e abre das 9h às "
             "16h; as coordenadas do site têm erro, então use o nome no mapa.",
             ["Bushiribana · cobrança não publicada",
              "Natural Bridge · caiu em 2005",
              "Baby Bridge · a que está de pé",
              "Donkey Sanctuary · doação · 9h–16h",
              "Use o nome no mapa, não o GPS do site"]),

            ("O noroeste: borboletas, Palm Beach e o farol",
             "Cedo, a <b>Butterfly Farm</b>, US$ 19 o adulto — <b>e o ingresso deixa voltar "
             "durante a viagem</b>, por até um mês. O dia é de <b>Palm Beach</b>, pública, e "
             "o fim da tarde, do <b>California Lighthouse</b>: <b>US$ 5 para subir</b>, sem "
             "reserva, aberto até as 19h — a hora do pôr do sol no extremo noroeste.",
             ["Butterfly Farm · US$ 19 · volta grátis",
              "Palm Beach · pública",
              "Farol · US$ 5 · até 19h",
              "Sem reserva no farol",
              "Ônibus · passe do dia US$ 15"]),

            ("Oranjestad e a Baby Beach",
             "De manhã, <b>Oranjestad</b>: o Forte Zoutman, o prédio mais antigo da capital, "
             "e o bonde da Main Street, que a autoridade de turismo mostra “From $0”. Depois, "
             "a <b>Baby Beach</b>, no extremo sul, a cerca de 45 minutos dos hotéis: água "
             "rasa, <b>cabanas de sombra grátis</b>, e snorkel só dentro da área marcada.",
             ["Forte Zoutman · preço não publicado",
              "Bonde do centro · “From $0”",
              "Baby Beach · cabanas grátis",
              "45 minutos de Palm Beach",
              "Snorkel · só na área marcada"]),
        ],
        "fontes": ("Os preços e horários deste roteiro são os mesmos da ficha de custos, "
                   "apurados em 15 de novembro de 2026: a taxa de entrada, as praias, o "
                   "farol e o táxi na Aruba Tourism Authority (aruba.com); o parque na Aruba "
                   "Conservation Foundation; o ônibus no Arubus; os impostos na lei de "
                   "hospedagem e no departamento de impostos; a diária no Banco Central de "
                   "Aruba. <b>Nenhum valor veio de agregador de viagem.</b>"),
    },
}

base.ROTEIROS = ROTEIROS

if __name__ == "__main__":
    base.main("--aplica" in sys.argv)
