import re

text = '''
침해대응실습+네트워크일반+네트워크분석실습+컴퓨터구조+네트워크구축실습+JAVA언어실습+기초 운영체제실습+정보보호관리체계+통합보안실습+Linux 서버구축실습+클라우드보안실습+네트워크 분석+사물인터넷보안실습+현장실습+컴퓨터운영체제+정보통신개론+프로젝트실습+모의해킹실습+기초 C언어실습+DBMS보안실습+빅데이터컴퓨팅+정보보안기술+정보보호개론+사이버침해개론+집중수업+사이버보안관제실습+악성코드분석실습+Linux 체제실습+클라우드서버구축실습+양자암호통신+데이터베이스 보안

'''

# result = text.replace(' ', '')
# print(result)

# text_mod = re.sub('^([0-9]{10}_)([0-9]{2})v[0-9](\.[0-9])?$',r'\2',text,flags=re.MULTILINE)

# text_mod = re.findall('^([가-힣I]+)$',text,flags=re.MULTILINE)

# year_list = []

# print(text_mod)
# print(type(text_mod))
# year_list = text_mod.split()
# print(year_list)

# print("max : ", max(year_list))
# print("min : ", min(year_list))

items = text.split('+')
for item in items :
    print(item)