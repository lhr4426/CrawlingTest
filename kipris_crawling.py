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
search_box.send_keys('자동차')
search_box.send_keys(Keys.RETURN)
driver.implicitly_wait(3)

# 특허실용 클릭
searchPatentBtn = driver.find_element(By.ID, 'searchPatentBtn')
searchPatentBtn.click()

# 계속 사용할 WebDriverWait 설정 (TO까지 10초, 주기 1초)
main_waiter = WebDriverWait(driver, 10, 1)
total_page_waiter = main_waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#patentResultCountBoard > em.current")))

# 총 페이지 수
total_page = driver.find_element(By.CSS_SELECTOR, '#patentResultCountBoard').text.split()
total_page = int(total_page[4].replace(',',''))
print('total page :', total_page)


# 단일 테스트

# driver.find_element(By.CSS_SELECTOR, '#resultV1020180038328 > div.search_section_title > h1 > a').click()
# driver.implicitly_wait(2)
# driver.switch_to.window(driver.window_handles[1])
# pop_up = driver.find_element(By.TAG_NAME, 'iframe')
# driver.switch_to.frame(pop_up)
# time.sleep(2)
# print(driver.find_element(By.CSS_SELECTOR, '#divBiblioContent > div.detial_plan_info > ul > li:nth-child(11) > span > b').text)
# # driver.switch_to.parent_frame();
# driver.close()
# driver.switch_to.window(driver.window_handles[0])

# 태그가 div인 모든 요소

is_accepted_flag = False # 해당 특허가 공개거나 등록인지 아닌지를 판별하기 위한 플래그
patent_name = ''

for page in range(1, total_page) :
    time.sleep(2)
    elements = driver.find_elements(By.TAG_NAME, 'div')

    for element in elements:
        ipc_id = element.get_attribute('id')

        # div인 요소의 id가 resultV로 시작하지 않으면 무시
        if not ipc_id.startswith('resultV') :
            continue
        
        driver.find_element(By.CSS_SELECTOR, f'#{ipc_id} > div.search_section_title > h1 > a').click()
        driver.implicitly_wait(2)
        driver.switch_to.window(driver.window_handles[1])

        # test 1. 로딩바가 사라지는걸 기다리기
        # loading_waiter = main_waiter.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#loadingBarBack")))

        # test 2. iframe의 존재 여부로 확인하기 (이 방법이 더 빠른듯)
        iframe = main_waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ifrmDetailArea")))

        # iframe으로 포커스 넘어가기 전에 특허 제목 뽑기
        patent_name = main_waiter.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="apttl"]')))
        patent_name = patent_name.text
        # iframe = driver.find_element(By.CSS_SELECTOR, '#ifrmDetailArea')
        driver.switch_to.frame(iframe)
        
        license_state = main_waiter.until(EC.visibility_of_element_located((By.XPATH, '//strong[contains(text(), "법적상태")]/following-sibling::span')))
        license_state = license_state.text
        
        if license_state.startswith("공개") or license_state.startswith("등록") :
            is_accepted_flag = True

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(1)

        if not is_accepted_flag :
            continue
    
        # CSV로 저장할 수 있도록
        print(ipc_id, end=',')
        print(patent_name, end=',')
        first_ipc = driver.find_element(By.CSS_SELECTOR, f'#{ipc_id} > div.search_basic_info > ul > li:nth-child(1) > span.point01 > a:nth-child(1)')
        print(first_ipc.text, end=',')
        print(license_state)
        is_accepted_flag = False

    current_page = int(driver.find_element(By.CSS_SELECTOR,'#searchResultPaging > strong').text)
    next_page = current_page + 1
    driver.execute_script(f'getSearchResultPage({next_page})')

