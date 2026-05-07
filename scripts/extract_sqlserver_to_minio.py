from common import build_spark, env

spark = build_spark("extract_sqlserver_to_minio")

jdbc_url = (
    f"jdbc:sqlserver://{env('SQLSERVER_HOST')}:{env('SQLSERVER_PORT')};"
    f"databaseName={env('SQLSERVER_DATABASE')};encrypt=false;trustServerCertificate=true"
)
properties = {
    "user": env("SQLSERVER_USER"),
    "password": env("SA_PASSWORD"),
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
}

query = """
(
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE='BASE TABLE'
  AND TABLE_CATALOG='SeguroDB'
  AND TABLE_SCHEMA='dbo'
) t
"""

for row in spark.read.jdbc(url=jdbc_url, table=query, properties=properties).collect():
    schema = row["TABLE_SCHEMA"]
    table = row["TABLE_NAME"]
    dbtable = f"{schema}.{table}"
    df = spark.read.jdbc(url=jdbc_url, table=dbtable, properties=properties)
    output = f"s3a://{env('LANDING_BUCKET')}/{table}/{table}.csv"
    df.coalesce(1).write.mode("overwrite").option("header", "true").csv(output)
    print(f"CSV salvo: {output}")

spark.stop()
