import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, DUBAI_USER_NOT_VERIFIED
from buy_a_home.steps.RemoveSavedPropertySteps import RemoveSavedPropertySteps


class TestExpatReSelectProperty:
    """Expat user: As a user, on entry to the financing Sub-journey, if I don't have any saved properties I am
    prompted to select a home: BUAH-1942"""

    @pytest.mark.smoke
    @pytest.mark.expat_user
    def test_expat_user_need_to_search_home_for_financing_page_if_0_for_saved_properties(self):
        with allure.step("Template: Go to Search page (BUAH-1422)"):
            LogInAsUserSteps.login_as_user(DUBAI_USER_NOT_VERIFIED)

        home_page = HomePage()
        RemoveSavedPropertySteps.remove_save_properties_expat_user(home_page)

        with allure.step("Select Get Financing"):
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_FINANCING.value)

        with allure.step("Select \"Yes, check bank loan page\""):
            home_page.click_check_bank_loan_btn()

        with allure.step("Click to \"View loan options\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        with allure.step("Click to \"Search a home\" button"):
            saved_properties_page = SavedPropertiesPage()
            saved_properties_page.click_search_home_btn()

        with allure.step("Click to star for 1st home in Feature locations module"):
            search_home_page = SearchHomePage()
            search_data = search_home_page.get_data_from_home_with_star(
                search_home_page.get_first_item_from_locator(
                    search_home_page.lst_of_results_quick_search))
            assert_that(search_home_page.is_selected_star_present(search_data[0]),
                        "Star wasn't selected for home")
            search_home_page.click_property_detail(search_data[0])

        with allure.step("Click to \"Check financing options\" button"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("User clicks to \"Yes, check bank loan options\""):
            property_details_page.click_check_bank_loan_btn()

        with allure.step("User clicks to \"View Loan option\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        with allure.step("Check that selected property displays in Chosen home"):
            bank_loan_page = BankLoanPage()
            bank_loan_page.click_property_details(bank_loan_page.lnk_chosen_home)
            property_details_price = bank_loan_page.get_property_details_price(bank_loan_page.lbl_chosen_home_price)
            assert_that(search_data[0] == property_details_price, "Price for selected home and price from property"
                                                                  "details aren't equaled")
