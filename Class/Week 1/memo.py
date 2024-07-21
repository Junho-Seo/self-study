# 아래 함수를 수정하시오.
def add_numbers(num1, num2):
    result = num1 + num2
    return result

num1 = int(input())
num2 = int(input())
sum_result = add_numbers(num1, num2)
print(f'{num1}과 {num2}를 인자로 넘긴 경우,', sum_result)
# 수정한 add_numbers() 함수를 호출하시오.