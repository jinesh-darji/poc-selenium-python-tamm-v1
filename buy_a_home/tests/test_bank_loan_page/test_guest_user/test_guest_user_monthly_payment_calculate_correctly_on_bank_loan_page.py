import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.steps.CalculateMontlyPaymentSteps import CalculateMonthlyPaymentSteps
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from framework.utils.DataReader import DataReader


class TestMonthlyPaymentBank:
    """Bank loan page: Monthly payment calculate correctly: BUAH-1748"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_guest_user_monthly_payment_calculate_correctly_on_bank_loan_page(self):
        with allure.step("Template: Go to Search page (BUAH-1422)"):
            NavigateSteps.go_to_search_page()

        with allure.step("Select random home from Recently added locations"):
            search_home_page = SearchHomePage()
            search_home_page.click_random_result_of_search()

        with allure.step("User clicks to \"Check financing Options\" button"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("User clicks to \"Yes, check bank loan options\""):
            property_details_page.click_check_bank_loan_btn()

        with allure.step("User clicks to \"View Loan Options\" button under \"Loan Calculator\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()
            bank_loan_page = BankLoanPage()

        with allure.step("User clicks on the first Bank option under the Results section"):
            random_bank = bank_loan_page.get_random_data_from_locator(bank_loan_page.list_bank_names)
            # bank_loan_page.click_bank_name(random_bank[0]) # keep it because we have only one bank, keep for future

        with allure.step("Change \"Down payment\" value"):
            down_payment_percentage = bank_loan_page.get_down_payment_percentage_bank()
            bank_loan_page.send_dawn_payment_and_return_data(
                DataReader.get_data("Monthly Payment Calculation.min down payment value"))

        with allure.step("Click to \"Required Documents\""):
            bank_loan_page.click_required_documents_btn()
            assert_that(bank_loan_page.is_required_documents_opened(), "Required documents pop-up isn't opened")

        with allure.step("Close \"Required Documents\" pop-up"):
            bank_loan_page.click_required_documents_close_btn()

        with allure.step("Get new \"Down payment value\""):
            down_payment_percentage_new = bank_loan_page.get_down_payment_percentage_bank()
            assert_that(down_payment_percentage != down_payment_percentage_new, 'Down Payments are equaled')

        with allure.step("Get \"Calculated Loan Amount\" value"):
            calculated_loan_amount = bank_loan_page.get_calculated_loan_amount_value()
            calculated_loan_amount_bank = bank_loan_page.get_bank_loan_amount_price()
            assert_that(calculated_loan_amount == calculated_loan_amount_bank, 'Loan amount values are not equaled')

        with allure.step("Get \"Tenure\" value"):
            tenure_value = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_property)
            tenure_value_bank = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_bank)
            assert_that(tenure_value == tenure_value_bank, 'Tenure data is not equaled')

        with allure.step("Change \"Tenure\" value"):
            bank_loan_page.click_tenure_slider((DataReader.get_data("Monthly Payment Calculation.step for slider")))
            tenure_value_2 = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_property)
            tenure_value_bank_2 = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_bank)
            assert_that(tenure_value_2 == tenure_value_bank_2, 'Tenure data is not equaled')

        with allure.step("Check \"Monthly payment\" value"):
            monthly_payment = CalculateMonthlyPaymentSteps.\
                calculate_monthly_payment_bank_loan_page(calculated_loan_amount)

        with allure.step("Check that calculate data according PMT formula == calculated data on the page"):
            assert_that(monthly_payment[0] == monthly_payment[1], "Calculate data isn't equaled")
