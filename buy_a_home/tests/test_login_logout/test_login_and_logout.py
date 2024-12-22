import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.smart_pass.SmartPassPage import SmartPassPage

login = "persona.user3"
password = "Persona.user3"


class TestLoginLogout:
    """Test login and logout via smartpass: BUAH-2645"""

    @pytest.mark.smoke
    def test_login_and_logout(self):
        with allure.step("Click to left panel"):
            home_page = HomePage()
            home_page.click_left_panel()

        with allure.step("Click to smart pass button"):
            home_page.click_smart_pass()

        with allure.step("Send login and password"):
            smart_pass_page = SmartPassPage()
            smart_pass_page.send_username(login)
            smart_pass_page.send_password(password)

        with allure.step("Click to login button"):
            smart_pass_page.click_login()

        with allure.step("Click to left panel"):
            home_page.click_left_panel()

        with allure.step("Check the profile is present"):
            assert_that(home_page.is_profile_present(), "Profile label is absent")

        with allure.step("Click to logout button"):
            home_page.click_logout()

        with allure.step("Click to left panel"):
            home_page.click_left_panel()

        with allure.step("Check the profile is not present"):
            assert_that(not_(home_page.is_profile_present()), "Profile label is absent")
            assert_that(home_page.is_smart_pass_btn_presnet(), "Smartpass button is absent")
