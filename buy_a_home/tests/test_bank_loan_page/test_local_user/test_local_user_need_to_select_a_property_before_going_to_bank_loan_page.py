import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage

from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER


class TestEmiratiCanNotReSelectProperty:
    """Local user: As a logged in user, I can not select a property to proceed for Financing options if saved
    properties page is empty: BUAH-1851"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_local_user_need_to_select_a_property_before_going_to_bank_loan_page(self):
        with allure.step("Template: Go to Search page (BUAH-1422)"):
            LogInAsUserSteps.login_as_user(FAKE_USER)

        with allure.step("Select Get Financing"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_FINANCING.value)

        with allure.step("Select \"Yes, check bank loan page\""):
            home_page.click_check_bank_loan_btn()

        with allure.step("Click to \"View loan options\""):
            financing_page = FinancingPage()
            assert_that(financing_page.is_opened(), "Financing page isn't opened")
            financing_page.click_start_btn()

        with allure.step("Check that Search a home button is displayed"):
            saved_properties_page = SavedPropertiesPage()
            assert_that(saved_properties_page.btn_search_a_home.is_present(), "Search a home button is not displayed")

