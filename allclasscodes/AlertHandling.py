import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome() # It will open the Chrome browser
driver.maximize_window() # Maximize the browser window
driver.get("https://demo.automationtesting.in/Alerts.html") # Open the Alerts demo website
nav_simple_alert = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a') # Find the simple alert navigation link by its XPath
nav_simple_alert.click() # Click the simple alert navigation link
simp_button = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button') # Find the simple alert button by its XPath
simp_button.click() # Click the simple alert button
time.sleep(2) # Wait for 2 seconds to allow the alert to appear
driver.switch_to.alert.accept() # Switch to the alert and accept it
time.sleep(3)

confirm_alert = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a') # Find the confirm alert button by its XPath
confirm_alert.click() # Click the confirm alert button
time.sleep(2) # Wait for 2 seconds to allow the alert to appear
confirm_button = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button') # Find the confirm alert button by its XPath
confirm_button.click() # Click the confirm alert button
time.sleep(2) # Wait for 2 seconds to allow the alert to appear
driver.switch_to.alert.dismiss() # Switch to the alert and dismiss it
time.sleep(5)

promp_alert = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a') # Find the prompt alert button by its XPath
promp_alert.click() # Click the prompt alert button
time.sleep(2) # Wait for 2 seconds to allow the alert to appear
prompt_button = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button') # Find
prompt_button.click() # Click the prompt alert button
time.sleep(2) # Wait for 2 seconds to allow the alert to appear
driver.switch_to.alert.send_keys("Testmorning") # Switch to the alert and enter text
driver.switch_to.alert.accept() # Switch to the alert and accept it
time.sleep(5) # Wait for 2 seconds to allow the text to be entered
