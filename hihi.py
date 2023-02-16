from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


print("검색할 내용")
question = input()

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get('https://www.onetonline.org/')
driver.implicitly_wait(3)

search_box = driver.find_element(By.CSS_SELECTOR, '#headersearchlg')
search_box.send_keys(question)
search_box.send_keys(Keys.RETURN)

items = driver.find_elements(By.CSS_SELECTOR, "#content > table > tbody > tr:nth-child(-n+3) > td:nth-child(2) > a:nth-child(2)")

print("검색 :", question)
for item in items :
    print(item.text)