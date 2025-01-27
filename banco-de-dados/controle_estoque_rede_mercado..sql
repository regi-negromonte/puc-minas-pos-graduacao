CREATE TABLE Produto (
    ProdutoID serial PRIMARY KEY,
    Nome VARCHAR(100),
    Descricao TEXT,
    Preco DECIMAL(10, 2),
    Categoria VARCHAR(50)
);

CREATE TABLE Fornecedor (
    FornecedorID serial PRIMARY KEY,
    Nome VARCHAR(100),
    Contato VARCHAR(50),
    Endereco TEXT
);

CREATE TABLE Filial (
    FilialID serial PRIMARY KEY,
    Nome VARCHAR(100),
    Endereco TEXT,
    Cidade VARCHAR(50),
    Estado VARCHAR(50)
);

CREATE TABLE Estoque (
    EstoqueID serial PRIMARY KEY,
    ProdutoID INT,
    FilialID INT,
    Quantidade INT,
    DataAtualizacao DATE,
    FOREIGN KEY (ProdutoID) REFERENCES Produto (ProdutoID),
    FOREIGN KEY (FilialID) REFERENCES Filial (FilialID)
);

-- A tabela MovimentacaoCD é usada para registrar tanto as entradas quanto as saídas de produtos no centro de distribuição (CD).

CREATE TABLE MovimentacaoCD (
    MovimentacaoID serial,
    ProdutoID INT,
    TipoMovimentacao VARCHAR(10), -- 'Entrada' ou 'Saída' conforme CONSTRAINT abaixo
    DataMovimentacao DATE,
    Quantidade INT,
    FilialID INT, -- Pode ser nulo para entradas NO CD
    PRIMARY KEY (MovimentacaoID, DataMovimentacao),
    FOREIGN KEY (ProdutoID) REFERENCES Produto (ProdutoID),
    FOREIGN KEY (FilialID) REFERENCES Filial (FilialID),
    CONSTRAINT chk_tipo_movimentacao CHECK (TipoMovimentacao IN ('Entrada', 'Saída'))
) PARTITION BY RANGE (DataMovimentacao);

-- Partições para a tabela MovimentacaoCD com base na data de movimentação dos produtos

CREATE TABLE MovimentacaoCD_2024 PARTITION OF MovimentacaoCD FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
CREATE TABLE MovimentacaoCD_2025 PARTITION OF MovimentacaoCD FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
-- Adicionar mais partições conforme necessário

-- Tabela que associa os produtos aos seus fornecedores

CREATE TABLE ProdutoFornecedor (
    ProdutoID INT,
    FornecedorID INT,
    PRIMARY KEY (ProdutoID, FornecedorID),
    FOREIGN KEY (ProdutoID) REFERENCES Produto (ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedor (FornecedorID)
);

	