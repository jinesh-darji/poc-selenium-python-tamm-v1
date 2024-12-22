import pytest
import allure
from hamcrest import assert_that

from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage


class TestAreaOfHome:
    """Test that User is able to see homes in results of search from specific area: BUAH-1377"""

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_user_is_able_to_see_homes_in_result_of_search_from_specific_area(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Select some area and Click Apply button"):
            search_home_page = SearchHomePage()
            area = search_home_page.get_random_area_drpdwn()

        NavigateSteps.go_to_search_results_page()

        with allure.step("Select random home according search result"):
            search_results_page = SearchResultsPage()
            area_2 = search_results_page.set_and_return_new_random_area()
            if area_2 != '':
                area = area_2
            search_results_page.click_random_result_of_search()

        with allure.step("Check that area on property detail is equal area data from search field"):
            WorkWithPropertySteps.set_actions_on_property_or_building_page([[self.is_area_present, [area]]],
                                                             [[self.is_area_present, [area]]])

    def is_area_present(self, area):
        """
        Check that area is exist on property details page
        :param area: area
        :return: bool: area is exist or not
        """
        property_detail_page = PropertyDetailsPage()
        assert_that(property_detail_page.is_area_data_present(area), "Area doesn't present")
