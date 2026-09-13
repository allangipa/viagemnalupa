// Ver na rua — abre o Street View do Google num modal, sob demanda.
// O iframe só é criado quando o visitante clica, e é destruído ao fechar:
// nada disso pesa no carregamento da página.
// A chave é restrita por referenciador a viagemnalupa.com.br — por isso pode ficar à vista.
(function () {
  "use strict";
  var CHAVE = "AIzaSyDnRhOBpKFfVI-w30KkdTsJvSdhUsZJgHA";
  var botoes = document.querySelectorAll("[data-sv]");
  if (!botoes.length) return;

  var modal, quadro, titulo, nota, fechar, fundo, ultimoBotao = null;

  function monta() {
    modal = document.createElement("div");
    modal.className = "sv-modal";
    modal.setAttribute("role", "dialog");
    modal.setAttribute("aria-modal", "true");
    modal.setAttribute("aria-labelledby", "sv-titulo");
    modal.hidden = true;
    modal.innerHTML =
      '<div class="sv-fundo" data-sv-fecha></div>' +
      '<div class="sv-cx">' +
        '<div class="sv-topo">' +
          '<div><h4 id="sv-titulo"></h4><p class="sv-nota"></p></div>' +
          '<button type="button" class="sv-fechar" aria-label="Fechar">' +
            '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true">' +
            '<path d="M5 5l14 14M19 5L5 19" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>' +
          '</button>' +
        '</div>' +
        '<div class="sv-quadro"><div class="sv-carregando">CARREGANDO</div></div>' +
        '<p class="sv-rodape"></p>' +
      '</div>';
    document.body.appendChild(modal);
    quadro = modal.querySelector(".sv-quadro");
    titulo = modal.querySelector("#sv-titulo");
    nota   = modal.querySelector(".sv-nota");
    fechar = modal.querySelector(".sv-fechar");
    fundo  = modal.querySelector("[data-sv-fecha]");
    fechar.addEventListener("click", esconde);
    fundo.addEventListener("click", esconde);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !modal.hidden) esconde();
    });
  }

  function abre(b) {
    if (!modal) monta();
    ultimoBotao = b;
    var pano = b.getAttribute("data-sv-pano");
    var loc  = b.getAttribute("data-sv-loc");
    var head = b.getAttribute("data-sv-head") || "0";
    var pitch = b.getAttribute("data-sv-pitch") || "0";
    var fov  = b.getAttribute("data-sv-fov") || "90";

    titulo.textContent = b.getAttribute("data-sv-titulo") || "Ver na rua";
    nota.textContent = b.getAttribute("data-sv-nota") || "";
    nota.hidden = !nota.textContent;

    var src = "https://www.google.com/maps/embed/v1/streetview?key=" + CHAVE +
      (pano ? "&pano=" + encodeURIComponent(pano)
            : "&location=" + encodeURIComponent(loc)) +
      "&heading=" + head + "&pitch=" + pitch + "&fov=" + fov;

    quadro.innerHTML = '<div class="sv-carregando">CARREGANDO</div>';
    var f = document.createElement("iframe");
    f.src = src;
    f.loading = "lazy";
    f.allowFullscreen = true;
    f.referrerPolicy = "strict-origin-when-cross-origin";
    f.title = titulo.textContent;
    quadro.appendChild(f);

    // Link para abrir no Google Maps, fora do site
    var externo = pano
      ? "https://www.google.com/maps/@?api=1&map_action=pano&pano=" + encodeURIComponent(pano)
      : "https://www.google.com/maps/@?api=1&map_action=pano&viewpoint=" + encodeURIComponent(loc) +
        "&heading=" + head;
    modal.querySelector(".sv-rodape").innerHTML =
      'Imagem do Google Street View. A data da captura aparece no canto da imagem — ' +
      'panorama antigo pode não refletir obras ou mudanças recentes. ' +
      '<a href="' + externo + '" target="_blank" rel="noopener">Abrir no Google Maps</a>.';

    modal.hidden = false;
    document.body.style.overflow = "hidden";
    fechar.focus();
  }

  function esconde() {
    if (!modal || modal.hidden) return;
    modal.hidden = true;
    quadro.innerHTML = "";              // destrói o iframe
    document.body.style.overflow = "";
    if (ultimoBotao) ultimoBotao.focus();
  }

  Array.prototype.forEach.call(botoes, function (b) {
    b.addEventListener("click", function () { abre(b); });
  });
})();
