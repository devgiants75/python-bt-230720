### matplotlib 라이브러리 ###

#! 1. pie() 함수
# 원형 그래프(파이 차트)를 작성하는 함수
# : 전체에 대한 각 부분의 비율을 시각적으로 보여주는데 사용

import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)

data = [1, 2, 3]
axes.pie(data)

# 형태가 타원이 아닌 일반 원의 형태로 출력될 수 있도록 설정
plt.axis('equal') 

plt.show()

#! 2. pie()함수의 매개변수

# 2-1. labels: 각 섹션의 라벨 설정
# 2-2. colors: 각 섹션의 색상 설정
# 2-3. shadow: 섹션에 그림자 추가

import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)

data = [1, 2, 3, 4, 5]
labelsData = ['A', 'B', 'C', 'D', 'E']
colorsData = ['red', 'orange', 'green', 'yellow', 'blue']
axes.pie(data, labels=labelsData, colors=colorsData, shadow=True)
plt.title('Pie Chart')
# 범례 지정: 각 계열의 이름을 표시하기 위해 차트 한 공간에 만든 박스
plt.legend(title='Data') 

plt.axis('equal') 

plt.show()