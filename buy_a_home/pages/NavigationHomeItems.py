from enum import Enum

from framework.utils.DataReader import DataReader


class NavigationHomeItems(Enum):
    SELECT_HOME = DataReader.get_data("Navigation Items.select home")
    GET_FINANCING = DataReader.get_data("Navigation Items.get financing")
    DEED_TRANSFER = DataReader.get_data("Navigation Items.deed transfer")
    GET_UTILITIES = DataReader.get_data("Navigation Items.get utilities")
    GET_INSURANCE = DataReader.get_data("Navigation Items.get insurance")
    GET_MOVERS = DataReader.get_data("Navigation Items.get movers")
