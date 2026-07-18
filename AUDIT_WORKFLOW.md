# Workflow de verificação do catálogo

## Princípio de governança

Existe uma única fonte de verdade: `data/data_resources.csv`. O JSON do site é um artefato de build. A planilha no Drive não deve ser atualizada em paralelo.

## Ordem de evidência

1. página institucional da própria fonte;
2. documentação técnica ou metodologia oficial;
3. página oficial de acesso/download ou documentação da API;
4. licença ou termos oficiais;
5. somente na ausência desses itens, documentação do órgão gestor.

Descrições editoriais, agregadores e resultados de busca não substituem evidência oficial.

## Revisão por fonte

Para cada linha:

1. confirmar nome, sigla, identidade autodeclarada, objetivo e responsável;
2. testar página oficial, acesso aos dados e documentação de API;
3. conferir temas, produtos, formatos, cobertura e resoluções;
4. distinguir download integral, parcial, condicionado ou inexistente;
5. registrar licença e restrições sem inferir abertura;
6. descrever usos acadêmicos concretos;
7. explicitar limitações relevantes para interpretação ou reprodutibilidade;
8. registrar `verification_url` e a data efetiva da revisão.

A identidade oficial preserva o vocabulário da própria fonte; não há taxonomia normalizada imposta pelo catálogo.

## Controle de qualidade

Antes de publicar, execute:

```bash
python3 scripts/build_catalog.py
```

O script bloqueia cabeçalho divergente, campos essenciais vazios, IDs inválidos ou duplicados, nomes duplicados, URLs essenciais não HTTPS, valores fora das listas de acesso/API e datas inválidas. O workflow repete essa validação antes do deploy.

## Frequência

- trimestral: verificação automatizada/manual de links;
- anual: revisão de conteúdo das 51 fontes;
- imediata: correção de link quebrado, mudança de licença, acesso, versão ou responsável;
- por pull request: validação estrutural e inspeção do diff.

`last_verified` é por linha; não deve ser alterado em massa sem nova verificação.

## Critério de utilidade acadêmica

A avaliação prioriza descoberta, download, integração por API, reprodutibilidade, séries temporais, escala espacial, ensino, comparação entre estudos e adequação a perguntas de pesquisa. Limitações devem cobrir, quando aplicável, viés amostral, cobertura desigual, defasagem, resolução, dependência de credenciais, quotas, licenças e falta de acesso à base integral.
