# -*- coding: utf-8 -*-
"""Poe a foto de capa da cidade na primeira tela do guia.

Visual 2 do _build/docs/concorrentes-2026-10-17.md. Medido em 17/10/2026,
no guia de Lisboa a 375 px: a primeira imagem estava a 4.761 px do topo -
seis telas abaixo. O Dica de Portugal poe a foto acima da dobra, logo
depois do titulo. A primeira tela entregava menos do que a pagina tem.

A FOTO E A MESMA DO CARTAO DA HOME, lida de la pelo slug: nao se escolhe
imagem nova nem se baixa nada. O cartao ja tem srcset com as variantes de
400, 640 e 820 px que o imagens/srcset.py gerou, e o alt. Vem tudo junto.

O CREDITO vem do proprio guia: a mesma foto aparece num ponto, com a
<figure class="foto"> e o <p class="foto-cred">. O script acha pelo nome
do arquivo e copia o credito para a capa. Cinco cartoes usam uma foto
que so existe na home (a vista geral da cidade, que nao e ponto nenhum):
o credito dessas esta em RESERVA, copiado de onde foi registrado - os
CAPAS de novos2/cartoes.py e sevilha/cartao.py, e a mensagem do commit
908b4b6 para Cancun e Fortaleza, que nasceram sem gerador de cartao. Se
nao achar em lugar nenhum, a capa entra SEM credito e o script avisa -
porque imagem sem procedencia e o que este site nao publica, e e melhor
o aviso do que inventar.

Onde entra: logo depois do </div> que fecha o .hero, antes do .painel
(Lisboa, Rio, Santiago) ou do fim da faixa (cidades do novos/gera.py). O
hero em si - eyebrow, h1, abertura, assinatura - nao muda: o Allan ve a
faixa de foto primeiro; texto sobre foto, como o .hero-foto da home, e
decisao para depois, se ele quiser.

E POS-PROCESSADOR, como assinatura.py: tres familias de gerador. Aceita
slugs na linha de comando para ensaiar numa cidade so. Idempotente.

Uso
---
    python _build/layout/capa.py lisboa            # so mostra, so Lisboa
    python _build/layout/capa.py --aplica lisboa   # escreve, so Lisboa
    python _build/layout/capa.py --aplica          # escreve nos 20
"""
import glob
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

JA = re.compile(r'(?s)\n?<figure class="hero-capa">.*?</figure>\n?')

# Fotos que so a home usa: o credito nao esta em nenhum ponto do guia.
# Formato curto, o mesmo de 164 das 200 legendas dos guias (Maceio, por
# exemplo); "recortada" onde a licenca pede que o recorte seja dito.
RESERVA = {
    "llao-llao.webp": "Fernando · CC BY-SA 4.0 · via Wikimedia Commons",            # novos2/cartoes.py
    "praia.webp": "Flickr · CC BY 2.0 · via Wikimedia Commons",                    # novos2/cartoes.py
    "plaza-de-espana.webp": "Wzwz · domínio público · via Wikimedia Commons",      # sevilha/cartao.py
    "zona-hotelera.webp": "ProtoplasmaKid · CC BY-SA 4.0 · via Wikimedia Commons · recortada",  # commit 908b4b6
    "beira-mar.webp": "GLandovsky · CC BY-SA 4.0 · via Wikimedia Commons · recortada",          # commit 908b4b6
}


def le(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def escreve(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def capa_da_home(home, slug):
    """A tag <img> do cartao da cidade, com srcset/src/alt/width/height."""
    i = home.find('href="./destinos/%s/"' % slug)
    if i < 0:
        return None
    a = home.rfind("<article", 0, i)
    m = re.search(r"<img[^>]*>", home[a:i])
    return m.group(0) if m else None


def credito_do_guia(h, arquivo):
    """O <p class="foto-cred"> da <figure class="foto"> que usa o mesmo arquivo."""
    for m in re.finditer(r'(?s)<figure class="foto">(.*?)</figure>', h):
        if arquivo in m.group(1):
            c = re.search(r'<p class="foto-cred">(.*?)</p>', m.group(1), re.S)
            if c:
                return c.group(1).strip()
    return None


def main(aplica, so):
    home = le(os.path.join(RAIZ, "index.html"))
    posto = trocado = pulado = sem_cred = 0
    for p in sorted(glob.glob(os.path.join(RAIZ, "destinos", "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(p))
        if so and slug not in so:
            continue
        h = le(p)
        img = capa_da_home(home, slug)
        if not img:
            print("   PULADO %-16s sem cartao na home" % slug); pulado += 1; continue
        # os caminhos do cartao sao relativos a raiz (./assets/...); o guia esta dois niveis abaixo
        # cada caminho comeca depois de aspas, espaco ou virgula (src e os
        # itens do srcset); ancorar ali evita trocar dentro do que ja foi
        # trocado - "../../assets/img/" contem "./assets/img/"
        img = re.sub(r'(^|["\s,])\./assets/img/', r"\1../../assets/img/", img)
        img = re.sub(r'\s+loading="lazy"', "", img)
        if 'fetchpriority="high"' not in img:
            img = img.replace("<img ", '<img fetchpriority="high" ', 1)
        arquivo = re.search(r'src="[^"]*/([^"/]+\.webp)"', img).group(1)
        cred = credito_do_guia(h, arquivo) or RESERVA.get(arquivo)
        if not cred:
            sem_cred += 1
            print("   AVISO  %-16s capa %s sem credito no guia" % (slug, arquivo))
        fig = ('<figure class="hero-capa">\n  %s\n%s</figure>\n'
               % (img, ('  <figcaption><p class="foto-cred">%s</p></figcaption>\n' % cred) if cred else ""))
        if JA.search(h):
            h2 = JA.sub("\n" + fig, h, count=1); modo = "trocado"
        else:
            i = h.find('class="assinatura"')
            if i < 0:
                i = h.find("</h1>")
            j = h.find("</div>", i)
            if j < 0:
                print("   PULADO %-16s sem o fim do hero" % slug); pulado += 1; continue
            j += len("</div>")
            h2 = h[:j] + "\n" + fig + h[j:]; modo = "posto"
        if h2 != h:
            if modo == "posto": posto += 1
            else: trocado += 1
            if aplica:
                escreve(p, h2)
        print("   %-16s %-28s credito: %-4s %s" % (slug, arquivo, "sim" if cred else "NAO", modo if h2 != h else "igual"))
    print("   %d posta(s), %d trocada(s), %d pulada(s), %d sem credito   %s"
          % (posto, trocado, pulado, sem_cred, "escrito" if aplica else "SO MOSTRANDO"))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--aplica"]
    main("--aplica" in sys.argv, set(args))
