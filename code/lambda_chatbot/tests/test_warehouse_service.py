from src.lambda_handler import lambda_handler
from src.warehouse_service import get_movements_by_warehouse_and_date
from src.warehouse_movement_item import WarehouseMovementItem


def test_get_movements_by_warehouse_and_date():
    movements = get_movements_by_warehouse_and_date(
        warehouse='Warehouse_A',
        operation_date='2023-10-06'
    )

    assert len(movements) == 1
    assert "[Operation #909828eb]  Item: Noise Cancelling Headphones - Qty: 12 - DestinationWarehouse_C" == movements[0].__str__()


def test_get_empty_movements_by_warehouse_and_date():
    movements = get_movements_by_warehouse_and_date(
        warehouse='Warehouse_A',
        operation_date='2020-11-11'
    )

    assert len(movements) == 0
    assert movements == []