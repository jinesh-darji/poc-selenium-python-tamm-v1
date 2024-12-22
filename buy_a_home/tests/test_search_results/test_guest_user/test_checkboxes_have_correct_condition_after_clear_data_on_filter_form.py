import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from framework.browser.Browser import Browser


class TestChbxesQuickSearchAndFilterFormClearButton:
    """Test that checkboxes have correct condition after clear data on filter form BUAH-2375"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_checkboxes_have_correct_condition_after_clear_data_on_filter_form(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Select Villa checkbox and check that data from quick search are displayed on filter "
                         "form"):
            search_home_page = SearchHomePage()
            search_home_page.click_villa_chbx(search_home_page.chbx_villa_quick_search)
            filter_form = FilterForm()
            assert_that(search_home_page.is_chbx_desabled_or_enabled_present(search_home_page.
                                                                             chbx_apartment_quick_search, )
                        and
                        search_home_page.is_chbx_desabled_or_enabled_present(search_home_page.
                                                                             chbx_villa_quick_search_disable),
                        "Checkbox Apartment is selected"
                        "or Checkbox Villa is deselected")

        with allure.step("Check that Apartment is deselected and Villa checkbox is selected on filter form"):
            self.click_apply_btn_and_click_filter_icon()
            assert_that(filter_form.is_chbx_desabled_or_enabled_present(filter_form.chbx_apartment_filter_enable)
                        and filter_form.is_chbx_desabled_or_enabled_present(filter_form.chbx_villa_filter_disable),
                        "Checkbox Apartment is selected or "
                        "Checkbox Villa is deselected")

        with allure.step("Go to previous page"):
            Browser.back_page()

        with allure.step("Check that Apartment is deselected and Villa checkbox is selected on quick search"):
            assert_that(search_home_page.is_chbx_desabled_or_enabled_present(search_home_page.
                                                                             chbx_apartment_quick_search, )
                        and
                        search_home_page.is_chbx_desabled_or_enabled_present(search_home_page.
                                                                             chbx_villa_quick_search_disable),
                        "Checkbox Apartment is selected"
                        "or Checkbox Villa is deselected")

        with allure.step("Click Apply button and click Filter icon"):
            self.click_apply_btn_and_click_filter_icon()

        with allure.step("Click Clear button"):
            filter_form.click_clear_btn()

        with allure.step("Check that Apartment and Villa checkboxes are deselected"):
            assert_that(filter_form.is_chbx_desabled_or_enabled_present(filter_form.chbx_apartment_filter_enable)
                        and filter_form.is_chbx_desabled_or_enabled_present(filter_form.chbx_villa_filter_enable),
                        "Checkbox Apartment is selected or "
                        "Checkbox Villa is selected")

        with allure.step("Close Filter form"):
            filter_form.click_close_filter_pop_up_btn()

        with allure.step("Open filter form"):
            search_results_page = SearchResultsPage()
            search_results_page.click_filter_icon()

        with allure.step("Check that Apartment is deselected and Villa checkbox is selected on filter form"):
            filter_form = FilterForm()
            assert_that(search_home_page.is_chbx_desabled_or_enabled_present(filter_form.
                                                                             chbx_apartment_filter_enable)
                        and
                        search_home_page.is_chbx_desabled_or_enabled_present(filter_form.chbx_villa_filter_disable),
                        "Checkbox Apartment is selected"
                        "or Checkbox Villa is deselected")

    def click_apply_btn_and_click_filter_icon(self):
        """
        Method connected with clicking Apply Buttons and Filter icon
        """
        search_home_page = SearchHomePage()
        search_home_page.click_apply_btn()
        search_home_page.click_filter_icon()
