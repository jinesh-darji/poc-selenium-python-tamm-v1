from framework.elements.Button import Button
from framework.elements.InputDropdown import InputDropdown
from framework.elements.Label import Label
from framework.elements.List import List
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class BasePageSearchAndFilter(BasePage):
    page_name = "Base Page Search And Filter"
    locator_reader = LocatorReader(page_name)

    lbl_0_property_details = Label(locator_reader, "lbl_0_property_details")

    btn_filter_icon_search_results = Button(locator_reader, 'btn_filter_icon_search_results')
    btn_filter_icon = Button(locator_reader, 'btn_filter_icon')

    lst_area_list = List(locator_reader, "list_area_list_dropdown_result_page")

    drd_area_result_page = InputDropdown(locator_reader, "area_dropdown_result_page",
                                         "area_dropdown_result_page", "area_input_dropdown_result_page")

    def get_random_area_drpdwn(self):
        """
        Get name of area for inputting data in drop-down
        :return: str: selected area from drop down
        """
        return self.set_and_return_random_data_drpdwn(self.drd_area_result_page, self.lst_area_list)

    def get_specific_area_drpdwn(self, value):
        """
        Get specific name of area for inputting data in drop-down
        :return: str: selected area from drop down
        """
        return self.set_and_return_specific_data_drpdwn(self.drd_area_result_page, value)

    def get_value_from_drop_down_filter(self, field_locator):
        """
        Get value from drop-down
        :return: str: data from drop-down
        """
        field_locator.wait_for_is_present()
        field_locator.wait_for_list_is_not_empty()
        data = field_locator.get_text()
        return data

    def click_filter_icon(self):
        self.btn_filter_icon.wait_until_location_stable()
        self.btn_filter_icon.click()

    def click_filter_icon_search_results(self):
        self.btn_filter_icon_search_results.wait_until_location_stable()
        self.scroll_to_element(self.btn_filter_icon_search_results)
        self.btn_filter_icon_search_results.click()

    def click_apartment_chbx(self, apartment_locator):
        apartment_locator.wait_until_location_stable()
        apartment_locator.click()

    def click_villa_chbx(self, villa_locator):
        villa_locator.scroll_by_script()
        villa_locator.wait_until_location_stable()
        villa_locator.click()

    def set_and_return_random_data_drpdwn(self, dropdown_locator, dropdown_list):
        """
        Set and input data in drop-down and returning selected item
        :return: str: selected value from drop down
        """
        dropdown_locator.wait_until_location_stable()
        dropdown_locator.open_dropdown()
        data = dropdown_list.get_random_items_from_list(1)
        dropdown_locator.select_value(data)
        return data

    def set_and_return_specific_data_drpdwn(self, dropdown_locator, value):
        """
        Set and input data in drop-down and returning selected item
        :return: str: selected value from drop down
        """
        dropdown_locator.wait_until_location_stable()
        dropdown_locator.open_dropdown()
        dropdown_locator.select_value(value)
        return value

    def set_and_return_new_random_area(self):
        """
        Set new random area if result of search gave 0 property details
        :return: text: area
        """
        area = ''
        while not self.lbl_0_property_details.try_wait_for_absent():
            area = self.get_random_area_drpdwn()
        return area
