import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage


class TestAreaOfHome:
    """Test that Guest user: login pop up is displayed after selecting Save a property: BUAH-1938"""

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_log_in_pop_up_displays_heart_icon(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Click to heart button for random home"):
            search_home_page = SearchHomePage()
            price_for_star = search_home_page.get_random_price_for_home()
            search_home_page.click_star(price_for_star)

            search_home_page.click_close_login_popup_btn()

        NavigateSteps.go_to_search_results_page_with_villa_chbx()

        with allure.step("Click to heart button for random home"):
            search_results_page = SearchResultsPage()
            price_for_star = search_results_page.get_random_price_for_home()
            search_results_page.click_star(price_for_star)

        with allure.step("Click to close login pop up"):
            search_results_page.click_close_login_popup_btn()

        with allure.step("Click to random property details"):
            price_of_home = search_results_page.get_random_property_details_of_price()
            search_results_page.click_property_detail(price_of_home)

        with allure.step("Click to heart button"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_star_property(price_of_home)

        with allure.step("Click to close login pop up"):
            search_results_page.click_close_login_popup_btn()

        assert_that(not_(property_details_page.is_login_pop_up_present()), "\"login pop-up\" is present")
