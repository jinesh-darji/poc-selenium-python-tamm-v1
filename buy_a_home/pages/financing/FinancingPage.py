from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageHomeFromList import BasePageHomeFromList
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class FinancingPage(BasePageJourney, BasePageHeader, BasePageHomeFromList):
    page_name = "Financing Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_financing_page")

    btn_start = Button(locator_reader, "btn_start")

    def __init__(self):
        super(FinancingPage, self).__init__(self.page_element)

    def is_start_button_present(self):
        return self.btn_start.is_displayed()

    def click_start_btn(self):
        self.wait_page_to_load()
        self.scroll_to_element(self.btn_start)
        self.btn_start.click()
