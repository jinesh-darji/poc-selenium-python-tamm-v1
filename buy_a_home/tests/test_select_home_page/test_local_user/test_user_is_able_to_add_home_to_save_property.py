import pytest
import allure
from hamcrest import assert_that

from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage


class TestAddDataToSavedProperties:
    """Test that User is able to add home to save property: BUAH-1406, BUAH-1795"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_user_is_able_to_add_home_to_save_property(self):
        LogInAsUserSteps.login_as_user(FAKE_USER)

        NavigateSteps.go_to_search_page_local_user()

        with allure.step("Click to star for random home in Feature locations module"):
            search_home_page = SearchHomePage()
            search_data = search_home_page.get_data_from_home_with_star(search_home_page.get_first_item_from_locator(
                search_home_page.lst_of_results_quick_search))
            assert_that(search_home_page.is_selected_star_present(search_data[0]), "Star wasn't selected for home")

        NavigateSteps.go_to_search_results_page()

        with allure.step("Click Load More button and if home with star wasn't found"):
            search_results_page = SearchResultsPage()
            while search_results_page.lbl_star_results.try_wait_for_absent():
                search_results_page.click_btn_load_more()

        with allure.step("Select to star for the first home in Search results page"):
            search_data_2 = search_results_page.click_and_return_data_for_home_with_selected_star(
                search_results_page.get_first_item_from_locator(
                    search_results_page.lst_of_results_price_with_stars))

            WorkWithPropertySteps.set_actions_on_property_or_building_page([[self.is_selected_star_present,
                                                                             [search_data_2[0]]]],
                                                                           [[self.is_selected_star_present,
                                                                             [search_data_2[0]]]])

        NavigateSteps.go_to_saved_properties_page_local_user()

        with allure.step("Check that homes from previous steps are displayed on the Saved Properties page"):
            saved_properties_page = SavedPropertiesPage()
            assert_that(saved_properties_page.is_home_with_specific_price_present(search_data[0]) and
                        saved_properties_page.is_home_with_specific_price_present(search_data_2[0]),
                        "The first and the Second page isn't displayed")

        with allure.step("Click to last selected home"):
            saved_properties_page.click_property_detail(search_data_2[0])

        with allure.step("Check that Price, Island, Area data exist on Property details page"):
            property_detail_page = PropertyDetailsPage()
            assert_that(property_detail_page.is_price_present(search_data_2[0]) and property_detail_page.
                        is_island_data_present(search_data_2[1]) and property_detail_page.is_area_data_present
                        (search_data_2[2]), "Price or Island or Area aren't exist on Property Details Page")

    def is_selected_star_present(self, price):
        with allure.step("Check that star was selected for selected home"):
            property_detail_page = PropertyDetailsPage()
            assert_that(property_detail_page.is_selected_star_present(price), "Star wasn't selected for home")
