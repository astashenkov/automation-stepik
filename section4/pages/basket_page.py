from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):

    def is_empty_basket(self):
        try:
            empty_basket_alert = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE_CONTAINER).text
        except NoSuchElementException:
            return False
        return True

    def is_empty_basket_message_present(self):
        try:
            empty_basket_alert = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE_CONTAINER).text
            assert empty_basket_alert, 'Empty basket message is not exist.'
        except NoSuchElementException:
            return False
        return True
