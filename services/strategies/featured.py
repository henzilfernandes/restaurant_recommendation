import copy
import logging
from typing import List

from models.restaurant import Restaurant
from services.strategies.strategy import Strategy, Options


class Featured(Strategy):
    def __init__(self, priority):
        super().__init__(priority)
        self.logger = logging.getLogger()

    def perform(self, result: List[Restaurant], available_restaurants: List[Restaurant], options: Options):
        """
        Featured restaurants of primary cuisine and primary cost bracket. If none, then all featured restaurants of
        primary cuisine, secondary cost and secondary cuisine, primary cost
        :param result:
        :param available_restaurants:
        :param options:
        :return:
        """
        self.logger.info("starting strategy Featured")
        if not available_restaurants:
            return result, available_restaurants

        primary_cuisine = options.primary_cuisine
        primary_cost_bracket = options.primary_cost_bracket

        remaining_restaurants: List[Restaurant] = []
        is_present = False
        for restaurant in available_restaurants:
            if restaurant.is_recommended and primary_cuisine and primary_cuisine == restaurant.cuisine and \
                    primary_cost_bracket and primary_cost_bracket == restaurant.cost_bracket:
                result.append(restaurant)
                is_present = True
            else:
                remaining_restaurants.append(restaurant)

        if is_present:
            return result, remaining_restaurants

        available_restaurants = copy.deepcopy(remaining_restaurants)
        remaining_restaurants = []

        secondary_cuisines = options.secondary_cuisines
        secondary_cost_brackets = options.secondary_cost_brackets

        for restaurant in available_restaurants:
            if not restaurant.is_recommended:
                remaining_restaurants.append(restaurant)
                continue
            if primary_cuisine and primary_cuisine == restaurant.cuisine and \
                    secondary_cost_brackets and restaurant.cost_bracket in secondary_cost_brackets:
                result.append(restaurant)
            elif primary_cost_bracket and primary_cost_bracket == restaurant.cost_bracket and \
                    secondary_cuisines and restaurant.cuisine in secondary_cuisines:
                result.append(restaurant)
            else:
                remaining_restaurants.append(restaurant)
        return result, remaining_restaurants
