USE SeguroDB;
GO

CREATE TABLE clientes (
  cliente_id INT PRIMARY KEY,
  nome VARCHAR(120),
  cpf VARCHAR(14),
  email VARCHAR(120),
  telefone VARCHAR(20),
  data_cadastro DATE
);
CREATE TABLE enderecos (
  endereco_id INT PRIMARY KEY,
  cliente_id INT,
  cidade VARCHAR(80),
  uf CHAR(2),
  logradouro VARCHAR(120),
  numero VARCHAR(10)
);
CREATE TABLE corretores (
  corretor_id INT PRIMARY KEY,
  nome VARCHAR(120),
  creci VARCHAR(30),
  regiao VARCHAR(60)
);
CREATE TABLE produtos_seguro (
  produto_id INT PRIMARY KEY,
  nome_produto VARCHAR(120),
  tipo VARCHAR(40),
  premio_base DECIMAL(12,2)
);
CREATE TABLE apolices (
  apolice_id INT PRIMARY KEY,
  cliente_id INT,
  corretor_id INT,
  produto_id INT,
  data_inicio DATE,
  data_fim DATE,
  status VARCHAR(20)
);
CREATE TABLE parcelas (
  parcela_id INT PRIMARY KEY,
  apolice_id INT,
  numero_parcela INT,
  valor DECIMAL(12,2),
  vencimento DATE,
  status_pagamento VARCHAR(20)
);
CREATE TABLE sinistros (
  sinistro_id INT PRIMARY KEY,
  apolice_id INT,
  data_sinistro DATE,
  descricao VARCHAR(200),
  valor_reclamado DECIMAL(12,2),
  status VARCHAR(20)
);
CREATE TABLE pagamentos (
  pagamento_id INT PRIMARY KEY,
  parcela_id INT,
  data_pagamento DATE,
  valor_pago DECIMAL(12,2),
  forma_pagamento VARCHAR(30)
);
CREATE TABLE veiculos (
  veiculo_id INT PRIMARY KEY,
  cliente_id INT,
  placa VARCHAR(10),
  modelo VARCHAR(80),
  ano INT
);
CREATE TABLE imoveis (
  imovel_id INT PRIMARY KEY,
  cliente_id INT,
  tipo VARCHAR(40),
  cidade VARCHAR(80),
  valor_avaliado DECIMAL(14,2)
);
CREATE TABLE beneficiarios (
  beneficiario_id INT PRIMARY KEY,
  apolice_id INT,
  nome VARCHAR(120),
  parentesco VARCHAR(40),
  percentual_cobertura DECIMAL(5,2)
);
GO
