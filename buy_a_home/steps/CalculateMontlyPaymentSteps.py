import allure

from buy_a_home.pages.financing.BankLoanPage import BankLoanPage


class CalculateMonthlyPaymentSteps:
    """Calculate Monthly Payment methods"""

    @staticmethod
    def calculate_monthly_payment_with_formula(page_locator, interest_rate_locator, tenure_years, price_home):
        """
        Method connected with calculate monthly payment and compare data form gape and formula
        :param page_locator: Locator of page with Monthly payment
        :param interest_rate_locator: interest rate
        :param tenure_years: tenure years
        :param price_home: price
        """
        result_of_pmt_formula = round(page_locator.
                                      get_pmt_data_from_loan_calculator(interest_rate_locator, tenure_years,
                                                                        int(price_home)), 2)
        return result_of_pmt_formula

    @staticmethod
    def calculate_monthly_payment_bank_loan_page(loan_amount_bank):
        """
        Method connected with calculate monthly payment and compare data form gape and formula on Bank Loan page
        :param loan_amount_bank: loan amount price
        """
        with allure.step("Calculate monthly payment with formula according data from Bank Loan page"):
            bank_loan_page = BankLoanPage()
            interest_rate_bank = bank_loan_page.get_interest_rate_bank()
            tenure_years_bank = bank_loan_page.get_tenure_years(bank_loan_page.lbl_tenure_years_bank)

        with allure.step("Get monthly payment from page"):
            monthly_payment = bank_loan_page.get_monthly_payment(bank_loan_page.lbl_monthly_payment_financing)

            pmt_formula = CalculateMonthlyPaymentSteps.calculate_monthly_payment_with_formula(bank_loan_page,
                                                                                              interest_rate_bank,
                                                                                              tenure_years_bank,
                                                                                              loan_amount_bank)

        with allure.step("Create list with monthly payment from page and payment from PMT formula"):
            list_payment = [monthly_payment, pmt_formula]

        return list_payment
