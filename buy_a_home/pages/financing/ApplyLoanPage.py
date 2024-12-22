from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ApplyLoanPage(BasePage):
    page_name = "Apply Loan Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_apply_loan")

    btn_submit = Button(locator_reader, "btn_submit")

    def __init__(self):
        super(ApplyLoanPage, self).__init__(self.page_element)

    def click_submit_btn(self):
        self.btn_submit.click()
