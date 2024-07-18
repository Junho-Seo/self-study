#%%
#__pycache__ 폴더
# 모듈을 가져올 때 캐시 기능을 활용하여
# 빠르게 가져오기 위해 파이썬이 만들어주는 폴더
# 우리 코드로 치면
# test 모듈에 대한 정보가 캐시에 저장
# day4_live.py를 다시 실행할 때 빠르게 가져옴
# 지우거나 무시해도 정상 작동 됨. 따라서 *.pyc -> .gitignore에 포함시키자!!


#모듈: 파이썬 파일 하나
# import: 통째로 포함시킨다.
# as(alias의 약어): 별명(이름) 지어주기
import testd4 as module

# '.' 으로 내부로 접근
print(module.number)
module.print_number()
module.plus5()
module.print_number()

# 함수에서 다른 모듈의 변수를 직접 가져와서 쓸 수는 없다.
def func():
    # 안먹힌다!
    # global의 범위는 모듈까지다. 직접 가져와 변경하는 등 불가능.
    global number
    print(number)

#func()
# %%
# from... import... 전체가 아니라 일부가 필요할 때 쓰는 문법
# 사용하는 이유:
# 엄청 큰 모듈을 가져와서 쓰는 경우에 통째로 가져오는 것보다 효율과 가독성이 좋아짐
# 둘 다 쓰지만 from을 조금 더 자주 쓰게될 것
from testd4 import print_number, plus5

print_number()
plus5()
# 정상 호출됨

# %%

# https://random-data-api.com/api/v2/users
# https://random-data-api.com/
# -> 서버의 주소
# api/v2/users
# -> users 정보들을 요청하는 상세 주소

# pprint (딕셔너리의 가독성을 높혀주는 내장함수)
# from pprint import pprint

# if는 false, None, 0일 때 통과 불가능

#%%
# 조건문, 반복문
# if <조건>:
#    조건문이 만족할 때 실행할 코드
#    == 조건문 결과가 True 일 때

num = 1
# num이 홀수일 때만 출력

print(num % 2 == 1) # True
if num % 2 == 1:
    print(num)

# 조건이 여러가지 일 때
# num 값이 홀수라면 "홀수" 출력
# num 값이 짝수라면 "짝수" 출력
# num 값이 0이라면 "0" 출력
num = 10

if num % 2 == 1: # 조건 1이 True 라면
    print('홀수')

elif num == 0: # 조건 1은 False이고, 조건2 가 True라면
    print('0')

elif num % 2 == 0:
    print('짝수')
# elif : 한 번이라도 True를 만나면, 아래 조건문은 비교 X
#       -> 효율적인 코드를 구현 가능
#       -> 따라서 많이 걸러지는 조건일 수록 if 대신 elif를 사용하는게 좋다
# else
# 남은 조건이 한 가지이다 -> else 사용하는게 버그가 가장 적음. 하지만 막 쓰면 안된다!
#                       -> "남은 조건이 없는가 ?" 잘 생각해야함
#                          ex. 소수가 들어오면 어떡하지? 모르겠으면 -> elif

#%%
# 기본적인 반복문
# for
# - 반복 횟수가 정해져 있을 때 사용

# while
# - 특정 조건이 만족될 때까지 반복

# break: 반복을 중간에 중단
# contine: 반복 중에 코드 일부를 건너뛰게 하기 위해
# pass: 아무것도 하지 않는다

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1, 3, 5, 7 만 출력하도록 반복문으로 구성
# 반복문을 돌리며 숫자가 홀수라면 출력, 8을 만나면 반복문 종료
for num in numbers: # 여기의 num은 numbers에서 값을 "복사"하여 만든 "새로운 변수"
                    # 여기의 num은 해당 for문에서만 사용되는 지역 변수
    # 여기에 아래 코드가 있으면 그 아래 코드를 전부 무시하고 반복한다! (오류나지 않음)
    # continue
    
    # 여기에 아래 코드가 있어도 원본 배열은 바뀌지 않는다
    # num = 10
    
    if num == 8:
        break
    # break를 만나면 반복문 탈출

    # 1. 숫자가 홀수라면 출력해라 (조건문에 만족하면 출력해라)
    # if num % 2 == 1:
    #     print(num)

    # 1-1. 숫자가 홀수가 아니라면 넘어가라 (조건문에 만족하지 않으면 넘어가라)
    # 조건이 많고 복잡할 때 아닌 경우를 하나씩 없앨 수 있다.
    # -> 코드 가독성이 많이 올라간다.
    if num % 2 == 0:
        continue
    
    print(num)



# %%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1, 3, 5, 7 만 출력하도록 반복문으로 구성
# 반복문을 돌리며 숫자가 홀수라면 출력, 8을 만나면 반복문 종료

idx = -1
while True: # 무한 루프에 주의하자!
    idx += 1
    if numbers[idx] == 8:
        break
    if numbers[idx] % 2 == 0:
        continue

    print(numbers[idx], end=' ')

# %%
# list comprihension
numbers = [1, 2, 3, 4, 5]

# 각 숫자에 +5 한 값들을 저장해보자.
# [표현식 for 변수 in 배열]
new_numbers = [num + 5 for num in numbers]
print(new_numbers)

# 조건문을 활용하는 방법
# 짝수만 담기
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# 리스트 2개 -> 모든 조합 찾기
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
comb = [(x, y) for x in list1 for y in list2]
print(comb)
#%%
# 가장 많이 활용되는 list comprihension 예시
# 이차원 리스트 입력
# 3 4 1 2
# 2 1 4 5
# 1 1 1 2
# 2 3 3 4
# 1 1 1 0
li = [list(map(int, input().split())) for _ in range(5)]
print(li)

# %%
# isinstance 알아보기