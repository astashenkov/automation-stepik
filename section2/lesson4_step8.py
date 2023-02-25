import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(value: int) -> str:
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
browser.find_element(By.ID, 'book').click()

button = browser.find_element(By.ID, 'solve')
browser.execute_script('return arguments[0].scrollIntoView(true);', button)

x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
button.click()

print(browser.switch_to.alert.text)
browser.quit()
