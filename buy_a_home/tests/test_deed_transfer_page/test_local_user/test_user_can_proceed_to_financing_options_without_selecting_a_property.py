import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps


class TestFinancingPageWithProperty:
    """User can go to property registration form: BUAH-1853, BUAH-1933"""

    @pytest.mark.smoke
    @pytest.mark.guest_user
    def test_user_can_proceed_to_financing_options_with_selected_property(self):
        LogInAsUserSteps.login_as_user(FAKE_USER)

        NavigateSteps.go_to_search_page_local_user()

        search_home_page = SearchHomePage()
        search_data = search_home_page.get_data_from_home_with_star(search_home_page.get_first_item_from_locator(
            search_home_page.lst_of_results_quick_search))
        assert_that(search_home_page.is_selected_star_present(search_data[0]), "Star wasn't selected for home")

        with allure.step("Click to \"Home\" breadcrumb"):
            search_home_page.click_buah_breadcrumb()

        with allure.step("Go to \"Financing page\""):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_FINANCING.value)

        with allure.step("Select \"Yes, check bank loan page\""):
            home_page.click_check_bank_loan_btn()

        with allure.step("Click to \"View loan options\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        with allure.step("User clicks to Select property with price from previous step"):
            financing_page.click_property_detail(search_data[0])

        with allure.step("Bank Loan page is opened"):
            bank_loan_page = BankLoanPage()
            assert_that(not_(bank_loan_page.is_chosen_home_present()),
                        "\"Chosen home\" is present")
