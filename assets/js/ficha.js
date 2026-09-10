/* Ficha de custos interativa — a mesma para todos os destinos.
   Toda a configuração vem do JSON #calc-cfg que a página traz, e todos os
   valores unitários vêm dos atributos data- da própria tabela apurada.
   Este arquivo não guarda preço nenhum: ele só faz aritmética.

   Sem JavaScript a página continua correta e indexável — a tabela é a ficha
   apurada, e os controles ficam escondidos até o script assumir. */
(function () {
  [].slice.call(document.querySelectorAll(".ficha-calc")).forEach(iniciar);
  abasDaPagina();

  /* Troca de cidade sem recarregar, quando a página tem mais de uma ficha
     (é o caso de /calculadora/). Nas páginas de destino não existe nada
     disso: lá cada ficha mora na sua própria página. */
  function abasDaPagina() {
    var botoes = [].slice.call(document.querySelectorAll("[data-troca]"));
    if (!botoes.length) return;
    var fichas = [].slice.call(document.querySelectorAll(".ficha-calc"));
    function mostrar(slug, empurraURL) {
      fichas.forEach(function (f) { f.hidden = f.dataset.cidade !== slug; });
      botoes.forEach(function (b) {
        var on = b.dataset.troca === slug;
        b.classList.toggle("atual", on);
        b.setAttribute("aria-current", on ? "true" : "false");
      });
      if (empurraURL) history.replaceState(null, "", "#" + slug);
    }
    botoes.forEach(function (b) {
      b.addEventListener("click", function (e) { e.preventDefault(); mostrar(b.dataset.troca, true); });
    });
    function doHash() {
      var h = location.hash.replace("#", "");
      mostrar(fichas.some(function (f) { return f.dataset.cidade === h; })
              ? h : fichas[0].dataset.cidade, false);
    }
    // link compartilhado, botão voltar, ou hash digitado na barra
    addEventListener("hashchange", doHash);
    doHash();
  }

  function iniciar(raiz) {
  var tab = raiz.querySelector(".tab-ficha");
  var calc = raiz.querySelector(".calc");
  var raw = raiz.querySelector(".calc-cfg");
  if (!tab || !calc || !raw) return;

  var CFG;
  try { CFG = JSON.parse(raw.textContent); } catch (e) { return; }
  var HOSP = {};
  CFG.hosp.forEach(function (h) { HOSP[h.k] = h; });

  var DIA = 86400000;
  var dec = CFG.dec == null ? 2 : CFG.dec;

  function moeda(n, casas) {
    var c = casas == null ? dec : casas;
    return CFG.moeda + " " + n.toLocaleString("pt-BR",
      { minimumFractionDigits: c, maximumFractionDigits: c });
  }
  function m0(n) { return CFG.moeda + " " + Math.round(n).toLocaleString("pt-BR"); }
  function num0(n) { return Math.round(n).toLocaleString("pt-BR"); }
  function plural(n, um, muitos) { return n + " " + (n === 1 ? um : muitos); }
  function dt(s) { return s ? new Date(s + "T12:00:00") : null; }
  function cruza(a, b, x, y) { return a <= dt(y) && b >= dt(x); }
  function brdata(d) {
    return d.toLocaleDateString("pt-BR", { day: "numeric", month: "long", year: "numeric" });
  }

  var linhas = [].slice.call(tab.querySelectorAll("tbody tr[data-tipo]"));
  var ingressos = linhas.filter(function (t) { return t.dataset.tipo === "ingresso"; });
  var lHosp = tab.querySelector('tr[data-tipo="hosp"]');
  var lMetro = tab.querySelector('tr[data-tipo="metro"]');

  /* Caixas de seleção injetadas aqui, e não no HTML: sem JS elas não
     funcionariam, e caixa que não funciona é pior que nenhuma. */
  ingressos.forEach(function (tr) {
    var td = tr.cells[0], nome = td.textContent.trim();
    var lab = document.createElement("label");
    var cb = document.createElement("input");
    lab.className = "cx";
    cb.type = "checkbox";
    cb.checked = true;
    cb.addEventListener("change", render);
    lab.appendChild(cb);
    lab.appendChild(document.createTextNode(nome));
    td.textContent = "";
    td.appendChild(lab);
  });

  var cIda = raiz.querySelector(".c-ida");
  var cVolta = raiz.querySelector(".c-volta");
  var cPes = raiz.querySelector(".c-pes");
  var cHosp = raiz.querySelector(".c-hosp");
  var cDur = raiz.querySelector(".c-dur");
  var cAlertas = raiz.querySelector(".c-alertas");
  var cRes = raiz.querySelector(".res");
  var totRot = raiz.querySelector(".tot-rot");
  var totVal = raiz.querySelector(".tot-val");
  var totDia = raiz.querySelector(".tot-dia");
  [cIda, cVolta, cPes, cHosp].forEach(function (el) {
    if (el) { el.addEventListener("input", render); el.addEventListener("change", render); }
  });

  /* A viagem acompanha o leitor entre as cidades: os campos entram na URL
     e os links das outras cidades carregam os mesmos parâmetros. Quem clica
     em "Santiago" não precisa digitar as datas de novo. */
  var ISO = /^\d{4}-\d{2}-\d{2}$/;
  (function lerURL() {
    try {
      var q = new URLSearchParams(location.search);
      if (ISO.test(q.get("d") || "")) cIda.value = q.get("d");
      if (ISO.test(q.get("v") || "")) cVolta.value = q.get("v");
      var np = parseInt(q.get("p"), 10);
      if (np >= 1 && np <= 8) cPes.value = np;
    } catch (e) { /* URL estranha não pode derrubar a página */ }
  })();

  var abas = [].slice.call(raiz.querySelectorAll(".calc-cidades a.cc"));
  function levarViagem() {
    var q = "?d=" + encodeURIComponent(cIda.value) +
            "&v=" + encodeURIComponent(cVolta.value) +
            "&p=" + encodeURIComponent(cPes.value);
    abas.forEach(function (a) {
      a.href = a.href.split("?")[0].split("#")[0] + q + "#calculadora";
    });
  }

  function periodo() {
    var a = dt(cIda.value), b = dt(cVolta.value);
    if (!a || !b || isNaN(a) || isNaN(b) || b <= a)
      return { noites: Math.max(1, CFG.dias - 1), d: CFG.dias, ok: false };
    var n = Math.min(29, Math.round((b - a) / DIA));
    return { noites: n, d: n + 1, ok: true, a: a, b: b };
  }

  /* As datas avisam; elas não mexem no preço. Multiplicar a diária por um
     fator de alta que ninguém apurou seria inventar número. */
  function alertas(pr) {
    var av = [];
    if (!pr.ok) {
      av.push(["a", "Datas incompletas",
        "Preencha chegada e volta (a volta precisa ser depois da chegada). Enquanto isso, " +
        "a conta está usando o cenário apurado: " + plural(CFG.dias, "dia", "dias") + "."]);
      return av;
    }
    (CFG.eventos || []).forEach(function (e) {
      if (cruza(pr.a, pr.b, e[0], e[1])) av.push([e[2], e[3], e[4]]);
    });
    var j = CFG.janela;
    if (j && (pr.a < dt(j[0]) || pr.b > dt(j[1]))) av.push([j[2], j[3], j[4]]);
    return av;
  }

  function render() {
    var pr = periodo();
    var d = pr.d, noites = pr.noites;
    var p = Math.max(1, Math.min(8, parseInt(cPes.value, 10) || 1));
    var h = HOSP[cHosp.value] || CFG.hosp[0];
    var quartos = Math.ceil(p / 2);
    var un = h.pessoa ? p : quartos;
    var fator = 1 - (h.desc || 0);

    var hRef = h.ref * noites * un * fator;
    var hMin = h.mn * noites * un * fator;
    var hMax = h.mx * noites * un * fator;

    var ing = 0, outros = 0, pcts = [];
    linhas.forEach(function (tr) {
      var t = tr.dataset.tipo, v = parseFloat(tr.dataset.v);
      if (t === "ingresso") {
        var on = tr.querySelector("input").checked;
        tr.classList.toggle("off", !on);
        if (on) ing += v;
      } else if (t === "fixo") {
        outros += v * p;
      } else if (t === "dia") {
        var q = tr.dataset.grupo ? 1 : p;
        var sub = v * d * q;
        outros += sub;
        if (tr.dataset.rot) tr.cells[0].textContent = tr.dataset.rot.replace("{d}", d);
        tr.cells[1].textContent = moeda(sub);
      } else if (t === "metro") {
        var pd = parseFloat(tr.dataset.dia), teto = parseFloat(tr.dataset.teto);
        var mp = Math.min(d * pd, teto * Math.ceil(d / 7));
        outros += mp * p;
        tr.cells[0].textContent = (d * pd >= teto * Math.ceil(d / 7))
          ? "Metrô, teto semanal" : "Metrô, " + plural(d, "dia", "dias");
        tr.cells[1].textContent = moeda(mp);
      } else if (t === "pct") {
        pcts.push(tr);
      }
    });

    /* Uma conta só, aplicada três vezes: no valor de referência e nos dois
       extremos da faixa de hospedagem. Assim os percentuais (IVA, IOF)
       acompanham a faixa em vez de ficarem presos ao valor central. */
    function totalCom(hv) {
      var b = ing * p + outros + hv, e = 0;
      pcts.forEach(function (tr) {
        e += (tr.dataset.base === "hosp" ? hv : b) * parseFloat(tr.dataset.p);
      });
      return b + e;
    }
    var total = totalCom(hRef), tMin = totalCom(hMin), tMax = totalCom(hMax);

    pcts.forEach(function (tr) {
      var pp = parseFloat(tr.dataset.p);
      var sobre = tr.dataset.base === "hosp" ? hRef : (ing * p + outros + hRef);
      var val = sobre * pp;
      tr.cells[1].textContent = (val < 0 ? "\u2212 " : "") + moeda(Math.abs(val));
    });

    if (lHosp) {
      lHosp.cells[0].textContent = "Hospedagem, " + plural(noites, "noite", "noites");
      lHosp.cells[1].textContent = moeda(hRef);
    }

    cDur.innerHTML = pr.ok
      ? "<b>" + plural(d, "dia", "dias") + "</b> &middot; " +
        plural(noites, "noite", "noites") + " de hospedagem &middot; " +
        brdata(pr.a) + " a " + brdata(pr.b)
      : "<b>" + plural(CFG.dias, "dia", "dias") + "</b> &middot; cenário apurado";

    cAlertas.innerHTML = alertas(pr).map(function (x) {
      return '<div class="aviso ' + x[0] + '"><span class="t">' + x[1] +
             "</span><p>" + x[2] + "</p></div>";
    }).join("");

    if (totRot) {
      totRot.textContent = p === 1 ? "Total por pessoa"
                                   : "Total do grupo, " + plural(p, "pessoa", "pessoas");
      totVal.textContent = moeda(total);
      totDia.textContent = m0(total / p / d) + " por pessoa por dia";
    }

    var faixa = (Math.round(tMin) === Math.round(tMax))
      ? ["Hospedagem", m0(hRef), "Esta categoria tem valor único apurado, sem faixa observada."]
      : ["Faixa da hospedagem", m0(tMin) + "–" + num0(tMax),
         "A diária observada varia entre " + m0(h.mn) + " e " + m0(h.mx) +
         ". Este é o total do grupo nos dois extremos."];

    cRes.innerHTML =
      cel("Total do grupo", m0(total), plural(d, "dia", "dias") + " · " +
          plural(p, "pessoa", "pessoas") + " · " + plural(noites, "noite", "noites") + " de hospedagem", "") +
      cel("Por pessoa", m0(total / p), "Hospedagem " + m0(hRef / p) +
          " · o resto " + m0((total - hRef) / p), "c") +
      cel("Por pessoa por dia", m0(total / p / d),
          "Só o que está nesta ficha. O que não foi apurado continua de fora.", "") +
      cel(faixa[0], faixa[1], faixa[2], "c");

    levarViagem();
  }

  function cel(rot, big, sub, cls) {
    return '<div class="pcel"><span class="rotp">' + rot + '</span>' +
           '<span class="big ' + cls + '">' + big + '</span>' +
           '<span class="sub">' + sub + "</span></div>";
  }

  calc.hidden = false;
  render();
  }
})();
