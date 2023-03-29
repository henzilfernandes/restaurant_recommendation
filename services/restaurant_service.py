import logging
from typing import List

from models.restaurant import Restaurant


class RestaurantService:
    restaurants: List[Restaurant] = []
    logger = logging.getLogger()

    @classmethod
    def add_restaurant(cls, payload):
        """
        creates restaurant with given restaurant info
        :param payload: {"restaurant_id": "3455", "cuisine": "south_indian", "cost_bracket": 2, "rating": 3,
        "is_recommended": true}
        :return: restaurant
        """
        try:
            restaurant = Restaurant(restaurant_id=payload.get("restaurant_id"), cuisine=payload.get("cuisine"),
                                    cost_bracket=payload.get("cost_bracket"), rating=payload.get("rating"),
                                    is_recommended=payload.get("is_recommended"))
            cls.restaurants.append(restaurant)
            return restaurant
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to add restaurant {payload}, ex {ex}, traceback {traceback.format_exc()}")
            return None

    @classmethod
    def update_restaurant(cls, restaurant_id, payload):
        """
        updates restaurant details for given restaurant id
        :param restaurant_id:
        :param payload: {"cuisine": "south_indian", "cost_bracket": 2, "rating": 3,
        "is_recommended": true}
        :return: restaurant
        """
        try:
            restaurant = cls.get_restaurant(restaurant_id)
            if not restaurant:
                return None

            if payload.get("cuisine"):
                restaurant.cuisine(payload["cuisine"])
            if payload.get("cost_bracket") is not None:
                restaurant.cost_bracket(payload["cost_bracket"])
            if payload.get("rating") is not None:
                restaurant.rating(payload["rating"])
            if payload.get("is_recommended") is not None:
                restaurant.is_recommended(payload["is_recommended"])
            return restaurant
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to update restaurant id {restaurant_id} payload {payload}, error {ex}, traceback "
                          f"{traceback.format_exc()}")
            return None

    @classmethod
    def delete_restaurant(cls, restaurant_id):
        try:
            for restaurant in cls.restaurants:
                if restaurant.restaurant_id == restaurant_id and restaurant.active():
                    restaurant.active(False)
                    return restaurant
            cls.logger.error(f"no restaurant with id {restaurant_id} for delete")
            return None
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to delete restaurant {restaurant_id}, error {ex}, "
                          f"traceback {traceback.format_exc()}")
            return None

    @classmethod
    def get_restaurant(cls, restaurant_id):
        """
        return restaurant details for given restaurant id
        :param restaurant_id:
        :return: restaurant
        """
        try:
            for restaurant in cls.restaurants:
                if restaurant.restaurant_id == restaurant_id and restaurant.active():
                    return restaurant
            cls.logger.info(f"no restaurant with give restaurant id {restaurant_id}")
            return None
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to get restaurant with id {restaurant_id}, error {ex}, traceback "
                             f"{traceback.format_exc()}")
            return None
