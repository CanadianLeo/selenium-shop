import math
from typing_extensions import Self
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException

from pages.locators import BasePageLocators

MAIN_LINK = "https://selenium1py.pythonanywhere.com/"

class BasePage:
    def __init__(self: Self, browser: WebDriver, url: str, timeout: int = 10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def go_to_basket_page(self: Self) -> None:
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()


    def go_to_login_page(self: Self) -> None:
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()


    def should_be_login_link(self: Self) -> None:
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def open(self: Self) -> None:
        self.browser.get(self.url)


    def is_element_present(self: Self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    def is_not_element_present(self: Self, how: str, what: str, timeout: int = 4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    

    def is_disappeared(self: Self, how: str, what: str, timeout: int = 4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    def solve_quiz_and_get_code(self: Self) -> None:
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")
        
        except NoAlertPresentException:
            pass


    def should_be_authorized_user(self: Self) -> None:
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
