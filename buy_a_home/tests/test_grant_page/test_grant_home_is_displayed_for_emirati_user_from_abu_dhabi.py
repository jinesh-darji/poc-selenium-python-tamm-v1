import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.select_home.HomeGrantPage import HomeGrantPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, ABU_DHABI_USER_NOT_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps
from framework.browser.Browser import Browser


class TestGrantPageAbuDhabiUser:
    """Grant home display for Emirati user from Abu Dhabi: BUAH-2218"""

    @pytest.mark.smoke
    def test_grant_home_is_displayed_for_emirati_user_from_abu_dhabi(self):
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

        with allure.step("Go back and click to \"Select home\""):
            Browser.back_page()
            NavigateSteps.go_to_select_home_page()

        with allure.step("Select \"Buy a new home\""):
            home_page.click_buy_home_btn()

        with allure.step("Check that Ready home grant module is displayed"):
            select_home_page = SelectHomePage()
            assert_that(not_(select_home_page.is_ready_home_grant()), "\"Ready home grant\" module is not present")

