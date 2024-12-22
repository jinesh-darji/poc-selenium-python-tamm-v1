import allure
from hamcrest import assert_that

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage


class NavigateSteps:
    """Navigate methods"""

    @staticmethod
    def go_to_select_home_page():
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

    @staticmethod
    def go_to_select_home_page_local_user():
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Buy a home' button"):
            home_page.click_buy_home_btn()

    @staticmethod
    def go_to_search_page():
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Search' Button on 'Select Home' Page"):
            select_home_page = SelectHomePage()
            select_home_page.click_search_btn()

        with allure.step("Check that 'Apply' Button is displayed on 'Search Home' page"):
            search_home_page = SearchHomePage()
            assert_that(search_home_page.is_apply_button_present(), "Apply button is not displayed")

    @staticmethod
    def go_to_search_page_local_user():
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Buy a home' button"):
            home_page.click_buy_home_btn()

        with allure.step("Select 'Search' Button on 'Select Home' Page"):
            select_home_page = SelectHomePage()
            select_home_page.click_search_btn()

        with allure.step("Check that 'Apply' Button is displayed on 'Search Home' page"):
            search_home_page = SearchHomePage()
            assert_that(search_home_page.is_apply_button_present(), "Apply button is not displayed")

    @staticmethod
    def go_to_home_grant_page_local_user():
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Apply for ready home grant' button"):
            home_page.click_apply_for_ready_nome_grant_btn()

    @staticmethod
    def go_to_search_results_page():
        with allure.step("Select 'Apartment' and 'Villa' checkboxes"):
            search_home_page = SearchHomePage()
            search_home_page.scroll_to_top()
            search_home_page.click_apartment_chbx(search_home_page.chbx_apartment_quick_search)
            search_home_page.click_villa_chbx(search_home_page.chbx_villa_quick_search)

        with allure.step("Select 'Apply' Button for going to Search results page"):
            search_home_page.click_apply_btn()

    @staticmethod
    def go_to_search_results_page_with_villa_chbx():
        with allure.step("Select 'Villa' checkbox"):
            search_home_page = SearchHomePage()
            search_home_page.scroll_to_top()
            search_home_page.click_villa_chbx(search_home_page.chbx_villa_quick_search)

        with allure.step("Select 'Apply' Button for going to Search results page"):
            search_home_page.click_apply_btn()

    @staticmethod
    def go_to_saved_properties_page():
        with allure.step("Go to Home Page"):
            search_home_page = SearchHomePage()
            search_home_page.click_buah_breadcrumb()

        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Saved properties' Button on 'Select Home' Page"):
            select_home_page = SelectHomePage()
            select_home_page.click_saved_properties_btn()

    @staticmethod
    def go_to_saved_properties_page_local_user():
        with allure.step("Go to Home Page"):
            search_home_page = SearchHomePage()
            search_home_page.click_buah_breadcrumb()

        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Buy a home' button"):
            home_page.click_buy_home_btn()

        with allure.step("Select 'Saved properties' Button on 'Select Home' Page"):
            select_home_page = SelectHomePage()
            select_home_page.click_saved_properties_btn()
