import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, DUBAI_USER_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.HomeGrantPage import HomeGrantPage


class TestExpatGrant:
    """Logged in "Emirati" user from Dubai. No pop up with options after selecting \"Select Home\" """

    @pytest.mark.smoke
    @pytest.mark.expat_user
    def test_TS006_emirati_user_Dubai(self):
        LogInAsUserSteps.login_as_user(DUBAI_USER_VERIFIED)

        NavigateSteps.go_to_select_home_page()

        with allure.step("Check that Ready home grant isn't displayed"):
            home_grant_page = HomeGrantPage()
            assert_that(not_(home_grant_page.is_apply_via_adha_button_present()), 'Apply button is absent')
