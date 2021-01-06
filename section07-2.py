# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 정류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    
    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용

model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)         # super
print(model1.type)          # super
print(model1.car_name)      # sub
print(model1.show())        # super class
print(model1.show_model())  # sub
print(model1.__dict__)

# Method Overriding(오버라이딩)
# 슈퍼클래스에 있는것을 모두 사용하는게 아니라
# 서브클래스에 있으면 서브클래스에 있는 것을 사용함

model2 = BenzCar("GLC_Coupe", 'suv', 'black')

print(model2.show())

# Parent Method Call

model3 = BenzCar('Amg63', 'sedan', 'silver')

print(model3.show())

# Inheritance Info

print(BmwCar.mro())
print(BenzCar.mro())

print("\n\n")


# 예제 2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(A, B, Z):
    pass

# M 클래스는 A, B, Z를 상속 받았고
# A 클래스는 X, Y를 상속 받았고
# B 클래스는 Y, Z를 상속 받아서
# X, Y, Z
# A, B
# M
# 이렇게 정의된다

print(M.mro())

print(A.mro())