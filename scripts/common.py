import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()


def env(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        raise ValueError(f"Variável obrigatória ausente: {name}")
    return value


def build_spark(app_name: str) -> SparkSession:
    packages = ",".join([
        "io.delta:delta-spark_2.12:3.2.0",
        "org.apache.hadoop:hadoop-aws:3.3.4",
        "com.microsoft.sqlserver:mssql-jdbc:12.6.3.jre11",
    ])
    return (
        SparkSession.builder.appName(app_name)
        .master(env("SPARK_MASTER", "local[*]"))
        .config("spark.jars.packages", packages)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.hadoop.fs.s3a.endpoint", env("MINIO_ENDPOINT"))
        .config("spark.hadoop.fs.s3a.access.key", env("MINIO_ROOT_USER"))
        .config("spark.hadoop.fs.s3a.secret.key", env("MINIO_ROOT_PASSWORD"))
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
        .getOrCreate()
    )
