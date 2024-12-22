import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.select_home.HomeGrantPage import HomeGrantPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, ABU_DHABI_USER_NOT_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps


class TestGrantPageAbuDhabiUserFromSelectHome:
    """User from Abu Dhabi can go to home grant page from Select home page: BUAH-2612"""

    @pytest.mark.smoke
    def test_user_from_abu_dhabi_can_go_to_home_grant_page_from_select_home_page(self):
        LogInAsUserSteps.login_as_user(ABU_DHABI_USER_NOT_VERIFIED)

        NavigateSteps.go_to_select_home_page_local_user()

        with allure.step("Check that Ready home grant module is displayed"):
            select_home_page = SelectHomePage()
            assert_that(not_(select_home_page.is_ready_home_grant()), "\"Ready home grant\" module is not present")

        with allure.step("Click to Apply button for Home grant"):
            select_home_page.click_apply_btn()

        with allure.step("Check that Home grant page is opened"):
            home_grant_page = HomeGrantPage()
            assert_that(home_grant_page.is_opened(), "Home grant page isn't opened")
