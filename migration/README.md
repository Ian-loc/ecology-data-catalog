# Matriz de migração DATA1-B

## Finalidade

`data1b_migration_matrix.csv` registra uma decisão proposta para cada uma das 51 fontes antes da migração do esquema 0.7.0 para 0.8.0.

A matriz não duplica os campos existentes. Os valores atuais permanecem no arquivo canônico `data/data_resources.csv` e são associados pelo `resource_id` durante a validação.

## Ligações com o CSV atual

| Decisão | Campo atual usado como base |
|---|---|
| tipo funcional | `official_identity` |
| escala geográfica | `geographic_coverage` |
| formatos | `data_formats` |
| protocolos e ferramentas | `access_protocols` |
| situação institucional | `institutional_status` |
| evidência | `verification_url` |

## Colunas da matriz

- `resource_id`: identificador preservado do catálogo;
- `resource_type_proposed`: função principal controlada;
- `geographic_scope_proposed`: maior extensão geográfica geral;
- `data_formats_proposed`: formatos normalizados;
- `access_protocols_proposed`: protocolos e interfaces técnicas;
- `access_tools_proposed`: pacotes, clientes e ambientes separados dos protocolos;
- `institutional_status_proposed`: situação institucional normalizada e multivalorada;
- `citation_guidance_url_proposed`: página oficial específica de citação, somente quando confirmada;
- `confidence`: `alta`, `média` ou `baixa`;
- `migration_status`: decisão pronta ou dependente de revisão manual;
- `rationale`: justificativa funcional e geográfica;
- `exceptions`: exceções codificadas que impedem migração automática.

## Estado atual

- 51 fontes representadas;
- 24 decisões de alta confiança;
- 27 decisões de confiança média;
- nenhuma decisão de baixa confiança;
- 16 registros sem exceção estão prontos para a futura migração;
- 35 registros permanecem em revisão manual por confiança média ou exceção técnica;
- todo valor `other_documented` exige exceção explícita e revisão manual, mesmo quando a classificação geral tem alta confiança;
- URLs de orientação de citação permanecem vazias até confirmação oficial específica;
- CSV canônico ainda permanece em 0.7.0, com 34 campos;
- nenhuma proposta deve ser aplicada antes da revisão dos registros marcados como `revisão_manual`.

## Validação

Execute:

```bash
python3 scripts/validate_migration_matrix.py
```

O teste confere cardinalidade, IDs, vocabulários, coerência com o CSV atual, exceções, confiança, status de migração e regras cruzadas do contrato `schema/v0.8.0-draft.json`.
