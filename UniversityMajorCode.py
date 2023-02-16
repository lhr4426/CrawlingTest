import requests, bs4
import json
import xml.etree.ElementTree as ET
from xml_to_dict import XMLtoDict

file_path = "api_keys.json"
my_key = ""

with open(file_path, "r") as json_file :
    json_data = json.load(json_file)
    my_key = json_data['decode'].encode("utf-8")

url = 'http://openapi.academyinfo.go.kr/openapi/service/rest/BasicInformationService/getUniversityMajorCode'
params ={'serviceKey' : my_key, 'pageNo' : '1', 'numOfRows' : '10', 'svyYr' : '2022', 'schlId' : '0000149', 'schlMjrId' : '0012796' }

response = requests.get(url, params=params)
result = bs4.BeautifulSoup(response.content, 'xml')

xd = XMLtoDict()
all_data = xd.parse(response.content)['response']['body']['items']['item']
print(all_data)

print(all_data['korSchlNm'])
print(all_data['korMjrNm'])
print(all_data['korSrsLclftNm'])
print(all_data['korSrsMclftNm'])
print(all_data['korSrsSclftNm'])



