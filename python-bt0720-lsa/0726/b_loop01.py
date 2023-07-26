### 반복문(Loop) ###

# 특정 코드를 여러 번 실행하도록 프로그램에 지시하는 프로그래밍 구조
# 반복문의 종류: for, while

# 1. For반복문 사용법
# : 주로 시퀀스(리스트, 튜플, 문자열 등)나 다른 반복 가능한 객체를 순회하는데 사용
'''
for 변수 in 시퀀스:
    반복할 코드

# 변수는 시퀀스의 각 요소를 참조
# 반복할 코드는 시퀀스의 각 요소에 대해 한 번씩 실행된다
'''

# 리스트의 모든! 요소를 출력하는 for문
fruits = ['apple', 'mange', 'orange']

for fruit in fruits:
    print(fruit)

# 2. range()함수와 For문
# range()함수와 함께 for문을 사용할 경우 특정 횟수만큼 반복 가능
# range()함수는 숫자 시퀀스를 생성
'''
for i in range(횟수):
    반복할 코드

# i : 현재의 반복 횟수를 참조
'''

# 5번 반복하여 숫자를 출력하는 for문
for i in range(5):
    print(i)

# 시작 값, 종료 값, 스텝 값을 지정 가능: range(시작 값, 종료 값, 스텝 값)
# 1부터 10까지 2씩 증가하는 숫자를 출력
for i in range(1, 10, 2):
    print(i)

# 3.리스트, 튜플, 딕셔너리와 For문

# 3-1. 리스트
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# 3-2. 튜플
languages = ('python', 'java', 'c++')

for language in languages:
    print(language)

# 3-3. 딕셔너리
fruitColors = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

for fruit, color in fruitColors.items():
    print(f'The color of {fruit} is {color}.')

# items()메서드는 딕셔너리의 모든 키-값 쌍을 반환하는 메서드
# 키: keys()
# 값: values()

# 4. 중첩 For문

# 4-1. 기본적인 중첩 for문
'''
for 변수1 in 외부시퀀스:
    for 변수2 in 내부시퀀스:
        반복할 코드
'''

# 2차원 리스트
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in matrix:
#     for number in row:
#         print(number)

# 5. for문과 조건문의 결합
for row in matrix:
    for number in row:
        if number > 5:
            print(number)

