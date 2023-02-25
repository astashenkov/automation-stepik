from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link1 = 'http://suninjuly.github.io/registration1.html'
    link2 = 'http://suninjuly.github.io/registration2.html'
    browser.get(link1)

    input_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
    input_surname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    input_email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
    input_phone = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone:"]')
    input_address = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your address:"]')

    input_name.send_keys('Some name')
    input_surname.send_keys('Some surname')
    input_email.send_keys('Some email')
    input_phone.send_keys('Some phone')
    input_address.send_keys('Some address')

    time.sleep(5)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    title = browser.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Congratulations! You have successfully registered!'

finally:
    time.sleep(5)
    browser.quit()
