import time

import allure
from hamcrest import assert_that

from buy_a_home.pages.select_home.BuildingDetailsPage import BuildingDetailsPage
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from framework.browser.Browser import Browser
from framework.utils.StringUtil import StringUtil
from framework.utils.WaiterUtil import WaiterUtil


class WorkWithPropertySteps:
    """Common actions with property"""

    @staticmethod
    def set_actions_on_property_or_building_page(unit_actions, property_actions):
        """
        Check that property details page was opened or building details page was opened
        :return: list: list of data about called function
        """
        global value, price_of_home
        data_list = []
        building_details_page = BuildingDetailsPage()
        property_details = PropertyDetailsPage()
        start_time = time.time()
        while WaiterUtil.wait_for_time(
                    start_time, "After the expected time Building Details page is displayed ") \
                and not building_details_page.page_element.try_wait_for_absent():
            price_of_home = building_details_page.get_random_property_details_of_price()
            building_details_page.click_property_detail(StringUtil.get_text_without_letters(price_of_home[0]))
            for function_and_args in unit_actions:
                value = function_and_args[0](*function_and_args[1])
        if property_details.is_property_page_opened():
            price_of_home = property_details.get_price_property()
            for function_and_args in property_actions:
                value = function_and_args[0](*function_and_args[1])
            data_list.append(value)
            data_list.append(price_of_home)
        return data_list

    @staticmethod
    def refresh_page_if_search_result_is_empty():
        """
        Method connected with refreshing page while search result is empty
        :return: list: list of data from function
        """
        search_results_page = SearchResultsPage()
        search_results_page.wait_page_to_load()
        start_time = time.time()
        while WaiterUtil.wait_for_time(
                    start_time, "After the expected time the empty result is present") \
                and not search_results_page.lbl_absent_property_details.try_wait_for_absent():
            Browser.refresh_page()

    @staticmethod
    def check_selected_property_in_chosen_home(page_locator, price):
        with allure.step("Check that selected property displays in Chosen home"):
            page_locator.click_property_details_lnk(page_locator.lnk_chosen_home)
            property_details_price = page_locator.get_property_details_price(page_locator.lbl_chosen_home_price)
            assert_that(price == property_details_price, "Price for selected home and price from property "
                                                         "details aren't equaled")
