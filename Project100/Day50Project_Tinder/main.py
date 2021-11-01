import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

EMAIL = "pythoncodepriya@gmail.com"
PASSWORD = "python@100priya"

chrome_drive_path = "C:\\Users\\lisipriya\Python\\Chrome\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.maximize_window()
driver.get("https://tinder.com/")

time.sleep(2)
accept_all = driver.find_element_by_xpath('//*[@id="s-1736306725"]/div/div[2]/div/div/div[1]/button').click()
# Log in button
driver.find_element_by_xpath('//*[@id="s-1736306725"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div['
                             '2]/div[2]/a').click()
time.sleep(2)

# Log in with facebook
login_fb = driver.find_element_by_xpath('//*[@id="s-1514966289"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_fb.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# switching to fb login window
driver.switch_to.window(fb_login_window)
print(driver.title)

# email
driver.find_element_by_id("email").send_keys(EMAIL)

# password
password = driver.find_element_by_id("pass")
password.send_keys(PASSWORD)

# login
password.send_keys(Keys.ENTER)

# Switching back to tinder page
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
current_url = driver.current_url
print(current_url)


if current_url == "https://tinder.com/":
    login_fb.click()
    time.sleep(3)


# allow location
driver.find_element_by_xpath('//*[@id="s-1514966289"]/div/div/div/div/div[3]/button[1]').click()

# disable notification
driver.find_element_by_xpath('//*[@id="s-1514966289"]/div/div/div/div/div[3]/button[2]').click()

# time.sleep(5)
# click on like button
# like_button = driver.find_element_by_xpath('//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
actions = ActionChains(driver)
while range(0, 100):
    try:
        # like_button.click()
        time.sleep(5)
        # actions.send_keys(Keys.ARROW_LEFT)
        like_button = driver.find_element_by_xpath(
            '//*[@id="s-1736306725"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()
        time.sleep(2)
    except NoSuchElementException:
        time.sleep(4)
        actions.send_keys(Keys.ARROW_LEFT)




