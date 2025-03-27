import boto3
import json
from botocore.exceptions import ClientError

TABLE_NAME = 'devrel-chatbot-dev-warehouse'
FIXTURE_PATH = '../../fixtures/warehouse.json'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

with open(FIXTURE_PATH, 'r') as file:
    items = json.load(file)

for item in items:
    try:
        table.put_item(Item=item)
        print(f"Inserted item: {item}")
    except ClientError as e:
        print(f"Failed to insert item: {e.response['Error']['Message']}")