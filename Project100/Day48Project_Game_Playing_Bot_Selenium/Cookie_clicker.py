import time
from selenium import webdriver


chrome_drive_path = "C:\\Users\\lisipriya\Python\\Chrome\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.maximize_window()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element_by_id("cookie")
five_min_timer = time.time() + 60*5  # 5 minutes from now
five_sec_timer = time.time() + 5    # 5 seconds from now

#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()
    if time.time() > five_sec_timer:
        item_prices = []
        prices = driver.find_elements_by_css_selector("#store b")

        # Convert <b> text into an integer price.
        for price in prices:
            element_text = price.text
            if element_text != "":
                price_value = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(price_value)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        five_sec_timer = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min_timer:
        cookie_per_sec = driver.find_element_by_id("cps").text
        print(cookie_per_sec)
        break

driver.close()


