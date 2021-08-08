#집합 sets
#집합 => 순서X, 중복X

#선언
a = set()
b = set([1,2,4,7,2,1,6])
c = set([1,3,'pen','cap','plate'])
d = {'foo','bar','baz','foo','qux'}
e = {41,'foo',(1,2,3), 3.141592}
print(a)
print(b)
print(c)
print(d)
print(e)

#형 변환
f = tuple(c)
print(f)
print(f[1:3])

g = list(c)
print(g)

#길이
print(len(a))
print(len(c))

#집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1&s2) #교집합
print(s1.intersection(s2))
print(s1|s2)  #합집합
print(s1.union(s2))
print(s1-s2) #차집합
print(s1.difference(s2))

#중복 원소 확인
print(s1.isdisjoint(s2)) #중복 존재 => false

#부분집합 확인
print(s1.issubset(s2)) #부분집합 아니니 => false
print(s1.issuperset(s2))

#추가, 제거
s1 = set([1,2,3,4])
s1.add(5)
print(s1)

s1.remove(4)
print(s1)
# s1.remove(10)  존재 X -> 예외 발생
s1.discard(10) #존재하지 않아도 예외 발생 X
print(s1)

s1.clear()
print(s1)

#리스트도 clear로 가능

