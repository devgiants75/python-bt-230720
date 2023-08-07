### 클래스 변수 ###

# 1. 클래스 변수의 정의

#! VS 인스턴스 변수
# : 인스턴스마다 서로 다른 값을 가지는 경우에는 인스턴스 변수를 사용
# : 모든 인스턴스 변수들은 self 키워드를 붙여 사용

# EX) 사람 클래스
# - 이름, 나이, 주소 등 (사람마다 다른 값을 가지는 것들)

#! 클래스 변수
# : 클래스 내부에서 정의되지만 메서드 외부에서 선언되는 변수
# : 해당 클래스의 모든 인스턴스에서 공유되는 값을 저장
# : 메모리 공간 낭비를 막을 수 있다.

# EX) 한국 사람 클래스
# - 소속 국가 (한국 사람이면 모두 같은 값을 가지는 변수)

class Korean:
    country = '한국' # country - 클래스 변수

    def __init__(self, name, age, address):
        self.name = name # self.name - 인스턴스 변수
        self.age = age # self.age - 인스턴스 변수
        self.address = address # self.address - 인스턴스 변수

man1 = Korean('이준국', 29, '부산')
### VSC 줄 복사: alt + shift + 방향키
### VSC 줄 이동: alt + 방향키
print(man1.name)
print(man1.age)
print(man1.address) # 인스턴스 변수는 해당 인스턴스에서만 불러오기 가능
# print(Korean.name) # Error 

# 클래스 변수는 해당 인스턴스 또는 클래스 모두에게서 불러오기 가능
print(man1.country) 
print(Korean.country)

#! 인스턴스 변수 & 클래스 변수
# 인스턴스 변수
# 목적: 인스턴스마다 다른 값을 저장
# 접근 방식: 인스턴스 접근만 가능

# 클래스 변수
# 목적: 인스턴스가 공유하는 값을 저장
# 접근 방식: 인스턴스 & 클래스 접근이 모두 가능

class MyClass:
    class_variable = "이것은 클래스 변수입니다."

    def show_class_variable(self):
        print(self.class_variable) # 인스턴스 내에서 클래스 변수에 접근 가능

instance1 = MyClass()
instance2 = MyClass()

print(instance1.class_variable)
print(instance2.class_variable)

MyClass.class_variable = "변경된 클래스 변수 값"

print(instance1.class_variable)
print(instance2.class_variable)