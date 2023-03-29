import logging
from typing import List

from constants.tracking import Trackers
from models.restaurant import Restaurant
from models.user import User
from services.strategies.any_cuisine_any_cost import AnyCuisineAnyCost
from services.strategies.featured import Featured
from services.strategies.primary_cuisine_cost_greater import PrimaryCuisinePrimaryCostGreater
from services.strategies.primary_cuisine_primary_cost_lesser import PrimaryCuisinePrimaryCostLesser
from services.strategies.primary_cuisine_secondary_cost_greater import PrimaryCuisineSecondaryCostGreater
from services.strategies.primary_cuisine_secondary_cost_lesser import PrimaryCuisineSecondaryCostLesser
from services.strategies.secondary_cuisine_primary_cost_greater import SecondaryCuisinePrimaryCostGreater
from services.strategies.secondary_cuisine_primary_cost_lesser import SecondaryCuisinePrimaryCostLesser
from services.strategies.strategy import Options, Strategy
from services.strategies.top_new import TopNew
from services.tracking_service import TrackingService


class RecommendationService:
    strategies: List[Strategy] = sorted([Featured(1), PrimaryCuisinePrimaryCostGreater(2),
                                        PrimaryCuisineSecondaryCostGreater(3), SecondaryCuisinePrimaryCostGreater(4),
                                        TopNew(5), PrimaryCuisinePrimaryCostLesser(6),
                                        PrimaryCuisineSecondaryCostLesser(7), SecondaryCuisinePrimaryCostLesser(8),
                                        AnyCuisineAnyCost(9)], key=lambda x: x.priority)
    logger = logging.getLogger()

    @classmethod
    def get_recommendations(cls, user: User, available_restaurants: List[Restaurant]):
        """
        return list of recommended restaurants from available restaurants for given user
        :param user: user object
        :param available_restaurants: list of restaurant objects
        :return: list of restaurants
        """
        try:
            primary_cuisine, secondary_cuisines = TrackingService.get_tracker_insights(user, Trackers.Cuisine)
            primary_cost_bracket, secondary_cost_brackets = \
                TrackingService.get_tracker_insights(user, Trackers.Cost_Bracket)
            options = Options(primary_cuisine=primary_cuisine, secondary_cuisines=secondary_cuisines,
                              primary_cost_bracket=primary_cost_bracket,
                              secondary_cost_brackets=secondary_cost_brackets)

            recommended_restaurants: List[Restaurant] = []
            for strategy in cls.strategies:
                recommended_restaurants, available_restaurants = strategy.perform(recommended_restaurants,
                                                                                  available_restaurants, options)

            return recommended_restaurants
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to get restaurant recommendation for user {user.user_id}, error {ex}, "
                             f"traceback {traceback.format_exc()}")
            return []
