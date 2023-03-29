from constants.cuisines import Cuisine


class CuisineTracking:
    type: Cuisine
    no_of_orders: int

    def __init__(self, cuisine_type: Cuisine, no_of_orders: int):
        self.type = cuisine_type
        self.no_of_orders = no_of_orders
