import logging
from typing import List

from models.restaurant import Restaurant
from services.strategies.strategy import Strategy, Options


class PrimaryCuisineSecondaryCostGreater(Strategy):
    def __init__(self, priority):
        super().__init__(priority)
        self.logger = logging.getLogger()

    def perform(self, result: List[Restaurant], available_restaurants: List[Restaurant], options: Options):
        """
        All restaurants of Primary cuisine, secondary cost bracket with rating >= 4.5
        :param result:
        :param available_restaurants:
        :param options:
        :return:
        """
        self.logger.info("starting strategy PrimaryCuisineSecondaryCostGreater")
        if not available_restaurants:
            return result, available_restaurants

        primary_cuisine = options.primary_cuisine
        secondary_cost_brackets = options.secondary_cost_brackets
        remaining_restaurants: List[Restaurant] = []

        for restaurant in available_restaurants:
            if restaurant.rating < 4.5:
                remaining_restaurants.append(restaurant)
                continue
            if primary_cuisine and restaurant.cuisine == primary_cuisine and \
                    secondary_cost_brackets and restaurant.cost_bracket in secondary_cost_brackets:
                result.append(restaurant)
            else:
                remaining_restaurants.append(restaurant)
        return result, remaining_restaurants
