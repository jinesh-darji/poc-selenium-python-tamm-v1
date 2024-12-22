import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.deed_transfer.DeedTrasferPage import DeedTransferPage
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from framework.browser.Browser import Browser


class TestRegistrationPage:
    """User can go to property registration form: BUAH-1982"""

    @pytest.mark.smoke
    def test_local_user_can_go_to_property_registration_form(self):

        with allure.step("Template: Go to Search page (BUAH-1422) "):
            LogInAsUserSteps.login_as_user(FAKE_USER)

            NavigateSteps.go_to_search_page_local_user()

        with allure.step("Select random home from Recently added locations"):
            search_home_page = SearchHomePage()
            search_home_page.click_random_result_of_search()

        with allure.step("User clicks on \"Check financing Options\" button"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("Select \"No, proceed to deed transfer\" button"):
            property_details_page.click_proceed_deed_transfer_btn()

        self.click_view_btn()

        with allure.step("Close ADM registration pop up"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            deed_transfer_property_registration_page.click_close_registration_pop_up_btn()

        with allure.step("Reload page"):
            Browser.refresh_page()

        with allure.step("Close ADM registration pop up"):
            deed_transfer_property_registration_page.click_close_registration_pop_up_btn()

        with allure.step("Go to previous page"):
            Browser.back_page()

        self.click_view_btn()

        with allure.step("Select \"No\" button on ADM registration pop up"):
            deed_transfer_property_registration_page.click_no_registration_pop_up_btn()
            assert_that(not_(deed_transfer_property_registration_page.is_registration_pop_up_present()),
                        'ADM registration pop up is present')

        with allure.step("Go to previous page"):
            Browser.back_page()

        self.click_view_btn()

        with allure.step("Check that ADM registration pop up is present"):
            assert_that(deed_transfer_property_registration_page.is_registration_pop_up_present(),
                        'ADM registration pop up isn\'t present')

    def click_view_btn(self):
        with allure.step("Select \"View\" button for the 1st step"):
            deed_transfer_page = DeedTransferPage()
            deed_transfer_page.click_view_btn()
