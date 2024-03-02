from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

current_time = time.time()
multiplication_factor = 1
# Every 5 seconds we get a hold of the money
while True:
    cookie.click()

    if time.time() - current_time >= 5 * multiplication_factor:
        money = driver.find_element(By.ID, value="money").text
        print(money)
        multiplication_factor += 1




