import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.deed_transfer.DeedTrasferPage import DeedTransferPage
from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.get_utilities.GetUtilitiesPage import GetUtilitiesPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.get_insurance.GetInsurancePage import GetInsurancePage
from framework.browser.Browser import Browser


class TestNavigationArrows:
    """Navigation Arrows: BUAH-1397"""

    @pytest.mark.smoke
    def test_navigation_arrows(self):
        with allure.step("Go to select home"):
            NavigateSteps.go_to_select_home_page()

        with allure.step("Select Next link on Select home page"):
            select_home_page = SelectHomePage()
            select_home_page.click_next_link()

            financing_page = FinancingPage()
            assert_that(financing_page.is_opened(), "Financing page isn't opened")

        with allure.step("Select Next link on Financing page"):
            financing_page.click_next_link()

            deed_transfer_page = DeedTransferPage()
            assert_that(deed_transfer_page.is_opened(), "Deed Transfer page isn't opened")

        with allure.step("Select Next link on Deed transfer page"):
            deed_transfer_page.click_next_link()

            get_utilities_page = GetUtilitiesPage()
            assert_that(get_utilities_page.is_opened(), "Get Utilities page isn't opened")

        with allure.step("Select Next link on Get Utilities page"):
            get_utilities_page.click_next_link()

            get_insurance_page = GetInsurancePage()
            assert_that(get_insurance_page.is_opened(), "Get Insurance page isn't opened")

        with allure.step("Back to previous page"):
            Browser.back_page()
            assert_that(get_utilities_page.is_opened(), "Get Utilities page isn't opened")

        with allure.step("Select Prev link on Get Utilities page"):
            get_utilities_page.click_prev_link()
            assert_that(deed_transfer_page.is_opened(), "Deed Transfer page isn't opened")

        with allure.step("Select Prev link on Deed Transfer page"):
            deed_transfer_page.click_prev_link()
            assert_that(financing_page.is_opened(), "Financing page isn't opened")

        with allure.step("Select Prev link on Financing page"):
            financing_page.click_prev_link()
            assert_that(select_home_page.is_opened(), "Select Home page isn't opened")
