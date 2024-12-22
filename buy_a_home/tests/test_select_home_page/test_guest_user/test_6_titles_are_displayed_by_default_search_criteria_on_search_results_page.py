import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from framework.utils.DataReader import DataReader


class TestTitlesOnThePage:
    """Test that 6 titles are displayed by default search criteria on Search Results page: BUAH-1371"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_6_titles_are_displayed_by_default_search_criteria_on_search_results_page(self):
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Search' Button on 'Select Home' Page"):
            select_home_page = SelectHomePage()
            select_home_page.click_search_btn()

        with allure.step("Click Load more button"):
            search_home_page = SearchHomePage()
            count_homes = search_home_page.get_count_of_home_results()
            search_home_page.click_btn_load_more()
            count_homes_2 = search_home_page.get_count_of_home_results()
            assert_that(count_homes != count_homes_2, "Load more button doesn't work")

        NavigateSteps.go_to_search_results_page()

        with allure.step("Check that 6 titles and Load more button are displayed on Search Results page"):
            search_results_page = SearchResultsPage()
            assert_that(search_results_page.get_count_of_home_results() == DataReader.
                        get_data("Qty of items.qty of properties")
                        and search_results_page.is_load_more_btn_present,
                        "6 titles and Load More button aren't displayed by default")

        with allure.step("Click Load More button and check that quantity of homes is increased or Load More button is "
                         "absent"):
            search_results_page.click_btn_load_more()
            assert_that(search_results_page.get_count_of_home_results() != DataReader.
                        get_data("Qty of items.qty of properties")
                        or not_(search_results_page.is_load_more_btn_present),
                        "Quantity of homes is increased or Load More button is absent")
