# 파이썬의 기본 데이터 타입(자료형)

# 1. 숫자형: 숫자(Number)형태로 이루어진 자료형
# : 정수(integer, int)와 실수(float)
a = 1
a = -1
a = 0

a = 1.7
a = -3.14

# 16 진수: 0x로 시작하는 숫자 + (숫자 0부터 알파벳 f까지 입력 가능)
a = 0xa1b
a = 0xcab

num1 = 1
num2 = 2
print(num1 + num2)

# 2. 논리형(boolean: 불리언)
# : 참(True)과 거짓(False)의 두 개의 값만을 가지는 자료형
# : 파이썬의 예약어, 첫문자를 항상 대문자로 사용해야 한다.

bool1 = True
bool2 = False
# bool3 = true (Error)
print(type(a))
# : type이라는 키워드를 사용해 해당 변수의 자료형을 확인하는 파이썬의 내장 함수
# 출력값: <class 'int'> 변수 a의 자료형은 int이다.

# 논리형의 경우 조건문의 리턴 값으로 사용된다.
print(1 == 1)
print(2 > 1)
print(2 < 1)

print(bool1 + bool2) # 출력값 1

# 파이썬에서는 비어있는 자료형을 False로 인식: '', [], {}, ()
# 숫자 0 또한 False로 인식
# None(값이 없음)도 False로 인식

# 3. 문자열(str)
# : 문자, 단어 등으로 구성된 문자들의 집합

# 3-1. 문자열 자료형 선언 방식: 4가지
# 큰따옴표(""), 작은따옴표(''), 큰따옴표 3개 연속 표시(""""""), 작은따옴표 3개 연속 표시('''''')
sentence1 = "I'll be back"
sentence2 = '"I Like Python" she says'
sentence3 = '''
여러 줄로 문장을 표현하고 싶을 땐
따옴표 3개를 연속으로 표시합니다.
'''
print(sentence1)
print(sentence2)
print(sentence3)

# 이스케이프 코드(백 슬래시 \ 를 사용하여 표현)
# \n: 줄바꿈
# \t: 탭 간격
# \\: 문자기호 \ 그 자체를 표현
# \', \": 따옴표 그 자체를 표현

lines = "\'Python is fun\' \n I Like Python"
print(lines)

# 3-2. 문자열 자료형 연산
print(sentence1 + sentence2)
print(sentence1 * 2) # 문자열의 곱셈은 해당 문자열을 정수배 만큼 반복해서 연결

message = "I like you!"
# len(): 문자열의 길이를 구하는 파이썬 내장 함수 (length)
# 문자열의 경우 공백, 기호를 포함
print(len(message)) # 출력값: 11

# 3-3. 문자열 인덱싱과 슬라이싱
# 문자열 인덱싱(Indexing): 문자열 안의 특정한 값을 뽑아내는 역할
# 변수명[인덱스 번호]
# 문자열의 전체 인덱스 번호 == 문자열의 길이 - 1
print(message[0]) # I
print(message[5]) # e
print(message[9]) # u

# 파이썬은 0부터 숫자를 시작
# 공백 문자도 문자와 동일하게 취급
# 마이너스(-) 기호를 붙일 경우 문자열 뒤에서부터 읽는다.(마이너스의 경우 -1부터 시작)

print(message[-1]) # !
print(message[-3]) # o