import time

import allure
import pytest
from hamcrest import assert_that

from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.steps.WorkOnFilterFormSteps import WorkOnFilterFormSteps
from framework.browser.Browser import Browser
from framework.utils.Comparer import Comparer
from framework.utils.DataReader import DataReader
from framework.utils.WaiterUtil import WaiterUtil


class TestExistDataPropertyDetailsPage:
    """Test that User is able to apply only apartment checkbox and amenity in search page and see data in property
    detail page: BUAH-1369"""

    @pytest.mark.smoke
    @pytest.mark.guest_user
    def test_results_after_selecting_apartment_chbx_and_amenity_on_property_page(self):

        global list_of_amenities_final

        NavigateSteps.go_to_search_page()

        with allure.step("Select Villa checkbox checkbox and check that data from quick search are displayed on "
                         "filter form"):
            search_home_page = SearchHomePage()
            search_home_page.click_villa_chbx(search_home_page.chbx_villa_quick_search)
            search_home_page.click_apply_btn()
            search_home_page.click_filter_icon()
            filter_form = FilterForm()
            assert_that(filter_form.chbx_apartment_filter_enable.is_present(),
                        "Checkbox Apartment is deselected" and filter_form.chbx_villa_filter_disable.is_present(),
                        "Checkbox Villa is selected")
            filter_form.click_show_amenities_lnk()

        with allure.step("Get 2 random Amenities"):
            list_of_amenities = filter_form.get_amenities(DataReader.get_data("Qty of items.qty of amenities"))

        with allure.step("Select 2 random Amenities and apply filter"):
            filter_form.click_random_checkboxes(filter_form.chbx_of_amenity, list_of_amenities)
            filter_form.click_apply_btn_filter()

        with allure.step("Select new amenities if 0 property details was found and select Apply button"):
            search_results_page = SearchResultsPage()
            start_time = time.time()
            while WaiterUtil.wait_for_time(
                    start_time, "After the expected time the empty result is present") \
                    and not search_results_page.lbl_0_property_details.try_wait_for_absent():
                Browser.scroll_to_top()
                filter_form = FilterForm()
                list_of_amenities_new = WorkOnFilterFormSteps.get_new_list_of_data_on_filter_form(
                    [filter_form.click_and_get_new_random_amenities, [list_of_amenities,
                                                                      DataReader.get_data(
                                                                          "Qty of items.qty of amenities")]])
                WorkOnFilterFormSteps.actions_if_filter_form_opened([filter_form.click_to_amenitie,
                                                                [list_of_amenities_new]])
                if list_of_amenities_new is not None:
                    list_of_amenities = list_of_amenities_new

        with allure.step("Selection random home according search result"):
            search_results_page = SearchResultsPage()
            search_results_page.click_random_result_of_search()

        with allure.step("Check that property details page was opened or building details page was opened"):
            property_details_page = PropertyDetailsPage()
            data_list = WorkWithPropertySteps.set_actions_on_property_or_building_page([[property_details_page.
                                                                                  get_amenities_list_property_details,
                                                                                    []]],
                                                                                  [[property_details_page.
                                                                                  get_amenities_list_property_details,
                                                                                    []]])
            assert_that(Comparer.check_include_1_list_to_second(list_of_amenities, data_list[0]), "Amenities from one "
                                                                                                  "list aren't existed "
                                                                                                  "in second list")
