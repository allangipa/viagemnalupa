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

  var cDias = document.getElementById("c-dias");
  var cPes = document.getElementById("c-pes");
  var cHosp = document.getElementById("c-hosp");
  [cDias, cPes, cHosp].forEach(function (el) {
    if (el) { el.addEventListener("input", render); el.addEventListener("change", render); }
  });

  function render() {
    var d = Math.max(1, Math.min(30, parseInt(cDias.value, 10) || 1));
    var p = Math.max(1, Math.min(8, parseInt(cPes.value, 10) || 1));
    var h = HOSP[cHosp.value] || HOSP.manhattan;
    var noites = Math.max(1, d - 1);
    var quartos = Math.ceil(p / 2);

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
