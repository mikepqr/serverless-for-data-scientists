import json
import pickle
from io import BytesIO

import boto3
from botocore.config import Config

s3client = boto3.client('s3', config=Config(signature_version='s3v4'))


def congfigure_bucket_as_website(bucket_name):
    s3client.create_bucket(Bucket=bucket_name)
    website_configuration = {
        "ErrorDocument": {"Key": "error.html"},
        "IndexDocument": {"Suffix": "index.html"},
    }
    s3client.put_bucket_website(Bucket=bucket_name,
                                WebsiteConfiguration=website_configuration)
    bucket_policy = json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": ["s3:GetObject"],
                    "Resource": ["arn:aws:s3:::{}/*".format(bucket_name)],
                }
            ],
        }
    )
    s3client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)


def pickle_to_s3(obj, bucket_name, key):
    congfigure_bucket_as_website(bucket_name)
    with BytesIO() as data:
        pickle.dump(obj, data)
        data.seek(0)
        s3client.create_bucket(Bucket=bucket_name)
        s3client.put_object(Body=data, Bucket=bucket_name, Key=key)


def pickle_from_s3(bucket_name, key):
    with BytesIO() as data:
        s3client.download_fileobj(Bucket=bucket_name, Key=key, Fileobj=data)
        data.seek(0)
        return pickle.load(data)
