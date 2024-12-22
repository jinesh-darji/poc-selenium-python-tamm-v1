from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class MyAppointmentsPage(BasePage):
    page_name = "My Appointments Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_my_appointments")

    def __init__(self):
        super(MyAppointmentsPage, self).__init__(self.page_element)

