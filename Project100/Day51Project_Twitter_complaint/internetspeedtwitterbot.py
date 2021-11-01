from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PROMISED_DOWN = 325
PROMISED_UP = 35
TWITTER_EMAIL = "pythoncodepriya@gmail.com"
TWITTER_USERNAME = "@pythoncodepriya"
TWITTER_PASSWORD = "Twitterbot"


class InternetSpeedTwitterBot:
    def __init__(self, chrome_drive_path):
        self.driver = webdriver.Chrome(executable_path=chrome_drive_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]') \
            .click()
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Back to test "
                                                                                                    "results")))
        self.driver.find_element_by_partial_link_text("Back to test results").click()
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.tweet_at_provider(self.down, self.up)
        self.driver.close()

    def tweet_at_provider(self, down, up):
        self.driver.get("https://twitter.com/home")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='username']"))).send_keys(TWITTER_EMAIL)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                          '2]/div[2]/div[2]/div/div').click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='on']"))).send_keys(TWITTER_USERNAME)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                          '2]/div[2]/div[2]/div/div').click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='current-password']"))).send_keys(
            TWITTER_PASSWORD)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                          '2]/div[2]/div[2]/div/div/span/span').click()
        message = f"Hey internet provider why is my internet speed is {down}down/{up}up when I pay for " \
                  f"{PROMISED_DOWN}down/{PROMISED_UP}up? "
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root'))).click()

        element = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
        ActionChains(self.driver).move_to_element(element).send_keys(f"""{message}""").perform()

        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                          '2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div['
                                          '3]/div/span/span').click()
