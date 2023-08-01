### 파이썬 표준 라이브러리 - random 모듈 ###
# : 난수를 생성하는 기능 제공
# : 임의의 수를 생성하거나, 시퀀스를 무작위로 섞는 등의 작업을 수행

import random

# 난수 생성
print(random.random()) # 0.0과 1.0 사이의 실수
print(random.uniform(1, 10)) # 1.0과 10.0 사이의 실수
print(random.randint(1, 10)) # 1과 10 사이의 정수

# 시퀀스 관련 함수 사용
my_list = [1, 2, 3, 4, 5]
random_my_list = random.choice(my_list)
print(random_my_list)

random.shuffle(my_list)
print(my_list) # my_list의 요소가 무작위로 섞인 리스트