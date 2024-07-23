# 1444. List.pop() List.extend() lv5
# G
#%%
# 주어진 리스트에서 홀수를 모두 제거하고 짝수만을 남긴 리스트를 반환하는 even_elements 함수를 작성하시오.
# 단, extend와  pop을 활용하여 구현한다.
def even_elements(lst):
    pass



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)


#%%
def even_elements(lst):
    even_lst = []
    while lst:
        element = lst.pop()
        if element % 2 == 0:
            even_lst.extend([element])
    even_lst.reverse()  # Reverse the list to maintain the original order
    return even_lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)



#%%
# 아래 함수를 수정하시오.
def even_elements():
    pass


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
