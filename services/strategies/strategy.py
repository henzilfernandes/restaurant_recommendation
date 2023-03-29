from abc import ABC, abstractmethod
from typing import List

from constants.cuisines import Cuisine
from models.restaurant import Restaurant


class Options:
    primary_cuisine: Cuisine
    secondary_cuisines: set[Cuisine]
    primary_cost_bracket: int
    secondary_cost_brackets: set[int]

    def __init__(self, primary_cuisine=None, secondary_cuisines=None, primary_cost_bracket=None,
                 secondary_cost_brackets=None):
        if secondary_cost_brackets is None:
            secondary_cost_brackets = set()
        if secondary_cuisines is None:
            secondary_cuisines = set()
        self.primary_cuisine = primary_cuisine
        self.secondary_cuisines = secondary_cuisines
        self.primary_cost_bracket = primary_cost_bracket
        self.secondary_cost_brackets = secondary_cost_brackets


class Strategy(ABC):
    def __init__(self, priority):
        self._priority = priority

    @property
    def priority(self):
        return self._priority

    @abstractmethod
    def perform(self, result: List[Restaurant], available_restaurants: List[Restaurant], options: Options):
        pass
