class CostTracking:
    type: int
    no_of_orders: int

    def __init__(self, cost_type: int, no_of_orders: int):
        self.type = cost_type
        self.no_of_orders = no_of_orders
