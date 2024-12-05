from minio import Minio
from minio.error import S3Error
from app.log import LOG


class S3Storage:
    def __init__(
        self,
        endpoint: str,
        access_key: str,
        secret_key: str,
        secure: bool,
        bucket_name: str,
    ):
        self.bucket_name = bucket_name
        self.client = Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=() if secure else False,
        )

    def get_bucket(self):
        try:
            if not self.client.bucket_exists(self.bucket_name):
                self.client.make_bucket(self.bucket_name)
            return self.client
        except S3Error as exc:
            LOG.error("Error getting bucket: {}".format(exc))
            return None

    def create_bucket(self):
        try:
            if not self.client.bucket_exists(self.bucket_name):
                self.client.make_bucket(self.bucket_name)
            return self.bucket_name
        except S3Error as exc:
            LOG.error("Error creating bucket: {}".format(exc))
            return None

    def init(self):
        try:
            if self.client.bucket_exists(self.bucket_name):
                return self.bucket_name
            else:
                self.client.make_bucket(self.bucket_name)
                return self.bucket_name
        except S3Error as exc:
            LOG.error("Error initializing bucket: {}".format(exc))
            return None

    def upload_file(self, file_path, object_name):
        try:
            client = self.get_bucket()
            client.fput_object(self.bucket_name, object_name, file_path)
            return object_name
        except S3Error as exc:
            LOG.error("Error uploading file: {}".format(exc))
            return None

    def list_files(self):
        try:
            client = self.get_bucket()
            return client.list_objects(self.bucket_name)
        except S3Error as exc:
            LOG.error("Error listing files: {}".format(exc))
            return None

    def delete_file(self, object_name):
        try:
            client = self.get_bucket()
            client.remove_object(self.bucket_name, object_name)
            return object_name
        except S3Error as exc:
            LOG.error("Error deleting file: {}".format(exc))
            return None
