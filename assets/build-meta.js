async function renderBuildMeta(){
  const targets=[...document.querySelectorAll("[data-build-meta]")];
  if(!targets.length)return;
  try{
    const response=await fetch("data/build-meta.json",{cache:"no-store"});
    if(!response.ok)throw new Error("metadados indisponíveis");
    const meta=await response.json();
    const commit=String(meta.commit||"desconhecido");
    const shortCommit=commit==="local"?commit:commit.slice(0,12);
    const label=`v${meta.version||"?"} · ${shortCommit} · ${meta.records||"?"} fontes × ${meta.fields||"?"} campos`;
    targets.forEach(target=>target.textContent=label);
  }catch(error){
    targets.forEach(target=>target.textContent="versão não identificada");
  }
}
renderBuildMeta();
