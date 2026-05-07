USE SeguroDB;
GO
INSERT INTO clientes VALUES
(1,'Ana Lima','111.111.111-11','ana@email.com','11999990001','2024-01-10'),
(2,'Bruno Rocha','222.222.222-22','bruno@email.com','11999990002','2024-02-11'),
(3,'Carla Souza','333.333.333-33','carla@email.com','11999990003','2024-03-12');
INSERT INTO enderecos VALUES
(1,1,'São Paulo','SP','Rua A','100'),(2,2,'Campinas','SP','Rua B','200'),(3,3,'Santos','SP','Rua C','300');
INSERT INTO corretores VALUES
(1,'João Vendas','CRECI123','Capital'),(2,'Maria Broker','CRECI456','Interior');
INSERT INTO produtos_seguro VALUES
(1,'Auto Premium','Auto',2500.00),(2,'Residencial Plus','Residencial',1800.00),(3,'Vida Total','Vida',1300.00);
INSERT INTO apolices VALUES
(1,1,1,1,'2025-01-01','2025-12-31','ATIVA'),(2,2,2,2,'2025-02-01','2026-01-31','ATIVA'),(3,3,1,3,'2025-03-01','2026-02-28','ATIVA');
INSERT INTO parcelas VALUES
(1,1,1,500.00,'2025-01-10','PAGO'),(2,1,2,500.00,'2025-02-10','PENDENTE'),(3,2,1,450.00,'2025-02-15','PAGO');
INSERT INTO sinistros VALUES
(1,1,'2025-04-10','Colisão leve',2200.00,'EM_ANALISE'),(2,2,'2025-04-20','Dano elétrico',12000.00,'APROVADO');
INSERT INTO pagamentos VALUES
(1,1,'2025-01-09',500.00,'PIX'),(2,3,'2025-02-14',450.00,'CARTAO');
INSERT INTO veiculos VALUES
(1,1,'ABC1D23','Corolla',2022),(2,2,'XYZ9K88','Onix',2021);
INSERT INTO imoveis VALUES
(1,2,'Apartamento','Campinas',450000.00),(2,3,'Casa','Santos',820000.00);
INSERT INTO beneficiarios VALUES
(1,3,'Daniel Souza','Filho',60.00),(2,3,'Elisa Souza','Cônjuge',40.00);
GO
