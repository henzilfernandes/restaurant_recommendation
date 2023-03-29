import logging
from typing import List

from constants.cuisines import Cuisine
from models.cost_tracking import CostTracking
from models.cuisine_tracking import CuisineTracking
from models.user import User


class UserService:
    users: List[User] = []
    logger = logging.getLogger()

    @classmethod
    def get_cuisines(cls, cuisine_tracking):
        if not cuisine_tracking:
            return []
        cuisines: List[CuisineTracking] = []
        for cuisine in cuisine_tracking:
            cuisines.append(CuisineTracking(Cuisine[cuisine["type"]], cuisine["no_of_orders"]))
        return cuisines

    @classmethod
    def get_cost_brackets(cls, cost_tracking):
        if not cost_tracking:
            return []
        cost_brackets: List[CostTracking] = []
        for cost_bracket in cost_tracking:
            cost_brackets.append(CostTracking(cost_bracket["type"], cost_bracket["no_of_orders"]))
        return cost_brackets

    @classmethod
    def add_user(cls, payload):
        """
        creates a new user with it cost and cuisine tracking data
        :param payload: {"cuisine_tracking": [{"type": "south_indian", "no_of_orders": 5}], "cost_tracking":
        [{"type": 2, "no_of_orders": 4}]}
        :return: user
        """
        try:
            cuisines: List[CuisineTracking] = []
            if payload.get("cuisine_tracking"):
                for cuisine in payload["cuisine_tracking"]:
                    cuisines.append(CuisineTracking(Cuisine[cuisine["type"]], cuisine["no_of_orders"]))

            user = User(cuisines=cls.get_cuisines(payload.get("cuisine_tracking")),
                        cost_bracket=cls.get_cost_brackets(payload.get("cost_tracking")))
            cls.users.append(user)
            return user
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to add user {payload} error {ex}, traceback {traceback.format_exc()}")
            return None

    @classmethod
    def update_user(cls, user_id, payload):
        """
        updates existing user data with cost and cuisine tracking
        :param payload: {"cuisine_tracking": [{"type": "south_indian", "no_of_orders": 5}], "cost_tracking":
        [{"type": 2, "no_of_orders": 4}]}
        :param user_id: user id of user
        :return: user
        """
        try:
            user = cls.get_user(user_id)
            if not user:
                return None
            if payload.get("cuisine_tracking"):
                cuisines = user.cuisines()
                cuisines.extend(cls.get_cuisines(payload.get("cuisine_tracking")))
            if payload.get("cost_tracking"):
                cost_brackets = user.cost_bracket()
                cost_brackets.extend(cls.get_cost_brackets(payload["cost_tracking"]))
            return user
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to update user {payload}, error {ex}, traceback {traceback.format_exc()}")
            return None

    @classmethod
    def delete_user(cls, user_id):
        """
        deletes user for given user id
        :param user_id:
        :return: user
        """
        try:
            user = cls.get_user(user_id)
            if not user:
                return None
            user.active(False)
            return user
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to delete user id {user_id}, error {ex}, traceback {traceback.format_exc()}")
            return None

    @classmethod
    def get_user(cls, user_id):
        """
        gets user for give user id if active
        :param user_id:
        :return: user
        """
        try:
            for user in cls.users:
                if user.user_id == user_id and user.active:
                    return user
            cls.logger.error(f"no user with user id {user_id}")
            return None
        except Exception as ex:
            import traceback
            cls.logger.error(f"failed to get user {user_id}, error {ex}, traceback {traceback.format_exc()}")
            return None
