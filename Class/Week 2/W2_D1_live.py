# 단순 구조에 집중
# 비선형 구조는 알고리즘 시간에

# 메서드
# 결론적으로 함수(def로 정의되는 코드 묶음)이다.
# 객체의 상태를 조작하거나 동작을 수행
# 클래스(class) 라는 객체 안에서 사용
#   파이썬에서 '타입을 표현하는 방법'
#   ex. help함수를 통해 str을 호출해보면 class 였다는 것을 확인
#   내장함수로 불러도 되고 class로 불러도 됨(특수한 경우)

# 메서드는 어딘가(클래스)에 속해 있는 '함수'이며,
# 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재

# 메서드 호출방법
# 데이터 타입 객체.함수이름()
# 'hello'.capitalize()
print('hello'.capitalize()) # Hello
# 맨 앞 글자를 대문자로 바꿔주는 메서드

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]


# 시퀀스 데이터 구조
# 문자열
# 조회/탐색 및 검증 메서드
# .find(x) 인자로 받는 x의 첫 번째 위치를 반환, 없으면 -1 반환
# .index(x) find와 같은 기능이나 없으면 오류 발생
# .isupper(x) '모두' 대문자인지 여부
# .islower(x) '모두' 소문자인지 여부
# .isalpha(x) '모두' 알파벳인지 여부

#@@ is가 붙은 함수의 특징.
#@@ 사실 여부를 묻는다.
#@@ 반환값이 Ture / False
#@@ 함수를 만들 때 T/F를 반환할 경우 is~로 이름을 하면 알아보기 쉬움 (팁) 

#%%
# find
text = 'banana'
print(text.find('a')) # 1
# a라는 문자열이 나오는 첫 번째 위치
print(text.find('z')) # -1
# z라는 문자열이 나오는 첫 번째 위치

#%%
# index
print(text.find('a')) # 1
print(text.find('z')) # ValueError

#@@ 긴 에러의 경우 봐야할 부분:
#@@ 마지막 줄과 그 위의 마지막 문단을 보면 에러 내용을 파악 가능

#%%
# isupper
# islower
string1 = 'HELLO'
string2 = 'Hello'

print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.islower()) # False
print(string2.islower()) # False

#%%
# isalpha
string1 = 'Hello'
string2 = '123sjh2395hi'

print(string1.isalpha()) # True
print(string2.isalpha()) # False


# 문자열 조작 메서드
# 중요 활용 메서드는 교안에 빨간 글씨로 표현
# 나머지는 알고있으면 편한 것들

#@@ 원본을 조작하지는 않고 새 문자열을 반환함
#@@ 문자열은 불변 데이터 타입이기 때문

# .replace(old, new[,count])
# .strip([chars])
# .split(sep=None, maxsplit=-1)
# 'separator'.join(iterable)

#%%
# .replace(old, new[,count])
#@@ 대괄호: 선택 인자(써도 되고 안 써도 되는 인자)라는 표시
#@@ 프로그래밍에서의 문법적 표기
#@@ 파이썬에 대괄호를 그대로 넣으면 오류남
text = 'Hello, world!'
new_text = text.replace('world', 'Python')

print(new_text) # Hello, Python!
# 원본 문자열이 바뀌지는 않음을 주의

text = 'Hello, world! world world'
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python! Python Python

text = 'Hello, world! world world'
new_text = text.replace('world', 'Python', 1)
print(new_text) # Hello, Python! world world
# 뒤에 1을 붙여 첫 번째 world만 변환된다!

#%%
# .strip([chars]) 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
text = '  Hello, world!  '
new_text = text.strip()
print(new_text) # Hello, world!

#%%
# .split(sep=None, maxsplit=-1)
# 지정한 문자를 구분자로 문자열을 분리하여 문자열의 '리스트'로 반환
#@@ input().split() 으로 문제에서 주로 활용
text = 'Hello, world!'
words = text.split(',')
words2 = text.split() # 아무것도 안 넣으면 공백을 기준으로 나눔
print(words) # ['Hello', ' world!']
print(words2) # ['Hello,', 'world!']

#%%
# 'separator'.join(iterable)
# iterable의 문자열을 연결한 문자열을 반환
#@@ split의 반대 동작
words = ['Hello', 'world!']
text = '-'.join(words)
print(text) # Hello-world!

#%%
# capitalize
# title
# upper
# lower
# swapcase
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
# 첫 글자만 대문자로 만들고 나머지를 소문자로 만든다
new_text2 = text.title()
# 문자열 간 공백을 기준으로 맨 앞 글자를 대문자로 만든다
new_text3 = text.upper() # 모두 대문자
new_text4 = text.lower() # 모두 소문자
new_text5 = text.swapcase() # 기존의 대소문자를 서로 교체하는 메서드

print(new_text1) # Hello, world!
print(new_text2) # Hello, World!
print(new_text3) # HELLO, WORLD!
print(new_text4) # hello, world!
print(new_text5) # HEllO, WOrLD!


# 메서드는 이어서 활용 가능하다.
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')
print(new_text) # HEzzO, WOrLD!
#@@ 100%는 아님.
#@@ 앞쪽에서 반환된 결과가 있어야하고 타입도 맞아야함.
#@@ T/F.replace() -> 앞쪽이 bolean 이므로 불가능.


#%%
# 리스트 값 추가 및 삭제 메서드
# .append(x)
# .extend(iterable)
# .insert(i,x)
# .remove(x)
# .pop()
# .pop(i)
# .clear()

#%%
# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]
print(my_list.append(4)) # None
#@@ .append(4) 의 반환이 없다.
#@@ 원본을 바꾸기 때문에 반환이 없으므로 None이 출력됨

#%%
# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]

#@@ extend 주의사항.
my_list.extend(5)
# iterable(반복가능한)이 아닌 것을 넣으면 에러 출력
my_list.append([9, 9, 9])
print(my_list) # [1, 2, 3, 4, 5, 6, [9, 9, 9]]
my_list.extend([5])
print(my_list) # [1, 2, 3, 4, 5, 6, [9, 9, 9], 5]

#@@ extend, append 모두 하나의 인자만 받을 수 있으므로 주의

#%%
# insert(i,x) 지정 인덱스i 위치에 항목x 삽입
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) # [1, 5, 2, 3]

#%%
# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list) # [1, 3, 2, 2, 2]

#%%
# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
# 제일 끝 제거 후 반환
print(item2) # 1
# 0번째 인덱스 제거 후 반환
print(my_list) # [2, 3, 4]

#%%
# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []


#%%
#리스트 탐색 및 정렬 메서드


#%%
# index(x) 리스트에서 첫 번째로 일치하는 항목 x의 인덱스 반환
my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1

#%%
# count(x) 리스트에서 항목 x의 개수를 반환
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count) # 3

#%%
# reverse() 리스트의 순서를 역순으로 변경(정렬x)
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list) # [9, 1, 8, 2, 3, 1]
print(my_list.reverse()) # None
#@@ 원본을 뒤집어서 반환이 없으므로 None 출력
#@@ return개념 헷갈리면 함수 파트 다시 정리하기

#%%
# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list) # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list) # [100, 3, 2, 1]


#%%
# 다양한 리스트 메서드
# https://docs.python.org/ko/3/tutorial/datastructures.html
# 예제 코드도 함께 확인하면 이해가 쉽다.

#%%
# 참고
# 데이터 타입과 복사
# 파이썬에서는 데이터의 분류에 따라 복사가 달라짐
# 가변 데이터 타입과 불변 데이터 타입을 다르게 다뤄야한다.

# 할당
# 할당은 복사가 아니다!

# 가변 데이터의 경우
a = [1, 2, 3, 4]
# a에는 '리스트의 주소'가 들어갔다
b = a
# -> b는 a로부터 방 주소를 받았다.
b[0] = 100

print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]
# => 복사가 일어나지 않았다.
# -> b는 a와 같은 방을 바라보고 있다!
# -> 따라서 b를 변경시켰지만 a도 같은 값을 출력

# 불변 데이터의 경우
a = 20
# a는 20을 바라본다
b = a
# b도 20을 바라본다
b = 10
# b는 10이라는 값을 '재할당' 받았다

print(a) # 20
print(b) # 10

# 할당 연산자(=)를 통한 복사는 '객체의 참조'를 복사

#%%
# 얕은 복사
a = [1, 2, 3]
b = a[:]
c = a.copy() #@@ .copy는 [:]와 같은 기능

b[0] = 100
c[0] = 999
print(a) # [1, 2, 3]
print(b) # [100, 2, 3]
print(c) # [999, 2, 3]

# 리스트를 복사하여 b, c에 할당
# -> 모습만 같고 다른 주소를 바라보고있다

# 얕은 복사의 한계
# 1단계까지만 가능하다
a = [1, 2, [3, 4, 5]] 
#     1단계   2단계(중첩 리스트)
b = a[:]

b[0] = 999
b[2][1] = 100
print(a) # [1, 2, [3, 100, 5]]
print(b) # [999, 2, [3, 100, 5]]
# 안쪽 중첩 리스트는 다시 같은 방을 바라본다

# 깊은 복사
# 내장 모듈의 힘을 빌린다! (유일한 방법)
# 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
import copy

a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a) # [1, 2, [3, 4, 5]]
print(b) # [1, 2, [3, 100, 5]]

#%%
# 문자 유형 판별 메서드
# 문자열에 포함된 문자들의 유형을 판별하는 메서드

# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())    # T
print("'123.45'.isdecimal():", '123.45'.isdecimal())  # F
print("'-123'.isdecimal():", '-123'.isdecimal())      # F
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())          # F
print("'½'.isdecimal():", '½'.isdecimal())            # F
print("'²'.isdecimal():", '²'.isdecimal())            # F
print()

# isdigit() : 일반 숫자뿐만 아니라 유니코드 숫자(①), 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())      # T
print("'123.45'.isdigit():", '123.45'.isdigit())    # F
print("'-123'.isdigit():", '-123'.isdigit())        # F
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())            # F
print("'½'.isdigit():", '½'.isdigit())              # F
print("'²'.isdigit():", '²'.isdigit())              # T
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())      # T
print("'123.45'.isnumeric():", '123.45'.isnumeric())    # F
print("'-123'.isnumeric():", '-123'.isnumeric())        # F
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())            # T
print("'½'.isnumeric():", '½'.isnumeric())              # T
print("'²'.isnumeric():", '²'.isnumeric())              # T
