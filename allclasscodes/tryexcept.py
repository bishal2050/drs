import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException


driver = webdriver.Chrome() # It will open the Edge browser
driver.maximize_window() # Maximize the browser window
driver.get("https://demoblaze.com/") # Open the Google website
try:
    try:
        nav_login_id = driver.find_element("id", "login2")  # Find the login button by its ID
        nav_login_id.click()  # Click the login button
        txt_username = driver.find_element(By.ID, "loginusername")  # Find the username input field by its ID
        txt_username.send_keys("testmorning")  # Enter the username
        txt_password = driver.find_element(By.ID, "loginpassword")  # Find the password input field by its ID
        txt_password.send_keys("test123")  # Enter the password
        btn_login = driver.find_element(By.XPATH,
                                        "//*[@id='logInModal']/div/div/div[3]/button[2]")  # Find the login button by its XPath
        btn_login.click()  # Click the login button

    except ElementNotInteractableException:
        print(f"Element not interactable:")
        driver.implicitly_wait(10)
        txt_username = driver.find_element(By.ID, "login")  # Find the username input field by its ID
        txt_username.send_keys("testmorning")  # Enter the username
        txt_password = driver.find_element(By.ID, "loginpassword")  # Find the password input field by its ID
        txt_password.send_keys("test123")  # Enter the password
        btn_login = driver.find_element(By.XPATH,
                                        "//*[@id='logInModal']/div/div/div[3]/button[2]")  # Find the login button by its XPath
        btn_login.click()  # Click the login button

except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(5) # Wait for 5 seconds to allow the login process to complete
# driver.close() # Close the browser window
driver.quit() # Quit the driver and close all associated windows