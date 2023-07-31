### 매개변수 ###

# 1. 매개변수의 정의
# : 함수가 호출될 때 함수에 전달되는 값들을 받아내는 역할
def greet(name): # name: 매개변수
    print(f'hello, {name}!')

greet('이승아') # '이승아': 인수

# 2. 위치 매개변수: 함수를 호출할 때 전달된 인수의 순서대로 매개변수에 대입
def info(name, age):
    print(f'I am {name} and I am {age} years old.')

info(50, 'seungah')

# 3. 기본(디폴드 default) 매개변수
def greet(name="Python"):
    print(f'Hello {name}')

greet('이승아')
greet()

# 4. 키워드 매개변수
# : 인수의 순서를 무시하고 직접 매개변수에 값을 지정
def info(name, age):
    print(f'{name}, {age}')
info(age=50, name='이승아')

# 5. 가변 매개변수
# : 개수가 정해지지 않은 인수를 받는 매개변수
# : 일반 매개변수 앞에 *를 붙여 표시
def add(*numbers):
    return sum(numbers) # 가변 매개변수는 함수 내에서 튜플로 취급

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

