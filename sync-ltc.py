import boto3
import os

bucket = boto3.resource("s3").Bucket("agriculture-vlab-data")
for obj in bucket.objects.filter(Prefix="ltc/", MaxKeys=1000):
    dest = os.path.join("/home/jovyan/LTC/", obj.key[4:])
    destdir = os.path.dirname(dest)
    os.makedirs(destdir, exist_ok=True)
    bucket.download_file(obj.key, dest)
