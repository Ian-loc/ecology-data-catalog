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
- O conector disponível confirma runs associados a pull requests, mas não expõe o run disparado por push na `main`.
- A tentativa de inspeção externa do GitHub Pages não obteve acesso de rede ao domínio. Portanto, publicação não é marcada como confirmada sem evidência direta do site.

## Backlog

| Prioridade | Frente | Estado | Evidência ou critério de conclusão |
|---|---|---|---|
| P0 | Identificação verificável do build | integrado | `build-meta.json` contém versão, commit, data, fontes e campos |
| P0 | Impedir versionamento de artefatos derivados | concluído | `.gitignore` cobre JSON, metadados de build e cache Python |
| P0 | Confirmar deploy posterior ao merge | bloqueado | requer inspeção direta do site ou evidência do run de push da `main` |
| UX1 | Arquitetura, linguagem e navegação | validado e documentado | PR #5 integrado; run 29700737238 concluído com sucesso; Drive atualizado |
| UX1 | Confirmar publicação da nova interface | bloqueado | site deve exibir o commit `678d7e716bf31c856bc70c3b028b23457c6f537f` no build |
| UX2 | Filtros e resultados | planejado | filtros essenciais/avançados, chips ativos, ordenação e estado na URL |
| UX3 | Redesenho dos cards | planejado | cards curtos, estados claros e detalhes agrupados |
| UX4 | Acessibilidade, responsividade e desempenho | planejado | teclado, contraste, mobile, carregamento e testes verificados |
| DATA1 | Restaurar `resource_type` e escala controlada | planejado | esquema, CSV, codebook, validação e interface atualizados |
| DATA1 | Normalizar formatos, protocolos e citações | planejado | campos não misturam formatos, visualizações e notas livres |
| DATA1 | Ampliar validações cruzadas | planejado | inconsistências semânticas bloqueiam o build |
| DATA2 | Revisar as 51 fontes em lotes auditáveis | planejado | cada lote tem evidência, diff, validação e changelog |
| RELEASE1 | Título, ORCID, licenças e CFF | validado e documentado | PR #5 integrado, CI aprovado e Drive atualizado |
| RELEASE2 | Criar versão `1.0.0` | bloqueado | trabalho não lançado encerrado e site/CSV/metadados verificados |
| DOI | Arquivar no Zenodo como Dataset | bloqueado | release estável publicada e metadados conferidos |
| POST-DOI | Propagar DOI de versão e conceito | bloqueado | repositório, site, ORCID e currículos atualizados |

## Ciclo UX1 + RELEASE1 documental — resultado

- **PR:** #5 — `Reorganizar interface e preparar governança da release`;
- **Commit integrado:** `678d7e716bf31c856bc70c3b028b23457c6f537f`;
- **Validação:** GitHub Actions run `29700737238`, sucesso;
- **Conteúdo científico:** `data/data_resources.csv` não foi alterado;
- **Interface:** navegação, busca no hero, atalhos, exploração por áreas, linguagem e hierarquia visual implementadas;
- **Governança:** título oficial, ORCID, licença de dados separada e workflow até DOI implementados;
- **Drive:** fase registrada na aba `project_changelog`;
- **Publicação:** ainda não confirmada por evidência direta do site;
- **DOI:** não criado e permanece bloqueado.

## Próximo ciclo autorizado

O próximo ciclo técnico é **UX2 — filtros e resultados**. Ele pode ser desenvolvido em branch própria, mas não deve ser marcado como publicado enquanto a evidência de deploy permanecer ausente.

Consulte `IMPLEMENTATION_WORKFLOW.md` para a sequência completa até a release estável e o Zenodo.
