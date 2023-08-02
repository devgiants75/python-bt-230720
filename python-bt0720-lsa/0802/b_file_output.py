### 파일 출력 ###

# 1. (텍스트 파일) 생성하기
file = open('file_output.txt', 'wt')
# write() 함수를 사용하여 파일에 내용을 작성
file.write('Hello, this is a sample text file!')
file.close()

# 2. (텍스트 파일) 내용 추가하기
file = open('file_output.txt', 'a')
file.write('\n') # \n 줄바꿈
file.write('This is additional text!')
file.close()