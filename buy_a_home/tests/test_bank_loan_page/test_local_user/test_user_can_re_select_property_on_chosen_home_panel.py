import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SearchResultsPage import SearchResultsPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps

from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage


class TestEmiratiCanReSelectProperty:
    """Local user can re-select property on chosen home panel: BUAH-2480"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_user_can_re_select_property_on_chosen_home_panel(self):
        with allure.step("Template: Go to Search page (BUAH-1422)"):
            LogInAsUserSteps.login_as_user(FAKE_USER)
            NavigateSteps.go_to_select_home_page_local_user()

        with allure.step("Select Search for home"):
            select_home_page = SelectHomePage()
            select_home_page.click_search_btn()

        with allure.step("Click to star for random home in Feature locations module"):
            search_home_page = SearchHomePage()
            search_data = search_home_page.get_data_from_home_with_star(
                search_home_page.get_first_item_from_locator(
                    search_home_page.lst_of_results_quick_search))
            assert_that(search_home_page.is_selected_star_present(search_data[0]),
                        "Star wasn't selected for home")

        NavigateSteps.go_to_search_results_page_with_villa_chbx()

        with allure.step("Select to star for the first home in Search results page"):
            search_results_page = SearchResultsPage()
            search_results_page.wait_page_to_load()
            search_data_2 = search_results_page.click_and_return_data_for_home_with_selected_star(
                search_results_page.get_first_item_from_locator(
                    search_results_page.lst_of_results_price_with_stars))

            self.go_to_bank_loan_page()

            self.check_selected_property_in_chosen_home(search_data_2[0])

        with allure.step("Click to chosen home button"):
            bank_loan_page = BankLoanPage()
            bank_loan_page.click_choose_property_button()

        with allure.step("Select other property"):
            saved_properties_page = SavedPropertiesPage()
            saved_properties_page.click_random_property_with_selected_heart_without_specific_price(search_data_2[0])

            self.go_to_bank_loan_page()

            self.check_selected_property_in_chosen_home(search_data[0])

    def go_to_bank_loan_page(self):
        with allure.step("Click to \"Check financing options\" button"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("Click to \"Yes, check bank loan options\""):
            property_details_page.click_check_bank_loan_btn()

        with allure.step("Click to \"View Loan option\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

    def check_selected_property_in_chosen_home(self, price):
        with allure.step("Check that selected property displays in Chosen home"):
            bank_loan_page = BankLoanPage()
            bank_loan_page.click_property_details(bank_loan_page.lnk_chosen_home)
            property_details_price = bank_loan_page.get_property_details_price(bank_loan_page.lbl_chosen_home_price)
            assert_that(price == property_details_price, "Price for selected home and price from property"
                                                         "details aren't equaled")
