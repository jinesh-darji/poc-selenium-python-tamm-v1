import allure
from hamcrest import assert_that, not_

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
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.steps.CalculateMontlyPaymentSteps import CalculateMonthlyPaymentSteps
from buy_a_home.steps.EtisalatLeadSteps import EtisalatLeadSteps, REFRESH_LEAD_ETISALAT
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, ABU_DHABI_USER_NOT_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.steps.RemoveSavedPropertySteps import RemoveSavedPropertySteps
from buy_a_home.steps.WorkOnFilterFormSteps import WorkOnFilterFormSteps

from framework.elements.Dropdown import Dropdown
from framework.utils.DataReader import DataReader
from framework.utils.StringUtil import StringUtil

PRICE_FOR_REGISTERED_PROPERTY = "1,270,806.00"  # Price for registered property
MIN_ROOM = "2"
MAX_ROOM = "8"


class TestEmiratiAbuDhabiNotVarified:
    """Logged in "Emirati" user from Abu Dhabi.
User is not verified in ADM.
User searches and selects a home.
Checks financing products and required documents.
Checks property registration information.
Checks water and electricity connection steps.
Checks Etisalat connection.
Checks insurance companies.
Checks movers companies."""

    def test_TS002_emirati_Abu_Dhabi_not_varified(self):

        EtisalatLeadSteps.refresh_lead_etisalat(REFRESH_LEAD_ETISALAT)
        LogInAsUserSteps.login_as_user(ABU_DHABI_USER_NOT_VERIFIED)
        home_page = HomePage()
        RemoveSavedPropertySteps.remove_save_properties_local_user(home_page)

        with allure.step("Open \"Buy a Home\" journey homepage, Click on \"Select Home\" button and User clicks"
                         " on \"Search for Home\" button under \"Search for Home\" step 1"):
            NavigateSteps.go_to_search_page_local_user()

        with allure.step("User clicks on filter icon"):
            search_home_page = SearchHomePage()
            search_home_page.click_filter_icon()

        with allure.step("Select Apartment checkbox"):
            filter_form = FilterForm()
            filter_form.chbx_apartment_filter_enable.scroll_by_script()
            search_home_page.click_apartment_chbx(filter_form.chbx_apartment_filter_enable)
            assert_that(filter_form.chbx_apartment_filter_disable.is_present(),
                        "Checkbox Apartment isn't selected")

        with allure.step("Selects price range"):
            print()

        with allure.step("Select min and max for rooms"):
            self.get_items_dropdown()

        with allure.step("Click on Apply button"):
            filter_form = FilterForm()
            filter_form.click_apply_btn_filter()

        with allure.step("Select random home in Search results page"):
            bedrooms_list_2 = WorkOnFilterFormSteps.get_search_criteria_if_result_is_empty([self.get_items_dropdown, []])

        with allure.step("User clicks on the save icon on one of the property cards"):
            search_results_page = SearchResultsPage()
            price_of_home = search_results_page.get_first_property_details_of_price()
            search_results_page.click_property_detail(StringUtil.get_text_without_letters(price_of_home))
            price_for_star = search_results_page.get_the_first_home_with_price()
            building_details_page = BuildingDetailsPage()
            building_details_page.click_star(price_for_star)

        with allure.step("Select random home in Search results page"):
            search_results_page.click_property_detail(price_for_star)
            search_results_page.wait_page_to_load()

        with allure.step("Check that property details page was opened or building details page was opened"):
            WorkWithPropertySteps.set_actions_on_property_or_building_page(
                [[self.other_steps_with_home, []]],
                [[self.other_steps_with_home, []]])

    def other_steps_with_home(self):
        with allure.step("User clicks on Services button on screen"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_services_btn()

            with allure.step("Deselect all services"):
                property_details_page.click_services_all_checkbx()

        with allure.step("Select randomly 2 nearby services"):
            list_of_services = property_details_page.get_services(DataReader.get_data("Qty of items.qty of services"))
            property_details_page.click_random_checkboxes(property_details_page.chbx_of_service,
                                                          list_of_services)
        with allure.step("User closes Services pop-up screen"):
            property_details_page.click_services_close_btn()

        with allure.step("User clicks on \"Check financing Options\" button"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("User clicks on \"Yes, check bank loan options\""):
            property_details_page.click_check_bank_loan_btn()

        with allure.step("User clicks on \"View Loan Options\" button under \"Loan Calculator\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        with allure.step("User clicks on the first Bank option under the Results section"):
            bank_loan_page = BankLoanPage()
            random_bank = bank_loan_page.get_random_data_from_locator(bank_loan_page.list_bank_names)
            # bank_loan_page.click_bank_name(random_bank[0]) # now opened because we have only one bank,keep for feature

        with allure.step("Change \"Down payment\" value"):
            down_payment_percentage = bank_loan_page.get_down_payment_percentage_bank()
            down_payment_value = bank_loan_page.send_dawn_payment_and_return_data(
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
            monthly_payment = CalculateMonthlyPaymentSteps.calculate_monthly_payment_bank_loan_page(calculated_loan_amount)
            self.compare_mounthly_payment_and_data_from_PMT_formula(monthly_payment[0], monthly_payment[1])

        with allure.step("User clicks on \"Tell Me About Deed Transfer\" button"):
            bank_loan_page.click_tell_me_about_deed_transfers_btn()

        self.check_adm_registration()

        with allure.step("User scrolls down and check the Property Registration steps"):
            print()

        with allure.step("Click on \"Continue\" button"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            deed_transfer_property_registration_page.click_continue_btn()

        with allure.step("User clicks on \"View\" button under water and electricity"):
            get_utilities_page = GetUtilitiesPage()
            get_utilities_page.click_view_btn_water_and_electricity()

        with allure.step("40. User can check the steps for applying for water and electricity"):
            print()

        with allure.step("User clicks on Continue button"):
            water_electricity_page = WaterElectricityPage()
            water_electricity_page.click_continue_btn_water_and_electricity()

        with allure.step("User clicks randomly on \"View Details\" button of one of the Etisalat package cards"):
            etisalat_page = EtisalatPage()
            etisalat_page.click_to_1st_view_details_button()

        with allure.step("User clicks on \"Cancel\" button"):
            etisalat_page.click_to_cancel_details_pop_up()

        with allure.step("User clicks on \"Request\" button"):
            etisalat_page.click_to_1st_request_button()

        with allure.step("Check pop-up message"):
            assert_that(etisalat_page.is_error_message_packages_present(), "Message about registered property is "
                                                                           "absent")

        with allure.step("Click to Ok button in pop-up"):
            etisalat_page.click_to_ok_btn_in_error_pop_up()

        with allure.step("Navigate to \"Buy a Home\" journey homepage"):
            self.go_to_home_page()

        with allure.step("47. Click on \"Get Insurance\""):
            home_page = HomePage()
            assert_that(home_page.is_select_home_step_present(), "Select home button isn't present")
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_INSURANCE.value)

        with allure.step("User clicks on \"Find Movers\" button"):
            get_insurance_page = GetInsurancePage()
            get_insurance_page.click_find_movers_btn()

        with allure.step("User clicks on \"Finish Journey\" button"):
            move_new_home = MoveNewHomePage()
            move_new_home.click_to_finish_journey_btn()
            assert_that(home_page.is_select_home_step_present())

    def go_to_home_page(self):
        """
        Method connected with going to Home page
        """
        with allure.step("Navigate to \"Buy a Home\" journey homepage"):
            search_home_page = SearchHomePage()
            search_home_page.click_buah_breadcrumb()

    def get_items_dropdown(self):
        """
        Method connected with getting min and max value from drop-down
        :return:
        """
        filter_form = FilterForm()
        filter_form.click_show_amenities_lnk()
        bedrooms_list = \
            [Dropdown.get_specific_item_from_dropdown(
                filter_form.drpdwn_min_bedrooms_filter_form,
                filter_form.lbl_minBedrooms_item_dropdown_filter,
                MIN_ROOM)]
        return bedrooms_list

    def compare_mounthly_payment_and_data_from_PMT_formula(self, monthly_payment, result_of_pmt_formula):
        with allure.step("Check that calculate data according PMT formula == calculated data on the page"):
            assert_that(monthly_payment == result_of_pmt_formula, "Calculate data isn't equaled")

    def check_adm_registration(self):
        deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
        if deed_transfer_property_registration_page.is_in_progress_message_present():
            pass
        else:
            with allure.step("Select \"Yes\" button on ADM registration pop up"):
                deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
                deed_transfer_property_registration_page.click_yes_registration_pop_up_btn()

            with allure.step("Check that Success pop up is present"):
                assert_that(deed_transfer_property_registration_page.is_success_pop_up_present(),
                            'Success pop up isn\'t present')

            with allure.step("Select OK button"):
                deed_transfer_property_registration_page.click_ok_btn_on_success_pop_up()
                assert_that(not_(deed_transfer_property_registration_page.is_success_pop_up_present()),
                            'Success pop up is present')

            with allure.step("Check that in progress message is present"):
                assert_that(deed_transfer_property_registration_page.is_in_progress_message_present(),
                            'Message isn\'t present')
