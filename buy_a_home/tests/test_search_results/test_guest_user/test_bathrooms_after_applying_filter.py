import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.steps.WorkOnFilterFormSteps import WorkOnFilterFormSteps
from framework.elements.Dropdown import Dropdown
from framework.utils.EnvReader import EnvReader


class TestDropDownsBathrooms:
    """Test that drop down data apply correctly for bathrooms: BUAH-2454"""

    @pytest.mark.skip(reason="bathrooms are hidden now")
    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_bathrooms_after_applying_filter(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Select Villa on quick search"):
            search_home_page = SearchHomePage()
            search_home_page.click_villa_chbx(search_home_page.chbx_villa_quick_search)

        with allure.step("Click Apply button"):
            search_home_page.click_apply_btn()

        with allure.step("Click Filter icon"):
            search_results_page = SearchResultsPage()
            search_results_page.click_filter_icon_search_results()

        with allure.step("Select min and max for bathrooms"):
            filter_form = FilterForm()
            bathrooms_list = self.get_items_dropdown()

        with allure.step("Click apply button"):
            filter_form.click_apply_btn_filter()

        with allure.step("Select random home in Search results page"):
            bathrooms_list_2 = WorkOnFilterFormSteps.get_search_criteria_if_result_is_empty(
                [self.get_items_dropdown_from_filter_form, []])
            if bathrooms_list_2 is not None:
                bathrooms_list = bathrooms_list_2
            search_results_page.click_random_result_of_search()

        with allure.step("Check that qty of bathrooms is exist in range between min and max for selected data in "
                         "drop-downs"):
            WorkWithPropertySteps.set_actions_on_property_or_building_page(
                [[self.is_correct_qty_bathrooms, [bathrooms_list]]],
                [[self.is_correct_qty_bathrooms, [bathrooms_list]]])

    def get_items_dropdown_from_filter_form(self):
        """
        Method connected with getting min and max value from drop-down on filter form
        """
        search_results_page = SearchResultsPage()
        search_results_page.click_filter_icon_search_results()

        filter_form = FilterForm()
        filter_form.click_show_amenities_lnk()

        return self.get_items_dropdown()

    def get_items_dropdown(self):
        filter_form = FilterForm()
        bathrooms_list = \
            [Dropdown.get_and_click_upper_case_item(filter_form.drpdwn_min_bathrooms_filter_form,
                                                    filter_form.lbl_minBathrooms_item_dropdown_filter,
                                                    filter_form.lst_minBathrooms_dropdown_form),
             Dropdown.get_and_click_upper_case_item
             (filter_form.drpdwn_max_bathrooms_filter_form,
              filter_form.lbl_maxBathrooms_item_dropdown_filter,
              filter_form.lst_maxBathrooms_dropdown_form)]

        return bathrooms_list

    def is_correct_qty_bathrooms(self, bathrooms_list):
        property_detail_page = PropertyDetailsPage()
        property_detail_page.wait_page_to_load()
        for i in range(0, len(bathrooms_list)):
            bathrooms_list[i] = 0 if bathrooms_list[i] == EnvReader().get_from_locale("Base Page Journey.min") \
                else bathrooms_list[i]
            bathrooms_list[i] = 10 if bathrooms_list[i] == EnvReader().get_from_locale("Base Page Journey.max") \
                else bathrooms_list[i]

        assert_that(
            property_detail_page.get_qty_bathrooms() in range(int(bathrooms_list[0]), int(bathrooms_list[1]) + 1),
            "Qty of bathrooms isn't exist in range between min and max for selected data in drop-downs")
