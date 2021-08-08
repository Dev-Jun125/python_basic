# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로('../../~~~'), 절대 경로('C:/user/.....')

# 파일 읽기

f = open('./resource/it_news.txt', 'r', encoding = 'UTF-8')
print(dir(f))
print(f.encoding)
print(f.name)
print(f.mode)
cts = f.read()
print(cts)
f.close()

# with 문 사용

with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
print()

# read() : 전체 읽기 바이트 수 제한 가능
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c) # 커서가 존재 마지막에 읽은 곳을 기억함
    f.seek(0,0)
    c = f.read(20)
    print(c)
print()

# 한 줄 씩 읽기 개행문자 전까지
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
print()

# readlines 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end="")
print()

# 파일 쓰기

with open('./resource/djWriteTest.txt', 'w') as f:
    f.write('I love Python\n')

with open('./resource/djWriteTest.txt', 'w') as f: #w로 모드를 하면 이전 거 지워지고 현재 쓰는 거만 a 추가모드로 해야 뒤에 이어붙임
    f.write('I love Python2\n')

with open('./resource/djWriteTest.txt', 'a') as f:
    f.write('I love Python3\n')


# writelines : 리스트 -> 파일
with open('./resource/djWriteTest2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Bananan\n', 'Melon\n']
    f.writelines(list)

# 
with open('./resource/djWriteTest3.txt', 'w') as f:
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)

