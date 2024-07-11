import os
import logging
from .minio import storage_client
from minio.error import S3Error
from app.config import BaseConfig


def upload_file(file, object_name):
    if not file:
        return False

    try:
        size = os.fstat(file.fileno()).st_size
        storage_client.put_object(BaseConfig.MINIO_BUCKET, object_name, file, size)
        return True
    except S3Error as e:
        logging.error(f"Error uploading file: {e}")
        return False
