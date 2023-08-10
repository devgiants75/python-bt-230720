### 검색 결과 웹 페이지 정보 가져오기 ###

# 네이버에서 '파이썬'을 검색한 결과화면의 URL
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=파이썬

# 사용자가 서버에게 요청하는 정보들이 전달되는 구역(물음표 오른쪽)
# 검색어나 다른 조건을 웹 페이지에서 입력하는 경우 URL에 파라미터가 추가됨.
# 해당 파라미터들은 '파라미터명 = 값'(key = value)형태로 구성
# 정보가 여러 개인 경우 &를 사용하여 이어서 작성
# ?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=파이썬

# 입력한 검색어 '파이썬'은 query라는 파라미터로 전달

import requests

# 네이버 검색 URL
url = 'https://search.naver.com/search.naver'

# 검색어 파라미터 설정
params = {"query": "파이썬"}

# HTTP 헤더
# WhatIsMyBrowser 페이지에서 해당 정보 가져옴.(아래 URL 첨부)
# https://www.whatismybrowser.com/detect/what-is-my-user-agent/
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

# requests 라이브러리를 사용하여 웹 페이지 정보 가져오기
response = requests.get(url, params=params, headers=headers, timeout=10)

# requests.get()메소드의 인자 구조
# 1. url(필수): 가져올 웹페이지의 URL을 문자열로 전달
# 2. params: URL에 추가할 파라미터를 딕셔너리 형태로 전달
# 3. headers: 웹페이지 요청시 함께 전달될 HTTP 헤더를 딕셔너리 형태로 전달(User-Agent 설정 시 사용)
# 4. timeout: 요청에 대한 최대 대기 시간을 초 단위로 지정
#           지정한 시간 내에 응답이 오지 않으면 timeout 오류 발생

# 가져온 웹 페이지 정보 출력 (상태 코드 & 내용의 일부 200자 이내로 출력)
print(f'Status code: {response.status_code}')
print(response.text[:200])