from enum import Enum


class Cuisine(Enum):
    south_indian = 1
    north_indian = 2
    chinese = 3


class AllCuisines:
    cuisines = [Cuisine.south_indian, Cuisine.north_indian, Cuisine.chinese]

