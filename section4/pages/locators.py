from selenium.webdriver.common.by import By


class BasketPageLocators:
    NOT_EMPTY_CONTAINER = (By.CSS_SELECTOR, '.basket-title.hidden-xs')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')


class BasePageLocators:
    LOGIN_LINK = (By.ID, 'login_link')
    GO_BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL_FILD = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD_FILD = (By.ID, 'id_registration-password1')
    CONFIRM_REGISTRATION_PASSWORD_FILD = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main  .price_color')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    ADDED_TO_BASKET_PRODUCT_TITLE = (By.CSS_SELECTOR, '.alert-noicon.alert-success div strong')
    ADDED_TO_BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
