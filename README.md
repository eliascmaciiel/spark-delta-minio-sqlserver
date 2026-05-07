# Trabalho 2 - Arquitetura de Dados (Repositório Separado do Trabalho 1)

Projeto acadêmico reprodutível com **Apache Spark + SQL Server + MinIO + Delta Lake**.

## Objetivo
Pipeline local para:
1. Extrair todas as tabelas de `SeguroDB` (SQL Server).
2. Salvar CSV em `landing-zone`.
3. Ler CSV e converter para Delta.
4. Salvar Delta em `bronze`.
5. Executar DML (INSERT/UPDATE/DELETE) em tabelas Delta.

## Arquitetura
Consulte `docs/arquitetura.md`.

## Pré-requisitos
- Docker + Docker Compose
- Python 3.11+
- UV
- Java/JDK 11+
- Driver ODBC 18 para SQL Server (para `pyodbc`)

## Configuração
```bash
cp .env.example .env
```
> A senha `SA_PASSWORD` deve respeitar as regras do SQL Server (forte, com maiúscula, minúscula, número e símbolo).

## Subir containers
```bash
docker compose up -d
docker compose ps
```

Serviços/portas padrão:
- SQL Server: `localhost:1433`
- MinIO API: `http://localhost:9000`
- MinIO Console: `http://localhost:9001`

## Ambiente Python (UV)
### Windows (PowerShell)
```powershell
uv venv
.venv\Scripts\activate
uv sync
```

### Linux/macOS
```bash
uv venv
source .venv/bin/activate
uv sync
```

## Sobre o uv.lock
Este repositório **não versiona `uv.lock` manual/placeholder**.
Gere localmente com:
```bash
uv lock
# ou
uv sync
```

## Ordem de execução (scripts)
```bash
python scripts/create_buckets.py
python scripts/setup_sqlserver.py
python scripts/extract_sqlserver_to_minio.py
python scripts/convert_landing_to_bronze.py
python scripts/dml_delta_bronze.py
```

## Notebooks
- `notebooks/01_setup_sqlserver.ipynb`
- `notebooks/02_extract_to_landing_zone.ipynb`
- `notebooks/03_convert_landing_to_bronze_delta.ipynb`
- `notebooks/04_dml_delta_bronze.ipynb`

## Validação
- Buckets no Console MinIO (`localhost:9001`): `landing-zone` e `bronze`.
- CSV por tabela: `s3a://landing-zone/<tabela>/<tabela>.csv`.
- Delta por tabela: `s3a://bronze/<tabela>`.
- DML: script mostra SELECT antes/depois para `clientes`, `apolices`, `sinistros`.

## Observação sobre carga inicial
`convert_landing_to_bronze.py` usa `mode("overwrite")` para carga inicial da camada bronze.

## Troubleshooting
- JDBC/driver: confira pacote `com.microsoft.sqlserver:mssql-jdbc`.
- S3A/MinIO: confira `MINIO_ENDPOINT`, credenciais e `path.style.access=true`.
- SQL Server indisponível: aguarde subir container; `setup_sqlserver.py` possui espera ativa.
- Delta: confirme extensões Delta no `SparkSession`.
