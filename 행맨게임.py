# 행맨 게임 제작



import time
import csv
import random
import winsound # 음악 재생
# 처음 이름 입력 받기 및 인사
name = input('What is your name?')

print('Hello ', name, "Time to play hangman game!")
print()
time.sleep(1)

print("Start Loading")
print()
time.sleep(0.5)

words = [] # 워드에 넣을 공간 만들어 놓기
# 워드 랜덤 추출
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 헤더 스킵
    for c in reader : 
        words.append(c)

q = random.choice(words)
word = q[0].strip()


#추측 단어
guess = ''
guesses = ''
#기회
turns = 10

# 본 문

while turns >0:
    failed = 0 # 실패 횟수

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내 추축 문자가 포함된 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end='')
        else:
            print("_", end=' ')
            failed +=1

    if failed ==0:
        print()
        print('Congraturations! The Guesses is correct!')
        break
    print()

    
    # 추측 단어 문자 단위 입력
    print()
    guess = input("guess a charater : ")
    
    # 사용자가 입력한 알파벳 추가
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -=1
        # 오류 메시지
        print('Oops! ')

        #남은 기회
        print("you have", turns, 'more guesses!')

        if turns == 0:
            print("You hangman game failed. Bye~")
