import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from framework.browser.Browser import Browser


class TestApplyButtonSearch:
    """Apply button should be disabled if neither of Apartment or Villa checkboxes are checked: BUAH-1619"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_always_available_apply_button_for_search(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Check that Apartment and Villa checkboxes are deselected"):
            search_home_page = SearchHomePage()
            assert_that(search_home_page.chbx_apartment_quick_search.is_present() and
                        search_home_page.chbx_villa_quick_search.is_present(), "Checkbox Apartment is selected "
                                                                               "or Checkbox Villa is selected")

        with allure.step("Check that Apply button is available"):
            assert_that(not_(search_home_page.btn_apply_not_available.get_element_disabled()),
                        "Apply button isn't available")

        with allure.step("Select Apartment checkbox and check that Apply button is available"):
            search_home_page.click_apartment_chbx(search_home_page.chbx_apartment_quick_search)
            assert_that(not_(search_home_page.btn_apply_not_available.get_element_disabled()),
                        "Apply button isn't available")

        with allure.step("Click filter icon and check that Apartment and Villa checkboxes are deselected"):
            search_home_page.click_filter_icon()
            filter_form = FilterForm()
            assert_that(filter_form.chbx_apartment_filter_disable.is_present()
                        and filter_form.chbx_villa_filter_enable.is_present(), "Checkbox Apartment isn't selected or "
                                                                               "Checkbox Villa is selected")

        with allure.step("Check that Apply button is available on Filter Form"):
            assert_that(not_(filter_form.btn_apply_filter_not_available.get_element_disabled()),
                        "Apply button isn't available")

        with allure.step("Select Villa and check that Apply button is available on Filter Form"):
            filter_form.click_villa_chbx(filter_form.chbx_villa_filter_enable)
            assert_that(not_(search_home_page.btn_apply_not_available.get_element_disabled()),
                        "Apply button isn't available")

        with allure.step("Click Apply button"):
            filter_form.click_apply_btn_filter()

        with allure.step("Go to previous page"):
            Browser.back_page()

        with allure.step(
                "Check that Apartment checkbox isn't selected, Villa - is selected, Apply button is selected "):
            assert_that(search_home_page.chbx_apartment_quick_search_disable.is_present()
                        and search_home_page.chbx_villa_quick_search_disable.is_present(),
                        "Checkbox Apartment is selected or "
                        "Checkbox Villa is deselected")
            assert_that(not_(search_home_page.btn_apply_not_available.get_element_disabled()),
                        "Apply button isn't available")
