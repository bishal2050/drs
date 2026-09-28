import unittest
from pathlib import Path

from ddt import data, ddt
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from utilities.csv_reader import read_csv_data


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEST_DATA_PATH = PROJECT_ROOT / "testdata" / "login_data.csv"
LOGIN_TEST_CASES = read_csv_data(
    TEST_DATA_PATH,
    ("username", "password", "result_type", "expected_result"),
)


@ddt
class MyTestCase(unittest.TestCase):
    @data(*LOGIN_TEST_CASES)
    def test_login(self, test_case):
        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get("https://demoblaze.com/")
            login_page = LoginPage(driver)
            login_page.login_function(
                test_case["username"],
                test_case["password"],
            )

            if test_case["result_type"] == "welcome":
                actual_result = driver.find_element(By.ID, "nameofuser").text
            elif test_case["result_type"] == "alert":
                alert = driver.switch_to.alert
                actual_result = alert.text
                alert.accept()
            else:
                self.fail(f"Unsupported result_type: {test_case['result_type']}")

            self.assertEqual(test_case["expected_result"], actual_result)
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()
