from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def find_country(country_code) :
    europe_list = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "ES", "FI", "FR", "GR", "GB", "HR", "HU", "IE", "IT", "LT", "LU", "LV", "MT", "NL", "SE", "SI", "SK", "PL", "PT"]
    if country_code == "US" :
        return 1
    elif country_code in europe_list :
        return 2
    elif country_code == "CN" :
        return 3
    elif country_code == "JP" :
        return 4
    elif country_code == "WO" :
        return 5

if __name__ == "__main__" :
    # 드라이버 설정 
    driver = webdriver.Chrome('chromedriver.exe')

    # 키프리스 열기
    driver.get('https://patentscope.wipo.int/search/en/search.jsf')
    driver.implicitly_wait(3)

    # 자동차 검색
    search_keyword = input("검색할 단어 입력 : ")
    print("검색 기준 국가 설정\n1. 미국\n2. 유럽\n3. 중국\n4. 일본")
    search_country = int(input())
    search_box = driver.find_element(By.ID, 'simpleSearchForm:fpSearch:input')
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)

    total_page = driver.find_element(By.XPATH, '//*[@id="resultListCommandsForm:invalidPageNumber"]/span').text.split()
    total_page = int(total_page[2].replace(',',''))
    # print(current_page)
    print(total_page)

    main_waiter = WebDriverWait(driver, 10, 1)

    # //*[@id="resultListCommandsForm:j_idt1952"]

    for page in range(1, 100) :
        time.sleep(1.5)
        loading_waiter = main_waiter.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="pageBlockUI_blocker"]')))
        result_patents = driver.find_elements(By.XPATH, '//*[@id="resultListForm:resultTable_data"]/tr')

        for result in result_patents :
            patent_code = result.get_attribute("data-rk")
            find_code = find_country(patent_code[:2])
            if find_code == search_country or find_code == 5 :
                print(driver.find_element(By.XPATH,f'//tr[@data-rk="{patent_code}"]/descendant::span[@class="notranslate ps-patent-result--title--patent-number"]').text, end=',')
                print(driver.find_element(By.XPATH,f'//tr[@data-rk="{patent_code}"]/descendant::span[@class="trans-section needTranslation-biblio"]').text, end=',')
                print(driver.find_element(By.XPATH,f'//tr[@data-rk="{patent_code}"]/descendant::span[@class="ps-field--value ps-patent-result--ipc notranslate"]/span[position()=1]').text)

                

        next_page = main_waiter.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultListCommandsForm"]/div/div[2]/*[position()=3]')))
        next_page.click()    

