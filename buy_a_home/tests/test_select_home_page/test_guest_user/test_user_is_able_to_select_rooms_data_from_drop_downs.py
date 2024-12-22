import pytest
import allure
from hamcrest import assert_that

from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.steps.WorkOnFilterFormSteps import WorkOnFilterFormSteps
from framework.elements.Dropdown import Dropdown
from framework.utils.EnvReader import EnvReader


class TestRoomsDropDown:
    """Test that User is able to select rooms data from drop-downs"""

    @pytest.mark.smoke
    @pytest.mark.guest_user
    def test_user_is_able_to_select_rooms_data_from_drop_downs(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Select min and max bedrooms dropdowns"):
            search_home_page = SearchHomePage()
            bedrooms_list = \
                [Dropdown.get_and_click_upper_case_item(search_home_page.drd_min_bedrooms_result_page,
                                                        search_home_page.lbl_minBedrooms_item_dropdown,
                                                        search_home_page.lst_minBedrooms_list_dropdown),
                 Dropdown.get_and_click_upper_case_item
                 (search_home_page.drd_max_bedrooms_result_page, search_home_page.lbl_maxBedrooms_item_dropdown,
                  search_home_page.lst_maxBedrooms_list_dropdown)]

        NavigateSteps.go_to_search_results_page()

        with allure.step("Select random home in Search results page"):
            bedrooms_list_2 = WorkOnFilterFormSteps.get_search_criteria_if_result_is_empty([self.get_items_dropdown,
                                                                                            []])
            if bedrooms_list_2 is not None:
                bedrooms_list = bedrooms_list_2
            search_results_page = SearchResultsPage()
            search_results_page.click_random_result_of_search()

        with allure.step("Check that qty of bedrooms is exist in range between min and max for selected data in "
                         "drop-downs"):
            WorkWithPropertySteps.set_actions_on_property_or_building_page(
                [[self.is_correct_qty_bedrooms, [bedrooms_list]]],
                [[self.is_correct_qty_bedrooms, [bedrooms_list]]])

    def get_items_dropdown(self):
        """
        Method connected with getting min and max value from drop-down
        :return:
        """
        filter_form = FilterForm()
        filter_form.click_show_amenities_lnk()
        bedrooms_list = \
            [Dropdown.get_and_click_upper_case_item(filter_form.drpdwn_min_bedrooms_filter_form,
                                                    filter_form.lbl_minBedrooms_item_dropdown_filter,
                                                    filter_form.lst_minBedrooms_dropdown_form),
             Dropdown.get_and_click_upper_case_item
             (filter_form.drpdwn_max_bedrooms_filter_form,
              filter_form.lbl_maxBedrooms_item_dropdown_filter,
              filter_form.lst_maxBedrooms_dropdown_form)]

        return bedrooms_list

    def is_correct_qty_bedrooms(self, bedrooms_list):
        property_detail_page = PropertyDetailsPage()
        property_detail_page.wait_page_to_load()
        for i in range(0, len(bedrooms_list)):
            bedrooms_list[i] = 0 if bedrooms_list[i] == EnvReader().get_from_locale("Property Details Page.studio") \
                else bedrooms_list[i]
            bedrooms_list[i] = 0 if bedrooms_list[i] == EnvReader().get_from_locale("Base Page Journey.min") \
                else bedrooms_list[i]
            bedrooms_list[i] = 10 if bedrooms_list[i] == EnvReader().get_from_locale("Base Page Journey.max") \
                else bedrooms_list[i]

        assert_that(property_detail_page.get_qty_bedrooms() in range(int(bedrooms_list[0]), int(bedrooms_list[1]) + 1),
                    "Qty of bedrooms isn't exist in range between min and max for selected data in drop-downs")
