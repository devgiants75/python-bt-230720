# 1. 어떤 수가 양수인지, 음수인지, 아니면 0인지 판단하는 중첩 if-else 문

num = 15

if num > 0:
    print('The number is positive')
else:
    if num < 0:
        print('The number is negative')
    else:
        print('The number is zero')


# 2. 1부터 10까지 합을 구하는 프로그램 작성
#    for 반복문과 산술 연산자를 사용

# 합계를 저장할 변수를 0으로 초기화합니다.
total = 0
# 1부터 10까지의 모든 정수를 순회(반복)하면서 합계를 업데이트합니다.
for i in range(1, 11):
    total += i # total = total + i

# 최종 합계를 출력합니다.
print('The sum from 1 to 10 is ', total)