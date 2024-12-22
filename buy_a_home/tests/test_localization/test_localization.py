import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.get_insurance.GetInsurancePage import GetInsurancePage
from buy_a_home.pages.get_utilities.EtisalatPage import EtisalatPage
from buy_a_home.pages.get_utilities.GetUtilitiesPage import GetUtilitiesPage
from buy_a_home.pages.get_utilities.WaterElectricityPage import WaterElectricityPage
from buy_a_home.pages.move_new_home.MoveNewHomePage import MoveNewHomePage
from buy_a_home.pages.select_home.BuildingDetailsPage import BuildingDetailsPage
from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from framework.utils.LocalizationUtil import LocalizationUtil
from framework.utils.SoftAssert import SoftAssert


class TestPropertyDetailsSavedProperties:
    """Test localization"""

    @pytest.mark.localization
    def test_localization(self):
        with allure.step("Change language to Arabic"):
            home_page = HomePage()
            home_page.click_switch_language()

        with allure.step("Check localization on \"Home\" page"):
            home_page.wait_page_to_load()
            self.steps_for_checking_of_localization(home_page)

        with allure.step("Select \"Select Home\" Page"):
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select \"Search\" Button on \"Select Home\" Page"):
            select_home_page = SelectHomePage()

            with allure.step("Check localization on \"Select Home\" page"):
                select_home_page.wait_page_to_load()
                self.steps_for_checking_of_localization(select_home_page)

            select_home_page.click_search_btn()

        with allure.step("Select 'Apply' Button for going to Search results page"):
            search_home_page = SearchHomePage()

            with allure.step("Check localization on Search Home page"):
                search_home_page.wait_page_to_load()
                self.steps_for_checking_of_localization(search_home_page)

            search_home_page.click_apply_btn()

        with allure.step("Select random home in Search results page"):
            WorkWithPropertySteps.refresh_page_if_search_result_is_empty()
            search_results_page = SearchResultsPage()
            price_of_home = search_results_page.get_first_property_details_of_price()
            search_results_page.click_property_detail(price_of_home)

        with allure.step("Check localization on Search Results page"):
            search_results_page.wait_page_to_load()
            self.steps_for_checking_of_localization(search_results_page)

        with allure.step("Select property on Building Details page"):
            building_details_page = BuildingDetailsPage()
            price_of_home = building_details_page.get_random_property_details_of_price()

            with allure.step("Check localization on Building Details page"):
                building_details_page.wait_page_to_load()
                self.steps_for_checking_of_localization(building_details_page)

            building_details_page.click_property_detail(price_of_home)

        with allure.step("Click to \"Check financing options\" button for going to Financing page"):
            property_details = PropertyDetailsPage()

            with allure.step("Check localization on Property Details page"):
                property_details.wait_page_to_load()
                self.steps_for_checking_of_localization(property_details)

            property_details.click_check_financing_option_btn()

        with allure.step("Click to \"Yes, check bank loan options\""):
            property_details.click_check_bank_loan_btn()

        with allure.step("Click to \"View Loan options\" button on Financing page"):
            financing_page = FinancingPage()

            with allure.step("Check localization on Financing page"):
                financing_page.wait_page_to_load()
                self.steps_for_checking_of_localization(financing_page)

            financing_page.click_start_btn()

        with allure.step("Click to \"Tell me about deed transfers\" button on Bank Loan page"):
            bank_loan_page = BankLoanPage()

            with allure.step("Check localization on Bank Loan page"):
                bank_loan_page.wait_page_to_load()
                self.steps_for_checking_of_localization(bank_loan_page)

            bank_loan_page.click_tell_me_about_deed_transfers_btn()

        with allure.step("Click to \"Continue to get utilities\" button on Deed transfer property registration page"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()

            with allure.step("Check localization on Deed Transfer Property Registration page"):
                deed_transfer_property_registration_page.wait_page_to_load()
                self.steps_for_checking_of_localization(deed_transfer_property_registration_page)

            deed_transfer_property_registration_page.click_continue_btn()

        with allure.step("Click to \"View\" button on Get Utilities page"):
            get_utilities_page = GetUtilitiesPage()

            with allure.step("Check localization on Get Utilities page"):
                get_utilities_page.wait_page_to_load()
                self.steps_for_checking_of_localization(get_utilities_page)

            get_utilities_page.click_view_btn_water_and_electricity()

        with allure.step("Click to \"Continue to Etisalat\" button on Water Electricity page"):
            water_electricity_page = WaterElectricityPage()

            with allure.step("Check localization on Water and Electricity page"):
                water_electricity_page.wait_page_to_load()
                self.steps_for_checking_of_localization(water_electricity_page)

            water_electricity_page.click_continue_btn_water_and_electricity()

        with allure.step("Click to \"Load more\" button on Etisalat page"):
            etisalat_page = EtisalatPage()
            etisalat_page.click_to_1st_view_details_button()

            with allure.step("Check localization on Etisalat page"):
                etisalat_page.wait_page_to_load()
                self.steps_for_checking_of_localization(etisalat_page)

        with allure.step("Click to \"Cancel\" button"):
            etisalat_page.click_to_cancel_details_pop_up()

        with allure.step("Go to Home page"):
            etisalat_page.click_buah_breadcrumb()

        with allure.step("Click to \"Get Insurance\""):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_INSURANCE.value)

        with allure.step("Click to \"Find Movers\" button"):
            get_insurance_page = GetInsurancePage()

            with allure.step("Check localization on Get Insurance page"):
                get_insurance_page.wait_page_to_load()
                self.steps_for_checking_of_localization(get_insurance_page)

            get_insurance_page.click_find_movers_btn()

        with allure.step("Click to \"Finish Journey\" button"):
            move_new_home = MoveNewHomePage()

            assert_that(move_new_home.is_finish_journey_btn_present(), "\"Finish journey\" button is absent")

            with allure.step("Check localization on Move New Home page"):
                move_new_home.wait_page_to_load()
                self.steps_for_checking_of_localization(move_new_home)

            move_new_home.click_to_finish_journey_btn()

        SoftAssert.final_assert()

    def steps_for_checking_of_localization(self, page):
        with allure.step("Get text from page"):
            data_text = page.lbl_letters.get_elements_text()

        with allure.step("Check localization"):
            not_matching_words = LocalizationUtil.check_localization(data_text)

        SoftAssert.soft_assert(len(not_matching_words) == 0,
                               "Localization for " + page.page_name + " failed. Following words with localization "
                                                                      "issues found: " + str(not_matching_words))
