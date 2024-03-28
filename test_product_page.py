from selenium.webdriver.chrome.webdriver import WebDriver
from pytest import mark, param

from pages.login_page import LoginPage
from pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
LINKS = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

@mark.parametrize('link', LINKS)
def test_guest_can_add_product_to_basket(browser: WebDriver, link: str) -> None:
    page = ProductPage(browser, link)
    page.open()

    page.should_success_add_product_to_cart()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()

    page.should_success_banner_not_exist_after_add_to_cart()


def test_guest_cant_see_success_message(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()

    page.should_success_banner_not_exist()


def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()

    page.should_success_banner_not_exist_after_after_add_product_to_cart()


def test_guest_should_see_login_link_on_product_page(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()