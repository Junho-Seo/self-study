###OOP


##객체 지향 프로그래밍

# 절차 지향 프로그래밍 Procedual Programming
#   프로그램을 '데이터'와 '절차'로 구성하는 방식의 프로그래밍 패러다임
#   특징
#    '데이터'와 '함수(절차)'가 분리되어 있으며 함수 호출의 흐름(순서)가 중요하다.
#   소프트웨어 위기 Software Crisis
#    하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격
#    하드웨어의 발전 속도가 너무 빨라서 생긴 현상
#   따라서 OOP가 등장.
# 객체 지향 프로그래밍 Object Oriented Programming
#   데이터와 해당 데이터를 조작하는 메서드(메시지)를 하나의 객체(클래스)로 묶어 관리하는 방식의 프로그래밍 패러다임
# 절차 지향 vs 객체 지향
#   함수 호출의 흐름이 중요 vs 객체 간 상호작용과 메세지 전달이 중요

## 객체
# 클래스 class
#   파이썬에서 '타입'을 표현하는 방법
#   객체를 생성하기 위한 설계도
#   데이터와 기능을 함께 묶는 방법을 제공
# 객체 Object
#   클래서에서 정의한것을 토대로 메모리에 할당된 것
#   '속성'과 '행동'으로 구성된 모든 것
#   예시 (교안참조)

## 인스턴스
# 클래스와 객체
#   가수(클래스) -> 객체(아이유, BTS 등)
#   클래스로 만든 객체를 '인스턴스'라 부름
#   아이유는 객체다(o)
#   아이유는 인스턴스다(x)
#   아이유는 가수의 인스턴스다(o)
# 인스턴스 instance
#   클래스의 속성과 행동을 기반으로 생성된 개별 객체
#   클래스를 만든다 == 타입을 만든다
# 변수 name의 타입은 str 클래스다.
#   변수 name은 str 클래스의 인스턴스이다.
#   우리가 사용해왔던 데이터 타입은 사실 모두 클래스였다.
#   결국 문자열 타입의 변수는 str클래스로 만든 인스턴스다.
# '', 'hello', '파이썬' -> 문자열 타입(클래스)의 객체(인스턴스)
# [1, 2, 3] -> 리스트 타입(클래스)의 객체(인스턴스)
# 'hello'.upper()
#   ->문자열.대문자로()
#   ->객체.행동()
#   ->인스턴스.메서드()
#@@ 과거의 절차 지향이라면upper 함수가 중점이고 그 안에 데이터를 넣는다.
#@@ 현재의 객체지향은 데이터가 더 중점이 된다.
# 하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.
# 객체 정리
#   타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가?
#   속성(attribute): 어떤 상태(데이터)를 가지는가?
#   조작법(method;메서드): 어떤 행위(함수)를 할 수있는가?

##클래스
# 클래스 Class
#   파이썬에서 타입을 표현하는 방법
#   객체를 생성하기 위한 설계도
#   데이터와 기능을 함께 묶는 방법을제공
# 클래스 정의
#   class 키워드
#   클래스 이름은 파스칼 케이스(Pascal Case) 방식으로 작성
#       class MyClass:
#           pass
#@@ 기존 사용하던 방식은 스네이크 케이스 (Snake Case)
#@@ 언더바가 들어가는 위치에 언더바 대신 대문자를 사용
#@@ 함수와 클래스를 구분하기위해.
#@@ 카멜케이스 라고도 부름
#%%
# 클래스 정의
class Person:
    ## 속성
    blood_color = 'red'
    ## 메서드
    # 초기값이 필요하다는 의미의 함수
    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')

# (인스턴스) 메서드 호출
print(singer1.singing()) # iu가 노래합니다.

# 속성(변수) 접근
print(singer1.blood_color) # red

# 인스턴스 속성(변수)
print(singer1.name) # iu

#%%
## 클래스 구조
# 생성자 메서드
#   객체를 생성할 때 자동으로 호출되는 특별한 메서드
#   __init__: initialization; 초기화
#   생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
# 인스턴스 변수
#    - 인스턴스(객체)마다 별도로 유지되는 변수
#    - 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨
# 클래스 변수
#    - 클래스 내부에 선언된 변수
#    - 클래스로 생성된 모든 인스턴스들이 공유하는 변수
#인스턴스 메서드
#    - 각각의 인스턴스에서 호출할 수 있는 메서드
#    - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행
#
#%%
##인스턴스 변수와 클래스 변수
#- 가수가 몇 명인지 확인하고 싶다면?
#    - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정할 수 있음

# class.class_variable로 클래스 변수 참조

class Person:
    # 클래스 변수 count
    count = 0

    def __init__(self, name):
        # 인스턴스 변수 name
        self.name = name
        Person.count += 1

person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2

##########################

class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(c1.r) # 5
print(c2.r) # 10

# c1.pi
#   c1에게 pi라는 인스턴스 변수가 있는지를 먼저 확인 -> 없다.
#   없으면 찾으러 위의 클래스로 올라감
#   클래스의 pi를 출력.

# c1의 인스턴스 변수 pi를 생성
c1.pi =100
print(Circle.pi) # 3.14 -> 올바른 방법
print(c1.pi) # 100
print(c2.pi) # 3.14

#%%
## 메서드
# 종류
#   인스턴스(instance), 클래스(class), 정적(static)
# 인스턴스 메서드
#   클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
#   인스턴스의 상태를 조작하거나 동작을 수행
#   약속: 반드시 첫 번째 매개변수로 '인스턴스 자신(self)'(첫 번째 위치 인자)을 전달받음
#        self는 매개변수 이름이므로 변경 가능하지만 다른 이름을 사용하지 않을 것을 강력 권장
#        바꿀 수 있지만 바꾸면 안된다.
#   self 동작 원리
#       실제 파이썬 내부 동작에 따르면 무조건 필요한 인자
#       고민할 필요 없이 무조건 self(자기 자신)으로 시작
#   'hello'.upper() -> 객체 지향 방식의 메서드로 호출하는 표현(단축형 호출)
#   str.upper('hello') -> 실제 파이썬 내부 동작(절차 지향에 가까움)
# 생성자 메서드
#   인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
#   인스턴스 변수들의 초기값을 설정
class Person:
    def __init__(self, name):
        # 왼쪽 name: 인스턴스 변수 name
        # 오른쪽 name: 함수(생성자 메서드)의 매개변수 이름 (들어오는 인자값)
        # 둘은 다르다. 전혀 관계없음. 이름 변경 가능. ex. self.ssafy = name
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요. {self.name}입니다.')

person1 = Person('준호') # 인스턴스가 생성되었습니다.
person1.greeting() # 안녕하세요. 준호입니다.
# 위의 단축형 호출을 풀어내면
# Person.greeting(person1) 으로 내부 작동
# 위처럼 쳐도 같은 결과 출력됨

# 클래스 메서드
#   클래스가 호출하는 메서드
#   클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
# @classmethod 데코레이터를 사용하여 정의
#@@ 데코레이터: 함수를 꾸미는(기능을 추가하는) 함수
# 호출 시, 첫번째 인자로 호출하는 클래스(`cls`)가 전달됨
#@@ 인스턴스 메서드와 마찬가지로 cls라는 변수는 변경 가능하지만 절대 변경하면 안 된다. 주의.

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    # 하위 클래스(상속)을 이용하기위해 Person을 사용하지않고
    # 클래스 메서드 사용
    @classmethod
    def number_of_population(cls):
        print(f'인구 수는 {cls.count}입니다.')


person1 = Person('iu')
person2 = Person('BTS')

# 여기서 cls가 결정된다.
# 이 위에 단계에서는 cls가 뭔지 모름
Person.number_of_population() # 인구 수는 2입니다.

# 스태틱(정적) 메서드
#   클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
#   주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용
# @staticmethod 데코레이터를 사용하여 정의
# 호출 시 필수적으로 작성해야 할 매개변수가 없음.
#   즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용
#%%
class StringUtils:
    # 교안에는 자리가 없어 생략함
    # 파이썬에선 자동으로 붙여줘서 작동하지만
    # pass 하더라도 써주는 것을 권장
    def __init__(self):
        pass

    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()

text = 'hello, world'

result1 = StringUtils.reverse_string(text)
print(result1) # dlrow ,olleh

##메서드 정리
# 인스턴스 메서드 self
#    인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행
# 클래스 메서드 @classmethod + cls
#    인스턴스의 상태에 의존하지 않는 기능을 정의
#    클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
# 스태틱 메서드 @staticmethod
#    클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

# 누가 어떤 메서드를 사용해야 할까?
#   코드의 유지보수와 협업을 위한 약속
# 클래스가 사용해야 할 것
#    클래스 메서드
#    스태틱 메서드
# 인스턴스가 사용해야 할 것
#    인스턴스 메서드
#%%
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
# 모든 메서드 호출 가능하지만
# 클래스 메서드와 스태틱 메서드만 사용하도록 한다!!
print(MyClass.instance_method(instance)) # 사용x
print(MyClass.class_method())
print(MyClass.static_method())

# 인스턴스가 할 수 있는 것
# 마찬가지로 모든 메서드 호출 가능하지만
# 인스턴스 메서드만 사용하도록 한다!!
print(instance.instance_method()) 
print(instance.class_method()) # 사용x
print(instance.static_method()) # 사용x

# 할 수 있다 != 써도 된다
# 각자의 메서드는 OOP 패러다임에 따라 명확한 목적에 맞게 설계된 것이기 때문에
# 클래스와 인스턴스 각각 올바른 메서드만 사용한다.

##참고
# 인스턴스와 클래스 간의 이름 공간
#   클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
#   인스턴스를 만들면, 인스턴스 객체가 생성되고 "독립적인" 이름 공간 생성
#   인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색
#@@ 교안의 예시 보면 이해 쉬움
# 독립적인 이름 공간이 가지는 이점
#   각 인스턴스는 독립적인 메모리공간을 가지며, 클래스와 다른 인스턴스 간에는
#   서로의 데이터나 상태에 직접적인 접근이 불가능.
#   객체지향 프로그래밍의 중요한 특성 중 하나.
#   클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장.
#   서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음.
#       -> 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움.

# 매직 메서드
#   인스턴스 메서드
#   특정 상황에 자동으로 호출되는 메서드
#   __가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
#   스페셜 메서드 또는 매직 메서드라고 불림
# ex. __str__(self)
#       내장함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경

# 데코레이터
#   다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

# 절차 지향과 객체 지향은 대조되는 개념이 아니다!
#   절차 지향의 토대 위에 쌓인, 이점을 가지는 패러다임 -> 객체 지향
