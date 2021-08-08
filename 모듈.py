#모듈
# 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return x ** y




if __name__ == '__main__':
    print('called inner!')
    print(add(10, 20))
    print(subtract(20,10))
    print(multiply(20,30))
    print(divide(50,10))
    print(power(12,3))
    print('---------------')
    