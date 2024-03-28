from typing_extensions import Self

from pages.locators import BasePageLocators, BasketPageLocators

from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_page(self: Self) -> None:
        self.should_be_basket_url()
        self.should_be_basket_header()


    def should_be_basket_url(self: Self) -> None:
        assert "basket" in self.browser.current_url


    def should_be_basket_header(self: Self) -> None:
        assert "Basket" in self.browser.find_element(*BasketPageLocators.BASKET_PAGE_HEADER).text


    def should_be_backet_empty(self: Self) -> None:
        self.is_not_element_present(*BasketPageLocators.BASKET_PAGE_ITEMS)
        content_element = self.browser.find_element(*BasePageLocators.BASKET_PAGE_CONTENT)
        assert "Your basket is empty. Continue shopping" == content_element.text
