from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.support.ui import WebDriverWait
from selenium.webdriver.common.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://te.leidos.com/")

# Portal
# Find and input username
username = driver.find_element(By.CLASS_NAME, "form-control")
username.send_keys("$username")

# Find and input password
password = driver.find_element(By.ID, "password")
password.send_keys("$password")

# Find and select Leidos Employee
acc_type = driver.find_element(By.ID, "networkInputGroup")
acc_type.send_keys("Leidos Employee")

# Select None as Token
token = driver.find_element(By.ID, "tokenInputGroup")
token.send_keys("none")

# Login
sign_in = driver.find_element(By.ID, "submit")
token.send_keys("")

# Deltek
# Re-enter credentials
