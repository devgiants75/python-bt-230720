### 반복문 - While문 ###

# 1. while: ~동안
# 주어진 조건이 참인 동안(즉, 조건이 거짓이 될 때까지)
# 코드 블록을 반복적으로 실행하는 제어 흐름 구조

'''
while condition(조건):
    실행할 코드(조건이 참일 동안)

조건: 루프(반복)가 계속 실행되는지 아니면 중단되는지를 결정하는 boolean타입 표현식
'''

# 변수를 1씩 증가 시켜서 5보다 작을 때까지 출력

count = 0
while count < 5:
    print(count)
    count += 1 # count = count + 1

# 2. 무한 루프
# : 조건이 항상 참인 while문을 사용하여 생성

'''
while True(True값이 될 수 있는 조건):
    실행할 코드
'''
# count = 0
# while True:
#     count += 1

# 무한루프 실행 후 중단 단축키 : ctrl + f2

# 2-1. break
# : 무한 루프 종료
# break문: 루프의 실행을 즉시 중지, 루프 다음에 오는 코드를 실행

while True:
    userInput = input('종료하려면 "q"를 입력하세요 : ')
    if userInput == 'q':
        break

# 2-2. continue
# : 루프의 나머지 부분을 건너뛰고 다음 반복으로 직접 건너뛰는데 사용
# : 루프의 현재 반복을 중지, while문의 조건을 다시 확인

while True:
    userInput = input('종료하려면 "q"를 입력하세요2 : ')
    if userInput == 'q':
        break
    if not userInput.isdigit():
        print('숫자만 입력해주세요!')
        continue
    # isdigit(): 문자열이 숫자로만 이루어져있는지 확인하는 함수
    # 문자가 '단 하나'라도 있으면 False
    # 모든 문자가 '숫자'로만 이루어져있으면 True를 반환
    print(f'입력하신 숫자는 {userInput}입니다.')