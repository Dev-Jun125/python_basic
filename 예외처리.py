#예외 처리
#예외 종류
# syntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적 예외가 없지만 코드 실행 단계에서 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시


#SyntaxError : 문법 오류
# print('error)
# print('error'))
# if True
#     pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100/0)

# IndexError
# x = [50,70,90]
# # print(x[5])
# for i in range(0,4):
#     print(x.pop())

# KeyError
dic = {
    'name' : 'Lee',
    'Age' : 22,
    'City' : 'Incheon'
}
# print(dic['hobby'])
# print(dic.get('hobby'))

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAEP)

# # AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# ValueError
# x = [10,50,90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1,2]
y = (1,2)
z = 'test'

# print(x+y)
# print(x + z)
# print(y+z)

print(x + list(y))
print(x + list(z))


# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명 1: 여러개
# except 에러명 2: ...
# else: try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))

except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

print('----------')

# 오류 값을 정확하게 말고 전체적인 오류 다 잡기
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))

except Exception:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

######

try:
    z = 'Km'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))

except Exception as e:
    print(e)
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')
finally:
    print('Finally')


#######

#예외 발생 : raise
# raise 키워드로 예외 직접 발생
print('---------------')
try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok Pass')
    else:
        raise ValueError

except ValueError:
    print('Occurred Exception!')

else:
    print('Ok')
