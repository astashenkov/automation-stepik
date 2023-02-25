from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link1 = 'https://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()
browser.get(link1)

num_sum = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)
select = Select(browser.find_element(By.TAG_NAME, 'select'))
select.select_by_value(str(num_sum))
browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

time.sleep(5)
browser.quit()
