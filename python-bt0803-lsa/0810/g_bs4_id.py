#? 2-4. id 속성 활용
# : 같은 웹 페이지에서 같은 id 속성값을 가진 태그는 존재하지 X
# : 특정 id 속성값을 가진 태그는 오직 하나
# : find 메소드와 함께 사용

# 태그: soup.find('div', id='skipArea')
# 태그 내용: soup.find('div', id='skipArea').text

import requests
from bs4 import BeautifulSoup

url = 'https://www.giantsclub.com/html/?pcode=257'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# id로 요소를 찾을 때는 id 파라미터를 사용
id_element = soup.find(id='skipArea')
print(id_element)
print(id_element.text)