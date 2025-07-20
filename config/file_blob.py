from minio import Minio
from minio.error import S3Error

from config.config import debug, minio_access_key, minio_endpoint, minio_secret_key

try:
    # Initialize MinIO client
    minio_client = Minio(
        endpoint=minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=not debug,  # Set to True if using HTTPS
    )

    # Check if the connection is successful by listing buckets
    buckets = minio_client.list_buckets()
    print("MinIO Connection Successful. Buckets:", [bucket.name for bucket in buckets])
except S3Error as e:
    print("MinIO S3 Error:", e)
except Exception as e:
    print("MinIO Connection Error:", e)
