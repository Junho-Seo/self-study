## 클래스 복습
# 객체 지향 방식
#   (데이터 + 데이터를 다루는 로직) 한 세트로묶어서 개발하자!

# 용어

# 1. 객체를 만들기 위한 설계도: class(클래스)
# 2. 데이터
#   - 인스턴스 변수: 인스턴스가 독립적으로 가진 변수
#       - 다른 인스턴스와 값을 공유하지 않음
#   - 클래스 변수: 인스턴스끼리 공유하는 변수

# 3. 데이터를 다루는 로직(메서드)
#   - 인스턴스 메서드: 인스턴스가 독립적으로 가진 메서드
#       - 첫 파라미터: self(인스턴스 자기 자신)
#   - 클래스 메서드: 인스턴스끼리 공유하는 메서드
#       - 첫 파라미터: cls(클래스)
#   - 스태틱 메서드: 인스턴스나 클래스의 데이터와 무관한 메서드를 정의할 때 사용 (중요도 조금 낮음)
#       - 코드를 클래스 밖으로 빼도 문제가 없다.
#       - 뭔가 관련된 로직인데... 밖에 두기가 싫어.. class 안에 쓸래

#%%
## 클래스 연습
# 동물, 강아지, 고양이 -> 내 펫으로 관리 하려고 한다.
# - 강아지, 고양이가 동물 클래스를 상속
# - 펫이 강아지 고양이 클래스를 다중 상속
# import sys
# sys.stdin =
# sys.stdout = open('output.txt', 'w', )
class Animal:
    # 문제1. 전체 동물의 수를 관리할 수 있도록 total_animal 변수를 구성
    #       전체 동물의수를출력하는 get_total_animals 메서드를 구현

    # 인스턴스 각각과 관계없이, 전체적으로 관리되어야한다 -> 클래스 변수
    total_num = 0
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        # Animal.total_num += 1
        # 44,45 line 대신 여기에 이렇게 넣어도 똑같이 작동함.

        print(f'Animal - {name} 추가')
    
    def total_animal(self):
        Animal.total_num += 1
    
    # 클래스 변수를 써야함 + 인스턴스의 값이 필요가 없다 -> 클래스 메서드로 정의
    # 그냥 def로 적으면 아래 메서드가 클래스인지, 스태틱인지, 인스턴스인지 알 수가 없다.
    # 따라서, 아래와 같이 classmethod 데코레이터를 활용한다.
    @classmethod
    def get_total_animals(cls):
        print(f'현재 동물의 수는 {cls.total_num}입니다.')

    # 문제 2. 동물의 울음소리를 출력하는 make_sound 메서드를 정의하세요.
    # 각각의 인스턴스가 다른 결과물 -> 인스턴스 메서드
    def make_sound(self):
        print(f'{self.name} - {self.sound}')

    # 문제 3. 동물에 대해 소개하는 introduce 메서드를 정의하세요.
    # 인스턴스와 관계 X, 클래스의 변수와도 관계 X -> 스태틱 메서드
    @staticmethod
    def introduce():
        print("동물은 낭만이 있다.")


animal1 = Animal("호랑이", 5, "어흥")
animal2 = Animal("코끼리", 10, "뿌우")

animal1.total_animal()
animal2.total_animal()
Animal.get_total_animals()
# 인스턴스에서 클래스 메서드 호출 -> 권장 x
# animal1.get_total_animals() # 출력은 됨.

animal1.make_sound()
animal2.make_sound()

Animal.introduce()

#%% 데코레이터
## 데코레이터
# 함수 호출 전/후에
# 다른 함수에서도 많이 사용되는 동작을 추가하고 싶을 때 사용
# -> 모든 함수에 동일한 코드를 넣으면 관리가 안 된다!
# -> 그래서 만들어 놓은 게 데코레이터

# 잘못된 예시
# def say_hello():
#     # 호출 전 예시) 로그인 여부를 체크해야한다.
#     print('안녕하세요.')
#     # 호출 후 예시) '다음에 또 이용해주세요.' 출력해줘야 한다.

# def 다른함수():
#     # 호출 전 예시) 로그인 여부를 체크해야한다.
#     print('다른 함수 로직')
#     # 호출 후 예시) '다음에 또 이용해주세요.' 출력해줘야 한다.

# 데코레이터 특징(구조)
# 1. 다른 함수를 인자로 전달받는다.
def my_decorator(func):
    # 2. 데코레이터 내부에 전달받은 함수를 감싸는 새로운 함수를 정의
    def wrapper():
        # 전달받은 함수 호출 전/후에 하고싶은 로직을 추가
        print("함수 호출 전에 하고싶은 동작")
        func()
        print("함수 호출 후에 하고싶은 동작")
    
    # 3. 정의한 함수를 반환
    return wrapper

@my_decorator
def say_hello():
    print('안녕하세요.')

say_hello() # 함수 호출 전에 하고싶은 동작
            # 안녕하세요.
            # 함수 호출 후에 하고싶은 동작
# %%
# 문제4. Animal 클래스를 상속받는 Dog class를 작성하세요.
class Dog(Animal):
    # 문제5. name, age, sound, species 속성을 가지도록 생성자를 구성하세요.
    def __init__(self, name, age, sound, species):
        super().__init__(name, age, sound)
        # Animal.__init__(self, name, age, sound)
        # 다중 상속에서 클래스를 직접 지정하는 경우 위처럼 쓸 수 있다.
        # self 꼭 들어가야 함에 주의.
        self.species = species

        print(f'Dog - {name} 추가')

    # 문제6. 강아지의 울음소리를 출력하는 make_sound 메서드를 구성하세요
    #  - 부모 클래스 Animal이 가진 make_sound 를 "재정의" 해주었다.
    #  -> 오버라이딩(overriding)
    def make_sound(self): # 인스턴스로 받아야하니 self가 들어간다.
        print(f'{self.name}({self.species}) - {self.sound}')

dog1 = Dog('레오', 3, '왈루왈루', '골든 리트리버')
# Animal - 레오 추가
# Dog - 레오 추가
dog2 = Dog('리키', 5, '그르르', '치와와')
# Animal - 리키 추가
# Dog - 리키 추가
dog1.make_sound()
dog2.make_sound()
# 상속을 하는 경우 상위 클래스 생성자도 같이 출력됨
print('----------------------------------------')
# 문제7. 고양이 class도 만들어보시오.
class  Cat(Animal):
    def __init__(self, name, age, sound, species):
        super().__init__(name, age, sound)
        self.species = species

        print(f'Cat - {name} 추가')
    
    def make_sound(self):
        print(f'{self.name}({self.species}) - {self.sound}')

cat1 = Cat('디디', 8, '야옹','페르시안')
cat2 = Cat('모모 회장님', 7, '흠흠', '가짜 고양이')

cat1.make_sound()
cat2.make_sound()

print('----------------------------------------')

# 새로운 방법 (오류 수정 필요함. super의 탐색범위. 240725 mm확인하기)
class Pet(Dog, Cat):
    # 속성에 입양 기간 period 추가
    # 인스턴스를 animal이라는 변수로 전달
    def __init__(self, animal, period):
        # isinstance: 인스턴스가 어떤 클래스의 인스턴스인지 확인하고 싶을 때 사용
        # animal이 강아지 클래스의 인스턴스라면?
        #   - Dog의 생성자 호출
        if isinstance(animal, Dog):
            print('강아지 생성자')
            # 우리 머리에서는 Dog -> Animal 이렇게 따라갈 거 같은데
            # 실제로 super()는 무조건 Dog만 바라봄
            super(Dog, self).__init__(animal.name, animal.age, animal.sound, animal.species) # Dog 에서 가져온다고 지정한 것.
            self.period = period

        # animal이 고양이 클래스의 인스턴스라면?
        #   - Cat의 생성자 호출
        elif isinstance(animal, Cat):
            print('고양이 생성자')
            # super(Cat, self).__init__(animal.name, animal.age, animal.sound, animal.species) # Cat 에서 가져온다고 지정한 것.
            Cat.__init__(self, animal.name, animal.age, animal.sound, animal.species) # 위와 같은 코드. self 넣음에 주의.
            self.period = period

    def play(self):
        print(f'{self.name}({self.species}) 와 놀아줌!')

pet1 = Pet(dog1, 1) # 강아지 생성자
pet2 = Pet(cat1, 2) # 고양이 생성자

pet1.play()
pet1.make_sound()

pet2.play()
pet2.make_sound()

# OOP 디자인 패턴 공부해보기 (심화)
#   다른 개발자들의 좋은 설계 방법들
#   시스템마다 패턴 적용 방법이 다르기 때문에 어느 분야던 평생 공부하게 될 것
#   기술 면접 질문으로 한 번쯤 나올 수 있음. ex. 디자인 패턴 뭐뭐 알고있어요? -> 꼬리질문 뭐 구현해봤냐 설명해봐라
#   얕고 넓게 공부하기
# %%
