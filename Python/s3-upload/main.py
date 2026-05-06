import os
import boto3
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id=os.getenv("AWS_ACCESS_KEY")
aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
aws_s3_bucket_name=os.getenv("AWS_S3_BUCKET_NAME")
region_name=os.getenv("AWS_REGION")

local_file='testfile.txt'
name_for_s3='testfile.txt'

def main():
    print('in main method')

    s3_client = boto3.client(
        service_name='s3',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    response = s3_client.upload_file(local_file, aws_s3_bucket_name, name_for_s3)

    print(f'upload file response: {response}')


if __name__ == '__main__':
    main()