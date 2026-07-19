# Estado do workflow

## Regra operacional

Uma tarefa só é considerada concluída quando estiver:

1. implementada em branch;
2. revisada em pull request;
3. integrada à `main`;
4. validada pelo GitHub Actions;
5. publicada, quando afetar o site;
6. registrada no changelog do GitHub e no registro executivo do Google Drive.

Os estados usados são: `planejado`, `em desenvolvimento`, `em revisão`, `integrado`, `validado`, `publicado`, `documentado` e `concluído`.

## Limitação atual

GitHub Issues está desativado neste repositório. O backlog abaixo é, portanto, o registro versionado autoritativo das pendências até que Issues seja habilitado.

## Backlog

| Prioridade | Frente | Estado | Critério de conclusão |
|---|---|---|---|
| P0 | Identificar versão e commit efetivamente publicados | em desenvolvimento | site exibe versão, commit e dimensões produzidos pelo próprio deploy |
| P0 | Impedir versionamento de JSON e metadados derivados | em desenvolvimento | `.gitignore` cobre os artefatos gerados |
| P0 | Confirmar deploy posterior ao merge | planejado | workflow da `main` conclui validação e deploy com sucesso |
| P0 | Alinhar registro executivo no Drive | planejado | Drive registra versão, commit, PR, workflow run e situação do deploy |
| P1 | Restaurar classificação controlada do tipo de fonte | planejado | `resource_type` documentado, validado e aplicado às 51 fontes |
| P1 | Separar escala geográfica de descrição territorial | planejado | filtro usa categoria controlada e preserva descrição livre |
| P1 | Normalizar formatos, protocolos e citações | planejado | campos não misturam formatos, visualizações e notas livres |
| P1 | Ampliar validações cruzadas | planejado | inconsistências entre acesso, protocolo, autenticação e evidência bloqueiam o build |
| P1 | Revisar as 51 fontes em lotes auditáveis | planejado | cada lote tem diff, validação e changelog |
| P2 | Criar release formal e tag | planejado | versão estável publicada com release notes |
| P2 | Arquivar no Zenodo e obter DOI | planejado | DOI registrado no site, `CITATION.cff` e Drive |
| P2 | Instituir manutenção periódica | planejado | verificações trimestrais e anuais documentadas |

## Ciclo atual

**Branch:** `agent/p0-operational-closure`

**Escopo:** fechamento operacional da versão 0.7.0, sem alterar o conteúdo científico das 51 fontes.

**Mudanças previstas:**

- gerar `data/build-meta.json` no build;
- exibir versão, commit e dimensões no site;
- ignorar artefatos derivados;
- validar a branch em pull request;
- integrar e confirmar o deploy;
- registrar o resultado no Google Drive.
