##지난시간 복습
# 데이터 구조
# 여러 데이터를 효과적으로 사용, 관리하기 위한 구조

# 메서드
# 객체(class)에 속한 함수. 객체의 상태를 조작하거나 동작을 수행
# 호출 방법: 데이터 타입 객체.메서드()


##비시퀀스 데이터 구조
# 딕셔너리
# 고유한 항목(중복되지 않는 항목)들의 정렬되지 않은(순서가 없는) 컬렉션

#%%
# .clear() 딕셔너리의 모든 키/값 쌍을 제거
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) #{}

#%%
# .get(key[,default])
# 키에 해당하는 값을 반환. 키가 없으면 None 혹은 기본 값을 반환
#@@ 대괄호: 선택 인자(기본값이 존재한다)
#@@ dict[key]와 차이점: keyerror 대신 반환값을 준다.
person = {'name': 'Alice', 'age': 25}

print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country', 'Unknown')) # Unknown
#print(person['country']) # KeyError

#@@ 28줄과 30줄은 필요에 따라 사용. (반환값이 필요한가?)

#%%
# keys() 딕셔너리 키를 모은 객체를 반환
person = {'name': 'Alice', 'age': 25}
print(person.keys()) # dict_keys(['name', 'age'])
# 리스트 형태네? 시퀀스 같은데 반복이 가능하겠네?
for item in person.keys():
    print(item) # name
                # age
# 그대로 반복으로 사용 가능!
# 형변환이나 다른 방법으로 복잡하게 안 해도 됨 (파이썬)

#%%
# values() 딕셔너리 값을 모은 객체를 반환
person = {'name': 'Alice', 'age': 25}
print(person.values()) # dict_values(['Alice', 25])
for item in person.values():
    print(item) # Alice
                # 25


#%%
# items() 딕셔너리 키/값 쌍을 모은 객체를 반환
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
#@@ 튜플 형식이다
for key, value in person.items():
#@@ 언패킹을 활용한다. (item -> key, value)
    print(key) # name Alice
    print(value) # age 25


#%%
# pop(key[,default]) 키를 제거하고 연결됐던 값을 '반환'
# 없으면 에러나 default를 반환
person = {'name': 'Alice', 'age': 25}

print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country', None)) # None
print(person.pop('country')) # KeyError

#%%
# setdefault(key[,default])
# 키와 연결된 값을 반환 (get과 동일)
# 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
#@@ 잘 활용하면 간단한 조건문을 생략할 수 있다!
#@@ 있으면 반환, 없으면 추가 (elif)
person = {'name': 'Alice', 'age': 25}

print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

#%%
# update([other]) other가 제공하는 키/값 쌍으로 딕셔너리를 '갱신'
# 기존 키가 존재하는 경우 덮어쓴다.
# other: 여러개의 선택 인자를 넣을 수 있다는 뜻
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

# 키워드 인자로도 가능
person.update(age=50, country='KOREA')
print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}

# 다양한 딕셔너리 메서드
# https://docs.python.org/ko/3/library/index.html

#%%
# set
# 딕셔너리랑 마찬가지로 중복x 순서x
#@@ a = {} 빈 딕셔너리
#@@ a = set() 빈 set

#%%
# .add(x) 세트에 x를 추가
my_set = {'a', 'b', 'c', 1, 2, 3}

# 임의의 위치에 삽입, set는 순서가 없다는 것에 주의
my_set.add(4)
print(my_set) # {1, 2, 3, 'b', 4, 'a', 'c'}

my_set.add(4)
print(my_set) # {1, 2, 3, 'b', 4, 'a', 'c'}

#%%
# clear() 세트의 모든 항목을 제거
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.clear()
print(my_set) # set()

#%%
# remove(x) 세트에서 항목 x를 제거
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.remove(2)
print(my_set) # {1, 3, 'b', 'a', 'c'}

my_set.remove(10)
print(my_set) # KeyError

#%%
# pop() 세트에서 '임의의' 요소를 제거하고 '반환'
my_set = {'a', 'b', 'c', 1, 2, 3}

element = my_set.pop()

print(element) # 1
print(my_set) # {2, 3, 'b', 'a', 'c'}

# 주피터에서 실행하면 무조건 1만 빠진다 ?
# 파이썬에서의 '임의'의 의미는 후반부에 정리

#%%
# discard(x) 세트에서 항목 x를 제거.
# remove와 달리 에러 없음
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.discard(2)
print(my_set) # {1, 3, 'b', 'a', 'c'}

my_set.discard(10)
print(my_set.discard(10)) # None

#%%
# update(iterable) 세트에 다른 iterable 요소 추가
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.update([1, 4, 5])
print(my_set) # {1, 2, 3, 'b', 4, 5, 'a', 'c'}

#%%
# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
# set1 - set2
print(set1.intersection(set2)) # {1, 3}
# set1 & set2
print(set1.issubset(set2)) # False
# set1 <= set2
print(set3.issubset(set1)) # True
# set3 <= set1
print(set1.issuperset(set2)) # False
# set1 >= set2
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
# set1 | set2

#%% practice1
# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    pass


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    pass


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}

#%%practice2
# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기


# 1. [] 표기법을 사용한 방법
def dict_invert(input_dict):
    pass


# 2. get 메서드를 사용한 방법
def dict_invert(input_dict):
    pass


# 3. setdefault 메서드를 사용한 방법
def dict_invert(input_dict):
    pass


print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
print(
    dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
)  # {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}


#%%
## 참고 (교안에 메모함)(시험에 나오지 않음)
# 해시 테이블
#  해시 함수를 사용하여 변환한 값을
#  색인(index)으로 삼아 키(key)와 데이터(value)를 저장하는 자료구조
#  -> 데이터를 효율적으로 저장하고 검색하기 위해 사용

#  해시테이블 원리
#  hash function은 파이썬이 재실행 될 때마다 바뀐다.
#  hash table은 바뀌지 않음(bucket)
#  해시함수
#  인풋  >      >   아웃풋
#  정수  >그대로> 정수
#  문자열 >임의> 정수

#%%
# 정수
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)


# 문자열
my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())

print(hash(1))
print(hash(1))
print(hash('a'))
print(hash('a'))

print(hash(1))
print(hash(1.0))
print(hash('1'))
print(hash((1, 2, 3)))

# TypeError: unhashable type: 'list'
# print(hash((1, 2, [3, 4])))
# TypeError: unhashable type: 'list'
# print(hash([1, 2, 3]))
# TypeError: unhashable type: 'list'
# my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
# TypeError: unhashable type: 'set'
# my_dict = {{3, 2}: 'a'}


# %%
# 파이썬 문법 규격
# BNF: 프로그래밍 언어의 문법을 표현하기 위한 '문서상의' 표기법
# EBNF: BNF를 확장한 표기법
# []: 선택적 요소
# {}: 0번 이상 반복
# (): 그룹화
# BNF와 같은 표기법을 사용하는 이유
# 서로 다른 프로그래밍 언어, 데이터 형식, 프로토콜등의 문법을 통일하여 정의하기 위함