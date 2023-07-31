### 메소드 ###

# 특정한 객체를 통해서만 호출할 수 있는 함수를 메소드

# 문자열 메소드

# 1. format() 메소드: 문자열에 변수를 삽입 or 형식을 지정하는데 사용
print('Hello, {}. I am {} years old'.format('seungah', 50))

# 2. count() 메소드: 특정 문자나 문자열이 등장하는 횟수를 세는 데 사용
print('Hello, python'.count('o')) # 2

# 3. find() 메소드: 특정 문자나 문자열이 처음 등장하는 인덱스를 반환
# 찾고자 하는 문자나 문자열이 없는 경우 -1을 반환
print('Hello, python'.find('o')) # 4
print('Hello, python'.find('w')) # -1

# 4. index() 메소드: 특정 문자나 문자열이 처음 등장하는 인덱스를 반환
# 찾고자 하는 문자나 문자열이 없는 경우 ValueError가 발생
print('Hello, python'.index('o')) # 4
# print('Hello, python'.index('w')) # Error

# 5. 대소문자 변환 메소드
print('hello, python'.upper()) # 모든 소문자를 대문자로 변환
print('HELLO, PYTHON'.lower()) # 모든 대문자를 소문자로 변환
print('hello, python'.capitalize()) # 첫 글자만 대문자, 나머지 소문자 변환
print('hello, python'.title()) # 각 단어의 첫 글자를 대문자, 나머지 소문자 변환

# 6. join() 메소드: 문자열 리스트를 하나로 합쳐 하나의 문자열로 변환
print(', '.join(['apple', 'orange', 'banana']))

# 7. split() 메소드: 문자열을 특정 문자를 기준으로 분리하여 리스트를 생성
print('apple, orange, banana'.split(', '))

# 8. replace(): 특정 문자나 문자열을 다른 문자나 문자열로 교체
print('Hello, World'.replace('World', 'Python'))

# 9. 불필요한 문자열 제거 메소드
print('   Hello   '.strip()) # 문자열 양쪽 끝의 공백 및 다른 특정 문자를 제거
print('   Hello   '.lstrip())
print('   Hello   '.rstrip())