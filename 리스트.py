#리스트
#배열
#순서 o, 중복 o, 수정 o, 삭제 o

#선언
a = []
b= list()
c = [1,2,3,4,5]
d = [1,10,'ace','base','car']
e = [1,10,['ace','base','car']]
f = [21.42,'foobar', 3, 4, False, 3.12321]

print(type(e),e)
print(d[1])
print(d[-1])
print(e[-1])
print(e[-1][1])
print(list(e[-1][1]))

#슬라이싱
print(e[:3])
print(e[-1][1:3])

#리스트 연산
print(c+d)
print(d+e)
print('test'+str(c[2]))

#값 비교
print(c[:3])
print(c == c[:3]+c[3:])

#리스트 수정, 삭제
print('-------------------------')
print(c)
c[0] = 4
print(c)
c[1:2] = ['a', 'b', 'c']
print(c)
c[1:2] = [['a', 'b', 'c']]
print(c)
c[0] = ['a', 'b', 'c']
print(c)
c[:2] = []
print(c)
del c[0]
print(c)
print('------------------------')
#리스트 함수
a = [5,1,2,3,5,4]
print(a)
a.append(10) #끝에 데이터 추가
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(3))
print(a[3])
a.insert(2,7) # 원하는 위치에 삽입
print(a)
#del a[6]
#print(a)
a.remove(5)
print(a)
print(a.pop())
print(a)
a.insert(1,2)
print(a.count(2))
ex = [8,9]
a.extend(ex)
print(a)

#삭제 remove 원하는 것 삭제, pop 맨 뒤를 출력하고 삭제, del 원하는 위치 삭제

while a:
    data = a.pop()
    print(a)
    print(data)

    