from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(value: int) -> str:
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))

button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()
button.click()

time.sleep(5)
browser.quit()
