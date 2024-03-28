from typing_extensions import Self

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self: Self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self: Self) -> None:
        assert "login" in self.browser.current_url


    def should_be_login_form(self: Self) -> None:
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)


    def should_be_register_form(self: Self) -> None:
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)


    def register_new_user(self: Self, email: str, password: str) -> None:
        self.should_be_login_page()

        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        password_2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        email_field.send_keys(email)
        password_1_field.send_keys(password)
        password_2_field.send_keys(password)

        button.click()

        assert self.is_not_element_present(*LoginPageLocators.REGISTRATION_ALERT), \
            "User is not register"
