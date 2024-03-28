from typing_extensions import Self

from faker import Faker
from selenium.webdriver.chrome.webdriver import WebDriver
from pytest import fixture, mark, param

from pages.basket_page import BasketPage
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
@mark.need_review
def test_guest_can_add_product_to_basket(browser: WebDriver, link: str) -> None:
    page = ProductPage(browser, link)
    page.open()

    page.should_success_add_product_to_basket()


@mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()

    page.should_success_banner_not_exist_after_add_to_basket()


def test_guest_cant_see_success_message(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()

    page.should_success_banner_not_exist()


@mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()

    page.should_success_banner_not_exist_after_after_add_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()


@mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()


@mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()

    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()

    basket_page.should_be_backet_empty()


@mark.signed_user
class TestUserAddToBasketFromProductPage:
    @fixture(scope="function", autouse=True)
    def setup(self: Self, browser: WebDriver) -> None:
        page = ProductPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

        f = Faker("ru_RU")
        login_page.register_new_user(f.email(), f.name())
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self: Self, browser: WebDriver) -> None:
        page = ProductPage(browser, LINK)
        page.open()

        page.should_success_banner_not_exist()


    @mark.parametrize('link', LINKS)
    @mark.need_review
    def test_user_can_add_product_to_basket(self: Self, browser: WebDriver, link: str) -> None:
        page = ProductPage(browser, link)
        page.open()

        page.should_success_add_product_to_basket()