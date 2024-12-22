from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ConfirmedForm(BasePage):
    page_name = "Confirmed Form"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_confirmed_form")

    lnk_bank_loan = Link(locator_reader, "lnk_bank_loan")
    lnk_self_finance = Link(locator_reader, "lnk_self_finance")

    def __init__(self):
        super(ConfirmedForm, self).__init__(self.page_element)

    def click_bank_loan_lnk(self):
        self.lnk_bank_loan.click()

    def click_self_finance_lnk(self):
        self.lnk_self_finance.click()
