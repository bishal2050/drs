import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # Code to set up test environment
        self.driver = webdriver.Chrome()  # It will open the Edge browser
        self.driver.maximize_window()  # Maximize the browser window
        self.driver.get("https://demoblaze.com/")  # Open the Google website

    def test_login(self):
        # Code to perform the test
        nav_login_id = self.driver.find_element("id", "login2")  # Find the login button by its ID
        nav_login_id.click()  # Click the login button
        self.driver.implicitly_wait(10)  # Implicitly wait for elements to be present
        txt_username = self.driver.find_element(By.ID, "loginusername")  # Find the username input field by its ID
        txt_username.send_keys("testmorning")  # Enter the username
        txt_password = self.driver.find_element(By.ID, "loginpassword")  # Find the password input field by its ID
        txt_password.send_keys("test123")  # Enter the password
        btn_login = self.driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")  # Find the login button by its XPath
        btn_login.click()  # Click the login button
        time.sleep(5)

        expected_result = "Welcome testmorning"
        actual_result = self.driver.find_element(By.ID, "nameofuser").text  # Get the text of the welcome message
        self.assertEqual(expected_result, actual_result, "User was not successful")  # Assert that the expected and actual results
    def test_login_fail(self):
        # Code to perform the test
        nav_login_id = self.driver.find_element("id", "login2")  # Find the login button by its ID
        nav_login_id.click()  # Click the login button
        self.driver.implicitly_wait(10)  # Implicitly wait for elements to be present
        txt_username = self.driver.find_element(By.ID, "loginusername")  # Find the username input field by its ID
        txt_username.send_keys("testmorning")  # Enter the username
        txt_password = self.driver.find_element(By.ID, "loginpassword")  # Find the password input field by its ID
        txt_password.send_keys("test1234")  # Enter the password
        btn_login = self.driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")  # Find the login button by its XPath
        btn_login.click()  # Click the login button
        time.sleep(5)
        actual_result = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        expected_result = "Wrong password."
        self.assertEqual(expected_result, actual_result, "User was successful")  # Assert that the expected and actual results
    def tearDown(self):
        # Code to clean up after the test
        self.driver.quit()  # Quit the driver and close all associated windows

if __name__ == '__main__':
    unittest.main()
