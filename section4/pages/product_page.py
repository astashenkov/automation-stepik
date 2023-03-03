from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ), "Add to basket button don't present on the page."
        self.press_button(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def get_current_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_current_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_added_to_basket_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_PRODUCT_PRICE).text

    def get_add_to_basket_alert_message(self):
        return self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_ALERT_MESSAGE).text
