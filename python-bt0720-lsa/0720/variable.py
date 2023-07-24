# 1. 변수
# : 객체를 가리키는 상자
# : 어떠한 값을 저장할 때 사용하는 메모리 공간

# 메모리
# : 컴퓨터가 프로그램에서 사용하는 데이터를 기억하는 공간
# 객체
# : 프로그래밍을 하면서 사용하는 데이터(값)

# 1-1. 변수 선언 방법
# 변수명 = 데이터(값)
a = 1
b = '파이썬의 변수 선언 방법'
c = 2 + 3
print(a)
print(b)
print(b)
print(b)
print(c)

# 1-2. 변수 명명 규칙

# 필수 명명 규칙
# 1) 영문 문자와 숫자를 사용할 수 있다.
# 2) 대소문자를 구분
A = 2
print(a)
print(A)
# 3) 문자부터 시작해야 하며 숫자부터 시작하면 안된다.
a1 = 1
# 1a = 1 (Error)
# 4) _(밑줄 문자)로 시작 가능
# 5) 특수문자(+, -, *, /, $, @, % 등)는 사용 불가
# 6) 파이썬의 키워드(if, for, while, and, or)는 사용 불가

# 선택 명명 규칙
# 1) 가급적 소문자로만 구성
# 2) 한글 변수명 가능 but, 가급적 영문 변수명을 사용 권장
# 3) 변수명을 통해 어떤 것을 저장하고 있는지 파악할 수 있어야 한다.

# 1-3. 변수의 메모리 주소
# : id 키워드를 통해 확인 가능
# : id 함수는 변수가 가리키고 있는 객체의 주소 값을 리턴하는 파이썬 내장 함수
print(id(a))
