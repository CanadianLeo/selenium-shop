from typing_extensions import Self
from pytest import mark

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self: Self) -> None:
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE), \
            "It is not product page"


    def should_not_be_success_message(self: Self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_BANNER), \
            "Success message is presented, but should not be"
        

    def should_not_be_success_message_2(self: Self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_BANNER), \
            "Success message is presented, but should not be"
        
    

    def should_be_add_to_basket_button_exist_and_enable(self: Self) -> None:
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), \
            "Add to basket button is not exist"
        
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).is_enabled, \
            "Add to basket button is disabled"


    def get_product_name(self: Self) -> str:
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name_element.text
    

    def get_product_price(self: Self) -> str:
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price_element.text


    def add_to_basket_button_click(self: Self) -> None:
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()


    def add_to_basket(self: Self) -> None:
        self.should_be_product_page()
        self.should_be_add_to_basket_button_exist_and_enable()
        self.add_to_basket_button_click()

        self.solve_quiz_and_get_code()


    def should_success_add_product_to_basket(self: Self) -> None:
        self.add_to_basket()
        product_name = self.get_product_name()
        product_price = self.get_product_price()


        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_BANNER), \
            "Success banner after add product to basket is not exist"
        
        basket_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        assert product_price in basket_price.text, \
            "Product price not equal basket price after click add to basket button"
        
        product_name_on_banner = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_SUCCESS_BANNER)
        assert product_name == product_name_on_banner.text, \
            "Product name on page not equal product name on success banner after click add to basket button"

    @mark.xfail
    def should_success_banner_not_exist_after_add_to_basket(self: Self) -> None:
        self.add_to_basket()

        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_BANNER)

    
    def should_success_banner_not_exist(self: Self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_BANNER)

    
    def should_success_banner_not_exist_after_after_add_product_to_basket(self: Self) -> None:
        self.add_to_basket()

        assert self.is_disappeared(*ProductPageLocators.ADD_TO_CART_SUCCESS_BANNER)
