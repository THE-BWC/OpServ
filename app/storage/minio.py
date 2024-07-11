from minio import Minio
from app.config import BaseConfig

storage_client = Minio(
    BaseConfig.MINIO_ENDPOINT,
    access_key=BaseConfig.MINIO_ACCESS_KEY,
    secret_key=BaseConfig.MINIO_SECRET_KEY,
    secure=BaseConfig.MINIO_SECURE
)
