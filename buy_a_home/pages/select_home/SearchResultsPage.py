from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageHomeFromList import BasePageHomeFromList
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from buy_a_home.pages.base_page_journey_methods.BasePageSearchAndFilter import BasePageSearchAndFilter
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader


class SearchResultsPage(BasePageJourney, BasePageSearchAndFilter, BasePageHomeFromList, BasePageHeader):
    page_name = "Search Results Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_search_results_page")

    lbl_star_results = Label(locator_reader, 'lbl_star_results')

    def __init__(self):
        super(SearchResultsPage, self).__init__(self.page_element)
