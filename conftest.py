from typing import Generator
from pytest import fixture, FixtureRequest, Parser
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@fixture(scope="function")
def browser(request: FixtureRequest) -> Generator[WebDriver, None, None]:
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    yield browser
    browser.quit()
