import boto3
import pandas as pd
import io
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    if not key.endswith('.csv'):
        return {
            'statusCode': 200,
            'body': 'Not a CSV file'
        }

    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    df = pd.read_csv(response['Body'])

    parquet_buffer = io.BytesIO()

    df.to_parquet(
        parquet_buffer,
        engine='pyarrow',
        index=False
    )

    filename = os.path.basename(key).replace('.csv', '.parquet')

    region = key.split('region=')[1].split('/')[0]

    parquet_key = (
        f'youtube/cleaned_statistics/'
        f'region={region}/{filename}'
    )

    s3.put_object(
        Bucket=bucket,
        Key=parquet_key,
        Body=parquet_buffer.getvalue()
    )

    return {
        'statusCode': 200,
        'body': f'Created {parquet_key}'
    }