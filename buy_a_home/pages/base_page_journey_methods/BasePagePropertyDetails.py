from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.StringUtil import StringUtil


class BasePagePropertyDetails(BasePage):
    page_name = "Base Page Property Details"
    locator_reader = LocatorReader(page_name)

    lbl_area_field_data = Label(locator_reader, "lbl_area_data_field")
    lbl_star_property = Label(locator_reader, 'lbl_star_property')

    lbl_profile = Label(locator_reader, 'lbl_profile')

    lnk_chosen_home = Link(locator_reader, "lnk_chosen_home")

    def is_profile_present(self):
        return self.lbl_profile.is_present()

    def is_chosen_home_present(self):
        return self.lnk_chosen_home.is_present()

    def get_area_text(self):
        self.lbl_area_field_data.wait_until_location_stable()
        return self.lbl_area_field_data.get_text()

    def get_property_details_price(self, property_locator):
        property_locator.wait_until_location_stable()
        price = property_locator.get_text()
        price_regular = StringUtil.get_text_without_letters(price)
        return price_regular

    def click_star_property(self, price):
        price_regular = StringUtil.get_text_without_letters(price)
        self.lbl_star_property.format(price_regular).scroll_by_script()
        self.lbl_star_property.format(price_regular).click()

    def click_property_details(self, property_details_locator):
        property_details_locator.click()
