from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasketPage(BasePage):

    def is_empty_basket(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(BasketPageLocators.NOT_EMPTY_CONTAINER))
        except TimeoutException:
            return True

        return False

    def check_is_empty_basket(self):
        assert self.is_empty_basket(), 'The basket is not empty, but should be.'

    def is_empty_basket_message_exist(self):
        self.check_is_empty_basket()
        try:
            self.browser.find_element(*BasketPageLocators.NOT_EMPTY_CONTAINER).text
        except NoSuchElementException:
            return False

        return True

    def check_empty_basket_message_text(self):
        if self.is_empty_basket_message_exist():
            assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, \
                'The basket message is empty, but not should be.'
        else:
            assert False, 'The message is not exist, but should be.'
