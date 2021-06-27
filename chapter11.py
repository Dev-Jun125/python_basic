#반복문
#while

#while <expr>:
#   <statment(s)>

#while True: 는 무한반복
n = 5
while n > 0:
    print(n)
    n = n-1

a = ['foo','bar','baz']
print('---------------')
while a:
    print(a.pop())

print('------------------')
#break, continue
n=5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('loop end')
print(n)

n=5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('loop end')
print(n)

#if 중첩
i = 1
while i <=10:
    print('i = ', i)
    if i == 6:
        break
    i=i+1

#while else 구문
n = 10
while n > 0:
    n -= 1
    print(n)
else:
    print('else out')

a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'
i = 0
while i < len(a):
    if a[i] == s:
        print('found ',a[i])
        break
    i +=1
else:
    print(s,' not found in list')

#무한반복
#while True:
#   print('foo')

a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())

