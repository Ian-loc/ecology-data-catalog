# Estado do workflow

## Regra operacional

Uma tarefa só é concluída após branch, pull request, integração à `main`, GitHub Actions verde e registro no changelog. Alterações públicas também exigem confirmação do deploy. CI verde comprova estrutura interna, não verdade factual externa.

## Limitações

- revisão externa bloqueada até cada afirmação receber evidência oficial atual, data e revisor;
- prioridade e onda operacional não elevam confiança nem autorizam correções no CSV;
- URLs iguais entre homepage e acesso permanecem pendentes;
- novas fontes permanecem fora do CSV;
- planilha nativa e `.xlsx` são espelhos derivados e não substituem o CSV canônico;
- v1.0.0 e DOI permanecem bloqueados.

## Backlog

| Frente | Estado | Produto/critério |
|---|---|---|
| QC0 | concluído | 14 regras alinhadas |
| SELECT1 | concluído | política de seleção ativa |
| DATA1-BX | projeção concluída | 51 × 5 dimensões; confiança desconhecida |
| DATA1-BR | auditoria interna concluída | BR1–BR5 cobrem 35 casos |
| DATA1-BR-CLOSE | concluído | fila corrigida, evidência longa, documentação e validação integradas |
| STATE-SYNC | implementado_pendente_integracao | estados documentais corrigidos e contrato de espelhamento criado |
| DATA1-EXT | ativo | portão G0 e revisão por ondas W1A–W1C, W2–W5 |
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
- W1 subdividida operacionalmente em **W1A=2, W1B=3, W1C=2**;
- evidências externas registradas: **0**;
- candidatos: **18 fora do CSV**;
- esquema 0.8.0 não aplicado; expansão e DOI bloqueados;
- espelho nativo e `.xlsx`: **51 × 22**, históricos e incompletos em relação ao CSV atual.

## STATE-SYNC

A inspeção de 2026-07-21 confirmou que `IMPLEMENTATION_WORKFLOW.md` e `QUALITY_CORRECTION_WORKFLOW.md` ainda descreviam DATA1-BR-CLOSE como pendente. Também confirmou que os dois arquivos do Drive preservam a estrutura histórica de 22 campos, enquanto o CSV canônico possui 34.

O ciclo implementa:

- correção dos estados secundários;
- `DRIVE_MIRROR_CONTRACT.md` como regra de autoridade e regeneração;
- distinção explícita entre changelog atual e tabela de dados defasada no Drive;
- divisão de W1 em W1A–W1C para PRs menores;
- validação automática da existência e dos requisitos mínimos do contrato.

O estado permanece `implementado_pendente_integracao` até PR, CI, merge e changelog.

## Fechamento DATA1-BR-CLOSE

Enquanto esta sessão ainda preparava o pull request, outra sessão abriu e integrou o PR #28, gerando o merge commit `df66ab15a064e2b1b70a6e9387a1abcc20b7358a`. O estado foi novamente validado pelo PR #29, run `29778282362`, e o fechamento documental foi integrado pelo PR #30 no commit `ced7bc7274b740fdc0eed4963d36f0fc33b05d9f`.

`scientific_priority_tier` usa somente impacto e risco comparáveis. `execution_wave` organiza escopo, papéis dos links e documentação ausente. Número bruto de flags ou dimensões não entra na prioridade.

`migration/external_review_evidence.csv` registra uma linha por afirmação e dimensão; nenhuma evidência altera o CSV automaticamente.

## Espelhamento do Drive

A autoridade e a direção do fluxo são definidas em `DRIVE_MIRROR_CONTRACT.md`.

- GitHub `main` e `data/data_resources.csv` permanecem canônicos;
- os arquivos do Drive são derivados e não aceitam sincronização bidirecional automática;
- um espelho sincronizado deve declarar versão, esquema, commit-fonte, data e resultado da comparação;
- o estado 51 × 22 não deve ser usado para avaliar completude do catálogo 0.7.0;
- a regeneração obrigatória 51 × 38 ocorre após DATA1-C e DATA1-D.

## Próximos produtos

1. concluir **STATE-SYNC** por PR, CI, merge e changelog;
2. executar **G0** e produzir parecer de elegibilidade do Project COSMOS e regra geral para recursos bibliométricos;
3. executar **W1A** para TerraBrasilis e Google Earth Engine Data Catalog;
4. executar **W1B** para SiBBr, BDiA e HidroWeb;
5. executar **W1C** para SIRENE e Global Carbon Atlas;
6. realizar checkpoint científico conjunto pós-W1A–W1C;
7. produzir prévia 0.8.0 somente depois das decisões críticas, em arquivo não canônico;
8. preservar CSV 51 × 34, versão 0.7.0, candidatos e DOI bloqueado.

A autoridade documental segue `WORKFLOW_STATUS.md`, `IMPLEMENTATION_WORKFLOW.md`, `QUALITY_CORRECTION_WORKFLOW.md`, `FINAL_OBJECTIVES_AND_DOI_GATES.md`, `METHODOLOGY.md`, `CODEBOOK.md`, `DRIVE_MIRROR_CONTRACT.md` e contratos executáveis. A inspeção está em `DOCUMENTATION_CONSISTENCY_AUDIT.md`.

RES1 e EDU1 permanecem não bloqueantes para v1.0.0 e DOI.
