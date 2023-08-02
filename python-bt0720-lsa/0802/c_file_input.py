### 파일 입력 (input) ###

# 1. 전체 파일 읽기
# r (read, 읽기)모드를 사용해 파일 열기
# read()함수 사용

# 인코딩 오류 발생 시 - open함수에 encoding='' 속성을 추가
# : 다국어 사용 파일일 경우 주로 발생
file = open('my_file.txt', 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()

# with open('my_file.txt', 'rt') as file:
#    content = file.read(5)
#    print(content)

# 2. 파일의 한 줄씩 읽기
# 파일의 각 줄을 순차적으로 읽을 경우: readline()
file = open('my_file.txt', 'r', encoding='utf-8')
while True:
    line = file.readline()
    if not line: break
    print(line)
file.close()

# 3. 모든 줄을 리스트로 읽기
# readlines()함수: 파일의 각 줄을 요소로하는 리스트를 반환
file = open('my_file.txt', 'r', encoding='utf-8')
lines = file.readlines() # lines: 리스트
for line in lines:
    print(line)
file.close()

print(lines)