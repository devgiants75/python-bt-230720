# 1. 'Hello, World!'를
# 출력하는 함수를 작성
def hello_world():
    print('Hello World')
hello_world()

# 2. 주어진 두 숫자의 합을
# 반환하는 함수를 작성
def add(a, b):
    return a + b
print(add(3, 2))

# 3. 주어진 숫자 리스트의 합을
# 반환하는 함수를 작성
def sum_numbers(numbers):
    return sum(numbers)
print(sum_numbers([1, 2, 3, 4, 5]))

# 4. 이름을 인자로 받아
# 인사하는 함수를 작성
# 만약 이름이 주어지지 않은 경우,
# "Guest"라는 이름으로 인사
def greet(name="Guest"):
    print(f'Hello, {name}')
greet('Seungah')
greet()

# 가변 인자(매개변수)를 받아 평균을 반환하는 함수를 작성
# sum(), len() 내장함수 사용
def average(*args):
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5)) # 15 / 5 = 3.0