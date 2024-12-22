import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.get_utilities.EtisalatPage import EtisalatPage
from buy_a_home.pages.get_utilities.GetUtilitiesPage import GetUtilitiesPage
from buy_a_home.pages.get_utilities.WaterElectricityPage import WaterElectricityPage


class TestGuestViewPackages:
    """Bank loan page: Monthly payment calculate correctly: BUAH-1956"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_guest_user_can_go_to_etisalat_page_and_view_packages(self):
        with allure.step("Go to \"Get utilities\" page"):
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

        with allure.step("Click to close login pop-up"):
            etisalat_page.click_close_login_popup_btn()

        with allure.step("Click to random \"Request\" button"):
            etisalat_page.click_to_1st_request_button()

        with allure.step("Click to close login pop-up"):
            etisalat_page.click_close_login_popup_btn()
        assert_that(not_(etisalat_page.is_login_pop_up_present()), "\"login pop-up\" is present")
