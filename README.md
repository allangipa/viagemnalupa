# viagemnalupa.com.br

Site estático. HTML, CSS e JavaScript puros — **sem build, sem framework, sem dependência**.

## Publicar na Hostinger

1. hPanel → **Sites** → seu site → **Avançado** → **Git**
2. Conectar via **GitHub auto-deployments** (instala o Hostinger GitHub App)
3. Repositório: este · Branch: `main` · Diretório: `public_html` (padrão)
4. Cada `git push` na `main` publica sozinho.

Não é preciso comando de build. A raiz do repositório vira a raiz do site.

## Estrutura

```
index.html                                  home, com busca de destinos
destinos/index.html                         índice completo
destinos/nova-york/index.html               guia dos 17 pontos
destinos/nova-york/quanto-custa/index.html  ficha de custos
destinos/nova-york/roteiro-7-dias/index.html
sobre/index.html
contato/index.html
privacidade/index.html
assets/css/site.css                         sistema visual
assets/js/destinos.js                       busca e filtro
assets/js/consentimento.js                  faixa de cookies + carregador do AdSense
robots.txt · sitemap.xml · ads.txt · 404.html · .htaccess
```

## Ao adicionar um destino

1. Criar a pasta `destinos/<slug>/` com as três páginas.
2. Acrescentar o destino no array `DESTINOS` de `assets/js/destinos.js`.
3. Acrescentar as URLs no `sitemap.xml` com o `lastmod` do dia.

## Regra editorial

Todo número tem fonte e data. Toda lacuna está escrita. Estimativa é rotulada como estimativa.

## AdSense

Publisher `ca-pub-4401770243539507` (o mesmo dos outros sites). Instalado em 2/out/2026.

- `ads.txt` na raiz, com a linha do publisher.
- Em **todas** as páginas, entre marcadores, `_build/adsense/instala.py` põe a meta
  `google-adsense-account` + preconnect no `<head>` (`<!-- adsense:inicio/fim -->`) e a tag
  de `assets/js/consentimento.js` antes do `</body>` (`<!-- consentimento:inicio/fim -->`).
- O script do AdSense **não** está no HTML: o `consentimento.js` injeta. Sem escolha gravada,
  carrega e mostra a faixa; "Recusar anúncios" remove e não carrega mais. Escolha em
  `localStorage`, chave `vl-consentimento`. Se a mensagem GDPR do Google (`__tcfapi`) disser
  que o GDPR se aplica, a faixa some.
- Os geradores de `_build/` não sabem do AdSense: **depois de regerar página, rode
  `python _build/adsense/instala.py --aplica`**. O `_build/confere/tudo.py` reclama de página sem os blocos.
- **Desligar:** `python _build/adsense/desinstala.py --aplica` (tira os blocos de todas as páginas)
  e atualizar `/privacidade/`. Para só parar de carregar anúncio, `PUB = ''` no `consentimento.js`
  e `python _build/cachebust/atualiza.py --aplica`.
- Mudou o `consentimento.js`? Rode o cachebust: o `?v=` é o hash dele.
