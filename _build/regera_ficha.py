# -*- coding: utf-8 -*-
"""Regera a ficha de custos de uma cidade sem perder o bloco do voo, e roda
a cadeia inteira do LEIA-ME ate o confere.

O bloco <!-- voo:inicio --> ... <!-- voo:fim --> e escrito pela Action de
passagens (voos.yml), que tem o token; nesta maquina nao da para refaze-lo.
Este script guarda o bloco que esta no ar antes de regerar e o devolve
depois - inclusive trocando o bloco provisorio ("Ainda nao coletado") que
alguns geradores escrevem sozinhos. Sem essa troca, o espalha.py nao acha o
link da Aviasales na ficha e o voo some tambem do guia e do roteiro.

Uso
---
    python _build/regera_ficha.py <slug> <gerador.py> [args extras do gerador]

    python _build/regera_ficha.py barcelona _build/barcelona/gera_custos.py
    python _build/regera_ficha.py cancun _build/novos/gera_custos.py --so cancun
    python _build/regera_ficha.py bariloche _build/novos2/gera_custos.py --so bariloche

Grava direto (cada passo roda com --aplica). Para em qualquer rc != 0.
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
slug, gerador, extra = sys.argv[1], sys.argv[2], sys.argv[3:]
ficha = os.path.join(RAIZ, "destinos", slug, "quanto-custa", "index.html")
antes = io.open(ficha, encoding="utf-8").read()
voo = re.search(r"<!-- voo:inicio -->.*?<!-- voo:fim -->", antes, re.S)


def roda(*args):
    r = subprocess.run([sys.executable, "-X", "utf8"] + list(args), cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8")
    saida = (r.stdout + r.stderr).strip().splitlines()
    ruim = [l for l in saida if re.search(r"Traceback|PARADO|Error|erro|SEM ficha|nao achei", l, re.I)]
    print("  %-42s rc=%d %s" % (" ".join(args)[:42], r.returncode,
                                ("| " + " / ".join(ruim[:3])) if ruim else ""))
    if r.returncode != 0:
        print("\n".join(saida[-15:]))
        sys.exit("PAROU em " + " ".join(args))


roda(gerador, "--aplica", *extra)
if voo:
    h = io.open(ficha, encoding="utf-8").read()
    # o gerador pode por um bloco provisorio ("Ainda nao coletado"); troca
    # pelo que estava no ar, que veio da Action
    novo = re.search(r"<!-- voo:inicio -->.*?<!-- voo:fim -->", h, re.S)
    if novo:
        h = h[:novo.start()] + voo.group(0) + h[novo.end():]
    else:
        m = re.search(r'<section class="bloco">\s*<div class="reserva">', h)
        h = h[:m.start()] + voo.group(0) + "\n\n" + h[m.start():]
    io.open(ficha, "w", encoding="utf-8", newline="").write(h)
    print("  bloco do voo reposto")

for s in ["layout/reorganiza.py --todos", "layout/atalhos.py", "layout/vizinhos.py", "layout/sem_moldura.py",
          "layout/assinatura.py", "layout/faq.py", "layout/tamanhos.py", "layout/capa.py", "recortes/gratis.py",
          "parceiros/booking.py", "parceiros/espalha.py", "parceiros/aside.py",
          "nova-york/sv.py", "porto/sv.py", "granada/sv.py",
          "sitemap/atualiza.py", "schema/gera.py", "schema/editor.py", "schema/ofertas.py", "imagens/srcset.py",
          "layout/fontes.py", "adsense/instala.py", "drive/instala.py"]:
    partes = s.split()
    roda(os.path.join("_build", partes[0]), *partes[1:], "--aplica")
calc = io.open(os.path.join(RAIZ, "calculadora", "index.html"), encoding="utf-8").read()
if 'data-cidade="%s"' % slug in calc:
    roda(os.path.join("_build", "calculadora", "sincroniza.py"), "--refaz", slug, "--aplica")
else:
    roda(os.path.join("_build", "calculadora", "sincroniza.py"), "--aplica")
roda(os.path.join("_build", "recortes", "comparar.py"), "--aplica")
roda(os.path.join("_build", "cluster", "home.py"), "--aplica")
r = subprocess.run([sys.executable, "-X", "utf8", os.path.join("_build", "confere", "tudo.py")], cwd=RAIZ,
                   capture_output=True, text=True, encoding="utf-8")
fim = r.stdout.strip().splitlines()
i = next((k for k, l in enumerate(fim) if l.startswith("!!!") or l.startswith("Nada divergente")), len(fim) - 1)
print("\n".join(fim[i:]))
