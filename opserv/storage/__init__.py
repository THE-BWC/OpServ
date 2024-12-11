import logging
from typing import Literal

from opserv.config import BaseConfig
from .local_storage import LocalStorage
from .s3_storage import S3Storage

log = logging.getLogger(__name__)


class StorageFactory:
    @staticmethod
    def create(type: Literal["local", "s3"]):
        match type:
            case "local":
                return LocalStorage(BaseConfig.LOCAL_STORAGE_PATH)
            case "s3":
                return S3Storage(
                    BaseConfig.S3_ENDPOINT,
                    BaseConfig.S3_ACCESS_KEY,
                    BaseConfig.S3_SECRET_KEY,
                    BaseConfig.S3_SECURE,
                    BaseConfig.S3_BUCKET,
                )
