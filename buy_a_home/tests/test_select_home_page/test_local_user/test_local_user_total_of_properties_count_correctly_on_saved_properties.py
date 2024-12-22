import allure
import pytest
from hamcrest import assert_that, not_

from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from framework.browser.Browser import Browser

COUNT_OF_PROPERTIES_BEFORE_REMOVING = 2  # Counter before removing property
COUNT_OF_PROPERTIES_AFTER_REMOVING = 1  # Counter after removing property


class TestTotalCount:
    """Local user: saved properties: total of properties count correct: BUAH-2243"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_local_user_total_of_properties_count_correctly_on_saved_properties(self):
        LogInAsUserSteps.login_as_user(FAKE_USER)
        NavigateSteps.go_to_select_home_page_local_user()

        self.is_saved_properties_not_present()

        with allure.step("Select Search for home"):
            select_home_page = SelectHomePage()
            select_home_page.click_search_btn()

        with allure.step("Select star for the first home"):
            search_home_page = SearchHomePage()
            search_data = search_home_page.get_data_from_home_with_star(search_home_page.get_first_item_from_locator(
                search_home_page.lst_of_results_quick_search))
            assert_that(search_home_page.is_selected_star_present(search_data[0]), "Star wasn't selected for home")

        with allure.step("Select Villa and go to Search results page"):
            search_home_page.click_villa_chbx(search_home_page.chbx_villa_quick_search)
            search_home_page.click_apply_btn()

        with allure.step("Click to random home with available star"):
            search_results_page = SearchResultsPage()
            data_about_home = search_results_page.get_first_item_from_locator(search_results_page.
                                                                              lst_properties_without_selected_heart)
            search_results_page.click_star(data_about_home[0])
            assert_that(search_results_page.is_selected_star_present(data_about_home[0]),
                        "Star wasn't selected for home")

        with allure.step("Go to home page"):
            search_results_page.click_buah_breadcrumb()

            NavigateSteps.go_to_select_home_page_local_user()

        with allure.step("Select Saved properties button"):
            select_home_page.click_saved_properties_btn()

        self.check_count_of_title_and_props()

        with allure.step("Check that count of title = 2"):
            self.check_count_of_title_and_constants(COUNT_OF_PROPERTIES_BEFORE_REMOVING)

        with allure.step("Remove the first home from Saved properties page"):
            saved_properties_page = SavedPropertiesPage()
            saved_properties_page.click_heart_icon_saved_property(search_data[0])

        with allure.step("Click to \"Yes\" button"):
            saved_properties_page.click_yes_btn_remove_heart()

        with allure.step("Check that home was removed from Saved property page"):
            assert_that(not_(saved_properties_page.is_home_with_specific_price_present(search_data[0])),
                        "The first home is present")

        with allure.step("Refresh page"):
            Browser.refresh_page()

        self.check_count_of_title_and_props()

        with allure.step("Check that count of title = 1"):
            self.check_count_of_title_and_constants(COUNT_OF_PROPERTIES_AFTER_REMOVING)

    def is_saved_properties_not_present(self):
        with allure.step("Check that Saved property doesn't displayed"):
            select_home_page = SelectHomePage()
            assert_that(not_(select_home_page.is_saved_properties_btn_present()), 'Saved properties is displayed')

    def check_count_of_title_and_props(self):
        with allure.step("Check that count from Saved properties page = count properties on the page"):
            saved_properties_page = SavedPropertiesPage()
            count_of_title_for_props = saved_properties_page.get_count_of_props()
            count_of_props = saved_properties_page.get_count_of_home_results()
            assert_that(int(count_of_title_for_props) == count_of_props)

    def check_count_of_title_and_constants(self, constant):
        saved_properties_page = SavedPropertiesPage()
        count_of_title_for_props = saved_properties_page.get_count_of_props()
        assert_that(int(count_of_title_for_props) == constant, 'Counters are not equaled')
