import logging
import sys

from services.recommendation_service import RecommendationService
from services.restaurant_service import RestaurantService
from services.user_service import UserService

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

logger = logging.getLogger()


def create_users():
    payloads = [
        {"cuisine_tracking": [{"type": "south_indian", "no_of_orders": 5}, {"type": "north_indian", "no_of_orders": 2}],
         "cost_tracking": [{"type": 4, "no_of_orders": 2}, {"type": 3, "no_of_orders": 4}]}
    ]
    results = []
    for payload in payloads:
        user = UserService.add_user(payload)
        if user:
            results.append(user)
    logger.info("created users")
    for result in results:
        logger.info(result.__str__())
    return results


def create_restaurants():
    payloads = [
        {"restaurant_id": "1234", "cuisine": "south_indian", "cost_bracket": 1, "rating": 2.5, "is_recommended": False},
        {"restaurant_id": "1235", "cuisine": "south_indian", "cost_bracket": 1, "rating": 4.6, "is_recommended": False},
        {"restaurant_id": "1236", "cuisine": "south_indian", "cost_bracket": 2, "rating": 3, "is_recommended": False},
        {"restaurant_id": "1237", "cuisine": "south_indian", "cost_bracket": 2, "rating": 4.7, "is_recommended": False},
        {"restaurant_id": "1238", "cuisine": "south_indian", "cost_bracket": 3, "rating": 3.5, "is_recommended": True},
        {"restaurant_id": "1239", "cuisine": "south_indian", "cost_bracket": 3, "rating": 4.8, "is_recommended": False},
        {"restaurant_id": "1240", "cuisine": "south_indian", "cost_bracket": 4, "rating": 3.7, "is_recommended": False},
        {"restaurant_id": "1241", "cuisine": "south_indian", "cost_bracket": 4, "rating": 4.9, "is_recommended": False},
        {"restaurant_id": "1242", "cuisine": "north_indian", "cost_bracket": 1, "rating": 2.5, "is_recommended": False},
        {"restaurant_id": "1243", "cuisine": "north_indian", "cost_bracket": 1, "rating": 4.6, "is_recommended": False},
        {"restaurant_id": "1244", "cuisine": "north_indian", "cost_bracket": 2, "rating": 3, "is_recommended": False},
        {"restaurant_id": "1245", "cuisine": "south_indian", "cost_bracket": 2, "rating": 4.7, "is_recommended": False},
        {"restaurant_id": "1246", "cuisine": "north_indian", "cost_bracket": 3, "rating": 3.5, "is_recommended": False},
        {"restaurant_id": "1247", "cuisine": "south_indian", "cost_bracket": 3, "rating": 4.8, "is_recommended": False},
        {"restaurant_id": "1248", "cuisine": "north_indian", "cost_bracket": 4, "rating": 3.7, "is_recommended": False},
        {"restaurant_id": "1249", "cuisine": "north_indian", "cost_bracket": 4, "rating": 4.9, "is_recommended": False},
        {"restaurant_id": "1250", "cuisine": "chinese", "cost_bracket": 1, "rating": 2.5, "is_recommended": False},
        {"restaurant_id": "1251", "cuisine": "chinese", "cost_bracket": 1, "rating": 4.6, "is_recommended": False},
        {"restaurant_id": "1252", "cuisine": "chinese", "cost_bracket": 2, "rating": 3, "is_recommended": False},
        {"restaurant_id": "1253", "cuisine": "chinese", "cost_bracket": 2, "rating": 4.7, "is_recommended": False},
        {"restaurant_id": "1254", "cuisine": "chinese", "cost_bracket": 3, "rating": 3.5, "is_recommended": False},
        {"restaurant_id": "1255", "cuisine": "chinese", "cost_bracket": 3, "rating": 4.8, "is_recommended": False},
        {"restaurant_id": "1256", "cuisine": "chinese", "cost_bracket": 4, "rating": 3.7, "is_recommended": False}
    ]

    results = []
    for payload in payloads:
        restaurant = RestaurantService.add_restaurant(payload)
        if restaurant:
            results.append(restaurant)
    logger.info("created restaurants")
    for result in results:
        logger.info(result.__str__())
    return results


def get_recommendations(user_list, available_restaurants):
    for user in user_list:
        recommended_restaurants = RecommendationService.get_recommendations(user, available_restaurants)
        logger.info(f"recommended restaurants for user id {user.user_id}\n")
        for result in recommended_restaurants:
            logger.info(result.__str__())


if __name__ == '__main__':
    restaurants = create_restaurants()
    users = create_users()
    get_recommendations(users, restaurants)
