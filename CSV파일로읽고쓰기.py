# csv로 파일 읽고 쓰기
# 데이터사이언스나 전처리에서 자주 사용
# CSV : MEME - text/csv
# CSV 콤마로 주로 구분 사용자따로 다를 수 있음
import csv

with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for i in reader:
        print(i) # 리스트 형태로
        print(' : '.join(i)) # 포맷팅 가능


print()

with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|') # 구분 문자 지정 가능

    for i in reader:
        print(i)

with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader)


    print()

    for i in reader: # 키 벨류로 딕셔너리형태로 한 것을 포맷팅
        for j, k in i.items():
            print(j, k)
        print('----------')
    

    # 쓰기
    w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

    with open('./resource/djWriteCsv1.csv', 'w', encoding = 'utf8') as f:
        print(dir(csv))
        wt = csv.writer(f)

        print(dir(wt))
        print('-----')
        print(type(wt))

        for v in w:
            wt.writerow(v)

    with open('./resource/djWriteCsv2.csv', 'w', encoding = 'utf8') as f:
        fields = ['One', 'Two', 'Three']
        wt = csv.DictWriter(f, fieldnames=fields)
        wt.writeheader()

        for i in w:
            wt.writerow({
                'One' : i[0],
                'Two' : i[1],
                'Three' : i[2]
            })