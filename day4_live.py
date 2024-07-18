#%%
#@ import from 차이설명 다시 보기

# requests 외부 패키지 설치 예시 파트 주석
# request는 global에 설치됨 (전역 공간)
# 실제로는 전역 공간에 설치를 잘 하지 않음
# 동일 환경의 다른 프로젝트와 충돌이 날 수 있기 때문

#%%
#제어문

#조건문
# if / elif / else
# if 단독은 사용될 수 있으나 elif, else 는 단독사용 불가

#반복문
# 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
# == 조건식이 거짓(False)가 될 때 까지 반복
# 따라서 while문은 무한으로 반복될 수 있음

# #- `for`
#     - 반복 횟수가 명확하게 정해져 있는 경우에 유용
#     - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때 

# - `while`
#     - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
#     - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

# comprehesion의 목적: 리스트 생성하기
# for문을 짧게 만드는게 목적이 아님!
# 남용하지말자
# 가독성은 사용하지 않는게 더 좋음

#enumerate
#enumerate(iterable, start=0)
#                       -> 기본 인자
# 인덱스와 요소를 한 번에 뽑아낼 수 있다!
# 자주 사용하므로 익숙해지기

#---------------------------------------------
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
