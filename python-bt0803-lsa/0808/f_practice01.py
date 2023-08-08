### 예외 처리 예제 ###

# 입력받은 이름이 2 ~ 4자 사이가 아니면 NameError 예외를 발생시키고
# '이름은 2 ~ 4자 사이로 입력해주세요.'라는 예외 메시지를 출력하는 프로그램

class NameError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    name = input('이름을 입력해주세요.')
    if len(name) < 2 or len(name) > 4:
        raise NameError('이름은 2~4자 사이로 입력해주세요.')
except NameError as e:
    print(e)
else:
    print('입력된 이름은 {}입니다.'.format(name))