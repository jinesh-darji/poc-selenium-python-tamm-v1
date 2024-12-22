import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.deed_transfer.DeedTrasferPage import DeedTransferPage


class TestRegistrationPage:
    """User can go to property registration form: BUAH-1950"""

    @pytest.mark.smoke
    @pytest.mark.guest_user
    @pytest.mark.sanity
    def test_guest_user_cannot_check_registration_status(self):
        with allure.step("Go to \"Deed transfer page\""):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.DEED_TRANSFER.value)

        with allure.step("Select \"View\" button for the 1st step"):
            deed_transfer_page = DeedTransferPage()
            deed_transfer_page.click_view_btn()

        with allure.step("Property registration page is opened, property details is absent"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            assert_that(not_(deed_transfer_property_registration_page.is_chosen_home_present()),
                        "\"Chosen home\" is present")
            assert_that(not_(deed_transfer_property_registration_page.is_registration_pop_up_present()),
                        "\"Registration pop-up\" is present")
