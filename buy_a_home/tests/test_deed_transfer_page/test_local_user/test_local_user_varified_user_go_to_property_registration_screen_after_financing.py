import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.steps.WorkWithPropertySteps import WorkWithPropertySteps
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, ABU_DHABI_USER_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.steps.RemoveSavedPropertySteps import RemoveSavedPropertySteps


class TestPropertyBankLoanPage:
    """If user has landed on Deed Transfer process page immediately after get financing then user doesn't go to
    Property Registration screen: BUAH-1930"""

    @pytest.mark.smoke
    def test_local_user_verified_user_go_to_property_registration_screen_after_financing(self):
        LogInAsUserSteps.login_as_user(ABU_DHABI_USER_VERIFIED)

        home_page = HomePage()
        RemoveSavedPropertySteps.remove_save_properties_local_user(home_page)

        NavigateSteps.go_to_search_page_local_user()

        search_home_page = SearchHomePage()
        search_data = search_home_page.get_data_from_home_with_star(
            search_home_page.get_random_data_about_home_from_locator(search_home_page.
                                                                     lst_of_results_price_with_enabled_stars,
                                                                     True, search_home_page))
        assert_that(search_home_page.is_selected_star_present(search_data[0]), "Star wasn't selected for home")
        with allure.step("Select home with selected star"):
            search_home_page.click_property_detail_with_selected_star(search_data[0])

        with allure.step("Select \"Check financing options\""):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("Select \"Yes, check bank loan page\""):
            property_details_page.click_check_bank_loan_btn()

        with allure.step("Click to \"View loan options\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        bank_loan_page = BankLoanPage()
        WorkWithPropertySteps.check_selected_property_in_chosen_home(bank_loan_page, search_data[0])

        with allure.step("Select \"Tell me about deed transfers\" button"):
            bank_loan_page.click_tell_me_about_deed_transfers_btn()

        deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
        WorkWithPropertySteps.check_selected_property_in_chosen_home(deed_transfer_property_registration_page,
                                                                     search_data[0])
