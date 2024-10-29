import logging
from minio import Minio
from minio.error import S3Error

class S3Storage:
    def __init__(
        self,
        endpoint: str,
        access_key: str,
        secret_key: str,
        secure: bool,
        bucket_name: str,
    ):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.secure = secure
        self.bucket_name = bucket_name

    def get_client(self):
        return Minio(
            self.endpoint,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=self.secure
        )

    def get_bucket(self):
        try:
            client = self.get_client()
            if not client.bucket_exists(self.bucket_name):
                client.make_bucket(self.bucket_name)
            return client
        except S3Error as exc:
            logging.error("Error getting bucket: {}".format(exc))
            return None

    def create_bucket(self):
        try:
            client = self.get_client()
            if not client.bucket_exists(self.bucket_name):
                client.make_bucket(self.bucket_name)
            return self.bucket_name
        except S3Error as exc:
            logging.error("Error creating bucket: {}".format(exc))
            return None

    def init(self):
        try:
            client = self.get_client()
            if client.bucket_exists(self.bucket_name):
                return self.bucket_name
            else:
                client.make_bucket(self.bucket_name)
                return self.bucket_name
        except S3Error as exc:
            logging.error("Error initializing bucket: {}".format(exc))
            return None

    def upload_file(self, file_path, object_name):
        try:
            client = self.get_bucket()
            client.fput_object(self.bucket_name, object_name, file_path)
            return object_name
        except S3Error as exc:
            logging.error("Error uploading file: {}".format(exc))
            return None

    def list_files(self):
        try:
            client = self.get_bucket()
            return client.list_objects(self.bucket_name)
        except S3Error as exc:
            logging.error("Error listing files: {}".format(exc))
            return None

    def delete_file(self, object_name):
        try:
            client = self.get_bucket()
            client.remove_object(self.bucket_name, object_name)
            return object_name
        except S3Error as exc:
            logging.error("Error deleting file: {}".format(exc))
            return None
