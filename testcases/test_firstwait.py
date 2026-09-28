import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFirstWait(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")

    def test_login_flow(self):
        self.driver.find_element("id", "login2").click()
        self.driver.implicitly_wait(10)

        username = self.driver.find_element(By.ID, "loginusername")
        username.send_keys("testmorning")

        password = self.driver.find_element(By.ID, "loginpassword")
        password.send_keys("test123")

        login_button = self.driver.find_element(
            By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]"
        )
        login_button.click()

        time.sleep(5)

        welcome_text = self.driver.find_element(By.ID, "nameofuser").text
        self.assertEqual("Welcome testmorning", welcome_text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

