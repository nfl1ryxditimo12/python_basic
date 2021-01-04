# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱

print(d[3])
print(d[-2])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱

print(d[0:2])
print(e[2][1:3])

# 연산

print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]       # 슬라이싱 하여 리스트에 넣으면 동일한 리스트로 들어간다.
print(c)

c[1] = ['a', 'b', 'c']            # 하지만 그냥 인덱스로 설정하고 값을 넣으면 리스트 안에 리스트로 변경 된다.
print(c)

del c[1]
print(c)

del c[-1]
print(c)

print('\n\n\n')

# 리스트 함수

y = [5, 2, 3, 1, 4]
print(y)

y.append(6)             # 리스트 끝에 숫자를 삽입
print(y)

y.sort()                # 리스트를 오름차순으로 정렬
print(y)

y.reverse()             # 리스트를 내림차순으로 정렬
print(y)

y.insert(1, 10)         # 리스트에 (위치, 값) 을 대입
print(y)

# del 은 y[인덱스] 를 지우지만
# remove 는 (값) 을 지운다
y.remove(2)
y.remove(10)
print(y)

y.pop()                 # 맨 마지막 값을 지운다
print(y)

# append(ex) 를 할 경우 리스트가 추가 되지만
# extend(ex) 를 하면 값이 추가가 된다.
ex = [88, 77]
y.extend(ex)            # (변수) 가 리스트인 경우 리스트 끝에 연장시킨다.
print(y)


# 삭제 : del, remove, pop

print('\n\n\n')

# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c[2]            # 튜플은 삭제할 수 없다

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:3])

print(c + d)
print(c * 3)

print('\n\n')

# 튜플 함수

z = (5, 2, 1, 3, 4, 1)

print(z)
print(3 in z)               # 3 이 튜플 안에 있으면 True
print(z.index(5))           # 값 5의 인덱스를 출력
print(z.count(1))           # 1의 개수를 출력