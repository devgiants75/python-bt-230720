### 파이썬 외부 모듈 - numpy ###
# : 수치 연산 라이브러리
# : 대규모 다차원 배열 & 행렬 연산에 필요한 함수를 제공

# 외부 모듈 & 패키지 설치 시 alt enter shift
import numpy as np

# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# 2차원 배열 생성
arr2 = np.array(([1, 2, 3], [4, 5, 6]))
print(arr2)

# 배열의 형태 확인
print(arr2.shape) # (2, 3): 2행 3열

# 배열 연산
arr3 = arr1 + 2 # 배열의 모든 요소에 2의 값을 더해서 출력
print(arr3)

# 통계 함수 사용
print(np.mean(arr1)) # 넘파이 배열의 평균값
print(np.sum(arr2)) # 넘파이 배열의 총합