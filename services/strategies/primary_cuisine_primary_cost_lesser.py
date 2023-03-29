import logging
from typing import List

from models.restaurant import Restaurant
from services.strategies.strategy import Strategy, Options


class PrimaryCuisinePrimaryCostLesser(Strategy):
    def __init__(self, priority):
        super().__init__(priority)
        self.logger = logging.getLogger()

    def perform(self, result: List[Restaurant], available_restaurants: List[Restaurant], options: Options):
        """
        All restaurants of Primary cuisine, primary cost bracket with rating < 4
        :param result:
        :param available_restaurants:
        :param options:
        :return:
        """
        self.logger.info("starting strategy PrimaryCuisinePrimaryCostLesser")
        if not available_restaurants:
            return result, available_restaurants

        primary_cuisine = options.primary_cuisine
        primary_cost_bracket = options.primary_cost_bracket
        remaining_restaurants: List[Restaurant] = []
        for restaurant in available_restaurants:
            if restaurant.rating >= 4:
                remaining_restaurants.append(restaurant)
                continue

            if primary_cuisine and restaurant.cuisine == primary_cuisine and \
                    primary_cost_bracket and restaurant.cost_bracket == primary_cost_bracket:
                result.append(restaurant)
            else:
                remaining_restaurants.append(restaurant)
        return result, remaining_restaurants
