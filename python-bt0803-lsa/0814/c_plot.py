### matplotlib 라이브러리 ###

#! 1. plot()함수
# : 선 그래프를 그리기 위한 함수(꺾은선형그래프)
# : x값, y값을 이용하여 2차원 선 그래프를 생성
# : plot(x, y) 
# : x, y값에 각각의 데이터를 리스트 형태로 전달

import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)
# x축 값
x1 = [0, 1, 2, 3, 4]
x2 = [0, 1, 2, 3, 4]
# y축 값
y1 = [4, 1, 3, 5, 2]
y2 = [0, 7, 5, 3, 1]
axes.plot(x1, y1, color='r', linestyle='dotted')
axes.plot(x2, y2, marker='^', linewidth=2, linestyle='--')

# 그래프 제목 스타일링
plt.title('Data Visualization')
plt.xlabel('X 축')
plt.ylabel('Y 축')

plt.show()

#! 2. plot()함수 커스터마이징
# linestyle: 선의 스타일 설정
# 실선(- / solid), 점선(. / dotted), 대시(-- / dashed)

# linewidth: 선의 두께 설정
# 포인트(pt) 단위의 실수

# color: 선의 색상 설정
# 빨강(red), 파랑(blue), 노란색(yellow)

# marker: 각 데이터 포인트에 대한 마커 설정
# 표식 (o: 원, ^: 삼각형, s: 사각형)

