import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, DUBAI_USER_NOT_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps


class TestGrantPageDubaiUser:
    """Grant home doesn't display for Emirati user from Dubai: BUAH-2219"""

    @pytest.mark.smoke
    def test_grant_home_page_do_not_display_for_user_from_dubai(self):
        LogInAsUserSteps.login_as_user(DUBAI_USER_NOT_VERIFIED)

        with allure.step("Go to \"Select home\" page"):
            NavigateSteps.go_to_select_home_page()

        with allure.step("Check that grant home module is absent"):
            select_home_page = SelectHomePage()
            assert_that(not_(select_home_page.is_ready_home_grant()), "\"Ready home grant\" module is not present")
