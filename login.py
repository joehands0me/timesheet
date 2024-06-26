from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from values import user_value, pw_value

driver = webdriver.Chrome()
driver.get("https://te.leidos.com/")
wait = WebDriverWait(driver, 10)


# Portal
# Find and input username
def portal_login():
    username = driver.find_element(By.NAME, "username")
    username.send_keys(user_value)
    print("username inputted")

# Find and input password
    password = driver.find_element(By.ID, "password")
    password.send_keys(pw_value)
    print("password inputted")

# Find and select Leidos Employee
    acc_type = driver.find_element(By.ID, "networkInputGroup")
    acc_type.send_keys("Leidos Employee")

# Select None as Token
    token = driver.find_element(By.ID, "tokenInputGroup")
    token.send_keys("none")

# Login
    sign_in = driver.find_element(By.ID, "submit")
    sign_in.click()


# Deltek
# Re-enter credentials
def deltek_login():
    dt_username = wait.until(EC.presence_of_element_located((By.ID, "USER")))
    dt_pw = wait.until(EC.presence_of_element_located(
        (By.ID, "CLIENT_PASSWORD")))
    dt_db = wait.until(EC.visibility_of_element_located(
        (By.ID, "DATABASE")))
    dt_sign_in = wait.until(EC.element_to_be_clickable(
        (By.ID, "loginBtn")))

    dt_username.send_keys(user_value)
    dt_pw.send_keys(pw_value)
    dt_db.clear()
    dt_db.send_keys("LEIDOS")
    print("Deltek credentials entered")

# driver.execute_script("startLogin();")
    dt_sign_in.click()
    print("CLICK")


def input_times():
    ack_btn = wait.until(EC.presence_of_element_located((By.ID, "ackBtn")))
    ack_btn.click()

    charge_code = wait.until(
        EC.presence_of_element_located((By.ID, "UDT02_ID-_0_E")))
    plc = wait.until(EC.presence_of_element_located((By.ID, "UDT07_ID-_0_E")))

    if charge_code.get_attribute("value"):
        print(f"Charge code: {charge_code.get_attribute("value")}")
        pass
    else:
        charge_code.send_keys("338299.CP.4.3807.01.022101L.CN")

    if plc.get_attribute("value"):
        print(f"PLC: {charge_code.get_attribute("value")}")
        pass
    else:
        pass


portal_login()
deltek_login()
input_times()


input()
