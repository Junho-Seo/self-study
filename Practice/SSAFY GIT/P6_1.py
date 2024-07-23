## 2998. 세트와 딕셔너리 lv1

#%%
my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

for key in my_set:
    value = my_dict.get(key)
    print(value)

var = (1, 2, 3, 'A')
my_dict.update(var='변수로도 키 설정 가능')

print(my_dict)


#%%
my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
