import time

import allure

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.select_home.SavedPropertiesPage import SavedPropertiesPage
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage
from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from framework.utils.WaiterUtil import WaiterUtil


class RemoveSavedPropertySteps:
    """Remove saved property methods for different users"""

    @staticmethod
    def remove_save_properties_local_user(page):
        with allure.step("Click to BUAH breadcrumb"):
            page.click_buah_breadcrumb()

        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        with allure.step("Select 'Buy a home' button"):
            home_page.click_buy_home_btn()

        select_home_page = SelectHomePage()
        if select_home_page.is_saved_properties_btn_present():
            with allure.step("Select Saved properties button"):
                select_home_page = SelectHomePage()
                select_home_page.click_saved_properties_btn()

            with allure.step("Removed All Saved properties"):
                saved_properties_page = SavedPropertiesPage()
                start_time = time.time()
                while WaiterUtil.wait_for_time(start_time, "After the expected time the star icon is filled") \
                        and not saved_properties_page.lbl_star_filled_without_price.try_wait_for_absent():
                    with allure.step("Remove the first home from Saved properties page"):
                        saved_properties_page.click_random_property_with_selected_heart()

                    with allure.step("Click yes button"):
                        saved_properties_page.click_yes_btn_remove_heart()

        with allure.step("Click to BUAH breadcrumb"):
            saved_properties_page = SavedPropertiesPage()
            saved_properties_page.click_buah_breadcrumb()

    @staticmethod
    def remove_save_properties_expat_user(page):
        with allure.step("Click to BUAH breadcrumb"):
            page.click_buah_breadcrumb()

        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        select_home_page = SelectHomePage()
        if select_home_page.is_saved_properties_btn_present():
            with allure.step("Select Saved properties button"):
                select_home_page = SelectHomePage()
                select_home_page.click_saved_properties_btn()

            with allure.step("Removed All Saved properties"):
                saved_properties_page = SavedPropertiesPage()
                start_time = time.time()
                while WaiterUtil.wait_for_time(start_time, "After the expected time the star icon is filled") \
                        and not saved_properties_page.lbl_star_filled_without_price.try_wait_for_absent():
                    with allure.step("Remove the first home from Saved properties page"):
                        saved_properties_page.click_random_property_with_selected_heart()

                    with allure.step("Click yes button"):
                        saved_properties_page.click_yes_btn_remove_heart()

        with allure.step("Click to BUAH breadcrumbs"):
            saved_properties_page = SavedPropertiesPage()
            saved_properties_page.click_buah_breadcrumb()

    @staticmethod
    def remove_save_properties_expat_user_new(page):
        with allure.step("Click to BUAH breadcrumb"):
            page.click_buah_breadcrumb()

        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.SELECT_HOME.value)

        search_home_page = SearchHomePage()
        if search_home_page.is_saved_properties_lbl_present():
            with allure.step("Select Saved properties button"):
                search_home_page.click_saved_properties()

            with allure.step("Removed All Saved properties"):
                saved_properties_page = SavedPropertiesPage()
                start_time = time.time()
                while WaiterUtil.wait_for_time(start_time, "After the expected time the star icon is filled") \
                        and not saved_properties_page.lbl_star_filled_without_price.try_wait_for_absent():
                    with allure.step("Remove the first home from Saved properties page"):
                        saved_properties_page.click_random_property_with_selected_heart()

                    with allure.step("Click yes button"):
                        saved_properties_page.click_yes_btn_remove_heart()

        with allure.step("Click to BUAH breadcrumbs"):
            saved_properties_page = SavedPropertiesPage()
            saved_properties_page.click_buah_breadcrumb()
