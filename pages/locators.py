from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_CONTENT = (By.ID, "content_inner")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn-default")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    PRODUCT_PAGE = (By.CLASS_NAME, "product_page")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME_ON_SUCCESS_BANNER = (By.CSS_SELECTOR, ".alertinner > strong")
    ADD_TO_CART_SUCCESS_BANNER = (By.CLASS_NAME, "alert-success")
    CART_PRICE = (By.CLASS_NAME, "basket-mini")


class BasketPageLocators:
    BASKET_PAGE_HEADER = (By.CLASS_NAME, "page-header")
    BASKET_PAGE_ITEMS = (By.CLASS_NAME, "basket-items")
