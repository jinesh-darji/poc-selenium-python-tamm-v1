from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageHomeFromList import BasePageHomeFromList
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from buy_a_home.pages.base_page_journey_methods.BasePagePropertyDetails import BasePagePropertyDetails
from buy_a_home.pages.base_page_journey_methods.BasePageSearchAndFilter import BasePageSearchAndFilter
from framework.elements.Button import Button
from framework.elements.Checkbox import Checkbox
from framework.elements.Dropdown import Dropdown
from framework.elements.InputDropdown import InputDropdown
from framework.elements.Label import Label
from framework.elements.List import List
from framework.utils.LocatorReader import LocatorReader


class SearchHomePage(BasePageJourney, BasePageSearchAndFilter, BasePageHomeFromList, BasePageHeader,
                     BasePagePropertyDetails):
    page_name = "Search Home Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_search_home_page")

    lst_minBedrooms_list_dropdown = List(locator_reader, "minBedrooms_list_dropdown")
    lst_maxBedrooms_list_dropdown = List(locator_reader, "maxBedrooms_list_dropdown")

    lbl_minBedrooms_item_dropdown = Label(locator_reader, "minBedrooms_item_dropdown")
    lbl_maxBedrooms_item_dropdown = Label(locator_reader, "maxBedrooms_item_dropdown")
    lbl_minBedrooms_item = Label(locator_reader, "minBedrooms_dropdown")
    lbl_maxBedrooms_item = Label(locator_reader, "maxBedrooms_dropdown")
    lbl_saved_properties = Label(locator_reader, "lbl_saved_properties")

    btn_apply = Button(locator_reader, "btn_apply")
    btn_apply_not_available = Button(locator_reader, "btn_apply_not_available")

    chbx_apartment_quick_search = Checkbox(locator_reader, "chbx_apartment_quick_search")
    chbx_villa_quick_search = Checkbox(locator_reader, "chbx_villa_quick_search")
    chbx_apartment_quick_search_disable = Checkbox(locator_reader, "chbx_apartment_quick_search_disable")
    chbx_villa_quick_search_disable = Checkbox(locator_reader, "chbx_villa_quick_search_disable")

    drpdwn_area_quick_search = InputDropdown(locator_reader, "area_dropdown_quick_search",
                                             "area_arrow_dropdown_quick_search", "area_input_dropdown_quick_search")
    drd_min_bedrooms_result_page = Dropdown(locator_reader, "minBedrooms_dropdown", "minBedrooms_arrow_dropdown")
    drd_max_bedrooms_result_page = Dropdown(locator_reader, "maxBedrooms_dropdown", "maxBedrooms_arrow_dropdown")

    def __init__(self):
        super(SearchHomePage, self).__init__(self.page_element)

    def is_saved_properties_lbl_present(self):
        return self.lbl_saved_properties.is_present()

    def is_apply_button_present(self):
        return self.btn_apply.is_present()

    def click_apply_btn(self):
        self.btn_apply.scroll_by_script()
        self.btn_apply.wait_until_location_stable()
        self.btn_apply.click()

    def click_apartment_and_villa_chbxes(self):
        self.chbx_apartment_quick_search.wait_until_location_stable()
        self.chbx_apartment_quick_search.click()
        self.chbx_villa_quick_search.scroll_by_script()
        self.chbx_villa_quick_search.click()

    def click_area_drpdwn(self):
        self.drpdwn_area_quick_search.wait_until_location_stable()
        self.drpdwn_area_quick_search.click()

    def click_saved_properties(self):
        self.lbl_saved_properties.wait_until_location_stable()
        self.lbl_saved_properties.click()
