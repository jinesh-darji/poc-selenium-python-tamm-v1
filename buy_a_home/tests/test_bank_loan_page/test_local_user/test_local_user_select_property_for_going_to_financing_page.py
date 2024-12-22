import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.financing.BankLoanPage import BankLoanPage
from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, FAKE_USER
from buy_a_home.steps.NavigateSteps import NavigateSteps

from buy_a_home.pages.financing.FinancingPage import FinancingPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage


class TestEmiratiReSelectProperty:
    """Local user: As a logged in user, I can select a property to proceed for Financing options: BUAH-1847"""

    @pytest.mark.smoke
    @pytest.mark.local_user
    def test_local_user_select_property_for_going_to_financing_page(self):
        with allure.step("Template: Go to Search page (BUAH-1422)"):
            LogInAsUserSteps.login_as_user(FAKE_USER)

            NavigateSteps.go_to_select_home_page_local_user()

        with allure.step("Select Search for home"):
            select_home_page = SelectHomePage()
            select_home_page.click_search_btn()

        with allure.step("Click to star for first home in Feature locations module"):
            search_home_page = SearchHomePage()
            search_data = search_home_page.get_data_from_home_with_star(
                search_home_page.get_first_item_from_locator(
                    search_home_page.lst_of_results_quick_search))
            assert_that(search_home_page.is_selected_star_present(search_data[0]),
                        "Star wasn't selected for home")

        with allure.step("Go to home page"):
            search_home_page.click_buah_breadcrumb()

        with allure.step("Select Get Financing"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_FINANCING.value)

        with allure.step("Select \"Yes, check bank loan page\""):
            home_page.click_check_bank_loan_btn()

        with allure.step("Click to \"View loan options\""):
            financing_page = FinancingPage()
            assert_that(financing_page.is_opened(), "Financing page isn't opened")
            financing_page.click_start_btn()

        with allure.step("Select property"):
            saved_properties_page = SavedPropertiesPage()
            saved_properties_page.click_property_detail(search_data[0])

        with allure.step("Check that selected property displays in Chosen home"):
            bank_loan_page = BankLoanPage()
            bank_loan_page.click_property_details(bank_loan_page.lnk_chosen_home)
            property_details_price = bank_loan_page.get_property_details_price(bank_loan_page.lbl_chosen_home_price)
            assert_that(search_data[0] == property_details_price, "Price for selected home and price from property"
                                                                  "details aren't equaled")
