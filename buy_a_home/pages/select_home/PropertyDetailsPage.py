from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from buy_a_home.pages.base_page_journey_methods.BasePagePropertyDetails import BasePagePropertyDetails
from framework.elements.Button import Button
from framework.elements.Checkbox import Checkbox
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader
from framework.utils.StringUtil import StringUtil


class PropertyDetailsPage(BasePageJourney, BasePageHeader, BasePagePropertyDetails):
    page_name = "Property Details Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_property_details")

    lbl_price = Label(locator_reader, "lbl_price")
    lbl_price_value = Label(locator_reader, "lbl_price_value")
    lbl_rooms_qty = Label(locator_reader, "lbl_bedrooms")
    lbl_bathrooms_qty = Label(locator_reader, "lbl_bathrooms")
    lbl_size = Label(locator_reader, "lbl_size")
    lbl_property_type = Label(locator_reader, "lbl_property_type")
    lbl_area = Label(locator_reader, "lbl_area")
    lbl_island = Label(locator_reader, "lbl_island")
    lbl_amenities_details = Label(locator_reader, "lbl_amenities_details")
    lbl_selected_star_property = Label(locator_reader, "lbl_selected_star_property")
    lbl_interest_rate = Label(locator_reader, "lbl_interest_rate")
    lbl_services = Label(locator_reader, "lbl_services")

    chbx_services_all = Checkbox(locator_reader, "chbx_services_all")
    chbx_list_of_services = Checkbox(locator_reader, "chbx_list_of_services")
    chbx_of_service = Checkbox(locator_reader, "chbx_of_service")

    btn_check_financing_option = Button(locator_reader, "btn_financing_option")
    btn_go_to_saved_properties = Button(locator_reader, "btn_go_to_saved_properties")
    btn_services = Button(locator_reader, "btn_services")
    btn_services_close = Button(locator_reader, "btn_services_close")

    def __init__(self):
        super(PropertyDetailsPage, self).__init__(self.page_element)

    def is_services_pop_up_opened(self):
        return self.lbl_services.is_present()

    def is_property_page_opened(self):
        return self.page_element.is_present()

    def is_selected_star_present(self, price):
        """
        Return "true" if star is displayed for home with specific price
        :return: bool: True if selected star is displayed
        """
        return self.lbl_selected_star_property.format(price).is_present()

    def is_price_present(self, price_of_home):
        """
        Return "true" if specific price is displayed on Property details page
        :return: bool: price is displayed
        """
        return self.lbl_price.format(StringUtil.get_text_without_letters(price_of_home)).is_present()

    def is_area_data_present(self, area):
        """
        Return "true" if specific area is displayed
        :return: bool: area is displayed
        """
        self.lbl_area.format(area).wait_until_location_stable()
        return self.lbl_area.format(area).is_present()

    def is_island_data_present(self, island):
        """
        Return "true" if specific island is displayed
        :return: bool: area is displayed
        """
        self.lbl_island.format(island).wait_until_location_stable()
        return self.lbl_island.format(island).is_present()

    def get_price_property(self):
        price = self.lbl_price_value.get_text()
        return StringUtil.get_text_without_letters(price)

    def get_qty_bedrooms(self):
        self.lbl_rooms_qty.wait_until_location_stable()
        return int(self.lbl_rooms_qty.get_text())

    def get_qty_bathrooms(self):
        self.lbl_bathrooms_qty.wait_until_location_stable()
        return int(self.lbl_bathrooms_qty.get_text())

    def get_qty_size(self):
        return self.lbl_size.get_text().split(" ")[1].strip()

    def get_property_type(self):
        return self.lbl_property_type.get_text()

    def get_services(self, qty):
        self.chbx_list_of_services.wait_until_location_stable()
        services_list = self.chbx_list_of_services.get_random_items_from_list(qty)
        return services_list

    def get_amenities_list_property_details(self):
        property_detail_page = PropertyDetailsPage()
        property_detail_page.lbl_amenities_details.wait_until_location_stable()
        property_detail_page.lbl_amenities_details.scroll_by_script()
        amenities = property_detail_page.lbl_amenities_details.get_elements_text()
        new_list = amenities[0].split(', ')
        return new_list

    def click_btn_go_to_saved_properties(self):
        self.btn_go_to_saved_properties.click()

    def click_check_financing_option_btn(self):
        self.scroll_to_element(self.btn_check_financing_option)
        self.btn_check_financing_option.wait_until_location_stable()
        self.btn_check_financing_option.click()

    def click_services_btn(self):
        self.scroll_to_element(self.btn_services)
        self.btn_services.click()

    def click_services_all_checkbx(self):
        self.scroll_to_element(self.chbx_services_all)
        self.chbx_services_all.wait_until_location_stable()
        self.chbx_services_all.click()

    def click_services_close_btn(self):
        self.scroll_to_element(self.btn_services_close)
        self.btn_services_close.click()
