### 반환 값(return) ###

# 1. 반환 값
# : 함수에서 결과를 반환하는 역할
# : 함수의 실행을 즉시 종료, return문 뒤에 오는 값을 호출자에게 반환

# 두 숫자를 더한 결과를 반환하는 함수
def add(a, b):
    result = a + b
    return result

sum = add(5, 3)
print(sum)

# 2. 여러 값 반환(다중 반환)
# : 하나의 return문을 사용하여 여러 값을 반환 가능
# : 여러 반환 값은 튜플 형태로 반환

def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 2, 3, 4, 5])
print(minimum, maximum)

# 3. 조건문에 따른 다른 값 반환
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(5))
print(is_even(6))

# 4. return 없는 함수
# : 호출이 완료되면 None을 반환
def greet(name):
    print(f'Hello, {name}')

result = greet('SeungAh') # 출력값: Hello, SeungAh
print(result) # 출력값: None