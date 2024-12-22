from selenium.webdriver.common.keys import Keys

from buy_a_home.pages.base_page_journey_methods.BasePageFinancingDetails import BasePageFinancingDetails
from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from buy_a_home.pages.base_page_journey_methods.BasePagePropertyDetails import BasePagePropertyDetails
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.List import List
from framework.utils.LocatorReader import LocatorReader
from framework.utils.StringUtil import StringUtil


class BankLoanPage(BasePageJourney, BasePageFinancingDetails, BasePageHeader, BasePagePropertyDetails):
    page_name = "Bank Loan Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_bank_loan")

    lbl_property_type = Label(locator_reader, "lbl_property_type")
    lbl_property_size = Label(locator_reader, "lbl_property_size")
    lbl_property_rooms = Label(locator_reader, "lbl_property_rooms")
    lbl_property_bathrooms = Label(locator_reader, "lbl_property_bathrooms")
    lbl_down_payment_value = Label(locator_reader, "lbl_down_payment_value")
    lbl_calculated_loan_amount = Label(locator_reader, "lbl_calculated_loan_amount")
    lbl_bank_loan_amount = Label(locator_reader, "lbl_bank_loan_amount")
    lbl_interest_rate_bank = Label(locator_reader, "lbl_interest_rate")
    lbl_down_payment_percentage = Label(locator_reader, "lbl_down_payment_percentage")
    lbl_tenure_years_bank = Label(locator_reader, "lbl_tenure_years_bank")
    lbl_tenure_years_property = Label(locator_reader, "lbl_tenure_years_property")
    lbl_monthly_payment_bank = Label(locator_reader, "lbl_monthly_payment_bank")
    lbl_pop_up_required_documents = Label(locator_reader, "lbl_pop_up_required_documents")
    lbl_bank_item = Label(locator_reader, "lbl_bank_item")

    list_bank_names = List(locator_reader, "list_bank_names")

    btn_required_documents = Button(locator_reader, "btn_required_documents")
    btn_required_documents_close = Button(locator_reader, "btn_required_documents_close")
    btn_tell_me = Button(locator_reader, "btn_tell_me")

    def __init__(self):
        super(BankLoanPage, self).__init__(self.page_element)

    def is_required_documents_opened(self):
        self.lbl_pop_up_required_documents.wait_until_location_stable()
        return self.lbl_pop_up_required_documents.is_present()

    def click_bank_name(self, bank_name):
        self.lbl_bank_item.format(bank_name)
        self.lbl_bank_item.format(bank_name).click()

    def click_required_documents_btn(self):
        self.btn_required_documents.wait_until_location_stable()
        self.btn_required_documents.click()

    def click_required_documents_close_btn(self):
        self.btn_required_documents_close.wait_until_location_stable()
        self.btn_required_documents_close.click()

    def click_tell_me_about_deed_transfers_btn(self):
        self.btn_tell_me.wait_until_location_stable()
        self.btn_tell_me.click()

    def get_bank_loan_amount_price(self):
        # [1] is temporary solution until developers didn't add class names
        bank_loan_amount = self.lbl_bank_loan_amount.get_elements()[1].text
        return float(StringUtil.get_text_without_comma(bank_loan_amount))

    def get_calculated_loan_amount_value(self):
        self.lbl_calculated_loan_amount.wait_until_location_stable()
        calculated_loan_amount = self.lbl_calculated_loan_amount.get_text()
        return float(StringUtil.get_text_without_comma(calculated_loan_amount))

    def get_property_down_payment_value(self):
        self.lbl_down_payment_value.wait_until_location_stable()
        return self.lbl_down_payment_value.get_attribute("value")

    def get_interest_rate_bank(self):
        self.lbl_interest_rate_bank.wait_until_location_stable()
        interest_rate = self.lbl_interest_rate_bank.get_text()
        return float(interest_rate.replace('%', ''))

    def get_down_payment_percentage_bank(self):
        self.lbl_down_payment_percentage.wait_until_location_stable()
        down_payment_percentage = self.lbl_down_payment_percentage.get_text()
        return float(down_payment_percentage)

    def send_dawn_payment_and_return_data(self, price_increase):
        """
        Send new down payment value and returning data
        :return: int: down payment value
        """
        len_down_payment = len(self.lbl_down_payment_value.get_value())
        down_payment = self.lbl_down_payment_value.get_value()
        self.lbl_down_payment_value.wait_until_location_stable()
        self.lbl_down_payment_value.click()
        self.lbl_down_payment_value.send_keys(len_down_payment * Keys.BACKSPACE)
        new_down_payment = int(down_payment) + price_increase
        self.lbl_down_payment_value.send_keys(str(new_down_payment))
        return self.get_property_down_payment_value()
