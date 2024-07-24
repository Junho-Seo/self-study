## 2988. 함수 연습하기 - 기초 lv1
#%%
def my_multi(number_1, number_2):
    mult = number_1*number_2
    return mult

result_1 = my_multi(2, 3)
print(result_1)
# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.


def is_negative(number):
    if number <= 0:
        isneg = 'True'
    else:
        isneg = 'False'
    return isneg

result_2 = is_negative(3)
print(result_2)
# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.


def default_arg_func(default='기본 값'):
    return default

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')

print(result_3)
print(result_4)
#%%
def my_multi(number_1, number_2):
    return 
# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.


def is_negative(number):
    return
#
# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.


def default_arg_func(default):
    return

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')

