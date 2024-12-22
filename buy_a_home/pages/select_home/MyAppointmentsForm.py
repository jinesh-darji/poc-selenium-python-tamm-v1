from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class MyAppointmentsForm(BasePage):
    page_name = "My Appointments Form"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_my_appointments_form")

    btn_yes = Button(locator_reader, "btn_yes")
    btn_no = Button(locator_reader, "btn_no")
    btn_confirm_home_selection_and_continue_to_purchase = Button(locator_reader,
                                                                 "btn_confirm_home_selection_and_continue_to_purchase")
    btn_yes_search_for_another_home = Button(locator_reader, "btn_yes_search_for_another_home")
    btn_reschedule_appointment = Button(locator_reader, "btn_reschedule_appointment")
    btn_no_search_for_another_home = Button(locator_reader, "btn_no_search_for_another_home")
    btn_confirm_home_and_continue_to_purchase = Button(locator_reader, "btn_confirm_home_and_continue_to_purchase")

    def __init__(self):
        super(MyAppointmentsForm, self).__init__(self.page_element)

    def click_yes_btn(self):
        self.btn_yes.click()

    def click_no_btn(self):
        self.btn_no.click()

    def click_confirm_home_selection_and_continue_to_purchase_btn(self):
        self.btn_confirm_home_selection_and_continue_to_purchase.click()

    def click_yes_search_for_another_home_btn(self):
        self.btn_yes_search_for_another_home.click()

    def click_reschedule_appointment_btn(self):
        self.btn_reschedule_appointment.click()

    def click_no_search_for_another_home_btn(self):
        self.btn_no_search_for_another_home.click()

    def click_confirm_home_and_continue_to_purchase_btn(self):
        self.btn_confirm_home_and_continue_to_purchase.click()
