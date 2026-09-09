// Busca e filtro de destinos.
// Os cartões já vêm no HTML — este script apenas mostra e esconde.
// Sem JS, a página continua completa e indexável.
(function () {
  const grade = document.getElementById("grade");
  if (!grade) return;
  const cards = [...grade.querySelectorAll(".dest")];
  const vazio = document.getElementById("vazio");
  const contagem = document.getElementById("contagem");
  const q = document.getElementById("q");
  const chips = [...document.querySelectorAll(".chip")];
  let filtro = "todos";

  const semAcento = s => s.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

  function render() {
    const termo = semAcento(q.value.trim().toLowerCase());
    let visiveis = 0;
    cards.forEach(c => {
      const okF = filtro === "todos" ? true
        : filtro === "publicado" ? c.dataset.status === "publicado"
        : c.dataset.regiao === filtro;
      const okT = !termo || semAcento(c.dataset.busca).includes(termo);
      const mostra = okF && okT;
      c.hidden = !mostra;
      if (mostra) visiveis++;
    });
    if (vazio) vazio.hidden = visiveis !== 0;
    if (contagem) {
      contagem.textContent = visiveis === 1 ? "1 destino" : visiveis + " destinos";
    }
  }

  if (q) q.addEventListener("input", render);
  chips.forEach(c => c.addEventListener("click", () => {
    chips.forEach(o => o.setAttribute("aria-pressed", String(o === c)));
    filtro = c.dataset.f;
    render();
  }));
})();
