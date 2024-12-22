from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from buy_a_home.pages.base_page_journey_methods.BasePagePropertyDetails import BasePagePropertyDetails
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader
from framework.utils.StringUtil import StringUtil


class DeedTransferPropertyRegistrationPage(BasePageJourney, BasePagePropertyDetails, BasePageHeader):
    page_name = "Deed Transfer Property Registration Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_deed_transfer_property_registration")

    lbl_registration_pop_up = Label(locator_reader, "lbl_registration_pop_up")
    lbl_success_modal_pop_up = Label(locator_reader, "lbl_success_modal_pop_up")
    lbl_in_progress_message = Label(locator_reader, "lbl_in_progress_message")
    lbl_fee_payment = Label(locator_reader, "lbl_fee_payment")
    lbl_fee_payment_steps = Label(locator_reader, "lbl_fee_payment_steps")

    btn_continue_step = Button(locator_reader, "btn_continue_step")
    btn_close_adm_registration = Button(locator_reader, "btn_close_adm_registration")
    btn_no_adm_registration = Button(locator_reader, "btn_no_adm_registration")
    btn_yes_adm_registration = Button(locator_reader, "btn_yes_adm_registration")
    btn_ok_success_pop_up = Button(locator_reader, "btn_ok_success_pop_up")

    def __init__(self):
        super(DeedTransferPropertyRegistrationPage, self).__init__(self.page_element)

    def is_fee_payment_present(self):
        return self.lbl_fee_payment.is_present()

    def is_in_progress_message_present(self):
        return self.lbl_in_progress_message.is_present()

    def is_registration_pop_up_present(self):
        return self.lbl_registration_pop_up.is_present()

    def is_success_pop_up_present(self):
        return self.lbl_success_modal_pop_up.is_present()

    def get_fee_payment(self):
        if self.is_fee_payment_present():
            self.lbl_fee_payment_steps.get_elements()[1].click()
        return StringUtil.get_text_only_digits(self.lbl_fee_payment.get_text())

    def click_continue_btn(self):
        self.btn_continue_step.wait_until_location_stable()
        self.btn_continue_step.click()

    def click_close_registration_pop_up_btn(self):
        self.btn_close_adm_registration.wait_until_location_stable()
        self.btn_close_adm_registration.click()

    def click_no_registration_pop_up_btn(self):
        self.btn_no_adm_registration.wait_until_location_stable()
        self.btn_no_adm_registration.click()

    def click_yes_registration_pop_up_btn(self):
        self.btn_yes_adm_registration.wait_until_location_stable()
        self.btn_yes_adm_registration.click()

    def click_ok_btn_on_success_pop_up(self):
        self.btn_ok_success_pop_up.wait_until_location_stable()
        self.btn_ok_success_pop_up.click()
