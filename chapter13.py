#사용자 입력
#input
#기본 타입 -> str

name = input('enter your name : ')
grade =  input('enter your grade : ')
company = input('enter your company : ')

print(name, grade, company)

number = input('enter number : ')
print(number * 3)

number1 = int(input('enter number : '))
number2 = int(input('enter number : '))

print(number1 + number2)

floatNum = float(input('enter float : '))
print('input float :',floatNum)
print('input type', type(floatNum))

print("FirstName - {0}, LastName - {1}".format(input('Enter first name : '), input('Enter last name : ')))