import requests
from bs4 import BeautifulSoup

url = 'https://shopping.naver.com/home'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title.get_text())

else :
    print(response.status_code)
