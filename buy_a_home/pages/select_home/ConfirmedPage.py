from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ConfirmedPage(BasePage):
    page_name = "Confirmed Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_confirmed_page")

    def __init__(self):
        super(ConfirmedPage, self).__init__(self.page_element)
