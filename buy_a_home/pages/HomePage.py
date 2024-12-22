from buy_a_home.pages.NavigationHomeItems import NavigationHomeItems
from buy_a_home.pages.base_page_journey_methods.BasePageHeader import BasePageHeader
from buy_a_home.pages.base_page_journey_methods.BasePageHomeFromList import BasePageHomeFromList
from buy_a_home.pages.base_page_journey_methods.BasePageJourney import BasePageJourney
from buy_a_home.pages.base_page_journey_methods.BasePagePropertyDetails import BasePagePropertyDetails
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader
from framework.elements.Button import Button


class HomePage(BasePageJourney, BasePageHomeFromList, BasePageHeader, BasePagePropertyDetails):
    page_name = "Home Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "lbl_home_page")

    btn_buy_home = Button(locator_reader, "btn_buy_home")
    btn_apply_for_ready_home_grant = Button(locator_reader, "btn_apply_for_ready_home_grant")
    btn_navigation_panels = Button(locator_reader, "btn_navigation_panels")

    def __init__(self):
        super(HomePage, self).__init__(self.page_element)

    def is_select_home_step_present(self):
        self.scroll_to_element(self.btn_navigation_panels.format(NavigationHomeItems.SELECT_HOME.value))
        self.btn_navigation_panels.format(NavigationHomeItems.SELECT_HOME.value).wait_until_location_stable()
        return self.btn_navigation_panels.format(NavigationHomeItems.SELECT_HOME.value).is_present()

    def is_home_grant_option_present(self):
        self.scroll_to_element(self.btn_apply_for_ready_home_grant)
        self.btn_apply_for_ready_home_grant.wait_until_location_stable()
        return self.btn_apply_for_ready_home_grant.is_present()

    def click_navigation_panel_btn(self, panel_item):
        self.btn_navigation_panels.format(panel_item).wait_until_location_stable()
        self.scroll_to_element(self.btn_navigation_panels.format(panel_item))
        self.btn_navigation_panels.format(panel_item).click()

    def click_buy_home_btn(self):
        self.btn_buy_home.wait_until_location_stable()
        self.btn_buy_home.click()

    def click_apply_for_ready_nome_grant_btn(self):
        self.btn_apply_for_ready_home_grant.wait_until_location_stable()
        self.btn_apply_for_ready_home_grant.click()
