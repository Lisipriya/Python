from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_drive_path = "C:\\Users\\lisipriya\Python\\Chrome\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.maximize_window()
driver.get("http://secure-retreat-92358.herokuapp.com/")
# article_num = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(article_num.text)
first_name = driver.find_element_by_name("fName")
first_name.send_keys("Priya")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Twilio")
email = driver.find_element_by_name("email")
email.send_keys("priyatwilio@gmail.com")
email.send_keys(Keys.ENTER)
driver.close()
