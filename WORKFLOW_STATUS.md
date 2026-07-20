# Estado do workflow

## Regra operacional

Uma tarefa só é considerada concluída quando estiver implementada em branch, revisada em pull request, integrada à `main`, validada pelo GitHub Actions e registrada no changelog. Quando afetar o site, a publicação também precisa ser confirmada.

CI verde comprova estrutura e coerência interna. Não comprova, sozinho, que uma fonte externa esteja atual, acessível ou cientificamente correta.

## Limitações atuais

- a publicação só será marcada como confirmada mediante inspeção direta do site ou evidência equivalente;
- a revisão factual exige documentação oficial atual;
- o acesso web de pesquisa não está disponível neste ambiente;
- novas indicações podem ser registradas, mas novas fontes permanecem fora do CSV até a estabilização das 51 atuais;
- candidatos identificados por conhecimento prévio ou URL submetida permanecem em triagem, sem decisão final;
- auditoria interna e seleção de lotes não autorizam elevar confiança nem corrigir o CSV sem evidência externa atual.

## Backlog

| Prioridade | Frente | Estado | Evidência ou critério de conclusão |
|---|---|---|---|
| P0 | Identificação verificável do build | integrado | versão, commit, fontes e campos em `build-meta.json` |
| P0 | Confirmar deploy posterior ao merge | bloqueado | inspeção direta do site ou evidência equivalente |
| UX1–UX4 | Interface, filtros, cards, acessibilidade e desempenho | validado e documentado | PRs #5, #7, #9 e #11 |
| OBJ | Objetivos finais e portões para DOI | concluído | PR #17 |
| DATA1-A | Auditoria e projeto do esquema 0.8.0 | validado e documentado | PR #13 |
| DATA1-B | Matriz inicial de migração | validado e documentado | PR #15 |
| QC0 | Alinhar 14 regras semânticas | validado e documentado | PR #19 |
| SELECT1 | Inclusão, exclusão, duplicidade e lacunas | validado e documentado | PR #19 |
| CAND1 | Fila versionada de candidatos | em desenvolvimento | 18 candidatos; nenhum incluído no CSV |
| DATA1-BX | Completar campos da matriz | projeção canônica concluída | 51 fontes × 5 dimensões carregadas; confiança desconhecida; revisão externa pendente |
| DATA1-BR/BR1 | Revisar primeiro lote de sete casos | auditoria interna concluída; revisão externa bloqueada | contrato, seleção, achados e validador BR1; exige documentação oficial atual para concluir |
| DATA1-BR/BR2–BR5 | Revisar 28 casos restantes | planejado | quatro lotes de sete com os mesmos controles de evidência |
| DATA1-C | Migração atômica para 38 campos | bloqueado | decisões DATA1-B e DATA1-BX revisadas |
| DATA1-D | Validação semântica do esquema final | planejado | 14 regras ativas no CSV 0.8.0 |
| DATA2 | Revisar as 51 fontes no esquema final | planejado | links, acesso, formatos, licença, evidência e data revisados |
| UX5 | Interface dos 38 campos e testes de navegador | em desenvolvimento parcial | resumo público de qualidade criado; adaptação aos 38 campos ainda pendente |
| RELEASE1 | Título, ORCID, licenças e CFF | validado e documentado | PR #5 |
| RELEASE2 | Criar versão 1.0.0 | bloqueado | G1–G10 concluídos e deploy confirmado |
| DOI | Arquivar no Zenodo como Dataset | bloqueado | G1–G12 concluídos e depósito inspecionado |
| RES1 | Faixas de resolução por produto | P3, não bloqueante | tabela auxiliar com evidência e unidades comparáveis |
| EDU1 | Página didática de fenômenos | P3, não bloqueante | conteúdo referenciado e ligado às fontes |
| POST-DOI | Propagar identificadores | bloqueado | DOI de versão e conceito em repositório, site, ORCID e currículos |

## Estado consolidado

- **Versão formal:** 0.7.0;
- **Fontes canônicas:** 51;
- **Campos canônicos:** 34;
- **Fila de candidatos:** 18 registros separados do CSV;
- **Candidatos prioritários de saúde e demografia:** WHO GHO, GHDx, OpenDataSUS, DATASUS TabNet, SIDRA, WPP, EM-DAT, DesInventar, SINITOX e PAHO ENLACE;
- **Repositórios científicos candidatos:** SciELO Data, Zenodo, Harvard Dataverse e re3data;
- **DATA1-B:** 16 registros prontos e 35 em revisão manual;
- **DATA1-BX:** cinco valores atuais carregados para todas as 51 fontes, com confiança `desconhecida` e todas as dimensões ainda pendentes de verificação externa;
- **BR1 selecionado:** CEMADEN, dados.gov.br, MapBiomas, TerraBrasilis, BDQueimadas, Google Earth Engine e Global Forest Watch;
- **BR1 auditoria interna:** concluída, com riscos e dimensões de revisão registrados;
- **BR1 revisão factual:** bloqueada enquanto não houver acesso à documentação oficial atual;
- **Relatório de qualidade:** gerado automaticamente em `data/data_quality_report.json` durante o build;
- **Página inicial:** mostra documentação oficial, evidência revisada por pares e incertezas de acesso/licença;
- **Esquema 0.8.0:** ainda não aplicado;
- **Expansão:** bloqueada;
- **v1.0.0 e DOI:** bloqueados.

## Achados do BR1

As sete fontes são internamente coerentes com ressalvas, mas não estão prontas para migração. Os principais riscos compartilhados são:

- tratar portal, plataforma ou agregador como produtor original dos dados;
- generalizar acesso, licença, formatos e API para todos os produtos;
- misturar protocolos técnicos, ferramentas, catálogos de metadados e formatos de exportação;
- atribuir uma única resolução ou temporalidade a coleções heterogêneas;
- confundir alerta, foco de calor, incêndio, área queimada, desmatamento anual e detecção rápida;
- citar a plataforma sem preservar provedor, coleção, versão, camada e método do produto utilizado.

A decisão conservadora é manter o CSV 0.7.0 sem alterações até que cada dimensão seja confrontada com documentação oficial atual, URL de evidência, data e revisor.

## Interpretação correta do avanço DATA1-BX

A projeção canônica reduz risco de perda e permite comparar sistematicamente cinco dimensões: `data_product_types`, `visualization_types`, `data_sources`, `temporal_resolution` e `access_conditions`. Ela não aumenta a confiança dos valores.

A ferramenta `scripts/load_data1bx_from_canonical.py` garante que a matriz continue correspondente ao CSV 0.7.0 enquanto a revisão externa não começa. O validador `scripts/validate_br1_matrix.py` impede que uma seleção bloqueada seja apresentada como revisão factual concluída.

## Qualidade e apresentação

O build produz indicadores de documentação oficial, evidência revisada por pares, incerteza de acesso, licença variável e placeholders por campo. Esses indicadores descrevem a qualidade do catálogo; não certificam todos os produtos de cada plataforma.

## Resolução e página didática

### RES1

Registrar resolução no nível de produto, distinguindo célula raster, escala cartográfica, precisão de coordenadas, resolução temporal e limite de zoom. Não inferir resolução a partir do visualizador.

### EDU1

Criar página separada para explicar fenômenos, formas de medição, tipos de dados, limitações e fontes relacionadas.

RES1 e EDU1 permanecem não bloqueantes para v1.0.0 e DOI, salvo quando revelarem erro factual no catálogo.

## Checkpoints de reordenação

Reavaliar a ordem após:

1. BR1 — seleção e auditoria interna concluídas; revisão externa bloqueada;
2. cada lote BR2–BR5;
3. migração 0.8.0;
4. primeiros lotes DATA2;
5. testes funcionais da interface.

## Próxima execução

1. executar revisão externa BR1 por produto quando houver acesso atual à documentação oficial;
2. enquanto esse acesso não estiver disponível, selecionar BR2 entre os 28 casos manuais restantes e registrar somente auditoria interna;
3. não alterar confiança, evidência, data ou CSV com base em inferência;
4. manter os 18 candidatos fora do CSV até um ciclo de expansão autorizado;
5. preservar CSV 51 × 34, versão 0.7.0, esquema 0.8.0 não aplicado e DOI bloqueado.

Consulte `migration/br1_contract.json`, `migration/br1_review_matrix.csv`, `migration/data1bx_contract.json`, `migration/data1bx_migration_matrix.csv`, `QUALITY_CORRECTION_WORKFLOW.md`, `SELECTION_AND_COVERAGE_POLICY.md`, `FINAL_OBJECTIVES_AND_DOI_GATES.md` e `candidates/source_candidates.csv`.
