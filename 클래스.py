#클래스
#객체지향
#OOP 객체지향 프로그래밍
#코드 재사용, 상속, 유지보수
# self, 인스턴스 메소드, 인스턴스 변수
# 클래스와 인스턴스 차이
#네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재


class Dog(object): #object 상송
    #클래스 속성
    species = 'firstdog'

    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age


#클래스 정보
print(Dog)

# 인스턴스화
a = Dog('aa', 2)
b = Dog('bb',3)
c = Dog('cc', 4)

#네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)

print('{} is {} and {} is {}'.format(a.name, a. age, b.name, b.age))

print(Dog.species)
print(a.species)
print('--------------------')
#self 예제

class SelfTest:
    def func1():
        print('Func1 called')
    
    def func2(self):
        print('Func2 called')


f = SelfTest()
# print(f.func1())
SelfTest.func1() #클래스로 직접 호출
f.func2()#인스턴스로 호출
SelfTest.func2(f) 
print('---------------')
#클래스 변수, 인스턴스 변수
class Warehouse:
    #클래스 변수
    stock_num = 0 #재고

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num +=1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print(user1.stock_num)

del user1
print(Warehouse.__dict__)
print(user2.stock_num)
print('----------------')
#
class Dog2(object): #object 상송
    #클래스 속성
    species = 'firstdog'

    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def bark(self, sound):
        return '{} says {}!'.format(self.name, sound)

#인스턴스 생성
q = Dog2('qq', 4)
w = Dog2('ww', 3)
#메소드 호출
print(q.info())
print(q.bark('Wal Wal'))
print(w.bark('Wang Wang'))