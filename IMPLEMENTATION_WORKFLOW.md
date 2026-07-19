# Workflow de implementação — interface, dados, governança e release

## Objetivo

Melhorar a descoberta e comparação de fontes, corrigir ambiguidades científicas e preparar uma versão estável e arquivável sem misturar redesign, migração, revisão externa e DOI no mesmo ciclo.

O detalhamento das correções resultantes da auditoria transversal está em [QUALITY_CORRECTION_WORKFLOW.md](QUALITY_CORRECTION_WORKFLOW.md).

## Princípios

1. `data/data_resources.csv` é a fonte canônica;
2. JSON e metadados do site são derivados do CSV;
3. o Drive é changelog executivo, não fonte de publicação;
4. CI verde comprova estrutura e coerência interna, não verdade factual externa;
5. nenhuma fonte é declarada revisada sem inspeção de evidência atual;
6. nenhuma etapa é marcada como publicada sem evidência do site resultante;
7. a expansão não precede a estabilização das 51 fontes atuais;
8. `1.0.0` e DOI somente serão criados após fechamento técnico, científico e documental;
9. o depósito final representa o produto como **Dataset**;
10. licenças de código e dados permanecem separadas;
11. melhorias não bloqueantes devem ser entregues sem ampliar o escopo da release estável.

## Título oficial

**Ecology Data Catalog: catálogo de fontes de dados ambientais para pesquisa, ensino e extensão**

## Ciclos concluídos

| Ciclo | Resultado | Evidência |
|---|---|---|
| UX1 | arquitetura, linguagem e navegação | PR #5; run 29700737238 |
| UX2 | filtros, resultados e URLs compartilháveis | PR #7; run 29701061221 |
| UX3 | cards orientados à decisão | PR #9; run 29701341054 |
| UX4 | acessibilidade estrutural e desempenho | PR #11; run 29702280394 |
| DATA1-A | auditoria e proposta de esquema 0.8.0 | PR #13; run 29702732587 |
| DATA1-B | matriz inicial de migração | PR #15; run 29703654373 |
| OBJ | objetivos finais e portões para DOI | PR #17; run 29704132742 |

## Correção de rota após auditoria transversal

A auditoria identificou três problemas que precisam ser resolvidos antes de BR1:

1. a documentação descrevia 14 regras semânticas, mas o contrato JSON listava 11;
2. a matriz DATA1-B não cobria todos os campos cuja normalização foi prometida;
3. faltavam critérios formais de inclusão, exclusão, duplicidade e análise de lacunas.

Por isso, a ordem anterior foi alterada. BR1 não começa antes de QC0, SELECT1 e DATA1-BX.

## Ordem operacional atual

| Ordem | Ciclo | Prioridade | Estado | Critério de conclusão |
|---:|---|---|---|---|
| 1 | QC0 | P0 | em desenvolvimento | auditoria, JSON e CI usam exatamente as mesmas 14 regras |
| 2 | SELECT1 | P0 | em desenvolvimento | política de seleção e cobertura integrada e validada |
| 3 | DATA1-BX | P0 | planejado | matriz expandida para todos os campos-alvo de normalização |
| 4 | DATA1-BR | P0 | bloqueado por DATA1-BX | 35 casos revisados com evidência oficial |
| 5 | DATA1-C | P0 | bloqueado | 51 linhas migradas atomicamente para 38 campos |
| 6 | DATA1-D | P0 | planejado | regras cruzadas ativas no CSV final |
| 7 | DATA2 | P0 | planejado | 51 fontes auditadas no esquema final |
| 8 | UX5 | P1 | planejado | 38 campos exibidos e testes funcionais de navegador aprovados |
| 9 | RELEASE2 | P1 | bloqueado | v1.0.0 preparada e deploy confirmado |
| 10 | DOI | P1 | bloqueado | G1–G12 concluídos e depósito inspecionado |
| 11 | RES1 | P3 | não bloqueante | exemplos de resolução por produto documentados |
| 12 | EDU1 | P3 | não bloqueante | página didática referenciada e ligada ao catálogo |

## QC0 — alinhamento semântico

O contrato 0.8.0 deve exigir exatamente 14 regras:

1. software de publicação usa geografia não aplicável;
2. escopo global é coerente com cobertura do Brasil ou possui exceção;
3. escopo não aplicável exige cobertura não aplicável;
4. acesso programático positivo exige protocolo ou ferramenta;
5. acesso programático negativo não admite protocolo positivo sem exceção;
6. autenticação positiva exige condição correspondente;
7. download gratuito exige URL de acesso;
8. formatos não contêm protocolos ou visualizações;
9. visualizações não contêm formatos ou protocolos;
10. protocolos não contêm pacotes ou clientes;
11. URL de citação usa HTTPS;
12. listas são únicas e normalizadas;
13. DOI de evidência não é identificador da fonte;
14. placeholders não coexistem com valores positivos.

## SELECT1 — política de seleção

A expansão futura usa [SELECTION_AND_COVERAGE_POLICY.md](SELECTION_AND_COVERAGE_POLICY.md), que define:

- inclusão e exclusão;
- duplicidade, sucessão e versões regionais;
- relação entre agregador e provedor;
- fila de candidatos separada do CSV;
- matriz de lacunas temática, geográfica, institucional e de acesso.

Até DATA2, novas fontes podem ser registradas como candidatas, mas não publicadas no CSV canônico.

## DATA1-BX — completar a matriz

A matriz atual cobre:

- `resource_type`;
- `geographic_scope`;
- `data_formats`;
- `access_protocols`;
- `access_tools`;
- `institutional_status`;
- `citation_guidance_url`.

Antes da revisão BR1, ela também deve cobrir:

- `data_product_types`;
- `visualization_types`;
- `data_sources`;
- `temporal_resolution`;
- `access_conditions`.

Cada proposta precisa de confiança, justificativa, exceção e status. Nenhum campo pode ser declarado normalizado apenas porque possui texto não vazio.

## DATA1-BR — revisão dos 35 casos

Para cada caso:

1. confrontar proposta e documentação oficial atual;
2. registrar quais campos a evidência sustenta;
3. separar formato, protocolo, ferramenta e visualização;
4. confirmar tipo, escala, situação institucional e orientação de citação;
5. preservar incerteza quando a fonte não documentar o aspecto;
6. atualizar confiança, justificativa, exceção e estado;
7. manter `last_verified` vinculado à revisão efetivamente realizada.

## DATA1-C — migração atômica 0.8.0

Somente após 51 registros prontos:

1. atualizar cabeçalho para 38 campos;
2. migrar as 51 linhas em uma única branch;
3. atualizar codebook, metodologia, scripts e interface;
4. preservar IDs e conteúdo científico;
5. atualizar `CITATION.cff` para 0.8.0 somente junto à migração;
6. não criar DOI.

## DATA1-D e DATA2

DATA1-D implementa as 14 regras contra o CSV final. DATA2 revisa as 51 fontes no esquema estabilizado, verificando identidade, acesso, formatos, API, autenticação, licença, cobertura, evidência, limitações e data.

## RES1 — resolução por produto

A resolução detalhada pertence principalmente ao produto, não à fonte. Uma tabela auxiliar futura registrará resolução mais fina e mais grosseira apenas quando forem comparáveis e oficialmente documentadas.

Não inferir resolução pelo zoom de mapas. Distinguir:

- célula raster;
- escala cartográfica;
- precisão de coordenadas;
- resolução temporal;
- limite de exibição do visualizador.

RES1 não bloqueia v1.0.0 ou DOI, salvo correção de valor atual incorreto.

## EDU1 — página didática

Página separada para explicar fenômenos, métodos de observação, tipos de dados, incertezas e fontes relacionadas. Temas iniciais: clima, biodiversidade, fragmentação, carbono, solos, uso da terra, agroflorestas, sistemas alimentares e sensoriamento remoto.

EDU1 não bloqueia v1.0.0 ou DOI e deve começar depois de DATA2 ou com capacidade editorial separada.

## Checkpoints

Reavaliar prioridade e ordem após:

- QC0 + SELECT1;
- DATA1-BX;
- cada lote BR1–BR5;
- migração 0.8.0;
- primeiros lotes DATA2;
- testes funcionais da interface.

## Condições para v1.0.0 e DOI

A versão estável exige esquema final, migração sem perda, 51 fontes revisadas, CI sem inconsistências, interface funcional, documentação coerente e deploy confirmado. O DOI exige adicionalmente tag/release imutável e inspeção do depósito Dataset, conforme [FINAL_OBJECTIVES_AND_DOI_GATES.md](FINAL_OBJECTIVES_AND_DOI_GATES.md).
