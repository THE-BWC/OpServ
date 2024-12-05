import logging

from opserv.config import BaseConfig
from .local_storage import LocalStorage
from .s3_storage import S3Storage

log = logging.getLogger(__name__)


def storage(storage_type):
    if storage_type == "local":
        rt = LocalStorage(BaseConfig.LOCAL_STORAGE_PATH)
        return rt
    elif storage_type == "s3":
        rt = S3Storage(
            BaseConfig.S3_ENDPOINT,
            BaseConfig.S3_ACCESS_KEY,
            BaseConfig.S3_SECRET_KEY,
            BaseConfig.S3_SECURE,
            BaseConfig.S3_BUCKET,
        )
        return rt
