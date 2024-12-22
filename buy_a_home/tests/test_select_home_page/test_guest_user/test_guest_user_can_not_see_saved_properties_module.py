import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.pages.select_home.SelectHomePage import SelectHomePage
from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage


class TestExistDataPropertyDetailsPage:
    """Saved properties: Guest doesn't see data on this page after refreshing page: BUAH-1794"""

    @pytest.mark.smoke
    @pytest.mark.guest_user
    def test_guest_user_can_not_see_saved_properties_module(self):
        NavigateSteps.go_to_select_home_page()

        select_home_page = SelectHomePage()

        with allure.step("Check that \"Saved properties\" module is absent"):
            assert_that(not_(select_home_page.is_saved_properties_btn_present()), "\"Saved properties\" button is "
                                                                                  "present")

        with allure.step("Select 'Search' Button on 'Select Home' Page"):
            select_home_page.click_search_btn()

        with allure.step("Check that \"Saved properties\" module is absent"):
            search_home_page = SearchHomePage()
            assert_that(not_(search_home_page.is_saved_properties_lbl_present()), "\"Saved properties\" label is "
                                                                                  "present")
