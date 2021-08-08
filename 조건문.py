#조건문
#if
#관계연산자, 논리연산자, 일반 조건문, 다중 조건문, 중첩 조건문

#기본 형식
print(type(True)) #0이 아닌수, 'abc,' [1,2,3...], (1,2,3,...)...
print(type(False)) #0, "", [], (), {}....

#예
if 'a' :
    print('python')

if '' :
    print('python')
else :
    print('python!')

#관계 연산자
# >, >=, <, <=, ==, !=

x= 15
y = 10
print(x==y)
print(x != y)
print(x>y)
print(x<=y)

city = ''
if city:
    print('you are in ', city)
else:
    print('plz enter your city')

city = 'incheon'
if city:
    print('you are in ', city)
else:
    print('plz enter your city')

#논리 연산자
# and, or, not

a=75
b=40
c=10
print(a>b and b>c)
print(a>b and b<c)

print(a>b or b<c)
print(not a>b)

print(not True)
print(not False)

#산술, 관계, 논리 우선순위
#산술 > 관계 > 논리

print('-----------------------')
print(3 + 12 > 7 + 3)
print(5 + 10 * 3 > 7 + 3 * 20)
print( 5 + 10 > 3 and 7 + 3 == 10)
print(5 + 10 > 5 and not 7 + 3 == 10)

#복수의 조건이 모두 참일 경우에 실행
score1 = 70
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print("Fail")

id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')
if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

#다중 조건문
num = 90
if num >= 90:
    print('A')
elif num >= 80:
    print('B')
elif num>=70:
    print('C')
else:
    print('Fail')

#중첩조건문
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else :
        print('장학금 50%')
else:
    print('장학금 X')

#in not in

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {
    "name" : "lee",
    "city" : "seoul",
    "grade" : "A"
    }
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print("name" in e )
print("seoul" in e.values())
