# 입력 관련
# 문자열 기본 입력
# 표준입출력(standard input/output)
# 1. 기본적인 문자열 입력
# input: 표준 입력 / print: 표준 출력
#word = input()
#print(word)

# 2. 문자열 -> 리스트로 바꾸기
# abc 입력 -> ['a', 'b', 'c']
# 문자열 수정 시 많이 사용된다.
# 문제점 : 공백처리가 어렵다.
#word_list = list(input())
#print(word_list)

# 3. 양쪽 공백 제거 .strip() 사용빈도 높음
#word_strip = list(input().strip())
#print(word_strip)

# 4. 모든 공백 제거 (공백으로 문자열을 구분하는 방법)
# ab c d -> ['ab', 'c', 'd']
# .split() : 자동으로 리스트로 만들어준다.
#word_split = input().split()
#print(word_split)

# 5. 숫자를 리스트로 입력받기
# 12345 -> [1, 2, 3, 4, 5]
# numbers = list(input())
# print(numbers)
# 위처럼 하면 문자열로 들어감
# numbers = list(map(int, input()))
# print(numbers)
# map을 단일로 사용하면 데이터를 보여주지 않음(약속)
# 문제점 : 공백을 입력하면 버그발생. 공백은 int로 바꿀 수 없음

# 6. 공백을 포함한 숫자
# 1 2 3 4 5 -> [1, 2, 3, 4, 5]
# numbers = list(map(int, input().split()))
# print(numbers)

#-----------------------------
# 리스트의 활용
# 주어진 리스트
# 하드 코딩 한다 / 되어있다: 사용자 입력이 아니라, 코드 상에 데이터가 작성되어있다.
#numbers = [10, 20, 30]
#numbers2 = [40, 50, 60]

# [10, 20 , 30, 40, 50, 60]
# + : 더하기 연산 / 병합 연산
#print(numbers+numbers2)
# 뺄셈, 나눗셈은 리스트끼리 불가능
# 리스트에서 곱하기 연산자 = 여러번 반복 할 때 사용 (숫자만 가능)
#print(numbers * 3)

# slicing 연습
#numbers = [10, 20, 30, 40, 50]
#[40, 50]
#print(numbers[3:])
#[10, 20, 30, 40]
#print(numbers[:4])
#[10, 30, 50] (짝수 번 째 인덱스)
#print(numbers[::2])
#[20, 40] (홀수 번 째 인덱스)
#print(numbers[1::2])
#[20, 30, 40]
#print(numbers[1:4])

# 데이터 바꾸기
##x, y = 10, 20 #괄호 없으면 내부적으로 1. tuple로 변경 / 2. unpack
# x, y = 10, 20 ,30 이라고 하면 unpack 오류 발생
# ValueError: too many values to unpack (expected 2)
#print(x)
#print(y)

##x, y = y, x # x, y에다 각각 y의 값, x의 값을 저장해라.
# 다른 언어는 아래와 같이 임시값을 이용하여 복잡하게 한다.
# tmp = x
# x = y
# y = tmp
# 파이썬은 맨 위와 같이 매우 쉽게 한다



#반복문. 반복되는 코드를 제거하기 위해 사용
##numbers = [1, 2, 3, 4]
# 하나하나의 요소를 출력할거야
##print(numbers[0], end = '')
##print(numbers[1], end = '')
##print(numbers[2], end = '')
##print(numbers[3])

# for
# 요소를 반복하고 싶을 때 아래와 같이 작성
##for num in numbers:
    # print(num, end='')
    ##num += 2
    ##print(numbers)

# 리스트를 반복할 때, 인덱스 값으로 쓰고싶어.
# 리스트의 길이만큼 반복하면서, index를 사용
##for idx in range(len(numbers)):
    ##print(numbers[idx], end = '')

# while
# TODO: 조건문을 배우고 나서 학습 예정

# ------------

# 리스트가 아닌 딕셔너리를 사용하는 경우
# 1. index 값이 너무 크게 저장돼야 하는 경우
# - ex) 1 ~ 1억 사이의 숫자 10개
# - 리스트로 구현하면 [0] * 1억
#                        -> 메모리 차지를 너무 많이 한다
# - 딕셔너리로 구현하면 10개면 된다.

# 2. 들어올 수 있는 데이터가 문자라면?
#       or 어떤 데이터가 들어올지 모를 때

##bucket = {
    ##'a' : 1,
    ##'b' : 2,
##}

##for data in bucket:
        ##print(data)

# .items() : key, value 를 모두 반복하고 싶을 때 사용
##for key, value in bucket.items():
     ##print(key, value)

#------------------
#swea 솔빙클럽 예제 - 리스트 기초 - 숫자 합 구하기
# 하드코딩
##arr = [3, 10, 4, -2, 5, 6, 9, 10, 30, 5]

# 테스트 케이스 횟수(숫자)
##T = int(input())

##for test_case in range(1, T+1):
     #사용자의 숫자 입력 -> 숫자 리스트 변환
    ##indexes = list(map(int, input().split()))

    ##result = 0
     # 1. numbers 안에서 "하나 씩" 숫자를 가져온다
     #    -> 반복해서 하나하나 가져온다.
    ##for idx in indexes:
     # [반복문 안] 2. 하드코딩된 배열의 숫자를 가져옴
     #            3. 합하기
        ##result = result + arr[idx]
     # 4. 합계를 출력하기
     #  - #test_case 번호 + 결과(result)
    ##print(f'#{test_case} {result}')
     

#------------------
#swea 솔빙클럽 예제 - 리스트 기초 - 문자열 뒤집기
# 테스트 케이스 횟수(숫자)
##T = int(input())

##for test_case in range(1, T+1):
    # 1. 사용자의 입력(문자열)
    # - txt 파일에서 문자열 끝에 공백이 있을 수 있다.
    # - 줄바꿈(개행)이 공백으로 판단되어 오답처리될 수 있다.
    # - 따라서 strip이나 split을 사용 (일종의 버그를 고려해야하는 억까 문제)
    ##word = input().strip()
    # 2. 뒤집어서 출력
    ##print(f'#{test_case} {word[::-1]}')


#--------------------
#swea 솔빙클럽 예제 -  set 기초 - 교집합, 합집합, 차집합
T = int(input())

for tc in range(1, T+1):
         # 1 2 3 4 5
         # 1. 공백으로 구분되어 있으므로 input().split()
         # 2. 숫자이므로 map(int,)
         # 3. 중복을 제거해야 하므로 set
         #input1 = input().split()
         #input1_number =  map(int, iniput1)
         #input1_set = set(input1_number)
         # 위의 세 줄을 한 줄로 하면
         set1 = set(map(int, input().split()))

         # set
         # 1. 중복을 제거하기 위해 사용
         # 2. 정렬이 안 되어있다. (주의)
         set2 = set(map(int, input().split()))
         
         # 비트연산자 &(and) |(or)
         intersection = set1 & set2
         union = set1 | set2
         difference = set1 - set2
         
         # sorted: 정렬하는 기능. 리스트로 출력
         sorted_intersection = sorted(intersection)
         print(f'#{tc} Intersection: ', end='')
         for num in sorted_intersection:
              print(num, end=' ')
         print()#개행 추가라고 보면 됨

         sorted_union = sorted(union)
         print(f'#{tc} Union: ', end='')
         for num in sorted_union:
              print(num, end=' ')
         print()

         sorted_difference = sorted(difference)
         print(f'#{tc} Difference: ', end='')
         for num in sorted_difference:
              print(num, end=' ')
         print()

#-----------------
# sorted 파트 짧게 (강사님 풀이)
    #print(f"#{tc} Intersection: {' '.join(map(str, sorted(intersection)))}")
    #print(f"#{tc} Union: {' '.join(map(str, sorted(union)))}")
    #print(f"#{tc} Difference: {' '.join(map(str, sorted(difference)))}")



