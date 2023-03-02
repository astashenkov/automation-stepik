import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        default='en',
        action='store',
        help='Choose language'
    )


@pytest.fixture(scope="function")
def browser(request):
    print('\nStart browser...')
    browser_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nQuit browser.')
    browser.quit()
