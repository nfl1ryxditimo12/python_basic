# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1

while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is :", v2)

for v3 in range(1, 11):
    print("v3 is :", v3)

# 1 ~ 100 까지의 합

sum1 = 0
cnt1 = 0

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print("1 ~ 100 까지의 합 :", sum1)
print('1 ~ 100 :', sum(range(1, 101)))
print('1 ~ 100 :', sum(range(0, 101, 2)))       # 1 부터 100 까지의 짝수의 총 합, range(시작값, 끝값, 건너뛸 값)

print("\n\n\n")

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['Kim', 'Park', 'Cho', 'Choi', 'Yoo']

for name in names:
    print("You are name :", name)

word = "dreams"

for s in word:
    print("Word :", s)

my_info = {
    "name": "Kim",
    "age" : 33,
    "city": "Seoul"
}

# 키
for key in my_info:
    print("my_info : ", key)
print()

# 값
for key in my_info.values():
    print("my_info : ", key)
print()

# 키
for key in my_info.keys():
    print("my_info : ", key)
print()

# ('키', '값')
for key  in my_info.items():
    print("my_info : ", key)
print()

# 키 값
for key, v  in my_info.items():
    print("my_info : ", key, v)

print("\n\n\n")

name = "KennRY"

for n in name:
    if n.isupper():                     # isupper 은 문자가 대문자인지 판별하는 함수, islower 은 문자가 소문자인지 판별하는 함수
        print(n.lower(), end='')                # 문자를 소문자로 바꾼다.
    else:
        print(n.upper(), end='')                # 문자를 대문자로 바꾼다.
print()


# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")

# for - else 구문 (반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# for 문 안에 break 가 있으면 else 구문이 실행되지 않고
# for 문 안에 break 가 없으면 else 구문이 실행 된다.

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")
else:
    print("Not found 33......")

print("\n\n")

# continue
# continue 를 만나면 밑의 문장은 수행하지 않음

lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 :", type(v))

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))