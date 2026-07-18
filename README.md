# Catálogo de Fontes de Dados Ambientais

Catálogo público e pesquisável de fontes para ecologia, biodiversidade, clima, carbono, solo, vegetação e temas relacionados.

## Fonte única de dados

A fonte canônica é **[data/data_resources.csv](data/data_resources.csv)**. Ela alimenta o site e é o arquivo oferecido para download.

O arquivo `data/data_resources.json` não deve ser editado manualmente: ele é validado e gerado a partir do CSV pelo workflow do GitHub Pages. A planilha do Google Drive é apenas uma referência histórica/espelho e não participa da publicação.

## Conteúdo

- 51 fontes revisadas;
- identidade e descrição adotadas das páginas ou documentações oficiais;
- links distintos para página institucional, acesso aos dados, API e evidência;
- cobertura, formatos, acesso, licença, utilidade acadêmica e limitações;
- site estático com busca e filtros.

## Atualização

1. Edite somente `data/data_resources.csv`.
2. Use documentação oficial e registre a melhor evidência em `verification_url`.
3. Atualize `last_verified` apenas nas linhas realmente verificadas.
4. Execute `python3 scripts/build_catalog.py`.
5. Abra um pull request; o deploy da branch `main` valida o CSV e gera o JSON.

Os critérios completos estão em [AUDIT_WORKFLOW.md](AUDIT_WORKFLOW.md) e o inventário da revisão em [AUDIT_REPORT.md](AUDIT_REPORT.md).

## Limite de uso

O catálogo é um ponto de partida, não um selo de qualidade. Antes de utilizar dados, confira versão, licença, metodologia, resolução, cobertura, incerteza e adequação à pergunta científica.

## Licenças

- Código: MIT
- Curadoria original do catálogo: CC BY 4.0
- As fontes externas mantêm suas próprias licenças e condições.
