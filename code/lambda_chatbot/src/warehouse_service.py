import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from warehouse_movement_item import WarehouseMovementItem

TABLE_NAME = 'devrel-chatbot-dev-warehouse'

def get_movements_by_warehouse_and_date(warehouse: str, operation_date: str) -> list[WarehouseMovementItem]:
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    try:
        response = table.query(
            KeyConditionExpression=Key('pk').eq(warehouse) &
                                   Key('sk').eq(operation_date)
        )

        items = response.get('Items', [])
        return [WarehouseMovementItem.from_dict(item) for item in items]

    except ClientError as e:
        print(f"Failed to retrieve items: {e.response['Error']['Message']}")
        return []