from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class BasePageHeader(BasePage):
    page_name = "Base Page Header"
    locator_reader = LocatorReader(page_name)

    lbl_letters = Label(locator_reader, "lbl_letters")
    lbl_arabic = Label(locator_reader, "lbl_arabic")
    lbl_tamm_icon = Label(locator_reader, 'lbl_tamm_icon')

    btn_smart_pass = Button(locator_reader, "btn_smart_pass")
    btn_left_panel = Button(locator_reader, "btn_left_panel")
    btn_logout = Button(locator_reader, "btn_logout")

    def is_smart_pass_btn_presnet(self):
        return self.btn_smart_pass.is_present()

    def click_left_panel(self):
        self.btn_left_panel.wait_until_location_stable()
        self.btn_left_panel.click()

    def click_smart_pass(self):
        self.btn_smart_pass.wait_until_location_stable()
        self.btn_smart_pass.click()

    def click_logout(self):
        self.btn_logout.wait_until_location_stable()
        self.btn_logout.click()

    def click_tamm_icon(self):
        self.lbl_tamm_icon.scroll_by_script()
        self.lbl_tamm_icon.wait_until_location_stable()
        self.lbl_tamm_icon.click()

    def click_switch_language(self):
        self.lbl_arabic.wait_until_location_stable()
        self.lbl_arabic.click()
