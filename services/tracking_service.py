from constants.cost_brackets import AllCostBrackets
from constants.cuisines import AllCuisines, Cuisine
from constants.tracking import Trackers
from models.user import User


class TrackingService:
    secondary_categories_count = 2

    @classmethod
    def get_tracking_data(cls, user: User, tracking_type: Trackers):
        if tracking_type == Trackers.Cuisine:
            return user.cuisines
        if tracking_type == Trackers.Cost_Bracket:
            return user.cost_bracket

    @classmethod
    def get_tracker_categories(cls, tracking_type: Trackers):
        if tracking_type == Trackers.Cuisine:
            return AllCuisines.cuisines
        if tracking_type == Trackers.Cost_Bracket:
            return AllCostBrackets.brackets

    @classmethod
    def get_tracker_insights(cls, user: User, tracking_type: Trackers):
        """
        calculates and returns primary and secondary for a given user and give tracker type
        :param user:
        :param tracking_type
        :return: primary_tracker, secondary_trackers
        """

        tracking_data = cls.get_tracking_data(user, tracking_type)

        tracker_orders = {}
        # create aggregation map for tracker to no of orders
        for tracker_data in tracking_data:
            if tracker_data.type not in tracker_orders:
                tracker_orders[tracker_data.type] = tracker_data.no_of_orders
            else:
                tracker_orders[tracker_data.type] += tracker_data.no_of_orders

        primary_category = None
        secondary_categories = set()
        max_orders = -1
        # figure out primary tracker and secondary trackers from aggregated tracking data
        sorted_tracker_orders = sorted(tracker_orders.items(), key=lambda x:x[1], reverse=True)
        if len(sorted_tracker_orders) >= 1:
            primary_category = sorted_tracker_orders[0][0]

        secondary_tracker_orders = sorted_tracker_orders[1:1+cls.secondary_categories_count]
        for secondary_tracker_order in secondary_tracker_orders:
            secondary_categories.add(secondary_tracker_order[0])

        return primary_category, secondary_categories
