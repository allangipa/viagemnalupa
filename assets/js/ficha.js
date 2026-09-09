/* Ficha de custos interativa.
   A tabela já vem completa no HTML com o cenário apurado (7 dias, 1 pessoa,
   intermediário em Manhattan). Este script só recalcula em cima dela.
   Sem JavaScript a página continua correta e indexável — só não é interativa,
   e por isso os controles ficam escondidos até o script assumir. */
(function () {
  var tab = document.getElementById("tab-ficha");
  var calc = document.getElementById("calc");
  if (!tab || !calc) return;

  /* Diárias apuradas na própria página. "ref" é o valor de referência usado
     na conta; "min/max" é a faixa observada, mostrada junto para o leitor ver
     o tamanho da incerteza em vez de engolir um número só. */
  var HOSP = {
    hostel:    { ref: 45,  min: 35,  max: 55,  pessoa: true,  rot: "Hostel, dormitório em Manhattan" },
    economico: { ref: 78,  min: 60,  max: 95,  pessoa: false, rot: "Hotel econômico, quarto privativo" },
    brooklyn:  { ref: 220, min: 160, max: 280, pessoa: false, rot: "Intermediário no Brooklyn" },
    manhattan: { ref: 300, min: 250, max: 400, pessoa: false, rot: "Intermediário em Manhattan" },
    media:     { ref: 349, min: 349, max: 349, pessoa: false, rot: "Média geral de Manhattan" }
  };

  function usd(n) {
    return "US$ " + n.toLocaleString("pt-BR", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }
  function usd0(n) {
    return "US$ " + Math.round(n).toLocaleString("pt-BR");
  }
  function plural(n, um, muitos) { return n + " " + (n === 1 ? um : muitos); }

  var ingressos = [].slice.call(tab.querySelectorAll('tr[data-tipo="ingresso"]'));
  var lMetro = tab.querySelector('tr[data-tipo="metro"]');
  var lHosp = tab.querySelector('tr[data-tipo="hosp"]');
  var pe = document.getElementById("tot-rot");
  var pv = document.getElementById("tot-val");
  var pd = document.getElementById("tot-dia");

  /* Caixas de seleção injetadas aqui, e não no HTML: sem JS elas não
     apareceriam funcionando, e caixa que não funciona é pior que nenhuma. */
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

  var cIda = document.getElementById("c-ida");
  var cVolta = document.getElementById("c-volta");
  var cPes = document.getElementById("c-pes");
  var cHosp = document.getElementById("c-hosp");
  var cDur = document.getElementById("c-dur");
  var cAlertas = document.getElementById("c-alertas");
  [cIda, cVolta, cPes, cHosp].forEach(function (el) {
    if (el) { el.addEventListener("input", render); el.addEventListener("change", render); }
  });

  /* Datas do próprio conteúdo da página, já apuradas: a maratona e a semana
     do Thanksgiving. Nenhuma delas altera a conta sozinha — elas avisam.
     Multiplicar a diária por um fator de alta que ninguém apurou seria
     inventar número, que é exatamente o que este site não faz. */
  var DIA = 86400000;
  function dt(s) { return s ? new Date(s + "T12:00:00") : null; }
  function cruza(a, b, x, y) { return a <= dt(y) && b >= dt(x); }
  function brdata(d) {
    return d.toLocaleDateString("pt-BR", { day: "numeric", month: "long", year: "numeric" });
  }

  function periodo() {
    var a = dt(cIda.value), b = dt(cVolta.value);
    if (!a || !b || isNaN(a) || isNaN(b) || b <= a) return { noites: 6, d: 7, ok: false };
    var n = Math.min(29, Math.round((b - a) / DIA));
    return { noites: n, d: n + 1, ok: true, a: a, b: b };
  }

  function alertas(pr) {
    var av = [];
    if (!pr.ok) {
      av.push(["a", "Datas incompletas",
        "Preencha chegada e volta (a volta precisa ser depois da chegada). " +
        "Enquanto isso, a conta está usando o cenário apurado: 7 dias, 6 noites."]);
      return av;
    }
    if (cruza(pr.a, pr.b, "2026-10-30", "2026-11-02"))
      av.push(["", "Sua viagem pega a Maratona de Nova York",
        "Domingo, 1º de novembro. Ruas fechadas em cinco distritos e preços de hotel " +
        "já elevados nesse fim de semana. A conta abaixo <b>não</b> embute essa alta."]);
    if (cruza(pr.a, pr.b, "2026-11-22", "2026-11-29"))
      av.push(["", "Sua viagem pega a semana do Thanksgiving",
        "Quinta, 26 de novembro, e a 100ª edição do desfile da Macy's. A diária média " +
        "da cidade nessa semana foi de <b>US$ 452</b> contra <b>US$ 349</b> de média " +
        "geral <span class=\"flag\">Dado de 2023</span> — cerca de 30% a mais, e hoje " +
        "seria maior. A conta abaixo usa a diária normal: <b>some essa diferença por conta própria</b>."]);
    var fora = pr.a < dt("2026-11-01") || pr.b > dt("2026-11-30");
    if (fora)
      av.push(["b", "Fora de novembro de 2026",
        "Os preços desta página foram apurados para novembro. Ingressos mudam pouco; " +
        "<b>hotel muda muito</b>. Dezembro é o mês mais caro do ano em Nova York, com " +
        "diária média de <b>US$ 577</b> — 65% acima da média geral."]);
    return av;
  }

  function render() {
    var pr = periodo();
    var d = pr.d, noites = pr.noites;
    var p = Math.max(1, Math.min(8, parseInt(cPes.value, 10) || 1));
    var h = HOSP[cHosp.value] || HOSP.manhattan;
    var quartos = Math.ceil(p / 2);

    cDur.innerHTML = pr.ok
      ? "<b>" + plural(d, "dia", "dias") + "</b> &middot; " +
        plural(noites, "noite", "noites") + " de hotel &middot; " +
        brdata(pr.a) + " a " + brdata(pr.b)
      : "<b>7 dias</b> &middot; 6 noites de hotel &middot; cenário apurado";

    cAlertas.innerHTML = alertas(pr).map(function (x) {
      return '<div class="aviso ' + x[0] + '"><span class="t">' + x[1] +
             "</span><p>" + x[2] + "</p></div>";
    }).join("");

    var ing = 0;
    ingressos.forEach(function (tr) {
      var on = tr.querySelector("input").checked;
      tr.classList.toggle("off", !on);
      if (on) ing += parseFloat(tr.dataset.v);
    });
    var ingTotal = ing * p;

    var porDia = parseFloat(lMetro.dataset.dia);
    var teto = parseFloat(lMetro.dataset.teto);
    var metroPes = Math.min(d * porDia, teto * Math.ceil(d / 7));
    var metroTotal = metroPes * p;

    var un = h.pessoa ? p : quartos;
    var hRef = h.ref * noites * un;
    var hMin = h.min * noites * un;
    var hMax = h.max * noites * un;

    var total = ingTotal + metroTotal + hRef;
    var totMin = ingTotal + metroTotal + hMin;
    var totMax = ingTotal + metroTotal + hMax;

    lMetro.cells[0].textContent = (d * porDia >= teto * Math.ceil(d / 7))
      ? "Metrô, teto semanal" : "Metrô, " + plural(d, "dia", "dias");
    lMetro.cells[1].textContent = usd(metroPes);
    lMetro.cells[2].innerHTML = "2 viagens por dia a US$ 2,90, com teto de " +
      usd0(teto) + " por semana. Por pessoa.";

    lHosp.cells[0].textContent = "Hospedagem, " + plural(noites, "noite", "noites");
    lHosp.cells[1].textContent = usd(hRef);
    lHosp.cells[2].innerHTML = h.rot + ", " + usd0(h.ref) + "/noite" +
      (h.pessoa ? " por pessoa × " + plural(p, "pessoa", "pessoas")
                : " × " + plural(quartos, "quarto", "quartos"));

    pe.textContent = p === 1 ? "Total por pessoa" : "Total do grupo, " + plural(p, "pessoa", "pessoas");
    pv.textContent = usd(total);
    pd.textContent = usd0(total / p / d) + " por pessoa por dia";

    var cx = document.getElementById("res");
    if (cx) {
      cx.innerHTML =
        cel("Total do grupo", usd0(total), plural(d, "dia", "dias") + " · " +
            plural(p, "pessoa", "pessoas") + " · " + plural(noites, "noite", "noites") + " de hotel", "") +
        cel("Por pessoa", usd0(total / p), "Ingressos " + usd0(ing) + " · metrô " +
            usd0(metroPes) + " · hotel " + usd0(hRef / p), "c") +
        cel("Por pessoa por dia", usd0(total / p / d), "Sem passagem aérea, sem alimentação e sem seguro.", "") +
        cel("Faixa da hospedagem", hMin === hMax ? usd0(totMax)
              : usd0(totMin) + "–" + Math.round(totMax).toLocaleString("pt-BR"),
            hMin === hMax ? "Esta categoria tem valor único apurado, sem faixa."
                          : "A diária observada varia entre " + usd0(h.min) + " e " + usd0(h.max) +
                            ". Este é o total do grupo nos dois extremos.", "c");
    }
  }

  function cel(rot, big, sub, cls) {
    return '<div class="pcel"><span class="rotp">' + rot + '</span>' +
           '<span class="big ' + cls + '">' + big + '</span>' +
           '<span class="sub">' + sub + "</span></div>";
  }

  calc.hidden = false;
  render();
})();
