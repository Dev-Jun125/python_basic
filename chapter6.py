#튜플
#리스트와 비교 중요
#튜플 => 순서O, 중복ㅇ, 수정X, 삭제X = 불변

#선언
a = ()
b = (1) #원소 하니일 땐 ,를 찍어야 튜플로 인식
print(type(b))
b1 = (1,)
print(type(b1))
c = (1,2,3,4,5,6)
d = (10, 100, 'ace', 'base', 'car')
e = (12, 211, ('ace', 'base', 'car'))
#인덱싱
print(d[1])
print(d[0] + d[1] + d [1])
print(e[-1])
print(e[-1][1])
print(list(e[-1][1]))

#수정 X
#d[0] = 100
#TypeError: 'tuple' object does not support item assignment

#슬라이싱
print(d[0:3])
print(d[2:])
print(e[2][1:3])

#튜플 연산
print(c*3)
print(d+e)

#튜플 함수
print(c.index(3))
print(c.count(2))

#팩킹과 언팩킹

#패킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])

#언패킹
(x1, x2, x3, x4) = t
print(type(x1),type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

t2 = 1, 2, 3 
t3 = 4,
x1, x2, x3 =t2
x4, x5, x6 = 4, 5, 6
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)

