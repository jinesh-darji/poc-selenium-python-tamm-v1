from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class MoveNewHomePage(BasePageJourney, BasePageHeader):
    page_name = "Move New Home Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_move_new_home")

    btn_finish_journey = Button(locator_reader, "btn_finish_journey")

    def __init__(self):
        super(MoveNewHomePage, self).__init__(self.page_element)

    def is_finish_journey_btn_present(self):
        self.btn_finish_journey.wait_until_location_stable()
        return self.btn_finish_journey.is_present()

    def click_to_finish_journey_btn(self):
        self.btn_finish_journey.wait_until_location_stable()
        self.btn_finish_journey.click()
