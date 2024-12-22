from buy_a_home.pages.base_page_journey_methods.BasePageFinancingDetails import BasePageFinancingDetails
from buy_a_home.pages.base_page_journey_methods.BasePageHomeFromList import BasePageHomeFromList
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader
from framework.utils.StringUtil import StringUtil


class SavedPropertiesPage(BasePageJourney, BasePageFinancingDetails, BasePageHomeFromList):
    page_name = "Saved Properties Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_saved_properties")

    lbl_heart_saved = Label(locator_reader, "lbl_heart_saved")
    lbl_count_props = Label(locator_reader, "lbl_count_props")

    btn_search_a_home = Button(locator_reader, "btn_search_a_home")

    def __init__(self):
        super(SavedPropertiesPage, self).__init__(self.page_element)

    def get_count_of_props(self):
        count_test = self.lbl_count_props.get_text()
        return StringUtil.get_text_without_letters(count_test)

    def click_search_home_btn(self):
        self.btn_search_a_home.wait_for_is_displayed()
        self.btn_search_a_home.click()

    def click_heart_icon_saved_property(self, price):
        self.lbl_heart_saved.format(price).wait_until_location_stable()
        self.lbl_heart_saved.format(price).click()

    def click_random_property_with_selected_heart(self):
        self.lst_properties_with_selected_heart.wait_until_location_stable()
        price = self.lst_properties_with_selected_heart.get_random_items_from_list(1)
        self.click_heart_icon_saved_property(price)

    def click_random_property_with_selected_heart_without_specific_price(self, old_price):
        """
        Click to property with selected heart without specific price from list
        :type old_price: str: price for earlier selected home
        """
        self.list_of_results_price_with_filled_stars_without_specific_price.format(
            old_price).wait_until_location_stable()
        price = self.list_of_results_price_with_filled_stars_without_specific_price.format(old_price). \
            get_random_items_from_list(1)
        self.click_property_detail(price)
