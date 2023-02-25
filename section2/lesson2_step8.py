from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Some first name')
browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Some last name')
browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('Some email')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

time.sleep(5)
browser.quit()
