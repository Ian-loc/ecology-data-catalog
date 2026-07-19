# Workflow de implementação — interface, conteúdo, governança e release

## Objetivo

Melhorar a experiência de descoberta e comparação do catálogo, corrigir ambiguidades documentais e preparar uma primeira versão científica estável e arquivável, sem misturar redesign, revisão científica do CSV e publicação com DOI no mesmo ciclo.

## Princípios

1. busca e decisão do usuário vêm antes da documentação institucional;
2. a página pública é uma interface atualizável; cada versão científica citável deverá ser arquivada como objeto imutável;
3. o CSV em `data/data_resources.csv` é a fonte canônica;
4. o JSON e os metadados exibidos no site são derivados do CSV;
5. a planilha do Google Drive é registro histórico e changelog executivo, não fonte de publicação;
6. mudanças de interface não alteram silenciosamente o conteúdo científico das 51 fontes;
7. nenhuma etapa é marcada como publicada sem evidência do site resultante;
8. a versão `1.0.0` e o DOI somente serão criados após fechamento técnico, científico e documental;
9. o depósito final deverá representar a contribuição principal como **Dataset**;
10. manter apenas `CITATION.cff`, salvo necessidade concreta de `.zenodo.json` identificada em teste;
11. licenças de código e dados devem permanecer materialmente separadas.

## Título oficial

**Ecology Data Catalog: catálogo de fontes de dados ambientais para pesquisa, ensino e extensão**

O título deve ser usado de forma idêntica no site, README, `CITATION.cff`, Zenodo, ORCID, currículo, Lattes e documentação técnica.

## Ciclos de implementação

| Ciclo | Escopo | Estado | Critério de conclusão |
|---|---|---|---|
| UX1 | Arquitetura, linguagem e navegação | em desenvolvimento | busca no hero, navegação consistente, hierarquia de ações corrigida, título padronizado e CSV inalterado |
| UX2 | Filtros e resultados | planejado | filtros essenciais/avançados, chips ativos, ordenação, contagens e estado na URL |
| UX3 | Redesenho dos cards | planejado | cards curtos, estados de acesso claros e detalhes agrupados semanticamente |
| UX4 | Acessibilidade, responsividade e desempenho | planejado | teclado, contraste, mobile, carregamento, HTML e comportamento verificados |
| DATA1 | Correções estruturais do esquema | planejado | `resource_type`, escala geográfica controlada, formatos e citações normalizados |
| DATA2 | Revisão das 51 fontes | planejado | lotes auditáveis com evidência, diff, validação e changelog |
| RELEASE1 | Fechamento documental | em desenvolvimento | título fixado, ORCID incluído, licenças separadas e `CITATION.cff` validado |
| RELEASE2 | Versão estável | bloqueado | todo trabalho não lançado encerrado; site, CSV e metadados verificados |
| DOI | Arquivamento no Zenodo | bloqueado | release `v1.0.0` depositada como Dataset e metadados conferidos antes da publicação |
| POST-DOI | Propagação dos identificadores | bloqueado | DOI de versão e DOI de conceito registrados no repositório, site, ORCID e currículos |

## UX1 — tarefas

- [x] definir título oficial;
- [ ] criar navegação superior consistente;
- [ ] reposicionar a busca no hero;
- [ ] apresentar o benefício principal antes do nome institucional;
- [ ] reduzir botões concorrentes no hero;
- [ ] revisar rótulos de busca e filtros;
- [ ] criar atalhos de busca por temas e recursos frequentes;
- [ ] criar exploração pelas áreas de pesquisa;
- [ ] reduzir a altura do hero e ajustar a hierarquia tipográfica;
- [ ] manter estatísticas, filtros, cards e dados existentes funcionando;
- [ ] validar o build em pull request;
- [ ] registrar o resultado no changelog do GitHub e no Drive.

## RELEASE1 — tarefas documentais permitidas agora

- [x] preservar a classificação principal como `dataset`;
- [ ] incluir ORCID `0000-0003-1164-9318` no `CITATION.cff`;
- [ ] manter `version: "0.7.0"` até a release estável;
- [ ] manter a data efetiva da versão 0.7.0 e usar aspas no YAML;
- [ ] criar `LICENSE-DATA.md` para o CSV, metadados e curadoria original;
- [ ] esclarecer no README o escopo de MIT e CC BY 4.0;
- [ ] não criar `.zenodo.json` sem necessidade comprovada;
- [ ] documentar que o DOI não precisa constar no primeiro arquivo arquivado.

## Condições obrigatórias para `v1.0.0`

1. encerrar o bloco não lançado no changelog;
2. validar o CSV e os artefatos derivados;
3. verificar o site publicado e o commit exibido no build;
4. concluir UX1–UX4 ou registrar explicitamente o que fica para versões posteriores;
5. concluir DATA1 e a revisão mínima necessária das 51 fontes;
6. validar título, autor, ORCID, licenças, versão e data;
7. alterar `CITATION.cff` para `version: "1.0.0"` somente no dia da release;
8. criar tag e GitHub Release `v1.0.0`;
9. testar se a integração GitHub–Zenodo preserva o tipo Dataset;
10. se não preservar, realizar depósito manual classificado como Dataset;
11. conferir arquivos, autor, título, licença, tipo e versão antes de publicar;
12. após atribuição, inserir DOI de versão e DOI de conceito no repositório ativo.

## Citação planejada para a versão estável

Versão específica:

> LARA, Ian. *Ecology Data Catalog: catálogo de fontes de dados ambientais para pesquisa, ensino e extensão*. Versão 1.0.0. Zenodo, 2026. DOI: [DOI da versão].

Apresentação geral:

> LARA, Ian. *Ecology Data Catalog: catálogo de fontes de dados ambientais para pesquisa, ensino e extensão*. Zenodo, 2026. Concept DOI: [DOI de conceito].

## Ordem operacional atual

1. implementar UX1 e RELEASE1 documental na mesma branch, sem alterar o CSV;
2. revisar o diff e executar `python3 scripts/build_catalog.py` no GitHub Actions;
3. integrar apenas após validação automática;
4. verificar o site publicado;
5. registrar o resultado no GitHub e no Drive;
6. iniciar UX2;
7. manter RELEASE2 e DOI bloqueados até o fechamento técnico e científico.
