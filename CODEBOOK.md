# Dicionário de variáveis

| Campo | Definição |
|---|---|
| `resource_id` | Identificador estável DR0001… |
| `resource_name` | Nome oficial da fonte. |
| `acronym` | Sigla ou nome curto. |
| `official_identity` | Natureza declarada pela própria fonte. |
| `description` | Síntese objetiva do propósito. |
| `homepage_url` | Site institucional principal, página “Sobre” ou página oficial do órgão responsável dedicada à fonte. Não é, por padrão, o link direto para os dados. |
| `data_access_url` | Destino efetivo para pesquisar, visualizar, solicitar ou baixar dados. Deve apontar ao catálogo, busca, visualizador, formulário de acesso ou página de download mais direta e estável. |
| `research_areas` | Áreas condensadas usadas no filtro. |
| `keywords` | Temas específicos pesquisáveis. |
| `data_product_types` | Produtos disponibilizados. |
| `data_formats` | Formatos de arquivo ou representação. |
| `visualization_types` | Mapas, gráficos, dashboards e outras interfaces. |
| `geographic_coverage` | Abrangência espacial declarada. |
| `covers_brazil` | Presença de dados aplicáveis ao Brasil. |
| `spatial_resolution` | Escala ou resolução espacial. |
| `temporal_coverage` | Período coberto. |
| `temporal_resolution` | Frequência ou granularidade temporal. |
| `data_sources` | Origem empírica ou institucional dos dados. |
| `free_download` | Disponibilidade de download gratuito. |
| `access_conditions` | Cadastro, solicitação, embargo, quota ou restrição. |
| `programmatic_access` | Disponibilidade de acesso automatizado documentado. |
| `access_protocols` | Protocolos, APIs, pacotes ou mecanismos. |
| `authentication_required` | Necessidade de conta, token ou credencial. |
| `access_documentation_url` | Documentação técnica do acesso; não substitui automaticamente a página efetiva de acesso aos dados. |
| `license` | Licença dos dados ou condição declarada. |
| `institutional_status` | Natureza institucional. |
| `owner_or_manager` | Responsável pela fonte. |
| `academic_uses` | Usos relevantes para ensino e pesquisa. |
| `limitations` | Restrições e riscos de interpretação. |
| `academic_evidence_type` | Natureza da evidência externa/técnica. |
| `academic_evidence_url` | Artigo ou documento representativo. |
| `academic_evidence_note` | O que a evidência sustenta. |
| `verification_url` | Principal evidência oficial. |
| `last_verified` | Data efetiva da revisão, AAAA-MM-DD. |

## Regra dos links

Os botões **Site oficial** e **Acessar dados** devem cumprir funções diferentes. Quando `homepage_url` e `data_access_url` apontam para o mesmo destino, o registro permanece como pendência de revisão. A igualdade só pode ser mantida após confirmação de que uma única página realmente apresenta a fonte e oferece acesso efetivo aos dados.

`data_access_url = não se aplica` é reservado a recursos que não oferecem dados diretamente, como software de publicação ou guias de descoberta que encaminham a outros provedores.

## Valores controlados

- `free_download`: sim, parcial, não, desconhecido, não se aplica.
- `programmatic_access`: sim, parcial, não, desconhecido, não se aplica.
- `authentication_required`: sim, parcial, não, desconhecido, não se aplica.
- `covers_brazil`: sim, parcial, não, desconhecido, não se aplica.
- Campos multivalorados usam ` | ` como separador interno.

Consulte [METHODOLOGY.md](METHODOLOGY.md) para critérios interpretativos.
