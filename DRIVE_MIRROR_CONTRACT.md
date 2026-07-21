# Contrato de espelhamento do catálogo no Google Drive

## Finalidade

Este documento define como o catálogo canônico do GitHub deve ser representado nos dois arquivos de apoio mantidos no Google Drive:

- planilha nativa `World_Ecology_Databases_Systems_v0.5`;
- arquivo `World_Ecology_Databases_Systems_v0.5.xlsx`.

Esses arquivos facilitam consulta, histórico e interoperabilidade. Eles não são fontes independentes de publicação e não podem substituir `data/data_resources.csv`.

## Autoridade e direção do fluxo

1. `data/data_resources.csv` na branch `main` é a única fonte canônica dos registros publicados;
2. contratos JSON, validadores e documentação normativa definem a interpretação do esquema;
3. JSON e site são produtos derivados do CSV;
4. planilha nativa e `.xlsx` são espelhos derivados do mesmo CSV;
5. alterações manuais nos espelhos não retornam automaticamente ao GitHub;
6. qualquer proposta nascida no Drive deve entrar no fluxo de candidato, evidência, branch, pull request e validação antes de alcançar o CSV.

Fluxo autorizado:

`CSV em main → validação → artefatos do site → espelho nativo e .xlsx → verificação do espelho → changelog`

## Estado verificado em 2026-07-21

- GitHub: versão 0.7.0, 51 recursos e 34 campos;
- planilha nativa: aba `data_resources` verificada com 51 recursos e os 34 campos canônicos, na ordem correta;
- arquivo `.xlsx`: download bruto verificado com 51 recursos e 22 campos históricos;
- o changelog chegou a declarar que os dois arquivos estavam sincronizados; uma linha posterior corrigiu essa afirmação;
- a substituição do `.xlsx` pelo export da planilha nativa foi tentada duas vezes e falhou por erro interno de proxy `407` no upload.

Conclusão: a planilha nativa é o espelho operacional 0.7.0 atualmente verificado. O `.xlsx` permanece um espelho histórico incompleto e não deve ser tratado como sincronizado.

## Metadados obrigatórios de cada espelho

Toda regeneração deve registrar, em aba própria ou bloco claramente identificado:

- `catalog_version`;
- `schema_version`;
- `source_repository`;
- `source_branch`;
- `source_commit`;
- `source_file`;
- `generated_at`;
- `generated_by`;
- número de registros;
- número de campos;
- resultado da validação;
- observação explícita de que o arquivo é derivado e não canônico.

## Regras de conteúdo

1. `data_resources` deve reproduzir exatamente a ordem de colunas e as 51 linhas do CSV canônico da versão indicada;
2. `resource_id` deve permanecer único e inalterado;
3. valores vazios, listas multivaloradas, URLs, acentos e pontuação devem ser preservados;
4. nenhum valor pode ser enriquecido, abreviado ou corrigido somente no espelho;
5. abas históricas, dicionários, auditorias e changelog podem ser preservados, desde que não sejam confundidos com a tabela canônica;
6. abas legadas devem permanecer claramente identificadas como históricas;
7. fórmulas, filtros ou formatação não podem alterar o valor textual exportado;
8. a planilha nativa e o `.xlsx` devem ser gerados a partir do mesmo snapshot e declarar o mesmo commit.

## Verificação obrigatória

Antes de declarar um espelho sincronizado, confirmar:

- contagem de linhas e colunas;
- correspondência exata dos cabeçalhos;
- igualdade dos 51 `resource_id`;
- igualdade célula a célula da tabela canônica;
- ausência de linhas duplicadas ou deslocadas;
- preservação de URLs e separadores ` | `;
- presença dos metadados de geração;
- legibilidade da tabela e congelamento do cabeçalho;
- registro no `project_changelog`.

A simples ampliação da grade para 34 colunas não comprova sincronização; os 34 cabeçalhos e valores devem estar efetivamente preenchidos e comparados.

## Momento de regeneração

1. a planilha nativa 0.7.0 de 34 campos pode ser usada para consulta operacional, sempre como derivada;
2. o `.xlsx` de 22 campos deve ser substituído e verificado quando a operação de upload voltar a funcionar;
3. após DATA1-C e DATA1-D, os dois espelhos devem ser obrigatoriamente regenerados com 51 recursos e 38 campos;
4. a geração deve ser repetida após cada release que altere o CSV canônico.

A pendência do `.xlsx` não bloqueia DATA1-EXT, porque o CSV e a planilha nativa permanecem disponíveis. Ela bloqueia apenas a declaração de que ambos os espelhos estão sincronizados.

## Concorrência e conflitos

- uma única sessão deve ser responsável por cada ciclo de regeneração;
- antes de escrever, conferir o commit atual de `main` e a última entrada do changelog;
- se outra sessão alterar o CSV ou o Drive durante a geração, interromper a declaração de sincronização e reiniciar a comparação;
- nunca mesclar manualmente duas versões de `data_resources` no Drive;
- divergências e falhas de upload devem ser registradas como incidente operacional, com arquivos, commits e campos afetados.

## Critério de conclusão de cada espelho

Um espelho individual somente está sincronizado quando:

1. o commit-fonte está integrado à `main`;
2. a suíte relevante está verde;
3. o arquivo foi atualizado a partir desse commit;
4. as verificações de igualdade foram aprovadas;
5. o evento foi registrado no changelog do Drive.

A planilha nativa atende atualmente aos requisitos de conteúdo 51 × 34. O `.xlsx` ainda não atende.
