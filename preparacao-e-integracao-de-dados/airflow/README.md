# Projeto de Integração e Processamento de Dados - Faculdade ProData

Este repositório contém o código e os recursos necessários para o desenvolvimento de um sistema de produção de dados para a Faculdade ProData. O projeto foi desenvolvido como parte da disciplina de **Integração e Processamento de Fluxos Contínuos de Dados** do curso de **Ciência de Dados e Big Data** da Pontifícia Universidade Católica de Minas Gerais (PUC-MG).

## Descrição do Projeto

O objetivo deste projeto é criar um sistema analítico para a Faculdade ProData, que permita o armazenamento e análise em tempo real das notas dos alunos, cálculo de médias, e futuramente, a geração de previsões sobre as disciplinas. O sistema é composto por várias etapas, incluindo a geração de dados, normalização, e carregamento em um data lake para consumo.

### Fluxo de Trabalho

1. **Geração de Dados**:
   - **Grade Curricular**: Gera dados das disciplinas oferecidas em cada curso.
   - **Dados dos Alunos**: Gera dados fictícios dos alunos, incluindo informações pessoais, matrículas, e status.

2. **Carregamento na Camada Raw**:
   - Os dados gerados são carregados em um data lake na camada `raw`, onde são armazenados em formatos como `.csv`.

3. **Normalização dos Dados**:
   - Os dados brutos são normalizados e transformados em tabelas relacionais, seguindo as formas normais (1FN, 2FN, 3FN).

4. **Carregamento na Camada de Consumo**:
   - Os dados normalizados são carregados na camada `consume` do data lake, prontos para serem utilizados em análises e consultas.

5. **Automatização com Apache Airflow**:
   - O fluxo de trabalho é automatizado usando uma DAG (Directed Acyclic Graph) no Apache Airflow, que orquestra as tarefas de geração, normalização e carregamento dos dados.

## Estrutura do Repositório

- **`dag_trabalho_faculdade_prodata.py`**: Contém a DAG do Apache Airflow que orquestra o fluxo de trabalho.
- **`1_gerar_grade_curricular.py`**: Script para gerar a grade curricular dos cursos.
- **`2_gerar_dados_alunos.py`**: Script para gerar dados fictícios dos alunos.
- **`3_carregar_dados_camada_raw.py`**: Script para carregar os dados brutos na camada `raw` do data lake.
- **`5_normaliza_dados.py`**: Script para normalizar os dados brutos e prepará-los para a camada de consumo.
- **`6_carregar_dados_consume_zone.py`**: Script para carregar os dados normalizados na camada `consume` do data lake.
- **`Trabalho Prático.docx`**: Documento com as instruções e descrição do problema.
- **`Trabalho Prático.pdf`**: Relatório do trabalho em formato PDF.

## Dependências

Para executar este projeto, você precisará das seguintes dependências:

- **Python 3.x**
- **Apache Airflow**
- **Pandas**
- **Faker** (para geração de dados fictícios)
- **Azure Storage Blob** (para carregamento de dados no Azure Data Lake)

Você pode instalar as dependências do Python usando o seguinte comando:

```bash
pip install pandas faker azure-storage-blob