### 예외 처리 & 클래스 ###

# 교재 p.306
# 우리나라의 모든 도를 맞히는 퀴즈

# 지시사항
#* 1. Quiz 클래스는 다음과 같은 클래스 변수를 가지고 있습니다.
class Quiz:
    # 클래스 변수 answer 작성
    answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']

    # 클래스 메서드 challenge() 작성
    #* 2. challenge() 메소드는 사용자의 입력을 처리하고 일치하는 정답이 있으면 '정답입니다'를 출력한 뒤 해당 정답을 answer에서 제거합니다. 그리고 다시 challenge() 메소드를 호출합니다.
    #* 3. challenge() 메소드는 사용자의 입력이 틀린 경우 '틀렸습니다.'라는 예외 메시지를 출력할 수 있도록 예외를 발생 시킵니다.
    @classmethod
    def challenge(cls):
        user_input = input('도를 입력하세요 : ')
        if user_input in cls.answer:
            cls.answer.remove(user_input)
            print('정답입니다.')
            if len(cls.answer) == 0:
                print('모든 도를 맞혔습니다. 성공입니다.')
                return
            cls.challenge()
        else:
            raise Exception('틀렸습니다.')

#* 4. Quiz 클래스의 동작 확인은 다음과 같은 코드로 진행합니다.
try:
    print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
    Quiz.challenge()
except Exception as e:
    print(e)

#* 5. 정답을 모두 맞히면 다음과 같은 메시지를 출력합니다.
# 모든 도를 맞혔습니다. 성공입니다.