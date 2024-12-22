import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.select_home.HomeGrantPage import HomeGrantPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, ABU_DHABI_USER_NOT_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps


class TestGrantPageAbuDhabiUser:
    """Logged in "Emirati" user from Abu Dhabi checks ready-home grant information after check Search Home process
    page."""

    @pytest.mark.smoke
    def test_TS009_emirati_user_from_Aby_Dhabi_search_home_page(self):
        LogInAsUserSteps.login_as_user(ABU_DHABI_USER_NOT_VERIFIED)

        with allure.step("Go to \"Select home\" page"):
            NavigateSteps.go_to_select_home_page()

        with allure.step("Select \"Buy a new home\""):
            home_page = HomePage()
            home_page.click_buy_home_btn()

        with allure.step("Check that Ready home grant module is displayed"):
            select_home_page = SelectHomePage()
            assert_that(not_(select_home_page.is_ready_home_grant()), "\"Ready home grant\" module is not present")

        with allure.step("User clicks on \"Apply\" button of House Purchase Loan component"):
            select_home_page.click_apply_btn()

        with allure.step("User clicks on General Information link"):
            home_grant_page = HomeGrantPage()
            home_grant_page.click_general_info_lnk()

        with allure.step("Pop up with information was opened"):
            home_grant_page.wait_page_to_load()
            assert_that(home_grant_page.is_general_info_pop_up_present(), "General Information pop up isn't opened")

        with allure.step("User closes General Information screen"):
            home_grant_page.click_close_general_info_btn()

        with allure.step("Pop up with information was closed"):
            home_grant_page.wait_page_to_load()
            assert_that(not_(home_grant_page.is_general_info_pop_up_present()), "General Information pop up is opened")