#
#!
#?
#^
#*
###

# 교재 p.288
# 파이썬 클래스 복습 문제 #
# 가게 매출을 구할 수 있는 Shop 클래스 구현

# 1. Shop 클래스
# : total = 0 (클래스 변수 - 전체 매출액)
# : menu_list = [{'떡볶이': 3000}, {'어묵': 700}, {'튀김': 500}, {'김밥': 2000}]
# (클래스 변수 - {메뉴명: 가격} 딕셔너리)
class Shop:

    #! 클래스 변수
    total = 0 # 가게 총 매출
    menu_list = [{'떡볶이': 3000}, {'어묵': 700}, {'튀김': 500}, {'김밥': 2000}]
    # 가게 메뉴 리스트를 딕셔너리 형식으로 정리

    #! 클래스 메소드
    @classmethod
    def sales(cls, menu, amount):
        # for in 반복문 
        # 메뉴 리스트에서 메뉴를 가지고와서
        # 해당 메뉴(menu)가 메뉴 리스트에 있는지 확인
        for item in cls.menu_list:
            if menu in item:
                # 인스턴스의 총 합계를 할당더하기 연산을 통해 구현
                # 메뉴 가격과 판매량을 곱한 후 전체 매출액에 더함
                cls.total += item[menu] * amount
                return
        # 해당 메뉴가 없다면 {menu}는 메뉴에 없습니다. 라는 f-string 반환문을 작성 
        print(f'{menu}는 저희 가게 메뉴에 없습니다.')

# 매출이 생기면 아래의 방식으로 메뉴와 판매량을 작성
# sales()메소드는 클래스 변수 total과 menu_list를 사용해야 하므로 클래스 메소드로 구현
Shop.sales('떡볶이', 1)
Shop.sales('튀김', 5)
Shop.sales('김밥', 2)
Shop.sales('라면', 2)

# 모든 매출을 작성한 뒤, 
print('매출: {}원'.format(Shop.total)) # 매출 @원