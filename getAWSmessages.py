import os
import boto3
from dotenv import load_dotenv
import json

load_dotenv()

AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')
QUEUE_URL = os.getenv('QUEUE_URL')

sqs_client = boto3.client('sqs')
resp = sqs_client.receive_message(
    QueueUrl=QUEUE_URL,
    AttributeNames=['All'],
    MaxNumberOfMessages=10
)

json_formatted_str = json.dumps(resp, indent=2)

print(json_formatted_str)