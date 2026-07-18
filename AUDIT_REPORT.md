# Relatório da auditoria do catálogo

## Resultado

Foram revisadas **51 fontes e 26 variáveis** por fonte. A auditoria separou descrição institucional, acesso efetivo aos dados, API, utilidade acadêmica, limitações e evidência. As identidades usam a terminologia declarada pelas próprias fontes, sem converter tudo para uma taxonomia editorial única.

O CSV do GitHub é a fonte canônica; o site consome um JSON gerado automaticamente a partir dele. A planilha do Drive não alimenta o site.

## Principais correções

- atualização de endereços do Programa Queimadas, CNUC, OBIS, DataONE/KNB, Climate Data Guide, BIEN e ESGF;
- correção de versões/coberturas de MapBiomas, EDGAR, Project COSMOS e outras fontes;
- distinção entre página inicial, página de acesso e documentação de API;
- remoção de afirmações de download/API quando a base integral não é pública;
- inclusão de utilidade acadêmica e limitações em todas as linhas.

## Inventário verificado

| ID | Fonte | Identidade oficial | Evidência oficial | Verificada em |
|---|---|---|---|---|
| DR0001 | Plataforma Mineira para Adaptação às Mudanças Climáticas | Plataforma e ferramenta de apoio aos municípios mineiros | [evidência](https://clima-gerais.meioambiente.mg.gov.br/) | 2026-07-18 |
| DR0002 | Infraestrutura de Dados Espaciais do Sistema Estadual de Meio Ambiente e Recursos Hídricos | Infraestrutura de Dados Espaciais do SISEMA | [evidência](https://idesisema.meioambiente.mg.gov.br/) | 2026-07-18 |
| DR0003 | AdaptaBrasil MCTI | Sistema de Informações e Análises sobre Impactos das Mudanças do Clima | [evidência](https://adaptabrasil.mcti.gov.br/index.php/sobre) | 2026-07-18 |
| DR0004 | Sistema de Registro Nacional de Emissões | Sistema oficial de registro e transparência de emissões e remoções de gases de efeito estufa | [evidência](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene) | 2026-07-18 |
| DR0005 | Centro Nacional de Monitoramento e Alertas de Desastres Naturais | Centro nacional de monitoramento e alertas de desastres naturais | [evidência](https://www.gov.br/cemaden/pt-br) | 2026-07-18 |
| DR0006 | PANORAMA — Infraestrutura de Dados Espaciais do CENSIPAM | Infraestrutura de Dados Espaciais do CENSIPAM | [evidência](https://panorama.sipam.gov.br/) | 2026-07-18 |
| DR0007 | UrbVerde | Plataforma de inteligência territorial para sustentabilidade urbana | [evidência](https://urbverde.iau.usp.br/) | 2026-07-18 |
| DR0008 | Portal Brasileiro de Dados Abertos | Portal Brasileiro de Dados Abertos | [evidência](https://dados.gov.br/) | 2026-07-18 |
| DR0009 | Global Biodiversity Information Facility | Rede internacional e infraestrutura de dados de biodiversidade | [evidência](https://www.gbif.org/what-is-gbif) | 2026-07-18 |
| DR0010 | MapBiomas Brasil | Rede colaborativa que produz mapas e dados anuais de cobertura e uso da terra | [evidência](https://brasil.mapbiomas.org/produtos/) | 2026-07-18 |
| DR0011 | TerraBrasilis | Plataforma de dados geográficos | [evidência](https://terrabrasilis.dpi.inpe.br/) | 2026-07-18 |
| DR0012 | Programa Queimadas / Banco de Dados de Queimadas | Programa de monitoramento por satélites e Banco de Dados de Queimadas | [evidência](https://terrabrasilis.dpi.inpe.br/queimadas/portal/informacoes/perguntas-frequentes/) | 2026-07-18 |
| DR0013 | speciesLink | Rede de informação que integra dados de coleções científicas | [evidência](https://specieslink.net/) | 2026-07-18 |
| DR0014 | Sistema de Informação sobre a Biodiversidade Brasileira | Sistema de Informação sobre a Biodiversidade Brasileira | [evidência](https://www.sibbr.gov.br/) | 2026-07-18 |
| DR0015 | Banco de Dados e Informações Ambientais | Banco de Dados e Informações Ambientais | [evidência](https://bdiaweb.ibge.gov.br/) | 2026-07-18 |
| DR0016 | Cadastro Nacional de Unidades de Conservação | Cadastro Nacional de Unidades de Conservação | [evidência](https://dados.gov.br/dados/conjuntos-dados/unidadesdeconservacao) | 2026-07-18 |
| DR0017 | Sistema Nacional de Informações sobre Recursos Hídricos / HidroWeb | Sistema Nacional de Informações sobre Recursos Hídricos e ferramenta HidroWeb | [evidência](https://www.snirh.gov.br/hidroweb/) | 2026-07-18 |
| DR0018 | Banco de Dados Meteorológicos do INMET | Banco de Dados Meteorológicos do INMET | [evidência](https://bdmep.inmet.gov.br/) | 2026-07-18 |
| DR0019 | Google Earth Engine Data Catalog | Catálogo de dados do Google Earth Engine | [evidência](https://developers.google.com/earth-engine/guides/access) | 2026-07-18 |
| DR0020 | Application for Extracting and Exploring Analysis Ready Samples | Aplicação para extração e exploração de amostras prontas para análise | [evidência](https://appeears.earthdatacloud.nasa.gov/) | 2026-07-18 |
| DR0021 | Copernicus Climate Data Store | Climate Data Store | [evidência](https://cds.climate.copernicus.eu/) | 2026-07-18 |
| DR0022 | WorldClim | Base de dados climáticos globais de alta resolução espacial | [evidência](https://www.worldclim.org/) | 2026-07-18 |
| DR0023 | Climatologies at High Resolution for the Earth's Land Surface Areas | Conjunto de climatologias de alta resolução para as superfícies terrestres | [evidência](https://www.chelsa-climate.org/) | 2026-07-18 |
| DR0024 | Protected Planet / World Database on Protected Areas | Plataforma de conhecimento sobre áreas protegidas e outras medidas eficazes de conservação | [evidência](https://www.protectedplanet.net/en) | 2026-07-18 |
| DR0025 | IUCN Red List of Threatened Species | Fonte global de informação sobre o risco de extinção de espécies | [evidência](https://www.iucnredlist.org/about/background-history) | 2026-07-18 |
| DR0026 | Ocean Biodiversity Information System | Centro global de dados e informações de acesso aberto sobre biodiversidade marinha | [evidência](https://obis.org/data/access/) | 2026-07-18 |
| DR0027 | eBird | Projeto colaborativo de ciência cidadã sobre aves | [evidência](https://science.ebird.org/) | 2026-07-18 |
| DR0028 | Movebank | Plataforma online e repositório de dados de rastreamento animal | [evidência](https://www.movebank.org/cms/movebank-main) | 2026-07-18 |
| DR0029 | National Ecological Observatory Network | Observatório ecológico continental e instalação de pesquisa | [evidência](https://www.neonscience.org/data) | 2026-07-18 |
| DR0030 | Data Observation Network for Earth | Projeto comunitário e federação de repositórios de dados | [evidência](https://www.dataone.org/) | 2026-07-18 |
| DR0031 | Knowledge Network for Biocomplexity | Repositório de dados ecológicos e ambientais | [evidência](https://knb.ecoinformatics.org/) | 2026-07-18 |
| DR0032 | PANGAEA Data Publisher for Earth & Environmental Science | Editora e biblioteca de dados para ciências da Terra e ambientais | [evidência](https://www.pangaea.de/) | 2026-07-18 |
| DR0033 | Dryad | Plataforma comunitária de publicação e preservação de dados de pesquisa | [evidência](https://datadryad.org/) | 2026-07-18 |
| DR0034 | iNaturalist | Rede social online e plataforma de ciência cidadã sobre biodiversidade | [evidência](https://www.inaturalist.org/pages/about) | 2026-07-18 |
| DR0035 | Climate Data Guide | Portal de conhecimento especializado para descoberta e avaliação de dados climáticos | [evidência](https://climatedataguide.ucar.edu/) | 2026-07-18 |
| DR0036 | Fine-Root Ecology Database | Base de dados de ecologia de raízes finas | [evidência](https://roots.ornl.gov/) | 2026-07-18 |
| DR0037 | SoilGrids | Sistema global de mapeamento digital de propriedades do solo | [evidência](https://soilgrids.org/) | 2026-07-18 |
| DR0038 | World Soil Information Service | Serviço mundial de informações de perfis de solo | [evidência](https://www.isric.org/explore/wosis) | 2026-07-18 |
| DR0039 | Global Biodiversity Information Facility Integrated Publishing Toolkit | Software livre e de código aberto para publicação de dados de biodiversidade | [evidência](https://www.gbif.org/ipt) | 2026-07-18 |
| DR0040 | TRY Plant Trait Database | Base global de dados curados de características de plantas | [evidência](https://www.try-db.org/) | 2026-07-18 |
| DR0041 | Botanical Information and Ecology Network | Ecossistema de dados integrado e versionado para ciência da biodiversidade vegetal | [evidência](https://bien.nceas.ucsb.edu/bien/data-and-access/) | 2026-07-18 |
| DR0042 | AmeriFlux | Rede de sítios de fluxos de ecossistemas nas Américas | [evidência](https://ameriflux.lbl.gov/data/data-policy/) | 2026-07-18 |
| DR0043 | FLUXNET | Rede global de sítios de torres de fluxos e sistema de dados harmonizados | [evidência](https://fluxnet.org/data/) | 2026-07-18 |
| DR0044 | Global Forest Watch | Plataforma online de monitoramento florestal | [evidência](https://www.globalforestwatch.org/) | 2026-07-18 |
| DR0045 | Global Carbon Atlas | Plataforma para explorar e visualizar dados de fluxos de carbono | [evidência](https://globalcarbonatlas.org/) | 2026-07-18 |
| DR0046 | EDGAR — Emissions Database for Global Atmospheric Research | Base de dados independente de emissões antropogênicas globais | [evidência](https://edgar.jrc.ec.europa.eu/) | 2026-07-18 |
| DR0047 | Copernicus Data Space Ecosystem | Ecossistema aberto de dados e serviços Copernicus | [evidência](https://dataspace.copernicus.eu/) | 2026-07-18 |
| DR0048 | Earth System Grid Federation | Esforço de código aberto e plataforma distribuída de dados e computação | [evidência](https://esgf.github.io/) | 2026-07-18 |
| DR0049 | International Long Term Ecological Research Network | Rede internacional de redes de pesquisa ecológica de longa duração | [evidência](https://www.ilter.network/) | 2026-07-18 |
| DR0050 | ORNL Distributed Active Archive Center | Centro de arquivo ativo distribuído e repositório de dados da NASA | [evidência](https://www.earthdata.nasa.gov/centers/ornl-daac) | 2026-07-18 |
| DR0051 | Project COSMOS | Base de dados de pesquisa sobre mudanças climáticas | [evidência](https://interactive.carbonbrief.org/cosmos/methodology/index.html) | 2026-07-18 |

## Escopo da conclusão

“Verificada” significa que a linha foi confrontada com página ou documentação oficial disponível na data indicada. Não significa certificação externa da qualidade científica de todos os datasets hospedados por cada fonte. Licenças, quotas, versões e disponibilidade podem mudar; por isso o processo contínuo está em [AUDIT_WORKFLOW.md](AUDIT_WORKFLOW.md).
