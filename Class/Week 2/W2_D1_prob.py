# 오늘 학습 내용:리스트, 문자열 메서드
# 내일: dict, set 메서드
# 수,목: OOP -> 입학식 있어서 월, 화에 미리 학습!
# 금요일 관통: 데이터 사이언스 라이브


# 복사
# 모든 프로그래밍 언어에 있는 개념
original = [1, 2, [3, 4, 5]]
# 리스트는 실제로 연속되게 주소에 저장된다. (python tutor 생각하면 됨)

# 할당(== 참조 복사) (복사 아님)
# 주소값을 그대로 가져와서 쓴다
reference_copy = original 

# 얕은 복사
# 새로운 리스트를 생성 (1차원까지만)
shallow_copy = original[:]

# 깊은 복사
# 새로운 리스트를 생성 (내부까지 전부)
import copy
deep_copy = copy.deepcopy(original)

# 깊은 복사 vs 새로운 리스트
# 뭐가 더 빠를까?
# 새로 만드는 게 더 빠르다!
# 깊은 복사는 특정 시점의 전체 데이터가 필요하거나 하는 경우에 사용한다
# (시간 효율이 너무 떨어짐)
new_original = [1, 2, [3, 4, 5]]

print(id(original))
print(id(reference_copy)) # == original
print(id(shallow_copy)) # 다 다름
print(id(deep_copy)) # 다 다름

print(id(original[2]))
print(id(reference_copy[2])) # == original
print(id(shallow_copy[2])) # == original
print(id(deep_copy[2])) # 다 다름

# 주소값 개념: Java, C++ 배울 때 중요함. 학습하기 (임베디드, B형 등에 필요)


# isdecimal, isdigit, isnumeric
# 문자열 소수, 음수는 어떻게 구분할까?
number = '-30.5'
# 마이너스와 .을 빼고 판별한다
is_number = number.replace('-','').replace('.','') # 반환값이 있기 때문에 .으로 이어갈 수 있다.
if is_number.isdigit():
    print(float(number)) # -30.5


# replace 활용도 높음. 잘 활용하기


# OOP 기초
# - 오늘, 내일 내용으로 수목 라이브 들으면서 바로 이해할 수 있도록 선행 학습

## 프로그래밍 패러다임
# - 패러다임?
#   - 특정한 방식이나 철학에 따라 문제를 이해하고 해결하는 틀 또는 접근방식
#   - 과학적 패러다임 예시
#       - 지구중심설, 태양중심설 등
# - 프로그래밍 패러다임
#   - 소프트웨어를 설계하고 작성하는데 사용하는 특정한 스타일이나 접근 방식
#   - 종류
#     - 절차 지향 프로그래밍(Procedual Programming)
#       - 프로그램을 절차나 함수의 집합으로 구성하는 방식
#       - 순차적으로 실행되는 명령어 목록으로 문제를 해결
#       - 단점: 복잡한 프로그래밍 유지보수가 너무 어렵다.
#       - ex) C언어, 운영체제 등
#     - 객체 지향 프로그래밍(Object-Oriented Programming; OOP)
#       - 데이터와 해당 데이터를 처리하는 로직. 하나의 객체로 묶어서 프로그램을 설계
#       - ex) C++, java, python 등
#     - 함수형, 선언형 등
#
#   - 알아야 할 용어
#      - 클래스(class)
#      - 객체와 인스턴스 (Object and Instance)   
#      - 속성(Attribute) == 데이터
#      - 메서드(Method) == 함수

#%%
# class: 객체를 생성하기 위한 설계도 또는 청사진
class Person:
    # 매직 메서드: '__'로 감싸진 메서드
    # 파이썬이 사용하는 특별한 메서드들을 의미
    # 특정 상황에서 자동으로 호출
    # __init__ :인스턴스 생성 시 자동으로 호출되는 매직 메서드
    #           객체를 초기화 할 때 사용한다.
    # self: 만들어진 객체 자기 자신.
    def __init__(self):
        self.life = 1
    
    def __str__(self):
        return "Person 클래스임"

    
print(Person) # <class '__main__.Person'>

# student라는 객체(object)를 생성했다.
# student 는 Person 클래스의 인스턴스(Instance)라고 한다
# 오브젝트와 인스턴스나 비슷한 말인데, 부를 때 방식에 따라 차이만 있다.
student = Person()
print(student) # Person 클래스임

print(student.life) # 1
student.life = 0 # 접근하여 값 수정도 가능
print(student.life) # 0


# %%
class Person:
    def __init__(self, name, hobby):
        self.life = 1
        self.name = name
        self.hobby = hobby
    
    def __str__(self):
        return "Person 클래스임"
    
    # 메서드 정의
    def 자기소개(self):
        print(f'제 이름은 {self.name}입니다.')
        print(f'취미는 {self.hobby}입니다.')

    # self 빠트리면 객체에서 호출 못한다. 주의!
    def func():
        print('self 없는 func')

# 0 positional arguments, but 1 was given
# 아무것도 안받을건데, 하나 전달해줬다.
# - 이 때 하나 == 객체 자기자신이 전달됨
# student.func()

student = Person('서준호', '영화보기')
print(student.name) # 서준호
# 메서드 호출
student.자기소개()   # 제 이름은 서준호입니다.
                    # 취미는 영화보기입니다.
student2 = Person('김싸피', '공부하기')
# 객체 추가 생성 가능
student2.자기소개()  # 제 이름은 김싸피입니다.
                    # 취미는 공부하기입니다.

# 한 번에 여러 데이터를 사용하는데 의의가 있다.
# %%
