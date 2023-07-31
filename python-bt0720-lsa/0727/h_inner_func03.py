### 시퀀스 내장 함수 ###

# 시퀀스 자료형 : 요소들이 연속적으로 이어진 자료형
# 리스트, 튜플, 문자열 등

# 1. enumerate() 함수 - 리스트
# 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플(tuple)형태로 함께 추출

# for item in enumerate([리스트]):
    # 반복 실행문

for item in enumerate(['가위', '바위', '보']):
    print(item)
# (0, '가위') # (인덱스번호, 요소값)
# (1, '바위')
# (2, '보')

# 2. range() 함수
# 숫자 리스트를 생성하는데 사용
# 주로 for 반복문에서 사용, 일정한 간격의 숫자 시퀀스를 생성 가능

# range(stop): 0부터 stop-1까지의 정수를 반환
for i in range(5):
    print(i)

# range(start, stop): start ~ stop-1
for i in range(1, 5):
    print(i)

# range(start, stop, step): start ~ stop-1, step간격으로 반환
for i in range(0, 10, 2):
    print(i)

# 3. len() 함수
# : 컨테이너에 있는 원소의 개수를 반환
# : 리스트, 튜플, 문자열, 딕셔너리

# len(s): s의 원소 개수를 반환

my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # 5

my_string = "Hello, Python" # 문자열은 공백, 기호를 포함
print(len(my_string)) # 13

# 4. sorted() 함수
# 리스트를 정렬하여 반환 (기본: 오름차순 정렬)
# 내림차순 정렬: reverse=True 설정

my_list = [5, 1, 6, 3, 7]
# 오름차순 정렬
print(sorted(my_list))

# 내림차순 정렬
print(sorted(my_list, reverse=True))

# 5. zip() 함수
# : 여러 개의 순회 가능한(iterable) 값을 받아
# 각 객체의 동일한 인덱스에 있는 요소들끼리 짝찌어 튜플로 반환

list1 = [1, 2, 3]
list2 = ['one', 'two', 'three']

result = zip(list1, list2)
for i in result:
    print(i)

list1 = [1, 2, 3]
list2 = ['one', 'two']

result = zip(list1, list2)
for i in result:
    print(i)
# 결괏값: 각각의 순회 가능한 값의 길이가 다를 경우
# 동일한 인덱스 번호의 값만을 추출 (가장 짧은 길이의 값을 기준으로 튜플을 반환)
# (1, 'one')
# (2, 'two')