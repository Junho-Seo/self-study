## 삼항 연산자
#%%
# if, else로 이루어진 간단한 조건문을 한 줄로 작성할 수 있게 해주는 구문
# a, b 중 큰 수를 출력하라
a = 10
b = 20
if a > b:
    print(a)
else:
    print(b)

# 위와 같은 코드
print(a) if a > b else print (b)

# 사용법
# <조건이 True 일 때 로직> if <조건문> else <조건이 False일 때 로직>

# age라는 key가 있으면 age값을 출력, 없으면 Unknown 출력
di = {
    'name': 'test'
    # 'age': 50
}

print(di['age']) if di.get('age') else print('Unknown')

# 왜 쓰나요?
# - 코드의 간결성, 가독성을 위해 제공되는 문법
#   - 조건과 표현식이 간단할 때만 사용해야한다!
# - 성능은 'if-else' 문과 동일함

#%%
## 클래스 복습 + 상속
# 클래스를 왜 이해해야 하는가?
# 반드시 지금 이해하고 넘어가는게 좋음.
# 알고리즘 주차 끝나고 장고에서 활용 예정이기 때문.

# Person이라는 class를 생성
# life, name, hobby 속성값들이 있다.
class Person:
    # 생성자 매직 메서드
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

    def func():
        print('self 없는 func')

student = Person('서준호', '영화보기')
print(student.name) # 서준호
# 메서드 호출
student.자기소개()   # 제 이름은 서준호입니다.
                    # 취미는 영화보기입니다.
student2 = Person('김싸피', '공부하기')
# 객체 추가 생성 가능
student2.자기소개()  # 제 이름은 김싸피입니다.
                    # 취미는 공부하기입니다.

# class를 따로따로 다 만들면 중복된 코드가 너무 많다(비효율적이다.)
# - 중복된 코드의 문제점
#       유지보수가 많이 힘들다.
#       수정 및 관리 시에 코드를 100% 파악해야 가능.
# - 그럼 중복을 어떻게 피할까?
#       -> 만들어진 코드를 활용하는 기법들이 필요하다.
#       -> OOP 측에서는 "상속"을 통해서 중복을 피한다.

# 상속
# 부모의 재산을 물려받는다.
# == 부모 클래스의 속성과 메서드를 물려받는다.

# 사람이긴한데, 학생(성적 데이터 추가)
# Person class 로 부터 상속받는다.
class Student(Person):
    # 성적 데이터는 person에는 없지만 Student에만 있어야함
    # 즉, 부모 클래스에는 없는 데이터가 추가됨
    def __init__(self, name, hobby, grade):
        # 1. 각각 다 적어주는 방법: 중복이 많이 발생
        # self.name = name
        # self.hobby = name
        # self.grade = name

        #2. 부모가 가진 __init__ 메서드를 가져와서 쓰면 중복이 많이 없어짐
        # super(): 부모 클래스(Person)
        super().__init__(name, hobby)
        self.grade = grade

    # 부모 클래스로부터 받아온 메서드에 추가 로직을 구현하는 방법
    def new_자기소개(self):
        # 자기소개() 메서드는 이미 받아왔으니, self로 접근가능
        self.자기소개()
        print(f'성적은 {self.grade}입니다.')

stu = Student('김싸피', '공부하기', 'A+')
stu.new_자기소개()

# 사람이긴한데, 강사(과목 데이터 추가)
class Teacher(Person):
    def __init__(self, name, hobby, subject):
        super().__init__(name, subject)
        self.subject = subject

    # 부모 클래스가 가진 메서드와 이름을 똑같게 한다면?
    # 메서드 이름이 동일하면, 덮어쓰기된다.
    # 메서드 오버라이딩(overriding) 이라고 한다.
    def 자기소개(self):
        super().자기소개()
        print(f'맡은 과목: {self.subject}')

tea = Teacher('KKR', '게임하기','Python')
tea.자기소개()

#%%