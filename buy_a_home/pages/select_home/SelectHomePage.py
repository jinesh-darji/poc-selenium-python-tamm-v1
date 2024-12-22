from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class SelectHomePage(BasePageJourney, BasePageHeader):
    page_name = "Select Home Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_select_home_page")

    btn_search_home = Button(locator_reader, 'btn_search_home')
    btn_saved_properties = Button(locator_reader, 'btn_saved_properties')
    btn_apply_grant = Button(locator_reader, "btn_apply_grant")

    lbl_home_grant = Label(locator_reader, "lbl_home_grant")

    def __init__(self):
        super(SelectHomePage, self).__init__(self.page_element)

    def is_ready_home_grant(self):
        return self.lbl_home_grant.is_present()

    def is_saved_properties_btn_present(self):
        return self.btn_saved_properties.is_present()

    def click_search_btn(self):
        self.btn_search_home.wait_until_location_stable()
        self.btn_search_home.click()

    def click_saved_properties_btn(self):
        self.btn_saved_properties.wait_until_location_stable()
        self.btn_saved_properties.click()

    def click_apply_btn(self):
        self.btn_apply_grant.wait_until_location_stable()
        self.btn_apply_grant.click()
