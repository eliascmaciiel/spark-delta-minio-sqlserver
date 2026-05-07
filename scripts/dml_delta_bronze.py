from common import build_spark, env

spark = build_spark("dml_delta_bronze")
spark.sql("CREATE DATABASE IF NOT EXISTS bronze")

tables = ["clientes", "apolices", "sinistros"]
for t in tables:
    spark.sql(f"DROP TABLE IF EXISTS bronze.{t}")
    spark.sql(f"CREATE TABLE bronze.{t} USING DELTA LOCATION 's3a://{env('BRONZE_BUCKET')}/{t}'")

print("ANTES - clientes")
spark.sql("SELECT * FROM bronze.clientes ORDER BY cliente_id").show(truncate=False)
spark.sql("INSERT INTO bronze.clientes VALUES (99,'Novo Cliente','999.999.999-99','novo@email.com','11990000000','2026-01-01')")
print("DEPOIS INSERT - clientes")
spark.sql("SELECT * FROM bronze.clientes ORDER BY cliente_id").show(truncate=False)

print("ANTES - apolices")
spark.sql("SELECT * FROM bronze.apolices ORDER BY apolice_id").show(truncate=False)
spark.sql("UPDATE bronze.apolices SET status='CANCELADA' WHERE apolice_id=2")
print("DEPOIS UPDATE - apolices")
spark.sql("SELECT * FROM bronze.apolices ORDER BY apolice_id").show(truncate=False)

print("ANTES - sinistros")
spark.sql("SELECT * FROM bronze.sinistros ORDER BY sinistro_id").show(truncate=False)
spark.sql("DELETE FROM bronze.sinistros WHERE sinistro_id=1")
print("DEPOIS DELETE - sinistros")
spark.sql("SELECT * FROM bronze.sinistros ORDER BY sinistro_id").show(truncate=False)

spark.stop()
