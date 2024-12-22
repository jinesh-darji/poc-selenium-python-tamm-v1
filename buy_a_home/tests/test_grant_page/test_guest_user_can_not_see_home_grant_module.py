import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage


class TestGuestHomeGrant:
    """Guest user can not see "Ready home grant" on Select home page: BUAH-1767"""

    @pytest.mark.smoke
    @pytest.mark.guest_user
    def test_guest_user_can_not_see_home_grant_module(self):
        NavigateSteps.go_to_select_home_page()

        with allure.step("Select Apply for Ready Home Grant"):
            select_home_page = SelectHomePage()
            assert_that(not_(select_home_page.is_ready_home_grant()), "\"Ready home grant\" module is present")
