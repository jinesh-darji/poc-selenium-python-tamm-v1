import pytest
import allure
from hamcrest import assert_that

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from framework.elements.Dropdown import Dropdown


class TestRoomsDropDownSaveConditions:
    """Test that User is able to select rooms data from drop-downs and their conditions will save after going to
    previous page"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_test_drop_downs_save_their_conditions_after_going_from_previous_page(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Select min and max bedrooms drop-downs"):
            search_home_page = SearchHomePage()

            bedrooms_list = \
                [Dropdown.get_and_click_upper_case_item(search_home_page.drd_min_bedrooms_result_page,
                                                        search_home_page.lbl_minBedrooms_item_dropdown,
                                                        search_home_page.lst_minBedrooms_list_dropdown),

                 Dropdown.get_and_click_upper_case_item(search_home_page.drd_max_bedrooms_result_page,
                                                        search_home_page.lbl_maxBedrooms_item_dropdown,
                                                        search_home_page.lst_maxBedrooms_list_dropdown)]

        NavigateSteps.go_to_search_results_page()

        with allure.step("Select filter icon"):
            search_results_page = SearchResultsPage()
            search_results_page.click_filter_icon_search_results()

        with allure.step("Check that data from drop-downs for rooms = data from previous step"):
            filter_form = FilterForm()
            assert_that(bedrooms_list == Dropdown.get_list_of_visible_drpdwn_values(
                filter_form.get_value_from_drop_down_filter(filter_form.lst_minBedrooms_qty_form),
                filter_form.get_value_from_drop_down_filter(filter_form.lst_maxBedrooms_qty_form)),
                        "Qty of rooms from Filter form isn't equal qty from Search page")
