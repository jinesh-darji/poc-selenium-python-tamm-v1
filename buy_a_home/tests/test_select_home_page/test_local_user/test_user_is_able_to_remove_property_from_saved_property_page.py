import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage


class TestRemoveDataFromSavedProperties:
    """Test that User is able to remove data from this page: BUAH-1409"""

    @pytest.mark.regression
    def test_user_is_able_to_remove_property_from_saved_property_page(self):
        LogInAsUserSteps.login_as_user(FAKE_USER)

        NavigateSteps.go_to_search_page_local_user()

        with allure.step("Click to star for random home in Feature locations module"):
            search_home_page = SearchHomePage()
            search_data = search_home_page.get_data_from_home_with_star(search_home_page.get_first_item_from_locator(
                search_home_page.lst_of_results_quick_search))
            assert_that(search_home_page.is_selected_star_present(search_data[0]), "Star wasn't selected for home")

        NavigateSteps.go_to_search_results_page_with_villa_chbx()

        with allure.step("Select to star for the first home in Search results page"):
            search_results_page = SearchResultsPage()
            search_results_page.wait_page_to_load()
            search_data_2 = search_results_page.click_and_return_data_for_home_with_selected_star(
                search_results_page.get_first_item_from_locator(search_results_page.lst_of_results_price_with_stars))

            WorkWithPropertySteps.set_actions_on_property_or_building_page([[self.is_selected_star_present,
                                                                             [search_data_2[0]]]],
                                                                           [[self.is_selected_star_present,
                                                                             [search_data_2[0]]]])

        NavigateSteps.go_to_saved_properties_page_local_user()

        with allure.step("Check that homes from previous steps are displayed on the Saved Properties page"):
            saved_properties_page = SavedPropertiesPage()
            assert_that(saved_properties_page.is_home_with_specific_price_present(search_data[0]) and
                        saved_properties_page.is_home_with_specific_price_present(search_data_2[0]),
                        "The first and the second home isn't displayed")

        with allure.step("Remove the first home from Saved properties page"):
            saved_properties_page.click_heart_icon_saved_property(search_data[0])

        with allure.step("Click \"Yes\" button"):
            saved_properties_page.click_yes_btn_remove_heart()

        with allure.step("Check that home was removed from Saved property page"):
            assert_that(not_(saved_properties_page.is_home_with_specific_price_present(search_data[0])) and
                        saved_properties_page.is_home_with_specific_price_present(search_data_2[0]),
                        "The first home is present and the Second home isn't displayed")

    def is_selected_star_present(self, price):
        with allure.step("Check that star was selected for selected home"):
            property_detail_page = PropertyDetailsPage()
            assert_that(property_detail_page.is_selected_star_present(price), "Star wasn't selected for home")
