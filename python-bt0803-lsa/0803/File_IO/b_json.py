### JSON 파일 입출력 ###

# JSON 파일
# : JavaScript Object Notation의 약자
# : 키-값 쌍으로 이루어진 데이터 (파이썬의 딕셔너리 데이터타입)

# 파이썬에서 JSON 파일 생성
# json 모듈 사용 - dump 함수
# : Python 객체를 JSON 문자열로 변환하고 파일에 저장
# json.dump(데이터, 데이터를 담을 파일 객체)

import json

data = {
    "이름":"이승아",
    "나이":50,
    "직업":"개발자"
}

with open('data.json', 'w') as file:
    json.dump(data, file)

# JSON 파일 읽기
# json 모듈의 load 함수

with open('data.json', 'r') as file:
    data = json.load(file)
print(data)