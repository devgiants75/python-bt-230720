### 예외 처리 ###

#! 1. if문(고전적인 예외 처리 방법)
a = int(input('정수를 입력하세요.'))
b = int(input('정수를 입력하세요.'))

# a / b
if b == 0:
    print('0으로 나눌 수 없습니다.')  
    # b에 0값이 들어올 경우 ZeroDivisionError: division by zero 에러 발생
else:
    print('{} / {} = {}'.format(a, b, a / b))

num1 = 5
num2 = 3
print(num1 + num2)

# 고전적인 if 조건문 예외 처리의 경우
# 코드의 복잡성 증가, 가독성 저하, 예상치 못한 에러 처리의 어려움이 존재

#! 2. 예외의 종류

# 내장 예외의 종류
# BaseException: 최상위 예외 클래스 - Exception
# ValueError: 잘못된 값이 입력될 때 발생
# TypeError: 잘못된 타입의 데이터 연산 시 발생
# ZeroDivisionError: 0으로 나누는 경우 발생
# SyntaxError: 문법이 틀렸을 경우 발생 (들여쓰기)