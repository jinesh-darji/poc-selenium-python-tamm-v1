import pytest
import allure
from hamcrest import assert_that

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage


class TestFeaturedDataAreInPropertyDetailsPage:
    """Test Data from Featured locations in Search home are displayed for selected home on Property details page:
    BUAH-1421"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_data_from_featured_locations_are_displayed_on_property_details(self):

        NavigateSteps.go_to_search_page()

        with allure.step("Select random home in Feature locations module"):
            search_home_page = SearchHomePage()
            search_data = search_home_page.get_data_from_selected_home()

        with allure.step("Check that Island, Area, Price data exist in property details page"):
            property_detail_page = PropertyDetailsPage()
            assert_that(property_detail_page.is_price_present(search_data[0]) and property_detail_page.
                        is_island_data_present(search_data[1]) and property_detail_page.is_area_data_present
                        (search_data[2]), "Price or Island or Area aren't exist on Property Details Page")
