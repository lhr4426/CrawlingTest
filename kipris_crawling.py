from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 드라이버 설정 
driver = webdriver.Chrome('chromedriver.exe')
# 키프리스 열기
driver.get('http://www.kipris.or.kr/khome/main.jsp')
driver.implicitly_wait(3)

# 자동차 검색
search_box = driver.find_element(By.ID, 'inputQueryText')
search_box.send_keys('이산사건 시뮬레이션')
search_box.send_keys(Keys.RETURN)
driver.implicitly_wait(3)

# 특허실용 클릭
searchPatentBtn = driver.find_element(By.ID, 'searchPatentBtn')
searchPatentBtn.click()
time.sleep(1)

total_page = driver.find_element(By.CSS_SELECTOR, '#patentResultCountBoard').text.split()
total_page = int(total_page[4].replace(',',''))
print('total page :', total_page)


driver.find_element(By.CSS_SELECTOR, '#resultV1020180038328 > div.search_section_title > h1 > a').click()
driver.implicitly_wait(2)
driver.switch_to.window(driver.window_handles[1])

pop_up = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(pop_up)

time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR, '#divBiblioContent > div.detial_plan_info > ul > li:nth-child(11) > span > b').text)
driver.switch_to.parent_frame();
driver.close()
driver.switch_to.window(driver.window_handles[0])







# 태그가 div인 모든 요소

# is_accepted_flag = False

# for page in range(1, total_page) :
#     time.sleep(0.5)
#     elements = driver.find_elements(By.TAG_NAME, 'div')
#     for element in elements:
#         ipc_id = element.get_attribute('id')

#         # div인 요소의 id가 resultV로 시작하지 않으면 무시
#         if not ipc_id.startswith('resultV') :
#             continue

#         openDetail = driver.find_element(By.CSS_SELECTOR, f'#{ipc_id} > div.search_section_title > h1 > a')
#         openDetail.click()
#         driver.switch_to.window(driver.window_handles[-1])
#         time.sleep(1.5)
#         license_state = driver.find_element(By.CSS_SELECTOR, '#divBiblioContent > div.detial_plan_info > ul > li:nth-child(11) > span > b').text

#         if license_state.startswith("공개") or license_state.startswith("등록") :
#             is_accepted_flag = True

#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])
#         driver.implicitly_wait(1)

#         if not is_accepted_flag :
#             continue
    
#         print(ipc_id, end=' : ')
#         first_ipc = driver.find_element(By.CSS_SELECTOR, f'#{ipc_id} > div.search_basic_info > ul > li:nth-child(1) > span.point01 > a:nth-child(1)')
#         print(first_ipc.text)
#         is_accepted_flag = False

#     current_page = int(driver.find_element(By.CSS_SELECTOR,'#searchResultPaging > strong').text)
#     next_page = current_page + 1
#     driver.execute_script(f'getSearchResultPage({next_page})')
#     driver.implicitly_wait(3)
