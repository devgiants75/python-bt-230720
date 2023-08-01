### 파이썬 표준 라이브러리 - math 모듈 ###

import math

# 1. 상수 사용
# math.pi() : (파이 - 원주율)
print(math.pi) # 3.141592....

# 2. 제곱근 함수 사용
# math.sqrt()
print(math.sqrt(16)) # 4.0

# math 모듈의 함수들은 부동 소숨점 수를 반환
# 정수를 입력하더라도 무조건 소수점 자리를 반환
# 4 -> 4.0, 17 -> 17.0

# 3. 기타 수학 함수
# math.fabs(): 절댓값
# math.factorial(): 팩토리얼
# math.ceil(): 올림
# math.floor(): 버림

print(math.fabs(-5)) # 5.0
print(math.factorial(5)) # 5 * 4 * 3 * 2 * 1 = 120
print(math.ceil(2.3)) # 3
print(math.floor(2.7)) # 2