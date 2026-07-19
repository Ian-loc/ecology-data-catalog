# Workflow de correções de qualidade

## Objetivo

Corrigir as fragilidades identificadas na auditoria transversal antes de migrar o catálogo para 0.8.0, expandir o número de fontes ou preparar a versão 1.0.0 e o DOI.

O princípio central é simples: **controle de processo não substitui verificação científica**. CI verde comprova estrutura e coerência interna; não comprova, por si só, que links, formatos, APIs, licenças, resoluções e classificações externas estejam atuais ou corretos.

## Regras de prioridade

1. corrigir primeiro contradições entre documentos, contratos e validadores;
2. completar a matriz de migração antes de revisar os 35 casos pendentes;
3. revisar as fontes atuais antes de expandir o catálogo;
4. manter melhorias didáticas e de resolução como enriquecimentos não bloqueantes;
5. reavaliar a ordem ao final de cada ciclo, usando evidência de custo, risco e dependência;
6. não alterar versão, CSV canônico ou DOI enquanto os respectivos portões estiverem bloqueados.

## Ordem operacional revisada

| Ordem | Ciclo | Prioridade | Escopo | Estado inicial | Critério de conclusão |
|---:|---|---|---|---|---|
| 1 | QC0 | P0 | Alinhar as 14 regras semânticas entre auditoria, JSON e CI | em desenvolvimento | contrato e teste exigem o mesmo conjunto exato de regras |
| 2 | DATA1-BX | P0 | Expandir a matriz para todos os campos cuja normalização foi prometida | planejado | 51 linhas com propostas ou estados explícitos para todos os campos-alvo |
| 3 | SELECT1 | P0 | Definir inclusão, exclusão, duplicidade e análise de lacunas | em desenvolvimento | política versionada e validada pelo CI |
| 4 | DATA1-BR | P0 | Revisar os 35 casos pendentes contra documentação oficial | bloqueado por DATA1-BX | nenhuma decisão pendente ou inferida sem evidência |
| 5 | DATA1-C | P0 | Migrar atomicamente para 38 campos | bloqueado | 51 IDs preservados, zero perda e versão 0.8.0 validada |
| 6 | DATA1-D | P0 | Ativar validações semânticas no CSV final | planejado | as 14 regras bloqueiam estados inconsistentes |
| 7 | DATA2 | P0 | Auditar as 51 fontes no esquema final | planejado | links, acesso, formatos, licença, evidência e data revisados |
| 8 | UX5 | P1 | Exibir e filtrar os 38 campos; testar em navegador | planejado | testes estruturais e funcionais aprovados |
| 9 | RELEASE2 | P1 | Preparar v1.0.0 e confirmar deploy | bloqueado | G1–G10 concluídos e site inspecionado |
| 10 | DOI | P1 | Criar release imutável e depósito Dataset | bloqueado | G1–G12 concluídos |
| 11 | RES1 | P3 | Faixas de resolução por produto | baixa prioridade; não bloqueante | tabela auxiliar documentada e auditada |
| 12 | EDU1 | P3 | Página didática sobre fenômenos ambientais | baixa prioridade; não bloqueante | conteúdo curto, referenciado e ligado às fontes do catálogo |

## QC0 — contrato semântico

Correções imediatas:

- exigir exatamente 14 regras no contrato 0.8.0;
- adicionar ao JSON as regras sobre `visualization_types`, unicidade/trim de listas e DOI de evidência;
- impedir que o validador aceite apenas “dez ou mais” regras;
- manter CSV, CFF, versão e interface inalterados.

## DATA1-BX — completar a matriz antes da revisão externa

A matriz DATA1-B cobre tipo, escala, formatos, protocolos, ferramentas, situação institucional e orientação de citação. A auditoria também prometeu normalizar:

- `data_product_types`;
- `visualization_types`;
- `data_sources`;
- `temporal_resolution`;
- `access_conditions`.

Antes de BR1, a matriz deverá ser ampliada com estes campos e com estados explícitos de confiança e revisão. Não é permitido declarar a normalização completa enquanto essas dimensões não estiverem cobertas.

### Regra de migração

- valor controlado confirmado → proposta explícita;
- heterogeneidade real entre produtos → placeholder documentado e justificativa;
- ausência de evidência → `unknown`, revisão pendente;
- texto científico que não cabe em vocabulário → preservado em campo narrativo, sem perda;
- nenhuma transformação automática apenas por correspondência de palavras.

## SELECT1 — critérios de seleção e cobertura

A política de seleção deve responder:

- o que conta como fonte elegível;
- o que deve ser excluído;
- como reconhecer duplicidades e recursos sucessores;
- como tratar versões regionais, software e catálogos agregadores;
- como registrar candidatos sem colocá-los imediatamente no CSV;
- como medir lacunas temáticas, geográficas, institucionais e de acesso.

A expansão permanecerá bloqueada até essa política estar ativa.

## DATA1-BR e DATA2 — revisão científica

Cada revisão deverá registrar, no mínimo:

- fonte e URL oficial;
- grupo de campos sustentado pela evidência;
- data efetiva da inspeção;
- resultado observado;
- incerteza ou limitação;
- alteração proposta;
- revisor e PR.

A evidência acadêmica representativa não substitui documentação oficial de API, formato, licença ou autenticação.

## RES1 — resolução mínima e máxima por produto

### Viabilidade

É possível registrar faixas com boa precisão quando a documentação oficial informa a resolução nativa de produtos específicos. Não é cientificamente seguro inferir resolução a partir do nível de zoom de um geovisualizador.

### Conceitos que não devem ser misturados

- **raster:** tamanho de célula ou resolução angular;
- **vetor/cartografia:** escala nominal, unidade mínima de mapeamento ou precisão posicional;
- **pontos:** precisão/incerteza das coordenadas, não “pixel”;
- **tempo:** intervalo de observação ou atualização;
- **visualizador:** limite de zoom e generalização de exibição, que não representam necessariamente a resolução dos dados.

### Estrutura recomendada

Criar, após a estabilização do esquema principal, uma tabela auxiliar `data/product_resolution_examples.csv`, ligada por `resource_id`, com:

- `product_name`;
- `resolution_dimension`;
- `finest_resolution`;
- `coarsest_resolution`;
- `unit_or_scale`;
- `resolution_type`;
- `coverage_or_version`;
- `evidence_url`;
- `last_verified`;
- `confidence`;
- `notes`.

A faixa só poderá aparecer no card da fonte quando os produtos comparados usarem a mesma dimensão e unidade. Caso contrário, a interface deverá informar “varia por produto” e mostrar exemplos documentados.

RES1 é **não bloqueante para v1.0.0 e DOI**, exceto quando a auditoria identificar que o valor atual de `spatial_resolution` está incorreto.

## EDU1 — página didática sobre fenômenos

Criar uma página separada, sem transformar os cards em textos enciclopédicos. Cada módulo deverá responder:

1. o que é o fenômeno;
2. como é medido ou observado;
3. quais tipos de dados o representam;
4. quais limitações e incertezas são comuns;
5. quais fontes do catálogo podem ser usadas;
6. quais referências sustentam a explicação.

Temas iniciais possíveis:

- mudanças climáticas, riscos e adaptação;
- biodiversidade e agrobiodiversidade;
- fragmentação, conectividade e efeitos de borda;
- carbono em vegetação e solo;
- uso e cobertura da terra;
- agroflorestas e serviços ecossistêmicos;
- sistemas alimentares, clima e biodiversidade;
- sensoriamento remoto, resolução e escala.

Regras editoriais:

- linguagem acessível sem simplificação enganosa;
- separação entre definição, evidência e exemplo;
- referências verificáveis;
- atualização independente do CSV científico;
- nenhuma afirmação causal baseada apenas em visualização;
- links diretos para filtros do catálogo relacionados ao tema.

EDU1 é **não bloqueante para v1.0.0 e DOI** e deve ser iniciado somente após DATA2 ou quando houver capacidade editorial separada.

## Checkpoints de reordenação

A ordem será reavaliada após:

1. QC0 + SELECT1;
2. DATA1-BX;
3. cada lote BR1–BR5;
4. migração 0.8.0;
5. primeiros lotes DATA2;
6. testes funcionais da interface.

Uma tarefa pode subir de prioridade quando:

- bloqueia outra etapa;
- revela risco de perda de dados;
- afeta a validade científica;
- corrige informação pública incorreta;
- reduz retrabalho significativo.

Uma tarefa pode descer de prioridade quando:

- é apenas enriquecimento;
- exige pesquisa externa indisponível;
- aumenta o esquema sem benefício decisório claro;
- pode ser entregue com segurança em v1.1.0.

## Estado protegido

Durante este workflow:

- versão formal permanece 0.7.0;
- CSV permanece com 51 fontes e 34 campos até DATA1-C;
- `doi_allowed` permanece `false`;
- nenhuma nova fonte entra diretamente no catálogo;
- candidatos podem ser registrados fora do CSV canônico;
- RES1 e EDU1 não desbloqueiam nem bloqueiam o DOI.
