/* Faixa de consentimento e carregador do Google AdSense.
 *
 * Instalado em 2/out/2026 por _build/adsense/instala.py, que poe em todas
 * as paginas a meta de verificacao no <head> e a tag deste arquivo antes
 * do </body>. Para desligar o AdSense: python _build/adsense/desinstala.py
 * --aplica (tira os dois blocos); para so parar de carregar anuncio sem
 * mexer nas paginas, ponha PUB = '' abaixo e rode o cachebust.
 *
 * Comportamento (o mesmo dos sites Vestigio, Arquitetura e Xadrez):
 * - o script do AdSense NAO esta escrito no HTML; entra por aqui;
 * - sem escolha gravada, carrega de imediato (BLOQUEIA = false) e mostra
 *   a faixa; "Entendi" grava e mantem; "Recusar anuncios" grava, remove o
 *   script e nas proximas visitas ele nao carrega;
 * - a escolha fica em localStorage, chave vl-consentimento;
 * - Europa, Reino Unido e Suica: se a mensagem GDPR do Google (CMP
 *   certificada) aparecer e disser que o GDPR se aplica, esta faixa sai da
 *   frente e quem pergunta e o Google.
 */
(function () {
  var CHAVE = 'vl-consentimento', PUB = 'pub-4401770243539507', BLOQUEIA = false;

  function ler() { try { return localStorage.getItem(CHAVE); } catch (e) { return null; } }
  function gravar(v) { try { localStorage.setItem(CHAVE, v); } catch (e) {} }
  function carrega() {
    if (!PUB || document.getElementById('ads-google')) return;
    var s = document.createElement('script');
    s.id = 'ads-google'; s.async = true; s.crossOrigin = 'anonymous';
    s.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-' + PUB;
    document.head.appendChild(s);
  }

  var escolha = ler();
  if (escolha === 'aceitar' || (escolha === null && !BLOQUEIA)) carrega();
  if (escolha !== null) return;

  var css =
    '.consentimento{position:fixed;left:0;right:0;bottom:0;z-index:60;' +
      'background:var(--noite,#122334);color:var(--gelo,#E9EFED);' +
      'border-top:1px solid var(--rule,#23405C);box-shadow:0 -12px 30px -18px rgba(0,0,0,.7)}' +
    '.consentimento[hidden]{display:none}' +
    '.consentimento .c-in{max-width:72rem;margin:0 auto;padding:.85rem 16px;' +
      'display:flex;align-items:center;gap:.6rem 1.4rem;flex-wrap:wrap}' +
    '.consentimento p{flex:1 1 26rem;margin:0;font-size:.86rem;line-height:1.5;color:var(--nevoa,#94A8B6)}' +
    '.consentimento p a{color:var(--gelo,#E9EFED);text-decoration:underline}' +
    '.consentimento .c-bt{display:flex;gap:.6rem;flex-wrap:wrap}' +
    '.consentimento button{font-family:"Archivo",sans-serif;font-size:.86rem;font-weight:600;' +
      'min-height:44px;padding:.55rem 1.1rem;border-radius:var(--raio-s,9px);cursor:pointer;' +
      'background:transparent;color:var(--gelo,#E9EFED);border:1px solid var(--rule,#23405C)}' +
    '.consentimento button:hover{border-color:var(--ambar,#FFB703);color:var(--ambar,#FFB703)}' +
    '.consentimento button.principal{background:var(--ambar,#FFB703);color:var(--tinta,#0B1622);border-color:var(--ambar,#FFB703)}' +
    '.consentimento button.principal:hover{background:transparent;color:var(--ambar,#FFB703)}' +
    '.consentimento button:focus-visible{outline:2px solid var(--ciano,#43D3C2);outline-offset:2px}' +
    '@media (max-width:44rem){.consentimento .c-in{padding:.7rem 16px}' +
      '.consentimento p{font-size:.8rem;flex-basis:100%}' +
      '.consentimento .c-bt{width:100%}.consentimento button{flex:1 1 0}}';

  function monta() {
    var st = document.createElement('style');
    st.textContent = css;
    document.head.appendChild(st);

    var caixa = document.createElement('div');
    caixa.className = 'consentimento';
    caixa.id = 'consentimento';
    caixa.setAttribute('role', 'dialog');
    caixa.setAttribute('aria-live', 'polite');
    caixa.setAttribute('aria-label', 'Aviso de cookies');
    caixa.innerHTML =
      '<div class="c-in">' +
      '<p>Este site usa cookies do Google AdSense para exibir anúncios e medir audiência. ' +
      'Não pedimos cadastro nem e-mail. Detalhes na <a href="/privacidade/">política de privacidade</a>.</p>' +
      '<div class="c-bt">' +
      '<button type="button" data-consent="recusar">Recusar anúncios</button>' +
      '<button type="button" data-consent="aceitar" class="principal">Entendi</button>' +
      '</div></div>';
    document.body.appendChild(caixa);

    // a faixa nao pode cobrir o fim da pagina: o rodape ganha folga do
    // tamanho dela enquanto ela estiver na tela
    var folga = function () {
      document.body.style.paddingBottom = caixa.hidden ? '' : caixa.offsetHeight + 'px';
    };
    var fecha = function () { caixa.hidden = true; folga(); };
    folga();
    window.addEventListener('resize', folga);

    caixa.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-consent]');
      if (!b) return;
      var v = b.getAttribute('data-consent');
      gravar(v);
      fecha();
      if (v === 'aceitar') carrega();
      else { var x = document.getElementById('ads-google'); if (x) x.remove(); }
    });

    // Europa, Reino Unido, Suica: quem pergunta e a mensagem do Google (a
    // plataforma certificada que o AdSense exige la). Se ela diz que o GDPR
    // se aplica, esta faixa sai da frente. Sem a mensagem publicada, nao
    // dispara.
    var n = 0, t = setInterval(function () {
      if (typeof window.__tcfapi === 'function') {
        clearInterval(t);
        window.__tcfapi('addEventListener', 2, function (tc, ok) {
          if (ok && tc && tc.gdprApplies) fecha();
        });
      } else if (++n > 40) clearInterval(t);
    }, 250);
  }

  if (document.body) monta();
  else document.addEventListener('DOMContentLoaded', monta);
})();
