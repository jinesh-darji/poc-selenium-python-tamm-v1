import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from framework.utils.DataReader import DataReader


class TestGuestUserServices:
    """Guest user check services pop-up: BUAH-2439"""

    @pytest.mark.guest_user
    @pytest.mark.regression
    def test_guest_user_check_services_on_property_details_page(self):
        with allure.step("Open \"Buy a Home\" journey homepage, Click on \"Select Home\" button and User clicks"
                         " on \"Search for Home\" button under \"Search for Home\""):
            NavigateSteps.go_to_search_page()

        with allure.step("Go to property details page for the first property"):
            search_home_page = SearchHomePage()
            data_about_home = search_home_page.get_first_item_from_locator(search_home_page.
                                                                           lst_properties_without_selected_heart)
            search_home_page.click_property_detail(data_about_home[0])

        with allure.step("User clicks on Services button on screen"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_services_btn()

        with allure.step("Select all services"):
            property_details_page.click_services_all_checkbx()

        with allure.step("Select randomly 2 nearby services"):
            list_of_services = property_details_page.get_services(DataReader.get_data("Qty of items.qty of services"))
            property_details_page.click_random_checkboxes(property_details_page.chbx_of_service,
                                                          list_of_services)

        with allure.step("User closes Services pop-up screen"):
            property_details_page.click_services_close_btn()

        with allure.step("Check that pop up is closed"):
            assert_that(not_(property_details_page.is_services_pop_up_opened()), "Services pop-up is opened")
