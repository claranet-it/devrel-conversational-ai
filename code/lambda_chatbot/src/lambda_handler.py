from src.warehouse_service import get_movements_by_warehouse_and_date


def lambda_handler(event, context):
    slots = event['currentIntent']['slots']
    warehouse = slots['warehouse']
    date = slots['date']

    movements = get_movements_by_warehouse_and_date(warehouse, date)
    if movements:
        movement_list = ", ".join(m.__str__() for m in movements)
        response_message = f"Sure, here is the list of movements: {movement_list}."
    else:
        response_message = "There are no recorded movements for the given warehouse and date."

    return {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': response_message
            }
        }
    }

