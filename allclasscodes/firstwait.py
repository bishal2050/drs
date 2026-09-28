import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # It will open the Edge browser
driver.maximize_window() # Maximize the browser window
driver.get("https://demoblaze.com/") # Open the Google website
nav_login_id = driver.find_element("id", "login2") # Find the login button by its ID
nav_login_id.click() # Click the login button
driver.implicitly_wait(10) # Wait for 10 seconds to allow the login modal to appear
# time.sleep(3) # Wait for 3 seconds to allow the login modal to appear
txt_username = driver.find_element(By.ID, "loginusername") # Find the username input field by its ID
txt_username.send_keys("testmorning") # Enter the username
txt_password = driver.find_element(By.ID, "loginpassword") # Find the password input field by its ID
txt_password.send_keys("test123") # Enter the password
btn_login = driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]") # Find the login button by its XPath
btn_login.click() # Click the login button
time.sleep(5) # Wait for 5 seconds to allow the login process to complete
# driver.close() # Close the browser window
driver.quit() # Quit the driver and close all associated windows