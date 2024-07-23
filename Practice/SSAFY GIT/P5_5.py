## 1468.메서드를 활용한 중복 요소 제거 lv2

# 아래 함수를 수정하시오.
def remove_duplicates(arr):
    set_lst = set(arr)
    new_lst = list(set_lst)
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)


####################################
# 아래 함수를 수정하시오.
def remove_duplicates():
    new_lst = []
    pass

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
