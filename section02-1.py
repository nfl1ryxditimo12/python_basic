# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello Python!")      # 작은따옴표 큰따옴표 둘다 파이썬은 상관이 없다.
print("""Hello Python!""")
print('''Hello Python!''')

print()     # 그냥 쓰면 줄바꿈만 된다

# Separator 옵션 사용
# sep='기준' 기준에 들어오는 문자로 공백을 바꿔준다.

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
# end='기준' 기준에 들어오는 문자를 기준으로 print 문의 끝을 바꿔준다.

print('Welcome To', end='')
print(' the black paradise', end='')
print(' piano notes')
print()

# format 옵션 사용
# {}.format() 소괄호 사이에 문자를 넣으면 중괄호로 출력이 됨.
# {0} {1}.format() 소괄호 첫번째에 들어오는 문자는 {0} 으로 매핑이 된다.

print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

# %s : 문자, %d : 정수, %f : 실수

print('%s\'s favorite number is %d' % ('Seongsu', 777))

# %5d 는 5칸의 공백, %05d 는 5칸을 0으로 채우고
# 4.2f 에서 4는 정수부 공백 2는 소수점 2자리 까지만 표시 하라는 뜻.

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6543.123))

print()

# 탈출 문자 \' \\ \"
print('\'you\'')
print("'you'")
print("\"you\"")
print("\\you\\\n\n\n")
print('\t\t\ttest')

print()

