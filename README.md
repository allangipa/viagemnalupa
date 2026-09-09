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
assets/css/site.css                         sistema visual
assets/js/destinos.js                       busca e filtro
robots.txt · sitemap.xml · 404.html · .htaccess
```

## Ao adicionar um destino

1. Criar a pasta `destinos/<slug>/` com as três páginas.
2. Acrescentar o destino no array `DESTINOS` de `assets/js/destinos.js`.
3. Acrescentar as URLs no `sitemap.xml` com o `lastmod` do dia.

## Regra editorial

Todo número tem fonte e data. Toda lacuna está escrita. Estimativa é rotulada como estimativa.
