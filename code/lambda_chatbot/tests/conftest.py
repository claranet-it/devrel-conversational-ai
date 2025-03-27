import pytest


@pytest.fixture
def good_request_event():
    return {
        "currentIntent": {
            "slots": {
                "warehouse": "Warehouse_A",
                "date": "2023-10-06"
            }
        }
    }


@pytest.fixture
def bad_request_event():
    return {
        "currentIntent": {
            "slots": {
                "warehouse": "Warehouse_A",
                "date": "2017-11-11"
            }
        }
    }