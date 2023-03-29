from enum import Enum


class Trackers(Enum):
    Cuisine = 1
    Cost_Bracket = 2


class AllTrackers:
    trackers = [Trackers.Cuisine, Trackers.Cost_Bracket]