#함수
#def
#복잡한 코드를 쉽게
#코드 재사용
#코드의 안정성

#def function_name(parameter):
#   cdde

def firstFunc(w):
    print('Hello,', w)

word = "Python!"
firstFunc(word)

def returnFunc(w):
    return "Hello, " + str(w)
print(returnFunc(word))

#다중 반환

def mulFunc(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3
x, y, z = mulFunc(10)
print(x, y, z)

#튜플 리턴
def mulFunc2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)
q= mulFunc2(10)
print(q, type(q))

#리스트 리턴
def mulFunc3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]
q= mulFunc3(20)
print(q, type(q))

#딕셔너리 리턴
def mulFunc3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'k1' : y1, 'k2' : y2, 'k3' : y3}
a= mulFunc3(20)
print(a, type(a), a.get('k1'))
print(a.items())
print(a.keys())

#중요
# *args, **kwargs
print('--------------------')
#*args(언팩킹) # 보통 튜플

def argsFunc(*args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('--------------')
argsFunc('lee')
argsFunc('lee', 'Park')
argsFunc('lee', 'Park', "Kim")

# **kwargs (언팩킹)  보통 딕셔너리
def kwargsFunc(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('---------------')

kwargsFunc(
    name1 = 'Lee',
    name2 = 'Kim',
    name3 = 'cho'
    )

def example(args1, args2, *args, **kwargs):
    print(args1, args2, args, kwargs)

example(10, 20, 'lee', 'kim', 'park', age = 22, name = 'kim', phone ='01011112222')

#중첩함수

def nestedFunc(num):
    def inFunc(num):
        print(num)
    
    print('In Func')
    inFunc(num + 100)

nestedFunc(100)

#람다식
#메모리 절약, 가독성 향상, 코드 간결
#함수 -> 객체 생성 -> 리소스(메모리) 할당
#람다 -> 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
#남발 시 가독성 역으로 감소
print('-------------')
def mul_func1(x, y):
    return x * y
print(mul_func1(20,30))

mul_func2 = lambda x,y:x*y
print(mul_func2(30, 40))

def func_final(x,y,func):
    print(x * y * func)

func_final(10,20,mul_func2(10,20))