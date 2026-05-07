import boto3
from common import env

s3 = boto3.client(
    "s3",
    endpoint_url=env("MINIO_ENDPOINT"),
    aws_access_key_id=env("MINIO_ROOT_USER"),
    aws_secret_access_key=env("MINIO_ROOT_PASSWORD"),
    region_name=env("MINIO_REGION", "us-east-1"),
)

for bucket in [env("LANDING_BUCKET", "landing-zone"), env("BRONZE_BUCKET", "bronze")]:
    existing = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]
    if bucket not in existing:
        s3.create_bucket(Bucket=bucket)
        print(f"Bucket criado: {bucket}")
    else:
        print(f"Bucket já existe: {bucket}")
