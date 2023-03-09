from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)
x = int(browser.find_element(By.TAG_NAME, 'img').get_attribute('valuex'))
browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()
browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

time.sleep(5)
browser.quit()
