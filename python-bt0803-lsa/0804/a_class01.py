### 객체 & 클래스 정의 ###

#! 1. 객체란 ?
# 서로 많은 데이터를 하나로 묶어서 표현한 것

# EX) 웹 페이지에 작성할 게시글 
# : 게시글 번호, 작성자, 제목, 내용, 작성일자, 수정일자, ...

#! 2. 클래스란?
# 객체를 만드는 도구

# 와플(객체) & 와플 머신(클래스)
# : 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질 수 있다.

#! 3. 인스턴스란?
# 클래스를 이용해서 생성한 객체를 가리키는 용어

# 와플 머신 클래스로 만든 와플은 객체(object)
# 와플은 와플 머신 클래스로 만든 인스턴스(instance) 
# 객체 = 인스턴스

# 이승아 / 사람
# 안성탕면 / 라면
# 자동차 / BMW
# 프로그래밍언어 / 파이썬

#! 3. 클래스 정의
# : 클래스를 생성
# - class 키워드로 클래스를 정의
# - 클래스 이름은 Upper Camel Case 규칙을 따름

#? 파이썬 명명 규칙 
# 변수, 함수, 파일명: snake_case (my_best_friend)
# 클래스: Upper Camel Case

# UpperCamelCase: 첫 글자 & 이어지는 단어의 첫 글자를 대문자로 작성
# (MyBestFriend)
# LowerCamelCase: 이어지는 단어의 첫 글자만 대문자로 작성
# (myBestFriend)

#? 클래스 기본 형식 - 들여쓰기 문법을 따름
# class 클래스명:
    # 본문 (클래스 상세정의)

#! 4. 객체 생성
# 객체명 = 클래스명()

# 객체1 = 클래스()
# 객체2 = 클래스()

#! 5. 클래스 정의와 객체 생성
class WaffleMachine:
    pass # 아무런 정의 없이 클래스를 생성

waffle = WaffleMachine()
# waffle (객체)
# WaffleMachine (클래스)

print(waffle) 
# <__main__.WaffleMachine object at 0x0000027536C710D0>
# : 0x0000027536C710D0주소에 저장된 WaffleMachine 객체