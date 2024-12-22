import pytest
import allure
from hamcrest import assert_that

from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.HomeGrantPage import HomeGrantPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage


class TestGeneralInfoGrant:
    """User is able to see general information about buying home from a home grant: BUAH-1469"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_general_information_about_buying_home_is_displayed_on_a_home_grant(self):
        LogInAsUserSteps.login_as_user(FAKE_USER)

        NavigateSteps.go_to_select_home_page_local_user()

        with allure.step("Select Apply for Ready Home Grant"):
            select_home_page = SelectHomePage()
            select_home_page.click_apply_btn()

        with allure.step("Select General information"):
            home_grant_page = HomeGrantPage()
            home_grant_page.click_general_info_lnk()

        with allure.step("Pop up with information was opened"):
            home_grant_page.wait_page_to_load()
            assert_that(home_grant_page.is_general_info_pop_up_present(), "General Information pop up isn't opened")
