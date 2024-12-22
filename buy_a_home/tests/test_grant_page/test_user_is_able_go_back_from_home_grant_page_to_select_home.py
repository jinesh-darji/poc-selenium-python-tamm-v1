import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.HomeGrantPage import HomeGrantPage
from framework.browser.Browser import Browser


class TestGoBackGrantPage:
    """User is able to go back from home grant page: BUAH-1471"""

    @pytest.mark.regression
    @pytest.mark.local_user
    def test_user_is_able_go_back_from_home_grant_page_to_select_home(self):
        LogInAsUserSteps.login_as_user(FAKE_USER)

        NavigateSteps.go_to_home_grant_page_local_user()

        with allure.step("Check that Home grant page is opened"):
            home_grant_page = HomeGrantPage()
            assert_that(home_grant_page.is_opened(), "Home grant page isn't opened")

        with allure.step("Go back and check that home page is opened"):
            Browser.back_page()
            home_page = HomePage()
            assert_that(home_page.is_opened(), "Home page isn't opened")
