from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from buy_a_home.pages.base_page_journey_methods.BasePageSearchAndFilter import BasePageSearchAndFilter
from framework.elements.Button import Button
from framework.elements.Checkbox import Checkbox
from framework.elements.Dropdown import Dropdown
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.elements.List import List
from framework.elements.Slider import Slider
from framework.utils.LocatorReader import LocatorReader


class FilterForm(BasePageJourney, BasePageSearchAndFilter):
    page_form = "Filter Form"
    locator_reader = LocatorReader(page_form)
    page_element = Label(locator_reader, "lbl_filter_form")

    chbx_apartment_filter_enable = Checkbox(locator_reader, "checkbox_apartment_filter_enable")
    chbx_villa_filter_enable = Checkbox(locator_reader, "checkbox_villa_filter_enable")
    chbx_apartment_filter_disable = Checkbox(locator_reader, "checkbox_apartment_filter_disable")
    chbx_villa_filter_disable = Checkbox(locator_reader, "checkbox_villa_filter_disable")
    chbx_list_of_amenities = Checkbox(locator_reader, "checkbox_list_of_amenities")
    chbx_of_amenity = Checkbox(locator_reader, "checkbox_of_amenity")

    btn_apply_filter = Button(locator_reader, "btn_apply_filter")
    btn_apply_filter_not_available = Button(locator_reader, "btn_apply_filter_not_available")
    btn_close_filter_form = Button(locator_reader, "btn_close_filter_pop_up")
    btn_clear = Button(locator_reader, "btn_clear")

    lnk_show_amenities = Link(locator_reader, "lnk_show_amenities")

    sld_price_slider = Slider(locator_reader, "slider_range_price")

    lst_minBedrooms_dropdown_form = List(locator_reader, "minBedrooms_list_dropdown_form")
    lst_minBathrooms_dropdown_form = List(locator_reader, "minBathrooms_list_dropdown_form")
    lst_maxBedrooms_dropdown_form = List(locator_reader, "maxBedrooms_list_dropdown_form")
    lst_maxBathrooms_dropdown_form = List(locator_reader, "maxBathrooms_list_dropdown_form")
    lst_minBedrooms_qty_form = List(locator_reader, "minBedrooms_list_dropdown_filter")
    lst_maxBedrooms_qty_form = List(locator_reader, "maxBedrooms_list_dropdown_filter")

    lbl_minBedrooms_item_dropdown_filter = Label(locator_reader, "lbl_minBedrooms_item_dropdown_filter")
    lbl_minBathrooms_item_dropdown_filter = Label(locator_reader, "lbl_minBathrooms_item_dropdown_filter")
    lbl_maxBedrooms_item_dropdown_filter = Label(locator_reader, "lbl_maxBedrooms_item_dropdown_filter")
    lbl_maxBathrooms_item_dropdown_filter = Label(locator_reader, "lbl_maxBathrooms_item_dropdown_filter")

    drpdwn_min_bedrooms_filter_form = Dropdown(locator_reader, "lbl_minBedrooms_item_dropdown_filter",
                                               "minBedrooms_arrow_dropdown_filter")
    drpdwn_min_bathrooms_filter_form = Dropdown(locator_reader, "lbl_minBathrooms_item_dropdown_filter",
                                                "minBathrooms_arrow_dropdown_filter")
    drpdwn_max_bedrooms_filter_form = Dropdown(locator_reader, "lbl_maxBedrooms_item_dropdown_filter",
                                               "maxBedrooms_arrow_dropdown_filter")
    drpdwn_max_bathrooms_filter_form = Dropdown(locator_reader, "lbl_maxBathrooms_item_dropdown_filter",
                                                "maxBathrooms_arrow_dropdown_filter")

    def __init__(self):
        super(FilterForm, self).__init__(self.page_element)

    def is_filter_form_opened(self):
        self.btn_close_filter_form.wait_until_location_stable()
        self.btn_close_filter_form.is_displayed()

    def get_amenities(self, qty):
        self.chbx_list_of_amenities.wait_until_location_stable()
        amenities_list = self.chbx_list_of_amenities.get_random_items_from_list(qty)
        return amenities_list

    def click_show_amenities_lnk(self):
        self.lnk_show_amenities.wait_until_location_stable()
        self.scroll_to_element(self.lnk_show_amenities)
        self.lnk_show_amenities.click()

    def click_apply_btn_filter(self):
        self.btn_apply_filter.wait_until_location_stable()
        self.scroll_to_element(self.btn_apply_filter)
        self.btn_apply_filter.click()

    def click_close_filter_pop_up_btn(self):
        self.btn_close_filter_form.wait_for_is_present()
        self.btn_close_filter_form.wait_until_location_stable()
        self.btn_close_filter_form.click()

    def click_and_get_new_random_amenities(self, list_of_amenities, qty):
        """
        Method connected with deselection previous amenities and getting new random list of amenities if result of
        search gave 0 property details on Filter Form
        :param list_of_amenities: list: list of previous selected amenities
        :param qty: qty of amenities
        :return: list: list of amenities
        """
        self.click_to_amenitie(list_of_amenities)
        list_of_amenities = self.get_amenities(qty)
        return list_of_amenities

    def click_to_amenitie(self, list_of_amenities):
        for i in list_of_amenities:
            self.chbx_of_amenity.format(i).scroll_by_script()
            self.chbx_of_amenity.format(i).wait_until_location_stable()
            self.chbx_of_amenity.format(i).click()

    def click_clear_btn(self):
        self.btn_clear.wait_until_location_stable()
        self.btn_clear.click()
