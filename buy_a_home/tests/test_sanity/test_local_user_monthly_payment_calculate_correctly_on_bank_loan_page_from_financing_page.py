import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.steps.CalculateMontlyPaymentSteps import CalculateMonthlyPaymentSteps
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from framework.utils.DataReader import DataReader
from framework.utils.StringUtil import StringUtil


class TestMonthlyPaymentBank:
    """Bank loan page: Monthly payment calculate correctly: BUAH-1977"""

    @pytest.mark.regression
    def test_local_user_monthly_payment_calculate_correctly_on_bank_loan_page_from_financing_page(self):
        with allure.step("Template: Go to Search page (BUAH-1422)"):
            LogInAsUserSteps.login_as_user(FAKE_USER)

            NavigateSteps.go_to_search_page_local_user()

        with allure.step("Select random home from Recently added locations"):
            search_home_page = SearchHomePage()
            search_data = search_home_page.get_data_from_selected_home()
            price_of_home = StringUtil.get_text_without_letters(search_data[0])

        with allure.step("Add to Saved properties selected home"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_star_property(price_of_home)

        with allure.step("Go to home page"):
            property_details_page.click_go_back_breadcrumb()
            home_page = HomePage()
            home_page.click_buah_breadcrumb()

        with allure.step("Click Financing icon"):
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_FINANCING.value)

        with allure.step("User clicks on \"Yes, check bank loan options\""):
            home_page.click_check_bank_loan_btn()

        with allure.step("User clicks on \"View Loan Options\" button under \"Loan Calculator\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        with allure.step("User clicks to Select property with price from previous step"):
            financing_page.click_property_detail(price_of_home)

        with allure.step("User check price from \"Chosen home\" with other price fields"):
            bank_loan_page = BankLoanPage()
            bank_loan_page.click_property_details(bank_loan_page.lnk_chosen_home)
            property_details_price = bank_loan_page.get_property_details_price(bank_loan_page.
                                                                               lbl_chosen_home_price)
            assert_that(price_of_home == property_details_price, "Price for selected home and price from property "
                                                                 "details aren't equaled")

        with allure.step("User clicks on the first Bank option under the Results section"):
            random_bank = bank_loan_page.get_random_data_from_locator(bank_loan_page.list_bank_names)
            # bank_loan_page.click_bank_name(random_bank[0]) # keep it because we have only one bank,keep for future

            with allure.step("Change \"Down payment\" value"):
                down_payment_percentage = bank_loan_page.get_down_payment_percentage_bank()
                down_payment_value = bank_loan_page.send_dawn_payment_and_return_data(
                    DataReader.get_data("Monthly Payment Calculation.down payment value"))

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

            with allure.step("Get new \"Down payment\" value"):
                down_payment_value_new = bank_loan_page.get_property_down_payment_value()
                assert_that(down_payment_value != down_payment_value_new, 'Values are equaled')

            with allure.step("Check that price of home is equal Down Payment Value plus Calculated Loan Amount"):
                assert_that(float(StringUtil.get_text_without_comma(property_details_price)) ==
                            (float(down_payment_value_new) + calculated_loan_amount))

            with allure.step("Get \"Tenure\" value"):
                tenure_value = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_property)
                tenure_value_bank = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_bank)
                assert_that(tenure_value == tenure_value_bank, 'Tenure data is not equaled')

            with allure.step("Change \"Tenure\" value"):
                bank_loan_page.click_tenure_slider(DataReader.
                                                   get_data("Monthly Payment Calculation.step for slider"))
                tenure_value_2 = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_property)
                tenure_value_bank_2 = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_bank)
                assert_that(tenure_value_2 == tenure_value_bank_2, 'Tenure data is not equaled')

            with allure.step("Check \"Monthly payment\" value"):
                monthly_payment = CalculateMonthlyPaymentSteps.calculate_monthly_payment_bank_loan_page \
                    (calculated_loan_amount)
                assert_that(monthly_payment[0] == monthly_payment[1], "Calculate data isn't equaled")
