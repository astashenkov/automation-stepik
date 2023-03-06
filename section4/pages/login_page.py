from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'You are not on the login page!'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form don't presented on the page!"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form don't presented on the page!"

    def register_new_user(self, email, password):
        email_fild = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FILD)
        password_fild = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FILD)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTRATION_PASSWORD_FILD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        email_fild.send_keys(email)
        password_fild.send_keys(password)
        confirm_password.send_keys(password)
        register_button.click()
