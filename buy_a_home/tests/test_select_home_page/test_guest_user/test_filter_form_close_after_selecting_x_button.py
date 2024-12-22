import pytest
import allure
from hamcrest import assert_that, not_

from buy_a_home.steps.NavigateSteps import NavigateSteps
from buy_a_home.pages.select_home.FilterForm import FilterForm
from buy_a_home.pages.select_home.SearchHomePage import SearchHomePage


class TestCloseButtonFilterForm:
    """Test that Filter form can be closed after selecting "X" button: BUAH-1373"""

    @pytest.mark.regression
    @pytest.mark.guest_user
    def test_filter_form_close_after_selecting_x_button(self):
        NavigateSteps.go_to_search_page()

        with allure.step("Select filter icon"):
            search_home_page = SearchHomePage()
            search_home_page.click_filter_icon()

        with allure.step("Close filter pop-up"):
            filter_form = FilterForm()
            filter_form.click_close_filter_pop_up_btn()

        with allure.step("Check that Filter Form is closed"):
            assert_that(not_(filter_form.is_filter_form_opened()), "X button for filter form is displayed")
