# A simple Python script to create an AWS S3 bucket
# Bucket names must be globally unique across all AWS accounts.
# Make sure you have configured your AWS credentials

import boto3
import sys


try:
    def main():
        create_s3bucket(bucket_name)

except Exception as e:
    print(e)   

# Create an S3 client with the specified region        

def create_s3bucket(bucket_name, region=""):
    s3_bucket=boto3.client(
        's3',
        region_name=region
    )

    bucket = s3_bucket.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': ''},
        ACL= 'private')

    print(bucket)

bucket_name = sys.argv[1]

if __name__ == '__main__':
    main() 

