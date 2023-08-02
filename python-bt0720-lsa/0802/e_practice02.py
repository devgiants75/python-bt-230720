# "message.txt"라는 파일을 생성하고
# , 그 안에 "Hello, Python!" 이라는 메시지를 쓰는 파이썬 프로그램을 작성
with open('message.txt', 'wt', encoding='utf-8') as file:
    file.write('Hello, Python!')

# "message.txt" 파일에 "Learning file I/O is fun!"이라는
# 새로운 줄을 추가하는 파이썬 프로그램을 작성
with open('message.txt', 'a', encoding='utf-8') as file:
    file.write("Learning file I/O is fun!")

# "message.txt" 파일의 내용을 읽어서 콘솔에 출력하는 파이썬 프로그램을 작성
with open('message.txt', 'r', encoding='utf-8') as file:
    print(file.read())