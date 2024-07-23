## 1450. Dict.keys() lv4

#%%
# 아래 함수를 수정하시오.
def get_keys_from_dict(dict):
    keys = dict.keys()
    return list(keys)

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']


#%%
# 아래 함수를 수정하시오.
def get_keys_from_dict():
    pass


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']
