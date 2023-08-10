### 웹 페이지 분석 및 추출하기 ###

# cmd(명령 프롬프트) & vsc(터미널 창)에서 bs4 라이브러리 설치
# pip install beautifulSoup4

#! 1. BeautifulSoup 객체 생성 기본 방법

import requests
from bs4 import BeautifulSoup

url = '검색 대상 URL'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#! 2. BeautifulSoup 메소드 사용
# 각각의 다른 모듈(.py)에서 사용법 작성