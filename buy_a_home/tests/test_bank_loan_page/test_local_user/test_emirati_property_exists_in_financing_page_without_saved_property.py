import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.select_home.PropertyDetailsPage import PropertyDetailsPage
from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, ABU_DHABI_USER_NOT_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps

from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage


class TestFinancingPageWithoutSavedProperty:
    """Local user: property is displayed in chosen home after going to bank loan page without added home to
    saved properties: BUAH-1941"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_emirati_property_exists_in_financing_page_without_saved_property(
                self):
        with allure.step("Template: Go to Search page (BUAH-1422)"):
            LogInAsUserSteps.login_as_user(ABU_DHABI_USER_NOT_VERIFIED)
            NavigateSteps.go_to_select_home_page_local_user()

        with allure.step("Select Search for home"):
            select_home_page = SelectHomePage()
            select_home_page.click_search_btn()

        with allure.step("Select the first home"):
            search_home_page = SearchHomePage()
            data_about_home = search_home_page.get_first_item_from_locator(search_home_page.
                                                                           lst_properties_without_selected_heart)
            search_home_page.click_property_detail(data_about_home[0])

        with allure.step("Click to \"Check financing options\" button"):
            property_details_page = PropertyDetailsPage()
            property_details_page.click_check_financing_option_btn()

        with allure.step("Click to \"Yes, check bank loan options\""):
            property_details_page.click_check_bank_loan_btn()

        with allure.step("Click to \"View Loan Options\" button under \"Loan Calculator\""):
            financing_page = FinancingPage()
            financing_page.click_start_btn()

        with allure.step("Check that selected property displays in Chosen home"):
            bank_loan_page = BankLoanPage()
            bank_loan_page.click_property_details(bank_loan_page.lnk_chosen_home)
            property_details_price = bank_loan_page.get_property_details_price(bank_loan_page.lbl_chosen_home_price)
            assert_that(data_about_home[0] == property_details_price, "Price for selected home and price from property"
                                                                      "details aren't equaled")

        with allure.step("Go to home page"):
            bank_loan_page.click_buah_breadcrumb()

        NavigateSteps.go_to_select_home_page_local_user()

        with allure.step("Select Saved properties button"):
            select_home_page.click_saved_properties_btn()

        with allure.step("Check that your home is present on Save properties page"):
            saved_properties_page = SavedPropertiesPage()
            assert_that(saved_properties_page.is_home_with_specific_price_present(data_about_home[0]),
                        'Home is not present')
