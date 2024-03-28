from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_add_to_cart_button_exist(browser: WebDriver):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), "Кнопка 'Добавить в корзину' не найдена"
