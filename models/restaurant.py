from datetime import datetime

from constants.cuisines import Cuisine
from utils.helpers import str_uuid


class Restaurant:
    _onboarded_time: datetime

    def __init__(self, restaurant_id=str_uuid(), cuisine="south_indian", cost_bracket=1, rating=1,
                 is_recommended=False):
        self._active = True
        self._onboarded_time = datetime.utcnow()
        self._restaurant_id = restaurant_id
        if cuisine == "south_indian":
            self._cuisine = Cuisine.south_indian
        elif cuisine == "north_indian":
            self._cuisine = Cuisine.north_indian
        else:
            self._cuisine = Cuisine.chinese
        self._cost_bracket = cost_bracket
        self._rating = rating
        self._is_recommended = is_recommended

    @property
    def restaurant_id(self):
        return self._restaurant_id

    @restaurant_id.setter
    def restaurant_id(self, u_id):
        self._restaurant_id = u_id

    @property
    def cuisine(self):
        return self._cuisine

    @property
    def cost_bracket(self):
        return self._cost_bracket

    @property
    def rating(self):
        return self._rating

    @property
    def is_recommended(self):
        return self._is_recommended

    @property
    def onboarded_time(self):
        return self._onboarded_time

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    @cuisine.setter
    def cuisine(self, cuisine_name):
        if cuisine_name == "north_indian":
            self._cuisine = Cuisine.north_indian
        elif cuisine_name == "chinese":
            self._cuisine = Cuisine.chinese
        else:
            self._cuisine = Cuisine.south_indian

    @cost_bracket.setter
    def cost_bracket(self, value):
        self._cost_bracket = value

    @rating.setter
    def rating(self, value):
        self._rating = value

    @is_recommended.setter
    def is_recommended(self, value):
        self._is_recommended = value

    def __str__(self):
        cuisine_str = ""
        if self._cuisine == Cuisine.south_indian:
            cuisine_str = "south indian"
        elif self._cuisine == Cuisine.north_indian:
            cuisine_str = "north indian"
        else:
            cuisine_str = "chinese"

        return f"restaurant id {self._restaurant_id}, cuisine {cuisine_str}, cost bracket {self._cost_bracket}, " \
               f"rating {self._rating}, recommended {self._is_recommended}, on boarded time {self._onboarded_time}"
