from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.List import List
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class BasePageJourney(BasePage):
    page_name = "Base Page Journey"
    locator_reader = LocatorReader(page_name)

    lbl_absent_property_details = Label(locator_reader, "lbl_absent_property_details")
    lbl_buah_breadcrumb = Label(locator_reader, 'lbl_buah_breadcrumb')
    lbl_go_back_breadcrumb = Label(locator_reader, 'lbl_go_back_breadcrumb')
    lbl_monthly_payment = Label(locator_reader, "lbl_monthly_payment_property")
    lbl_monthly_payment_financing = Label(locator_reader, "lbl_monthly_payment_financing")
    lbl_chosen_home_price = Label(locator_reader, "lbl_chosen_home_price")
    lbl_star_enabled = Label(locator_reader, "lbl_star_enabled")
    lbl_star_enabled_without_price = Label(locator_reader, "lbl_star_enabled_without_price")
    lbl_star_filled_without_price = Label(locator_reader, "lbl_star_filled_without_price")
    lbl_next_page = Label(locator_reader, 'lbl_next_page')
    lbl_prev_page = Label(locator_reader, 'lbl_prev_page')

    txb_tenure_years = TextBox(locator_reader, "txb_tenure_years")

    btn_continue_without_selecting = Button(locator_reader, 'btn_continue_without_selecting')
    btn_close_login_popup = Button(locator_reader, 'btn_close_login_popup')
    btn_load_more = Button(locator_reader, 'btn_load_more')
    btn_check_bank_loan_options = Button(locator_reader, "btn_check_bank_loan_options")
    btn_proceed_to_deed_transfer = Button(locator_reader, "btn_proceed_to_deed_transfer")
    btn_yes_remove_save = Button(locator_reader, "btn_yes_remove_save")
    btn_no_remove_save = Button(locator_reader, "btn_no_remove_save")
    btn_close_save_remove_pop_up = Button(locator_reader, "btn_close_save_remove_pop_up")
    btn_choose_home = Button(locator_reader, "btn_choose_home")

    lst_of_results_price_with_stars = List(locator_reader, "list_of_results_price_with_stars")
    lst_of_results_price_with_enabled_stars = List(locator_reader, "list_of_results_price_with_enabled_stars")
    lst_properties_without_selected_heart = List(locator_reader, "list_properties_without_selected_heart")
    lst_properties_with_selected_heart = List(locator_reader, "list_of_results_price_with_filled_stars")
    list_of_results_price_with_filled_stars_without_specific_price = \
        List(locator_reader, "list_of_results_price_with_filled_stars_without_specific_price")

    def is_chbx_desabled_or_enabled_present(self, checkbox_locator):
        """
        Return "true" if checkbox is selected or is deselected (depends from locator)
        :return: bool: locator is present
        """
        return checkbox_locator.is_present()

    def is_load_more_btn_present(self):
        self.btn_load_more.wait_until_location_stable()
        return self.btn_load_more.is_present()

    def is_login_pop_up_present(self):
        return self.btn_close_login_popup.is_present()

    def get_random_data_from_locator(self, object_locator):
        list_of_data = []
        data_list = object_locator.get_random_items_from_list(1)
        list_of_data.append(data_list)
        return list_of_data

    def click_random_checkboxes(self, locator_of_checkboxes, list_checkboxes):
        for i in list_checkboxes:
            self.scroll_to_element(locator_of_checkboxes.format(i))
            locator_of_checkboxes.format(i).wait_until_location_stable()
            locator_of_checkboxes.format(i).click()

    def click_buah_breadcrumb(self):
        self.lbl_buah_breadcrumb.scroll_by_script()
        self.lbl_buah_breadcrumb.click_js()  # Confirmed by customer to use it here

    def click_go_back_breadcrumb(self):
        self.lbl_go_back_breadcrumb.scroll_by_script()  # Confirmed by customer to use it here
        self.lbl_go_back_breadcrumb.click_js()

    def click_choose_property_button(self):
        self.btn_choose_home.wait_until_location_stable()
        self.btn_choose_home.click()

    def click_continue_without_selecting_btn(self):
        self.btn_continue_without_selecting.wait_until_location_stable()
        self.btn_continue_without_selecting.click()

    def click_close_login_popup_btn(self):
        self.btn_close_login_popup.scroll_by_script()
        self.btn_close_login_popup.wait_until_location_stable()
        self.btn_close_login_popup.click()

    def click_star_enabled_lbl(self, price):
        self.lbl_star_enabled.format(price).wait_until_location_stable()
        self.lbl_star_enabled.format(price).scroll_by_script()
        self.lbl_star_enabled.format(price).click()

    def click_btn_load_more(self):
        self.scroll_to_element(self.btn_load_more)
        self.btn_load_more.wait_until_location_stable()
        self.btn_load_more.click()

    def click_check_bank_loan_btn(self):
        self.btn_check_bank_loan_options.wait_until_location_stable()
        self.scroll_to_element(self.btn_check_bank_loan_options)
        self.btn_check_bank_loan_options.click()

    def click_proceed_deed_transfer_btn(self):
        self.btn_proceed_to_deed_transfer.wait_until_location_stable()
        self.scroll_to_element(self.btn_proceed_to_deed_transfer)
        self.btn_proceed_to_deed_transfer.click()

    def click_yes_btn_remove_heart(self):
        self.btn_yes_remove_save.wait_until_location_stable()
        self.btn_yes_remove_save.click()

    def click_no_btn_remove_heart(self):
        self.btn_no_remove_save.wait_until_location_stable()
        self.btn_no_remove_save.click()

    def click_next_link(self):
        self.lbl_next_page.wait_until_location_stable()
        self.lbl_next_page.click()

    def click_prev_link(self):
        self.lbl_prev_page.wait_until_location_stable()
        self.lbl_prev_page.click()

    def click_close_remove_saved_property_pop_up(self):
        self.btn_close_save_remove_pop_up.wait_until_location_stable()
        self.btn_close_save_remove_pop_up.click()
