### 워드 클라우드 ###

#! 1. 워드 클라우드(word cloud)
# : 텍스트 데이터에서 자주 등장하는 단어를 시각적으로 표현하는 외부 라이브러리
# : 소셜 미디어 분석, 설문조사 결과 분석 등 
# : pip install wordcloud

#! wordcloud 생성하기
import wordcloud
import matplotlib.pyplot as plt

# 여러분들이 사용하시는 프로그래밍 언어는 무엇인가요? - 설문조사
# 43명이 설문조사에 참여

words = {
    'Python': 16,
    'Java': 5,
    'C': 7,
    'C++': 9,
    'JSP': 6
}

wc = wordcloud.WordCloud()
cloud = wc.generate_from_frequencies(words)

plt.figure()
plt.imshow(cloud)
plt.show()
