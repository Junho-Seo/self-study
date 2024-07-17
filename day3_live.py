#%%
# fucntion
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

result = make_sum(100, 30)
return_value = print(result) #130 (반환값)
print(return_value) # None
# print 함수는 return(반환)이 없다!
# return과 출력은 다른 개념

def my_func():
    print('hello world') #hello world

result = my_func()
print(result) #None


# %%
#매개변수와 인자
# 1. Positional Arguments 위치 인자
# 그 값이 누락될 수 없다. (둘 중 하나를 안 쓰거나 하는 등)
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25)
# 안녕하세요, Alice님! 25살이시군요.
greet('Alice')
# TypeError: greet() missing 1 required positional argument: 'age'
greet(25, 'Alice')
# 안녕하세요, 25님! Alice살이시군요.

#%%
# 2. Default Argument Values 기본 인자 값
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')
# 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)
# 안녕하세요, Charlie님! 40살이시군요.

#%%
# 3. Keyword Arguments 키워드 인자
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)
# 안녕하세요, Dave님! 35살이시군요.
#greet(age=35, 'Dave')
# SyntaxError: positional argument follows keyword argument
# - 애초에 빨간줄로 오류 표시 해줌
# - 쓰려면 아래와 같이 둘 다 키워드 인자로 사용해야함
greet(age=35, name='Dave')
# 안녕하세요, Dave님! 35살이시군요.

#%%
# 4. Arbitrary Argument Lists 임의의 인자 목록
# 앞선 인자들의 단점: 인자의 개수가 제한적이다
def calculate_sum(*args):
    print(args)
    print(type(args))
    # 여러 개의 인자를 tuple로 처리함을 볼 수있음
    # 관습적으로 임의의 인자는 args 라고 지정
    total = sum(args)
    print(f'합계: {total}')

calculate_sum(1, 300, 4000, 1000)

#%%
# 5. Arbitrary Keyword Argument Lists 임의의 키워드 인자 목록
# key-value 형태로 들어오기 때문에 dict로 처리
def print_info(**kwargs):
    print(kwargs)
    # kwargs 또한 관습적 이름이다

print_info(name='Eve', age=30)


#%%
# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')


#%%
#재귀 함수
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)


# 팩토리얼 계산 예시
print(factorial(5))  # 120


#%%
# Built-in function 내장 함수
# ex) print()
# 내장 함수가 아닌 함수는 그냥 "함수" 라고 표현
# 일부 번역 서적에서 외장 함수라는 표현을 사용하나 잘못된 표현
# 슬라이싱 [::-1]는 그냥 뒤집기 / sorted + reverse는 내림차순 "정렬"
numbers = [1, 2, 3, 4, 5]

print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]

#%%
# 유용한 내장 함수 map & zip
# map(function, iterable)
# iterable : 반복 가능한 객체(요소) ex. collection
# map
numbers = [1, 2, 3]
result = map(str, numbers)
print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']

numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]

#%%
# zip (*iterables) 임의의 iterable을 모아 튜플로
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]

kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)


scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]
for score in zip(*scores):
    print(score)

#%%
#함수와 scope
#이름 검색 규칙 Name Resolution (=LEGB Rule)
# 파이썬이 함수를 찾아가는 순서.
# Local scpoe > Enclosed scpoe > Global scope > Built-in scope
a = 1
b = 2

def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  # 10 2 500

    local(500)
    print(a, b, c)  # 10 2 3

enclosed()
print(a, b)  # 1 2

#%%
num = 0  # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언
    num += 1

print(num)  # 0
increment()
print(num)  # 1

#주의. global 키워드 선전 전에 참조 불가, 매개변수에는 사용 불가.


#%%
#패킹
#예시.변수에 담긴 값들은 튜플 형태로 묶임
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)

# 애스터리스크는 남은 요소들을 리스트로 패킹하여 할당
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


def my_func(*objects):
    print(objects)  # (1, 2, 3, 4, 5)
    print(type(objects))  # <class 'tuple'>


my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>

#%%
#언패킹
packed_values = 1, 2, 3, 4, 5

a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5


def my_function(x, y, z):
    print(x, y, z)

# "인자"에 *를 넣으면 묶는것이 아닌 푸는것!
names = ['alice', 'jane', 'peter']
my_function(*names)  # alice jane peter


def my_function(x, y, z):
    print(x, y, z)

# **는 딕셔너리의 key-value쌍을 언패킹하여 함수의 키워드 인자로 전달
my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3

#%%
#람다 표현식
def addition(x, y):
    return x + y


result = addition(3, 5)
print(result)  # 8


# lambda 표현식으로 작성한 addition 함수
addition = lambda x, y: x + y

result = addition(3, 5)
print(result) # 8

# with map 함수
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2


# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2) # [1, 4, 9, 16, 25]





