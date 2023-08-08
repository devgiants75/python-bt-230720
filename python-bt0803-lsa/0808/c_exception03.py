# 파이썬 예외 처리 방식 #

#! 1. 모든 예외를 처리하는 방식
# : 모든 예외를 처리하면 예상치 못한 오류가 발생할 때도 프로그램이 계속 될 수 있다.
# : 가능한 특정 예외를 지정하여 처리하는 것을 권장
# try - except 문을 사용하여 예외 처리

#* 예외 처리 기본 형태
# try:
#     코드 작성 영역
# exception:
#     예외 발생 시 처리 영역

try:
    a = int(input('정수를 입력하세요 : '))
    b = int(input('정수를 입력하세요 : '))
    print('{} / {} = {}'.format(a, b, a / b))
except:
    print('예외가 발생했습니다.')

#! 2. 특정 예외만 처리하는 방식
# except 절은 여러 개를 동시에 사용 가능
# except 절 뒤에 처리할 예외명을 생략하면 발생한 예외의 종류와 상관없이 오류 처리

# 1. 0으로 나누려고 하는 경우 - 0으로 나눌 수 없습니다.
# 2. 정수가 아닌 값을 입력하는 경우 - 정수만 입력할 수 있습니다.

try:
    a = int(input('정수를 입력하세요 : '))
    b = int(input('정수를 입력하세요 : '))
    print('{} / {} = {}'.format(a, b, a / b))
except ZeroDivisionError: 
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except Exception:
    print('기타 오류가 발생했습니다.') # 예상치 못한 예외들도 모두 처리하는 구문

#! 3. 예외 메시지 처리하기
# 모든 예외는 기본적으로 예외 메시지를 내장하고 있다.
# as 키워드를 통해 except문의 예외 메시지를 가져올 수 있다.

#* 예외 메시지 처리의 기본형태
# try: 
#   코드 작성 영역
# except 예외명 as 예외메시지명:
#   예외 발생 처리 영역

# 리스트에 존재하지 않는 인덱스를 사용: IndexError 예외 발생
a = [10, 20, 30, 40, 50]

try:
    a[10]
except IndexError as message:
    print(message) # list index out of range

try:
    a = int(input('정수를 입력하세요 : '))
    b = int(input('정수를 입력하세요 : '))
    print('{} / {} = {}'.format(a, b, a / b))
except ZeroDivisionError as e1: 
    print(e1) 
except ValueError as e2:
    print(e2) # invalid literal for int() with base 10: '안녕'