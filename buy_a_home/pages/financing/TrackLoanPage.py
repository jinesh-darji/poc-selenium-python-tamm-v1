from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TrackLoanPage(BasePage):
    page_name = "Track Loan Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_track_loan_page")

    def __init__(self):
        super(TrackLoanPage, self).__init__(self.page_element)
