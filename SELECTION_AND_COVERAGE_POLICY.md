# Política de seleção, exclusão, duplicidade e cobertura

## Objetivo

Explicitar por que uma fonte entra, como duplicidades são evitadas e quais lacunas permanecem. O catálogo não é declarado completo ou representativo de todo o universo ambiental.

## Unidade de seleção

A unidade elegível é uma **fonte de dados ou infraestrutura de informação** com identidade própria, responsável identificável e acesso verificável: base, repositório, catálogo, portal, plataforma, sistema, serviço, rede ou software de publicação.

## Critérios mínimos de inclusão

A fonte deve:

1. ser relevante para pesquisa, ensino ou extensão ambiental;
2. disponibilizar dados, metadados ou serviço de descoberta/acesso, não apenas conteúdo editorial;
3. possuir documentação oficial verificável;
4. ter governança identificável;
5. oferecer utilidade distinta ou reduzir lacuna;
6. permitir descrição no nível de fonte;
7. permitir registro honesto de acesso, licença, limitações e incertezas.

## Critérios de exclusão

Excluir do CSV canônico:

- notícias, blogs e materiais somente didáticos;
- artigos ou relatórios sem infraestrutura associada;
- dataset isolado pertencente a fonte já catalogada;
- ferramenta sem função de publicação, descoberta ou acesso;
- mirror sem governança própria;
- recurso descontinuado sem função independente;
- recurso cuja identidade ou função não tenha evidência suficiente.

## Recursos bibliométricos e editoriais

Bases de literatura, rankings e redes de citação exigem um portão de escopo antes da migração. A decisão deve avaliar reutilização estruturada, função de descoberta ambiental, governança, condições de acesso, utilidade distinta e destino adequado: catálogo principal, seção auxiliar, fusão ou exclusão.

### Regra derivada de G0

Um recurso bibliométrico pode permanecer no catálogo principal quando:

1. oferece dados ou metadados estruturados, busca, rede de citações ou função de descoberta reutilizável;
2. possui metodologia oficial e governança identificável;
3. tem utilidade distinta para pesquisa, ensino ou extensão ambiental;
4. permite registrar acesso, licença e limitações com honestidade;
5. não é apresentado como substituto de fontes ambientais primárias.

Materiais apenas narrativos, noticiosos ou didáticos, sem infraestrutura estruturada, continuam excluídos.

A natureza bibliométrica deve ser explícita. Cobertura de publicações e citações não deve ser confundida com cobertura espacial ou temporal de observações ambientais.

### Decisão do Project COSMOS

G0 confirmou a elegibilidade do Project COSMOS para o catálogo principal como infraestrutura bibliométrica. A decisão completa está em `G0_COSMOS_SCOPE_DECISION.md`.

A permanência não implica que a base integral seja aberta, que exista API pública ou que o recurso forneça medições ambientais. Esses atributos permanecem descritos com suas limitações e sujeitos à revisão factual final.

## Duplicidade e relação entre recursos

### Mesmo recurso, nomes diferentes

Manter uma linha quando nomes, siglas ou URLs representam a mesma infraestrutura e governança.

### Portal e base subjacente

Manter linhas separadas somente quando possuem função, documentação, acesso ou governança próprios e a separação melhora a descoberta sem duplicação integral.

### Agregador e provedor

Podem coexistir, mas devem alertar sobre dupla contagem e preservar o provedor original.

### Versões regionais

Criar linha própria somente com governança, documentação, cobertura e acesso próprios.

### Recurso sucessor

Manter o sucessor ativo, registrar a relação e não conservar duas linhas quando o anterior apenas redireciona.

## Candidatos

Novas fontes entram primeiro em `candidates/source_candidates.csv`, com nome, URL, justificativa, tema, cobertura, duplicidade, evidência, prioridade e decisão: incluir, excluir, fundir ou aguardar evidência.

Uma URL fornecida pelo usuário autoriza triagem inicial, não decisão final. Nenhum candidato é publicado sem revisão de elegibilidade e completude.

## Matriz de lacunas

A cobertura deve cruzar área de pesquisa, escala geográfica, tipo funcional, natureza institucional, download gratuito, acesso programático e presença de dados do Brasil.

A matriz orienta busca; não cria cotas e frequência de registros não mede importância científica.

## Critérios de prioridade para expansão

Prioridade maior para fontes que reduzam lacunas brasileiras ou latino-americanas, tenham documentação estável, acesso reutilizável, cubram temas pouco representados e possuam uso científico demonstrável.

Prioridade menor para recursos redundantes, pouco documentados, estritamente comerciais ou já cobertos por fonte mais estável.

## Revisão da seleção

- antes de expansão: revisar duplicidades, escopo e lacunas;
- anualmente: reavaliar recursos descontinuados, incorporados ou renomeados;
- imediatamente: atualizar fusão, sucessão ou mudança institucional;
- antes da migração: resolver portões de escopo pendentes.

## Estado atual

Enquanto DATA1 e DATA2 não estiverem concluídos, novas fontes permanecem fora do CSV. O portão G0 do Project COSMOS está resolvido com decisão `manter_confirmado`; W1A é o próximo ciclo de DATA1-EXT. Nenhuma alteração automática do CSV 0.7.0 foi autorizada por G0.
