### 워드 클라우드 - 한글 사용 ###

import wordcloud
import matplotlib.pyplot as plt

words = {
    '파이썬': 20,
    '빅데이터': 5,
    '웹크롤링': 7,
    '인공지능': 9,
    '딥러닝': 12,
}

# 한글 폰트 경로 가져오기
# 파일 탐색기 > C드라이브 > Windows 폴더 > Fonts 폴더
# 사용하고자 하는 폰트 우클릭 - 복사
wc = wordcloud.WordCloud(font_path = 'c:\Windows\Fonts\HMFMOLD.TTF')
cloud = wc.generate_from_frequencies(words)

plt.figure()
plt.imshow(cloud)

plt.show()