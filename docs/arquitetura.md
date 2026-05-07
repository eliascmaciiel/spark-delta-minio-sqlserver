# Arquitetura do Pipeline

1. **Origem relacional**: SQL Server (SeguroDB).
2. **Landing zone**: MinIO bucket `landing-zone` com CSV por tabela.
3. **Bronze**: MinIO bucket `bronze` com tabelas Delta.
4. **Processamento**: PySpark com integração JDBC + S3A + Delta Lake.
5. **Consistência**: DML no bronze para simular manutenção de dados.
