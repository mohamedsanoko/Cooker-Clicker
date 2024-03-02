from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

current_time = time.time()
multiplication_factor = 1
# Every 5 seconds we get a hold of the money

store_iterator = 1
element_to_buy_number = 1
while True:
    cookie.click()
    if time.time() - current_time >= 5 * multiplication_factor:
        money = int(driver.find_element(By.ID, value="money").text)
        multiplication_factor += 1
        # Looping through the store to find the most expensive item we can buy
        for store_iterator in range(1, 9):
            store_element_price = driver.find_element(By.XPATH, value=f"/html/body/div[3]/div[5]/div/div[{store_iterator}]/b").text.split("-")[1].strip()
            store_element_price = store_element_price.replace(",", "")
            store_element_price = int(store_element_price)
            if money > store_element_price:
                element_to_buy_number = store_iterator
            else:
                break
        store_element_to_buy = driver.find_element(By.XPATH, value=f"/html/body/div[3]/div[5]/div/div[{element_to_buy_number}]")
        store_element_to_buy.click()

    if multiplication_factor >= 60:
        break

cookie_per_seconds = driver.find_element(By.ID, value="cps").text
print(f"cookies/seconds: {cookie_per_seconds}")

driver.close()


