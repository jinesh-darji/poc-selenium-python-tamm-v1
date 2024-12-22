import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.select_home.HomeGrantPage import HomeGrantPage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, ABU_DHABI_USER_NOT_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps


class TestGrantPageAbuDhabiUser:
    """Logged in "Emirati" user from Abu Dhabi  checks ready-home grant information"""

    @pytest.mark.smoke
    def test_TS008_emirati_user_Abu_Dhabi(self):
        LogInAsUserSteps.login_as_user(ABU_DHABI_USER_NOT_VERIFIED)

        with allure.step("Go to \"Select home\" page"):
            NavigateSteps.go_to_select_home_page()

        with allure.step("Check that pop up with home grant option is displayed"):
            home_page = HomePage()
            assert_that(home_page.is_home_grant_option_present(), 'Home grant option is absent')

        with allure.step("Select Apply for ready home grant button"):
            home_page.click_apply_for_ready_nome_grant_btn()

        with allure.step("Check that Ready Home Grant page is opened "):
            home_grant_page = HomeGrantPage()
            assert_that(home_grant_page.is_opened(), "Home grant page isn't opened")

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
