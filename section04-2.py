# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String

raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인

multi = \
"""
문자열
멀티라인
테스트
"""         # 문자열 멀티라인일 때 """를 다음 줄에 쓰고 싶으면 \ 표시를 해야한다.

print(multi)

# 문자열 연상

str_o1 = "*"
str_o2 = "abc "
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print('a' in str_o4)        # 'a' 가 str_o4 에 포함이 되냐? 를 묻는 연산자 in
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환

print(str(77) + 'a')
print(str(10.4))

print('\n\n')

# 문자열 함수

# a = 'niceman'
# b = 'orange'

# print(a.islower())      # 문자열 내 소문자로만 이루어져 있으면 True
# print(b.endswith('e'))  # 문자열 끝이 뭐로 끝나는지에 따른 값 반환
# print(a.capitalize())   # 문자열 내 첫 글자를 대문자로 바꿔주는 함수
# print(a.replace('nice', 'good')) # 문자열의 특정 글자를 바꿔주는 함수
# print(list(reversed(b)))         # 문자열을 뒤바꿔주는 함수 ( list로 형변환을 해야함!! )

a = 'niceman'
b = 'orange'

print(a[0:3])           # 0 - 2 까지 출력
print(a[:4])            # 0 - 3 까지 출력
print(a[0:])            # 0 - 끝까지 출력
print(a[0:len(a)])      # 0 - a의 길이까지 출력 ( 끝까지 )
print(a[:])             # 처음부터 끝까지 출력

print(b[0:4:2])         # 3번째 수만큼 건너뜀
print(b[1:-2])          # r 부터 -2 전까지, 즉 n 까지 출력
print(b[::-1])          # 끝에서 처음까지 출력