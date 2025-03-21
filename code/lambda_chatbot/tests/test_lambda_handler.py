from src.lambda_handler import lambda_handler


def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert response['body'] == '"Hello from Lambda!"'