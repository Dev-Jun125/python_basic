#문자형

str1 = "hello python!"
print(str1)
print(len(str1))

#이스케이프 문자
print('I\'m Dongjun')
#개행문자, 탭, \

#raw string 
raw_1 = r'D:\python'
print(raw_1)

#멀티라인 입력
multi_str = """
11111111111111111111111111111111111111111111111111111111111111111
222222222222222222222222222222222222222222222222
3333333333333333333333333333333333333
44444444444444444444444444444444444444444444444444
555555555555555555555555555555555
"""
print(multi_str)

#문자열 연산
print(str1 * 3)
print('y' in str1)
sum = 0
print(str1[1])
for i in range(len(str1)):
    if 'h' in str1[i]:
        sum = sum + 1
    
print(sum) 

#문자열 형 변환
print(str(66), type(str(66)))

#문자열 함수
print(str1.capitalize()) # 첫문자 대문자로
print(str1.endswith("!")) #마지막 문자 확인
print(str1.replace("hello","Bye"))
print(sorted(str1))
print(str1.split(' '))

#반복(시퀀스)

print(dir(str1))
for i in str1:
    print(i)

#슬라이싱
print(str1[0:3])
print(str1[-7:])
print(str1[:-1])
print(str1[0:10:4])
print(str1[::-1])

#아스키 코드 (or 유니 코드)
a = 'a'
print(a)
print(ord(a))
print(chr(97))
