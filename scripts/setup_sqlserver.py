from pathlib import Path
import time
import pyodbc
from common import env

BASE_CONN = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={env('SQLSERVER_HOST')},{env('SQLSERVER_PORT')};"
    f"UID={env('SQLSERVER_USER')};PWD={env('SA_PASSWORD')};"
    "TrustServerCertificate=yes;"
)


def wait_for_sqlserver(max_attempts: int = 30, sleep_seconds: int = 5) -> None:
    for attempt in range(1, max_attempts + 1):
        try:
            with pyodbc.connect(BASE_CONN, timeout=5):
                print("SQL Server disponível.")
                return
        except pyodbc.Error:
            print(f"Tentativa {attempt}/{max_attempts}: aguardando SQL Server...")
            time.sleep(sleep_seconds)
    raise RuntimeError("SQL Server não ficou disponível a tempo.")


def execute_sql_file(cursor: pyodbc.Cursor, sql_file: Path) -> None:
    sql_text = sql_file.read_text(encoding="utf-8")
    for batch in [b.strip() for b in sql_text.split("GO") if b.strip()]:
        cursor.execute(batch)


if __name__ == "__main__":
    wait_for_sqlserver()
    with pyodbc.connect(BASE_CONN, autocommit=True) as conn:
        cursor = conn.cursor()
        for file_name in ["01_create_database.sql", "02_create_tables.sql", "03_insert_sample_data.sql"]:
            sql_path = Path("sql") / file_name
            print(f"Executando {sql_path}")
            execute_sql_file(cursor, sql_path)
    print("SQL Server preparado com sucesso.")
