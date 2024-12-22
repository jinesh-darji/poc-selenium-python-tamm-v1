from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from framework.elements.Label import Label
from framework.elements.List import List
from framework.utils.LocatorReader import LocatorReader


class SearchForOfferPage(BasePageJourney):
    page_name = "Search For Offer Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_search_for_offer")

    lst_Insurance = List(locator_reader, "list_insurance")

    lbl_your_insurance_item = Label(locator_reader, "lbl_your_insurance_item")
    lbl_your_insurance_opened = Label(locator_reader, "lbl_your_insurance_opened")

    def __init__(self):
        super(SearchForOfferPage, self).__init__(self.page_element)

    def is_your_insurance_opened(self, your_insurance):
        self.lbl_your_insurance_opened.format(your_insurance).wait_until_location_stable()
        return self.lbl_your_insurance_opened.is_present()

    def click_your_insurance_item(self, your_insurance):
        self.lbl_your_insurance_item.format(your_insurance).wait_until_location_stable()
        self.lbl_your_insurance_item.format(your_insurance).click()
