from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class GetUtilitiesPage(BasePageJourney, BasePageHeader):
    page_name = "Get Utilities Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_get_utilities_page")

    btn_view_water = Button(locator_reader, "btn_view_water")
    btn_apply_etisalat = Button(locator_reader, "btn_apply_etisalat")

    def __init__(self):
        super(GetUtilitiesPage, self).__init__(self.page_element)

    def is_apply_btn_present(self):
        self.btn_apply_etisalat.wait_until_location_stable()
        return self.btn_apply_etisalat.is_present()

    def click_view_btn_water_and_electricity(self):
        self.btn_view_water.wait_until_location_stable()
        self.btn_view_water.click()
