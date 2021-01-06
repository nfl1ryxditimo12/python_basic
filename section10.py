# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

"""====================="""

# SyntaxError : 잘못된 문법

# print('Test)                   # ' 콤마 하나가 빠져서 문법 오류 발생

# if True                        # : 콜론이 빠져서 문법 오류 발생
#     pass

# x => y

"""====================="""

# NameError : 참조변수 없음

a = 10
b = 15

# print(c)                       # c 라는 변수를 못찾아서 NameError 발생

"""====================="""

# ZeroDivisionError : 0 나누기 에러

# print(10 / 0)                  # 0 으로는 나눌수 없어서 오류 발생

"""====================="""

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]

print(x[0])
# print(x[3])                    # 인덱스는 2까지인데 3을 출력하려 해서 범위 오류 발생

"""====================="""

# KeyError

dic = {
    'name': 'Kim',
    'Age' : 33,
    'City': 'Seoul',
}

# print(dic['hobby'])           # hobby 라는 키가 없어서 KeyError 발생
print(dic.get('hobby'))        # 딕셔너리변수.get('키') 로 사용하면 찾는 키가 없어도 None 으로 뜨고 오류는 발생하지 않음

"""====================="""

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time

print(time.time())
# print(time.month())           # 클래스 안에 찾는 메서드가 없으면 AttributeError 발생

"""====================="""

# ValueError : 참조 값이 없을 때 발생

x = [1, 5, 9]

# x.remove(10)                  # 값에 10이 없어서 ValueError 발생
# x.index(10)                   # 인덱스 10이 없어서 ValueError 발생

"""====================="""

# FileNotFoundError

# f = open('test.txt', 'r')     # 경로에 text.txt 파일이 없어서 404 오류 발생

"""====================="""

# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)                  # x 와 y 의 타입이 달라서 연산 불가로 인한 오류
# print(x + z)                  # 마찬가지

# print(x + list(y))            # 형변환을 통해 연산이 가능해진다.

"""====================="""

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1

name = ['kim', 'Lee', 'park']

try:
    z = 'kim' # cho 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not Found it! - Occurred ValueError!')
else:                                                   # 정상 실행시에만 작동
    print('Ok! else!')
print('\n\n')

# 예제 2

name = ['kim', 'Lee', 'park']

try:
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:                                                 # except에 아무것도 안 쓸 경우 모든 에러를 확인한다.
    print('Not Found it! - Occurred Error!')
else:
    print('Ok! else!')
print('\n\n')

# 예제 3

name = ['kim', 'Lee', 'park']

try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:                                                 
    print('Not Found it! - Occurred Error!')
else:
    print('Ok! else!')
finally:                                               # 정상적으로 실행하던 오류가 뜨던 finally는 무조건 작동함
    print("finally Ok!")
print('\n\n')

# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')    
finally:
    print('ok Finally!!!')
print('\n\n')

# 예제 5

name = ['kim', 'Lee', 'park']

try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l:                                # 무슨 에러가 뜬지 알기 쉽게 계층적으로 뜰 것 같은 오류를 작성하는게 좋다
    print(l)
except IndexError:                                           
    print('Not Found it! - Occurred IndexError!')
except NameError:                                           
    print('Not Found it! - Occurred NameError!')
except Exception:                                      # Exception 을 쓰나 안쓰나 똑같지만 앞에 모든 오류들을 먼저 작성하고 마지막에 써야 무슨 오류인지 확인 가능하다.                                           
    print('Not Found it! - Occurred Error!')
else:
    print('Ok! else!')
finally:
    print("finally Ok!")
print('\n\n')

# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Ki'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError                              # if 구문에서 raise로 오류를 직접 만들수 있다.
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('Ok!')