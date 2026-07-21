# Workflow de correções de qualidade

## Objetivo

Corrigir fragilidades antes de migrar para 0.8.0, expandir fontes ou preparar v1.0.0 e DOI. Controle de processo não substitui verificação científica: CI verde comprova estrutura, não atualidade ou correção de links, APIs, licenças, formatos e resoluções.

## Regras de prioridade

1. corrigir contradições entre documentos, contratos e validadores;
2. revisar as 51 fontes atuais antes de expandir;
3. separar risco científico, esforço operacional e decisão de escopo;
4. registrar evidência por afirmação e dimensão;
5. não alterar CSV, versão ou DOI enquanto os portões estiverem bloqueados;
6. reavaliar a ordem após cada ciclo relevante;
7. manter RES1 e EDU1 como enriquecimentos não bloqueantes;
8. tratar planilha nativa e `.xlsx` como espelhos derivados, conforme `DRIVE_MIRROR_CONTRACT.md`.

## Ordem operacional atual

| Ordem | Ciclo | Estado | Produto/critério |
|---:|---|---|---|
| 1 | QC0 | concluído | 14 regras semânticas alinhadas |
| 2 | SELECT1 | concluído | política de seleção e cobertura |
| 3 | DATA1-BX | projeção concluída | 51 × 5 dimensões; confiança desconhecida |
| 4 | DATA1-BR | auditoria interna concluída | BR1–BR5 cobrem 35 casos |
| 5 | DATA1-BR-CLOSE | concluído | fila comparável e evidência longa |
| 6 | STATE-SYNC | concluído | estados coerentes, contrato e verificação dos espelhos |
| 7 | MIRROR-XLSX | bloqueado por upload | substituir o espelho histórico de 22 campos |
| 8 | DATA1-EXT | ativo | revisão factual por ondas |
| 9 | G0 | concluído | elegibilidade do Project COSMOS |
| 10 | W1A | ativo | TerraBrasilis e Google Earth Engine Data Catalog |
| 11 | W1B | planejado | SiBBr, BDiA e HidroWeb |
| 12 | W1C | planejado | SIRENE e Global Carbon Atlas |
| 13 | DATA1-C | bloqueado | migração atômica para 38 campos |
| 14 | DATA1-D | planejado | 14 regras no CSV final |
| 15 | DATA2 | planejado | revisão das 51 fontes no esquema final |
| 16 | UX5 | parcial | 38 campos e testes funcionais |
| 17 | RELEASE2 | bloqueado | v1.0.0 e deploy confirmado |
| 18 | DOI | bloqueado | G1–G12 concluídos |
| 19 | RES1 | P3 | resolução por produto |
| 20 | EDU1 | P3 | página didática referenciada |

## G0 — decisão de escopo

O Project COSMOS cumpre a unidade de seleção como infraestrutura bibliométrica de informação climática. A decisão mantém o recurso no catálogo principal, sem tratá-lo como fonte de medições ambientais.

A decisão exige:

- metodologia e governança identificáveis;
- função estruturada de descoberta e análise bibliométrica;
- utilidade distinta para pesquisa e ensino climático;
- declaração de que a base integral não é aberta;
- não generalização da licença do conteúdo público para a base integral;
- não comparação com disponibilidade de dados ambientais empíricos;
- preservação do CSV 0.7.0 até ciclo autorizado.

G0 resolveu elegibilidade, não todos os atributos factuais. A tabela de evidências permanece vazia porque nenhuma nova alegação canônica foi verificada ou alterada neste portão.

O PR #34, commit `6f48a7265be2757eac223c6e768e98faa2579da8`, passou no run `29838354760` e foi registrado no changelog. G0 está concluído; W1A está ativo. O documento completo é `G0_COSMOS_SCOPE_DECISION.md`.

## STATE-SYNC

A inspeção confirmou duas classes de divergência:

- workflows secundários ainda indicavam DATA1-BR-CLOSE como pendente, embora `WORKFLOW_STATUS.md` e a `main` comprovassem seu encerramento;
- os dois arquivos do Drive não estavam no mesmo estado.

Estado verificado após os PRs #32 e #33:

- GitHub: 51 × 34;
- planilha nativa: 51 × 34, com os 34 cabeçalhos canônicos;
- `.xlsx`: 51 × 22;
- a substituição do `.xlsx` foi tentada duas vezes e falhou por proxy `407`;
- o changelog recebeu uma linha corretiva para impedir declaração indevida de sincronização total.

STATE-SYNC está concluído como ciclo de coerência, contrato e diagnóstico. O reparo do arquivo bruto permanece isolado em MIRROR-XLSX e não bloqueia a revisão científica.

## DATA1-BR-CLOSE

A primeira proposta de fila somava quantidade de flags e dimensões. Isso era inadequado porque BR1–BR5 foram descritos com granularidades diferentes.

O modelo corrigido usa:

- `scientific_priority_tier`: somente impacto e risco científico;
- `execution_wave`: escopo, papéis dos links, documentação ausente e sequência;
- `external_review_evidence.csv`: várias evidências por fonte, dimensão e afirmação.

## DATA1-EXT

Cada evidência factual deve registrar:

- fonte e dimensão revisada;
- afirmação e valor atual;
- valor observado oficialmente;
- URL e tipo de evidência;
- data, revisor e organização;
- suporte ao valor atual;
- ação e valor propostos;
- limitações.

Documentação oficial sustenta API, formato, licença e autenticação. Literatura revisada por pares confronta identidade, uso efetivo, limitações e interpretação; não substitui documentação técnica atual.

A onda W1 é executada em três PRs pequenos, sem alterar sua composição:

- W1A: TerraBrasilis e Google Earth Engine Data Catalog;
- W1B: SiBBr, BDiA e HidroWeb;
- W1C: SIRENE e Global Carbon Atlas.

O checkpoint científico ocorre após o conjunto W1A–W1C, não após cada arquivo isolado.

## Migração e revisão final

DATA1-C somente começa quando decisões críticas estiverem resolvidas. A migração deve preservar 51 IDs, todo o conteúdo científico e produzir 38 campos. DATA1-D ativa as 14 regras no CSV final. DATA2 revisa as 51 fontes no esquema estabilizado.

## Espelhamento do Drive

Não se deve copiar manualmente alterações entre GitHub, planilha nativa e `.xlsx`.

- o CSV em `main` é a autoridade;
- a planilha nativa 51 × 34 é o espelho operacional verificado;
- o `.xlsx` 51 × 22 permanece histórico até substituição e nova comparação;
- a falha do upload deve ser tratada como incidente operacional, não como evidência de sincronização;
- a regeneração completa 51 × 38 ocorre após DATA1-C e DATA1-D.

## RES1 — resolução por produto

Não é cientificamente seguro inferir resolução pelo zoom de um visualizador. Distinguir célula raster, escala cartográfica, precisão de coordenadas, suporte espacial, resolução temporal e limite de exibição.

A tabela futura `data/product_resolution_examples.csv` deve registrar produto, tipo de resolução, valores mais fino e mais grosseiro, unidade ou escala, versão, evidência, data, confiança e notas. Faixas só podem ser comparadas quando usam a mesma dimensão e unidade.

RES1 é não bloqueante para v1.0.0 e DOI, salvo quando revelar erro factual no valor atual.

## EDU1 — página didática

A página didática deve explicar fenômeno, medição, tipos de dados, limitações, fontes relacionadas e referências. Linguagem acessível não autoriza simplificação enganosa ou inferência causal por visualização.

EDU1 é não bloqueante para v1.0.0 e DOI e deve começar após DATA2 ou com capacidade editorial separada.

## Checkpoints de reordenação

Reavaliar após W1A–W1C, eventual reparo MIRROR-XLSX, migração 0.8.0, regeneração dos espelhos, primeiros lotes DATA2 e testes funcionais. Uma tarefa sobe quando bloqueia dependências, evita perda, corrige informação pública ou reduz retrabalho; desce quando é apenas enriquecimento ou pode ser entregue com segurança depois.

## Estado protegido

- versão formal 0.7.0;
- CSV 51 × 34 até DATA1-C;
- `doi_allowed = false`;
- nenhuma nova fonte entra diretamente no catálogo;
- candidatos permanecem fora do CSV;
- planilha nativa e `.xlsx` não substituem o CSV canônico;
- G0 não autoriza alteração automática do CSV;
- RES1 e EDU1 não desbloqueiam nem bloqueiam o DOI.
