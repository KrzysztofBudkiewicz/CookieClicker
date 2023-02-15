from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import keyboard

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)

language_button = driver.find_element(By.ID, "langSelect-EN")
language_button.click()
time.sleep(5)

accept_cookies_button = driver.find_element(
    By.XPATH, "//a[@data-cc-event='click:dismiss']")
accept_cookies_button.click()


def click_on_cookie(num):
    big_cookie = driver.find_element(By.ID, "bigCookie")
    for i in range(num):
        big_cookie.click()


while True:
    click_on_cookie(200)
    try:
        items = driver.find_elements(By.CLASS_NAME, "enabled")
        for item in items[::-1]:
            item.click()
    except:
        print("Not enough cookies for upgrade")
    if keyboard.is_pressed("q"):
        break

driver.close()
