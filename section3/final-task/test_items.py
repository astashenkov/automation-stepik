import selenium
from selenium.webdriver.common.by import By


def test_exists_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    try:
        text_on_the_button = browser.find_element(
            By.CSS_SELECTOR, '.btn-add-to-basket'
        ).text
    except selenium.common.exceptions.NoSuchElementException:
        text_on_the_button = ''

    assert text_on_the_button, "Didn't find button"
