# Auditoria de consistência documental

Data da inspeção inicial: 2026-07-20  
Follow-up: 2026-07-21

## Escopo inspecionado

Foram confrontados `README.md`, `WORKFLOW_STATUS.md`, `IMPLEMENTATION_WORKFLOW.md`, `QUALITY_CORRECTION_WORKFLOW.md`, `AUDIT_WORKFLOW.md`, `METHODOLOGY.md`, `CODEBOOK.md`, `SELECTION_AND_COVERAGE_POLICY.md`, `DATA1_SCHEMA_AUDIT.md`, `FINAL_OBJECTIVES_AND_DOI_GATES.md`, `release/doi_readiness.json`, documentos de `migration/`, validadores e histórico de pull requests.

No follow-up, também foram comparados o CSV canônico e as estruturas `data_resources` da planilha nativa e do `.xlsx` mantidos no Drive.

## Hierarquia documental

1. `WORKFLOW_STATUS.md` registra o estado operacional comprovado e a próxima execução.
2. `IMPLEMENTATION_WORKFLOW.md` descreve a sequência de implementação e dependências.
3. `QUALITY_CORRECTION_WORKFLOW.md` explica a justificativa científica e os checkpoints de reordenação.
4. `FINAL_OBJECTIVES_AND_DOI_GATES.md` define o produto final e os portões de release e DOI.
5. `METHODOLOGY.md` e `CODEBOOK.md` definem interpretação e significado dos campos.
6. `DRIVE_MIRROR_CONTRACT.md` define a geração e verificação dos espelhos do Drive.
7. Contratos JSON, matrizes CSV e validadores são a representação executável das decisões.
8. O Google Drive mantém changelog executivo, histórico e espelhos derivados; não é fonte canônica.

Em caso de divergência, o estado comprovado no GitHub, os contratos executáveis e o CSV canônico prevalecem sobre textos históricos e espelhos.

## Problemas encontrados em 2026-07-20

- `QUALITY_CORRECTION_WORKFLOW.md` e `IMPLEMENTATION_WORKFLOW.md` ainda apresentavam DATA1-BX como incompleto e DATA1-BR como bloqueado, apesar da conclusão interna de BR1–BR5.
- `WORKFLOW_STATUS.md` no branch declarava DATA1-BR-CLOSE concluído antes de PR, CI, merge e changelog.
- `migration/data1br_review_batches.csv` mantinha uma distribuição antiga e incompatível com os contratos reais BR1–BR5; `validate_doi_readiness.py` ainda dependia desse arquivo.
- a primeira fila externa somava número de flags e dimensões, favorecendo lotes com taxonomias mais detalhadas;
- problemas de links, esforço documental, risco científico e decisão de escopo estavam misturados em uma única pontuação;
- uma única URL de evidência por fonte era insuficiente para sustentar identidade, API, licença, formato, resolução, atualização e método;
- `access_protocols` precisava distinguir o uso atual no esquema 0.7.0 da separação futura entre protocolos e ferramentas no esquema 0.8.0.

## Ajustes decididos em 2026-07-20

- remover a matriz antiga de lotes e usar somente `br_batch_registry.json`, contratos BR1–BR5 e suas matrizes;
- separar `scientific_priority_tier` de `execution_wave`;
- usar apenas impacto e risco, comparáveis em todos os lotes, para a prioridade científica;
- tratar links e documentação ausente apenas como critérios operacionais de onda;
- tratar COSMOS em um portão de escopo `G0`, sem pontos artificiais;
- criar `external_review_evidence.csv` em formato longo, permitindo várias evidências por fonte e dimensão;
- manter todas as correções canônicas bloqueadas até evidência oficial, data e revisor;
- atualizar os documentos de estado e os validadores no mesmo PR.

## Follow-up de 2026-07-21 — STATE-SYNC

A nova inspeção confirmou que `WORKFLOW_STATUS.md` estava atualizado, mas os dois workflows secundários ainda preservavam o estado anterior à integração de DATA1-BR-CLOSE. Também identificou divergência entre os arquivos do Drive.

O PR #32 integrou o contrato e o alinhamento documental no commit `f35b2c766043308d9e19751539a2c99972df949b`. O run `29836549232` passou integralmente.

### Correção após concorrência no Drive

Durante o fechamento, outra operação atualizou a planilha nativa e acrescentou ao changelog uma linha declarando sincronização dos dois arquivos. A verificação direta mostrou:

- planilha nativa: 51 recursos × 34 campos, com cabeçalhos canônicos;
- `.xlsx`: 51 recursos × 22 campos no arquivo bruto baixado do Drive;
- a substituição do `.xlsx` por export da planilha nativa falhou duas vezes por proxy interno `407`;
- uma nova linha do changelog corrigiu a declaração anterior e preservou o histórico.

Ações consolidadas:

1. DATA1-BR-CLOSE aparece como `concluído` e DATA1-EXT como `ativo`;
2. W1 é subdividida em W1A–W1C apenas para limitar o tamanho dos PRs;
3. `DRIVE_MIRROR_CONTRACT.md` registra autoridade, fluxo unidirecional, metadados e verificações;
4. `validate_quality_correction_plan.py` exige STATE-SYNC e o diagnóstico separado dos espelhos;
5. STATE-SYNC é encerrado como ciclo de coerência e diagnóstico;
6. o reparo do arquivo bruto é isolado em MIRROR-XLSX e não bloqueia DATA1-EXT;
7. nenhuma linha do CSV, candidato, interface, versão ou portão de DOI é alterado.

## Estado protegido

Nenhum ajuste desta auditoria altera `data/data_resources.csv`, os 51 `resource_id`, os 34 campos, a versão 0.7.0, os candidatos, a interface pública ou a autorização de DOI.
