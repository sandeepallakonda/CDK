import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    buckets = s3.list_buckets()
    bucket_names = [b['cdk003'] for b in buckets['Buckets']]

    return {
        'statusCode': 200,
        'body': json.dumps(bucket_names)
    }
