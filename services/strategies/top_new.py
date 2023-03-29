import logging
from datetime import datetime
from typing import List

from models.restaurant import Restaurant
from services.strategies.strategy import Strategy, Options


class TopNew(Strategy):
    def __init__(self, priority):
        super().__init__(priority)
        self.logger = logging.getLogger()

    def perform(self, result: List[Restaurant], available_restaurants: List[Restaurant], options: Options):
        """
        Top 4 newly created restaurants by rating
        :param result:
        :param available_restaurants:
        :param options:
        :return:
        """
        self.logger.info("starting strategy TopNew")
        if not available_restaurants:
            return result, available_restaurants

        sorted_restaurants = sorted(available_restaurants,
                                    key=lambda x: (x.onboarded_time.strftime('%m/%d/%Y %I:%M %p'), x.rating),
                                    reverse=True)
        result.extend(sorted_restaurants[0:4])
        return result, sorted_restaurants[4:]
