import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from framework.utils.StringUtil import StringUtil


class TestFeesPayment:
    """Not verified user: Property registration page: 2 Fee Payment step: payment = 1% of price for selected home:
    BUAH-2446"""

    @pytest.mark.skip("Fee is unavailable for current version of app")
    @pytest.mark.smoke
    def test_local_not_verified_user_fees_payment(self):
        with allure.step("Login as Local and not verified user"):
            LogInAsUserSteps.login_as_user(FAKE_USER)

        NavigateSteps.go_to_search_page_local_user()

        search_home_page = SearchHomePage()
        search_data = search_home_page.get_data_from_home_with_star(search_home_page.get_first_item_from_locator(
            search_home_page.lst_of_results_quick_search))
        assert_that(search_home_page.is_selected_star_present(search_data[0]), "Star wasn't selected for home")

        with allure.step("Select property with selected heart"):
            search_home_page.click_property_detail(search_data[0])

        with allure.step("Select Check Financing options"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("Select \"Yes, check bank loan page\""):
            property_details_page.click_check_bank_loan_btn()

        with allure.step("Click to \"View loan options\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        with allure.step("Click to \"Tell me about...\""):
            bank_loan_page = BankLoanPage()
            bank_loan_page.click_tell_me_about_deed_transfers_btn()

        with allure.step("Close Registration pop up"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            deed_transfer_property_registration_page.click_close_registration_pop_up_btn()

        with allure.step("Get fee payment"):
            fee_payment = deed_transfer_property_registration_page.get_fee_payment()

        with allure.step("Check that fee payment = 1% from price of selected home"):
            self.check_fee_payment(fee_payment, search_data[0])

    def check_fee_payment(self, fee_payment, price_of_home):
        assert_that(float(fee_payment) == int(StringUtil.get_text_without_comma(price_of_home)) / 100 * 1,
                    "Fee payment does not equal 1% of price for selected home")