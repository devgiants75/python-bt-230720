#? 2-1. find()메소드
# : 지정된 태그들 중에서 가장 첫 번째 태그만 가져오는 메소드
# : 일반적으로 하나의 태그만 존재하는 경우에 사용

import requests
from bs4 import BeautifulSoup

url = 'https://www.giantsclub.com/html/?pcode=257'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# find: 조건에 맞는 첫 번째 태그만 반환
# 태그 전체 반환
a_tag = soup.find('a')
print(a_tag.text)

a_tag_href = soup.find('a').get('href')
print(a_tag_href)

# 태그 내용 반환: soup.find('a').text
# 태그 속성값: soup.find('a').get('href')
