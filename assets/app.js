const $ = selector => document.querySelector(selector);

const els = {
  q: $("#q"),
  area: $("#area"),
  brazil: $("#brazil"),
  coverage: $("#coverage"),
  download: $("#download"),
  programmatic: $("#programmatic"),
  list: $("#list"),
  empty: $("#empty"),
  count: $("#count"),
  areaLinks: $("#area-links"),
  heroSearch: $("#hero-search")
};

let all = [];
let filtered = [];

const split = value => String(value || "").split("|").map(item => item.trim()).filter(Boolean);
const norm = value => String(value || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
const esc = value => String(value || "").replace(/[&<>"']/g, char => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[char]));
const opt = (element, values) => [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b, "pt-BR")).forEach(value => element.add(new Option(value, value)));
const detail = (label, value) => `<div class="detail"><strong>${label}</strong><span>${esc(value || "Não informado")}</span></div>`;
const link = (label, url) => url && /^https:\/\//.test(url) ? `<a class="source" href="${esc(url)}" target="_blank" rel="noopener">${label} ↗</a>` : "";

function card(resource) {
  const acronym = resource.acronym && resource.acronym !== resource.resource_name ? `<span class="acronym"> · ${esc(resource.acronym)}</span>` : "";
  return `<article class="card">
    <div class="top"><h3>${esc(resource.resource_name)}${acronym}</h3><span class="tag">${esc(resource.official_identity)}</span></div>
    <p class="description">${esc(resource.description)}</p>
    <div class="chips">${split(resource.research_areas).map(area => `<span class="chip">${esc(area)}</span>`).join("")}</div>
    <div class="access"><span>Download gratuito: <b>${esc(resource.free_download)}</b></span><span>API ou acesso automatizado: <b>${esc(resource.programmatic_access)}</b></span><span>Dados para o Brasil: <b>${esc(resource.covers_brazil)}</b></span></div>
    <details><summary>Ver detalhes, evidências e limitações</summary>
      <div class="details">
        ${detail("Palavras-chave", resource.keywords)}
        ${detail("Produtos", resource.data_product_types)}
        ${detail("Formatos", resource.data_formats)}
        ${detail("Visualizações", resource.visualization_types)}
        ${detail("Protocolos e ferramentas", resource.access_protocols)}
        ${detail("Autenticação", resource.authentication_required)}
        ${detail("Resolução espacial", resource.spatial_resolution)}
        ${detail("Cobertura temporal", resource.temporal_coverage)}
        ${detail("Resolução temporal", resource.temporal_resolution)}
        ${detail("Origem dos dados", resource.data_sources)}
        ${detail("Condições de acesso", resource.access_conditions)}
        ${detail("Licença", resource.license)}
        ${detail("Responsável", resource.owner_or_manager)}
        ${detail("Tipo de instituição", resource.institutional_status)}
        ${detail("Utilidade acadêmica", resource.academic_uses)}
        ${detail("Limitações", resource.limitations)}
        ${detail("Tipo de evidência acadêmica", resource.academic_evidence_type)}
        ${detail("Síntese da evidência", resource.academic_evidence_note)}
        ${detail("Verificado em", resource.last_verified)}
      </div>
      <div class="source-links">
        ${link("Acessar dados", resource.data_access_url)}
        ${link("Página oficial", resource.homepage_url)}
        ${link("Documentação de acesso", resource.access_documentation_url)}
        ${link("Evidência acadêmica ou técnica", resource.academic_evidence_url)}
        ${link("Evidência oficial", resource.verification_url)}
      </div>
    </details>
  </article>`;
}

function render() {
  els.list.innerHTML = filtered.map(card).join("");
  els.empty.hidden = filtered.length > 0;
  els.count.textContent = `${filtered.length} de ${all.length} fontes`;
}

function filter() {
  const query = norm(els.q.value);
  const fields = [
    "resource_name", "acronym", "official_identity", "description", "research_areas",
    "keywords", "data_product_types", "data_formats", "visualization_types",
    "geographic_coverage", "data_sources", "access_protocols", "access_conditions",
    "license", "owner_or_manager", "academic_uses", "limitations", "academic_evidence_note"
  ];

  filtered = all.filter(resource =>
    (!query || norm(fields.map(key => resource[key]).join(" ")).includes(query)) &&
    (!els.area.value || split(resource.research_areas).includes(els.area.value)) &&
    (!els.brazil.value || resource.covers_brazil === els.brazil.value) &&
    (!els.coverage.value || resource.geographic_coverage === els.coverage.value) &&
    (!els.download.value || resource.free_download === els.download.value) &&
    (!els.programmatic.value || resource.programmatic_access === els.programmatic.value)
  );

  render();
}

function goToCatalog() {
  $("#catalogo").scrollIntoView({behavior: "smooth", block: "start"});
}

function setQuery(value) {
  els.q.value = value;
  filter();
  goToCatalog();
}

function renderAreas() {
  const counts = new Map();
  all.flatMap(resource => split(resource.research_areas)).forEach(area => counts.set(area, (counts.get(area) || 0) + 1));
  els.areaLinks.innerHTML = [...counts.entries()]
    .sort((a, b) => a[0].localeCompare(b[0], "pt-BR"))
    .map(([area, count]) => `<button class="area-card" type="button" data-area="${esc(area)}"><strong>${esc(area)}</strong><span>${count} ${count === 1 ? "fonte" : "fontes"}</span></button>`)
    .join("");

  els.areaLinks.querySelectorAll("[data-area]").forEach(button => button.addEventListener("click", () => {
    els.area.value = button.dataset.area;
    filter();
    goToCatalog();
  }));
}

async function init() {
  try {
    const response = await fetch("data/data_resources.json");
    if (!response.ok) throw Error("Não foi possível carregar os dados.");

    all = await response.json();
    all.sort((a, b) => a.resource_name.localeCompare(b.resource_name, "pt-BR"));
    filtered = [...all];

    opt(els.area, all.flatMap(resource => split(resource.research_areas)));
    opt(els.coverage, all.map(resource => resource.geographic_coverage));
    renderAreas();

    [els.q, els.area, els.brazil, els.coverage, els.download, els.programmatic].forEach(element => element.addEventListener("input", filter));
    els.heroSearch.addEventListener("submit", event => { event.preventDefault(); filter(); goToCatalog(); });
    document.querySelectorAll("[data-query]").forEach(button => button.addEventListener("click", () => setQuery(button.dataset.query)));
    $("#clear").addEventListener("click", () => {
      $("#filters").reset();
      els.q.value = "";
      filter();
      els.q.focus();
    });

    $("#n-total").textContent = all.length;
    $("#n-free").textContent = all.filter(resource => resource.free_download === "sim").length;
    $("#n-api").textContent = all.filter(resource => resource.programmatic_access === "sim").length;
    $("#n-br").textContent = all.filter(resource => ["sim", "parcial"].includes(resource.covers_brazil)).length;
    $("#updated").textContent = all.map(resource => resource.last_verified).filter(Boolean).sort().at(-1) || "não informada";
    render();
  } catch (error) {
    els.list.innerHTML = `<div class="empty"><h3>Falha ao carregar o catálogo</h3><p>${esc(error.message)}</p></div>`;
  }
}

init();
