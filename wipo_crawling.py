from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 드라이버 설정 
driver = webdriver.Chrome('chromedriver.exe')

# 키프리스 열기
driver.get('https://patentscope.wipo.int/search/en/search.jsf')
driver.implicitly_wait(3)

# 자동차 검색
search_box = driver.find_element(By.ID, 'simpleSearchForm:fpSearch:input')
search_box.send_keys('car')
search_box.send_keys(Keys.RETURN)
driver.implicitly_wait(3)

result_patents = driver.find_elements(By.XPATH, '//*[@id="resultListForm:resultTable_data"]/tr')

for result in result_patents :
    print(result.get_attribute("data-rk"))

current_page = int(driver.find_element(By.XPATH, '//*[@id="resultListCommandsForm:pageNumber"]').text)
total_page = driver.find_element(By.XPATH, '//*[@id="resultListCommandsForm:invalidPageNumber"]/span').text.split()
total_page = int(total_page[2].replace(',',''))
# print(current_page)
print(total_page)

main_waiter = WebDriverWait(driver, 10, 1)

while current_page != total_page :
    next_page_btn = main_waiter.until(EC.presence_of_element_located((By.XPATH, '//*[@id="resultListForm:j_idt2200"]')))
    next_page_btn.click()
    current_page = current_page + 1
    time.sleep(1)




while True :
    continue
