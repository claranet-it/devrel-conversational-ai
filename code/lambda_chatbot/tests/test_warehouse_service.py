from warehouse_service import get_movements_by_warehouse_and_date


def test_get_movements_by_warehouse_and_date():
    movements = get_movements_by_warehouse_and_date(
        warehouse='a',
        operation_date='2023-10-06'
    )

    assert len(movements) == 1
    assert "[Operation #909828eb]  Item: Noise Cancelling Headphones - Qty: 12 - Destination: c" == movements[0].__str__()


def test_get_empty_movements_by_warehouse_and_date():
    movements = get_movements_by_warehouse_and_date(
        warehouse='a',
        operation_date='2020-11-11'
    )

    assert len(movements) == 0
    assert movements == []