### matploblib 라이브러리 ###

#! figure & subplot
# 1. figure
# : subplot을 포함할 수 있는 전체 영역
# : 한 figure 안에 여러 개의 subplot이 포함될 수 있음.
# - figure() 함수를 사용하여 생성
# - figure(figsize=(너비, 높이)) 

# 2. subplot
# :실제로 그래프를 그리는 영역
# - add_subplot() 함수를 사용하여 생성
# = add_subplot(nrows, ncols, index)
# nrows: 그리드의 행 수
# ncols: 그리드의 열 수
# index: 그래프를 그릴 위치(1부터 시작)

# 2행 2열의 subplot으로 구성된 figure을 작성

# add_subplot(2, 2, 1): 2행 2열의 subplot중 첫 번째 subplot
# add_subplot(2, 2, 2)
# add_subplot(2, 2, 3)
# add_subplot(2, 2, 4)

# matplotlib 라이브러리에서 pyplot 모듈을 불러와  
# 이름을 plt로 수정하는 import 형식
import matplotlib.pyplot as plt

figure = plt.figure()
axes1 = figure.add_subplot(2, 2, 1) # 2행, 2열, 1번째 subplot
axes2 = figure.add_subplot(2, 2, 2)
axes3 = figure.add_subplot(2, 2, 3)
axes4 = figure.add_subplot(2, 2, 4)

# 그래프 출력
plt.show()

# 여러 개의 subplot을 동시에 생성: subplots()함수 사용
axes = plt.subplots(nrows=3, ncols=3)
plt.show()