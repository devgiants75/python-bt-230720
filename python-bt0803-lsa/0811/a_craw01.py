# BeautifulSoup 외부 패키지 설치
# cmd(명령 프롬프트)
# : pip install beautifulSoup4 / pip install bs4
# : pip list (설치 확인)

# vsc 터미널(ctrl + shift + `) 
# : pip install beautifulSoup4

# find()메소드 사용 - 웹 페이지 분석 및 추출
import requests
from bs4 import BeautifulSoup

url = 'https://www.giantsclub.com/html/?pcode=855'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# find(): 조건에 맞는 첫 번째 태그만 반환
# id로 요소를 찾을 때는 id 파라미터를 사용
id_element = soup.find(id='skipArea')
print(id_element)
print(id_element.text)