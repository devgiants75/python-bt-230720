### 네이버 웹툰 페이지 - 실시간 인기 웹툰 ###

# 라이브러리
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://comic.naver.com/index'

# 엑셀 파일로 저장하기
fileName = 'naver_webtoon.csv'
f = open(fileName, 'w', encoding='utf-8', newline="")
writer = csv.writer(f)

# 컬럼 속성명
columns_name = ['순위', '웹툰명']

writer.writerow(columns_name)

# 웹 서버에 요청하기
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')
# 전체 영역에서 'class_='text'를 찾지 않고
# 실시간 인기 웹툰 영역으로 범위 제한
cartoonsBox = soup.find('div', attrs={'class': 'component_wrap'})

# 실시간 인기 웹툰 영역에서 class명이 text인 값을 모두 가져와서 cartoons 변수에 할당
cartoons =  cartoonsBox.find_all(class_='text')
