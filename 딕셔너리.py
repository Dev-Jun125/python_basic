#딕셔너리
#JSON 형태와 비슷
#딕서너리 => 순서X, 키 중복X, 수정O, 삭제O

#선언
a = {
    'name' : 'KIM',
    'phone' : '01011112222',
    'birth' : '111111',
}
print(a)
print(type(a))

#출력
print(a['name']) # 속성으로 접근 시 키 없으면 에러
print(a.get('name')) # 키 없으면 None  출력
print(a.get('KIM'))

#딕셔너리 추가
a['address'] = 'incheon'
print(a)
a['rank'] = [1, 2, 3]
print(a)
print(len(a)) #키의 갯수

#딕셔너리 키, 딕셔너리 벨류, 딕셔너리 아이템 반복문에서 사용 가능
print(a.keys())
print(a.values())
print(a.items())
print(list(a.keys()))
print(tuple(a.keys()))

# print(a.pop('rank'))
# print(a)

# print(a.popitem())
# print(a)

# print(a.popitem())
# print(a)


# print(a.popitem())
# print(a)


# print(a.popitem())
# print(a)

print('rank' in a)
print('address' not in a)

# 수정
a['test'] = 'test'
print(a)
a['address'] = 'seoul'
print(a)

a.update(address='incheon')
print(a)
