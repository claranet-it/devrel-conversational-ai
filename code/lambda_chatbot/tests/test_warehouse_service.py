from src.lambda_handler import lambda_handler
from src.warehouse_service import get_movements_by_warehouse_and_date


def test_get_movements_by_warehouse_and_date():
    movements = get_movements_by_warehouse_and_date(
        warehouse='Warehouse_A',
        operation_date='2023-10-06'
    )

    expected_movements = [
        {
            "pk": "Warehouse_A",
            "sk": "2023-10-06",
            "item_description": "Noise Cancelling Headphones",
            "quantity": 12,
            "destination": "Warehouse_C",
            "operation_id": "909828eb"
        }
    ]

    assert len(movements) == 1
    assert movements == expected_movements


def test_get_empty_movements_by_warehouse_and_date():
    movements = get_movements_by_warehouse_and_date(
        warehouse='Warehouse_A',
        operation_date='2020-11-11'
    )

    assert len(movements) == 0
    assert movements == []