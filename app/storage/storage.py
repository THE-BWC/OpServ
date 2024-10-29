from app.config import BaseConfig
from .local_storage import LocalStorage
from .s3_storage import S3Storage

def storage(s_type):
    if s_type == "local":
        return  LocalStorage(BaseConfig.LOCAL_STORAGE_PATH)
    else:
        return S3Storage(
            BaseConfig.S3_ENDPOINT,
            BaseConfig.S3_ACCESS_KEY,
            BaseConfig.S3_SECRET_KEY,
            BaseConfig.S3_SECURE,
            BaseConfig.S3_BUCKET
        )
