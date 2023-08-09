### 웹 크롤링 준비(환경설정) ###

#! 1. 크롬 설치
# 웹 크롤링은 크롬, 파이어폭스, 사파리 등 다양한 웹 브라우저에서 가능
# 크롬에 있는 '개발자 도구'를 이용하여 크롤링 수행 시 필요한 정보 확인
# 마이크로소프트 엣지(개발자 도구), 파이어폭스(파이어버그)

#! 2. requests 라이브러리 설치
# : 사용자가 서버에 요청하는 request를 용이하게 수행하는 라이브러리
# : 명령 프롬프트(cmd)창에서 확인
# : pip install requests (requests 설치 명령어)
# : pip list (requests 버전 확인)

# 파이썬 표준 라이브러리 요청을 처리하기 위해 urllib라는 패키지가 존재
# 하지만 사용법이 requests보다 어려움

#! 3. BeautifulSoup 패키지 설치
# : 구문을 분석해서 필요한 내용만 추출할 수 있는 기능을 가진 외부 패키지
# : 명령 프롬프트(cmd)창에서 확인
# : pip install BeautifulSoup4 (BeautifulSoup4 설치 명령어)
# : pip list (BeautifulSoup4 버전 확인)

#! 4. 크롬 개발자 도구 사용
# 웹 페이지에서 오른쪽 마우스 클릭 - '검사' 선택
# 개발자 도구의 'Elements'탭을 사용 - 웹 페이지의 HTML 구조 확인 가능
