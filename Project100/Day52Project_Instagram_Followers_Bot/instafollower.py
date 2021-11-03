import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INSTAGRAM_USERNAME = " "
INSTAGRAM_PASSWORD = " "
SIMILAR_ACCOUNT = ""


class InstaFollower:
    def __init__(self, chrome_drive_path):
        self.driver = webdriver.Chrome(executable_path=chrome_drive_path)
        pass

    def login(self):
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/")
        # username
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(INSTAGRAM_USERNAME)
        # password
        self.driver.find_element_by_name("password").send_keys(INSTAGRAM_PASSWORD)
        # login
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(3)
        # save password info (Not now)
        self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        time.sleep(5)
        # notification alert (Not now)
        self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        self.driver.find_element_by_partial_link_text(" followers").click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):

        follow_List = self.driver.find_elements_by_css_selector("li button")
        print("fList len is {}".format(len(follow_List)))

        for follow in follow_List:
            try:
                follow.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]').click()
                time.sleep(1)

    def log_out(self):
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="f2ccedcaa080c28"]/div/div/div').click()
        drp_element = self.driver.find_element_by_xpath("//*[text()='Log Out']")
        action = ActionChains(self.driver)
        action.click(on_element=drp_element).perform()
        self.driver.close()

