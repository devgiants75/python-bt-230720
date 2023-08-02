### 모듈 실습 문제 ###
# p.221

import time
import random
# 파이썬으로 자동으로 실행되는 로또 추첨 프로그램을 다음 지시사항에 따라 구현하세요.

# 지시사항
# 1. 1에서 45 사이의 모든 정수를 순서대로 pot 리스트에 저장합니다.
pot = list(range(1, 46))

# 빈 jackpot 리스트를 생성합니다.
jackpot = []

# 2. 다음 과정을 6번 반복합니다.
# for 반복문에서 _(언더바) 사용 시 특별히 사용되지 않는 변수
for _ in range(6):
# - pot 리스트를 무작위로 섞어 줍니다. - random 모듈의 shuffle 메서드 사용
    random.shuffle(pot)

# - pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.
    jackpot.append(pot.pop())

# - 2초 동안 잠시 멈춥니다. - time 모듈의 sleep() 메서드 사용
    time.sleep(2)

# 3. jackpot 리스트의 모든 요소를 오름 차순 정렬합니다.
jackpot.sort()
# 4. jackpot 리스트의 모든 요소를 출력합니다.
print(jackpot)
# time 모듈과 random 모듈을 활용하는 문제입니다.