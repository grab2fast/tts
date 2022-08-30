import base64
import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    response = s3.get_object(
        Bucket="expressapi",
        Key=event['queryStringParameters']['filename'],
    )
    file = response['Body'].read()
    return {
        'headers': { "Content-Type": "audio/mpeg", 'Content-Disposition': "attachment; filename=speech.mp3" },
        'statusCode': 200,
        'body': base64.b64encode(file).decode('utf-8'),
        'isBase64Encoded': True
    }
