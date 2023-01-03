from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com/')
driver.implicitly_wait(3)

cafe = driver.find_element(By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[2]')
print(cafe.text)

test = driver.find_element(By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[@class="nav_item"]/a[@data-clk="svc.blog"]')
print(test.text)

test2 = driver.find_element(By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[2]/following-sibling::a[@data-clk="svc.more"]')
print(test2.text)

while True :
    continue