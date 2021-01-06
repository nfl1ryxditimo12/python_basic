# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function(parameter):
#     code

# 함수 호출
# function(parameter)

# 함수 선언 위치 중요!!!


# 예제 1

def hello(world):
    print("Hello", world)

hello("python")
hello(777)

# 예제 2

def hello_return(world):
    val = "Hello " + str(world)
    return val

func = hello_return("Python!!!!!")
print(func)

# 예제 3 (다중리턴)

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1), val2, val3)

# 예제 4 (데이터 타입 반환)

def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt[0]))

# 예제 5
# *args, *kwargs

def args_func(*args):                   # args 는 매개변수가 몇 개 올지 모르는 상황에서
    # print(args)                       # 들어오는 모든 매개변수를 튜플로 리턴함
    # for t in args:
    #     print(t)
    
    for i, v in enumerate(args):   # enumerate 함수는 인덱스를 표시해준다.
        print(i, v)

args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'Lee')

print('\n\n\n')

# kwargs
# * 이 하나만 들어올 경우 튜플
# * 이 두개 들어올 경우 딕셔너리로 반환

def kwargs_func(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1 = 'Kim')
kwargs_func(name1 = 'Kim', name2 = 'Park', name3 = "Lee")

print("\n\n\n")

# 전체 혼합

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1 = 24, age2 = 35)

print("\n\n")


# 예제 6
# 중첩 함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print(">>>", num)

    print("in func")
    func_in_func(num + 1000)

nested_func(10000)

# 예제 7 (hint)

def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]

print(func_mul3(5))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당

def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda num: num * 10

print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    print( x * y * func(10))

func_final(10, 10, lambda_mul_10)

# 한번만 사용 할 경우 바로 람다식을 만들어서 사용 할 수 있다.

print(func_final(10, 10, lambda x : x * 1000))