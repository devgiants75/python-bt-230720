### 웹 크롤링: 웹 페이지 정보 가져오기 ###

# 네이버 메인 페이지의 전체 소스코드를 가져오기
# https://www.naver.com

# requests: 웹 페이지의 정보를 가져오기
# BeautifulSoup: 원하는 정보만을 가져오기

import requests

# 네이버 웹 페이지 URL
url = 'https://www.naver.com'

# HTTP GET 요청을 통해 웹 페이지 정보 가져오기
response = requests.get(url)

# HTTP 응답 상태 코드 출력 (200이면 성공)
print("Status Code : ", response.status_code)

# 웹 페이지의 내용 출력
print(response.text)

# pip install requests