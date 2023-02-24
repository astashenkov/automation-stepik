from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    page = 'http://suninjuly.github.io/registration1.html'
    browser.get(page)

    input_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
    input_surname = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
    input_email = browser.find_element_by_css_selector('input[placeholder="Input your email"]')

    input_name.send_keys('Add some name')
    input_surname.send_keys('Add some surname')
    input_email.send_keys('Add some email')

    time.sleep(5)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    title = browser.find_element_by_name('h1')
    assert title.text == 'Congratulations! You have successfully registered!'


finally:
    time.sleep(5)
    browser.quit()
