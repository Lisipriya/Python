from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "priyatwilio@gmail.com"
ACCOUNT_PASSWORD = "priyatwilio"

chrome_drive_path = "C:\\Users\\lisipriya\Python\\Chrome\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in = driver.find_element_by_css_selector(".join-form button")
sign_in.click()

#Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element_by_id("session_key")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("session_password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)