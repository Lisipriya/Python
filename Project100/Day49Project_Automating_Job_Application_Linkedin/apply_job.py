import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

EMAIL = "priyatwilio@gmail.com"
Password = "priyatwilio"
keywords = "python developer"
location = "London, England, United Kingdom"

chrome_drive_path = "C:\\Users\\lisipriya\Python\\Chrome\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.maximize_window()
driver.get("https://www.linkedin.com/")

time.sleep(2)
email = driver.find_element_by_id("session_key")
email.send_keys(EMAIL)
pwd = driver.find_element_by_id("session_password")
pwd.send_keys(Password, Keys.ENTER)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom")
time.sleep(2)
# apply_button = driver.find_element_by_xpath('//*[@id="ember987"]')
# apply_button.click()
#
# driver.find_element_by_css_selector(".display-flex input").send_keys("1234567890")

jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")

# For each job in the jobs list, click the Save button,
# scroll down to the bottom of the right hand pane and then click the Follow button.

for job in jobs:

    if "Fintern" in job.text:
        job.click()
        time.sleep(4)
        try:
            apply_button = driver.find_element_by_class_name("jobs-apply-button")
            apply_button.click()
            phone = driver.find_element_by_css_selector(".display-flex input")
            if phone.text == "":
                phone.send_keys("1234567890")
            submit_button = driver.find_element_by_css_selector("footer button")
            # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
                print("Complex application, skipped.")
                continue
            else:
                submit_button.click()

            # Once application completed, close the pop-up window.
            time.sleep(2)
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

        # If already applied to job or job is no longer accepting applications, then skip.
        except NoSuchElementException:
            print("No application button, skipped.")
            continue

time.sleep(5)
        # driver.find_element_by_css_selector(".display-flex button").click()
        # driver.find_element_by_xpath("//span[contains(@class, 'artdeco-button__text') and text()='Next']").click()
        # driver.find_element_by_xpath("//span[contains(@class, 'artdeco-button__text') and text()='Review']").click()
        # driver.find_element_by_css_selector(".display-flex input").send_keys("1")
        # driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:('
        #                              'urn:li:fs_normalized_jobPosting:2770759961,36091762,multipleChoice)"]').click()
        # driver.find_element_by_xpath("//option[@value='No']").click()
        # driver.find_element_by_xpath("//span[contains(@class, 'artdeco-button__text') and text()='Review']").click()
    # Submit
    # submit_application = driver.find_elements_by_tag_name("button")[5]
    # submit_application.click()
# driver.quit()
