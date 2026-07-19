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
- O conector disponível confirma runs associados a pull requests, mas não expõe o run disparado por push na `main`. Por isso, o deploy posterior ao merge não pode ser marcado como verificado apenas com a evidência atualmente observável.

## Backlog

| Prioridade | Frente | Estado | Evidência ou critério de conclusão |
|---|---|---|---|
| P0 | Gerar identificação verificável do build | integrado | `build-meta.json` é gerado com versão, commit, data, fontes e campos |
| P0 | Exibir versão e commit publicados | integrado | páginas principal e Sobre consomem `data/build-meta.json` |
| P0 | Impedir versionamento de artefatos derivados | concluído | `.gitignore` cobre JSON, metadados de build e cache Python |
| P0 | Validar alterações em pull request | concluído | PR #3; run 29699990478 concluído com sucesso |
| P0 | Confirmar deploy posterior ao merge | bloqueado | requer evidência do run de push da `main` ou inspeção direta do site publicado |
| P0 | Alinhar registro executivo no Drive | documentado | aba `project_changelog` criada na planilha histórica do projeto |
| P1 | Restaurar classificação controlada do tipo de fonte | planejado | `resource_type` documentado, validado e aplicado às 51 fontes |
| P1 | Separar escala geográfica de descrição territorial | planejado | filtro usa categoria controlada e preserva descrição livre |
| P1 | Normalizar formatos, protocolos e citações | planejado | campos não misturam formatos, visualizações e notas livres |
| P1 | Ampliar validações cruzadas | planejado | inconsistências entre acesso, protocolo, autenticação e evidência bloqueiam o build |
| P1 | Revisar as 51 fontes em lotes auditáveis | planejado | cada lote tem diff, validação e changelog |
| P2 | Criar release formal e tag | planejado | versão estável publicada com release notes |
| P2 | Arquivar no Zenodo e obter DOI | planejado | DOI registrado no site, `CITATION.cff` e Drive |
| P2 | Instituir manutenção periódica | planejado | verificações trimestrais e anuais documentadas |

## Ciclo P0 — resultado

- **PR:** #3 — `Fechar rastreabilidade operacional da versão 0.7.0`
- **Commit integrado:** `a25b3d8b220d4725d14a04dffb84456dcb8dc89a`
- **Validação do PR:** GitHub Actions run `29699990478`, sucesso
- **Drive:** aba `project_changelog` criada em `World_Ecology_Databases_Systems_v0.5`
- **Situação final:** implementação, validação, integração e documentação confirmadas; publicação pós-merge ainda não observável neste ambiente

O P1 não deve ser iniciado como concluído ou publicado enquanto o deploy da `main` permanecer sem evidência verificável.
