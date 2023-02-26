import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistered(unittest.TestCase):
    """Refactoring test from section 1 lesson 6 step 11 with using unittest framework."""

    def test_registration1(self):
        """Test registration on the first page."""

        chrome_browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/registration1.html'
        chrome_browser.get(link)

        input_name = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your first name"]'
        )
        input_name.send_keys('Some name')

        input_surname = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your last name"]'
        )
        input_surname.send_keys('Some surname')

        input_email = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your email"]'
        )
        input_email.send_keys('Some email')

        input_phone = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your phone:"]'
        )
        input_phone.send_keys('Some phone')

        input_address = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your address:"]'
        )
        input_address.send_keys('Some address')

        button = chrome_browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()

        title = chrome_browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(title.text, 'Congratulations! You have successfully registered!')
        chrome_browser.quit()

    def test_registration2(self):
        """Test registration on the second page."""

        chrome_browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/registration2.html'
        chrome_browser.get(link)

        input_name = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your first name"]'
        )
        input_name.send_keys('Some name')

        input_surname = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your last name"]'
        )
        input_surname.send_keys('Some surname')

        input_email = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your email"]'
        )
        input_email.send_keys('Some email')

        input_phone = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your phone:"]'
        )
        input_phone.send_keys('Some phone')

        input_address = chrome_browser.find_element(
            By.CSS_SELECTOR,
            'input[placeholder="Input your address:"]'
        )
        input_address.send_keys('Some address')

        button = chrome_browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()

        title = chrome_browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(title.text, 'Congratulations! You have successfully registered!')
        chrome_browser.quit()
