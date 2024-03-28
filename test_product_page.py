from selenium.webdriver.chrome.webdriver import WebDriver

from pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser: WebDriver) -> None:
    page = ProductPage(browser, LINK)
    page.open()

    page.add_to_cart()
