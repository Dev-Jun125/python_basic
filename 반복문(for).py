#반복문
#for
#for in <collection>
#   <loop body>

for i in range(10):
    print(i)

print('-----------')

for i in range(1,10,2):
    print(i)

print('-----------')

for i in range(1,11):
    print(i)

#1~1000까지 합

sum = 0
for i in range(1,1001):
    sum = sum + i
print('-------------')
print(sum)

print('-------------------')
#iterables 자료형 반복
#문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
#iterable 리턴 함수 range, reversed, enumerate, filter, map, zip

names = ['Kim', "Park", "Cho", 'Lee', "Choi", 'Yoo']
for i in names:
    print('you are ', i)

import random
lottoNumber =[]
for i in range(6):
    lottoNumber.append(random.randint(1,45))
print(lottoNumber)
for i in lottoNumber:
    print("lotto :", i)

word = 'Python'
for i in word:
    print(i)
infoDict = {
    'name' : 'Kim',
    'Age' : 22,
    'City' : 'Incheon'
}

for i in infoDict:
    print(infoDict[i])

for i in infoDict.values():
    print(i)

name = 'FineAPPle'

for i in name:
    if i.isupper():
        print(i)
    else:
        print(i.upper())

#break
number = []
for i in range(10):
    number.append(random.randint(1,10))
print(number)

for i in number:
    if i == 8 or i == 10:
        print('Found!', i)
        break
    else:
        print('Not Found', i)

#continue

lt = ['1', 2, 5, True, 4.312, complex(4)]

for i in lt:
    if type(i) is bool:
        continue
    print(i, type(i))


#for - else 구문

for i in number:
    if i == 8:
        print('found', i)
        break

else:
    print('not found')

#구구단

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end ='\t')

    print()

#변환   reversed
name2 = "Hello Python!"

print(reversed(name2))
print(list(reversed(name2)))
print(tuple(reversed(name2)))
print(set(reversed(name2)))
