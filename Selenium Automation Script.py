from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://safora.se/en/")

driver.maximize_window()


time.sleep(3)


contact_link = driver.find_element(By.LINK_TEXT, "Contact")
contact_link.click()

time.sleep(2)


name = driver.find_element(By.NAME, "name")
email = driver.find_element(By.NAME, "email")
message = driver.find_element(By.NAME, "message")

name.send_keys("Test User")
email.send_keys("testuser@gmail.com")
message.send_keys("This is an automation test message.")


submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

time.sleep(3)


page_source = driver.page_source

if "Thank you" in page_source or "success" in page_source:
    print("Test Passed - Form submitted successfully")
else:
    print("Test Failed")

driver.quit()