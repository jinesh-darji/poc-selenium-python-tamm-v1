from framework.elements.Link import Link
from framework.utils.LocatorReader import LocatorReader
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.elements.Label import Label


class HomeGrantPage(BasePage):
    page_name = "Home Grant Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_home_grant_page")

    lbl_general_info_pop_up = Label(locator_reader, "lbl_general_info_pop_up")

    btn_apply_via_adha = Button(locator_reader, "btn_apply_via_adha")
    btn_close_general_info = Button(locator_reader, "btn_close_general_info")

    lnk_general_info = Link(locator_reader, "lnk_general_info")

    def __init__(self):
        super(HomeGrantPage, self).__init__(self.page_element)

    def is_apply_via_adha_button_present(self):
        return self.btn_apply_via_adha.is_present()

    def is_general_info_pop_up_present(self):
        self.lbl_general_info_pop_up.wait_until_location_stable()
        return self.lbl_general_info_pop_up.is_present()

    def click_apply_via_adha_btn(self):
        self.btn_apply_via_adha.click()

    def click_general_info_lnk(self):
        self.lnk_general_info.click()

    def click_close_general_info_btn(self):
        self.btn_close_general_info.click()
