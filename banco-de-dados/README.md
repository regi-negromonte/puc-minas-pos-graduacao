# Projeto de Banco de Dados para Controle de Estoque de uma Rede de Mercado

Este repositório contém o projeto de banco de dados desenvolvido para o controle de estoque de uma rede de mercado, como parte do curso de **Ciência de Dados e Big Data** da **Pontifícia Universidade Católica de Minas Gerais (PUC Minas)**.

## Objetivo do Projeto

**Este projeto tem caráter didático e não pretende ser um sistema completo de controle de estoque.** O objetivo principal é colocar em prática os conceitos aprendidos em banco de dados relacionais e não relacionais, aplicando técnicas como particionamento de dados e modelagem de tabelas em um cenário simples e controlado. O foco está na aprendizagem e na experimentação de ferramentas e estratégias para lidar com grandes volumes de dados.

## Estrutura do Banco de Dados

O banco de dados é composto pelas seguintes tabelas:

- **Produto**: Armazena informações sobre os produtos, como nome, descrição, preço e categoria.
- **Fornecedor**: Contém dados dos fornecedores, incluindo nome, contato e endereço.
- **Filial**: Registra informações sobre as filiais da rede, como nome, endereço, cidade e estado.
- **Estoque**: Controla a quantidade de produtos em cada filial, com a data da última atualização.
- **MovimentacaoCD**: Registra as movimentações de produtos no centro de distribuição (CD), incluindo entradas e saídas. Esta tabela é particionada por intervalo de datas para otimizar o desempenho.
- **ProdutoFornecedor**: Tabela associativa que relaciona produtos aos seus fornecedores.

### Particionamento de Dados

A tabela `MovimentacaoCD` foi particionada por intervalo de datas para melhorar o desempenho e a eficiência no armazenamento e recuperação de dados. O particionamento permite que consultas específicas em intervalos de datas sejam mais rápidas e que o gerenciamento de grandes volumes de dados seja mais eficaz.

Exemplo de partições criadas:
- `MovimentacaoCD_2024`: Para movimentações ocorridas em 2024.
- `MovimentacaoCD_2025`: Para movimentações ocorridas em 2025.

## Scripts SQL

O arquivo `controle_estoque_rede_mercado.sql` contém os scripts SQL para a criação das tabelas e partições do banco de dados. Este script pode ser executado em um sistema de gerenciamento de banco de dados PostgreSQL para criar a estrutura do banco de dados.

## Como Executar o Projeto

1. **Pré-requisitos**:
   - PostgreSQL instalado e configurado.
   - Acesso a um servidor de banco de dados PostgreSQL.

2. **Executando o Script SQL**:
   - Abra o terminal ou prompt de comando.
   - Conecte-se ao banco de dados PostgreSQL usando o comando `psql`.
   - Execute o script SQL com o comando `\i controle_estoque_rede_mercado.sql`.

3. **Testes e Simulações**:
   - Após a criação do banco de dados, você pode inserir dados de teste para simular o funcionamento do sistema.
   - Realize consultas e atualizações de estoque para verificar o desempenho do banco de dados.


**Nota**: Este projeto foi desenvolvido como parte de uma atividade avaliativa do curso de **Ciência de Dados e Big Data** da **PUC Minas**.

**Atenção**: Este projeto tem um propósito **didático** e não pretende ser um sistema completo de controle de estoque. O foco está na aplicação prática de conceitos de banco de dados, como particionamento e modelagem, em um cenário simples e controlado.