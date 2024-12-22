import pytest
import allure

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
from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from framework.utils.SoftAssert import SoftAssert


class TestAccessibility:
    """Test accessibility: BUAH-1603"""

    @pytest.mark.accessibility
    def test_accessibility(self):
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Search' Button on 'Select Home' Page"):
            select_home_page = SelectHomePage()
            select_home_page.click_search_btn()

        with allure.step("Select 'Apartment' and 'Villa' checkboxes"):
            search_home_page = SearchHomePage()
            search_home_page.chbx_apartment_quick_search.scroll_by_script()
            search_home_page.click_apartment_chbx(search_home_page.chbx_apartment_quick_search)
            search_home_page.click_villa_chbx(search_home_page.chbx_villa_quick_search)

        with allure.step("Select 'Apply' Button for going to Search results page"):
            search_home_page.click_apply_btn()

        with allure.step("Select random home in Search results page"):
            WorkWithPropertySteps.refresh_page_if_search_result_is_empty()
            search_results_page = SearchResultsPage()
            price_of_home = search_results_page.get_random_property_details_of_price()
            search_results_page.click_property_detail(price_of_home)

            WorkWithPropertySteps.set_actions_on_property_or_building_page([[self.navigate_to_pages, []]],
                                                                      [[self.navigate_to_pages, []]])

        SoftAssert.final_assert()

    def navigate_to_pages(self):
        with allure.step("Click to \"Check financing options\" button for going to Financing page"):
            property_details = PropertyDetailsPage()
            property_details.click_check_financing_option_btn()

        with allure.step("Click to \"Yes, check bank loan options\""):
            property_details.click_check_bank_loan_btn()

        with allure.step("Click to \"View Loan options\" button on Financing page"):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        with allure.step("Click to \"Tell me about deed transfers\" button on Bank Loan page"):
            bank_loan_page = BankLoanPage()
            bank_loan_page.click_tell_me_about_deed_transfers_btn()

        with allure.step("Click to \"Continue to get utilities\" button on Deed transfer property registration page"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            deed_transfer_property_registration_page.click_continue_btn()

        with allure.step("Click to \"View\" button on Get Utilities page"):
            get_utilities_page = GetUtilitiesPage()
            get_utilities_page.click_view_btn_water_and_electricity()

        with allure.step("Click to \"Continue to Etisalat\" button on Water Electricity page"):
            water_electricity_page = WaterElectricityPage()
            water_electricity_page.click_continue_btn_water_and_electricity()

        with allure.step("Click to \"Load more\" button on Etisalat page"):
            etisalat_page = EtisalatPage()
            etisalat_page.click_to_1st_view_details_button()

        with allure.step("Click to \"Cancel\" button"):
            etisalat_page.click_to_cancel_details_pop_up()

        with allure.step("Go to Home page"):
            etisalat_page.click_buah_breadcrumb()

        with allure.step("Click to \"Get Insurance\""):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_INSURANCE.value)

        with allure.step("Click to \"Find Movers\" button"):
            get_insurance_page = GetInsurancePage()
            get_insurance_page.click_find_movers_btn()

        with allure.step("Click to \"Finish Journey\" button"):
            move_new_home = MoveNewHomePage()
            move_new_home.click_to_finish_journey_btn()
