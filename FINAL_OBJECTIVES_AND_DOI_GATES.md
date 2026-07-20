# Objetivos finais e critérios obrigatórios antes do DOI

## 1. Produto final

O **Ecology Data Catalog: catálogo de fontes de dados ambientais para pesquisa, ensino e extensão** será um conjunto de dados curado, versionado e citável para localizar, comparar e avaliar fontes ambientais. A unidade de registro é uma fonte ou infraestrutura, não um dataset individual.

## 2. Objetivo geral

Disponibilizar catálogo público, verificável e reutilizável sobre ecologia, biodiversidade, clima, carbono, solo, vegetação, espécies, biosfera e temas relacionados, apoiando uso responsável em pesquisa, ensino e extensão.

## 3. Objetivos específicos finais

1. **Descoberta:** localizar fontes por tema, cobertura, formato e acesso.
2. **Comparação:** comparar função, escala, formatos, protocolos, ferramentas e situação institucional.
3. **Avaliação científica:** registrar uso, limitações, evidência e data.
4. **Transparência:** separar autodescrição, classificação curatorial e evidência.
5. **Reprodutibilidade:** manter CSV, contratos, CI e histórico.
6. **Acessibilidade:** oferecer interface responsiva e navegável.
7. **Citação e preservação:** criar release estável, autoria, licença e DOI consistentes.
8. **Manutenção sustentável:** revisar e incluir fontes por lotes sem duplicar GitHub e Drive.

## 4. Limites deliberados

O catálogo não hospeda todos os datasets, não substitui documentação ou termos, não garante qualidade homogênea, não atribui DOI genérico a infraestruturas, não registra cada produto como linha e não certifica adequação metodológica universal.

Recursos bibliométricos ou editoriais sem dados ambientais diretos exigem decisão explícita de elegibilidade; não são incluídos ou excluídos automaticamente.

## 5. Definição mínima de completude científica

Uma fonte completa possui identidade e tipo separados, descrição, URL oficial, áreas e palavras-chave, produtos e formatos sem mistura, cobertura e escala coerentes, download e acesso programático, protocolo ou ferramenta quando aplicável, responsável, situação institucional, uso, limitações, evidência, data ISO e ausência de contradições bloqueantes.

Valores desconhecidos são permitidos quando explícitos e justificados. Uma URL não é presumida como evidência para todos os campos; evidências externas são registradas por afirmação e dimensão.

## 6. Critérios de qualidade da versão 1.0.0

### 6.1 Estrutura e dados

- 38 campos estabilizados;
- 51 IDs preservados;
- nenhuma decisão de migração pendente;
- exceções resolvidas;
- 14 regras ativas;
- CSV, JSON e interface consistentes.

### 6.2 Auditoria das fontes

- 51 fontes revisadas no esquema final;
- links, acesso, formatos, protocolos, ferramentas, Brasil e licenças conferidos;
- evidências, datas e revisores registrados;
- incertezas preservadas;
- duplicidades, versões e escopo resolvidos.

### 6.3 Interface pública

- busca, filtros, ordenação e URLs compartilháveis funcionais;
- 38 campos disponíveis;
- acessibilidade e responsividade validadas;
- versão e commit públicos;
- deploy confirmado.

### 6.4 Documentação e governança

- README, metodologia, codebook, workflows, licenças e CFF coerentes;
- changelog encerrado;
- GitHub canônico e Drive histórico executivo;
- inclusão, revisão e correção documentadas;
- licenças de código e dados separadas.

### 6.5 Arquivamento e citação

- `CITATION.cff` 1.0.0 somente na release;
- autoria `Lara, Ian` e ORCID `0000-0003-1164-9318`;
- tag e release `v1.0.0`;
- depósito **Dataset** inspecionado;
- DOI de versão e conceito propagados.

## 7. Portões obrigatórios para DOI

1. **G1 — escopo científico:** objetivos, unidade e limites.
2. **G2 — esquema:** 38 campos e codebook final.
3. **G3 — migração:** 51 registros sem perda ou decisão pendente.
4. **G4 — validação semântica:** 14 regras no CSV final.
5. **G5 — revisão das fontes:** 51 registros auditados.
6. **G6 — qualidade de acesso:** links e condições verificados.
7. **G7 — interface:** campos, filtros e acessibilidade.
8. **G8 — publicação:** deploy confirmado.
9. **G9 — documentação:** documentação e changelog coerentes.
10. **G10 — metadados de citação:** autor, ORCID, título, versão e data.
11. **G11 — release imutável:** tag e release v1.0.0.
12. **G12 — inspeção do depósito:** tipo Dataset, arquivos e metadados.

## 8. Regra de decisão

- **GO para v0.8.0:** após revisão externa suficiente dos 35 casos e migração validada.
- **GO para v1.0.0:** após DATA1, revisão das 51 fontes, interface e publicação verificável.
- **GO para DOI:** após G1–G12 concluídos.
- **NO-GO:** falha de CI, link crítico não verificado, decisão pendente, divergência entre artefatos ou ausência de evidência de deploy.

## 9. Estado atual

- versão 0.7.0;
- UX1–UX4, DATA1-A, DATA1-B, QC0, SELECT1 e projeção DATA1-BX concluídos;
- BR1–BR5 concluídos como auditoria interna;
- DATA1-BR-CLOSE integrado e validado por PR #29, run `29778282362`;
- DATA1-EXT ativo, começando por G0 e W1;
- tabela externa de evidências ainda vazia;
- esquema 0.8.0 não aplicado;
- v1.0.0 e DOI bloqueados.
