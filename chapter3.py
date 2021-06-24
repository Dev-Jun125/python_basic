#숫자형

#자료형
"""
int  정수
float 실수
complex 복소수
bool 불린형
str 문자열(시퀀스)
list 리스트(시퀀스)
tuple 튜플(시퀀스)
set 집합
dict 사전
"""

dict = {
    "name" : "dong jun",
    "age" : "25"
}
print(dict)

#숫자형 연산자
'''
+
-
*
/
// 몫
% 나머지
abs(x) 절대값
pow(x,y) x^y
divmod(x,y) 몫 나머지
'''

print(2**3)
print(pow(2,3))
int1 = 7777777777777777777777777777777777777
print(int1)

#다른 형을 계산하면 자동 형 변환
a = 7
f = 7.14
print(a+f)

#형 변환
a=3.0
b= 6
c=.7
d=12.7

print(type(int(b+c)))
print(int(b+d))

#모듈 사용
import math
print(math.pi)
print(math.ceil(5.1))

