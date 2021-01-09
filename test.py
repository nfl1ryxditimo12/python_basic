# print('Hello python!')

s = "a123"

for i in s:
    if type(i) != int():
        print("정수로만 이루어져 있지 않음")
    else:
        print("정수로만 이루어져있음")