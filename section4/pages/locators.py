from selenium.webdriver.common.by import By


class BasketPageLocators:

    EMPTY_MESSAGE_CONTAINER = (By.CSS_SELECTOR, '.content_inner p')


class BasePageLocators:

    LOGIN_LINK = (By.ID, 'login_link')
    GO_BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')


class LoginPageLocators:

    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main  .price_color')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    ADDED_TO_BASKET_PRODUCT_TITLE = (By.CSS_SELECTOR, '.alert-noicon.alert-success div strong')
    ADDED_TO_BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
