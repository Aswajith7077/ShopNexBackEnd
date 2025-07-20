from config.file_blob import minio_client


class BucketService:
    def __init__(self, minio_client):
        self.minio_client = minio_client

    def create_bucket(self, bucket_name):
        if not self.minio_client.bucket_exists(bucket_name):
            self.minio_client.make_bucket(bucket_name)
        else:
            print(f"Bucket '{bucket_name}' already exists.")

    def delete_bucket(self, bucket_name):
        if self.minio_client.bucket_exists(bucket_name):
            self.minio_client.remove_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' deleted.")
        else:
            print(f"Bucket '{bucket_name}' does not exist.")



    def upload_file_to_minio(self,bucket_name, file_path, object_name=None):
        """
        Upload a file to a MinIO bucket.

        :param bucket_name: Name of the bucket to upload to.
        :param file_path: Path to the file to upload.
        :param object_name: Name of the object in the bucket. If not specified, file_path is used.
        :return: True if file was uploaded, else False.
        """
        try:
            if object_name is None:
                object_name = file_path

            minio_client.fput_object(bucket_name, object_name, file_path)
            print(
                f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}'."
            )
            return True
        except Exception as e:
            print(f"Error uploading file: {e}")
            return False


    def list_files_in_bucket(self,bucket_name):
        """
        List files in a MinIO bucket.

        :param bucket_name: Name of the bucket to list files from.
        :return: List of file names in the bucket.
        """
        try:
            objects = minio_client.list_objects(bucket_name)
            file_list = [obj.object_name for obj in objects]
            print(f"Files in bucket '{bucket_name}': {file_list}")
            return file_list
        except Exception as e:
            print(f"Error listing files: {e}")
            return []


    def delete_file_from_minio(self,bucket_name, object_name):
        """
        Delete a file from a MinIO bucket.

        :param bucket_name: Name of the bucket to delete from.
        :param object_name: Name of the object to delete.
        :return: True if file was deleted, else False.
        """
        try:
            minio_client.remove_object(bucket_name, object_name)
            print(f"File '{object_name}' deleted from bucket '{bucket_name}'.")
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False

    def get_file_url(self,bucket_name, object_name, expiry=3600):
        """
        Generate a presigned URL for a file in a MinIO bucket.

        :param bucket_name: Name of the bucket.
        :param object_name: Name of the object.
        :param expiry: Expiry time in seconds for the presigned URL.
        :return: Presigned URL for the file.
        """
        try:
            url = minio_client.presigned_get_object(bucket_name, object_name, expires=expiry)
            print(f"Presigned URL for '{object_name}': {url}")
            return url
        except Exception as e:
            print(f"Error generating presigned URL: {e}")
            return None
    
    def download_file_from_minio(self,bucket_name, object_name, file_path):
        """
        Download a file from a MinIO bucket.

        :param bucket_name: Name of the bucket to download from.
        :param object_name: Name of the object to download.
        :param file_path: Path where the file will be saved.
        :return: True if file was downloaded, else False.
        """
        try:
            minio_client.fget_object(bucket_name, object_name, file_path)
            print(f"File '{object_name}' downloaded from bucket '{bucket_name}' to '{file_path}'.")
            return True
        except Exception as e:
            print(f"Error downloading file: {e}")
            return False
    
