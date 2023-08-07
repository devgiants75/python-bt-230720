### 서브 클래스의 __init__() ###

# 부모 클래스 없이는 서브 클래스 구현 불가!
# : 서브 클래스의 생성자를 구현할 때에는 반드시 
# : 슈퍼 클래스의 생성자를 먼저 호출해야 한다.

class ParentClass:
    def __init__(self, name):
        self.name = name
        print(f"Parent's __init__ called with name: {self.name}")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)  # 부모 클래스의 __init__ 메서드 호출
        self.age = age
        print(f"Child's __init__ called with name: {self.name} and age: {self.age}")

child = ChildClass('DoKyung', 10)

# 서브 클래스의 인스턴스 자료형 # 

# 슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
# 서브 클래스의 객체는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스

# 어떤 객체가 어떤 클래스의 인스턴스인지 확인하는 함수
# : 결괏값을 불리언(Boolean)타입으로 반환
# : isinstance(객체, 클래스)

print(isinstance(child, ChildClass)) # True
print(isinstance(child, ParentClass)) # True