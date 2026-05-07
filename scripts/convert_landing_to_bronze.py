from common import build_spark, env

spark = build_spark("convert_landing_to_bronze")

tables = [
    "clientes", "enderecos", "corretores", "produtos_seguro", "apolices", "parcelas",
    "sinistros", "pagamentos", "veiculos", "imoveis", "beneficiarios"
]

for table in tables:
    landing_path = f"s3a://{env('LANDING_BUCKET')}/{table}"
    bronze_path = f"s3a://{env('BRONZE_BUCKET')}/{table}"
    df = spark.read.option("header", "true").csv(landing_path)
    df.write.format("delta").mode("overwrite").save(bronze_path)
    print(f"Delta salvo em {bronze_path}")

spark.stop()
