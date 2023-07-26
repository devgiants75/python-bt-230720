### 조건문(Condition) ###

# 특정 조건을 충족할 경우 특정 코드 블록을 실행하는 프로그래밍 구문
# If문: 만약 ~ 라면
# 해당 조건이 참(True)인 경우에만 코드 블록을 실행

# 1. 조건문 작성법
'''
if 조건:
    (조건이 True인 경우)실행할 코드

1. 조건: 참(True) 또는 거짓(False)의 값을 갖는 표현식
2. 실행할 코드: if문 바로 아래에 들여쓰기를 하여 작성
3. if문의 맨 끝에는 조건 뒤에 콜론(:)을 반드시 기재
'''

# 2. 기본 if문
# 어떤 수가 10보다 큰지 확인하는 조건문 작성

num = 15

if num > 10:
    print('The number is greater than 10.')

# 3. else 문
# if문의 조건이 충족되지 않을 때(즉, if문의 조건이 False일 때) 실행되는 코드 블록을 지정
'''
if 조건:
    조건이 True일 때 실행할 코드
else:
    조건이 False일 때 실행할 코드
'''

# 어떤 수가 10보다 큰지 확인하고
# 10보다 클 경우 '안녕하세요' 출력
# 10보다 크지 않을 경우 '반갑습니다' 출력

num = 5

if num > 10:
    print('안녕하세요')
else:
    print('반갑습니다') # 10 이하의 수를 조건으로 하는 else문

# 4. 조건문에서 다양한 연산자 활용
# and, or, not연산자

# x and y
# x or y
# not x

money = 2000
card = True

# 돈이 3000보다 많거나 카드가 있을 경우 '택시를 탑니다' 출력
# 그렇지 않을 경우 '걸어갑니다' 출력

if money > 3000 or card: # False or True: True
    print('택시를 탑니다')
else:
    print('걸어갑니다')

# 5. 중첩 if-else문
'''
if 조건1:
    조건1이 참일 때 실행할 코드
    if 조건2:
        조건1과 조건2 모두 참일 때 실행할 코드
    else:
        조건1은 참이지만, 조건2는 거짓일 때 실행할 코드
else:
    조건1이 거짓일 때 실행할 코드
'''

num = 5

if num > 0:
    print('양수입니다')
    if num > 10:
        print('양수이면서 10보다 큽니다.')
    else:
        print('양수이지만 10보다 작습니다')
else:
    print('음수입니다')

# 6. elif문: else if의 줄임말
# 이전 if문 또는 elif 조건이 False일 때 확인되는 추가 조건을 지정

'''
if 조건1:
    실행할 코드1
elif 조건2:
    실행할 코드2(조건1이 거짓이고, 조건2가 참일 때 실행할 코드)
... 
elif 조건 999:
    실행할 코드999
else:
    모든 조건이 거짓일 때 실행할 코드
'''

# 어떤 수가 10보다 큰지, 10인지, 또는 10보다 작은지를 확인하는 코드
num = 11

if num > 10:
    print('The number is greater than 10')
elif num == 10:
    print('The number is exactly 10')
else:
    print('The number is less than 10')

# 조건문과 삼항 연산자
# if-else문을 더 간결하게 표현하는 방법

# 삼항연산자
# value_if_true(실행될 코드-참) if condition(조건) else value_if_false(실행될 코드-거짓)

# if-else
'''
if condiont(조건):
    value_if_true
else:
    value_if_false
'''

# 어떤 숫자가 10보다 큰지 아닌지를 판단하여 문자열을 반환하는 삼항 연산자
num = 15
result = "Greater than 10" if num > 10 else "Not greater than 10"
print(result)
