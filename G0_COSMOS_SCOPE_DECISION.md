# G0 — decisão de escopo do Project COSMOS

Data da decisão: 2026-07-21  
Recurso: `DR0051 — Project COSMOS`  
Resultado: **manter no catálogo principal como infraestrutura bibliométrica, com papel e limitações explícitos**.

## Questão de decisão

O Project COSMOS deve permanecer no catálogo principal, ser movido para seção auxiliar, fundido a outro recurso ou excluído?

## Base considerada

A decisão usa:

- a política de seleção versionada do catálogo;
- a linha canônica `DR0051` da versão 0.7.0;
- a metodologia oficial já registrada e verificada em 2026-07-18: `https://interactive.carbonbrief.org/cosmos/methodology/index.html`;
- a auditoria interna BR5;
- a distinção entre fonte de dados ambientais e infraestrutura de informação relevante à pesquisa ambiental.

Esta etapa resolve elegibilidade e destino no catálogo. Ela não substitui nova verificação factual de todos os atributos de acesso, licença, atualização ou cobertura.

## Avaliação pelos critérios mínimos

| Critério | Avaliação | Justificativa |
|---|---|---|
| Relevância ambiental | atende | organiza literatura e relações de citação sobre mudanças climáticas |
| Dados, metadados ou descoberta | atende com ressalva | disponibiliza exploração estruturada de publicações, autores, instituições, rankings e rede de citações; não é apenas texto editorial |
| Documentação oficial | atende | existe metodologia oficial identificável |
| Governança | atende | responsabilidade institucional atribuída ao Carbon Brief Ltd |
| Utilidade distinta | atende | permite análise bibliométrica e descoberta da estrutura da pesquisa climática |
| Descrição no nível de fonte | atende | identidade, corpus, acesso e limitações podem ser descritos separadamente |
| Registro honesto de acesso e limitações | atende | a base integral não é aberta; a interface pública e as restrições podem ser declaradas |

## Confronto com os critérios de exclusão

O recurso não deve ser excluído como notícia, blog ou material somente didático. Embora seja produzido por uma organização de comunicação científica, sua função aqui é uma base bibliométrica estruturada com metodologia e interface próprias.

Também não é um dataset isolado pertencente a outra fonte já catalogada, nem um mirror sem governança própria. Sua função é distinta das bases ambientais primárias e dos repositórios de dados ecológicos.

## Decisão

### Destino

**Catálogo principal.**

A permanência é justificada pela unidade de seleção do projeto, que inclui fontes de dados e infraestruturas de informação relevantes para pesquisa, ensino ou extensão ambiental.

### Papel científico

COSMOS deve ser apresentado como:

- base bibliométrica de pesquisa climática;
- infraestrutura de descoberta e análise de literatura;
- recurso para bibliometria, ensino e estudos sobre produção científica.

COSMOS **não é fonte direta de medições ambientais**, observações de campo, séries climáticas, inventários de emissões ou produtos geoespaciais. Resultados empíricos encontrados por meio da interface devem remeter às publicações e fontes originais.

### Condições de permanência

A linha deve continuar deixando explícito que:

1. a base integral não é aberta para download público;
2. o acesso público ocorre por metodologia, rankings, mapa e outras visualizações;
3. não há API pública documentada nem download integral aberto no estado registrado;
4. cobertura e data de corte pertencem ao corpus bibliométrico, não à cobertura espaço-temporal de um fenômeno ambiental;
5. a licença do conteúdo público não deve ser generalizada para a base integral;
6. o recurso não deve ser comparado a bases de medições ambientais em análises de disponibilidade de dados empíricos.

## Implicações para o esquema 0.8.0

Na migração futura, a proposta deve preservar:

- `resource_type = database`;
- `geographic_scope = not_applicable`, porque a unidade principal é literatura e citação, não cobertura geográfica de observações ambientais;
- `covers_brazil = não se aplica`;
- `free_download = não`;
- `programmatic_access = não`;
- `authentication_required = não se aplica` para a interface pública, sem inferir condições da base integral;
- limitações explícitas sobre acesso restrito e natureza bibliométrica.

Nenhum desses valores é aplicado automaticamente ao CSV 0.7.0 neste ciclo. A migração continua subordinada a DATA1-C e aos contratos de 0.8.0.

## Regra geral derivada

Recursos bibliométricos e editoriais podem permanecer no catálogo principal quando:

1. oferecem dados ou metadados estruturados, busca, rede de citações ou outra função de descoberta reutilizável;
2. possuem metodologia e governança identificáveis;
3. têm utilidade ambiental distinta;
4. permitem descrever acesso, licença e limitações com honestidade;
5. não são apresentados como substitutos das fontes ambientais primárias.

Materiais apenas narrativos, noticiosos ou didáticos, sem infraestrutura estruturada associada, continuam excluídos.

## Estado após G0

- elegibilidade: confirmada;
- destino: catálogo principal;
- decisão na fila: `manter_confirmado`;
- status: `escopo_resolvido`;
- evidência factual adicional: ainda necessária durante a revisão final dos atributos;
- alteração do CSV 0.7.0: nenhuma;
- próximo ciclo científico: W1A — TerraBrasilis e Google Earth Engine Data Catalog.
