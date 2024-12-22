import numpy as np
from selenium.webdriver.common.keys import Keys

from framework.elements.Label import Label
from framework.elements.Slider import Slider
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.StringUtil import StringUtil


class BasePageFinancingDetails(BasePage):
    page_name = "Base Page Financing Details"
    locator_reader = LocatorReader(page_name)

    lbl_monthly_payment_specific_home = Label(locator_reader, "lbl_monthly_payment_specific_home")
    lbl_home_loan_calculator = Label(locator_reader, 'lbl_home_loan_calculator')

    sld_tenure_slider = Slider(locator_reader, "sld_tenure")

    def get_tenure_years(self, tuner_locator):
        tuner_locator.wait_until_location_stable()
        return float(tuner_locator.get_text())

    def get_interest_rate(self, locator_interest_rate):
        locator_interest_rate.wait_until_location_stable()
        return float(locator_interest_rate.get_value())

    def get_pmt_data_from_loan_calculator(self, interest_rate, tenure_years, price):
        """
        Get monthly payment data according PMT formula
        :param interest_rate: rate of home
        :param tenure_years: credit period
        :param price: price of home
        :return: int: monthly payment of home
        """
        monthly_payment = - np.pmt(interest_rate / 100 / 12, tenure_years * 12, price)
        return monthly_payment

    def get_monthly_payment(self, payment_locator):
        payment_locator.wait_until_location_stable()
        return float(StringUtil.get_text_without_comma(payment_locator.get_text().split(" ")[1]))

    def get_monthly_payment_for_specific_home(self, price):
        """
        Get monthly payment for specific home
        :return: float: monthly payment
        """
        self.lbl_monthly_payment_specific_home.format(price).scroll_by_script()
        return float(StringUtil.get_text_without_comma(self.lbl_monthly_payment_specific_home.format(price).
                                                       get_text().split(" ")[1]))

    def click_home_loan_calculator(self):
        self.lbl_home_loan_calculator.wait_until_location_stable()
        self.scroll_to_element(self.lbl_home_loan_calculator)
        self.lbl_home_loan_calculator.click()

    def click_tenure_slider(self, step):
        self.sld_tenure_slider.click_on_slider(step)

    def send_and_return_interest_rate_and(self, locator_page, interest_rate):
        """
        Method connected with sending new interest rate and returning data
        :return: text: interest rate
        """
        len_interest_rate = len(locator_page.get_value())
        locator_page.wait_until_location_stable()
        locator_page.scroll_by_script()
        locator_page.click()
        locator_page.send_keys(len_interest_rate * Keys.BACKSPACE)
        locator_page.send_keys(str(interest_rate))
        return self.get_interest_rate(locator_page)
