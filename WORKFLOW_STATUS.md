# Estado do workflow

## Regra operacional

Uma tarefa só é considerada concluída quando estiver:

1. implementada em branch;
2. revisada em pull request;
3. integrada à `main`;
4. validada pelo GitHub Actions;
5. publicada, quando afetar o site;
6. registrada no changelog do GitHub e no registro executivo do Google Drive.

Os estados usados são: `planejado`, `em desenvolvimento`, `em revisão`, `integrado`, `validado`, `publicado`, `documentado`, `bloqueado` e `concluído`.

## Limitações atuais

- GitHub Issues está desativado neste repositório; este arquivo é o backlog versionado autoritativo.
- O conector disponível confirma runs associados a pull requests, mas não expõe o run disparado por push na `main`. O deploy precisa ser conferido por evidência do site ou por outra forma observável.

## Backlog

| Prioridade | Frente | Estado | Evidência ou critério de conclusão |
|---|---|---|---|
| P0 | Identificação verificável do build | integrado | `build-meta.json` contém versão, commit, data, fontes e campos |
| P0 | Impedir versionamento de artefatos derivados | concluído | `.gitignore` cobre JSON, metadados de build e cache Python |
| P0 | Confirmar deploy posterior ao merge | bloqueado | requer inspeção direta do site ou evidência do run de push da `main` |
| UX1 | Arquitetura, linguagem e navegação | em desenvolvimento | branch implementada, CSV inalterado; falta PR, validação, merge e publicação |
| UX2 | Filtros e resultados | planejado | filtros essenciais/avançados, chips ativos, ordenação e estado na URL |
| UX3 | Redesenho dos cards | planejado | cards curtos, estados claros e detalhes agrupados |
| UX4 | Acessibilidade, responsividade e desempenho | planejado | teclado, contraste, mobile, carregamento e testes verificados |
| DATA1 | Restaurar `resource_type` e escala controlada | planejado | esquema, CSV, codebook, validação e interface atualizados |
| DATA1 | Normalizar formatos, protocolos e citações | planejado | campos não misturam formatos, visualizações e notas livres |
| DATA1 | Ampliar validações cruzadas | planejado | inconsistências semânticas bloqueiam o build |
| DATA2 | Revisar as 51 fontes em lotes auditáveis | planejado | cada lote tem evidência, diff, validação e changelog |
| RELEASE1 | Título, ORCID, licenças e CFF | em desenvolvimento | implementados na branch; falta validação e integração |
| RELEASE2 | Criar versão `1.0.0` | bloqueado | trabalho não lançado encerrado e site/CSV/metadados verificados |
| DOI | Arquivar no Zenodo como Dataset | bloqueado | release estável publicada e metadados conferidos |
| POST-DOI | Propagar DOI de versão e conceito | bloqueado | repositório, site, ORCID e currículos atualizados |

## Ciclo atual — UX1 + RELEASE1 documental

- **Branch:** `agent/ux1-information-architecture`
- **Escopo:** reorganização da interface e preparação documental, sem alterar `data/data_resources.csv`.
- **Título oficial:** `Ecology Data Catalog: catálogo de fontes de dados ambientais para pesquisa, ensino e extensão`.
- **Implementado:** navegação, busca no hero, atalhos, exploração por áreas, linguagem revisada, título padronizado, ORCID, `LICENSE-DATA.md`, workflow de release e validação de frontend.
- **Pendente:** abrir PR, validar CI, revisar diff final, integrar, verificar o site e registrar o resultado no Drive.
- **DOI:** não deve ser criado neste ciclo.

Consulte `IMPLEMENTATION_WORKFLOW.md` para a sequência completa até a release estável e o Zenodo.
