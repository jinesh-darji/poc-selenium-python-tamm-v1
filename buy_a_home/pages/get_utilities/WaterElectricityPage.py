from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class WaterElectricityPage(BasePageJourney, BasePageHeader):
    page_name = "Water Electricity Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_water_electricity")

    btn_continue = Button(locator_reader, "btn_continue")

    def __init__(self):
        super(WaterElectricityPage, self).__init__(self.page_element)

    def click_continue_btn_water_and_electricity(self):
        self.btn_continue.wait_until_location_stable()
        self.btn_continue.scroll_by_script()
        self.btn_continue.click()
