#%%

#금일 배운 내용
# (1) 함수 (파라미터, 인자, 람다, 재귀함수)
# (2) zip, map

#%%
# 재귀함수
# (1) 리스트의 요소를 모두 더하는 함수
def sum_list(nums) :
    if not nums:
        return 0
    return nums[0] + sum_list(nums[1:])

#%%
def sum_list(nums, idx) :
    if idx >= len(nums) :
        return 0
    return nums[idx] + sum_list(nums, idx+1)
nums = [1,2,3]
sum_list(nums, 0) #6
sum_list(nums, 1) #5

#1 + sum_list([1,2,3], 1)
#1 + (2 + sum_list([1,2,3], 2))
#1 + (2 + (3 + sum_list([1,2,3], 3)))
#1 + (2 + (3 + (0)))

#%%
#문자열을 거꾸로 출력하는 재귀함수
#"hello" -> "olleh"
def reverse_string(s, idx) :
    if idx >= len(s) :
        return ""
    return reverse_string(s, idx+1) + s[idx]

reverse_string("hello", 0) #'olleh'

#%%
#람다식 : 함수를 간소화해서 표현

radius = [10,1,2,4,1.5] #반지름 리스트
sorted(radius) #[1, 1.5, 2, 4, 10]
sorted(radius, reverse=True) #[10, 4, 2, 1.5, 1]
sorted(radius, key=lambda r : r**2*3.14159) #[1, 1.5, 2, 4, 10]

rects = [(1,5), (3,3), (10,4), (2,2)] #[(가로, 세로), ]
#가로 길이 기준 정렬
sorted(rects) #[(1, 2), (2, 2), (3, 3), (10, 4)]

sorted(rects, key=lambda x:x[1]) #[(2, 2), (3, 3), (10, 4), (1, 5)]

def sort_by_width(rect) :
    return rect[1]
sorted(rects, key=sort_by_width) #[(2, 2), (3, 3), (10, 4), (1, 5)]

#%%
rects = [(1,5), (3,3), (10,4), (2,2)]
#map : 리스트를 통해 새로운 리스트 만듬
#사각형의 넓이 리스트
print(map(lambda rect : rect[0]*rect[1], rects)) #<map object at 0x00000161FDBAEF40>
#map은 실행 조건식만 가지고 있고,
#map함수가 실제로 실행되는 경우 형변환 list, tuple, 반복문 등에 쓰일때
print(list(map(lambda rect : rect[0]*rect[1], rects))) #[5, 9, 40, 4]


#사각형의 둘레값을 갖는 새로운 리스트
rects = [(1,5), (3,3), (10,4), (2,2)]
print(map(lambda rect : 2*(rect[0]+rect[1]), rects)) #지연 평가
print(list(map(lambda rect : 2*(rect[0]+rect[1]), rects))) #실제로 평가
print(tuple(map(lambda rect : 2*(rect[0]+rect[1]), rects))) #실제로 평가
print(set(map(lambda rect : 2*(rect[0]+rect[1]), rects))) #실제로 평가

#%%
names = ['홍길동', '김현수', '이기찬']
ages = [20,30,35]

#사람정보를 갖는 딕셔너리
list(map(lambda name, age:{'name':name, 'age':age}, names, ages))
# [{'name': '홍길동', 'age': 20},
#  {'name': '김현수', 'age': 30},
#  {'name': '이기찬', 'age': 35}]

no = 0
def create_user(name, age) :
    global no
    no += 1
    print(f'{name} 안녕하세요~!')
    return {'no':no, 'name':name, 'age':age}
list(map(create_user, names, ages))

# 홍길동 안녕하세요~!
# 김현수 안녕하세요~!
# 이기찬 안녕하세요~!
# [{'no': 1, 'name': '홍길동', 'age': 20},
#  {'no': 2, 'name': '김현수', 'age': 30},
#  {'no': 3, 'name': '이기찬', 'age': 35}]
# %%
# 대규모 도서 대여 서비스 LV5
number_of_book = 100 #대여가능한 책의 수

def decrease_book(num) :
    global number_of_book
    number_of_book -= num
    print('남은 책의 수 :', number_of_book)
    
number_of_people = 0 #회원 수
def increase_user() :
    global number_of_people
    number_of_people += 1


names = ['김시습', '허균', '남영로']
ages = [20, 16, 52]
address = ['서울', '강릉', '조선']

def create_user(name, age, addr) :
    increase_user()
    print(f'{name}님 환영합니다!')
    return {'name':name, 'age':age, 'address':addr}
    
many_user = list(map(create_user, names, ages, address))
print(many_user) 
#[{'name': '김시습', 'age': 20, 'address': '서울'}, 
# {'name': '허균', 'age': 16, 'address': '강릉'}, 
# {'name': '남영로', 'age': 52, 'address': '조선'}]


#LV5 추가 내용
def rental_book(info) :
    decrease_book(info['age']//10) #문제 요구 조건
    print(f"{info['name']}님이 {info['age']//10}권의 책을 대여하였습니다.")

#[{'name': '김시습', 'age': 20, 'address': '서울'}, 
# {'name': '허균', 'age': 16, 'address': '강릉'}, 
# {'name': '남영로', 'age': 52, 'address': '조선'}]
info = list(map(lambda user : {'name':user['name'], 'age':user['age']}, many_user))
print(info)  
#[{'name': '김시습', 'age': 20}, 
# {'name': '허균', 'age': 16},
# {'name': '남영로', 'age': 52}]

list(map(rental_book, info))
# 남은 책의 수 : 98
# 김시습님이 2권의 책을 대여하였습니다.
# 남은 책의 수 : 97
# 허균님이 1권의 책을 대여하였습니다.
# 남은 책의 수 : 92
# 남영로님이 5권의 책을 대여하였습니다.


list(map(rental_book, map(lambda user : {'name':user['name'], 'age':user['age']}, many_user)))
# 남은 책의 수 : 98
# 김시습님이 2권의 책을 대여하였습니다.
# 남은 책의 수 : 97
# 허균님이 1권의 책을 대여하였습니다.
# 남은 책의 수 : 92
# 남영로님이 5권의 책을 대여하였습니다.