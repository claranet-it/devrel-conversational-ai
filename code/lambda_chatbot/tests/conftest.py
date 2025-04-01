import pytest


@pytest.fixture
def good_request_event():
    return {
        "currentIntent": {
            "slots": {
                "warehouse": "a",
                "date": "2023-10-06"
            }
        }
    }


@pytest.fixture
def bad_request_event():
    return {
        "currentIntent": {
            "slots": {
                "warehouse": "a",
                "date": "2017-11-11"
            }
        }
    }