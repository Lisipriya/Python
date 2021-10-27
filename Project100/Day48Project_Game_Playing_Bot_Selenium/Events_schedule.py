from selenium import webdriver


chrome_drive_path = "C:\\Users\\lisipriya\Python\\Chrome\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.maximize_window()
driver.get("https://www.python.org/")
# time.sleep(5)
# driver.execute_script("window.scrollTo(0, 750)")
# time.sleep(1)

times = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
names = driver.find_elements_by_css_selector('.event-widget li a')

upcoming_events = {}
for i in range(len(times)):
    upcoming_events[i] = {
        "time" : times[i].text,
        "names": names[i].text
    }
print(upcoming_events)

"""for time in times:
    print(time.text)
for name in names:
    print(name.text)"""
driver.close()
