#? 2-2. find_all()메소드
# : 지정한 태그들을 모두 가져오는 메소드
# : 가져온 태그들은 모두 리스트에 보관(리스트 형태로 반환)

# 태그: soup.find_all('li')
# 태그 내용: soup.find_all('li')[0].text
# 태그 내용: soup.find_all('li')[1].text
# 태그 속성값: soup.find_all('li')[0].get('id')

import requests
from bs4 import BeautifulSoup

url = 'https://www.giantsclub.com/html/?pcode=257'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# find_all(): 조건에 맞는 모든 태그를 리스트 형태로 반환
# 모든 <span> 태그를 찾아오기
span_tag = soup.find_all('span')
for tag in span_tag:
    print(tag.text)
