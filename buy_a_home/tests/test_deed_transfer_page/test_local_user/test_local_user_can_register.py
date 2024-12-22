import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.deed_transfer.DeedTrasferPage import DeedTransferPage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER


class TestRegisterAction:
    """User can register on property registration page: BUAH-2213"""

    @pytest.mark.smoke
    def test_local_user_can_register(self):
        with allure.step("Login as Local and not verified user"):
            LogInAsUserSteps.login_as_user(FAKE_USER)

        self.go_to_deed_transfer_page()

        with allure.step("Select \"Yes\" button on ADM registration pop up"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            deed_transfer_property_registration_page.click_yes_registration_pop_up_btn()

        with allure.step("Check that Success pop up is present"):
            assert_that(deed_transfer_property_registration_page.is_success_pop_up_present(),
                        'Success pop up isn\'t present')

        with allure.step("Select OK button"):
            deed_transfer_property_registration_page.click_ok_btn_on_success_pop_up()
            assert_that(not_(deed_transfer_property_registration_page.is_success_pop_up_present()),
                        'Success pop up is present')

        with allure.step("Check that in progress message is present"):
            assert_that(deed_transfer_property_registration_page.is_in_progress_message_present(),
                        'Message isn\'t present')

        with allure.step("Go to home page"):
            deed_transfer_property_registration_page.click_buah_breadcrumb()

            self.go_to_deed_transfer_page()

        with allure.step("Check that in progress message is present"):
            assert_that(deed_transfer_property_registration_page.is_in_progress_message_present(),
                        'Message isn\'t present')

    def go_to_deed_transfer_page(self):
        with allure.step("User clicks Deed Transfer button"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.DEED_TRANSFER.value)

        with allure.step("Select \"View\" button for the 1st step"):
            deed_transfer_page = DeedTransferPage()
            deed_transfer_page.click_view_btn()
