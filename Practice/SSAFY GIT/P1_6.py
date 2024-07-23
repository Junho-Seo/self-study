## 1435. 반짝 반짝 작은 별 lv3

#%%
twinkle = '반짝 반짝'
to_from = '에서도'
star = '작은 별'
beauty = '아름답게 비치네'
east = '동쪽 하늘'
west = '서쪽 하늘'

print(f'{twinkle} {star} {beauty}')
print(f'{east}{to_from} {west}{to_from}')
print(f'{twinkle} {star} {beauty}')

# %%
twinkle = '반짝 반짝'
to_from = '에서도'
star = '작은별'
beauty = '아름답게 비치네'
east = '동쪽 하늘'
west = '서쪽 하늘'

# 첫 번째 방법
print(f'{twinkle} {star} {beauty}\n{east}{to_from} {west}{to_from}\n{twinkle} {star} {beauty}')

# 두 번째 방법
print(f'{twinkle} {star} {beauty}')
print(f'{east}{to_from} {west}{to_from}')
print(f'{twinkle} {star} {beauty}')
