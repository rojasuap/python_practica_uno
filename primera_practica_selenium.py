import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TestSelectSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_single_input_field(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        text_input_message = driver.find_element_by_xpath('//*[@id="user-message"]')
        button_message = driver.find_element_by_xpath('//*[@id="get-input"]/button')
        text_output_message = driver.find_element_by_xpath('//*[@id="display"]')
        text_input_message.send_keys('Pedro Rojas Enciso')
        button_message.click()
        self.assertRegex(text_output_message.text, "Pedro Rojas Enciso")

    def test_single_Checkbox(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        time.sleep(2)
        check_single_button = driver.find_element_by_id('isAgeSelected')
        check_single_button.click()
        label_text = driver.find_element_by_id('txtAge')
        time.sleep(1)
        self.assertRegex(label_text.text, "Success - Check box is checked")

    def test_radio_button(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
        time.sleep(2)
        radio_button_male = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[1]/div[2]/label[1]/input"
        )
        radio_button_female = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[1]/div[2]/label[2]/input"
        )
        button_check = driver.find_element_by_id('buttoncheck')
        text_output_message = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]')

        for i in [0, 1]:
            if i == 0:
                radio_button_male.click()
                button_check.click()
                time.sleep(2)
                self.assertRegex(text_output_message.text, "Male")
            else:
                radio_button_female.click()
                button_check.click()
                time.sleep(2)
                self.assertRegex(text_output_message.text, "Female")


if __name__ == '__main__':
    unittest.main()
