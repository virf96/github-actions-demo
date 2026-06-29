import io

from google.cloud import storage

from config import BUCKET_NAME


def upload_json(blob_path, data):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(blob_path)
    blob.upload_from_string(data, content_type="application/json")


def upload_parquet(blob_path, dataframe):
    buffer = io.BytesIO()
    dataframe.to_parquet(buffer, index=False)
    buffer.seek(0)

    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(blob_path)
    blob.upload_from_file(buffer, content_type="application/octet-stream")
