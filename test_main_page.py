from selenium.webdriver.chrome.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser: WebDriver) -> None:
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser: WebDriver) -> None:
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_login_link()
