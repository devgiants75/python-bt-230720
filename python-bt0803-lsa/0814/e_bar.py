### matplotlib 라이브러리 ###

#! 1. bar() 함수
# : 수직 막대 그래프(바 차트)를 그리는 데 사용
# : 주로 범주형 데이터의 각 항목에 대한 값을 비교할 때 사용

import matplotlib.pyplot as plt 

figure = plt.figure()
axes1 = figure.add_subplot(121)
axes2 = figure.add_subplot(122)
x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y = [8, 6, 5, 4, 10, 3, 7]

# color: 막대의 색상 설정
# edgecolor: 막대 테두리 색상 설정
# barh(): 수평 막대 그래프
axes1.bar(x, y, color='skyblue', edgecolor='black')
axes2.barh(x, y, color='skyblue', edgecolor='black')
plt.title('weekday chart')
plt.show()