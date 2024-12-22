import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.get_utilities.EtisalatPage import EtisalatPage
from buy_a_home.pages.get_utilities.GetUtilitiesPage import GetUtilitiesPage
from buy_a_home.pages.get_utilities.WaterElectricityPage import WaterElectricityPage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER


class TestLocalNotVerifiedRequest:
    """Test that local and not verified user have received error message after selecting request button: BUAH-2214"""

    @pytest.mark.regression
    @pytest.mark.local_user
    def test_local_not_verified_error_message_after_selecting_request(self):
        with allure.step("Login as Local and not verified user"):
            LogInAsUserSteps.login_as_user(FAKE_USER)

        with allure.step("Go to \"Get utilities page\""):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_UTILITIES.value)

        with allure.step("Select \"View\" button for the 1st step"):
            get_utilities_page = GetUtilitiesPage()
            get_utilities_page.click_view_btn_water_and_electricity()

        with allure.step("Select \"Continue\" button on \"Water and Electricity\" page"):
            water_electricity_page = WaterElectricityPage()
            water_electricity_page.click_continue_btn_water_and_electricity()

        with allure.step("Select \"View\" button for random package"):
            etisalat_page = EtisalatPage()
            etisalat_page.click_to_1st_view_details_button()

        with allure.step("Select \"Request\" button"):
            etisalat_page.click_to_request_button_pop_up()
            assert_that(etisalat_page.is_error_message_packages_present(), "Error message isn't present")

        with allure.step("Close error message about selecting package"):
            etisalat_page.click_to_ok_btn_in_error_pop_up()
            assert_that(not_(etisalat_page.is_error_message_packages_present()), "Error message is present")

        with allure.step("Click to random \"Request\" button"):
            etisalat_page.click_to_1st_request_button()
            assert_that(etisalat_page.is_error_message_packages_present(), "Error message isn't present")

        with allure.step("Click to close button for error pop up"):
            etisalat_page.click_to_close_btn_in_error_pop_up_package()
            assert_that(not_(etisalat_page.is_error_message_packages_present()), "Error message is present")
