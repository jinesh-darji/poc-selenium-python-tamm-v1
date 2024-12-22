import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.get_utilities.EtisalatPage import EtisalatPage
from buy_a_home.pages.get_utilities.GetUtilitiesPage import GetUtilitiesPage
from buy_a_home.pages.get_utilities.WaterElectricityPage import WaterElectricityPage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, DUBAI_USER_NOT_VERIFIED, DUBAI_USER_VERIFIED, \
    ABU_DHABI_USER_NOT_VERIFIED, ABU_DHABI_USER_VERIFIED


class TestGuestViewPackages:
    """Check that all kind of users can go to water and Electricity page and view Etisalat packages: BUAH-1954,
    BUAH-2642, BUAH-2643, BUAH-2644"""

    @pytest.mark.smoke
    @pytest.mark.parametrize("user", [DUBAI_USER_NOT_VERIFIED,
                                      DUBAI_USER_VERIFIED, ABU_DHABI_USER_NOT_VERIFIED, ABU_DHABI_USER_VERIFIED])
    def test_guest_user_can_go_to_etisalat_page_and_view_packages(self, user):
        with allure.step("Login as all kind of users"):
            LogInAsUserSteps.login_as_user(user)

        with allure.step("Go to \"Get utilities page\""):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_UTILITIES.value)
            get_utilities_page = GetUtilitiesPage()
            assert_that(get_utilities_page.is_opened(), "Get utilities page isn\'t opened")

        with allure.step("Select \"View\" button for the 1st step"):
            get_utilities_page.click_view_btn_water_and_electricity()
            water_electricity_page = WaterElectricityPage()
            assert_that(water_electricity_page.is_opened(), "Water and Electricity page isn\'t opened")

        with allure.step("Select \"Continue to etisalat\" button on \"Water and Electricity\" page"):
            water_electricity_page.click_continue_btn_water_and_electricity()
            etisalat_page = EtisalatPage()
            assert_that(etisalat_page.is_opened(), "Etisalat page isn\'t opened")

            self.click_view_details_btn()

            self.click_to_close_package_details()

        with allure.step("Click to Load more button"):
            etisalat_page.click_load_more_btn()

        self.click_view_details_btn()

        self.click_to_close_package_details()

        assert_that(not_(etisalat_page.is_package_details_pop_up_present()), "\"Package details\" is opened")

    def click_view_details_btn(self):
        with allure.step("Select \"View\" button for random package"):
            etisalat_page = EtisalatPage()
            etisalat_page.click_to_1st_view_details_button()

    def click_to_close_package_details(self):
        with allure.step("Close Package Details"):
            etisalat_page = EtisalatPage()
            etisalat_page.click_to_close_details_pop_up()
