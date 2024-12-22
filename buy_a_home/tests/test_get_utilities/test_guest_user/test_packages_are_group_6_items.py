import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.HomePage import HomePage
from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.get_utilities.EtisalatPage import EtisalatPage
from buy_a_home.pages.get_utilities.GetUtilitiesPage import GetUtilitiesPage
from buy_a_home.pages.get_utilities.WaterElectricityPage import WaterElectricityPage
from framework.utils.DataReader import DataReader


class Test6PackagesEtisalat:
    """Etisalat page: Divide the offers from etisalat into groups to make it more organized (group of 6 with a more
    button): BUAH-2339"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_packages_are_group_6_items(self):
        with allure.step("Go to \"Get utilities\" page"):
            home_page = HomePage()
            home_page.click_navigation_panel_btn(NavigationHomeItems.GET_UTILITIES.value)

        with allure.step("Select \"View\" button for the 1st step"):
            get_utilities_page = GetUtilitiesPage()
            get_utilities_page.click_view_btn_water_and_electricity()

        with allure.step("Select \"Continue\" button on \"Water and Electricity\" page"):
            water_electricity_page = WaterElectricityPage()
            water_electricity_page.click_continue_btn_water_and_electricity()

        with allure.step("Check that 6 property are displayed and Load more button is present"):
            etisalat_page = EtisalatPage()
            assert_that(etisalat_page.get_count_of_packages() == DataReader.get_data("Navigation Items.qty of packages")
                        and etisalat_page.is_load_more_btn_present,
                        "6 items and Load More button aren't displayed by default")

        with allure.step(
                "Click Load More button and check that quantity of packages is increased or Load More button is "
                "absent"):
            etisalat_page.click_btn_load_more()
            assert_that(etisalat_page.get_count_of_packages() != DataReader.get_data("Navigation Items.qty of packages")
                        or not_(etisalat_page.is_load_more_btn_present),
                        "Quantity of packages is increased or Load More button is absent")
