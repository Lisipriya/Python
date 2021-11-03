import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HOUSING_FIND_URL = "https://housing.com/rent/search-C8G2M1P5bp8fs9w5gm0jsim_g7khohd393v9detR3"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfzIg1rpDQ-VC3_VD3dbHdzyyAkLT2eR-88sl4WrGMc95l5Bg/viewform" \
              "?usp=sf_link "
EMAIL = "pythoncodepriya@gmail.com"
PASSWORD = "python@100priya"


response = requests.get(HOUSING_FIND_URL)
rental_response = response.text

soup = BeautifulSoup(rental_response, "html.parser")
# print(soup.prettify())

# property prices list
all_prices = soup.find_all(name="div", class_="css-1cxwewr")
all_property_prices = [tag.getText() for tag in all_prices]

# property address list
all_address = soup.find_all(name="div", class_="css-qpjd2j")
all_property_address = [tag.getText() for tag in all_address]

# property link list
all_link_elements = soup.find_all(name="a", class_="css-1ym6yxe")
# all_property_link = [tag.get("href") for tag in all_list]
all_property_link = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_property_link.append(f"https://housing.com{href}")
    else:
        all_property_link.append(href)
print(all_property_link)
# Entering values in google form using selenium
chrome_drive_path = "C:\\Users\\lisipriya\Python\\Chrome\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.maximize_window()
driver.get(GOOGLE_FORM)
time.sleep(4)
i = 0
#
while i < len(all_property_prices):
    time.sleep(4)
    # Enter price
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(all_property_prices[i])

    # Enter the address
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(all_property_address[i])

    # Enter the link
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(all_property_link[i])

    # Click on Submit
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    time.sleep(2)

    # Submit another response
    driver.find_element_by_link_text("Submit another response").click()

    i += 1
print(driver.title)
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/a/span').click()
base_window = driver.window_handles[0]
form_window = driver.window_handles[1]
driver.switch_to.window(form_window)
print(driver.title)
driver.find_element_by_link_text("Go to Google Forms").click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='username']"))).send_keys(EMAIL)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='current-password']"))).send_keys(PASSWORD)
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id=":38"]/div[2]/div[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span/div').click()
driver.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span/div/div[1]').click()

