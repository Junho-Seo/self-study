###OOP2

## 상속
# 상속 Inheritance
#   기존 클래스(부모 클래스)의 속성과 메서드를 물려받아
#   새로운 하위 클래스를 생성하는 것
# 상속이 필요한 이유
#   1. 코드 재사용: 기능을 그대로 가져오면서 중복 코드를 줄임
#   2. 계층 구조: 관계를 표현하고 더 구체적인 클래스를 만들 수 있음.
#   3. 유지 보수의 용이성: 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화 할 수있음.

# 클래스 상속
# 상속 없이 구현하는 경우
#   학생/교수 정보를 별도 표기하기 어려움
#   학생/교수 클래스로 분리했지만 메서드가 중복으로 정의될 수 있음.
# 상속 없는 경우 - 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk()  # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk()  # 반갑습니다. 박교수입니다.


# 상속 없는 경우 - 2
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')

# 상속을 사용한 계층구조 변경
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()  # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk()  # 반갑습니다. 김학생입니다.

# 다중 상속
#   둘 이상의 상위 클래스로부터 상속받을 수 있는 것
#   중복된 속성이나 메서드가 있는 경우 '상속 순서'에 의해 결정됨
#   person - Mom -  FirstChild
#           └Dad┘
# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    def __init__(self, name, age, address):
        Dad.__init__()

    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
# print(baby1.gene)  # XY
#   상속의 순서 Dad, Mom 순으로 상속받았으므로 중복 속성은 Dad에서 가져옴

# 다이아몬드 문제
# 파이썬에서의 해결책
#   MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록을 생성.
#   깊이 우선, 왼쪽에서 오른쪽으로, 계층구조에서 겹치는 같은 클래스를 두번 검색하지 않음
#   그래서, 속성이 D 에서 발견되지 않으면, B 에서 찾고,
#   거기에서도 발견되지 않으면, C 에서 찾고, 이런 식으로 진행됨.
#       class D(B, C):
#           pass

# MRO (Method Resolution Oerder; 메서드 결정 순서)
# super()
#   부모 클래스 객체를 반환하는 내장 함수
# super 사용 전
#%%
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

# super 사용 예시 - 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id, gpa):
        super().__init__(name, age, number, email) # super에서는 self 사용하지 않음. 주의.
        self.student_id = student_id
        self.gpa = gpa


#%%
# super 사용 예시 - 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()
        self.value_c = 'Child'

child1 = Child()
print(child1.value_a) # ParentA
print(child1.value_c) # Child
print(child1.value_b) # AttributeError

#@@ 클래스, 스태틱 메서드도 동일하게 상속 적용가능함.
# 클래스 메서드에서의 예시
# 자식 클래스에서 부모 클래스의 클래스 메서드 호출
class Animal:
    total_count = 0

    def __init__(self, name):
        self.name = name
        Animal.total_count += 1

    @classmethod
    def get_total_count(cls):
        return f'전체 동물 수: {cls.total_count}'


class Dog(Animal):
    dog_count = 0

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        Dog.dog_count += 1

    @classmethod
    def get_dog_info(cls):
        # cls.get_total_count()는 부모 클래스의 클래스 메서드를 호출하여 전체 동물 수를 출력
        return f'{cls.get_total_count()}, 강아지 수: {cls.dog_count}'


class Cat(Animal):
    cat_count = 0

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        Cat.cat_count += 1

    @classmethod
    def get_cat_info(cls):
        # cls.get_total_count()는 부모 클래스의 클래스 메서드를 호출하여 전체 동물 수를 출력
        return f'{cls.get_total_count()}, 고양이 수: {cls.cat_count}'


dog1 = Dog('멍멍이', '삽살개')
dog2 = Dog('바둑이', '진돗개')
print(Dog.get_dog_info())  # 출력: 전체 동물 수: 2, 강아지 수: 2


cat1 = Cat('노아', '페르시안')
cat2 = Cat('루비', '코숏')
print(Cat.get_cat_info())  # 출력: 전체 동물 수: 4, 고양이 수: 2

# mro()메서드
#   해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
class A:
    def __init__(self):
        print('A Constructor')


class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')


class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')


# [<class '__main__.D'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.A'>,
# <class 'object'>]
print(D.mro()) 

# MRO가 필요한 이유
#   - 부모 클래스들이 여러 번 액세스 되지 않도록,
#     각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고
#     각 부모를 오직 한 번만 호출하고,부모들의 우선순위에 영향을 주지 않으면서
#     서브 클래스를 만드는 단조적인 구조 형성
#   - 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도움
#   - 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상
# super의 2가지 사용 사례
#   단일 상속 구조
#       - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로,
#         코드를 더 유지 관리하기 쉽게 만들 수 있음
#       - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면
#         코드 수정이 더 적게 필요
#   다중 상속 구조
#       - MRO를 따른 메서드 호출
#       - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지

## 에러와 예외
# 디버깅
# 버그
#   소프트웨어에서 발생하는 오류 또는 결함
#   프로그램의 예상된 동작과 실제 동작 사이의 불일치
# 디버깅
#   소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
#   프로그램의 오작동 원인을 식별하여 수정하는 작업
# 디버깅 방법
#   - print 함수 활용
#   - 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
#   - [Python tutor](https://pythontutor.com/) 활용 (단순 파이썬 코드인 경우)
#   - 뇌 컴파일, 눈 디버깅 등
# 에러
#   - 프로그램 실행 중에 발생하는 예외 상황
# 에러 유형
#   - 문법 에러 `Syntax Error`
#     - 프로그램의 구문이 올바르지 않은 경우 발생 <br>(오타, 괄호 및 콜론 누락 등의 문법적 오류)
#   - 예외 `Exception`
#     - 프로그램 실행 중에 감지되는 에러
# 예외
#   - 프로그램 실행 중에 감지되는 에러
# 내장 예외
#   - 예외 상황을 나타내는 예외 클래스들
#   - 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용
#@@ 무한루프 걸렸을 경우 ctrl+c 또는 Delete를 연타하면 강제종료함.


## 예외 처리
# 예외 처리 Exception Handling
#   - 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고,
#     적절하게 처리할 수 있도록 하는 방법
# 예외 처리 사용구문
#   try: 예외가 발생할 수 있는 코드 작성
#   except: 예외가 발생했을 때 실행할 코드 작성
#   else: 예외가 발생하지 않았을 때 실행할 코드 작성
#   finally: 예외 발생 여부와 상관없이 항상 실행할 코드 작성
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')

# try-except 구조
try:
    reult = 10/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
# except 뒤에 아무것도 안 쓰면 모든 예외에 대해 출력.

try:
    num = int(input('숫자입력: '))
except ValueError:
    print('숫자가 아닙니다.')

# 복수 예외처리1
try:
    num = int(input('100을 나눌 값을 입력하시오: '))
    print(100/num)
        # 먼저 발생 가능한 에러가 무엇인지 예상해보기
        # 문자열, 0 등
except (ValueError, ZeroDivisionError):
    print('제대로 입력해주세요.')

# 복수 예외처리2
try:
    num = int(input('100을 나눌 값을 입력하시오: '))
    print(100/num)
except (ValueError):
    print('숫자를 입력하시오.')
except (ZeroDivisionError):
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')

# else & finally
#   예외가 발생하지 않았을 때 추가 작업을 진행
#   예외 발생 여부와 상관없이 항상 실행할 코드를 작성
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')

## 참고
# 예외처리 주의사항
#   내장 예외의 상속 계층 구조 주의
#       - 아래와 같이 예외를 작성하면
#       코드는 2번째 except 절에 이후로 도달하지 못함 
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except BaseException:
    print('숫자를 넣어주세요.')
# 하단 블록에 도달하지 못함
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
#   내장 예외 클래스는 상속 계층구조를 가지기 때문에
#   except절로 분기 시 "반드시 하위 클래스를 먼저 확인할 수 있도록 작성"

# 예외 객체 다루기
# 예외 객체: 예외가 발생했을 때 예외에 대한 정보를 담고있는 객체
# as 키워드
    my_list = []

    try:
        number = my_list[1]
    except IndexError as error:
        print(f'{error}가 발생했습니다.')

    # list index out of range가 발생했습니다.

# try-except와 if-else 함께 사용가능하다.
try:
    x = int(input('숫자를 입력하세요: '))
    if x < 0:
        print('음수는 허용되지 않습니다.')
    else:
        print('입력한 숫자:', x)
except ValueError:
    print('오류 발생')

# 예외 처리와 값 검사에 대한 2가지 접근 방식
# 1. EAFP (Easier to Ask for Forgiveness than Permission)
#     예외 처리를 중심으로 코드를 작성하는 접근 방식
#     "일단 실행하고 예외를 처리"
#     try-except
#   - 예외 상황을 예측하기 어려운경우에 유용 (백엔드 서버 관리에 활용 예정)
# 2. LBYL (Look Before You Leap)
#     값 검사를 중심으로 코드를 작성하는 접근 방식
#     "실행하기 전에 조건을 검사"
#     if-else
#   - 예외 상황을미리 방지하고 싶을 때 유용

# EAFP
my_dict = {}
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

# LBYL (일반적인 상황에서는 주로 이 방식 이용)
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')


# %%
### 파이썬 과목 종료
# 우리가 배운 것
#   새로운 사고방식을 익히는 과정
# 지속적인 Python 학습
#   알고리즘 학습: 논리적 사고와 문제 해결 능력 키우기
#   코드 리뷰: 다른 사람의 코드를 읽고 분석하는 습관 들이기
#   프로젝트 기반 학습: 관심있는 주제로 작은 프로젝트 시작하기

#%%
# 시험은 교안에서 출제.
# 단답식 서술형. 아는대로 길게 적기!
# ex class 상속에 대해 설명하라