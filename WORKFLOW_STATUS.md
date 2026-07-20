# Estado do workflow

## Regra operacional

Uma tarefa só é concluída após branch, pull request, integração à `main`, GitHub Actions verde e registro no changelog. Alterações públicas também exigem confirmação do deploy. CI verde comprova estrutura interna, não verdade factual externa.

## Limitações

- revisão externa bloqueada até cada afirmação receber evidência oficial atual, data e revisor;
- prioridade e onda operacional não elevam confiança nem autorizam correções no CSV;
- URLs iguais entre homepage e acesso permanecem pendentes;
- novas fontes permanecem fora do CSV;
- v1.0.0 e DOI permanecem bloqueados.

## Backlog

| Frente | Estado | Produto/critério |
|---|---|---|
| QC0 | concluído | 14 regras alinhadas |
| SELECT1 | concluído | política de seleção ativa |
| DATA1-BX | projeção concluída | 51 × 5 dimensões; confiança desconhecida |
| DATA1-BR | auditoria interna concluída | BR1–BR5 cobrem 35 casos |
| DATA1-BR-CLOSE | concluído | fila corrigida, evidência longa, documentação e validação integradas |
| DATA1-EXT | ativo | portão G0 e revisão por ondas |
| DATA1-C | bloqueado | decisões e evidências resolvidas |
| DATA1-D | planejado | 14 regras no CSV 0.8.0 |
| DATA2 | planejado | 51 fontes no esquema final |
| UX5 | parcial | 38 campos e testes de navegador |
| RELEASE2 | bloqueado | G1–G10 e deploy confirmado |
| DOI | bloqueado | G1–G12 e depósito inspecionado |
| RES1 | P3, não bloqueante | resolução por produto |
| EDU1 | P3, não bloqueante | página didática referenciada |

## Estado consolidado

- versão **0.7.0**; CSV **51 × 34**;
- DATA1-B: **16 prontos + 35 revisão_manual**;
- DATA1-BX: confiança `desconhecida`;
- BR1–BR5: **35 de 35** casos distribuídos;
- fila integrada: **35 fontes**;
- prioridade científica: **P0=23, P1=9, P2=3, P3=0**;
- ondas: **G0=1, W1=7, W2=9, W3=7, W4=8, W5=3**;
- evidências externas registradas: **0**;
- candidatos: **18 fora do CSV**;
- esquema 0.8.0 não aplicado; expansão e DOI bloqueados.

## Fechamento DATA1-BR-CLOSE

O conteúdo foi integrado diretamente à `main` no commit `df66ab15a064e2b1b70a6e9387a1abcc20b7358a`. A integração concorrente foi documentada e submetida à suíte completa no PR #29, run `29778282362`, merge `e02b409c10bde4afc890ae53793095550d3e4e61`.

`scientific_priority_tier` usa somente impacto e risco comparáveis. `execution_wave` organiza escopo, papéis dos links e documentação ausente. Número bruto de flags ou dimensões não entra na prioridade.

`migration/external_review_evidence.csv` registra uma linha por afirmação e dimensão; nenhuma evidência altera o CSV automaticamente.

## Próximos produtos

1. **G0 — decisão de escopo:** parecer de elegibilidade do Project COSMOS e regra geral para recursos bibliométricos;
2. **W1 — dossiê factual:** SiBBr, SIRENE, BDiA, Global Carbon Atlas, TerraBrasilis, Google Earth Engine Data Catalog e HidroWeb;
3. **checkpoint pós-W1:** fila reavaliada com base nas lacunas reais;
4. **prévia 0.8.0:** somente depois das decisões críticas, em arquivo não canônico;
5. preservar CSV 51 × 34, versão 0.7.0, candidatos e DOI bloqueado.

A autoridade documental segue `WORKFLOW_STATUS.md`, `IMPLEMENTATION_WORKFLOW.md`, `QUALITY_CORRECTION_WORKFLOW.md`, `FINAL_OBJECTIVES_AND_DOI_GATES.md`, `METHODOLOGY.md`, `CODEBOOK.md` e contratos executáveis. A inspeção está em `DOCUMENTATION_CONSISTENCY_AUDIT.md`.

RES1 e EDU1 permanecem não bloqueantes para v1.0.0 e DOI.
