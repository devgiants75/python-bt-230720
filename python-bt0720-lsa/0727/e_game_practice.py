# 가위 바위 보 게임 - 반복문 & 조건문 #

# random 모듈
# random 모듈에 .choice() 함수를 호출할 경우
# choice함수 내에서 호출하는 데이터 내에서 random 모듈이 임의로 선택하여 반환
# 사용법
# import random
# random.choice(데이터)

import random

options = ['가위', '바위', '보']

while True:
    print('가위, 바위, 보 게임을 시작합니다. "끝"을 입력하면 게임이 종료됩니다.')
    user_choice = input('가위, 바위, 보 중 하나를 선택하세요 : ')

    if user_choice == '끝':
        print('게임을 종료합니다.')
        break

    if user_choice not in options:
        print('잘못된 입력입니다. 가위, 바위, 보 중 하나를 입력하세요')
        continue

    computer_choice = random.choice(options)
    print(f'컴퓨터의 선택 : {computer_choice}')
    if user_choice == computer_choice:
        print('무승부입니다.')
    elif (user_choice == '가위' and computer_choice == '보') and (user_choice == '바위' and computer_choice == '가위') and (user_choice == '보' and computer_choice == '바위'):
        print('사용자의 승리입니다.')
    else:
        print('컴퓨터의 승리입니다.')
