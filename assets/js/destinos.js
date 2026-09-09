// Busca e filtro de destinos — sem dependências
const DESTINOS = [
 {
  "cidade": "Nova York",
  "pais": "Estados Unidos",
  "regiao": "america-do-norte",
  "status": "publicado",
  "dias": 7,
  "slug": "nova-york",
  "diaria": "US$ 300",
  "diariaRot": "Diária, intermediário",
  "total": "US$ 2.167",
  "totalRot": "7 dias, por pessoa",
  "achado": "<b>O Met cobra do turista e deixa o morador pagar um centavo.</b> Não existe dia gratuito para quem vem de fora — e o museu fecha às quartas.",
  "busca": "nova york new york eua estados unidos manhattan brooklyn museu met moma estatua da liberdade empire state times square central park friends novembro"
 },
 {
  "cidade": "Santiago",
  "pais": "Chile",
  "regiao": "america-do-sul",
  "status": "producao",
  "dias": 5,
  "slug": "santiago",
  "diaria": "US$ 73",
  "diariaRot": "Diária, intermediário",
  "total": "19% off",
  "totalRot": "IVA isento no hotel",
  "achado": "<b>O Chile isenta os 19% de IVA da hospedagem</b> para turista estrangeiro que paga em moeda estrangeira. Basta pedir no check-in com o passaporte.",
  "busca": "santiago chile cerro san cristobal sky costanera la moneda bellavista valparaiso vinicola neruda metro iva"
 },
 {
  "cidade": "Buenos Aires",
  "pais": "Argentina",
  "regiao": "america-do-sul",
  "status": "producao",
  "dias": 5,
  "slug": "buenos-aires",
  "diaria": "US$ 80",
  "diariaRot": "Apartamento, 1 quarto",
  "total": "21% off",
  "totalRot": "IVA devolvido no hotel",
  "achado": "<b>O dólar blue acabou.</b> A diferença para o oficial hoje é de cerca de 1%. E pagar o hotel com cartão estrangeiro devolve 21% de IVA na hora.",
  "busca": "buenos aires argentina caminito la boca recoleta teatro colon casa rosada malba san telmo palermo tigre obelisco subte dolar blue cambio"
 },
 {
  "cidade": "Maceió",
  "pais": "Brasil",
  "regiao": "brasil",
  "status": "producao",
  "dias": 6,
  "slug": "maceio",
  "diaria": "R$ 200–500",
  "diariaRot": "Diária, intermediário",
  "total": "0,6 m",
  "totalRot": "Maré máxima p/ passeio",
  "achado": "<b>A maré manda no roteiro, não o calendário.</b> As piscinas naturais só existem com maré abaixo de 0,6 m. Escolha a data pela tábua da Marinha.",
  "busca": "maceio alagoas brasil pajucara ponta verde gunga frances maragogi paripueira sao miguel dos milagres patacho mare piscinas naturais nordeste"
 }
];
const grade = document.getElementById("grade");
const contagem = document.getElementById("contagem");
const q = document.getElementById("q");
const chips = [...document.querySelectorAll(".chip")];
let filtro = "todos";
const base = document.body.dataset.base || "./";

function card(d){
  const selo = d.status === "publicado"
    ? '<span class="selo">Publicado</span>'
    : '<span class="selo prod">Em produção</span>';
  const u = base + "destinos/" + d.slug + "/";
  return `<article class="dest">
    <div class="dest-topo">
      <div><h3><a href="${u}">${d.cidade}</a></h3>
      <span class="pais">${d.pais} · roteiro de ${d.dias} dias</span></div>
      ${selo}
    </div>
    <div class="numeros">
      <div class="num-b"><span class="r">${d.diariaRot}</span><span class="v">${d.diaria}</span></div>
      <div class="num-b"><span class="r">${d.totalRot}</span><span class="v c">${d.total}</span></div>
    </div>
    <p class="achado">${d.achado}</p>
    <div class="paginas">
      <a class="pg" href="${u}">Guia dos pontos</a>
      <a class="pg" href="${u}quanto-custa/">Quanto custa</a>
      <a class="pg" href="${u}roteiro-${d.dias}-dias/">Roteiro ${d.dias} dias</a>
    </div>
  </article>`;
}

function render(){
  const termo = q.value.trim().toLowerCase();
  const lista = DESTINOS.filter(d => {
    const okF = filtro === "todos" ? true
      : filtro === "publicado" ? d.status === "publicado"
      : d.regiao === filtro;
    const okT = !termo || d.busca.includes(termo)
      || d.cidade.toLowerCase().includes(termo) || d.pais.toLowerCase().includes(termo);
    return okF && okT;
  });
  grade.innerHTML = lista.length ? lista.map(card).join("")
    : `<p class="vazio">Nenhum destino encontrado para “${q.value}”. Ainda estamos no começo — a lista cresce toda semana.</p>`;
  contagem.textContent = lista.length === 1 ? "1 destino" : lista.length + " destinos";
}

q.addEventListener("input", render);
chips.forEach(c => c.addEventListener("click", () => {
  chips.forEach(o => o.setAttribute("aria-pressed", String(o === c)));
  filtro = c.dataset.f;
  render();
}));
render();
