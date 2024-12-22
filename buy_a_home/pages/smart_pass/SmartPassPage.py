from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.utils.LocatorReader import LocatorReader


class SmartPassPage(BasePageJourney):
    page_name = "Smart Pass Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_smart_pass_page")

    tbx_user_name_field = TextBox(locator_reader, "txb_user_name")
    tbx_user_password_field = TextBox(locator_reader, "txb_user_password")

    btn_login = Button(locator_reader, "btn_login")

    def __init__(self):
        super(SmartPassPage, self).__init__(self.page_element)

    def send_username(self, data):
        self.tbx_user_name_field.wait_until_location_stable()
        self.tbx_user_name_field.send_keys(data)

    def send_password(self, data):
        self.tbx_user_password_field.wait_until_location_stable()
        self.tbx_user_password_field.send_keys(data)

    def click_login(self):
        self.btn_login.wait_until_location_stable()
        self.btn_login.click()
