from framework.configuration import config
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.List import List
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.StringUtil import StringUtil
from framework.utils.WaiterUtil import WaiterUtil


class BasePageHomeFromList(BasePage):
    page_name = "Base Page Home From List"
    locator_reader = LocatorReader(page_name)

    btn_select_for_home_with_price_and_star = Button(locator_reader, 'btn_select_for_home_with_price_and_star')
    btn_select_home = Button(locator_reader, 'btn_select_home_according_price')

    lbl_price_home = Label(locator_reader, "lbl_price_selected_home")
    lbl_island_location = Label(locator_reader, "lbl_island_location")
    lbl_area_location = Label(locator_reader, "lbl_area_location")
    lbl_star = Label(locator_reader, 'lbl_star')
    lbl_absent_star = Label(locator_reader, 'lbl_absent_star')
    lbl_selected_star = Label(locator_reader, 'lbl_selected_star')

    lst_of_results_quick_search = List(locator_reader, "list_of_results_price")

    def is_island_present(self, price):
        return self.lbl_island_location.format(price).is_present()

    def is_area_present(self, price):
        return self.lbl_area_location.format(price).is_present()

    def is_home_with_specific_price_present(self, price):
        return self.is_price_present(price) and self.is_island_present(price) and self.is_area_present(price) and \
               self.is_selected_star_present(price)

    def is_price_present(self, price):
        return self.lbl_price_home.format(price).is_present()

    def is_selected_star_present(self, price):
        """
        Method check that star was selected for home
        :return: bool: True if selected star with specific star is present
        """
        price_regular = StringUtil.get_text_without_letters(price)
        return self.lbl_selected_star.format(price_regular).is_present()

    def get_count_of_home_results(self):
        """
        Get count of homes by search results
        :return: int: count of homes
        """
        self.lst_of_results_quick_search.wait_until_location_stable()
        return self.lst_of_results_quick_search.get_elements_count()

    def get_random_property_details_of_price(self):
        """
        Get random property details according price
        :return: str: random price for home
        """
        self.lst_of_results_quick_search.wait_until_location_stable()
        price = self.lst_of_results_quick_search.get_random_items_from_list(1)
        return StringUtil.get_text_without_letters(price)

    def get_first_property_details_of_price(self):
        """
        Get the 1st property details according price
        :return: str: price for home
        """
        self.lst_of_results_quick_search.wait_until_location_stable()
        price = self.lst_of_results_quick_search.get_elements_text()[0]
        return StringUtil.get_text_without_letters(price)

    def get_data_from_home_with_star(self, get_data_method):
        """
        Get Island, Area, Price data from random selected home with star
        :param get_data_method: method for working with data list from locator
        :return: list: list with parameters for selected home
        """
        random_home = get_data_method
        price_regular = StringUtil.get_text_without_letters(random_home[0])

        def wait_for_random_home():
            nonlocal random_home
            if not self.lbl_absent_star.format(price_regular).try_wait_for_absent():
                random_home_2 = get_data_method
                if random_home_2 is not None:
                    random_home = random_home_2
            else:
                return random_home

        WaiterUtil.wait_for_true(wait_for_random_home, config.CYCLE_WAIT_TIMEOUT)
        self.lbl_star.format(price_regular).scroll_by_script()
        self.click_star(price_regular)
        return random_home

    def get_random_price_for_home(self):
        price_of_home = self.lst_of_results_quick_search.get_random_items_from_list(1)
        price_regular = StringUtil.get_text_without_letters(price_of_home)
        return price_regular

    def get_the_first_home_with_price(self):
        price_of_home = self.lst_of_results_quick_search.get_elements_text()[0]
        price_regular = StringUtil.get_text_without_letters(price_of_home)
        return price_regular

    def get_island_location(self, price):
        """
        Method connected with returning island text for selected home
        :return: str: island text
        """
        return self.lbl_island_location.format(price).get_text()

    def get_area_location(self, price):
        """
        Get area text for selected home
        :return: str: area text
        """
        return self.lbl_area_location.format(price).get_text()

    def get_first_item_from_locator(self, object_locator):
        """
        Get the first data from list
        :param object_locator: locator for data
        :return: str: the first item from list
        """
        list_of_search = []
        price_of_home = object_locator.get_elements_text()[0]
        price_regular = StringUtil.get_text_without_letters(price_of_home)
        list_of_search.append(price_regular)
        list_of_search.append(self.get_island_location(price_regular))
        list_of_search.append(self.get_area_location(price_regular).split(",")[0].title())
        return list_of_search

    def get_data_from_selected_home(self):
        """
        Get Island, Area, Price data from opened random home
        :return: list: list with parameters for selected home
        """
        random_home = self.get_random_data_about_home_from_locator(self.lst_of_results_quick_search, False)
        self.btn_select_home.format(random_home[0]).scroll_by_script()
        self.btn_select_home.format(random_home[0]).click()
        return random_home

    def get_random_data_about_home_from_locator(self, object_locator, is_star, page=None):
        """
        Get random data from list about home from locator
        :param is_star: bool: true if star is present
        :param page: page with locators
        :param object_locator: locator for data
        :return: list: list of search data
        """
        if is_star:
            while page.lbl_star_enabled_without_price.try_wait_for_absent():
                page.click_btn_load_more()
        list_of_search = []
        price_of_home = object_locator.get_random_items_from_list(1)
        price_regular = StringUtil.get_text_without_letters(price_of_home)
        list_of_search.append(price_regular)
        list_of_search.append(self.get_island_location(price_of_home))
        list_of_search.append(self.get_area_location(price_of_home).split(",")[0].title())
        return list_of_search

    def click_and_return_data_for_home_with_selected_star(self, get_data_method):
        """
        Click to star for the first selected home and receiving Island, Area, Price data for
        random home
        :param get_data_method: method for working with data list from locator
        :return: list: list with parameters for selected home with star
        """
        random_home = self.get_data_from_home_with_star(get_data_method)
        price_regular = StringUtil.get_text_without_letters(random_home[0])
        self.click_property_detail_with_selected_star(price_regular)
        return random_home

    def click_random_result_of_search(self):
        price_of_home = self.lst_of_results_quick_search.get_random_items_from_list(1)
        price = StringUtil.get_text_without_letters(price_of_home)
        self.btn_select_home.format(price).wait_until_location_stable()
        self.btn_select_home.format(price).scroll_by_script()
        self.btn_select_home.format(price).get_elements()[0].click()

    def click_star(self, price):
        self.scroll_to_element(self.lbl_star.format(price))
        self.lbl_star.format(price).click()

    def click_property_detail(self, price):
        self.btn_select_home.format(price).wait_until_location_stable()
        self.btn_select_home.format(price).scroll_by_script()
        self.btn_select_home.format(price).click()

    def click_property_detail_with_selected_star(self, price):
        price_regular = StringUtil.get_text_without_letters(price)
        self.lbl_price_home.format(price_regular).wait_until_location_stable()
        self.btn_select_for_home_with_price_and_star.format(price_regular).click()
