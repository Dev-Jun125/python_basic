#파이썬 출력

print('hello', end ='\t')
print("hello", end ='\t')
print('''hello world''', end = '\t')
print("""hello world""")

#separator
print('P', "Y", 'T', "H", 'O', 'N', sep = ',')

print('%s %s' %('one','two'))
print('{} {}'.format('one','two'))
# 정렬
print('{:^100}'.format('good'))
# 글주 수 까지 출력
print('%.5s' % ('abcdefghijkl'))

print('%06.2f'%(3.12512312512321))
