import pytest
import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.deed_transfer.DeedTransferPropertyRegistrationPage import DeedTransferPropertyRegistrationPage
from buy_a_home.pages.deed_transfer.DeedTrasferPage import DeedTransferPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.steps.LogInAsUserSteps import LogInAsUserSteps, ABU_DHABI_USER_VERIFIED
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.steps.RemoveSavedPropertySteps import RemoveSavedPropertySteps


class TestPropertyBankLoanPage:
    """Deed transfer page: Clicking on Select button will take user to Property Registration screen for this
    particular selected property: BUAH-1932"""

    @pytest.mark.smoke
    def test_local_user_can_see_selected_property_on_bank_loan_page(self):
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

        with allure.step("Click to \"BUAH\" breadcrumbs"):
            search_home_page.click_buah_breadcrumb()

        with allure.step("Select Deed transfer page"):
            home_page.click_navigation_panel_btn(NavigationHomeItems.DEED_TRANSFER.value)

        with allure.step("Select View button for the 1st step"):
            deed_transfer_page = DeedTransferPage()
            deed_transfer_page.click_view_btn()

        with allure.step("Select \"Select\" button for home which was added so save property from previous steps"):
            deed_transfer_page.click_property_detail_with_selected_star(search_data[0])

        with allure.step("Check that selected property displays in Chosen home"):
            deed_transfer_property_registration_page = DeedTransferPropertyRegistrationPage()
            deed_transfer_property_registration_page.click_property_details \
                (deed_transfer_property_registration_page.lnk_chosen_home)
            property_details_price = deed_transfer_property_registration_page.get_property_details_price \
                (deed_transfer_property_registration_page.lbl_chosen_home_price)
            assert_that(search_data[0] == property_details_price, "Price for selected home and price from property "
                                                                  "details aren't equaled")
