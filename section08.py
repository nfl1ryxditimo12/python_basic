# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1 (클래스)

from pkg.fibonacci import Fibonacci
# pkg 폴더의 fibonacci.py 에서 Fibonacci 클래스 임포트

Fibonacci.fib1(300)

print("ex1 :", Fibonacci.fib2(400))
print("ex1 :", Fibonacci().title)

print()

# 사용2 (클래스)
# 이 방법은 사용하지 않는 클래스를 모두 불러와서 메모리 절약에 도움이 안됨
# 이 방법은 되도록 권장하지 않음

from pkg.fibonacci import *
# pkg 폴더의 fibonacci.py 에서 모든 클래스 임포트

Fibonacci.fib1(500)

print("ex2 :", Fibonacci.fib2(600))
print("ex2 :", Fibonacci().title)

print()

# 사용3 (클래스)
# import 클래스 as 원하는 이름 을 넣으면 긴 클래스 명을 짧게 사용할 수 있다.
# 이 방법은 가독성을 높일 수 있어 권장된다.

from pkg.fibonacci import Fibonacci as fb
# pkg 폴더의 fibonacci.py 에서 Fibonacci 클래스 임포트
# 대신 Fibonacci 클래스 이름이 너무 기니까 as 를 사용해 fb로 사용함

fb.fib1(1000)

print("ex3 :", fb.fib2(1600))
print("ex3 :", fb().title)

print()

# 사용4 (함수)

import pkg.calculations as c
# pkg 폴더의 모든 calculations 함수를 임포트
# 대신 calculations 함수가 너무 기니까 as를 사용해 c로 사용

print("ex4 :", c.add(10, 100))
print("ex4 :", c.mul(10, 100))

print()

# 사용5 (함수)
# 내가 사용할 만큼만 import 해오는게 좋음

from pkg.calculations import div as d
# pkg 폴더의 calculations.py 에서 div 메서드만 사용
# as를 사용해 d 로 변경

# 나누기를 하면 float로 돼서 int로 변경
print("ex5 :", int(d(100, 10)))

print()

# 사용6 (함수)

import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(builtins))