from typing import List

from models.cost_tracking import CostTracking
from models.cuisine_tracking import CuisineTracking
from utils.helpers import str_uuid


class User:
    _user_id: str

    def __init__(self, cuisines=None, cost_bracket=None):
        if cost_bracket is None:
            cost_bracket = []
        if cuisines is None:
            cuisines = []
        self._user_id = str_uuid()
        self._active = True
        self._cuisines = cuisines
        self._cost_bracket = cost_bracket

    @property
    def cost_bracket(self):
        return self._cost_bracket

    @property
    def cuisines(self):
        return self._cuisines

    @cuisines.setter
    def cuisines(self, _cuisine_tracking: List[CuisineTracking]):
        self._cuisines = []
        for cuisine in _cuisine_tracking:
            self._cuisines.append(cuisine)

    @cost_bracket.setter
    def cost_bracket(self, _cost_tracking: List[CostTracking]):
        self._cost_bracket = []
        for cost_tracking in _cost_tracking:
            self._cost_bracket.append(cost_tracking)

    @property
    def user_id(self):
        return self._user_id

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    def __str__(self):
        return f"user id {self._user_id}, cuisines {self._cuisines}, cost bracket {self._cost_bracket}"
