### 파이썬 모듈 ###

# 1. 모듈의 정의
# : 함수나 변수 또는 클래스를 모아놓은 파이썬 파일

# 2. 모듈의 필요성
# 2-1. 코드의 재사용성
# : 모듈은 한 번 작성하면 계속해서 재사용 가능
# : 개발 시간 단축 & 코드의 일관성 유지 용이

# 2-2. 코드의 구조화
# : 코드의 유지보수 용이 & 코드의 이해도가 높아짐

# 3. 파이썬 모듈의 사용방법

# 3-1. import 사용
# import 키워드를 사용하여 '불러오기'가 가능
# import 할 때에는 .py 확장자 생략하여 파일명만 작성

# b_my_module을 불러와서 사용하기
import b_my_module

print(b_my_module.add(3, 5))
print(b_my_module.sub(4, 2))

# 3-2. from import 사용
# from 모듈명  import 항목명(변수, 함수, 클래스명)
# : 특정 모듈에서 하나 이상의 특정 항목만 불러오기 가능
# : 항목을 사용할 때 모듈명을 접두어로 붙이지 않아도 사용 가능

# 여러 항목을 동시에 불러오는 경우 쉼표(,)를 사용하여 나열 가능

from b_my_module import greet, info

print(greet('이승아'))
print(info(50))

# 3-3. import as 사용
# : 모듈의 이름이 길거나 다른 모듈과 충돌할 가능성이 있는 경우
# : 모듈에 대한 별칭(alias)을 지정하는 것이 유용
# as 키워드를 사용하여 별칭 지정 가능

import b_my_module as mm

print(mm.add(5, 7))
print(mm.sub(5, 7))

from b_my_module import greet as hello
# b_my_module모듈 안의 greet 항목을 hello 별칭으로 사용

print(hello('이승아'))









