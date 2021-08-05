# 파이썬 외장 함수
# 실제 프로그램 개발 중 자주 사용
# ex) sys, pinckle, shutil, temfile, time, random

import sys
print(sys.argv)

#강제 종료
#sys.exit()

#파이썬 패키지 위치
print(sys.path)

#pickle : 객체 파일 쓰기
import pickle

#쓰기
f = open("test.obj", 'wb')
obj = {1 : 'python', 2 : 'study', 3 : 'basic'}
pickle.dump(obj,f)
f.close()

#읽기
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close

# os : 환경 변수, 디렉터리(파일) 처리 관련, 운영체제 작업 관련 

import os
print(os.environ) 
print(os.environ["USERNAME"])

#현재 경로
print(os.getcwd())

#time : 시간 관련 처리
import time

print(time.time())
print(time.localtime(time.time()))
print(time.localtime())
print(time.ctime())
print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime()))  # 형식 지정

#시간 간격 발생
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random 난수
import random

print(random.random()) # 0~1 실수 난수 발생
print(random.randint(1,45))
print(random.randrange(1,45))  #1~45 랜덤 정수

# 셔플
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# 랜덤 선택
c = random.choice(d)
print(c)

# webbrowser : os 웹 브라우저 실행
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.co.kr")
webbrowser.open_new_tab("http://google.co.kr")