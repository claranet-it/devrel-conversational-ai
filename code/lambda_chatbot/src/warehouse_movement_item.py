class WarehouseMovementItem:
    def __init__(self,
                 source: str,
                 date: str,
                 item_description: str,
                 quantity: int,
                 destination: str,
                 operation_id: str
     ):
        self.source = source
        self.date = date
        self.item_description = item_description
        self.quantity = quantity
        self.destination = destination
        self.operation_id = operation_id

    def __str__(self):
        return f'[Operation #{self.operation_id}]  Item: {self.item_description} - Qty: {self.quantity} - Destination: {self.destination}'

    @staticmethod
    def from_dict(data):
        return WarehouseMovementItem(
            source=data["pk"],
            date=data["sk"],
            item_description=data["item_description"],
            quantity=data["quantity"],
            destination=data["destination"],
            operation_id=data["operation_id"]
        )
