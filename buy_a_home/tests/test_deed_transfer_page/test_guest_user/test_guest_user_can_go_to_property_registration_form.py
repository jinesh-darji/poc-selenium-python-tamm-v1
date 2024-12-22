import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.deed_transfer.DeedTrasferPage import DeedTransferPage
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.steps.NavigateSteps import NavigateSteps


class TestRegistrationPage:
    """User can go to property registration form: BUAH-1775, BUAH-1934"""

    @pytest.mark.smoke
    @pytest.mark.guest_user
    def test_guest_user_can_go_to_property_registration_form(self):

        with allure.step("Template: Go to Search page (BUAH-1422) "):
            NavigateSteps.go_to_search_page()

        with allure.step("Select random home from Recently added locations"):
            search_home_page = SearchHomePage()
            search_home_page.click_random_result_of_search()

        with allure.step("Click to \"Check financing Options\" button"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("Select \"No, proceed to deed transfer\" button"):
            property_details_page.click_proceed_deed_transfer_btn()

        with allure.step("Select \"View\" button for the 1st step"):
            deed_transfer_page = DeedTransferPage()
            deed_transfer_page.click_view_btn()

        with allure.step("Property registration page is opened, property details is absent"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            assert_that(not_(deed_transfer_property_registration_page.is_chosen_home_present()),
                        "\"Chosen home\" is present")
            assert_that(not_(deed_transfer_property_registration_page.is_registration_pop_up_present()),
                        'ADM registration pop up is present')

