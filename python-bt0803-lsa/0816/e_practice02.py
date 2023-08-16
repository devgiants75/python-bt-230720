### 파이썬 데이터 시각화 - 엑셀 파일 시각화 ###

#! 엑셀이 있는 경우: 엑셀(xlsx)파일 만들기
# 엑셀 문서 작성 후 - 파일명: python0803으로 변경 (확장자: .xlsx)
# 필요한 패키지 (pandas, numpy / openpyxl: 엑셀 파일을 불러오는 패키지)

# cmd(명령 프롬프트) & vsc 터미널(ctrl + shift + `) 모두 설치
# pip install pandas
# pip install numpy
# pip install openpyxl

# 프로그램 구현에 필요한 모듈 가져오기
import pandas as pd
import numpy as np

# pd.read_excel() 함수를 사용하여 Excel 파일 불러오기
# './python0803.xlsx': Excel 파일의 경로
# sheet_name="Sheet1"은 불러올 시트의 이름
# header=None은 파일의 첫 번째 행을 컬럼명으로 사용하지 않겠다는 의미
# index_col=None은 파일의 첫 번째 열을 인덱스로 사용하지 않겠다는 의미
dataframe = pd.read_excel('D:\\python-bt0720-lsa-git\\python-bt0803-lsa\\python0803.xlsx', sheet_name='Sheet1', header=None, index_col=None)

# 데이터 추출 및 변환
# dataframe.iloc[0, 1:13]는 데이터프레임의 첫 번째 행과 2번째부터 13번째 열까지의 데이터를 선택
x축 = dataframe.iloc[0, 1:13].to_numpy()  # 선택한 행렬 데이터를 array 로 변환
y축2020 = dataframe.iloc[1, 1:13].to_numpy()
y축2021 = dataframe.iloc[2, 1:13].to_numpy()
y축2022 = dataframe.iloc[3, 1:13].to_numpy()
소비카테고리 = dataframe.iloc[5, 1:5].to_numpy()
이번달소비금액 = dataframe.iloc[6, 1:5].to_numpy()
이번달소비금액합계 = np.nansum(이번달소비금액, dtype="float16")
평균2020 = np.nanmean(y축2020, dtype="float16")
평균2021 = np.nanmean(y축2021, dtype="float16")
평균2022 = np.nanmean(y축2022, dtype="float16")

#! 엑셀이 없는 경우: 데이터 하드 코딩
# x축 = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
# y축2020 = [38, 50, 25, 35, 47, 33, 112, 72, 23, 32, 46, 82]
# y축2021 = [48, 60, 35, 45, 57, 43, 122, 82, 33, 42, 56, 92]
# y축2022 = [58, 70, 45, 55, 67, 53, 132, 92, 43, 52, 66, 102]
# 소비카테고리 = ["식비", "카페", "영화", "취미생활"]
# 이번달소비금액 = [32, 9, 3, 7]
# 이번달소비금액합계 = 85
# 평균2020 = 57
# 평균2021 = 66
# 평균2022 = 78

print(x축)
print(y축2020)
print(y축2021)
print(y축2022)
print(소비카테고리)
print(이번달소비금액)
print(이번달소비금액합계)
print(평균2020)
print(평균2021)
print(평균2022)

import matplotlib.pyplot as plt
import platform

figure = plt.figure()

# 현재 사용중인 PC의 OS에 따라서 matplotlib의 폰트를 다르게 설정해주는 코드
if platform.system() == 'Darwin': # Mac OS
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='Malgun Gothic')

axes = figure.add_subplot(3, 1, 1)

axes.plot(x축, y축2020, marker='o', label='2020년')
axes.plot(x축, y축2021, marker='^', label='2021년')
axes.plot(x축, y축2022, marker='s', label='2022년')

plt.legend()
plt.xlabel('월') 
plt.ylabel('카드사용금액')

plt.show()