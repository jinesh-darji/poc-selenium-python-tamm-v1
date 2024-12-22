import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.HomeGrantPage import HomeGrantPage


class TestGeneralInfoGrant:
    """Local user can see "Ready home grant" on Select home page: BUAH-1765"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_local_user_can_see_ready_home_grant_on_select_home_page(self):
        LogInAsUserSteps.login_as_user(FAKE_USER)

        NavigateSteps.go_to_select_home_page()

        with allure.step("Select Apply for Ready Home Grant"):
            home_page = HomePage()
            home_page.click_apply_for_ready_nome_grant_btn()

        with allure.step("Check that Ready home grand page is opened"):
            home_grant_page = HomeGrantPage()
            assert_that(home_grant_page.is_opened(), 'Page is not opened')
            assert_that(home_grant_page.is_apply_via_adha_button_present(), 'Apply button is absent')
