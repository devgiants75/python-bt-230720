### 정사각형과 원의 넓이를 계산하는 함수 모듈 ###

# 1. calculate_square_area 함수 (정사각형의 넓이)
# 한 변의 길이를 인자로 받아 정사각형의 넓이를 반환
def calculate_square_area(side):
    return side * side

import math
# 2. calculate_circle_area 함수 (원의 넓이)
# 반지름을 인자로 받아 원의 넓이를 반환
# 반지름 * 반지름 * 3.14(파이)

def calculate_circle_area(radius):
    return radius * radius * math.pi
