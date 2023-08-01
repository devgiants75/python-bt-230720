#
# b_my_module.py 파일 : 덧셈과 뺄셈을 구현하는 모듈
# 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 위의 모듈을 a_module01.py에서 불러오기

def greet(name):
    return f'Hello, {name}'

def info(age):
    return f'I"m {age} years old'