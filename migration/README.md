# Matrizes de migração DATA1

## Finalidade

A migração do esquema 0.7.0 para 0.8.0 é preparada em matrizes separadas:

- `data1b_migration_matrix.csv`: decisões iniciais sobre os quatro novos campos e normalizações técnicas já projetadas;
- `data1bx_migration_matrix.csv`: complemento obrigatório para cinco dimensões que ainda não estavam cobertas;
- `br1_review_matrix.csv`: primeiro lote de revisão aprofundada dos registros que permanecem dependentes de evidência externa.

Nenhuma matriz substitui o arquivo canônico `data/data_resources.csv`. Os valores permanecem associados pelo `resource_id`, e a versão 0.7.0 continua protegida até DATA1-C.

## DATA1-B — matriz inicial

`data1b_migration_matrix.csv` registra uma decisão proposta para cada uma das 51 fontes.

### Ligações com o CSV atual

| Decisão | Campo atual usado como base |
|---|---|
| tipo funcional | `official_identity` |
| escala geográfica | `geographic_coverage` |
| formatos | `data_formats` |
| protocolos e ferramentas | `access_protocols` |
| situação institucional | `institutional_status` |
| evidência | `verification_url` |

### Colunas

- `resource_id`: identificador preservado do catálogo;
- `resource_type_proposed`: função principal controlada;
- `geographic_scope_proposed`: maior extensão geográfica geral;
- `data_formats_proposed`: formatos normalizados;
- `access_protocols_proposed`: protocolos e interfaces técnicas;
- `access_tools_proposed`: pacotes, clientes e ambientes separados dos protocolos;
- `institutional_status_proposed`: situação institucional normalizada e multivalorada;
- `citation_guidance_url_proposed`: página oficial específica de citação, somente quando confirmada;
- `confidence`: confiança global da decisão DATA1-B;
- `migration_status`: decisão pronta ou dependente de revisão manual;
- `rationale`: justificativa funcional e geográfica;
- `exceptions`: exceções codificadas que impedem migração automática.

### Estado

- 51 fontes representadas;
- 24 decisões de alta confiança;
- 27 decisões de confiança média;
- nenhuma decisão de baixa confiança;
- 16 registros sem exceção estão prontos nesta matriz;
- 35 registros permanecem em revisão manual;
- todo valor `other_documented` exige exceção explícita;
- URLs de orientação de citação permanecem vazias até confirmação oficial;
- nenhuma proposta deve ser aplicada antes das revisões previstas.

## DATA1-BX — complemento obrigatório

A auditoria identificou cinco dimensões ausentes da matriz inicial:

- `data_product_types`;
- `visualization_types`;
- `data_sources`;
- `temporal_resolution`;
- `access_conditions`.

O contrato está em `data1bx_contract.json`. A matriz `data1bx_migration_matrix.csv` preserva os mesmos 51 IDs e registra, para cada dimensão:

- valor proposto;
- confiança específica do campo;
- estado de revisão;
- base de evidência;
- URL, data e revisor quando houver confirmação oficial;
- campos ainda pendentes.

### Estados

- `não_iniciado`: nenhum valor carregado; todas as cinco dimensões pendentes;
- `carregado_do_csv`: valor copiado do CSV 0.7.0, com confiança `desconhecida`; não equivale a verificação externa;
- `revisão_manual`: uma ou mais dimensões em avaliação;
- `confirmado_documentação_oficial`: cinco dimensões sustentadas por evidência oficial, data e revisor.

Uma confiança global por linha não é suficiente no DATA1-BX. A confiança deve ser registrada separadamente para cada dimensão.

## DATA1-BR — lote BR1

O contrato `br1_contract.json` seleciona sete fontes atuais que combinam uso científico elevado, impacto público e alto custo de interpretação incorreta:

1. CEMADEN (`DR0005`);
2. dados.gov.br (`DR0008`);
3. MapBiomas (`DR0010`);
4. TerraBrasilis (`DR0011`);
5. BDQueimadas (`DR0012`);
6. Google Earth Engine (`DR0019`);
7. Global Forest Watch (`DR0044`).

A matriz `br1_review_matrix.csv` registra:

- justificativa da seleção e nível de risco;
- riscos de agregação, escopo por produto, acesso, licença, temporalidade e semântica;
- achados de consistência interna;
- URLs já presentes no CSV;
- dimensões que precisam de confronto com documentação oficial;
- bloqueio explícito da revisão externa quando não há acesso web atual;
- decisão conservadora de manter o CSV até existir evidência contemporânea.

A auditoria interna não equivale a validação factual externa. Enquanto `external_review_status` for `bloqueada_sem_web`, a matriz não aceita URL de evidência usada, revisor, data ou decisão de correção.

## Validação

Execute:

```bash
python3 scripts/validate_migration_matrix.py
python3 scripts/validate_data1bx_matrix.py
python3 scripts/load_data1bx_from_canonical.py
python3 scripts/validate_br1_matrix.py
```

Os testes preservam os 51 IDs, a correspondência das matrizes com o CSV 0.7.0, a confiança por campo, os estados de evidência e o bloqueio de alterações automáticas.

## Estado protegido

- CSV canônico: 51 fontes × 34 campos;
- versão formal: 0.7.0;
- esquema 0.8.0: proposta não aplicada;
- DATA1-BX: projeção canônica concluída, confiança externa ainda desconhecida;
- BR1: seleção e auditoria interna concluídas; revisão factual externa bloqueada;
- candidatos: fora do CSV;
- DOI: bloqueado.
