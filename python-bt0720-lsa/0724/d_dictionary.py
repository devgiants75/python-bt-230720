### 딕셔너리 자료형 ###
# 키(key)와 값(value)의 쌍을 항목으로 가지는 자료형
# 중괄호{}로 표현, 각 항목은 콜론(:)으로 키와 값을 구분
# 키(key)를 통해 요솟값을 빠르게 검색 가능

# 변경 가능 O, 키는 중복 X, 값은 중복 O

# 1. Dictionary 생성
dict1 = {} # 빈 딕셔너리
dict2 = {'name': 'Jun Gook', 'age': 29, 'city': 'Busan'}
dict3 = dict(name='Jun Gook', age=29, city='Busan') # dict 함수를 이용한 딕셔너리

# 2. 키를 사용해 값에 접근
dict = {'name': 'Jun Gook', 'age': 28, 'city': 'Busan'}
print(dict['name']) # 출력: Jun Gook

# 3. Dictionary에 항목 추가/수정/삭제
dict['age'] = 29 # 기존 키의 값을 수정
dict['country'] = 'Korea' # 새로운 키와 값을 추가
print(dict)

del dict['country'] # 키 'country'의 항목 삭제
print(dict)

# 파이썬 교재 p.46 딕셔너리 내장 함수