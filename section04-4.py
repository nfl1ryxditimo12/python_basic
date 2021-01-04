# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리 집합 자료형

# 딕셔너리(Dict, Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MongoDB
# 선언

# 딕셔너리는 키 : 값 구성으로 되어 있고
# 키는 중복 허용이 안된다, 그러나 값은 중복 될 수 있다.

a = {
    'Name': 'kim',
    'Phone': '010-7777-7777',
    'Birth': 870214,
}

b = {
    0: 'Hello Python',
    1: 'Hello Coding',
}

c = {
    'arr': [1, 2, 3, 4, 5]
}

# print(type(a))

# 출력

print(a['Name'])                # 이 방식은 오류가 뜬다
print(a.get('Name'))            # 이 방식은 오류가 안뜬다
print(a.get('address'))         # 대신 None 라고 출력이 된다.
print(c['arr'][1:2])

# 딕셔너리 추가

a['address'] = 'Seoul'
print(a)

a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3,)
print(a)

print('\n\n')

# keys, values, items(키:값 한 쌍)

print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())

print(a.items())

items = list(a.items())
print(items)

print(2 in b)
print('name2' in b)
print(0 in b)
print('Hello' in b)
print('Hello Python' in b)

print('\n\n\n\n\n\n')

# 집합(Sets) (순서x, 중복x)

a = set()
b = set([1, 2, 3, 4])
c = set([1, 2, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)

t2 = tuple(c)
print(t2)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('\n\n\n')

print(s1.intersection(s2))          # 합집합
print(s1 & s2)                      

print(s1 | s2)                      # 교집합
print(s1.union(s2))

print(s1 - s2)                      # 차집합
print(s1.difference(s2))

# 추가 & 제거

s3 = set([7, 8, 10, 15])

s3.add(18)              # set 값 추가
s3.add(7)

print(s3)

s3.remove(15)           # set 값 제거
print(s3)

print(type(s3))