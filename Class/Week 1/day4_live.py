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
