### else문과 finallly문 ###

#! 1. else문
# : try 블록에서 예외가 발생하지 않으면 처리되는 구문
# : 주로 정상적으로 코드가 실행되는 경우 수행할 작업을 정의
# : 반드시 except 절 바로 다음에 위치!

#! 2. finally문
# : 예외 발생과 상관없이 항상 처리되는 구문
# : 주로 파일 닫기 등과 같은 필수적인 작업을 정의

# try:
#     코드 작성 영역
# except:
#     예외 발생 시 처리 영역
# else:
#     예외가 없을 때 처리 영역
# finally:
#     언제나 실행되는 영역

#! 3. else문 예제
try:
    number = int(input('정수를 입력하세요.'))
except ValueError as e:
    print(e)
else:
    print(f'입력한 숫자는 {number}입니다.')
finally:
    print('프로그램을 종료합니다.')

#! 4. finally문 예제
file = None # 미리 file 변수를 초기화

try:
    file = open('file.txt', 'r', encoding='utf-8')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('파일이 존재하지 않습니다.')
except Exception:
    print('파일 오류')
finally:
    if file: # file 객체가 정의되었는지 확인
        file.close()
        print('파일을 닫았습니다.')