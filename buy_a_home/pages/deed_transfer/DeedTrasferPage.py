from buy_a_home.pages.base_page_journey_methods.BasePageHomeFromList import BasePageHomeFromList
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class DeedTransferPage(BasePageJourney, BasePageHomeFromList):
    page_name = "Deed Transfer Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_deed_transfer")

    btn_view = Button(locator_reader, "btn_view")

    def __init__(self):
        super(DeedTransferPage, self).__init__(self.page_element)

    def is_view_button_present(self):
        return self.btn_view.is_displayed()

    def click_view_btn(self):
        self.btn_view.click()
