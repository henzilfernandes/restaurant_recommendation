import logging
from typing import List

from models.restaurant import Restaurant
from services.strategies.strategy import Strategy, Options


class SecondaryCuisinePrimaryCostGreater(Strategy):
    def __init__(self, priority):
        super().__init__(priority)
        self.logger = logging.getLogger()

    def perform(self, result: List[Restaurant], available_restaurants: List[Restaurant], options: Options):
        """
        All restaurants of secondary cuisine, primary cost bracket with rating >= 4.5
        :param result:
        :param available_restaurants:
        :param options:
        :return:
        """
        self.logger.info("starting strategy SecondaryCuisinePrimaryCostGreater")
        if not available_restaurants:
            return result, available_restaurants

        primary_cost_bracket = options.primary_cost_bracket
        secondary_cuisines = options.secondary_cuisines
        remaining_restaurants: List[Restaurant] = []
        for restaurant in available_restaurants:
            if restaurant.rating < 4.5:
                remaining_restaurants.append(restaurant)
                continue

            if primary_cost_bracket and primary_cost_bracket == restaurant.cost_bracket and \
                    secondary_cuisines and restaurant.cuisine in secondary_cuisines:
                result.append(restaurant)
            else:
                remaining_restaurants.append(restaurant)
        return result, remaining_restaurants
