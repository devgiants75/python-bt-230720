#? 2-3. class 속성 활용
# 공통적인 특징을 갖는 태그들은 같은 class 속성값으로 묶어줄 수 있다.
# find, find_all 메소드 모두 동일하게 사용 가능
# 클래스 이름으로 요소를 찾을 때: 'class_' 파라미터를 사용

# 태그: soup.find_all('div', class_='top_menu')
# 태그 내용: soup.find_all('div', class_='top_menu')[0].text
# 태그 내용: soup.find_all('div', class_='top_menu')[1].text

import requests
from bs4 import BeautifulSoup

url = 'https://www.giantsclub.com/html/?pcode=257'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 클래스 이름으로 요소를 찾을 때는 class_ 파라미터를 사용
class_elements = soup.find_all(class_='top_menu')
for element in class_elements:
    print(element.text)