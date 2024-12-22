import time

from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from framework.utils.WaiterUtil import WaiterUtil


class WorkOnFilterFormSteps:
    """Work With Filter form"""

    @staticmethod
    def get_search_criteria_if_result_is_empty(*actions):
        """
        Method connected with doing function while search result is empty
        :return: list: list of data from function
        """
        value_data = None
        search_results_page = SearchResultsPage()
        search_results_page.wait_page_to_load()
        start_time = time.time()
        while WaiterUtil.wait_for_time(
                start_time, "After the expected time the empty result is present") \
                and not search_results_page.lbl_0_property_details.try_wait_for_absent():
            search_results_page.wait_page_to_load()  # Need for stabilization of tests
            search_results_page.click_filter_icon_search_results()
            for function_and_args in actions:
                value_data = function_and_args[0](*function_and_args[1])
                filter_form = FilterForm()
                filter_form.click_apply_btn_filter()
        return value_data

    @staticmethod
    def get_new_list_of_data_on_filter_form(*actions):
        """
        Method connected with selection new random amenities if result of search gave 0 property details on Filter Form
        :return: list: 2 items of amenities
        """
        value_data = None
        search_results_page = SearchResultsPage()
        search_results_page.wait_page_to_load()
        search_results_page.click_filter_icon_search_results()
        for function_and_args in actions:
            value_data = function_and_args[0](*function_and_args[1])
        return value_data

    @staticmethod
    def actions_if_filter_form_opened(*actions):
        """
        Method connected with checking doing function while search result is empty
        """
        filter_form = FilterForm()
        filter_form.wait_page_to_load()
        for function_and_args in actions:
            function_and_args[0](*function_and_args[1])
            filter_form.click_apply_btn_filter()
