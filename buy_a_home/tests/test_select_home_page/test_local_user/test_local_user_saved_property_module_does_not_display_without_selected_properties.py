import allure
import pytest
from hamcrest import assert_that, not_

from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from framework.browser.Browser import Browser


class TestAddDataToSavedProperties:
    """Select home: Local user: "Saved properties" button isn't displayed if user didn't select heart for property:
    BUAH-1805"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_local_user_saved_property_module_does_not_display_without_selected_properties(self):
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

        with allure.step("Select Home page"):
            search_home_page.click_buah_breadcrumb()

            NavigateSteps.go_to_select_home_page_local_user()

        self.is_saved_properties_present()

        with allure.step("Refresh page"):
            Browser.refresh_page()

        self.is_saved_properties_present()

        with allure.step("Select Saved properties"):
            select_home_page.click_saved_properties_btn()

        with allure.step("Remove save for home"):
            saved_properties_page = SavedPropertiesPage()
            saved_properties_page.click_heart_icon_saved_property(search_data[0])

        with allure.step("Click yes button"):
            saved_properties_page.click_yes_btn_remove_heart()
            assert_that(not_(saved_properties_page.is_home_with_specific_price_present(search_data[0])),
                        'Home is not removed')

        with allure.step("Go back"):
            Browser.back_page()

        self.is_saved_properties_not_present()

    def is_saved_properties_present(self):
        with allure.step("Check that Saved property is displayed"):
            select_home_page = SelectHomePage()
            assert_that(select_home_page.is_saved_properties_btn_present(), 'Saved properties is not displayed')

    def is_saved_properties_not_present(self):
        with allure.step("Check that Saved property doesn't displayed"):
            select_home_page = SelectHomePage()
            assert_that(not_(select_home_page.is_saved_properties_btn_present()), 'Saved properties is displayed')
