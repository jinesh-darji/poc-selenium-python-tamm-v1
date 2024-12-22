import pytest
import allure
from hamcrest import assert_that

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from framework.browser.Browser import Browser
from framework.elements.Dropdown import Dropdown


class TestSaveConditionsRoomsDropDown:
    """Search home page: Rooms drop downs save their conditions after going to this page from search results page:
    BUAH-1388"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_bedrooms_drop_downs_save_their_conditions(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Select min and max bedrooms dropdowns"):
            search_home_page = SearchHomePage()
            bedrooms_list = \
                [Dropdown.get_and_click_upper_case_item(search_home_page.drd_min_bedrooms_result_page,
                                                        search_home_page.lbl_minBedrooms_item_dropdown,
                                                        search_home_page.lst_minBedrooms_list_dropdown),
                 Dropdown.get_and_click_upper_case_item
                 (search_home_page.drd_max_bedrooms_result_page,
                  search_home_page.lbl_maxBedrooms_item_dropdown,
                  search_home_page.lst_maxBedrooms_list_dropdown)]

        NavigateSteps.go_to_search_results_page()

        with allure.step("Check that data in drop-down for bedrooms have the same data"):
            search_home_page.click_filter_icon()
            filter_form = FilterForm()
            bedrooms_list_filter = \
                [filter_form.get_value_from_drop_down_filter(
                    filter_form.lst_minBedrooms_qty_form),
                    filter_form.get_value_from_drop_down_filter(
                        filter_form.lst_maxBedrooms_qty_form)]
            assert_that(bedrooms_list == bedrooms_list_filter, "Lists of bedrooms aren't equal")

        with allure.step("Close filter form"):
            filter_form.click_close_filter_pop_up_btn()

        with allure.step("Go to previous page"):
            Browser.back_page()

        with allure.step("Check that data in drop-down on Search page = data from filter form"):
            bedrooms_list_search = \
                [search_home_page.get_value_from_drop_down_filter(
                    search_home_page.lbl_minBedrooms_item),
                    search_home_page.get_value_from_drop_down_filter(
                        search_home_page.lbl_maxBedrooms_item)]
            assert_that(bedrooms_list_search == bedrooms_list_filter, "Lists of bedrooms aren't equal")
