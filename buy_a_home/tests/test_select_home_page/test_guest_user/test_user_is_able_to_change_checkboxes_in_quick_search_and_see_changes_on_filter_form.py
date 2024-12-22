import pytest
import allure
from hamcrest import assert_that

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from framework.browser.Browser import Browser


class TestChbxesQuickSearchAndFilterForm:
    """Test that User is able to change checkboxes in quick search and see changes on filter form BUAH-1375"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_user_is_able_to_change_checkboxes_in_quick_search_and_see_changes_on_filter_form(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Select all checkboxes and check that data from quick search are displayed on filter "
                         "form"):
            search_home_page = SearchHomePage()
            search_home_page.click_apartment_and_villa_chbxes()
            filter_form = FilterForm()
            self.check_that_apartment_and_villa_chckxes_are_selected()

        with allure.step("Check that Apartment and Villa checkboxes are deselected on filter form"):
            self.click_apply_btn_and_click_filter_icon()
            assert_that(filter_form.is_chbx_desabled_or_enabled_present(filter_form.chbx_apartment_filter_disable)
                        and filter_form.is_chbx_desabled_or_enabled_present(filter_form.chbx_villa_filter_disable),
                        "Checkbox Apartment is deselected or "
                        "Checkbox Villa is deselected")

        with allure.step("Go to previous page"):
            Browser.back_page()

        with allure.step("Check that Apartment and Villa checkboxes are selected on quick search"):
            self.check_that_apartment_and_villa_chckxes_are_selected()

        with allure.step("Select Apartment checkbox and check that data from quick search are displayed on filter "
                         "form"):
            search_home_page.click_apartment_chbx(search_home_page.chbx_apartment_quick_search_disable)
            self.click_apply_btn_and_click_filter_icon()
            filter_form = FilterForm()
            assert_that(filter_form.is_chbx_desabled_or_enabled_present(filter_form.chbx_apartment_filter_enable)
                        and filter_form.is_chbx_desabled_or_enabled_present(filter_form.chbx_villa_filter_disable),
                        "Checkbox Apartment is selected or "
                        "Checkbox Villa is unselected")

    def check_that_apartment_and_villa_chckxes_are_selected(self):
        """
        Nethod connected with checking that Apartment and Villa checkboxes are selected
        """
        search_home_page = SearchHomePage()
        assert_that(search_home_page.is_chbx_desabled_or_enabled_present(search_home_page.
                                                                         chbx_apartment_quick_search_disable)
                    and
                    search_home_page.is_chbx_desabled_or_enabled_present(search_home_page.
                                                                         chbx_villa_quick_search_disable),
                    "Checkbox Apartment is deselected "
                    "or Checkbox Villa is deselected")

    def click_apply_btn_and_click_filter_icon(self):
        """
        Method connected with clicking Apply Buttons and Filter icon
        """
        search_home_page = SearchHomePage()
        search_home_page.click_apply_btn()
        search_home_page.click_filter_icon()
