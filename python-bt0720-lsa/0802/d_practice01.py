# 파일 입출력 예제
# p.237

# 엄마돼지 아기돼지 동요 가사가 적힌 new_file.txt 열어서
# 해당 .txt파일에 '꿀'이라는 글자가 몇 번 나오는지 찾는 프로그램

file = open('new_file.txt', 'rt', encoding='utf-8') # 텍스트 파일을 읽는 모드

line_list = file.readlines()

count = 0
for line in line_list: # 17번 반복 (17개의 줄)
    for word in line:
        if word == '꿀':
            count += 1
print('꿀은 전체 {}번 나타납니다.'.format(count))