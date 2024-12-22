from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.List import List
from framework.utils.LocatorReader import LocatorReader


class EtisalatPage(BasePageJourney, BasePageHeader):
    page_name = "Etisalat Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_etisalat_page")

    lbl_error_message_about_package = Label(locator_reader, "lbl_error_message_about_package")
    lbl_package_details = Label(locator_reader, "lbl_package_details")

    lst_view_details = List(locator_reader, "lst_view_details")
    lst_request_btn = List(locator_reader, "lst_request_btn")
    lst_packages_details = List(locator_reader, "lst_packages_details")

    btn_request_pop_up = Button(locator_reader, "btn_request_pop_up")
    btn_close_view_details = Button(locator_reader, "btn_close_view_details")
    btn_cancel_view_details = Button(locator_reader, "btn_cancel_view_details")
    btn_ok_error_message = Button(locator_reader, "btn_ok_error_message")
    btn_close_error_message_package = Button(locator_reader, "btn_close_error_message_package")
    btn_load_more = Button(locator_reader, "btn_load_more")
    btn_submit = Button(locator_reader, "btn_submit")
    btn_ok_etisalat_confirmation = Button(locator_reader, "btn_ok_etisalat_confirmation")

    def __init__(self):
        super(EtisalatPage, self).__init__(self.page_element)

    def is_error_message_packages_present(self):
        return self.lbl_error_message_about_package.is_present()

    def is_package_details_pop_up_present(self):
        return self.lbl_package_details.is_present()

    def get_count_of_packages(self):
        self.lst_packages_details.wait_until_location_stable()
        return self.lst_packages_details.get_elements_count()

    def click_to_1st_view_details_button(self):
        self.lst_view_details.wait_for_is_present()
        self.lst_view_details.scroll_by_script()
        self.lst_view_details.get_elements()[0].click()

    def click_to_request_button_pop_up(self):
        self.btn_request_pop_up.wait_until_location_stable()
        self.btn_request_pop_up.click()

    def click_to_1st_request_button(self):
        self.lst_request_btn.try_wait_for_absent()
        self.lst_request_btn.wait_for_is_present()
        self.lst_request_btn.scroll_by_script()
        self.lst_request_btn.get_elements()[0].click()

    def click_to_close_details_pop_up(self):
        self.btn_close_view_details.wait_until_location_stable()
        self.btn_close_view_details.click()

    def click_to_cancel_details_pop_up(self):
        self.btn_cancel_view_details.wait_until_location_stable()
        self.btn_cancel_view_details.click()

    def click_to_ok_btn_in_error_pop_up(self):
        self.btn_ok_error_message.wait_until_location_stable()
        self.btn_ok_error_message.click()

    def click_to_close_btn_in_error_pop_up_package(self):
        self.btn_close_error_message_package.wait_until_location_stable()
        self.btn_close_error_message_package.click()

    def click_load_more_btn(self):
        self.lst_view_details.wait_for_is_present()
        self.lst_view_details.scroll_by_script()
        self.btn_load_more.click()

    def click_submit_btn(self):
        self.btn_submit.wait_for_is_present()
        self.btn_submit.scroll_by_script()
        self.btn_submit.click()

    def click_ok_btn(self):
        self.btn_ok_etisalat_confirmation.wait_for_is_present()
        self.btn_ok_etisalat_confirmation.scroll_by_script()
        self.btn_ok_etisalat_confirmation.click()
