import requests
import json
import pandas as pd

file_path = "api_keys.json"
my_key = ""

# ncs 대분류 리스트 (01 ~ 24)
ncsLclasCd_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']

# 내 api key 가져오기
with open(file_path, "r") as json_file :
    json_data = json.load(json_file)
    my_key = json_data["ncs"]

# 요청주소
url = 'http://apis.data.go.kr/B490007/ncsEduCource/openapi20'

# 모든 데이터를 저장하기
all_data = []

# 열 이름 만들기 (pandas에 쓸거임)
col_name = ['대분류명', '중분류명', '소분류명', '세분류명', '학과명', '과목명']

# 대분류 돌기 
for ncsLclascd in ncsLclasCd_list :
    # 페이지 초기화
    page_number = 1

    # 페이지 돌기
    while True :
        # 파라미터를 변경하기
        params ={'serviceKey' : 'NhC/Ogm81bAqynbgwtFbRfZESnH3/PsjF8RqxKIvooWfOrW5fVpRJB+p7q6cFn8rpcEOapTpDvgq4KHUqjn3nA==', 'pageNo' : str(page_number), 'numOfRows' : '100', 'returnType' : 'json', 'ncsLclasCd' : ncsLclascd }

        # 페이지에 request
        response = requests.get(url, params=params)

        # json파일을 dict로 가져오기
        datainfo = json.loads(response.text)['dataInfo']['code']

        # 데이터 코드가 000이면 정상 작동된 것. 아닐 시 반복문 탈출
        if datainfo != '000' :
            break
        else :    
            data = json.loads(response.text)['data']
            
            # 데이터의 길이만큼 돌기 
            # 열 이름에 맞게 데이터 가져옴
            for i in range(len(data)) :
                temp = []
                temp.append(data[i]['ncsLclasCdnm'])
                temp.append(data[i]['ncsMclasCdnm'])
                temp.append(data[i]['ncsSclasCdnm'])
                temp.append(data[i]['ncsSubdCdnm'])
                temp.append(data[i]['depttName'])
                temp.append(data[i]['asubjName'])
                all_data.append(temp)
            
            # 다음 페이지로
            page_number = page_number + 1

# 모든 데이터를 데이터프레임으로 변경
df = pd.DataFrame(all_data, columns=col_name)
print(df)

# 데이터프레임을 엑셀로 가공
address = "C:\\HyerimLee\\gitclones\\MakeSomething\\result\\"
df.to_excel(excel_writer=address+"ncs_api_test.xlsx")
