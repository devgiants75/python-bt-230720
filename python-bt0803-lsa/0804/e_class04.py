### 생성자 ###

class Candy:

    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

satang = Candy() # 값이 없는 인스턴스를 생성
satang.set_info('circle', 'red') # 값을 저장할 수 있는 메소드를 호출

#! 생성자를 이용한 인스턴스 생성
# 생성자: 인스턴스를 생성할 때 자동으로 호출되는 특별한 메소드

# 생성자의 형태
# : __init__() - 파이썬에서 생성자의 이름은 항상 __init__로 고정! (변경 불가!)
# : 인스턴스 변수의 초기화 용도로 사용
# : 생성자의 첫 번째 매개변수도 반드시 self로 선언

# 파이썬에서 '__'(언더바 2개)로 시작되는 메소드들은 
# 미리 기능과 역할이 부여된 메소드

class Candy2:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

satang2 = Candy2('circle', 'blue') # 생성자가 자동으로 호출
print(satang2.shape, satang2.color)

# 소멸자 #
# : 인스턴스가 소멸될 때 자동으로 호출되는 메소드
# : 소멸 - 메모리에서 삭제
# : __del__()

class Sample:
    def __del__(self):
        print('인스턴스가 소멸됩니다.')

sample = Sample()
del sample