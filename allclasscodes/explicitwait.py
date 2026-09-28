import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome() # It will open the Edge browser
driver.maximize_window() # Maximize the browser window
driver.get("https://demoblaze.com/") # Open the Google website
nav_login_id = driver.find_element("id", "login2") # Find the login button by its ID
nav_login_id.click() # Click the login button
ww = WebDriverWait(driver, 10) # Create a WebDriverWait object with a timeout of 10 seconds
txt_username = ww.until(EC.element_to_be_clickable((By.ID, "loginusername"))) # Wait until the username input field is present
# txt_username = driver.find_element(By.ID, "loginusername") # Find the username input field by its ID
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(txt_username))
txt_username.send_keys("testmorning") # Enter the username
txt_password = driver.find_element(By.ID, "loginpassword") # Find the password input field by its ID
txt_password.send_keys("test123") # Enter the password
btn_login = driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]") # Find the login button by its XPath
btn_login.click() # Click the login button
time.sleep(5) # Wait for 5 seconds to allow the login process to complete
# driver.close() # Close the browser window
driver.quit() # Quit the driver and close all associated windows