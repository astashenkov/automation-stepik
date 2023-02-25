from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(value: int) -> str:
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

browser.switch_to.window(browser.window_handles[1])

x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

time.sleep(5)
browser.quit()
