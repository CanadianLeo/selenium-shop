from typing_extensions import Self
from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage:
    def __init__(self: Self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def open(self: Self):
        self.browser.get(self.url)
