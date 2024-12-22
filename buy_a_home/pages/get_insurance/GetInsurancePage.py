from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class GetInsurancePage(BasePageJourney, BasePageHeader):
    page_name = "Get Insurance Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_get_insurance")

    btn_find_movers = Button(locator_reader, "btn_find_movers")
    btn_back_to_home = Button(locator_reader, "btn_back_to_home")

    def __init__(self):
        super(GetInsurancePage, self).__init__(self.page_element)

    def click_find_movers_btn(self):
        self.btn_find_movers.wait_until_location_stable()
        self.btn_find_movers.scroll_by_script()
        self.btn_find_movers.click()

    def click_back_to_home_btn(self):
        self.btn_back_to_home.wait_until_location_stable()
        self.btn_back_to_home.click()
