# 클래스 변수 & 클래스 메소드 & 정적 메소드 #

# 교재 p.282
# 가방을 만들 때마다, 현재 만들어진 가방이 몇 개인지 계산하는 Bag 클래스

class Bag:

    count = 0 # 초기화

    def __init__(self):
        Bag.count += 1 # 생성자가 호출될 때마다 count가 1씩 증가

    @classmethod
    def sell(cls):
        cls.count -= 1 # 가방이 판매될 때마다 count가 1씩 감소

    @classmethod
    def remain_bag(cls):
        return cls.count # 남아있는 가방의 개수를 반환하는 메소드
    
print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1.sell()
bag2.sell()
print('현재 가방: {}개'.format(Bag.remain_bag()))