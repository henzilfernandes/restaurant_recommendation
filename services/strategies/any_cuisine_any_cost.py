import logging
from typing import List

from models.restaurant import Restaurant
from services.strategies.strategy import Strategy, Options


class AnyCuisineAnyCost(Strategy):
    def __init__(self, priority):
        super().__init__(priority)
        self.logger = logging.getLogger()

    def perform(self, result: List[Restaurant], available_restaurants: List[Restaurant], options: Options):
        """
        All restaurants of any cuisine, any cost bracket
        :param result:
        :param available_restaurants:
        :param options:
        :return:
        """
        self.logger.info("starting strategy AnyCuisineAnyCost")
        if not available_restaurants:
            return result, available_restaurants

        result.extend(available_restaurants)
        return result, []
