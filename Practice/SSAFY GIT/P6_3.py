## 3000. 딕셔너리 메서드 2 lv3
#%%
data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

for item in data:
    for key in key_list:
        value = item.get(key, 'unknown')
        # get 메서드를 사용하여 키의 값을 가져오고
        #  키가 없으면 'unknown'을 반환합니다.
        item.setdefault(key, 'unknown')
        # setdefault 메서드를 사용하여
        # 키가 없을 때 'unknown'을 할당합니다.
        print(f'{key} 은/는 {value}입니다.')
    print()


#%%
data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# data를 순회하여 얻은 dict를 key_list를 순회하여 얻은 값에 따라 아래 조건을 만족하는 코드를 작성하시오.
#  만약 순회중인 dict에 key_list로 얻은 key가 없다면,
#   해당 key에 'unknown' 문자열을 할당한다.
#   get 메서드와 setdefault 메서드를 활용한다.
#  모든 상황에 대해 '{key} 은/는 {value}입니다.'를 출력한다.