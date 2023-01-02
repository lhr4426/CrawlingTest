from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 드라이버 설정 
driver = webdriver.Chrome('chromedriver.exe')
# 키프리스 열기
driver.get('http://www.kipris.or.kr/khome/main.jsp')
time.sleep(1)

# 자동차 검색
search_box = driver.find_element(By.ID, 'inputQueryText')
search_box.send_keys('자동차')
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# 특허실용 클릭
searchPatentBtn = driver.find_element(By.ID, 'searchPatentBtn')
searchPatentBtn.click()
time.sleep(2)

# 태그가 div인 모든 요소
elements = driver.find_elements(By.TAG_NAME, 'div')

for element in elements:
    ipc_id = element.get_attribute('id')

    # div인 요소의 id가 resultV로 시작하지 않으면 무시
    if not ipc_id.startswith('resultV') :
        continue
    
    print(ipc_id, end=' : ')
    first_ipc = driver.find_element(By.CSS_SELECTOR, f'#{ipc_id} > div.search_basic_info > ul > li:nth-child(1) > span.point01 > a:nth-child(1)')
    print(first_ipc.text)
