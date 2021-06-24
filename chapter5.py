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
