#파이썬 변수

#선언
a=700
#출력
print(a)

x = y = z = 100
print(x,y,z)

print(type(x))

#파이썬에 변수 고유 값 확인해보기
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m)==id(n))
 
#변수 선언 시
#Camel Case : numberOfCollegeGraduates -> Method에서 주로 사용
#Pascal Case : NumverOfCollegeGraduates -> Class 선언 시 주로
#Snake Case : number_of_college_graduates
#_시작 변수, _로 끝나는 변수, _, $로 시작하는 변수 등 가능
# 특수문자, 숫자로 시작하는 변수 불가
#예약어 사용 불가


