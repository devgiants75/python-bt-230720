### matplotlib 라이브러리 예제 ###

# 소음에 따른 스트레스 지수 조사 #
# 소음과 스트레스 지수의 상관관계를 시각적으로 표시 - 산포그래프

# 소음 : 20 ~ 70 (5씩 증가)
# 스트레스 : [10, 11, 15, 20, 30, 42, 55, 70, 88, 110, 150]

import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)

noise = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
stress = [10, 11, 15, 20, 30, 42, 55, 70, 88, 110, 150]

axes.scatter(noise, stress, s=50)
plt.xlabel('noise')
plt.ylabel('stress')

plt.show()