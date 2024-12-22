from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageHomeFromList import BasePageHomeFromList
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class BuildingDetailsPage(BasePageJourney, BasePageHomeFromList, BasePageHeader):
    page_name = "Building Details Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_building_details")

    def __init__(self):
        super(BuildingDetailsPage, self).__init__(self.page_element)
