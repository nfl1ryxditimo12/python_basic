# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언

# class 클래스명:
#     함수
#     함수
#     함수


# 예제 1

class UserInfo:
    # 속성, 메소드
    def __init__(self, name, height, weight, address):
        self.name = name
        self.height = height
        self.weight = weight
        self.address = address
    
    def user_info_p(self):
        print("Name :", self.name)
        print("Height :", self.height)
        print("Weight :", self.weight)
        print("Address :", self.address)

# 네임스페이스
user1 = UserInfo("Kim", '170cm', '70kg', '천안')
print(user1.name)
# 결과 : 'Kim'
user1.user_info_p()

user2 = UserInfo("Park", '175cm', '75kg', '천안')
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

print("\n\n\n")

# 예제 2
# self의 이해

class SelfTest:
    def function1():
        print("function1 called!")
    def function2(self):
        print(id(self))
        print("function2 called!")

self_test = SelfTest()              # 객체 생성
# self_test.function1()             # function1은 self 인자가 없어서 인스턴스 메소드가 아니고 클래스 메소드 이다.
SelfTest.function1()                # 그래서 클래스.function1() 로 불러야 된다
self_test.function2()               # function2는 self 인자를 갖고 있기 때문에 인스턴스로 사용 가능하다.

print(id(self_test))                # 인스턴스 id와 function2의 id는 동일하다
SelfTest.function2(self_test)

# 클래스 변수는 self 가 없고 인스턴스 변수는 self 가 있다

# 클래스 변수 :
# def function():
#     pass

# 인스턴스 변수 :
# def function(self):
#     pass

# 클래스 변수는 클래스로 직접 호출해야 하지만
# 인스턴스 변수는 클래스로 직접 호출이 안되고
# 객체를 찍어낸 후에 호출이 가능하다

print("\n\n\n")

# 예제 3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)       # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

del user1

# 자기 네임스페이스에 없으면 클래스 네임스페이스에서 찾고 거기에도 없으면 에러가 발생
print(user2.stock_num)
print(user3.stock_num)

