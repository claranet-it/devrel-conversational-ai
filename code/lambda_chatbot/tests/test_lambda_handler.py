from src.lambda_handler import lambda_handler


def test_good_request(good_request_event):
    context = {}
    response = lambda_handler(good_request_event, context)
    assert response['dialogAction']['message']['content'] == 'Sure, here is the list of movements: [Operation #909828eb]  Item: Noise Cancelling Headphones - Qty: 12 - DestinationWarehouse_C.'


def test_bad_request(bad_request_event):
    context = {}
    response = lambda_handler(bad_request_event, context)
    assert response['dialogAction']['message']['content'] == 'There are no recorded movements for the given warehouse and date.'