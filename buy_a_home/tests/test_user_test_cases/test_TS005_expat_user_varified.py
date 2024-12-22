import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.deed_transfer.DeedTrasferPage import DeedTransferPage
from buy_a_home.pages.get_insurance.GetInsurancePage import GetInsurancePage
from buy_a_home.pages.get_utilities.EtisalatPage import EtisalatPage
from buy_a_home.pages.get_utilities.GetUtilitiesPage import GetUtilitiesPage
from buy_a_home.pages.get_utilities.WaterElectricityPage import WaterElectricityPage
from buy_a_home.pages.move_new_home.MoveNewHomePage import MoveNewHomePage
from buy_a_home.steps.EtisalatLeadSteps import EtisalatLeadSteps, REFRESH_LEAD_ETISALAT
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, DUBAI_USER_VERIFIED

PRICE_FOR_REGISTERED_PROPERTY = "1,270,806.00"  # Price for registered property


class TestExpatGrant:
    """Logged in "Expat" user.
User is verified in ADM.
Goes to deed transfer to check property registration status.
Checks water and electricity connection steps.
Applies for Etisalat connection.
Checks insurance companies.
Checks movers companies."""

    @pytest.mark.smoke
    @pytest.mark.expat_user
    def test_TS005_expat_user_varified(self):
        EtisalatLeadSteps.refresh_lead_etisalat(REFRESH_LEAD_ETISALAT)
        LogInAsUserSteps.login_as_user(DUBAI_USER_VERIFIED)

        with allure.step("User clicks on \"Deed Transfer\" button"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.DEED_TRANSFER.value)

        with allure.step("User clicks on \"View\" button under \"Property Registration\" step"):
            deed_transfer_page = DeedTransferPage()
            deed_transfer_page.click_view_btn()

        with allure.step("Select \"Select\" button for register property"):
            deed_transfer_page.click_property_detail_with_selected_star(PRICE_FOR_REGISTERED_PROPERTY)

        with allure.step("Click on \"Continue\" button"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            deed_transfer_property_registration_page.click_continue_btn()

        with allure.step("User clicks on \"View\" button under water and electricity"):
            get_utilities_page = GetUtilitiesPage()
            assert_that(get_utilities_page.is_apply_btn_present(), "Apply button isn't present")
            get_utilities_page.click_view_btn_water_and_electricity()

        with allure.step("User clicks on Continue button"):
            water_electricity_page = WaterElectricityPage()
            water_electricity_page.click_continue_btn_water_and_electricity()
        #
        # with allure.step("Select \"Select\" button for register property"):
        #     deed_transfer_page.click_property_detail_with_selected_star(PRICE_FOR_REGISTERED_PROPERTY)

        with allure.step("User clicks randomly on \"View Details\" button of one of the Etisalat package cards"):
            etisalat_page = EtisalatPage()
            etisalat_page.click_to_1st_view_details_button()

        with allure.step("User clicks on \"Cancel\" button"):
            etisalat_page.click_to_cancel_details_pop_up()

        with allure.step("User clicks to \"Request\" button"):
            etisalat_page.click_to_1st_request_button()

        with allure.step("User clicks to \"Submit\" button"):
            etisalat_page.click_submit_btn()

        with allure.step("User clicks to \"Ok\" button"):
            etisalat_page.click_ok_btn()

        with allure.step("Click on \"Get Insurance\""):
            home_page = HomePage()
            assert_that(home_page.is_select_home_step_present(), "Select home button isn't present")
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_INSURANCE.value)

        with allure.step("User clicks on \"Find Movers\" button"):
            get_insurance_page = GetInsurancePage()
            get_insurance_page.click_find_movers_btn()

        with allure.step("User clicks on \"Finish Journey\" button"):
            move_new_home = MoveNewHomePage()
            move_new_home.click_to_finish_journey_btn()
            assert_that(home_page.is_select_home_step_present(), "\"Select Home\" step is not present")