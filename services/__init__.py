from services.file_blob import BucketService
from config.file_blob import minio_client

bucket_service = BucketService(minio_client)